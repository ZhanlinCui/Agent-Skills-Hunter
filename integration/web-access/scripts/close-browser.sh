#!/usr/bin/env bash
# 优雅关闭 agent-browser Chrome 实例（跨平台）
# 用法：bash close-browser.sh

UTILS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_utils.sh
source "$UTILS_DIR/_utils.sh"

CDP_PORT=9222
PROFILE_DIR="$HOME/.claude/browser-profile"

# 1. CDP Browser.close —— 协议层关闭，跨平台，Chrome 自己正常退出
# 用 Python 发 WebSocket 帧，不依赖外部包
python3 - <<'PYEOF' 2>/dev/null
import json, socket, base64, urllib.request, struct

try:
    data = json.loads(urllib.request.urlopen('http://localhost:9222/json/version', timeout=3).read())
    ws_url = data['webSocketDebuggerUrl']
    path = ws_url[len('ws://localhost:9222'):]

    s = socket.socket()
    s.settimeout(5)
    s.connect(('localhost', 9222))
    key = base64.b64encode(b'claude-web-access!!').decode()
    s.send(f'GET {path} HTTP/1.1\r\nHost: localhost:9222\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n'.encode())
    s.recv(4096)

    msg = json.dumps({"id": 1, "method": "Browser.close"}).encode()
    mask = bytes([0, 0, 0, 0])
    masked = bytes(b ^ mask[i % 4] for i, b in enumerate(msg))
    frame = bytes([0x81, 0x80 | len(msg)]) + mask + masked
    s.send(frame)
    s.close()
    print("Browser closed")
except Exception as e:
    print(f"CDP close failed: {e}", flush=True)
    exit(1)
PYEOF

# 2. 兜底：CDP 失败时按 OS 强制退出
if [ $? -ne 0 ]; then
  case "$(get_os)" in
    macos)
      OUR_PID=$(ps aux | grep "Google Chrome" | grep -- "--user-data-dir=${PROFILE_DIR}" | grep -v grep | awk '{print $2}' | head -1)
      [ -n "$OUR_PID" ] && kill_pid "$OUR_PID" && echo "Browser closed (osascript)"
      ;;
    linux)
      OUR_PID=$(ps aux | grep "google-chrome\|chromium" | grep -- "--user-data-dir=${PROFILE_DIR}" | grep -v grep | awk '{print $2}' | head -1)
      [ -n "$OUR_PID" ] && kill_pid "$OUR_PID" && echo "Browser closed (SIGTERM)"
      ;;
    windows)
      OUR_PID=$(wmic process where "name='chrome.exe'" get commandline,processid 2>/dev/null \
        | grep "browser-profile" | grep -oE '[0-9]+$' | head -1 | tr -d ' \r\n')
      [ -n "$OUR_PID" ] && kill_pid "$OUR_PID" && echo "Browser closed (taskkill)"
      ;;
    *)
      echo "Unknown OS — please close the browser manually"
      ;;
  esac
fi

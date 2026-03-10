#!/usr/bin/env bash
# web-access 共享工具函数，供 ensure-browser.sh 和 close-browser.sh source

# 返回 macos / linux / windows
get_os() {
  case "$(uname -s)" in
    Darwin)              echo "macos" ;;
    Linux)               echo "linux" ;;
    MINGW*|MSYS*|CYGWIN*) echo "windows" ;;
    *)                   echo "linux" ;;
  esac
}

# 跨平台 Chrome 路径探测
find_chrome() {
  # macOS
  local mac_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  [ -f "$mac_path" ] && echo "$mac_path" && return

  # Linux
  for p in \
    "$(command -v google-chrome 2>/dev/null)" \
    "$(command -v google-chrome-stable 2>/dev/null)" \
    "$(command -v chromium 2>/dev/null)" \
    "$(command -v chromium-browser 2>/dev/null)" \
    /usr/bin/google-chrome /usr/bin/google-chrome-stable \
    /usr/bin/chromium /usr/bin/chromium-browser /snap/bin/chromium; do
    [ -f "$p" ] && echo "$p" && return
  done

  # Windows（Git Bash）
  if [ "$(get_os)" = "windows" ]; then
    local local_app programfiles
    local_app=$(cygpath "$LOCALAPPDATA" 2>/dev/null)
    programfiles=$(cygpath "$PROGRAMFILES" 2>/dev/null)
    for p in \
      "$local_app/Google/Chrome/Application/chrome.exe" \
      "$programfiles/Google/Chrome/Application/chrome.exe"; do
      [ -f "$p" ] && echo "$p" && return
    done
  fi

  echo ""
}

# 按 OS 适当关闭进程
kill_pid() {
  local pid=$1
  case "$(get_os)" in
    macos)
      osascript -e "tell application \"System Events\" to tell (first process whose unix id is ${pid}) to quit" 2>/dev/null \
        || kill "$pid" 2>/dev/null
      ;;
    windows)
      taskkill /PID "$pid" /F 2>/dev/null
      ;;
    *)
      kill "$pid" 2>/dev/null
      ;;
  esac
}

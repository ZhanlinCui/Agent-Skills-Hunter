#!/usr/bin/env bash
# 环境探测 - 输出依赖状态供 AI 判断和处理

UTILS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_utils.sh
source "$UTILS_DIR/_utils.sh"

echo "OS:            $(uname -s) $(uname -m)"

CHROME_PATH=$(find_chrome)
echo "chrome:        ${CHROME_PATH:-missing}"
echo "node:          $(command -v node 2>/dev/null && node --version 2>/dev/null || echo 'missing')"
echo "npm:           $(command -v npm 2>/dev/null || echo 'missing')"
echo "agent-browser: $(command -v agent-browser 2>/dev/null || echo 'missing  → npm install -g agent-browser')"

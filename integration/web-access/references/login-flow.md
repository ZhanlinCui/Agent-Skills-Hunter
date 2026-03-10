# 登录态处理详细流程

## 登录检测信号

执行 `snapshot -i` 后，若出现以下任一信号，判定为需要登录：

- 页面含 `input[type=password]`
- 当前 URL 含 `/login`、`/signin`、`/auth`、`/account/login`
- 页面标题含"登录"、"Sign in"、"Log in"、"Login"
- 快照内容出现"请登录"、"未登录"、"登录后查看"等提示文本

## 处理步骤

浏览器始终以 headed（有窗口）模式运行，检测到登录信号后：

1. 告知用户：
   > "已在 Chrome 窗口打开 [网站名]，请完成登录。登录成功后告诉我，我来继续。"

2. 等待用户确认登录完成

3. 继续原来的操作（无需重启浏览器，登录态已写入 profile）

```bash
agent-browser --cdp 9222 open <url>
agent-browser --cdp 9222 snapshot -i
```

## Profile 路径

`~/.claude/browser-profile/`（登录态持久化，下次直接复用）

## 常见问题

**Q: 端口被占用无法启动？**
```bash
lsof -ti:9222 | xargs kill -9
bash ~/.claude/skills/web-access/scripts/ensure-browser.sh
```

**Q: 登录后 cookie 没有持久化？**
- 确保使用了 `--user-data-dir` 参数（ensure-browser.sh 已包含）
- 不要在浏览器关闭前清除 cookies

# Twitter 登录指南

由于当前是命令行环境，无法直接打开可视化浏览器。请按以下步骤完成登录：

## 方法 1：本地登录后上传（推荐）

### 步骤 1：在本地电脑安装 agent-browser

```bash
npm install -g agent-browser
agent-browser install
```

### 步骤 2：登录 Twitter

```bash
# 创建 profile 目录
mkdir -p ~/.agent-browser/main

# 打开 Twitter 登录页（这会打开可视化浏览器）
agent-browser --profile ~/.agent-browser/main open "https://x.com/login"
```

在打开的浏览器中：
1. 输入你的 Twitter 账号密码
2. 完成登录（包括可能的 2FA 验证）
3. 关闭浏览器

### 步骤 3：验证登录状态

```bash
# 测试是否已登录
agent-browser --profile ~/.agent-browser/main open "https://x.com/home"
agent-browser --profile ~/.agent-browser/main snapshot -c
```

应该能看到你的首页时间线，而不是登录页。

### 步骤 4：上传到服务器（如需要）

如果你在本机登录，但要在服务器运行：

```bash
# 压缩 profile 目录
tar czvf twitter-profile.tar.gz ~/.agent-browser/main

# 上传到服务器
scp twitter-profile.tar.gz user@server:~/

# 在服务器解压
tar xzvf twitter-profile.tar.gz -C ~/
```

## 方法 2：使用 Cookie（快捷但不持久）

### 步骤 1：在本地浏览器获取 Cookie

1. 在 Chrome/Firefox 登录 Twitter
2. 打开开发者工具 (F12)
3. 切换到 Application/Storage 标签
4. 复制 cookies

### 步骤 2：导入到 agent-browser

```bash
# 创建 cookie 文件
cat > twitter-cookies.json << 'EOF'
[
  {"name": "auth_token", "value": "你的token", "domain": ".x.com"},
  {"name": "ct0", "value": "你的ct0", "domain": ".x.com"}
]
EOF

# 使用脚本导入（需要 Playwright 脚本）
```

注意：Cookie 方式需要定期更新。

## 方法 3：使用环境变量（自动化）

如果你需要完全自动化：

```bash
# 设置 Twitter 凭据（仅示例，不推荐硬编码）
export TWITTER_USERNAME="your_username"
export TWITTER_PASSWORD="your_password"

# 使用脚本自动登录
```

## 验证登录成功

无论哪种方法，验证是否成功：

```bash
# 获取 Karpathy 的最新推文
agent-browser --profile ~/.agent-browser/main open "https://x.com/karpathy" --timeout 15000
sleep 3
agent-browser --profile ~/.agent-browser/main snapshot -c | grep -A 5 "2026-01"
```

如果看到 2026 年 1 月的推文，说明登录成功。

## 常见问题

**Q: 提示 "daemon already running"？**
```bash
agent-browser close
# 然后重试
```

**Q: Profile 目录在哪里？**
- macOS: `~/.agent-browser/main`
- Linux: `~/.agent-browser/main`
- Windows: `%USERPROFILE%\.agent-browser\main`

**Q: 如何更新登录状态？**
如果登录过期，重复步骤 2 重新登录即可，profile 会更新。

**Q: 多个 Twitter 账号？**
```bash
mkdir -p ~/.agent-browser/twitter-work
mkdir -p ~/.agent-browser/twitter-personal

agent-browser --profile ~/.agent-browser/twitter-work open "https://x.com/login"
# 登录工作账号

agent-browser --profile ~/.agent-browser/twitter-personal open "https://x.com/login"
# 登录个人账号
```

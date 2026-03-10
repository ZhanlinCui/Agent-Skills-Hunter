# Daily News Website Template

终端风格的日报网站模板，用于将 Markdown 日报转换为静态 HTML 网站。

## 特点

- **终端风格设计** - 黑色 header + 白色内容区
- **JetBrains Mono 字体** - 等宽字体显示代码/日期
- **响应式布局** - 适配手机和桌面
- **日期导航** - 快速切换历史日报
- **星级分组** - 五星/四星/值得一看

## 使用方法

### 1. 初始化网站

在 daily-news 工作目录下：

```bash
mkdir -p website/dist
python3 build.py
```

### 2. 部署到 Cloudflare Pages

```bash
cd website
git init
git add -A
git commit -m "Initial commit"
gh repo create daily-news-web --public --source=. --push
```

然后在 Cloudflare Pages 控制台：
- Build command: `python3 build.py`
- Build output: `dist`

### 3. 每日更新

生成新日报后：

```bash
cd website
python3 build.py
git add -A
git commit -m "Add report for $(date +%Y-%m-%d)"
git push origin main
```

Cloudflare Pages 会自动重新部署。

## 文件结构

```
website/
├── build.py          # 构建脚本
├── dist/             # 生成的静态网站
│   ├── index.html    # 首页（最新日报）
│   └── YYYY-MM-DD.html
└── README.md         # 本文件
```

## 自定义

修改 `build.py` 中的样式变量：

```python
:root {{
    --bg-primary: #fafafa;    # 主背景色
    --bg-terminal: #1a1a1a;   # 终端 header 背景
    --accent: #2563eb;        # 主题蓝色
    --star: #f59e0b;          # 星级颜色
}}
```

## 依赖

- Python 3.8+
- 无第三方依赖

## 自动部署

可与 GitHub Actions 配合，实现自动生成日报后自动推送：

```yaml
name: Build and Deploy
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'  # 每天 10:00 (北京时间)

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 build.py
      - uses: actions/deploy-pages@v4
```

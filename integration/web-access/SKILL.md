---
name: web-access
version: 1.1.0
license: MIT
description: |
  所有联网操作必须通过此 skill 处理，包括：搜索、网页抓取、登录后操作、动态页面交互等。
  触发场景：用户要求搜索信息、查看网页内容、访问需要登录的网站、操作网页界面、抓取社交媒体内容（小红书、微博、推特等）、读取动态渲染页面、以及任何需要真实浏览器环境的网络任务。
changelog:
  - version: 1.1.0
    date: 2026-03-10
    changes:
      - 新增"浏览哲学"框架：三个核心判断（我需要什么/够了吗/遇到阻碍怎么办）
      - 社交媒体/内容平台直走浏览器 CDP，跳过 WebFetch
      - 新增视频内容采帧分析能力（seek + screenshot）
      - 完善 already-running 状态处理：必须验证后才能使用
      - 细化 wait 命令使用时机说明
      - 新增 screenshot --annotate 作为 snapshot -i 失效时的升级方案
  - version: 1.0.0
    date: 2025-01-01
    changes:
      - 初始版本
---

# web-access Skill

## 首次安装

用户首次使用时，执行以下流程：

**Step 1：运行环境探测**
```bash
bash ~/.claude/skills/web-access/scripts/check-deps.sh
```

**Step 2：AI 根据输出处理缺失依赖**

探测脚本只报告事实，安装决策由 AI 完成。缺什么装什么，Chrome 缺失时提示用户手动下载（无法自动安装）。

**Step 3：安装完成后，向用户说明以下内容**

> web-access 已就绪。凡是联网的需求直接说就行，我会自动选最合适的方式：
> - 只需要搜索结果 → 直接搜，最快
> - 需要看完整页面 → 抓取页面内容，不启动浏览器
> - 需要登录或动态页面 → 自动启动浏览器，登录一次后持久保存
>
> Windows 用户需要 Git Bash 环境（安装 Git for Windows 即可）。

## 浏览哲学

**像人一样浏览，不像机器人一样执行程序。**

人类浏览网页时不会在开始前列出完整步骤，而是带着目标进入，边看边判断，遇到阻碍就解决，发现内容不够就深入——全程围绕「我要拿到什么」做决策。这个 skill 的所有行为都应遵循这个逻辑。

**三个核心判断：**

**① 我需要什么？** — 任务驱动，先想清楚目标信息的性质，再选最轻且能直达的方式。不要用重型工具做轻量任务，也不要用轻量工具面对它覆盖不到的内容。

**② 够了吗？** — 拿到的信息能完成任务，就是够了。不过度采集，不为了"完整"而浪费代价。大概了解一个视频，几帧就够；理解一篇文章，读文字就够；不需要全页截图去做能用 accessibility tree 完成的事。

**③ 遇到阻碍怎么办？** — 在层内解决，不退回，不打扰用户。弹窗、登录墙、广告、加载失败——像人一样判断这个阻碍是否真的挡住了目标内容：挡住了就处理，没挡住就绕过去继续。只有在确认无法自行解决时才告知用户。

## 信息获取通道选择

- **先评估任务，再选通道**：根据「目标信息的性质、什么工具能直接拿到」决定起点，选最轻且能直达的方案。
- **确保信息的真实性，一手信息优于二手信息**：搜索引擎和聚合平台是信息发现入口。当多次搜索尝试后没有质的改进时，升级到更根本的获取方式：定位一手来源（官网、官方平台、原始页面）。

| 场景 | 通道 |
|------|------|
| 只需搜索摘要或关键词结果，或需要发现信息来源 | **WebSearch** |
| URL 已知，静态公开页面 | **WebFetch** |
| 社交媒体、内容平台（微信公众号、微博、小红书、X/Twitter 等） | **浏览器 CDP**（直接，跳过 WebFetch） |
| 需要动态内容、登录态、交互操作，或需要像人一样在浏览器内自由导航探索 | **浏览器 CDP** |

浏览器 CDP 不要求 URL 已知——可从任意入口出发，通过页面内搜索、点击、跳转等方式找到目标内容。

WebFetch 请求时加 header `Accept: text/markdown, text/html`，支持该协议的网站直接返回 Markdown，省约 80% token。失败（空内容 / 403 / JS 渲染）时升级到浏览器层。


**降级禁止**：进入更重的通道后，不得回头用轻量工具完成同一目标——等同于重走已知不通的路。浏览器层遇到阻碍应在层内解决（如处理登录），而不是绕回。唯一例外：浏览器操作中衍生的新子目标，可重新选择通道。

进入浏览器层后，区分任务性质：

- **操作型**（导航、填表、点击）：用 accessibility tree 感知界面，无法识别时才截图辅助
- **内容型**（读帖子、看资讯、分析页面）：accessibility tree 读文字结构，同时判断图片是否承载核心信息——是则提取图片 URL 定向读取

**图片判断**：社交媒体、图文博客、截图类内容，默认图片有价值，主动去取；工具类、导航类页面，默认 accessibility tree 够用。

## 浏览器 CDP 模式

### 启动

```bash
bash ~/.claude/skills/web-access/scripts/ensure-browser.sh
```

- `Browser ready on port 9222` → 脚本自己启动的，状态可信，直接用（任务结束后关闭）
- `already running` → 检测到残留进程，状态不可信，必须验证：运行 `agent-browser --cdp 9222 open about:blank`，成功则可用；失败则执行 close 后重新 ensure（任务结束后不关闭）
- `ERROR` 或 agent-browser 无响应 → 执行 `bash ~/.claude/skills/web-access/scripts/close-browser.sh` 后重新运行

> **⚠️ 严禁降级**：只用 agent-browser CDP 模式，不切换到其他浏览器工具。Playwright MCP 底层同为 playwright-core + launchPersistentContext，能力等效，但 profile 路径不同——切换会丢失已有登录态，需重新登录。

### 常用命令

```bash
agent-browser --cdp 9222 open <url>           # 打开页面
agent-browser --cdp 9222 snapshot -i          # 可交互元素（操作用）
agent-browser --cdp 9222 snapshot             # 完整无障碍树（读文字用）
agent-browser --cdp 9222 click @ref-123       # 点击元素
agent-browser --cdp 9222 fill @ref-123 "内容" # 填写输入框
agent-browser --cdp 9222 wait load networkidle  # 仅用于 click/fill 触发导航后；open 已内置等待，勿在 open 后使用
agent-browser --cdp 9222 scroll down 3000     # 触发懒加载
agent-browser --cdp 9222 screenshot /tmp/x.png
agent-browser --cdp 9222 screenshot --annotate      # snapshot -i ref 失效时的升级方案，见 references/commands.md
agent-browser --cdp 9222 eval "<js>"          # 执行 JS，用于提取 DOM 信息
```

### 图片提取

判断内容在图片里时，用 `eval` 从 DOM 直接拿图片 URL，再定向打开截图读取——比全页截图精准得多。

需要知道的两个技术细节：
- **懒加载**：未进入视口的图片 `naturalWidth` 为 0，eval 前先 scroll 到底才能拿到完整列表
- **过滤噪声**：`naturalWidth > 200` 排除图标和头像，留下内容图

```bash
agent-browser --cdp 9222 scroll down 3000
agent-browser --cdp 9222 eval "JSON.stringify(Array.from(document.querySelectorAll('img')).map((img,i)=>({i,src:img.src,w:img.naturalWidth,h:img.naturalHeight})).filter(x=>x.w>200))"
# 对每张目标图片：
agent-browser --cdp 9222 open <img_url>
agent-browser --cdp 9222 screenshot /tmp/img_n.png
# 用 Read tool 读取截图内容
```

### 视频内容获取

CDP headed 模式下浏览器真实渲染，截图可捕获当前视频帧。核心能力：**seek 到任意时间点截图**，可对视频内容进行离散采样分析。

```bash
# 获取总时长，制定采样计划
agent-browser --cdp 9222 eval "document.querySelector('video').duration"
# seek + 播放 + 截图
agent-browser --cdp 9222 eval "var v=document.querySelector('video'); v.currentTime=60; v.play()"
sleep 2
agent-browser --cdp 9222 screenshot /tmp/frame.png
# 全屏截图画面更清晰
agent-browser --cdp 9222 eval "document.querySelector('video').requestFullscreen()"
```

采帧粒度（仅供参考，具体视频具体分析：大概了解 → 30-60s 间隔；理解叙事 → 10s；精细分析 → 1-2s）由任务需求自行判断，无需用户指定。

### 登录判断

登录判断的核心问题只有一个：**目标内容拿到了吗？**

打开页面后，先尝试获取目标内容，持续执行。在此过程中，结合两方面信息做判断：

1. **领域知识**：对该网站的了解——X/Twitter 的最新时间线、小红书的私密内容、微博的完整评论等，这类内容通常需要登录才能获取完整数据
2. **页面实际反馈**：内容是否符合预期？是降级版（如热门帖代替最新帖）？是否有明显缺失？

即使页面显示了登录提示，只要目标内容已经拿到，就不需要打扰用户登录。

只有当确认**目标内容无法获取**时，才推断：登录是否能解决这个问题？若推断成立，告知用户：
> "当前页面在未登录状态下无法获取[具体内容]，请在已打开的 Chrome 窗口中登录 [网站名]，完成后告诉我继续。"

登录完成后无需重启浏览器，直接继续原任务。

### 任务结束

ensure-browser.sh 返回 `Browser ready`（本次启动）→ 关闭浏览器（**必须用此脚本，勿直接 kill，否则会留下崩溃窗口**）：
```bash
bash ~/.claude/skills/web-access/scripts/close-browser.sh
```

## 特殊任务规则

### 核实任务

核实的目标是**一手来源**，而非更多的二手报道——多个媒体引用同一个错误会造成循环印证假象。

搜索用于**定位**来源，不用于**证明**真伪。找到来源后，直接访问读取原文。

| 信息类型 | 一手来源 |
|----------|---------|
| 政策/法规 | 发布机构官网 |
| 企业公告 | 公司官方新闻页 |
| 学术声明 | 原始论文/机构官网 |

**找不到官网时**：权威媒体的原创报道（非转载）可作为次级依据，但需向用户说明："未找到官方原文，以下核实来自[媒体名]报道，存在转述误差可能。"

### 工具能力边界理解

对任何工具（MCP、CLI、库）的能力有疑问时，**如果没有足够的知识把握，先查官方文档，如无足够文档介绍，可考虑查看源码，再作判断**，不猜测、不把不确定性转移给用户。

## References 索引

| 文件 | 何时加载 |
|------|---------|
| `references/commands.md` | 需要不常用命令时（drag、storage、pdf 等） |
| `references/login-flow.md` | 需要了解登录流程细节时 |

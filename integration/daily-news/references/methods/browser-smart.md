# 浏览器获取（Browser MCP）

使用 Browser MCP 获取页面内容，复用用户浏览器的登录态。

## 使用方式

```yaml
extends: browser-smart
detail_method: browser
```

## 前置条件

**必须**先完成 Browser MCP 配置：

1. **安装 Chrome 扩展**: https://chromewebstore.google.com/detail/bjfgambnhccakkhmkepdoekmckoijdlc
2. **连接扩展**: 点击 Chrome 工具栏的 Browser MCP 图标 → Connect
3. **配置 Claude Code**: 确保 `~/.claude.json` 中有 browsermcp 配置

## 执行流程

### 1. 检查连接状态

```
调用 mcp__browsermcp__browser_snapshot 测试连接
```

### 2. 打开目标页面

```
调用 mcp__browsermcp__browser_navigate
参数: {"url": "<source_url>"}
```

### 3. 等待页面加载

```
调用 mcp__browsermcp__browser_wait
参数: {"time": 3}
```

或等待特定文本出现：

```
调用 mcp__browsermcp__browser_wait_for
参数: {"text": "文章标题", "timeout": 10000}
```

### 4. 获取页面快照

```
调用 mcp__browsermcp__browser_snapshot
```

快照包含 accessibility tree，AI 可直接解析内容。

### 5. 提取文章列表

从 snapshot 中识别文章/帖子，输出 JSON。

## 输出格式

```json
[
  {"title": "...", "url": "https://...", "published_at": "YYYY-MM-DD"}
]
```

## 高级用法

### 滚动加载更多内容

```
调用 mcp__browsermcp__browser_evaluate_script
参数: {"function": "() => { window.scrollTo(0, document.body.scrollHeight); }"}
```

等待加载：
```
调用 mcp__browsermcp__browser_wait
参数: {"time": 2}
```

再次获取快照：
```
调用 mcp__browsermcp__browser_snapshot
```

### 点击元素

1. 先获取 snapshot 找到元素 ref
2. 点击：
```
调用 mcp__browsermcp__browser_click
参数: {"element": "加载更多按钮", "ref": "<ref_from_snapshot>"}
```

### 复用登录态

Browser MCP 直接使用用户浏览器的登录态，无需额外配置。只要浏览器已登录，就能访问需要登录的内容。

## 适用场景

- JS 渲染页面
- 需要登录的内容（Twitter/X、LinkedIn 等）
- 需要滚动加载的内容
- WebFetch 无法获取的页面
- 需要简单交互的页面（点击加载更多）

## 故障排除

**MCP 未连接？**
```
错误: No connection to browser extension
```
解决: 安装 Chrome 扩展并点击 Connect 按钮

**页面加载超时？**
增加等待时间或检查网络

**Snapshot 为空？**
可能是页面还在加载，增加等待时间后重试

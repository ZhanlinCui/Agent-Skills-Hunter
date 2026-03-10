# agent-browser 完整命令参考

> 所有命令格式：`agent-browser --cdp 9222 <command>`

## 导航类

```bash
agent-browser --cdp 9222 open <url>          # 打开 URL
agent-browser --cdp 9222 back                # 返回上一页
agent-browser --cdp 9222 forward             # 前进
agent-browser --cdp 9222 reload              # 刷新
agent-browser --cdp 9222 reload --hard       # 强制刷新（清缓存）
```

## 快照类（核心：获取页面状态）

```bash
agent-browser --cdp 9222 snapshot           # 基础快照（文本+结构）
agent-browser --cdp 9222 snapshot -i        # 带交互元素（含 ref 编号，用于后续操作）
agent-browser --cdp 9222 snapshot -c        # 带坐标信息
agent-browser --cdp 9222 snapshot -d        # 深度快照（展开折叠内容）
agent-browser --cdp 9222 snapshot -i -d     # 组合：交互元素 + 深度
```

## 交互类

```bash
agent-browser --cdp 9222 click @ref-123             # 点击元素（ref 来自 snapshot -i）
agent-browser --cdp 9222 click "Submit"              # 点击文本匹配的元素
agent-browser --cdp 9222 fill @ref-123 "text"       # 填写输入框
agent-browser --cdp 9222 type "hello world"          # 在当前焦点处输入
agent-browser --cdp 9222 press Enter                 # 按键（Enter/Tab/Escape/ArrowDown 等）
agent-browser --cdp 9222 select @ref-123 "option"   # 选择下拉选项
agent-browser --cdp 9222 drag @ref-from @ref-to     # 拖拽
agent-browser --cdp 9222 hover @ref-123              # 悬停（触发 tooltip/下拉菜单）
agent-browser --cdp 9222 scroll @ref-123 down 300   # 滚动元素
agent-browser --cdp 9222 scroll window down 500     # 滚动页面
```

## 信息获取

```bash
agent-browser --cdp 9222 get text @ref-123          # 获取元素文本
agent-browser --cdp 9222 get html @ref-123          # 获取元素 HTML
agent-browser --cdp 9222 get attr @ref-123 href     # 获取属性值
agent-browser --cdp 9222 get url                    # 获取当前页面 URL
agent-browser --cdp 9222 get title                  # 获取页面标题
```

## 等待机制

```bash
agent-browser --cdp 9222 wait element @ref-123             # 等待元素出现
agent-browser --cdp 9222 wait 2000                          # 等待 2 秒
agent-browser --cdp 9222 wait element --text "加载完成"     # 等待含特定文本的元素
agent-browser --cdp 9222 wait load networkidle              # 等待网络空闲
agent-browser --cdp 9222 wait element @ref-123 --hidden     # 等待元素消失
```

## 语义定位器（snapshot -i ref 的替代方案）

```bash
agent-browser --cdp 9222 find role button "登录"     # 按 ARIA role + 文本找元素
agent-browser --cdp 9222 find text "提交"            # 按文本内容找元素
agent-browser --cdp 9222 find label "用户名"         # 按关联 label 找输入框
```

## 截图与导出

```bash
agent-browser --cdp 9222 screenshot                 # 截图（viewport）
agent-browser --cdp 9222 screenshot --full          # 截图（全页面）
agent-browser --cdp 9222 screenshot -o out.png      # 保存到文件
agent-browser --cdp 9222 screenshot --annotate      # 注释截图（见下方说明）
agent-browser --cdp 9222 pdf -o page.pdf            # 导出 PDF
```

### annotate 模式

`--annotate` 在截图上叠加编号标签，同时输出对应的 ref 列表，ref 与 `snapshot -i` 共享同一套体系（`@e1`、`@e2`…），截图后立即可用于操作：

```bash
agent-browser --cdp 9222 screenshot --annotate
# 输出：[1] @e1 button "Submit"  [2] @e2 link "Home" ...
agent-browser --cdp 9222 click @e2   # 直接使用
```

**默认用 `snapshot -i`**。accessibility tree 依赖元素有语义标签（role、name、label），当页面元素缺乏这些语义信息时，snapshot 给出的 ref 可能无法命中或根本不出现。此时用 `--annotate`，它直接从视觉层枚举可见元素，能覆盖 accessibility tree 看不到的情况：

- 纯图标按钮（无文字、无 aria-label）
- canvas / WebGL 等自定义渲染元素
- 动态注入、框架渲染导致 accessibility tree 结构异常

## Cookies & Storage

```bash
agent-browser --cdp 9222 cookies                    # 列出所有 cookies
agent-browser --cdp 9222 cookies --domain x.com     # 过滤域名
agent-browser --cdp 9222 storage local              # 查看 localStorage
agent-browser --cdp 9222 storage session            # 查看 sessionStorage
```

## 常用组合模式

```bash
# 登录表单填写
agent-browser --cdp 9222 snapshot -i
agent-browser --cdp 9222 fill @ref-username "user@example.com"
agent-browser --cdp 9222 fill @ref-password "password"
agent-browser --cdp 9222 click @ref-submit
agent-browser --cdp 9222 wait load networkidle

# 翻页操作
agent-browser --cdp 9222 snapshot -i
agent-browser --cdp 9222 click @ref-next-page
agent-browser --cdp 9222 wait load networkidle
agent-browser --cdp 9222 snapshot
```

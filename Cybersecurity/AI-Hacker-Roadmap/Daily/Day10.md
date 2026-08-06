# Day 10 — XSS 与输出编码基础

## Mission

使用本地教学页面比较 `innerHTML` 与 `textContent`，理解同一个输入为什么会被当成 HTML 或普通文字。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：30–45 分钟

## 安全范围

只使用：

```text
Labs/XSSBasics/index.html
```

今天只输入普通文字和无害的 `<b>hello</b>`，不输入脚本。

## 今天需要理解

```text
innerHTML   把字符串当作 HTML 解析
textContent 把字符串当作普通文字显示
```

问题不只取决于输入是什么，还取决于输出放在什么上下文、使用什么 API。

## Part 1 — 启动本地页面

### Step 1 — 打开终端

从仓库根目录运行：

```bash
cd Cybersecurity/AI-Hacker-Roadmap/Labs/XSSBasics
python3 -m http.server 8000
```

看到 `Serving HTTP` 后保持终端运行。

如果 8000 被占用，改用 8010，并同步修改浏览器 URL。

### Step 2 — 打开页面

在浏览器访问：

```text
http://127.0.0.1:8000/
```

页面应显示：

```text
输入框
Render 按钮
innerHTML output
textContent output
```

## Part 2 — 普通文字基准

### Step 3 — 输入 hello

把输入框改成：

```text
hello
```

点击 `Render`。

预期：

```text
innerHTML output：hello
textContent output：hello
```

普通文字没有 HTML 特殊结构，因此两处看起来一样。

## Part 3 — HTML 文字对照

### Step 4 — 输入无害标签

输入：

```html
<b>hello</b>
```

点击 `Render`。

预期：

```text
innerHTML output：显示粗体 hello
textContent output：原样显示 <b>hello</b>
```

如果两处都显示普通文字，确认点击了 Render，并确认打开的是本项目页面。

## Part 4 — 查看代码证据

### Step 5 — 在 VS Code 打开源码

打开：

```text
Labs/XSSBasics/index.html
```

找到：

```javascript
htmlOutput.innerHTML = input.value;
textOutput.textContent = input.value;
```

逐行解释：

```text
input.value            用户输入
innerHTML              作为 HTML 结构解析
textContent            作为文字写入
```

### Step 6 — 建立安全理解

今天观察到：

```text
相同输入
→ 进入不同输出 API
→ 浏览器解释方式不同
```

安全输出通常要根据上下文正确编码，并优先使用不会把不可信文字当成 HTML 的 API。

## Part 5 — 停止服务

回到终端按：

```text
Control + C
```

确认终端回到命令提示符。

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| Connection refused | 本地服务没启动 | 重新运行 http.server |
| 404 | 终端不在 XSSBasics | 检查 cd 路径 |
| 点击后没变化 | 没点 Render 或浏览器缓存 | 再点击或刷新页面 |
| 两处都粗体 | 看错输出区域 | 对照两个标题 |
| 想输入脚本 | 超出 Day 10 | 今天只用 `<b>hello</b>` |

## 成功标准

- [x] 本地页面正常打开
- [x] hello 在两处都显示
- [x] `<b>hello</b>` 在两处表现不同
- [x] 找到 innerHTML 代码行
- [x] 找到 textContent 代码行
- [x] 能解释输出上下文
- [x] 已停止本地服务器

## 操作记录

```text
普通文字输入：hello

innerHTML 普通文字结果：hello

textContent 普通文字结果：hello

HTML 输入：<b>hello</b>

innerHTML HTML 结果：浏览器把 `<b>` 解析为 HTML 标签，显示粗体 hello

textContent HTML 结果：浏览器把输入当作普通文字，原样显示 `<b>hello</b>`

造成差别的两行代码：
htmlOutput.innerHTML = input.value;
textOutput.textContent = input.value;

我对输出编码的理解：同一个输入是否安全，取决于它被放入的输出上下文。innerHTML 会让浏览器把字符串解析为 HTML；textContent 则把它当作普通文字。处理不可信文字时，应优先使用 textContent；如果必须输出到 HTML 等其他上下文，则需要使用与该上下文匹配的安全处理方法。

我遇到的问题：没有
```

## 思考题

```text
1. `<b>` 为什么在 innerHTML 区域没有原样显示？
答：innerHTML 会把输入交给 HTML 解析器。浏览器因此把 `<b>` 和 `</b>` 识别为标签，并把中间的 hello 渲染成粗体，而不是显示标签本身。

2. textContent 为什么会显示尖括号？
答：textContent 创建的是文字内容，不会调用 HTML 解析器来解释输入。因此 `<` 和 `>` 只是普通字符，会和其他文字一起显示。

3. 输入验证和输出编码分别解决什么问题？
答：输入验证用来检查数据是否符合业务规则，例如类型、长度和允许范围。输出编码则根据输出上下文处理特殊字符，防止数据被当成 HTML 或代码解释。输入验证不能代替输出编码。
```

## 今日一句话总结

```text
今天我学会了：同一个输入通过 innerHTML 和 textContent 输出时会被浏览器以不同方式解释，处理不可信文字时应优先使用 textContent。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 10: learn XSS output contexts"
```

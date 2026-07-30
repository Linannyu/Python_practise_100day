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

- [ ] 本地页面正常打开
- [ ] hello 在两处都显示
- [ ] `<b>hello</b>` 在两处表现不同
- [ ] 找到 innerHTML 代码行
- [ ] 找到 textContent 代码行
- [ ] 能解释输出上下文
- [ ] 已停止本地服务器

## 操作记录

```text
普通文字输入：

innerHTML 普通文字结果：

textContent 普通文字结果：

HTML 输入：

innerHTML HTML 结果：

textContent HTML 结果：

造成差别的两行代码：

我对输出编码的理解：

我遇到的问题：
```

## 思考题

```text
1. `<b>` 为什么在 innerHTML 区域没有原样显示？
2. textContent 为什么会显示尖括号？
3. 输入验证和输出编码分别解决什么问题？
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 10: learn XSS output contexts"
```

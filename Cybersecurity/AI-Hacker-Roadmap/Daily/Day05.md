# Day 5 — 客户端参数可以被修改

## Mission

使用本地教学表单和 Postman Echo，证明网页上看不见的隐藏字段仍然会被客户端发送，也可以在 Burp 中修改。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：30–45 分钟

## 安全范围

- 本地页面：`Labs/ClientControls/form.html`
- 接收数据：`https://postman-echo.com/post`

本实验只回显你自己的教学数据。

## 今天需要理解

```text
网页界面限制
≠
服务器端安全验证
```

用户可以控制浏览器发出的请求。因此服务器必须重新验证重要数据。

## Part 1 — 启动本地页面

### Step 1 — 打开 VS Code 终端

确认终端当前位于仓库根目录 `Study_Computer`。运行：

```bash
cd Cybersecurity/AI-Hacker-Roadmap/Labs/ClientControls
python3 -m http.server 8000
```

成功后终端会显示类似：

```text
Serving HTTP on ... port 8000
```

保持这个终端运行，不要关闭。

如果提示端口被占用，改用：

```bash
python3 -m http.server 8005
```

后面的 URL 也要把 `8000` 改为 `8005`。

### Step 2 — 打开本地表单

在 Burp 自带浏览器访问：

```text
http://127.0.0.1:8000/form.html
```

页面应该显示：

```text
Day 5：客户端参数教学表单
Student name 输入框
Submit to Postman Echo 按钮
```

界面上看不到 `level` 输入框，这是正常的，因为它是隐藏字段。

## Part 2 — 产生基准请求

### Step 3 — 提交表单

在 `Student name` 输入：

```text
lin
```

点击：

```text
Submit to Postman Echo
```

浏览器会跳到 JSON 响应页面。

### Step 4 — 在 HTTP history 找请求

进入：

```text
Proxy → HTTP history
```

寻找：

```text
Host：postman-echo.com
Method：POST
Path：/post
```

不要选择加载本地 `form.html` 的 GET 请求。

### Step 5 — 检查正文

选中 POST 请求，在 Request 中找到空行后的正文。它应类似：

```text
student_name=lin&level=beginner
```

观察：

- `student_name=lin` 来自可见输入框。
- `level=beginner` 来自隐藏字段。
- 看不见不代表没有发送。

右键选择 `Send to Repeater`。

## Part 3 — 保存基准

### Step 6 — 不修改先发送

在 Repeater 中点击 `Send`。

确认响应正文的 `form` 中存在：

```json
"student_name": "lin",
"level": "beginner"
```

这就是基准结果。

## Part 4 — 只改隐藏参数

### Step 7 — 修改一个变量

在请求正文中只把：

```text
level=beginner
```

改为：

```text
level=advanced
```

不要同时修改姓名、方法、路径或请求头。

### Step 8 — 重新发送

点击 `Send`，确认响应正文 `form` 中：

```json
"student_name": "lin",
"level": "advanced"
```

应该看到：

```text
student_name 没变
level 发生变化
```

## Part 5 — 理解结果

本实验只证明：

```text
隐藏字段属于客户端请求
→ 用户能够修改
→ 服务器不能盲目信任
```

Postman Echo 只是回显内容，不代表 `advanced` 获得了任何真实权限。

## Part 6 — 停止本地服务

回到运行服务器的终端，按：

```text
Control + C
```

出现停止信息或终端提示符后，服务已经关闭。

## 常见错误与处理

| 现象 | 常见原因 | 处理 |
|---|---|---|
| `Connection refused` | 本地服务器没运行 | 重新执行 `python3 -m http.server 8000` |
| 本地页面 404 | 终端不在 `ClientControls` 目录 | 检查 `cd` 命令 |
| 找不到 POST | 选中了本地 GET 请求 | 查找 Host `postman-echo.com` |
| 正文没有 `level` | 选错请求 | 找点击提交按钮之后产生的 `/post` |
| 响应仍是 `beginner` | 修改后没重新发送 | 点击 `Send` 并看最新响应 |

## 成功标准

- [x] 本地表单成功打开
- [x] HTTP history 中找到 POST `/post`
- [x] 找到隐藏字段 `level=beginner`
- [x] 保存基准响应
- [x] 只修改 `level`
- [x] 新响应显示 `level=advanced`
- [x] 已停止本地服务器

## 操作记录

```text
网页上可见的字段：Student name

请求正文中的全部参数：student_name=lin&level=beginner

隐藏字段：level=beginner

修改前的值：level=beginner

修改后的值：level=advanced

响应中保持不变的字段：student_name 的值仍然是 lin

响应中发生变化的字段：level 从 beginner 变成 advanced

为什么服务器不能盲目信任客户端：用户可以控制并修改浏览器发出的请求，
包括网页上看不见的隐藏字段，所以服务器必须自己检查重要数据是否有效。

我遇到的问题：一开始不知道如何解释隐藏字段为什么仍能被服务器看到，
也不知道如何区分客户端限制和服务器验证。
```

## 思考题

```text
1. hidden 的意思是“服务器看不到”吗？
不是。hidden 只表示这个输入框不显示在网页界面上。提交表单时，
它仍然会进入请求正文，所以服务器能够收到它。

2. 为什么只在网页中限制输入还不够？
因为用户可以用 Burp 等工具修改浏览器发出的请求，绕过网页界面的限制。
因此网页限制可以帮助正常使用，但不能代替服务器端验证。

3. 应该由客户端还是服务器决定重要业务数据是否有效？
应该由服务器作最终决定。客户端可以先做输入检查来改善使用体验，
但重要数据必须由服务器再次验证，不能直接相信客户端传来的值。
```

## 今日一句话总结

```text
今天我学会了：隐藏字段只是网页上看不见，它仍然属于客户端请求，
也可以被用户修改。因此重要业务数据必须由服务器重新验证。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 5: modify a client-side parameter"
```

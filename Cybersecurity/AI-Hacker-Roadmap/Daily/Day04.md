# Day 4 — Cookie 与 Session

## Mission

在 Postman Echo 的测试请求中手动添加和删除 Cookie，观察 Cookie 如何通过请求头发送，并理解 Cookie 与 Session 的区别。

## 难度与时间

- 难度：⭐☆☆☆☆
- 核心任务：20–30 分钟

## 安全范围

只使用：

```text
https://postman-echo.com/get?day=4
```

今天只创建虚假的教学 Cookie：

```text
roadmap=day4
```

不要复制任何真实账号的 Cookie、Session ID 或 Token。

## 今日概念

- Cookie：浏览器保存的一小段数据，会通过 `Cookie` 请求头发送。
- Session：服务器用来记住一段访问或登录状态的机制。
- 网站常把 Session 标识放进 Cookie，但 Cookie 不等于整个 Session。

## Part 1 — 创建基准请求

### Step 1 — 打开 Burp 浏览器

确认：

```text
Proxy → Intercept → Intercept is off
```

点击 `Open browser`，访问：

```text
https://postman-echo.com/get?day=4
```

### Step 2 — 找到请求

进入：

```text
Proxy
→ HTTP history
```

寻找：

```text
Host：postman-echo.com
Method：GET
Path：/get?day=4
```

右键选择 `Send to Repeater`。

### Step 3 — 先分清请求 Cookie 与响应 Set-Cookie

在 Repeater 中先不修改，点击 `Send`。

先看左侧请求：

```text
Cookie: ...
```

如果左侧存在这一行，说明浏览器自动带上了以前保存的 Cookie。这不算做错，也不需要重新开始。

再看右侧响应：

```text
Set-Cookie: ...
```

它表示服务器正在让浏览器保存 Cookie，不表示这次请求已经发送了同一个 Cookie。

不要在学习记录中保存这两种字段的具体值，只记录：

```text
状态码：HTTP/2 200 OK
原始请求是否自动包含 Cookie：是
响应是否包含 Set-Cookie：是
具体值：未记录
```

### Step 4 — 建立不带 Cookie 的干净基准

如果左侧请求中有一个或多个 `Cookie:` 请求头，删除整个请求头，再点击 `Send`。

删除的是类似：

```http
Cookie: [具体值不记录]
```

不要删除右侧响应内容；右侧只是服务器已经返回的结果，不能直接编辑成下一次请求。

在最新响应正文的 `headers` 回显中确认没有发送 Cookie。服务器仍可能返回 `Set-Cookie` 响应头，这是正常现象。

这一次才是“不带 Cookie”的对照基准。

## Part 2 — 添加 Cookie

### Step 5 — 找到请求头区域

请求大致分为：

```text
请求行
请求头
空行
请求正文
```

在 `Host` 下面、最后一个空行之前添加：

```http
Cookie: roadmap=day4
```

不要把它写到空行之后。

### Step 6 — 发送

点击 `Send`，在响应正文的 `headers` 中寻找：

```json
"cookie": "roadmap=day4"
```

请求头名称也可能显示为 `Cookie`，大小写不同不影响结果。

## Part 3 — 删除 Cookie

### Step 7 — 受控比较

复制当前 Repeater 标签，或者保留响应记录。

只删除：

```http
Cookie: roadmap=day4
```

再次点击 `Send`。

比较：

```text
带 Cookie：响应 headers 中回显 roadmap=day4
不带 Cookie：响应不再回显该值
```

## 常见错误与处理

| 现象 | 常见原因 | 处理 |
|---|---|---|
| 找不到 `cookie` 回显 | `Cookie` 写在空行后面 | 把它移到请求头区域 |
| Cookie 值没有变化 | 修改后没有重新点击 `Send` | 重新发送并看最新响应 |
| 删除后仍看到旧值 | 正在查看上一次响应 | 确认选中最新 Repeater 历史 |
| 第一次请求已经有 Cookie | 浏览器自动带上以前保存的值 | 不用重来；先记录“有”，删除整个 `Cookie:` 头后建立干净基准 |
| 删除请求 Cookie 后仍看到 `Set-Cookie` | 混淆了请求头与响应头 | `Set-Cookie` 是服务器返回的，不代表本次请求发送了 Cookie |
| 请求一直等待 | Intercept 开着 | 切换为 `Intercept is off` |
| 不确定能否记录 | 可能是真实 Cookie | 不复制，改用教学值 `roadmap=day4` |

## 成功标准

- [x] 找到 Day 4 的 GET 请求
- [x] 确认原始请求没有 Cookie
- [x] 建立不带 Cookie 的基准
- [x] 正确添加 `Cookie: roadmap=day4`
- [x] 响应回显教学 Cookie
- [x] 删除 Cookie 后不再回显
- [x] 能用一句话区分 Cookie 与 Session

## 操作记录

```text
基准状态码：HTTP/2 200 OK

响应是否包含 Set-Cookie：是（具体值未记录）

基准响应正文是否回显请求 Cookie：没有；headers 中没有 cookie 字段

基准查询参数：args 中的 day 是 4

我添加的 Cookie 请求头：Cookie: roadmap=day4

带 Cookie 的响应：状态码是 200；响应正文的 headers 中回显
"cookie": "roadmap=day4"。

删除 Cookie 后的响应：状态码仍是 200；响应正文的 headers 中不再有
cookie 字段。响应仍可能出现 Set-Cookie，但它是服务器发给浏览器的响应头。

Cookie 是什么：浏览器保存的一小段数据。浏览器可以在之后的请求中通过
Cookie 请求头把它发给对应网站。

Session 是什么：服务器用来记住一段访问状态的机制，例如区分不同访问者
或记住登录状态。

它们为什么不是同一个东西：Cookie 是浏览器保存和发送的数据；Session
通常由服务器管理。网站可以把 Session 的标识放在 Cookie 中，但 Cookie
也可以保存其他数据，所以 Cookie 不等于整个 Session。

我遇到的问题：一开始把响应中的 Set-Cookie 和请求中的 Cookie 混淆了。
现在知道 Cookie 是客户端发送的请求头，Set-Cookie 是服务器返回的响应头。
```

## 隐私提醒

学习记录中不要保存：

```text
真实网站 Cookie
Session ID
Authorization
Token
密码
```

如果必须保留字段位置，写成：

```http
Cookie: [redacted]
```

## AI Prompt

```text
请只根据我提供的两个 Postman Echo 测试请求，
解释添加和删除 Cookie 请求头后发生的变化。
不要推测真实登录状态，也不要让我提供真实账号 Cookie。
```

## 今日一句话总结

```text
今天我学会了：Cookie 通过请求头从浏览器发送给服务器；Set-Cookie 通过
响应头从服务器发给浏览器。Session 是服务器记住访问状态的机制，Cookie
可以携带 Session 标识，但两者不是同一个概念。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 4: understand cookies and sessions"
```

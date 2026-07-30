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

### Step 3 — 发送基准

在 Repeater 中先不修改，点击 `Send`。

记录：

```text
状态码：
响应 headers 中是否存在 cookie：
```

这是“不带教学 Cookie”的基准。

## Part 2 — 添加 Cookie

### Step 4 — 找到请求头区域

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

### Step 5 — 发送

点击 `Send`，在响应正文的 `headers` 中寻找：

```json
"cookie": "roadmap=day4"
```

请求头名称也可能显示为 `Cookie`，大小写不同不影响结果。

## Part 3 — 删除 Cookie

### Step 6 — 受控比较

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
| 请求一直等待 | Intercept 开着 | 切换为 `Intercept is off` |
| 不确定能否记录 | 可能是真实 Cookie | 不复制，改用教学值 `roadmap=day4` |

## 成功标准

- [ ] 找到 Day 4 的 GET 请求
- [ ] 保存不带 Cookie 的基准
- [ ] 正确添加 `Cookie: roadmap=day4`
- [ ] 响应回显教学 Cookie
- [ ] 删除 Cookie 后不再回显
- [ ] 能用一句话区分 Cookie 与 Session

## 操作记录

```text
基准请求是否包含 Cookie：

我添加的 Cookie 请求头：

带 Cookie 的响应：

删除 Cookie 后的响应：

Cookie 是什么：

Session 是什么：

它们为什么不是同一个东西：

我遇到的问题：
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
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 4: understand cookies and sessions"
```

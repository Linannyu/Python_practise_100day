# Day 12 — 认证、Session 与登录流程

## Mission

在 PortSwigger 官方实验账号中，比较一次失败登录和一次成功登录的请求与响应，区分 Authentication、Session 和 Authorization。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：35–50 分钟

## 安全范围

使用 Day 7 的官方实验：

```text
https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls
```

只进行一次失败登录和一次成功登录，不做密码猜测或批量请求。

## 今天需要理解

```text
Authentication：确认你是谁
Session：让后续请求继续代表同一个用户
Authorization：判断这个用户能做什么
```

三者相关，但不是同一个概念。

## Part 1 — 新建实验实例

### Step 1 — 打开实验

点击 `Access the lab`。即使 Day 7 已完成，也可以启动新的临时实例。

进入 `My account` 登录页面。

### Step 2 — 隐私规则

今天会看到密码和 Cookie。学习记录中：

```text
用户名可以写实验用户名
密码不要复制
Cookie 只记录名称，不记录值
```

## Part 2 — 失败登录

### Step 3 — 提交一次错误密码

输入实验用户名：

```text
wiener
```

密码故意输入一个教学错误值，例如：

```text
wrong-day12
```

只提交一次。

### Step 4 — 找失败请求

在 `Proxy → HTTP history` 找到登录请求，通常是：

```text
POST /login
```

记录：

```text
请求方法与路径
username 位于正文的什么位置
password 位于正文的什么位置
响应状态码
页面错误信息
是否出现 Location
```

不要把完整请求复制进笔记，因为正文含密码。

## Part 3 — 成功登录

### Step 5 — 使用实验正确密码

返回登录页，使用实验提供的正确凭据登录。

不要把正确密码写进操作记录。

### Step 6 — 找成功请求

HTTP history 中会有另一条 POST `/login`。

根据时间顺序和响应判断哪一条是成功登录。记录：

```text
响应状态码
是否有 Location
是否有 Set-Cookie
Cookie 名称
浏览器最终页面
```

如果出现 `302`，它通常表示浏览器被引导到另一个页面。以你实际看到的状态为准。

## Part 4 — 对照

| 项目 | 失败登录 | 成功登录 |
|---|---|---|
| 方法与路径 |  |  |
| 状态码 |  |  |
| 错误信息 |  |  |
| Location |  |  |
| Set-Cookie 名称 |  |  |
| 最终页面 |  |  |

只写 Cookie 名称，例如 `session`；值写 `[redacted]`。

## Part 5 — 建立概念

### Authentication

成功登录响应证明实验接受了提供的身份凭据。

### Session

服务器可能通过 Cookie 标识后续请求属于同一已登录用户。Cookie 是客户端携带的值，Session 状态通常由服务器管理。

### Authorization

即使登录成功，服务器仍然必须检查当前用户是否有权访问某个页面或执行某个动作。

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| 两次都失败 | 正确登录时仍使用错误密码 | 重新查看实验说明 |
| 分不清两条请求 | 没看时间顺序 | 先清空筛选或按时间比较 |
| 成功响应看起来空 | 可能是重定向 | 查看状态码和 Location |
| 笔记里出现 Cookie 值 | 复制了完整请求 | 立即替换为 `[redacted]` |
| 实例过期 | 临时 Lab 超时 | 重新 Access the lab |

## 成功标准

- [ ] 只做一次失败登录
- [ ] 完成一次成功登录
- [ ] 找到两条登录请求
- [ ] 比较状态码与 Location
- [ ] 只记录 Cookie 名称
- [ ] 能区分 Authentication、Session、Authorization

## 操作记录

```text
失败登录方法与路径：
失败状态码：
失败错误信息：
失败 Location：

成功登录方法与路径：
成功状态码：
成功 Location：
成功 Set-Cookie 名称：
最终页面：

Authentication 是：
Session 是：
Authorization 是：

我遇到的问题：
```

## 思考题

```text
1. 登录成功是否代表可以访问所有功能？
2. Cookie 和服务器 Session 为什么不是同一个东西？
3. 302 和 200 在你的两个响应中分别对应什么行为？
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 12: inspect authentication flow"
```


# Day 13 — Access Control 与 IDOR

## Mission

完成 PortSwigger `User ID controlled by request parameter` 实验，理解“已经登录”为什么不等于“可以读取任何用户资料”。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：40–60 分钟

## 安全范围

只使用：

```text
https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter
```

## 今天需要理解

```text
Authentication：确认当前用户是 wiener
Authorization：检查 wiener 是否有权读取目标资料
IDOR：客户端控制对象标识，但服务器缺少正确所有权检查
```

## Part 1 — 打开与登录

### Step 1 — Access the lab

打开课程链接，点击 `Access the lab`。

### Step 2 — 使用实验账号

进入 `My account`，使用实验提供的账号登录。

账号只用于当前实验。不要在笔记中保存密码。

## Part 2 — 建立自己的资料基准

### Step 3 — 打开 My account

登录后观察浏览器 URL。寻找：

```text
id=wiener
```

### Step 4 — 找到请求

在 HTTP history 中找到打开账号页面的 GET 请求。确认请求中有：

```text
id=wiener
```

右键 `Send to Repeater`。

### Step 5 — 保存基准

在 Repeater 中不修改，点击 `Send`。

记录：

```text
状态码
页面显示的用户名
页面是否包含 API key 字段
```

API key 值不要复制到公开记录，用 `[redacted]`。

## Part 3 — 修改对象标识

### Step 6 — 只修改 id

只把：

```text
id=wiener
```

改成实验要求的：

```text
id=carlos
```

不要修改 Cookie。保留自己的登录 Session，以验证服务器是否正确执行授权检查。

### Step 7 — 发送并比较

点击 `Send`。比较：

```text
状态码是否变化
页面用户名是否变化
API key 字段是否变化
```

如果服务器返回另一个用户的资料，说明它只使用 `id` 查找对象，却没有检查当前登录用户是否有权读取该对象。

## Part 4 — 完成实验

### Step 8 — 提交实验答案

按照实验页面要求提交找到的值。

不要把该值写进 Markdown 记录。记录为：

```text
[redacted]
```

成功后确认：

```text
Solved
```

## 根本原因

错误逻辑：

```text
用户已登录
→ 直接相信 id 参数
→ 返回该 id 对应资料
```

正确逻辑：

```text
用户已登录
→ 根据当前 Session 确定身份
→ 检查是否有权访问目标对象
→ 允许或拒绝
```

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| 找不到 id | 没进入 My account | 登录后打开账号页 |
| 修改后被登出 | Cookie 被删除或改动 | 使用原请求，只改 id |
| 响应还是 wiener | 参数没改对或看旧响应 | 检查最新 Repeater 请求 |
| 实验未完成 | 没按页面要求提交值 | 回到 Lab 提交 |
| API key 出现在笔记 | 未脱敏 | 替换为 `[redacted]` |

## 成功标准

- [x] 登录实验账号
- [x] 找到 `id=wiener`
- [x] 保存自己的资料基准
- [x] 只修改 id
- [x] 比较两个资料响应
- [x] Lab 显示 Solved
- [x] API key 和 Cookie 已脱敏
- [x] 能说明缺少的是授权检查

## 实验记录

```text
Lab 名称：User ID controlled by request parameter

请求方法与路径：GET /my-account?id=wiener

对象标识参数：id

基准用户：wiener

修改后的用户：carlos

状态码变化：没有变化

页面内容变化：页面从 wiener 的资料变成 carlos 的资料，API key 字段也对应另一个用户；具体值没有记录。

敏感值记录：[redacted]

缺少的服务器检查：服务器没有检查当前 Session 代表的 wiener 是否有权读取 id=carlos 指向的资料对象，也就是缺少对象所有权的授权检查。

正确修复方向：如果页面只用于查看自己的资料，应根据服务器端 Session确定当前用户，而不是相信客户端提交的 id。如果功能确实允许指定 id，服务器必须在返回资料前检查当前用户对该对象的访问权限，无权时拒绝请求。

我遇到的问题：一开始容易把“已经登录”和“有权读取目标资料”当成同一件事。实验说明 Authentication 成功后，服务器仍需要单独执行 Authorization。
```

## 思考题

```text
1. 为什么这不是“密码错误”问题？
因为 wiener 已经使用正确实验账号登录，身份认证已经成功。问题发生在登录之后：服务器根据客户端提供的 id 返回资料，却没有检查资料是否属于当前用户。因此这是 Authorization 问题，不是密码验证问题。

2. 保留自己的 Cookie 有什么验证意义？
保留自己的 Cookie 可以让服务器继续把请求识别为已登录的 wiener。这样测试只改变 id，一个变量就能说明：wiener 的登录状态是否被允许读取 carlos的资料。Cookie 只保留在请求中，学习记录不保存具体值。

3. 如果服务器返回 403，会说明什么？
403 表示服务器理解请求，也识别到当前用户，但拒绝访问目标资料。在这个对照中，它会支持“服务器执行了授权检查并阻止了这次越权访问”的判断。不过一次 403 只能说明这一条请求被拒绝，不能自动证明整个应用所有权限检查都正确。
```

## 今日一句话总结

```text
今天我学会了：Authentication 只确认当前用户是谁，Authorization 还要检查这个用户是否有权访问目标对象。服务器不能只相信客户端提供的 id，而必须根据 Session 身份执行对象级权限检查。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 13 access control lab"
```

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

- [ ] 登录实验账号
- [ ] 找到 `id=wiener`
- [ ] 保存自己的资料基准
- [ ] 只修改 id
- [ ] 比较两个资料响应
- [ ] Lab 显示 Solved
- [ ] API key 和 Cookie 已脱敏
- [ ] 能说明缺少的是授权检查

## 实验记录

```text
Lab 名称：

请求方法与路径：

对象标识参数：

基准用户：

修改后的用户：

状态码变化：

页面内容变化：

敏感值记录：[redacted]

缺少的服务器检查：

正确修复方向：

我遇到的问题：
```

## 思考题

```text
1. 为什么这不是“密码错误”问题？
2. 保留自己的 Cookie 有什么验证意义？
3. 如果服务器返回 403，会说明什么？
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 13 access control lab"
```


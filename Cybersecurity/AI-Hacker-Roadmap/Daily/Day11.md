# Day 11 — Reflected XSS 官方实验

## Mission

先用普通标记确认输入被反射的位置，再完成 PortSwigger 最基础的 Reflected XSS 实验。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：35–55 分钟

## 安全范围

只使用：

```text
https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded
```

实验测试值只能输入该官方临时实例。

## 今天需要理解

```text
请求中的搜索输入
→ 服务器把它放进响应 HTML
→ 浏览器把响应当作页面解析
```

先确认“反射”，再确认“执行”，不要跳过基准。

## Part 1 — 打开实验

### Step 1 — Access the lab

在 Burp 自带浏览器打开课程链接，点击：

```text
Access the lab
```

等待临时博客或商店页面出现。页面应包含搜索功能。

### Step 2 — 确认 Intercept

返回 Burp，确认：

```text
Proxy → Intercept → Intercept is off
```

这样搜索请求可以正常到达实验服务器。

## Part 2 — 普通标记基准

### Step 3 — 搜索唯一标记

在实验搜索框输入：

```text
LIN-DAY11
```

点击 Search。

页面应显示你搜索的文字。

### Step 4 — 找到请求

进入：

```text
Proxy → HTTP history
```

寻找包含：

```text
LIN-DAY11
```

的 GET 请求。选中后查看 Request 和 Response。

### Step 5 — 在响应中定位

在 Response 搜索 `LIN-DAY11`。记录它周围实际出现的少量 HTML，例如它是在标签文字之间还是其他位置。

不要复制整个响应，只保存能证明位置的片段。

## Part 3 — 保存 Repeater 基准

### Step 6 — Send to Repeater

右键标记请求，选择 `Send to Repeater`。

先不修改，点击 `Send`。确认：

```text
状态码正常
响应中仍包含 LIN-DAY11
```

这证明参数与反射位置的关系可重复。

## Part 4 — 完成官方实验

### Step 7 — 使用官方测试值

回到实验搜索框，只在该实验实例输入：

```html
<script>alert(1)</script>
```

点击 Search。

### Step 8 — 观察结果

成功时浏览器会出现一个显示 `1` 的对话框。点击确定关闭。

页面顶部应显示：

```text
Solved
```

### Step 9 — 解释原因

只根据本实验说明：

```text
输入来自搜索参数
→ 响应没有把尖括号等内容安全编码
→ 输入进入 HTML 上下文
→ 浏览器把 script 当作页面代码
```

## Part 5 — 保存脱敏证据

记录：

```text
搜索参数名称
普通标记
普通标记所在响应位置
官方测试值
浏览器结果
Lab 状态
修复方向
```

删除 Cookie、实验临时域名和会话信息。

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| 搜索后没反射 | 选错实验或参数 | 先用 LIN-DAY11 找正确请求 |
| 看到文字但没有对话框 | 测试值被当作文字或位置不对 | 确认是指定的 nothing encoded 实验 |
| 请求卡住 | Intercept 开着 | 切换为 off |
| Lab 未 Solved | 在课程说明页而非实例操作 | 重新 Access the lab |
| 实例打不开 | 临时实例过期 | 启动新实例 |

## 成功标准

- [ ] 正确打开实验实例
- [ ] 先使用普通标记
- [ ] 在响应中找到标记位置
- [ ] 保存 Repeater 基准
- [ ] 只在实验中使用官方测试值
- [ ] 浏览器出现对话框
- [ ] Lab 显示 Solved
- [ ] 记录已脱敏

## 实验记录

```text
Lab 名称：

搜索参数：

普通标记：

标记出现在响应的什么位置：

官方测试值：

浏览器发生了什么：

为什么输入会被当作代码：

开发者应如何修复：

我遇到的问题：
```

## 思考题

```text
1. 为什么要先使用 LIN-DAY11，而不是一开始就输入 script？
2. “输入被反射”是否自动代表脚本一定能执行？
3. textContent 与这个实验的修复思路有什么联系？
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 11 reflected XSS lab"
```


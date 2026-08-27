# Day 26 — 整理漏洞证据

## Mission

从已经完成的 PortSwigger 官方实验中选一个，把现有记录整理成别人可以复查、同时不泄露会话信息的证据包。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：30–45 分钟

## 选择范围

只能选你已经完成的一项：

```text
Day 7：Client-side controls
Day 9：SQL Injection
Day 11：Reflected XSS
Day 13：IDOR
Day 14：Unprotected admin functionality
```

今天不重新测试，也不访问新目标，只整理已有证据。

## Step 1 — 选择证据最完整的一项

先检查哪一项同时具有：

- 修改前的基准。
- 一次关键改动。
- 修改后的观察结果。
- Lab 已解决的截图或记录。

缺少这些内容的实验先不要选。

## Step 2 — 创建目录和文件

假设选择 Day 13，在 VS Code 中创建：

```text
Labs/PortSwigger/Day13/
├── README.md
├── request-redacted.txt
├── response-summary.txt
└── screenshot.png
```

选择其他天时，把目录名换成对应的 `Day07`、`Day09`、`Day11` 或 `Day14`。

## Step 3 — 整理脱敏请求

把关键请求复制到 `request-redacted.txt`，但先删除或替换：

```text
Cookie 与 Session 值
Authorization
密码
API key
实验实例域名或 ID
公网 IP
个人账号信息
不必要的追踪 ID
```

可以保留：

```text
Cookie: [redacted]
```

不要保留：

```text
Cookie: 真实值
```

只保留证明那一次关键修改所需的请求行、必要请求头和必要正文。

## Step 4 — 写响应摘要

`response-summary.txt` 不需要保存完整响应，只写：

```text
Baseline status：
Baseline observable result：
Changed status：
Changed observable result：
Single changed element：
What this proves：
What this does not prove：
```

“observable result” 应该是你实际看见的文字、页面行为或 Lab 状态，不是猜测的服务器内部代码。

## Step 5 — 处理截图

截图前检查画面：

- 地址栏是否包含实验实例 ID。
- Burp 是否显示 Cookie 或 Session。
- 是否出现个人账号、邮箱或系统通知。
- 是否有无关浏览器标签。

如果有敏感内容，先裁剪或遮挡；不要只依赖缩小图片让文字看不清。截图应同时保留能证明结果的区域。

## Step 6 — 填写 README

```markdown
# Evidence — Lab name

## Scope

## Objective

## Baseline

## Single Change

## Observed Result

## Why This Evidence Supports the Finding

## Redactions

## Limitations
```

每个标题下至少写一句。`Limitations` 要说明这份证据没有测试哪些内容。

## Step 7 — 反向复查

先关闭自己的 Day 文件，只看证据包，尝试回答：

```text
测试了什么？
修改前是什么？
只改变了什么？
实际发生了什么？
为什么支持结论？
什么仍然无法确认？
```

如果任何一题答不出，回到对应文件补充证据，而不是补充猜测。

## Step 8 — 做秘密值搜索

在工作区根目录运行：

```bash
rg -n -i "cookie:|authorization:|password|api[_-]?key|token|session" \
  Cybersecurity/AI-Hacker-Roadmap/Labs/PortSwigger
```

搜索结果中的教学词语不一定是泄露，必须人工检查冒号或等号后面是否有真实值。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| 只有修改后请求 | 没保留基准 | 从原记录补充修改前状态 |
| 保存整份响应 | 认为越多越有证据 | 改为只保留能证明结果的摘要 |
| 截图遮掉了关键结果 | 脱敏范围太大 | 只遮秘密值，保留必要证据 |
| README 写成过程日记 | 没按证据链组织 | 使用 Baseline → Single Change → Result |
| 用猜测填空缺 | 原始证据不足 | 在 Limitations 诚实写明无法确认 |

## 成功标准

- [x] 目标明确属于已完成的官方实验
- [x] 有修改前基准
- [x] 有且只有一个关键改动
- [x] 响应摘要能证明观察结果
- [x] 截图保留证据且完成脱敏
- [x] 搜索并人工检查过秘密值

## 操作记录

```text
我选择的 Lab：Day 14 — Unprotected admin functionality（已完成的 PortSwigger 官方实验）。
证据包路径：Labs/PortSwigger/Day14/
基准证据：未使用管理员凭据，且正常导航没有显示管理功能；原始记录没有基准 HTTP 状态，因此在证据中明确写为“未记录”，没有猜测状态码。
单一改动：请求目标从公开提示路径 /robots.txt 改为提示的 /administrator-panel；其他测试前提保持不变。
观察结果：管理页面状态为 200，显示用户列表和 Delete 操作；完成实验目标后显示 User deleted successfully!，Lab 状态为 Solved。
我脱敏的字段：临时实验域名、实例 ID、Cookie、Session、Authorization、完整请求/响应头和不必要追踪值；截图地址栏和标签页实例编号已不透明遮挡。
仍无法确认：服务器源代码、完整基准 HTTP 响应、其他系统是否存在相同行为，以及真实网站的影响。
```

## 今日一句话总结

今天我把 Day 14 的已有记录整理成可复查的脱敏证据包：保留基准、一次路径变化、状态与 Solved 结果，同时清楚写出证据不能证明什么。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 26: build a redacted evidence package"
```

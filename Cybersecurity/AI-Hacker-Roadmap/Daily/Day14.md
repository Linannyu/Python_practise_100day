# Day 14 — Week 2 Boss Lab 与简短报告

## Mission

独立完成 `Unprotected admin functionality` 实验，并把分析过程写成第一份简短报告。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：50–75 分钟

## 安全范围

只使用：

```text
https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality
```

## Boss 规则

前 15 分钟不查看官方 Solution。只使用今天给出的渐进提示。

分析顺序：

```text
理解目标
→ 浏览正常页面
→ 寻找公开提示
→ 找到敏感功能
→ 验证是否有访问控制
→ 保存证据
→ 写报告
```

## Part 1 — 打开实验

### Step 1 — Access the lab

从课程页面点击 `Access the lab`，等待临时实验出现。

### Step 2 — 记录目标

只根据实验页面写下：

```text
需要找到什么功能：没有出现在正常导航中的管理用户功能
实验要求完成什么动作：删除实验中的虚拟用户 carlos
成功标志：页面显示 User deleted successfully!，Lab 状态变为 Solved
```

## Part 2 — 独立观察

### Step 3 — 浏览正常页面

查看主页、导航和普通功能。不要随机猜大量路径。

### Step 4 — 查看公开提示文件

如果 5–10 分钟后没有发现入口，使用提示 1：

```text
搜索引擎爬虫常读取哪个根目录文件？
```

提示 2：

```text
访问 /robots.txt
```

### Step 5 — 阅读 robots.txt

只阅读实际内容。寻找 `Disallow` 指向的路径。

记录该路径，但不要把临时实验域名写进公开报告。

本次实验记录：

```text
robots.txt 中的提示路径：/administrator-panel
```

## Part 3 — 验证敏感功能

### Step 6 — 打开提示路径

在当前实验实例访问 `robots.txt` 暴露的路径。

观察：

```text
是否需要登录：不需要管理员登录即可打开
状态码：200
页面是否提供管理操作：提供用户列表和 Delete 操作
```

### Step 7 — 理解问题

如果未登录用户能直接访问管理功能，说明：

```text
路径虽然没出现在正常导航但服务器没有实施访问控制
```

隐藏路径不是权限验证。

### Step 8 — 完成实验动作

只按照实验目标操作虚拟用户。完成后确认页面显示：

```text
Solved
```

## Part 4 — 保存证据

建议保存：

```text
robots.txt 中的相关一行
访问管理路径的状态码 200
未登录即可看到管理功能的事实
Solved 截图
```

删除：

```text
实验临时域名
Cookie
Session
不必要的用户数据
```

## Part 5 — 写简短报告

创建：

```text
Labs/PortSwigger/Day14-report.md
```

使用：

```markdown
# Unprotected Admin Functionality

## Summary
用 2–3 句话说明已经验证的问题。

## Authorized Target
PortSwigger Web Security Academy lab

## Preconditions
说明测试时是否登录。

## Steps to Reproduce
1.
2.
3.

## Observed Result

## Expected Result

## Security Impact

## Root Cause

## Recommended Fix

## Evidence
只放脱敏片段。
```

## 修复方向

报告中应写：

```text
服务器必须在每个管理请求上检查用户身份和角色不能只隐藏链接或使用不明显路径未授权请求应被拒绝
```

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| 找不到入口 | 没查看 robots.txt | 使用提示 2 |
| robots 路径 404 | 复制了多余字符 | 精确复制 Disallow 路径 |
| 以为路径隐藏就安全 | 混淆导航与授权 | 检查服务器是否拒绝访问 |
| 报告影响写得很大 | 超出实验证据 | 只写已验证管理操作 |
| 报告含实例域名 | 未脱敏 | 用 `[lab-instance]` 替换 |

## 成功标准

- [x] 前 15 分钟独立分析
- [x] 找到 robots.txt
- [x] 找到管理路径
- [x] 验证缺少访问控制
- [x] Lab 显示 Solved
- [x] 创建简短报告
- [x] 报告含修复建议
- [x] 证据已脱敏

## 实验记录

```text
Lab 名称：Unprotected admin functionality

授权范围：PortSwigger Web Security Academy 官方实验

公开提示文件：/robots.txt

公开提示内容：Disallow 指向 /administrator-panel

管理路径：/administrator-panel

访问管理页面是否需要管理员登录：不需要

管理页面状态码：200

可见功能：查看实验用户列表并执行 Delete 操作

实际结果：删除虚拟用户 carlos 后，页面显示 User deleted successfully!，Lab 状态显示 Solved。

脱敏截图：Images/day14-solved.png；临时实验域名和标签页中的实例编号已遮挡。

根本原因：服务器没有在管理页面和管理操作上执行身份与角色授权检查，只是依赖不明显的路径隐藏入口。

正确修复：每个管理页面和管理操作都必须在服务器端检查当前用户身份与管理员角色；未授权请求应被拒绝，不能把 robots.txt 或隐藏路径当作权限。

我使用的提示：课程提示 2，即访问 /robots.txt；没有在记录中保存临时域名。

我遇到的问题：一开始不知道为什么会想到 /robots.txt。后来理解到它是搜索引擎爬虫约定读取的根目录公开文件，实提示就是在引导查看这个文件。
```

## Week 2 复盘

```text
SQL Injection 的根本原因：服务器把不可信输入直接拼进 SQL，使输入可能改变原本固定的 SQL 结构。修复重点是参数化查询。

Reflected XSS 的根本原因：服务器把用户输入放进响应 HTML 时没有根据输出上下文安全编码，浏览器可能把输入当作页面代码解析。

Authentication 与 Authorization 的区别：Authentication 确认当前用户是谁；Authorization 判断这个用户是否有权访问某个对象或执行某个操作。

IDOR 缺少的检查：服务器缺少当前用户对目标对象的对象级所有权或访问权限检查，不能只相信客户端提供的 id。

隐藏入口为什么不是访问控制：只要路径被发现，任何人仍可以发送请求。真正的访问控制必须由服务器在每次请求上检查身份和角色并允许或拒绝。

我最容易混淆的概念：一开始把“不在导航中显示”和“没有访问权限”当成同一件事。robots.txt 反而可能公开隐藏路径，但它不会提供任何权限保护。
```

## 今日一句话总结

```text
今天我学会了：robots.txt 是公开的爬虫提示文件，Disallow 不是安全限制。管理入口即使被隐藏，服务器仍必须在每个管理请求上执行身份和角色授权检查。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete week 2 boss lab and report"
```

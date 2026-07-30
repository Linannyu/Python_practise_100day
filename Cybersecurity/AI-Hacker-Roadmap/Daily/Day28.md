# Day 28 — 综合授权靶场

## Mission

在不知道详细步骤的情况下，完成 PortSwigger `Information disclosure in error messages` 实验，并建立完整分析链。

## 难度与时间

- 难度：⭐⭐⭐⭐☆
- 核心任务：45–75 分钟

## 安全范围

只使用：

```text
https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages
```

## 分析流程

```text
阅读目标
→ 浏览正常功能
→ 找到可控输入
→ 保存基准请求与响应
→ 提出一个假设
→ 每次只改一个变量
→ 比较响应
→ 记录证据
→ 提交实验答案
```

## 先独立分析

前 20 分钟不要查看 Solution，也不要让 AI 给答案。先填写：

```text
目标：
可能的输入点：
基准请求：
基准响应：
我的假设：
最小测试：
预期结果：
```

## 渐进提示

只有卡住时逐条查看：

```text
提示 1：打开一个商品详情页并查看请求。
提示 2：寻找用于选择商品的参数。
提示 3：服务器预期参数是什么数据类型？
提示 4：尝试一个明显不是数字的普通字符串，观察错误响应。
```

仍然卡住 20 分钟后，可以阅读官方 Solution，并在记录中注明使用了哪一级提示。

## 成功标准

- [ ] 保存基准
- [ ] 写出可验证假设
- [ ] 每次只改一个变量
- [ ] 找到错误信息泄露的版本信息
- [ ] Lab 显示 `Solved`
- [ ] 完成脱敏证据与根本原因

## 根本原因与修复

报告应讨论：

```text
为什么详细错误不应直接返回给普通用户
用户应看到什么
详细错误应记录在哪里
为什么依赖升级与错误处理都重要
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 28 comprehensive lab"
```


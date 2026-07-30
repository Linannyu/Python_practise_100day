# Day 27 — 编写漏洞报告

## Mission

使用 `Reports/TEMPLATE.md`，把 Day 26 的证据写成一份完整但简洁的报告。

## 难度与时间

- 难度：⭐⭐⭐⭐☆
- 核心任务：40–60 分钟

## 报告原则

- 可复现：别人能按步骤得到同样结果。
- 有证据：结论引用请求和响应。
- 不夸大：只写已经验证的影响。
- 可修复：建议指向根本原因。
- 已脱敏：不泄露会话或个人信息。

## 写作流程

1. 复制 `Reports/TEMPLATE.md`。
2. 命名为：

```text
Reports/Day27-first-report.md
```

3. 填写 Summary、Scope、Steps、Evidence、Impact 和 Remediation。
4. 删除所有占位说明。
5. 使用下面的自检表。

## 报告自检

- [ ] 标题准确描述问题
- [ ] Scope 明确写出 PortSwigger 官方实验
- [ ] 复现步骤没有跳步
- [ ] Observed 与 Expected 分开
- [ ] Impact 没有超出证据
- [ ] Remediation 对应根本原因
- [ ] 没有 Cookie、密码、Token 或 API key

## AI 编辑 Prompt

```text
请把自己当作技术报告编辑，只检查：
- 是否清楚
- 是否可复现
- 结论是否超出证据
- 修复是否对应根本原因
- 是否可能泄露敏感信息

不要增加我没有验证的影响，不要改变技术事实。
```

## 成功标准

- [ ] 报告模板全部填写
- [ ] 完成脱敏检查
- [ ] 至少根据审阅修改一次
- [ ] 能在两分钟内口头概述报告

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 27: write first vulnerability report"
```


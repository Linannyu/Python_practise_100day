# Unprotected admin functionality in an authorized training lab

## Summary

在已完成的 PortSwigger Web Security Academy 官方实验中，管理功能可以在未使用管理员凭据的情况下访问。公开的 `/robots.txt` 提示了管理路径，直接访问该路径后返回了管理功能；完成实验指定动作后，页面显示 `User deleted successfully!`，Lab 状态显示 `Solved`。

这份报告只记录该授权实验中已经观察到的行为，不对任何真实网站作出判断。

## Authorized Scope

```text
平台：PortSwigger Web Security Academy 官方实验
Lab 名称：Unprotected admin functionality
测试日期：2026-08-09（依据 Day 14 的原始实验记录）
```

## Preconditions

测试在官方临时 Lab 实例中进行。测试时没有使用管理员凭据；临时实例域名、Cookie、Session 和其他会话信息均未保留。

## Steps to Reproduce

1. 在官方 Lab 中查看公开文件 `/robots.txt`。
2. 记录该文件中 `Disallow` 指向的 `/administrator-panel` 路径。
3. 在不使用管理员凭据的前提下，访问该管理路径。
4. 观察管理页面是否返回管理操作；仅按照该官方 Lab 的指定目标完成虚拟用户操作。

## Observed Result

管理页面返回状态 `200`，并显示实验用户列表和 Delete 操作。完成 Lab 指定操作后，页面显示 `User deleted successfully!`，同时 Lab 状态显示 `Solved`。

## Expected Result

管理页面和管理操作应在服务器端检查当前用户是否已认证并具有管理员角色。没有管理员权限的请求应被拒绝，而不是仅通过隐藏导航或不明显路径来保护功能。

## Evidence

- [脱敏请求摘要](../Labs/PortSwigger/Day14/request-redacted.txt)：记录公开提示路径和管理路径；不含实例域名或会话值。
- [响应摘要](../Labs/PortSwigger/Day14/response-summary.txt)：记录管理页面的 `200`、可见操作和 Lab 的完成提示。
- [脱敏截图](../Labs/PortSwigger/Day14/screenshot.png)：保留 `User deleted successfully!` 和 `Solved`，地址栏实例域名已不透明遮挡。

## Security Impact

在该官方 Lab 中，未使用管理员凭据的访问者能够到达管理功能并完成 Lab 指定的虚拟用户删除操作。这证明该实验中的管理功能缺少有效访问控制；不代表其他系统存在相同影响。

## Root Cause

从可观察行为看，管理路径及管理操作没有执行有效的服务器端身份与管理员角色检查。隐藏导航或使用不明显路径不是访问控制；`robots.txt` 是公开提示文件，不能承担权限保护作用。报告没有服务器源代码，因此不对内部实现作进一步断言。

## Recommended Remediation

- 在每一个管理页面和管理操作的服务器端入口执行身份认证与角色授权检查。
- 对没有管理员权限的请求返回拒绝响应或引导到适当登录流程。
- 不把隐藏链接、不可见导航、难猜路径或 `robots.txt` 当作安全机制。
- 为管理操作保留审计记录，并为授权规则建立自动化测试。

## Redactions

报告不包含临时实验域名、实例 ID、Cookie、Session、Authorization、密码、Token、API key、完整请求/响应头、完整响应正文或个人信息。截图中的地址栏和标签页实例编号已使用不透明遮挡。

## Limitations

本报告只覆盖一个已完成的官方教学 Lab。它不包含服务器源代码、完整基准 HTTP 响应或其他应用的证据，也不支持对真实网站、其他用户数据或其他管理操作作出结论。

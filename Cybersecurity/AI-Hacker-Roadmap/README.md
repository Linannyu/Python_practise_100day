# AI Hacker Roadmap

> 从零开始学习 HTTP、Web 安全基础、Python 工具和 AI 辅助验证的 30 天学习项目。

## 项目目的

我通过可重复的小练习，学习如何读懂 HTTP 请求与响应、审查简单 Web 代码、记录证据，并用 Python 编写安全辅助工具。重点是理解原理、保持授权范围，以及能清楚说明自己做了什么。

## 30 天学习范围

课程分成四个阶段：

1. HTTP、URL、Cookie、Session 和 Burp Suite 的基础观察。
2. 在官方授权靶场中理解 SQL、XSS、认证和访问控制的基础概念。
3. 用 Python 编写 URL 解析、HTTP 摘要与响应对比等本地小工具。
4. 用 AI 提出假设后，再以代码、请求或文档进行人工验证，并学习写脱敏证据和报告。

完整任务见 [Daily/INDEX.md](Daily/INDEX.md)，课程节奏见 [ROADMAP.md](ROADMAP.md)。

## 合法使用边界

本项目的操作只针对自己搭建的本地页面和明确授权的教学靶场，例如 PortSwigger Web Security Academy。不会对真实网站、账号、设备或网络进行未授权测试。

公开前不提交 Cookie、Session、Token、密码、个人信息、实验实例 ID 或完整实验响应。证据只保留脱敏后的必要摘要。

## 完成进度

- 当前阶段：Week 4 — AI-Assisted Security Workflow
- 当前天数：Day 29 / 30
- 最近完成：Day 29 — 2026-08-30
- 已完成每日任务：29 / 30
- 已完成官方授权实验：6 个（Day 7、9、11、13、14、28）
- 已完成本地 Python 工具：3 个（HTTP 摘要、URL 解析、Day 25 验证检查）
- 开始学习：2026-07-27

## 代表性 Lab

- [Day 14：未受保护的管理员功能](Labs/PortSwigger/Day14/README.md)：使用官方实验，保存了不含会话值的请求摘要、响应摘要和已脱敏截图。
- [Day 27：第一份脱敏报告](Reports/Day27-first-report.md)：把现象、影响、复现与修复建议分开写清楚。
- [Day 28：综合授权靶场证据](Labs/PortSwigger/Day28/README.md)：展示从观察到验证的简短证据链。

其他实验的学习解释保存在对应的 [Daily](Daily) 文件中，而不是复制靶场页面或保留敏感数据。

## Python 工具

- [http_inspector.py](Scripts/http_inspector.py)：只读取允许列表内 URL 的状态码、内容类型、字节数和正文摘要；不保存完整响应或认证信息。
- [url_parser.py](Scripts/url_parser.py)：把 URL 分成协议、主机、路径和查询参数，帮助理解请求结构。
- [day25_checks.py](Scripts/day25_checks.py)：用固定的本地示例检查 AI 对代码行为的判断是否可复现。

每个工具的安全范围和使用示例见 [Scripts/README.md](Scripts/README.md)。

## 目录结构

```text
AI-Hacker-Roadmap/
├── Daily/       # 每天的步骤、思考题和学习记录
├── Labs/        # 本地练习与授权实验的脱敏证据
├── Reports/     # 脱敏报告模板和示例报告
├── Scripts/     # 自编 Python 小工具及其安全说明
├── Resources/   # 课程参考资料
├── Payloads/    # 仅用于本地或官方靶场的学习材料
├── Tools/       # 工具配置说明
├── ROADMAP.md   # 30 天路线和完成状态
└── PORTFOLIO.md # 可展示的学习摘要
```

## 如何运行本地工具

在项目根目录运行。第一次使用时，先启用虚拟环境并安装依赖：

```bash
source .venv/bin/activate
pip install -r Scripts/requirements.txt
```

然后开两个终端：

```bash
# 终端 A：启动课程自己的本地页面
cd Labs/LocalHTTP
python3 -m http.server 8000

# 终端 B：回到 AI-Hacker-Roadmap 根目录后运行摘要工具
python3 Scripts/http_inspector.py http://127.0.0.1:8000/
python3 -m Scripts.day25_checks
```

HTTP 工具只允许 `localhost`、`127.0.0.1` 和课程指定的演示站点；输入其他主机时会在发出请求前拒绝。

## 我学到的内容

- HTTP 请求由方法、路径、查询参数、请求头、空行和可选正文组成；响应包含状态码、响应头和正文。
- 客户端页面显示的内容不能单独证明权限；服务端必须验证身份、权限和关键数据。
- SQL、XSS、认证和访问控制的风险需要在授权环境中用最小、可验证的步骤理解。
- AI 的说法是待验证的假设，不是结论；我会用代码、输出或官方文档来确认。
- 好的安全记录应当说明范围、事实、影响和修复方向，同时去除敏感信息。

下一步：完成 [Day 30](Daily/Day30.md) 的复盘和下一阶段计划。

# Day 29 — 整理 GitHub 项目

## Mission

把项目整理成别人能够安全阅读、运行和理解的作品集。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：45–75 分钟

## 今天不做

- 不自动公开仓库。
- 不上传实验 Cookie、Token 或个人信息。
- 不把 PortSwigger 实验页面代码复制进仓库。
- 不重写 Git 历史；如果发现历史敏感信息，先停下并制定处理方案。

## README 检查

项目根 README 应包含：

```text
项目目的
30 天学习范围
合法使用边界
完成进度
代表性 Lab
Python 工具
目录结构
如何运行本地工具
我学到的内容
```

## 隐私与秘密检查

运行搜索并逐条人工判断：

```bash
rg -n --hidden -i "cookie:|authorization:|password|api[_-]?key|token|session" Cybersecurity/AI-Hacker-Roadmap
```

文档中的教学词语不一定是泄露；重点检查它们后面是否存在真实值。

检查：

- [x] 公网 IP：未发现。
- [x] Cookie 与 Session 值：未发现真实值；证据文件只保留 `[redacted]` 或摘要。
- [x] Token、密码、API key：已移除 Day 07 中的实验临时密码；未发现 Token 或 API key。
- [x] 实验实例域名或 ID：未保留临时实验实例域名或 ID。
- [x] 真实姓名、邮箱、学校信息：未发现。
- [x] 无意提交的大文件：未发现；课程图片只保留必要的已脱敏截图。

## 项目质量检查

- [x] Day 文件编号完整：Day01–Day30 都存在。
- [x] 所有内部链接有效：已检查项目内 Markdown 相对链接。
- [x] Markdown 标题清楚：项目首页、作品集和每日文件均使用层级标题。
- [x] 截图有说明并已脱敏：Day 14 截图与证据文件不含会话值或临时实验地址。
- [x] Python 代码可以运行：已通过 Python 编译检查，并运行 Day 25 本地验证脚本。
- [x] `requirements.txt` 存在：`Scripts/requirements.txt` 已列出 `requests`。
- [x] `.venv/` 没有进入 Git：`.gitignore` 已忽略，Git 追踪列表中没有虚拟环境文件。
- [x] `git status` 只显示预期改动：仅包括 Day 29 的项目整理文件与脱敏修订。

## 作品集摘要

创建：

```text
PORTFOLIO.md
```

包含三个部分：

```text
我完成了什么
我能解释什么
我下一步要学习什么
```

## Git Commit

确认没有敏感内容后：

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Polish AI hacker roadmap portfolio"
```

是否推送或公开仓库由你之后单独决定。

## 本次整理结果

- 已更新项目首页 [README.md](../README.md)，使进度、范围、工具和安全边界与当前学习状态一致。
- 已创建 [PORTFOLIO.md](../PORTFOLIO.md)，用简短语言说明完成内容、可解释内容和下一步计划。
- 已检查常见敏感字段的搜索结果。教学文字会出现 `Cookie`、`Session` 和 `password` 等词；人工检查后没有保留真实会话值、个人信息或实验临时地址。
- 已移除 Day 07 中原本写下的实验临时登录凭据，因此今后公开项目时不需要上传账号或密码。

本日完成后，保留本地修改供自己检查；是否 Git commit、推送或公开，由项目拥有者单独决定。

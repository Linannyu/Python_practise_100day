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

- [ ] 公网 IP
- [ ] Cookie 与 Session 值
- [ ] Token、密码、API key
- [ ] 实验实例域名或 ID
- [ ] 真实姓名、邮箱、学校信息
- [ ] 无意提交的大文件

## 项目质量检查

- [ ] Day 文件编号完整
- [ ] 所有内部链接有效
- [ ] Markdown 标题清楚
- [ ] 截图有说明并已脱敏
- [ ] Python 代码可以运行
- [ ] `requirements.txt` 存在
- [ ] `.venv/` 没有进入 Git
- [ ] `git status` 只显示预期改动

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


# Day 18 — 批量检查本地授权页面

## Mission

启动自己的本地网站，让 Python 脚本依次请求三个固定页面，并使用允许列表阻止范围外主机。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：30–45 分钟

## 安全范围

脚本今天只能访问：

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/about.html
http://127.0.0.1:8000/missing.html
```

不要把列表替换成其他网站。

## Step 1 — 准备两个终端

在 VS Code 中打开两个终端：

- 终端 A：运行本地网站，运行后保持不动。
- 终端 B：运行检查脚本。

可以点击终端面板右上角的 `+` 新建第二个终端。

## Step 2 — 在终端 A 启动本地网站

从工作区根目录运行：

```bash
cd Cybersecurity/AI-Hacker-Roadmap/Labs/LocalHTTP
python3 -m http.server 8000
```

正常情况下会看到类似：

```text
Serving HTTP on 0.0.0.0 port 8000
```

这个终端会持续运行，不是卡死。暂时不要按 `Control + C`。

## Step 3 — 在终端 B 修改脚本

进入项目并启用环境：

```bash
cd Cybersecurity/AI-Hacker-Roadmap
source .venv/bin/activate
```

在 `Scripts/http_inspector.py` 中加入 URL 列表和主机检查。可以先把 Day 15–16 的单个 `url` 代码改成：

```python
from urllib.parse import urlparse

import requests

ALLOWED_HOSTS = {"127.0.0.1", "localhost"}

urls = [
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/about.html",
    "http://127.0.0.1:8000/missing.html",
]

for url in urls:
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        print(url, "| Blocked by allowlist")
        continue

    response = requests.get(url, timeout=10)
    content_type = response.headers.get("Content-Type", "(missing)")
    body_bytes = len(response.content)
    print(url, "|", response.status_code, "|", content_type, "|", body_bytes)
```

`continue` 的意思是：当前 URL 被阻止后，直接进入下一次循环，不执行下面的请求。

## Step 4 — 运行并记录

在终端 B 运行：

```bash
python Scripts/http_inspector.py
```

预期关系：

| 页面 | 预期状态码 | 原因 |
|---|---:|---|
| `/` | 200 | `index.html` 存在 |
| `/about.html` | 200 | 文件存在 |
| `/missing.html` | 404 | 这个文件故意不存在 |

Content-Type 和字节数记录实际输出，不要求固定数字。

## Step 5 — 验证允许列表真的工作

临时在 `urls` 最后增加一个不会被发送的测试字符串：

```python
"https://example.com/",
```

重新运行，应该只看到：

```text
https://example.com/ | Blocked by allowlist
```

它不应该输出状态码。验证后删除这行，让最终列表仍只包含三个本地 URL。

## Step 6 — 停止本地网站

回到终端 A，按：

```text
Control + C
```

看到终端重新出现提示符，才表示服务器已停止。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `Address already in use` | 8000 端口已有程序使用 | 找到之前运行服务器的终端并按 `Control + C` |
| 三个页面都连接失败 | 本地服务器没启动或已停止 | 在终端 A 重新运行服务器 |
| `/` 返回 404 | 服务器从错误目录启动 | 终端 A 必须位于 `Labs/LocalHTTP` |
| `NameError: urlparse` | 忘记导入 | 添加 `from urllib.parse import urlparse` |
| example.com 仍被请求 | 阻止判断放在请求之后 | 必须先检查 host，再调用 `requests.get` |
| 终端 A 无法输入命令 | 服务器正在前台运行 | 这是正常状态；用终端 B 执行脚本 |

## 成功标准

- [ ] 本地服务器成功启动
- [ ] `/` 与 `/about.html` 返回 `200`
- [ ] `/missing.html` 返回 `404`
- [ ] 非本地主机会在请求前被 allowlist 阻止
- [ ] 完成后停止本地服务器

## 操作记录

| URL | 状态码 | Content-Type | Bytes |
|---|---:|---|---:|
| `/` |  |  |  |
| `/about.html` |  |  |  |
| `/missing.html` |  |  |  |

## 思考题

为什么课程工具要设置允许列表，而不是接受任意目标？

提示：允许列表不仅是文字提醒，而是在发送请求前执行的代码限制。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 18: inspect local pages"
```

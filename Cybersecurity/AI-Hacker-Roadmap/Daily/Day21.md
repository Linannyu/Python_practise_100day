# Day 21 — 完成第一个安全辅助工具

## Mission

把 Week 3 的代码整理成可以重复运行和展示的 `Local HTTP Inspector`。

## 难度与时间

- 难度：⭐⭐⭐⭐☆
- 核心任务：45–75 分钟

## 工具范围

工具只允许：

```text
localhost
127.0.0.1
postman-echo.com
```

不实现端口扫描、目录爆破、登录尝试或任意目标批量请求。

## 完成后的用法

```bash
python Scripts/http_inspector.py \
  http://127.0.0.1:8000/ \
  http://127.0.0.1:8000/about.html \
  --output Scripts/output/report.json
```

先不要直接复制全部功能。按下面顺序逐段完成，每完成一段就运行一次。

## Step 1 — 整理导入和固定配置

脚本顶部应包含 Week 3 已用到的模块：

```python
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
```

然后设置：

```python
ALLOWED_HOSTS = {"localhost", "127.0.0.1", "postman-echo.com"}
TIMEOUT_SECONDS = 10
```

固定配置集中放置，后面更容易检查范围。

## Step 2 — 保留摘要函数

使用 Day 19 的思路，让函数只提取：

```text
url
status
content_type
bytes
sha256
```

不要把 Cookie、Authorization、完整请求头或完整正文加入输出。

## Step 3 — 加入命令行参数

建立解析函数：

```python
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Inspect allowlisted HTTP URLs."
    )
    parser.add_argument("urls", nargs="+", help="One or more URLs to inspect")
    parser.add_argument("--output", help="Optional JSON output path")
    return parser.parse_args()
```

逐项理解：

| 内容 | 作用 |
|---|---|
| `"urls"` | 位置参数，命令中直接写 URL |
| `nargs="+"` | 至少需要一个 URL，也允许多个 |
| `--output` | 可选参数；不写就只打印，不保存 |

先运行：

```bash
python Scripts/http_inspector.py --help
```

应看到工具说明，而不是发送请求。

## Step 4 — 请求前检查主机

对每个 URL：

1. 使用 `urlparse(url).hostname` 取得主机。
2. 如果不在 `ALLOWED_HOSTS`，打印 `Blocked by allowlist`。
3. 被阻止后直接处理下一个 URL。
4. 只有通过检查，才调用 `requests.get(..., timeout=TIMEOUT_SECONDS)`。

注意顺序：先检查，后请求。

## Step 5 — 友好处理单个失败

把单次请求放进：

```python
try:
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
except requests.RequestException as error:
    print(url, "| Request failed:", error)
    continue
```

这样一个页面失败时，后面的页面仍可继续。不要用空的 `except:` 隐藏所有错误。

## Step 6 — 可选保存 JSON

只有用户写了 `--output` 时才保存：

```python
if args.output:
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
```

报告继续包含：

```text
generated_at
scope
results
```

写完后打印保存位置。

## Step 7 — 按顺序自测

先启动本地服务器：

```bash
cd Cybersecurity/AI-Hacker-Roadmap/Labs/LocalHTTP
python3 -m http.server 8000
```

在另一个终端从项目根目录逐条运行：

1. 查看帮助：

```bash
python Scripts/http_inspector.py --help
```

2. 正常 `200`：

```bash
python Scripts/http_inspector.py http://127.0.0.1:8000/
```

3. 正常处理 `404`：

```bash
python Scripts/http_inspector.py http://127.0.0.1:8000/missing.html
```

4. 验证阻止范围外主机：

```bash
python Scripts/http_inspector.py https://example.com/
```

这里应显示 `Blocked by allowlist`，不应显示服务器状态码。

5. 保存 JSON：

```bash
python Scripts/http_inspector.py \
  http://127.0.0.1:8000/ \
  http://127.0.0.1:8000/about.html \
  --output Scripts/output/report.json
```

6. 验证 JSON：

```bash
python3 -m json.tool Scripts/output/report.json
```

7. 停止本地服务器后，再运行本地 URL，确认它显示友好连接错误，而不是整段 Python traceback。

## Step 8 — 整理说明文件

最终目录应逐步形成：

```text
Scripts/
├── http_inspector.py
├── url_parser.py
├── requirements.txt
├── README.md
└── output/
```

在 `Scripts/requirements.txt` 写：

```text
requests
```

更新 `Scripts/README.md`，用自己的话填写：

```text
用途
安全范围
安装
运行示例
输出字段
已知限制
```

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `urls` 属性不存在 | 忘记调用 `parse_arguments()` | 添加 `args = parse_arguments()` |
| 一个请求失败后全部停止 | 没有在循环内部捕获请求异常 | 把 `try/except` 放到单个 URL 的循环里 |
| example.com 得到状态码 | allowlist 检查发生得太晚 | 在 `requests.get` 前检查 |
| `--output` 被当成 URL | argparse 参数或命令顺序写错 | 对照目标用法检查 |
| 输出文件包含旧数据 | 写入逻辑使用追加 | 每次生成完整新报告并用 `"w"` |
| 测试连接失败却出现长 traceback | 没捕获 `requests.RequestException` | 只捕获 requests 的网络异常并打印 |

## 必须功能

- [ ] 接受一个或多个 URL
- [ ] 使用 allowlist 阻止其他主机
- [ ] 每个请求设置 `timeout`
- [ ] 输出状态码、Content-Type、字节数和 SHA-256 摘要
- [ ] 可选保存 JSON
- [ ] 单个请求失败时给出友好错误，不让整个程序崩溃

## 自测记录

```text
--help 能显示说明：
允许 localhost：
阻止 example.com：
正常处理 200：
正常处理 404：
服务器关闭时显示友好错误：
JSON 可以解析：
```

## 展示说明

用 3–5 句话说明：

```text
我解决了什么问题：
为什么设置 allowlist：
工具如何比较响应：
我学到了什么：
下一步可以改进什么：
```

## Git Commit

先检查输出文件没有敏感信息，再运行：

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete week 3 local HTTP inspector"
```

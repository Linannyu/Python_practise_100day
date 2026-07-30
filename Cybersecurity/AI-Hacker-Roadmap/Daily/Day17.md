# Day 17 — 用 Python 解析 URL 参数

## Mission

使用 Python 标准库 `urllib.parse`，把 URL 拆成协议、主机、端口、路径、原始查询字符串和查询参数。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：25–40 分钟

## 安全范围

今天只解析写在代码里的字符串，不发送任何网络请求。

## Step 1 — 创建文件

1. 在 VS Code 左侧展开 `Scripts`。
2. 新建 `url_parser.py`。
3. 输入：

```python
from urllib.parse import parse_qs, urlparse


def parse_url(url: str) -> dict:
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "host": parsed.hostname,
        "port": parsed.port,
        "path": parsed.path,
        "query": parsed.query,
        "parameters": parse_qs(parsed.query),
    }


test_url = "https://postman-echo.com/get?name=lin&day=17&topic=url"
result = parse_url(test_url)
print(result)
```

逐段理解：

| 代码 | 作用 |
|---|---|
| `urlparse(url)` | 按 URL 规则拆分字符串 |
| `parsed.scheme` | 协议，例如 `https` |
| `parsed.hostname` | 主机名，不包含端口 |
| `parsed.port` | 明确写出的端口；没写时是 `None` |
| `parsed.path` | 主机后、`?` 前的路径 |
| `parsed.query` | `?` 后面的原始查询字符串 |
| `parse_qs(...)` | 把查询字符串解析成字典 |

## Step 2 — 运行第一个测试

在项目根目录运行：

```bash
python3 Scripts/url_parser.py
```

在输出中确认：

```text
scheme = https
host = postman-echo.com
port = None
path = /get
name = ['lin']
day = ['17']
topic = ['url']
```

实际输出会是 Python 字典形式。`parse_qs` 的值是列表，因此会看到 `['lin']`，不是单独的 `lin`。

## Step 3 — 测试明确端口

把 `test_url` 改成：

```text
http://127.0.0.1:8000/about.html
```

保存并运行。重点记录：

```text
scheme = http
host = 127.0.0.1
port = 8000
path = /about.html
parameters = {}
```

没有 `?`，所以参数字典为空。

## Step 4 — 测试重复参数

把 `test_url` 改成：

```text
https://postman-echo.com/get?tag=a&tag=b
```

保存并运行。重点观察：

```text
'parameters': {'tag': ['a', 'b']}
```

两个同名参数没有互相覆盖，而是保存在同一个列表里。

## Step 5 — 恢复第一个测试 URL

完成记录后，把代码中的 `test_url` 恢复为：

```text
https://postman-echo.com/get?name=lin&day=17&topic=url
```

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `SyntaxError` | 引号、逗号或括号缺失 | 对照代码逐行检查 |
| `port` 显示 `None` | URL 没有明确写端口 | 这是正常结果 |
| 参数值外面有 `[]` | `parse_qs` 支持同名参数重复 | 不要手动删除列表 |
| `parameters` 是空字典 | URL 没有查询字符串 | 检查是否有 `?name=...` |
| 试图用 `split("?")` | 手写拆分容易漏掉 URL 规则 | 保留 `urlparse` 和 `parse_qs` |

## 成功标准

- [ ] 能拆分协议、主机、端口、路径
- [ ] 能使用 `parse_qs`
- [ ] 完成三个测试 URL
- [ ] 能解释为什么参数值是列表
- [ ] 没有发送网络请求

## 操作记录

```text
第一个 URL 的解析结果：
本地 URL 的端口：
重复 tag 参数的结果：
为什么使用标准库：
```

## 思考题

为什么 `https://example.test:8443/a` 的主机和端口要分开保存？

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 17: build a URL parser"
```

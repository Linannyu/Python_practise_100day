# Day 15 — 用 requests 发送 HTTP 请求

## Mission

创建 `Scripts/http_inspector.py`，使用 Python `requests` 发送一个 GET 请求，并把请求方法、最终 URL 和响应状态码打印出来。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：25–40 分钟

## 安全范围

今天脚本只允许访问：

```text
https://postman-echo.com/get?day=15
```

不要把地址换成真实登录页面、学校系统或其他未授权网站。

## 开始前先确认位置

1. 在 VS Code 左侧找到 `AI-Hacker-Roadmap`。
2. 打开 VS Code 顶部菜单 `Terminal` → `New Terminal`。
3. 在终端运行：

```bash
cd Cybersecurity/AI-Hacker-Roadmap
pwd
```

`pwd` 的最后一段应该是：

```text
AI-Hacker-Roadmap
```

如果已经在这个目录，不需要重复切换。

## Step 1 — 创建独立 Python 环境

依次运行，上一条完成后再运行下一条：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
```

看到终端提示符前出现 `(.venv)`，说明环境已经启用。`.venv/` 已被 `.gitignore` 排除，不需要手动上传。

确认版本：

```bash
python --version
python -m pip show requests
```

记录 `Version:` 后面的数字，不需要记录安装路径。

## Step 2 — 创建脚本

1. 在 VS Code 左侧展开 `Scripts`。
2. 新建文件 `http_inspector.py`。
3. 输入：

```python
import requests

url = "https://postman-echo.com/get?day=15"
response = requests.get(url, timeout=10)

print("Method:", response.request.method)
print("URL:", response.url)
print("Status:", response.status_code)
```

逐行理解：

| 代码 | 作用 |
|---|---|
| `import requests` | 导入用于发送 HTTP 请求的库 |
| `url = ...` | 把今天允许访问的地址保存到变量 |
| `requests.get(...)` | 发送 GET 请求，并等待响应 |
| `timeout=10` | 最多等待 10 秒，避免程序无限卡住 |
| `response.request.method` | 读取实际发送的方法 |
| `response.url` | 读取最终请求 URL |
| `response.status_code` | 读取服务器返回的状态码 |

注意：变量名 `response` 代表收到的响应，不是请求正文。

## Step 3 — 保存并运行

1. 按 `Command + S` 保存。
2. 确认终端仍显示 `(.venv)`。
3. 在项目根目录运行：

```bash
python Scripts/http_inspector.py
```

结果应类似：

```text
Method: GET
URL: https://postman-echo.com/get?day=15
Status: 200
```

URL 的显示形式可能有小差异，但方法应为 `GET`，正常情况下状态码应为 `200`。

## Step 4 — 对照已经学过的 HTTP

在代码旁用自己的话指出：

```text
Request：requests.get(...) 发出的内容
Response：变量 response 保存的服务器响应
状态码：response.status_code
查询参数：URL 中 ? 后面的 day=15
```

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `No module named 'requests'` | 虚拟环境未启用，或没有安装 | 运行 `source .venv/bin/activate`，再运行安装命令 |
| `python: command not found` | 当前环境只提供 `python3` | 先启用 `.venv`；仍不行就用 `python3` |
| 等待后出现 timeout | 网络或服务暂时不可用 | 保留代码，稍后重试；不要删除 `timeout` |
| 证书相关错误 | 本机证书或代理设置影响连接 | 记录完整错误，不要使用 `verify=False` 绕过 |
| 状态码不是 200 | 服务暂时变化 | 记录实际状态码，不要伪造作业结果 |

## 成功标准

- [x] `requests` 成功导入
- [x] 请求设置了超时
- [x] 输出方法、URL 和状态码
- [x] 正常情况下状态码为 `200`
- [x] 能指出 URL 中的查询参数

## 操作记录

```text
Python 版本：3.14.3
requests 版本：2.34.2
Method：GET
URL：https://postman-echo.com/get?day=15
Status：200
我遇到的问题：No problem
```

## 思考题

为什么网络请求应该设置 `timeout`，而不是无限等待？

提示：想一想服务器没有回应时，程序是否还能继续执行。

```text
因为服务器、网络或域名解析可能暂时没有回应。如果不设置 timeout，程序可能一直停在等待请求的位置，后面的代码无法继续运行。设置 timeout=10后，请求等待超过限制就会报告异常，让程序有机会停止、提示错误或继续处理其他任务，而不是无限等待。
```

## 今日一句话总结

```text
今天我学会了：requests.get() 可以发送 GET 请求，response 保存服务器返回的响应；网络请求应设置 timeout，并通过 response.status_code 检查实际状态码。这个 URL 的查询参数是 ? 后面的 day=15。
```

## Git Commit

确认脚本中没有 Cookie、Token 或密码后再运行：

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 15: send a request with Python"
```

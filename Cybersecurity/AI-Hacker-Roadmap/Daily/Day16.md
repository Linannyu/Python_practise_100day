# Day 16 — 读取状态码和响应头

## Mission

扩展 Day 15 的 `http_inspector.py`，读取状态码、响应头和响应正文大小，并比较一次 `200` 和一次 `404`。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：20–35 分钟

## 安全范围

只访问：

```text
https://postman-echo.com/get?day=16
https://postman-echo.com/test
```

## 开始前检查

在 VS Code 打开终端，进入项目并启用 Day 15 的环境：

```bash
cd Cybersecurity/AI-Hacker-Roadmap
source .venv/bin/activate
```

运行 Day 15 脚本，确认它仍能工作：

```bash
python Scripts/http_inspector.py
```

如果这里失败，先按 Day 15 的常见问题修复，不要一边报错一边继续加代码。

## Step 1 — 增加响应信息

打开 `Scripts/http_inspector.py`，在现有三个 `print` 后增加：

```python
content_type = response.headers.get("Content-Type", "(missing)")
server = response.headers.get("Server", "(missing)")
body_bytes = len(response.content)

print("Content-Type:", content_type)
print("Server:", server)
print("Body bytes:", body_bytes)
```

逐项理解：

| 内容 | 含义 |
|---|---|
| `response.headers` | 服务器返回的响应头集合 |
| `.get("Content-Type", "(missing)")` | 有这个头就取值，没有就显示 `(missing)` |
| `response.content` | 原始响应正文字节 |
| `len(...)` | 计算正文共有多少字节 |

`Server` 不是每个响应都会提供，所以显示 `(missing)` 也是有效结果。

## Step 2 — 观察 200

把 URL 确认成：

```python
url = "https://postman-echo.com/get?day=16"
```

保存后运行：

```bash
python Scripts/http_inspector.py
```

把实际的状态码、Content-Type 和 Body bytes 抄入下方表格。正文大小可能随服务返回内容变化，不需要和别人完全相同。

## Step 3 — 只改变 URL，观察 404

把代码中的 URL 临时改成：

```python
url = "https://postman-echo.com/test"
```

保存并再次运行：

```bash
python Scripts/http_inspector.py
```

预期重点：

```text
Status: 404
```

`404` 本身就是服务器返回的响应，说明请求到达了能够作出 HTTP 回应的一方；它不等于“完全没有连接到服务器”。

## Step 4 — 恢复 Day 16 地址

完成记录后，把 URL 改回：

```python
url = "https://postman-echo.com/get?day=16"
```

再运行一次，确认最终保存的版本返回正常结果。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `KeyError: 'Server'` | 使用了 `headers["Server"]` | 改用 `.get("Server", "(missing)")` |
| 两次都是 200 | 修改后没有保存，或改错了文件 | 按 `Command + S`，确认运行的是 `Scripts/http_inspector.py` |
| `Body bytes` 不同 | 响应正文内容可能变化 | 记录自己的实际值 |
| 404 被当成 Python 报错 | 混淆 HTTP 结果与程序异常 | 只要脚本正常打印，404 是有效观察 |
| 网络连接异常 | 没收到正常 HTTP 响应 | 记录异常；它与服务器返回 404 不同 |

## 成功标准

- [x] 输出 Content-Type
- [x] 输出 Server 或 `(missing)`
- [x] 输出正文大小
- [x] 分别观察并记录 `200` 和 `404`
- [x] 最终把 URL 恢复为 Day 16 地址

## 操作记录

| URL | 状态码 | Content-Type | Body bytes |
|---|---:|---|---:|
| `/get?day=16` | 200 | application/json; charset=utf-8 | 213 |
| `/test` | 404 | application/json; charset=utf-8 | 0 |

## 思考题

`404` 表示请求完全没有到达服务器吗？根据你实际收到的 HTTP 响应回答，不要只写定义。

```text
不表示。我的脚本收到了状态码 404、Content-Type 响应头和一份 0 字节的响应正文，说明请求已经到达能够返回 HTTP 响应的一方。这里的 404 表示服务器没有找到 /test 对应的资源。它与域名解析失败、连接失败或 timeout不同；那些情况通常不会得到正常的 HTTP 状态码。
```

## 今日一句话总结

```text
今天我学会了：状态码说明服务器处理请求的结果，Content-Type 描述响应正文的数据类型，Server 可能说明响应由什么服务器软件或服务处理，Body bytes 表示响应正文的字节数。404 是有效响应，不等于完全没有连接。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 16: inspect status and headers"
```

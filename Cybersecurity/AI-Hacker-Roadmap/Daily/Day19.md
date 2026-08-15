# Day 19 — 编写响应差异比较器

## Mission

比较两个本地页面的状态码、类型、大小和内容摘要，并通过一次受控修改观察哪些字段改变。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：30–45 分钟

## 安全范围

继续只使用 Day 18 的 `127.0.0.1:8000` 本地页面。

## 今日概念

- 状态码不同：服务器处理结果可能不同。
- Content-Type 不同：正文类型可能不同。
- 大小不同：内容可能改变，但它只是一条线索。
- SHA-256 摘要不同：内容字节发生了变化，但摘要不会告诉你具体改变了什么。

## Step 1 — 启动本地网站

终端 A：

```bash
cd Cybersecurity/AI-Hacker-Roadmap/Labs/LocalHTTP
python3 -m http.server 8000
```

终端 B：

```bash
cd Cybersecurity/AI-Hacker-Roadmap
source .venv/bin/activate
```

## Step 2 — 增加摘要函数

打开 `Scripts/http_inspector.py`，在顶部导入区增加：

```python
import hashlib
```

在循环之前增加：

```python
def summarize(response) -> dict:
    return {
        "status": response.status_code,
        "content_type": response.headers.get("Content-Type", "(missing)"),
        "bytes": len(response.content),
        "sha256": hashlib.sha256(response.content).hexdigest()[:12],
    }
```

这里截取摘要前 12 个字符只是为了方便显示；它仍然只用于判断内容是否变化。

## Step 3 — 获取两个基准响应

让脚本分别请求：

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/about.html
```

分别调用 `summarize()`，把结果保存成：

```python
home_summary = summarize(home_response)
about_summary = summarize(about_response)
```

然后逐项比较：

```python
for key in home_summary:
    result = "same" if home_summary[key] == about_summary[key] else "different"
    print(key, "|", home_summary[key], "|", about_summary[key], "|", result)
```

先记录这次输出，它是修改前的基准。

## Step 4 — 只修改一个本地文件

1. 打开 `Labs/LocalHTTP/about.html`。
2. 在页面正文中增加一句：

```text
Day 19 controlled change.
```

3. 保存文件。
4. 不修改 Python 脚本，不重启服务器。
5. 再次运行检查脚本。

重点观察：

```text
status 是否改变
content_type 是否改变
bytes 是否改变
sha256 是否改变
```

正常情况下，文字修改会改变 `bytes` 和 `sha256`，但不一定改变 `status` 与 `content_type`。

## Step 5 — 写出不过度的结论

合适的结论：

```text
修改 about.html 后，响应大小和摘要发生变化，证明收到的正文字节不同。
状态码仍为 200，说明请求仍成功。
仅凭摘要不同，不能说明存在漏洞。
```

不合适的结论：

```text
摘要不同，所以网站有漏洞。
```

## Step 6 — 停止服务器

完成记录后，在终端 A 按 `Control + C`。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| 摘要一直不变 | 文件未保存，或请求了另一个页面 | 保存 `about.html` 并检查 URL |
| `NameError: hashlib` | 忘记导入 | 添加 `import hashlib` |
| 比较结果只输出一次 | 循环缩进错误 | 确认 `print` 在 `for key...` 下面 |
| 两页摘要本来就不同 | 两个 HTML 文件内容本来不同 | 这是正常；受控修改前后还要分别记录 |
| 把 hash 当成加密 | 概念混淆 | 今天只把它当作内容指纹 |

## 成功标准

- [x] 生成两个响应摘要
- [x] 输出四项比较结果
- [x] 保留修改前的基准
- [x] 修改页面后大小或摘要发生变化
- [x] 能解释“不同”只是线索

## 操作记录

| 字段 | 修改前 | 修改后 | 是否不同 |
|---|---|---|---|
| status | 200 | 200 | 否 |
| content_type | text/html | text/html | 否 |
| bytes | 250 | 287 | 是 |
| sha256 | 6511fb8fd706 | b652717de789 | 是 |

**结果解释：** 修改 `about.html` 后，状态码仍然是 `200`，说明页面仍能正常返回；`Content-Type` 仍然是 `text/html`，说明正文类型没有改变。`bytes` 从 `250` 变为 `287`，SHA-256 也发生变化，说明收到的正文字节发生了变化。这些差异只能证明内容改变，不能仅凭它们判断存在漏洞。

你后来看到的 `250` 和 `6511fb8fd706`，表示页面内容又回到了修改前的版本。

## 思考题

如果 SHA-256 不同，你能仅凭这一项知道页面具体哪一行改变了吗？为什么？

**回答：** 不能。SHA-256 是根据整个响应正文计算出来的内容摘要。两个摘要不同，只能说明两份正文中至少有一些字节不同；它不会记录改变发生在哪一行，也不会显示增加、删除或替换了什么内容。要知道具体变化，还需要直接比较两份正文。

## 今日一句话总结

今天我用状态码、内容类型、字节数和 SHA-256 比较两个本地页面，并通过一次受控修改确认：字节数和摘要的变化能提示内容发生改变，但不能单独证明存在漏洞。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 19: compare HTTP responses"
```

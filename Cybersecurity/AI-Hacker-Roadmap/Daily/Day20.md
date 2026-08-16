# Day 20 — 保存测试结果

## Mission

把本地页面检查结果保存成结构清楚、可以再次读取的 JSON 文件。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：25–40 分钟

## 安全范围

只保存 Day 18–19 的本地测试数据。不要保存 Cookie、Token、密码、真实公网 IP 或响应正文。

## Step 1 — 准备结果列表

继续使用 `Scripts/http_inspector.py`。在每次本地请求完成后，把摘要和 URL 组成一个字典：

```python
item = {
    "url": url,
    "status": response.status_code,
    "content_type": response.headers.get("Content-Type", "(missing)"),
    "bytes": len(response.content),
    "sha256": hashlib.sha256(response.content).hexdigest()[:12],
}
```

在循环之前建立空列表：

```python
results = []
```

在每次得到 `item` 后加入列表：

```python
results.append(item)
```

不要把 `response.text`、请求头或 Cookie 加入结果。

## Step 2 — 组成总报告

在文件顶部增加：

```python
import json
from datetime import datetime, timezone
from pathlib import Path
```

全部请求完成后建立：

```python
report = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "scope": "localhost-only",
    "results": results,
}
```

字段含义：

| 字段 | 含义 |
|---|---|
| `generated_at` | 使用 UTC 记录生成时间 |
| `scope` | 明确报告只属于本地范围 |
| `results` | 每个页面的结果列表 |

## Step 3 — 创建目录并写入文件

继续加入：

```python
output_path = Path("Scripts/output/day20-results.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=2)

print("Saved:", output_path)
```

必须从 `AI-Hacker-Roadmap` 根目录运行脚本，这样相对路径才会保存到预期位置。

## Step 4 — 运行

1. 像 Day 18 一样先启动 `Labs/LocalHTTP` 的服务器。
2. 在第二个终端进入项目并启用 `.venv`。
3. 运行：

```bash
python Scripts/http_inspector.py
```

预期看到：

```text
Saved: Scripts/output/day20-results.json
```

然后在 VS Code 左侧打开该 JSON，确认有 `generated_at`、`scope` 和 `results`。

## Step 5 — 验证 JSON 语法

运行：

```bash
python3 -m json.tool Scripts/output/day20-results.json
```

如果终端打印格式化后的 JSON 且没有报错，说明文件语法有效。这个命令只验证 JSON 格式，不会替你判断内容是否正确。

## Step 6 — 隐私人工检查

打开生成文件，逐项确认：

- 只有 localhost 或 `127.0.0.1` URL。
- 没有 `Cookie`。
- 没有 `Authorization`。
- 没有密码、Token 或 API key。
- 没有完整响应正文。

完成后停止本地服务器。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| 找不到 JSON 文件 | 从错误目录运行，或写入代码没执行 | 回到项目根目录运行 |
| `NameError: results` | 没有在循环前建立列表 | 添加 `results = []` |
| JSON 里只有最后一项 | 循环中覆盖了变量但没 `append` | 每次使用 `results.append(item)` |
| `TypeError: ... not JSON serializable` | 放入了 response 对象等复杂对象 | 只保存示例中的字符串和数字 |
| JSON 每次追加重复内容 | 使用了追加模式 `"a"` | 使用写入模式 `"w"` |
| `json.tool` 报错 | 文件结构或写入不完整 | 先看报错行，再检查括号和写入过程 |

## 成功标准

- [x] JSON 文件成功生成
- [x] JSON 能通过 `json.tool`
- [x] 包含时间、范围和结果列表
- [x] 结果数量与实际请求数量一致
- [x] 不包含敏感信息或响应正文

## 操作记录

```text
输出文件：Scripts/output/day20-results.json
结果数量：2
scope：localhost-only
json.tool 是否通过：是
我主动排除的敏感字段：Cookie、Authorization、密码、Token、API key、请求头和完整响应正文
```

## 思考题

为什么报告中保存响应摘要比直接保存完整响应正文更适合今天的任务？

**回答：** 今天的目标是记录页面是否发生变化，而不是保存页面的全部内容。摘要比较短，可以用来判断正文字节是否改变，也能让 JSON 文件更小。完整响应正文可能很长，还可能意外包含不应该保存的信息。摘要不同只能说明内容发生变化，不能告诉我具体改变了什么，也不能单独证明存在漏洞。

## 今日一句话总结

今天我把两个本地页面的状态码、内容类型、字节数和 SHA-256 摘要保存为 JSON，并确认文件格式正确、范围只限 localhost、没有保存敏感字段或完整正文。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 20: save inspection results"
```

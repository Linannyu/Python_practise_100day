# Local HTTP Inspector

## 用途

`http_inspector.py` 用于读取允许列表中 HTTP 页面的一小段响应摘要，方便比较状态码、内容类型、大小和内容是否变化。

## 安全范围

只允许 `localhost`、`127.0.0.1` 和课程明确允许的 `postman-echo.com`。其他主机会在发送请求前显示 `Blocked by allowlist`，不会被请求。

工具不执行端口扫描、目录爆破或登录尝试，也不保存 Cookie、Authorization、密码、Token、请求头或完整响应正文。

## 安装

在 `AI-Hacker-Roadmap` 根目录启用虚拟环境后安装依赖：

```bash
source .venv/bin/activate
pip install -r Scripts/requirements.txt
```

## 运行示例

先在另一个终端启动本地课程页面：

```bash
cd Labs/LocalHTTP
python3 -m http.server 8000
```

再从项目根目录运行：

```bash
python Scripts/http_inspector.py http://127.0.0.1:8000/

python Scripts/http_inspector.py \
  http://127.0.0.1:8000/ \
  http://127.0.0.1:8000/about.html \
  --output Scripts/output/report.json
```

使用 `--help` 查看命令说明：

```bash
python Scripts/http_inspector.py --help
```

## 输出字段

- `url`：被检查的允许列表 URL。
- `status`：HTTP 状态码。
- `content_type`：响应的 Content-Type。
- `bytes`：响应正文的字节数。
- `sha256`：正文 SHA-256 摘要的前 12 个字符，只用于判断内容是否变化。

## 已知限制

- 只接受三个允许主机，不适合任意网站。
- 摘要不同只能说明内容字节不同，不能告诉你具体改了什么，也不能证明存在漏洞。
- JSON 只保存成功获得的摘要；被阻止或请求失败的 URL 只在终端显示原因。

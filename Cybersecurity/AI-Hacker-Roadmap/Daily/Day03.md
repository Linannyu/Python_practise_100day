# Day 3 — GET 与 POST

## Mission

在 Burp Repeater 中分别发送一个 GET 请求和一个 POST 请求，准确指出两种请求的数据写在什么位置。

## 难度与时间

- 难度：⭐☆☆☆☆
- 核心任务：25–40 分钟

## 安全范围

只使用 Postman 官方 Echo 服务：

```text
https://postman-echo.com/get
https://postman-echo.com/post
```

不要把练习请求发送给其他网站。

## 今天只需要理解

在今天的两个实验中：

```text
GET 数据写在 URL 查询参数中
POST 数据写在请求正文中
```

这是一种常见用法，不代表所有 GET 和 POST 永远只能这样使用。

## Part 1 — 准备 Burp

### Step 1 — 打开 Burp

确认顶部有：

```text
Proxy
Repeater
```

进入：

```text
Proxy → Intercept
```

确认按钮显示：

```text
Intercept is off
```

### Step 2 — 打开测试页面

点击 `Open browser`，访问：

```text
https://postman-echo.com/get?message=hello
```

正常结果是 JSON 页面，并且 `args` 中出现：

```json
"message": "hello"
```

## Part 2 — 观察 GET

### Step 3 — 在 HTTP history 找请求

进入：

```text
Proxy → HTTP history
```

寻找：

```text
Host：postman-echo.com
Method：GET
Path：/get?message=hello
```

不要选择 `/favicon.ico`。

右键正确请求，选择：

```text
Send to Repeater
```

### Step 4 — 保存 GET 基准

进入 `Repeater`，请求开头应类似：

```http
GET /get?message=hello HTTP/1.1
Host: postman-echo.com
```

如果显示 `HTTP/2`，不要修改协议版本。

点击 `Send`。确认：

```text
状态码：200
响应正文 args.message：hello
```

### Step 5 — 找到 GET 数据

在请求第一行中圈出：

```text
?message=hello
```

这里：

```text
message = 参数名称
hello   = 参数值
```

GET 实验没有在请求头结束后的空行下面填写正文。

## Part 3 — 建立 POST

### Step 6 — 保留 GET 标签

不要覆盖 GET 证据。可以：

```text
右键 Repeater 标签
→ Duplicate tab
```

如果没有 `Duplicate tab`，回到 HTTP history，再次 `Send to Repeater`。

把两个标签理解为：

```text
GET baseline
POST test
```

### 隐私检查 — 先删除自动 Cookie

浏览器请求可能自动包含：

```http
Cookie: ...
```

Day 3 不需要 Cookie。复制到作业、截图或笔记前，删除整行 Cookie，不要保存它的值。

`Sec-*`、`User-Agent`、`Accept`、`Priority` 等浏览器自动请求头可以保留，但为了减少干扰，也可以删除。最小请求只需要本节明确列出的结构。

### Step 7 — 修改请求方法和路径

在 POST 标签中，把第一行改为：

```http
POST /post HTTP/1.1
```

如果原来显示 `HTTP/2`，保留：

```http
POST /post HTTP/2
```

只修改方法和路径，不修改 `Host`。

### Step 8 — 设置正文类型

在请求头区域确认存在：

```http
Content-Type: application/x-www-form-urlencoded
```

如果不存在，就在 `Host` 下面添加。

这个请求头告诉服务器：正文使用表单的 `name=value` 格式。

### Step 9 — 加入空行和正文

在所有请求头下面保留一个空行，然后写：

```text
message=hello
```

结构应该是：

```http
POST /post HTTP/1.1
Host: postman-echo.com
Content-Type: application/x-www-form-urlencoded

message=hello
```

注意：

- `message=hello` 必须位于空行之后。
- 不要手动猜 `Content-Length`；让 Burp 处理。
- 不要把正文写进 URL。

### Step 10 — 发送 POST

点击 `Send`，确认：

```text
状态码：200
响应正文 form.message：hello
```

Postman Echo 通常把表单正文显示在：

```json
"form": {
  "message": "hello"
}
```

## Part 4 — 对照两个请求

| 项目 | GET 实验 | POST 实验 |
|---|---|---|
| 方法 | `GET` | `POST` |
| 路径 | `/get` | `/post` |
| 数据位置 | URL 的 `?` 后面 | 空行后的请求正文 |
| Content-Type | 本实验不依赖表单正文类型 | `application/x-www-form-urlencoded` |
| 回显位置 | `args` | `form` |

## 常见错误与处理

| 现象 | 常见原因 | 处理 |
|---|---|---|
| POST 返回 404 | 路径仍是 `/get` 或写错 `/post` | 检查第一行 |
| `form` 是空的 | 正文写在空行前面 | 把 `message=hello` 移到空行之后 |
| 数据出现在 `args` | 仍把数据写在 URL 中 | POST 路径只保留 `/post` |
| 请求一直等待 | Intercept 开着 | 切换到 `Intercept is off` |
| 找不到请求 | 选错 Host 或历史记录太多 | 过滤 `postman-echo.com` |

## 成功标准

- [x] GET 返回 `200`
- [x] GET 的 `args.message` 是 `hello`
- [x] POST 返回 `200`
- [x] POST 的 `form.message` 是 `hello`
- [x] 能指出 POST 请求头与正文之间的空行
- [x] 能用一句话说明本实验中 GET 与 POST 的数据位置

## 操作记录

```text
GET 请求第一行：
GET /get?message=hello HTTP/2
GET 数据写在：
路径的?后面
GET 响应中的回显位置：
"args":{"message":"hello"}
POST 请求第一行：
POST /post HTTP/2
POST 的 Content-Type：
Content-Type: application/x-www-form-urlencoded
POST 数据写在：
请求体，请求头的空行下面。
POST 响应中的回显位置：
"form":{"message":"hello"},
我最容易混淆的地方：
get的请求数据写在link里面，post的请求数据写在请求体里面
我遇到的问题：没有
```

## 思考题

```text
1. POST 正文为什么不能写在请求头区域？
正文写在请求头区域时，不会自动进入 args 或 form；空行是协议用来分隔“请求头”和“请求正文”的边界。写在空行上面可能被当成格式错误的请求头。只有写在空行下面，并配合正确 Content-Type，这里才会被解析进 form。

2. Content-Type 在本实验中描述的是哪部分数据？
Content-Type: application/x-www-form-urlencoded 描述的是请求正文格式，表示正文采用 name=value&name2=value2 的表单形式。

3. 为什么不能只看到 POST 就断定请求一定会修改服务器数据？
POST 只是请求方法，不保证服务器一定保存或修改数据。是否改变状态取决于服务器端 /post 的处理逻辑；这次 Echo 服务只是把内容回显给你。

```

## 今日一句话总结

```text
今天我学会了：GET 实验把参数放在 URL 中；POST 实验把表单数据放在空行后的请求正文中，Content-Type 告诉服务器如何解析正文。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 3: compare GET and POST"
```

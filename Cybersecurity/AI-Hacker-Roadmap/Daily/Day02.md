# Day 2 — URL、参数、请求头与响应

## Mission

使用 Burp Suite Repeater 拆解一个 HTTP 请求，分清 URL、参数、请求头和响应，并通过两次受控修改观察差别。

## 难度与时间

- 难度：⭐☆☆☆☆
- 核心任务：25–40 分钟

## 先解释你看到的 503

```text
503 Service Unavailable
```

它表示：

```text
你的请求已经到达服务器
→ 服务器目前无法处理请求
→ 服务器返回 503
```

这通常是测试服务临时维护、负载过高或发生故障，不代表你的 Burp 操作错误。

请不要快速连续点击 `Send`。Day 2 不再依赖当前返回 503 的 httpbin，改用 Postman 官方的 Echo API：

```text
https://postman-echo.com/get?name=lin&day=2
```

Postman Echo 会把收到的参数和请求头放进 JSON 响应，学习目标与 httpbin 相同。

## 安全范围

今天只允许使用：

```text
https://postman-echo.com/get
```

如果它也临时不可用，可以使用项目提供的本地备用服务：

```text
Labs/EchoServer/server.py
```

不要把练习步骤用于未授权网站。

## 核心目标

- [x] 能指出 URL 中的协议、主机、路径和查询字符串
- [x] 能区分参数与请求头
- [x] 能在响应中找到状态码、响应头和响应正文
- [x] 每次只修改一个位置
- [x] 能说明请求变化如何对应到响应变化

## Part 1 — 准备 Burp

### Step 1 — 打开 Burp Suite

如果 Burp 已经打开，直接进入下一步。

确认顶部能够看到：

```text
Dashboard
Target
Proxy
Repeater
```

### Step 2 — 让 Intercept 保持关闭

依次进入：

```text
Proxy
→ Intercept
```

按钮应该显示：

```text
Intercept is off
```

今天主要使用 `HTTP history`，不需要让请求停在 Intercept 中。

如果显示 `Intercept is on`，点击一次把它关闭。否则浏览器页面可能一直等待，因为请求被 Burp 暂停了。

### Step 3 — 打开 Burp 自带浏览器

点击：

```text
Proxy
→ Intercept
→ Open browser
```

继续使用 Burp 自带浏览器，不需要配置 Safari 或 Chrome。

## Part 2 — 产生一个基准请求

### Step 4 — 访问测试地址

在 Burp 浏览器的地址栏完整输入：

```text
https://postman-echo.com/get?name=lin&day=2
```

按 Enter。

正常情况下，页面会显示一段 JSON。JSON 可能挤在一行，也可能已经格式化；两种情况都没关系。

你应该能在页面中找到类似：

```json
"args": {
  "name": "lin",
  "day": "2"
}
```

字段顺序可能不同。

### Step 5 — 如果浏览器没有正常显示

根据现象处理：

| 现象 | 含义 | 处理 |
|---|---|---|
| 页面一直加载 | 请求可能停在 Intercept | 返回 Burp，确认 `Intercept is off` |
| `503 Service Unavailable` | Echo 服务暂时不可用 | 不连续重试，使用本文最后的本地备用路线 |
| `Cannot connect` 或超时 | 网络或地址问题 | 检查网络和 URL 是否完整 |
| 出现 JSON | 请求成功 | 继续下一步 |

## Part 3 — 在 HTTP history 中找到请求

### Step 6 — 打开历史记录

返回 Burp：

```text
Proxy
→ HTTP history
```

这里会出现很多浏览器请求。寻找满足以下条件的一行：

```text
Host：postman-echo.com
Method：GET
URL：/get?name=lin&day=2
```

不要误选：

```text
/favicon.ico
浏览器更新请求
其他网站的请求
```

如果请求太多，可以在过滤器中只显示：

```text
postman-echo.com
```

### Step 7 — 查看请求和响应

单击正确的历史记录。

下方或右侧通常会分成：

```text
Request
Response
```

先不要修改，确认：

- Request 中能找到 `name=lin&day=2`
- Response 状态码是 `200`
- Response body 中能找到 `args`

## Part 4 — 发送到 Repeater

### Step 8 — Send to Repeater

右键正确的 HTTP history 记录，选择：

```text
Send to Repeater
```

然后点击顶部：

```text
Repeater
```

你会看到一个新的 Repeater 标签。

### Step 9 — 确认基准请求

请求开头可能类似：

```http
GET /get?name=lin&day=2 HTTP/1.1
Host: postman-echo.com
```

也可能显示 `HTTP/2`。协议版本由 Burp 和服务器协商，今天不要修改它。

向下查看，你还会看到多行请求头，例如：

```http
Accept-Language: en-US,en;q=0.9
User-Agent: ...
Accept: ...
```

请求头结束后有一个空行。这个 GET 请求在空行后没有请求正文。

### Step 10 — 发送基准请求

在完全不修改的情况下，先点击一次：

```text
Send
```

这是基准请求。确认：

```text
状态码：200
args.name：lin
args.day：2
```

如果这里仍然是 `503`，不是参数错误，直接使用本文最后的本地备用路线。

## Part 5 — 拆解 URL

完整 URL：

```text
https://postman-echo.com/get?name=lin&day=2
```

把它拆成：

```text
协议：https
主机：postman-echo.com
路径：/get
查询字符串：name=lin&day=2
参数 1：name=lin
参数 2：day=2
```

符号含义：

```text
://  分隔协议与后面的地址
/    开始路径
?    开始查询字符串
=    分隔参数名称与参数值
&    分隔两个参数
```

## Part 6 — 第一次受控修改：参数

### Step 11 — 只修改 day

找到：

```text
day=2
```

只把它改成：

```text
day=second
```

请求行应类似：

```http
GET /get?name=lin&day=second HTTP/1.1
```

不要同时修改其他参数或请求头。

### Step 12 — 再次发送

点击 `Send`，在响应正文的 `args` 中寻找：

```json
"name": "lin",
"day": "second"
```

你应该观察到：

```text
name 没变
day 从 2 变成 second
```

这说明服务器读取了新的 URL 参数。

## Part 7 — 第二次受控修改：请求头

### Step 13 — 找到 Accept-Language

在请求头中寻找类似：

```http
Accept-Language: en-US,en;q=0.9
```

把整行改成：

```http
Accept-Language: zh-CN
```

如果原请求中没有 `Accept-Language`，就在 `Host` 后面新加这一行。

不要把它写在请求的最后一个空行之后；它必须位于请求头区域。

### Step 14 — 发送并寻找回显

点击 `Send`，在响应正文的 `headers` 部分寻找：

```json
"accept-language": "zh-CN"
```

服务可能把请求头名称显示成小写，也可能显示成：

```json
"Accept-Language": "zh-CN"
```

HTTP 请求头名称不区分大小写，因此两种显示都算成功。

## Part 8 — 区分参数与请求头

今天的请求中：

```text
name 和 day：
位于 URL 的 ? 后面
属于查询参数

Accept-Language：
位于请求行下面、空行上面
属于请求头
```

它们都会发送给服务器，但位置和用途不同。

## 成功标准

- [x] Burp 浏览器成功打开 Postman Echo
- [x] HTTP history 中找到正确 GET 请求
- [x] 请求成功发送到 Repeater
- [x] 基准响应状态是 `200`
- [x] `args` 中出现 `name=lin` 和 `day=2`
- [x] 修改后 `day` 变成 `second`
- [x] `headers` 中出现 `Accept-Language: zh-CN`
- [x] 能自己拆解 URL

## 操作记录

完成后填写：

```text
我使用的完整 URL：https://postman-echo.com/get?name=lin&day=2

协议：https

主机：postman-echo.com

路径：/get

查询字符串：name=lin&day=2

参数 1：name=lin

参数 2：day=2

基准状态码：200

基准响应中的 name：lin

基准响应中的 day：2

我修改的参数：day=second

修改参数后的响应："args":{"name":"lin","day":"second"},

我修改的请求头：Accept-Language: zh-CN

请求头在响应中的回显："accept-language":"zh-CN"

503 是客户端问题还是服务器暂时不可用：服务器暂时不可用

我遇到的问题：出现503问题，用AI解决
```

## 思考题

用自己的话回答：

```text
1. URL 参数写在请求的什么位置？
  写在路径的？后面，用&分隔多个参数。
2. 请求头写在请求的什么位置？
  请求行下面到空行上面。
3. 修改 day 参数后，响应中的什么字段变化了？
  args里面的day的值变化了。
4. 修改 Accept-Language 后，args 会变化吗？哪个部分会变化？
  args 不会变化。响应正文中 headers 对象里的 accept-language 变成了 zh-CN。
5. 状态码 200 和 503 分别说明什么？
  状态200是成功响应，503是服务器暂时不可用。
```

## 本地备用路线

只有 Postman Echo 也不可用时才使用。

### Step A — 启动本地 Echo 服务

打开 VS Code 终端，在仓库根目录运行：

```bash
python3 Cybersecurity/AI-Hacker-Roadmap/Labs/EchoServer/server.py
```

终端显示：

```text
Day 2 Echo Server: http://127.0.0.1:8002
```

保持该终端运行。

### Step B — 在 Burp 浏览器访问

```text
http://127.0.0.1:8002/get?name=lin&day=2
```

然后重复本文的 HTTP history、Repeater、参数修改和请求头修改步骤。

本地请求应类似：

```http
GET /get?name=lin&day=2 HTTP/1.1
Host: 127.0.0.1:8002
```

完成后回到终端按：

```text
Control + C
```

停止本地服务。

## AI Prompt

```text
请只根据我粘贴的 Day 2 请求和响应，
检查我对协议、主机、路径、查询参数、请求头、状态码和响应正文的理解。
先指出正确的地方，再用零基础中文解释错误。
不要补充我没有提供的字段，不讨论未授权网站。
```

## 今日一句话总结

```text
今天我学会了：拆分 URL，区分查询参数和请求头，并通过响应正文中的回显验证自己的修改。
```

## Git Commit

完成并确认记录中没有隐私信息后，在仓库根目录运行：

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 2 of AI hacker roadmap"
```

只暂存 `AI-Hacker-Roadmap`，不要使用 `git add .`。

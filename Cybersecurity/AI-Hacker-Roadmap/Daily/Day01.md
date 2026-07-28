# Day 1 — Packet Explorer

## Mission

使用 Burp Suite 抓取一个浏览器请求，将它发送到 Repeater，修改参数后重新发送。

## 难度

⭐☆☆☆☆

## 最低时间

10–20 分钟

## 安全范围

今天只使用公开的 HTTP 测试服务：

```text
https://httpbin.org/get?name=lin
```

## 核心目标

完成以下流程：

```text
浏览器访问页面
→ Burp HTTP history 出现请求
→ Send to Repeater
→ 修改 name 参数
→ Send
→ 响应中出现修改后的值
```

## Step 1 — 打开 Burp Suite

确认界面中可以看到：

- Dashboard
- Proxy
- Repeater

今天只使用 `Proxy` 和 `Repeater`。

## Step 2 — 打开 Burp 自带浏览器

依次点击：

```text
Proxy
→ Intercept
→ Open browser
```

今天不要配置 Safari 或 Chrome 的代理。

## Step 3 — 访问测试地址

在 Burp 浏览器中访问：

```text
https://httpbin.org/get?name=lin
```

## Step 4 — 找到请求

回到 Burp：

```text
Proxy
→ HTTP history
```

寻找包含以下内容的请求：

```text
/get?name=lin
```

## Step 5 — 发送到 Repeater

右键该请求，选择：

```text
Send to Repeater
```

然后打开：

```text
Repeater
```

## Step 6 — 修改参数

找到类似下面这一行：

```http
GET /get?name=lin HTTP/1.1
```

把 `lin` 修改为：

```text
hacker
```

修改后应类似：

```http
GET /get?name=hacker HTTP/1.1
```

点击：

```text
Send
```

## 成功标准

右侧响应正文中能够找到：

```json
"name": "hacker"
```

出现这一结果，就代表 Day 1 核心任务完成。

## 今日只需要理解的概念

### Request

浏览器发送给服务器的信息。

### Response

服务器返回给浏览器的信息。

### Parameter

请求中可以改变的输入值。

在这个例子中：

```text
name=lin
```

其中：

- `name` 是参数名称
- `lin` 是参数值

## AI Prompt

完成操作后，可以向 AI 提问：

```text
请用适合零基础学生的中文，逐行解释下面这个 HTTP 请求。
不要加入我没有看到的内容，也不要直接讨论真实网站攻击。
```

然后粘贴你在 Repeater 中看到的请求。

## 任务记录

### Burp 是否成功打开？

- [x] 成功
- [ ] 失败

### HTTP history 是否看到请求？

- [x] 成功
- [ ] 失败

### 是否成功发送到 Repeater？

- [x] 成功
- [ ] 失败

### 修改后响应是否出现 hacker？

- [x] 成功
- [ ] 失败

## 我的实际结果

填写：

```text
我看到的请求：
GET /get?name=lin HTTP/1.1
Host: httpbin.org
Sec-Ch-Ua: "Not;A=Brand";v="8", "Chromium";v="150"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive



我修改的内容：GET /get?name=hacker HTTP/2

服务器返回：
HTTP/2 200 OK
Date: Tue, 28 Jul 2026 03:45:03 GMT
Content-Type: application/json
Content-Length: 952
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {
    "name": "hacker"
  }, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Host": "httpbin.org", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"macOS\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "none", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6a6825be-3cff559f62ca7dcf7587596e"
  }, 
  "origin": "[已隐藏]",
  "url": "https://httpbin.org/get?name=hacker"
}


我遇到的问题：NO Problem
```

## 今日一句话总结

填写：

```text
今天我学会了：修改发送的请求参数，可以改变服务器返回的内容。
```

## Git Commit

完成后，在仓库根目录运行：

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Start day 1 of AI hacker roadmap"
```

注意：上面的 `git add` 只暂存这个项目文件夹，不会把仓库里的其他修改一起加入。

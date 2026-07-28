# Day 2 — URL、参数、请求头与响应

## Mission

使用 Burp Suite Repeater 拆解一个 HTTP 请求，分清 URL、参数、请求头和响应，并观察两次请求之间的差别。

## 难度

⭐☆☆☆☆

## 最低时间

15–25 分钟

## 安全范围

今天继续只使用公开的 HTTP 测试服务：

```text
https://httpbin.org/get
```

不要把今天的操作用于未授权网站。

## 核心目标

- [ ] 能指出 URL 中的协议、主机、路径和查询字符串
- [ ] 能区分参数与请求头
- [ ] 能在响应中找到状态码、响应头和响应正文
- [ ] 修改一个参数并说明响应发生了什么变化

## 今天需要认识的结构

观察这个 URL：

```text
https://httpbin.org/get?name=lin&day=2
```

它可以拆成：

```text
协议：https
主机：httpbin.org
路径：/get
查询字符串：name=lin&day=2
参数 1：name=lin
参数 2：day=2
```

`?` 表示查询字符串开始，`&` 用于分隔两个参数。

## Step 1 — 打开昨天的请求

打开 Burp Suite：

```text
Proxy
→ HTTP history
→ 找到昨天发送给 httpbin.org 的请求
→ Send to Repeater
```

如果昨天的 Repeater 标签仍然存在，也可以直接继续使用。

## Step 2 — 添加第二个参数

找到请求的第一行，把路径和参数改成：

```text
/get?name=lin&day=2
```

完整请求行可能显示为：

```http
GET /get?name=lin&day=2 HTTP/1.1
```

如果你的 Burp 显示 `HTTP/2`，保留它，不需要修改协议版本。

点击：

```text
Send
```

## Step 3 — 检查参数

在响应正文中寻找：

```json
"args": {
  "day": "2",
  "name": "lin"
}
```

参数顺序可能不同，只要同时看到 `day` 和 `name` 即可。

## Step 4 — 观察一个请求头

在请求中找到：

```http
Accept-Language: en-US,en;q=0.9
```

把它改成：

```http
Accept-Language: zh-CN
```

再次点击 `Send`。

然后在响应正文的 `headers` 部分寻找：

```json
"Accept-Language": "zh-CN"
```

这一步用于观察请求头与 URL 参数的区别：

- `name` 和 `day` 位于 URL 中，是参数。
- `Accept-Language` 位于请求头中，用于补充描述这次请求。

## Step 5 — 比较两次参数

只把：

```text
day=2
```

改成：

```text
day=second
```

再次发送，观察响应正文中 `args` 的变化。

## 成功标准

完成以下检查：

- [ ] 响应状态是 `200 OK`
- [ ] 响应的 `args` 中出现 `name=lin`
- [ ] 响应的 `args` 中出现修改后的 `day` 值
- [ ] 响应的 `headers` 中出现 `Accept-Language: zh-CN`

## 操作记录

填写：

```text
我使用的完整 URL：

协议：

主机：

路径：

查询字符串：

参数：

我修改的请求头：

第一次响应中的 day：

第二次响应中的 day：

我遇到的问题：
```

## 思考题

用自己的话回答：

```text
1. 参数和请求头分别写在请求的什么位置？

2. 修改 day 参数后，响应中的什么位置发生了变化？

3. HTTP 状态码 200 表示什么？
```

## AI Prompt

完成操作后，可以向 AI 提问：

```text
请只根据我粘贴的请求和响应，检查我对 URL、参数、请求头和响应的理解。
先指出我判断正确的地方，再用适合零基础学生的中文解释错误。
不要讨论未授权网站。
```

## 今日一句话总结

填写：

```text
今天我学会了：
```

## Git Commit

完成并确认记录中没有隐私信息后，在仓库根目录运行：

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 2 of AI hacker roadmap"
```

注意：只暂存 `AI-Hacker-Roadmap` 目录，不要使用 `git add .`。

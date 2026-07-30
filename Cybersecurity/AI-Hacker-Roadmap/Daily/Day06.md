# Day 6 — 用 Repeater 做受控比较

## Mission

建立 A、B、C 三个请求，每次只改变一个位置，并用响应中的目标字段判断改动效果。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：30–45 分钟

## 安全范围

只使用：

```text
https://postman-echo.com/get
```

## 今天需要理解

如果一次改变很多位置，即使响应发生变化，也无法判断是哪一个改动造成的。

今天使用：

```text
A：基准请求
B：只修改参数
C：回到 A，只增加请求头
```

## Part 1 — 产生基准

### Step 1 — 打开测试 URL

在 Burp 浏览器访问：

```text
https://postman-echo.com/get?value=alpha
```

确认页面 JSON 的 `args.value` 是：

```text
alpha
```

### Step 2 — 发送到 Repeater

在 `Proxy → HTTP history` 找到：

```text
GET /get?value=alpha
Host: postman-echo.com
```

右键 `Send to Repeater`。

### Step 3 — 建立 A

在 Repeater 不修改，点击 `Send`。

记录：

```text
状态码
args.value
响应正文大小
```

将标签理解为 `A-baseline`。如果 Burp 支持重命名标签，可以改名；不支持也没关系。

## Part 2 — 建立 B

### Step 4 — 复制 A

复制 A 标签。不要直接覆盖 A。

方法一：

```text
右键标签 → Duplicate tab
```

方法二：

```text
回到 HTTP history → 再次 Send to Repeater
```

### Step 5 — 只修改参数

在 B 中只把：

```text
value=alpha
```

改成：

```text
value=beta
```

点击 `Send`，确认：

```text
args.value：beta
```

其他你主动控制的字段应保持不变。

## Part 3 — 建立 C

### Step 6 — 从 A 复制

C 必须从原始 A 复制，不要从 B 复制。否则 C 会同时包含 `value=beta` 和新请求头，违反“一次一个变量”。

### Step 7 — 只增加请求头

保持：

```text
value=alpha
```

在请求头区域加入：

```http
X-Learning-Day: 6
```

它必须位于空行之前。

点击 `Send`，在响应正文的 `headers` 对象中寻找：

```json
"x-learning-day": "6"
```

请求头名称可能显示为不同大小写。

## Part 4 — 正确比较

重点比较：

```text
A 与 B：args.value
A 与 C：headers.x-learning-day
```

响应长度可以记录，但不能单独作为结论。测试服务可能加入动态字段，使长度发生小变化。

## 比较表

| 请求 | 唯一改动 | 状态码 | `args.value` | `x-learning-day` | 响应长度 |
|---|---|---:|---|---|---:|
| A | 无，基准 |  |  | 不存在 |  |
| B | `alpha → beta` |  |  | 不存在 |  |
| C | 增加请求头 |  |  | `6` |  |

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| C 中 value 是 beta | C 从 B 复制 | 重新从 A 建立 C |
| 看不到新请求头 | 写在空行之后 | 移到请求头区域 |
| 三个标签混乱 | 没保留基准 | 重新建立并命名 A/B/C |
| 响应长度不同就认为有问题 | 动态字段也会影响长度 | 查看目标 JSON 字段 |
| 所有响应都一样 | 修改后没有点击 Send | 重新发送 |

## 成功标准

- [ ] A、B、C 三个请求都成功返回
- [ ] A 保持未修改
- [ ] B 只改变 `value`
- [ ] C 从 A 建立，只增加请求头
- [ ] 使用目标字段而不是只看长度
- [ ] 能解释“受控变量”

## 操作记录

```text
A 请求第一行：
A 的 args.value：

B 唯一改动：
B 的 args.value：

C 唯一改动：
C 的 headers 回显：

哪个比较证明参数变化：
哪个比较证明请求头变化：

为什么不能只看响应长度：
我遇到的问题：
```

## 思考题

```text
1. 为什么 C 必须从 A 而不是 B 复制？
2. 如果一次修改参数和请求头，结论会有什么问题？
3. “响应不同”是否自动等于“存在漏洞”？
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 6: compare requests in Repeater"
```


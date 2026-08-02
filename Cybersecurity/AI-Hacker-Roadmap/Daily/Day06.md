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
| A | 无，基准 | 待记录 | `alpha` | 不存在 | 待记录 |
| B | `alpha → beta` | 待记录 | `beta` | 不存在 | 待记录 |
| C | 增加请求头 | 待记录 | `alpha` | `6` | 待记录 |

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
A 请求第一行：GET /get?value=alpha（协议版本未记录）
A 的 args.value："args":{"value":"alpha"}

B 唯一改动：value=beta
B 的 args.value："args":{"value":"beta"}

C 唯一改动：请求头添加了 X-Learning-Day: 6
C 的 headers 回显："headers":{"x-learning-day":"6"}

哪个比较证明参数变化：比较 A 和 B。两者只改变 value，响应中的
args.value 也从 alpha 变成 beta。

哪个比较证明请求头变化：比较 A 和 C。两者的 value 都是 alpha，
C 只增加 X-Learning-Day: 6，响应中也只出现对应的请求头回显。

为什么不能只看响应长度：响应长度只表示正文有多少字节，不能说明具体
哪个字段改变，也不能证明变化由哪个输入造成；动态字段也可能影响长度。

我遇到的问题：没有
```

## 思考题

```text
1. 为什么 C 必须从 A 而不是 B 复制？
因为 A 是没有修改的基准。从 A 建立 C，C 就只比 A 多一个请求头。
如果从 B 复制，C 会同时保留 value=beta 和新增请求头，一次改变两个变量。

2. 如果一次修改参数和请求头，结论会有什么问题？
如果响应发生变化，就无法判断变化是参数造成的、请求头造成的，还是两者共同造成的，因此不能得到清楚的因果结论。

3. “响应不同”是否自动等于“存在漏洞”？
不等于。响应不同只说明服务器对两个输入作出了不同回应，还要结合功能、预期行为和实际安全影响继续验证。本实验的 Echo 服务本来就会回显输入，所以这里的差异是预期结果，不是漏洞证据。
```

## 今日一句话总结

```text
今天我学会了：受控比较需要保留一个基准，每次只改变一个变量，再检查对应的目标字段。响应出现差异只是一条观察结果，不会自动证明存在漏洞。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 6: compare requests in Repeater"
```

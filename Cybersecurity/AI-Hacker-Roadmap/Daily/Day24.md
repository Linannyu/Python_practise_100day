# Day 24 — 让 AI 提出可验证假设

## Mission

把“这里可能有问题”改写成范围明确、一次只改一个变量、结果能够支持或否定的测试假设。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：30–45 分钟

## 安全范围

今天只设计针对下列本地材料的测试，不执行网络攻击：

```text
Labs/CodeReview/profile_app.py
Labs/LocalHTTP/
```

## 什么是可验证假设

一个完整假设必须回答：

```text
基准输入是什么？
只改变哪个输入？
根据哪一行代码，程序可能发生什么？
我要观察哪个输出？
什么结果支持假设？
什么结果否定或限制假设？
测试范围在哪里？
```

示例结构：

```text
如果把函数参数从 A 改成 B，
因为代码中的 X，
返回值可能从 C 变成 D。
如果实际输出出现 D，假设得到支持；
如果输出仍为 C，假设被否定或需要修正。
整个测试只调用本地函数。
```

## Step 1 — 从 Day 23 选三个输入点

分别为以下函数建立一项假设：

```text
H1：build_product_query(category)
基准输入：category = "laptop"
单一改动：只把 category 从 "laptop" 改为 "book"

H2：render_search(term)
基准输入：term = "laptop"
单一改动：只把 term 从 "laptop" 改为 "A & B"

H3：get_profile(requested_user, current_user, profiles)
基准输入：requested_user = "alice"，current_user = "alice"，profiles = SAMPLE_PROFILES
单一改动：只把 requested_user 从 "alice" 改为 "bob"；current_user 和 profiles 保持不变


```

先只填写基准输入和单一改动，不问 AI。

## Step 2 — 使用 AI 改进假设

提供本地代码和自己的草稿：

```text
请根据我提供的本地教学代码和草稿，帮助我完善 3 个测试假设。
每个假设必须包含：
- 基准输入
- 输入点
- 具体代码证据
- 一次最小改动
- 只在本地执行的验证方法
- 可直接观察的预期结果
- 支持该假设的结果
- 否定或限制该假设的结果
- 安全边界

不要执行测试，不要扩展目标，不要把假设写成已经确认的漏洞。
```

## Step 3 — 填写假设表

| 编号 | 基准 | 单一改动 | 代码证据 | 预期观察 | 支持结果 | 否定/限制结果 |
|---|---|---|---|---|---|---|
| H1 | `category = "laptop"` | 只改为 `"book"` | `"..." + category + "..."` 直接拼接 category。 | 返回的 SQL 字符串中类别文字从 `laptop` 变为 `book`。 | 返回 `SELECT name FROM products WHERE category = 'book'`，且其他固定文字不变。 | 返回值没有 `book`，或固定 SQL 结构也意外改变；需要重新检查函数或测试方式。 |
| H2 | `term = "laptop"` | 只改为 `"A & B"` | f-string 的 `{term}` 直接放进 HTML 字符串。 | 返回字符串中 `A & B` 是否原样出现，而不是变成 `A &amp; B`。 | 返回 `<p>You searched for: A & B</p>`，支持“此函数内部没有 HTML 编码”。 | 返回包含 `A &amp; B` 或其他编码结果；说明这个假设不符合实际输出，或存在未显示的外层处理。 |
| H3 | `requested_user = "alice"`、`current_user = "alice"`、`profiles = SAMPLE_PROFILES` | 只把 requested_user 改为 `"bob"`。 | `return profiles[requested_user]`；`current_user` 只被 `_ = current_user` 接收。 | 保持 current_user 为 alice 时，返回的资料是否跟随 requested_user 变为 bob。 | 返回 bob 的本地字典资料，支持“函数本身未使用 current_user 限制资料选择”。 | 返回 alice 的资料、拒绝访问或抛出 KeyError；需要重新检查输入或实际执行的代码。 |

### 三个完整假设

**H1 — SQL 字符串构造**

```text
基准输入：category = "laptop"。
输入点：build_product_query 的 category 参数。
代码证据：return 行使用 + category + 拼接字符串。
最小改动：只把 category 改为 "book"。
本地验证方法：只调用本地 build_product_query 并查看返回的 Python 字符串；不连接数据库。
预期观察：类别文字会从 laptop 改为 book。
支持结果：返回字符串为 SELECT name FROM products WHERE category = 'book'。
否定或限制结果：如果没有出现 book，或固定 SQL 文字也改变，假设需要修正。
安全边界：只读取本地函数返回值，不执行 SQL，不连接网络或数据库。
```

**H2 — HTML 字符串构造**

```text
基准输入：term = "laptop"。
输入点：render_search 的 term 参数。
代码证据：return 行使用 f"<p>You searched for: {term}</p>"。
最小改动：只把 term 改为普通文字 "A & B"。
本地验证方法：只调用本地 render_search 并查看返回的 Python 字符串；不放入浏览器。
预期观察：& 是否保持为 &，而不是 HTML 编码后的 &amp;。
支持结果：返回 <p>You searched for: A & B</p>，支持“此函数内部没有 HTML 编码”的判断。
否定或限制结果：若返回 A &amp; B 或其他编码形式，说明假设不符合实际输出，或存在未显示的处理。
安全边界：只使用本地普通文字，不启动网页、不在浏览器渲染。
```

**H3 — 本地字典资料选择**

```text
基准输入：requested_user = "alice"、current_user = "alice"、profiles = SAMPLE_PROFILES。
输入点：get_profile 的 requested_user 参数。
代码证据：return profiles[requested_user]；current_user 只被赋值给 _，没有参与判断。
最小改动：只把 requested_user 改为 "bob"，其他两个参数保持不变。
本地验证方法：只调用本地 get_profile 并查看返回的 SAMPLE_PROFILES 字典。
预期观察：返回资料是否从 alice 对应的字典改为 bob 对应的字典。
支持结果：current_user 仍为 alice 时，函数返回 bob 的本地字典，支持“函数本身没有用 current_user 限制选择”的判断。
否定或限制结果：返回 alice、拒绝访问或抛出 KeyError 时，需要检查输入和实际执行代码。
安全边界：只使用文件中的 alice、bob 和 SAMPLE_PROFILES；不使用真实账号、不连接网络。
```

适合今天的“观察”是函数返回的字符串或字典。不要连接数据库，不要启动真实网站。

## Step 4 — 质量检查

逐项检查并修改：

- 一次是否改变了多个变量？
- 预期结果是否能直接看到？
- 是否写明了具体代码证据？
- 是否存在可以否定假设的结果？
- 是否偷偷扩展到真实网站？
- 是否把 AI 的猜测写成已经成立？

不合格：

```text
这个函数可能不安全。
```

较合格：

```text
保持其他值不变，只改变 term；如果返回 HTML 字符串原样包含新 term，
则支持“函数没有在此处对 term 做 HTML 编码”的判断。
```

这仍然只说明函数返回字符串的行为，不自动证明浏览器执行结果。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| 不知道什么叫否定结果 | 只想证明自己的猜测 | 写出“如果输出没有按预期变化”意味着什么 |
| 一次改了输入和代码 | 没保持控制变量 | 测试时只改函数参数 |
| 预期写成“出现漏洞” | 结果不可直接观察 | 改成具体返回字符串或字典内容 |
| H3 同时改两名用户 | 变量太多 | 固定 current_user，只改 requested_user |
| AI 给出范围外步骤 | Prompt 边界没生效 | 删除范围外内容，不执行 |

## 成功标准

- [x] 完成三个假设
- [x] 每个假设有具体代码证据
- [x] 每次测试只改一个变量
- [x] 每个结果都能直接观察
- [x] 每个假设都能被否定或限制

## 操作记录

```text
最容易写的假设：H1，因为 category 只会进入一个容易观察的返回字符串位置。
最难写的假设：H2，因为要区分“函数返回原始 HTML 字符串”和“浏览器如何解释 HTML”；今天只能观察前者。
AI 修改了我的哪一部分：把“可能有问题”改成了固定基准、一次最小改动、可直接观察的结果和否定结果。
我拒绝了 AI 的哪条建议：任何连接数据库、启动网站、使用真实账号或扩展到课程范围外目标的建议都不采用。
三个测试是否都只在本地：是；三个设计都只调用 profile_app.py 中的函数和 SAMPLE_PROFILES，不执行网络或数据库操作。
```

## 思考题

为什么一个无法被否定的说法，不适合作为测试假设？

**回答：** 因为无法被否定的说法，不管看到什么结果都可以继续说“自己是对的”，所以测试不能帮助我们学习或修正判断。例如“这个函数可能不安全”没有指定输入、输出或相反结果；它不能被清楚检查。可测试假设必须提前写出：如果看到了什么具体输出，就支持它；如果没有看到，或看到相反输出，就否定或限制它。

## 今日一句话总结

今天我把三段本地代码的风险线索改写成单变量测试假设：每项都有基准、代码证据、可观察输出、支持结果和否定结果，但没有把假设当成已经确认的漏洞。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 24: design test hypotheses"
```

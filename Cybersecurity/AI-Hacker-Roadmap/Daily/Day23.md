# Day 23 — 让 AI 阅读简单 Web 代码

## Mission

先自己阅读本地教学代码，再让 AI 帮助追踪输入如何流向 SQL 字符串、HTML 字符串和用户资料，最后用具体代码核对 AI。

## 难度与时间

- 难度：⭐⭐⭐☆☆
- 核心任务：30–45 分钟

## 安全范围

只分析：

```text
Labs/CodeReview/profile_app.py
```

该文件不连接数据库、Web 服务器或网络。今天只读代码，不修改它。

## Step 1 — 第一次阅读，不问 AI

1. 在 VS Code 打开 `Labs/CodeReview/profile_app.py`。
2. 从文件顶部向下读一遍。
3. 找到三个以 `def` 开头的函数。
4. 对每个函数填写：

```text
函数名：build_product_query
输入参数：category: str
返回值："SELECT name FROM products WHERE category = '" + category + "'"
输入进入了哪里：进入 SQL 字符串中 `category = '` 与后面的单引号之间，然后由 return 返回整个字符串。
是否看到验证、编码或权限检查：没有看到对 category 的验证，也没有看到参数化查询；这个函数也没有权限检查。
我不确定的地方：调用方是谁、返回的字符串会不会被数据库执行，以及是否有外层保护，都没有在这个文件中显示。

函数名：render_search
输入参数：term: str
返回值：f"<p>You searched for: {term}</p>"
输入进入了哪里：进入 HTML 字符串的 `{term}` 位置，然后由 return 返回整个 HTML 字符串。
是否看到验证、编码或权限检查：没有看到对 term 的验证或 HTML 编码；这个函数不涉及资料权限检查。
我不确定的地方：调用方会不会把返回字符串放进浏览器，以及外层是否会进行编码，都没有在这个文件中显示。

函数名：get_profile
输入参数：requested_user: str,
    current_user: str,
    profiles: dict[str, dict[str, str]],
返回值：profiles[requested_user]
输入进入了哪里：requested_user 被用作 profiles 字典的键，选择对应的资料后由 return 返回。
是否看到验证、编码或权限检查：没有看到 requested_user 与 current_user 的比较，也没有看到其他所有权或权限检查。
我不确定的地方：requested_user 和 current_user 在真实应用中来自哪里、谁可以调用函数，以及外层是否有权限检查，都没有在这个文件中显示。

```

先使用“不确定”也可以，但不要跳过自己的判断。

## Step 2 — 标出输入到输出的路线

在记录中使用箭头：

```text
category → SQL 字符串 → return
term → HTML 字符串 → return
requested_user → profiles 字典索引 → return
```

再回答：

```text
current_user 是否真正参与了资料选择？
这段代码是否真的执行 SQL？
这段代码是否真的在浏览器渲染 HTML？
```

**回答：**

```text
category → SQL 字符串 → return
term → HTML 字符串 → return
requested_user → profiles 字典索引 → return

current_user 是否真正参与了资料选择？没有。它只被 `_ = current_user` 接收，但没有用于条件判断或字典选择。
这段代码是否真的执行 SQL？没有。从注释和 docstring 可见，build_product_query 只返回一个字符串，没有数据库连接或执行语句。
这段代码是否真的在浏览器渲染 HTML？没有。render_search 只返回 HTML 字符串；这个文件没有浏览器、Web 服务器或渲染代码。
```

### SQL 格式：先看懂 `build_product_query`

当 `category` 的普通值是 `Food` 时，这个函数会返回：

```sql
SELECT name FROM products WHERE category = 'Food'
```

| SQL 部分 | 零基础含义 |
|---|---|
| `SELECT` | 选择、取出数据。 |
| `name` | 要取出的列名；这里是商品名称。 |
| `FROM` | 说明数据从哪里来。 |
| `products` | 表名；可以把表理解成一张叫“products”的表格。 |
| `WHERE` | 设置筛选条件。 |
| `category = 'Food'` | 只选择 category 这一列等于 `Food` 的行；单引号表示 SQL 中的文字值。 |

Python 中的 `+` 是把字符串接在一起。因此代码把固定的 SQL 文字、`category` 的实际内容和最后的单引号拼成一个新字符串。问题不在于 `SELECT`、`FROM` 或 `WHERE` 本身，而在于把外部输入直接拼进 SQL。最小修复原则是：若将来真的使用数据库，应改用该数据库库提供的参数化查询接口，把“SQL 结构”和“category 的值”分开传递，而不是用 `+` 拼接。

### AI 分析与人工核对

| 函数 | 代码直接证明的事实 | 需要运行或更多上下文验证的假设 | 最小修复原则 |
|---|---|---|---|
| `build_product_query` | `category` 被 `+ category +` 拼入返回的 SQL 字符串；函数不连接或执行数据库。 | 这个字符串是否会被执行、是否有外层验证，以及实际影响。 | 使用数据库驱动提供的参数化查询，把 SQL 结构与值分开。 |
| `render_search` | `{term}` 被 f-string 直接放进返回的 HTML 字符串；函数没有编码步骤。 | 返回值是否会进入浏览器、外层是否会编码，以及实际影响。 | 在将不可信文字放入 HTML 前进行上下文正确的 HTML 编码。 |
| `get_profile` | 函数返回 `profiles[requested_user]`；`current_user` 只被赋给 `_`，未参与判断。 | 调用者是否已做外层权限检查、资料是否敏感，以及实际影响。 | 在返回资料前依据 current_user 和授权规则检查是否允许访问 requested_user。 |

注意：函数返回字符串，不等于字符串已经被数据库执行或浏览器渲染。

## Step 3 — 让 AI 分析

把完整本地文件内容和下面 Prompt 一起提供：

```text
请审查这个本地教学 Python 文件。
对每个函数只回答：
1. 输入来源
2. 数据流向
3. 缺少的验证、参数化、编码或权限检查
4. 可能造成的问题类型
5. 最小修复原则

把“代码直接证明的事实”和“需要运行或更多上下文验证的假设”分开。
请引用具体函数名或代码表达式。
不要提供针对真实网站的操作步骤。
```

## Step 4 — 逐项核对 AI

建立表格：

| 函数 | 我的判断 | AI 判断 | 代码证据 | 需要验证 |
|---|---|---|---|---|
| `build_product_query` | 输入直接拼进 SQL 返回字符串，缺少参数化。 | 这是 SQL 构造风险，不等于 SQL 已被执行。 | `"... category = '" + category + "'"`。 | 是否有数据库调用、外层保护和实际影响。 |
| `render_search` | 输入直接进入 HTML 返回字符串，未见编码。 | 这是 HTML 输出风险，不等于已在浏览器中渲染。 | `f"<p>You searched for: {term}</p>"`。 | 返回值是否进入浏览器、外层是否编码和实际影响。 |
| `get_profile` | requested_user 决定返回哪份资料，current_user 未参与选择。 | 这是缺少所有权检查的风险，不等于真实应用已泄露资料。 | `return profiles[requested_user]`，以及 `_ = current_user`。 | 参数来源、调用权限、外层检查和实际影响。 |

“代码证据”不要写“AI 说的”，而要写类似：

```text
使用 + 把 category 拼入 SQL 字符串
f-string 把 term 放进 HTML
返回 profiles[requested_user]，current_user 未参与判断
```

## Step 5 — 区分风险与已确认结果

今天能从代码确认：

- 输入被直接放进返回字符串或字典查询。
- 函数内部有没有明显的参数化、HTML 编码或所有权检查。

今天不能仅凭文件确认：

- SQL 是否在其他地方被执行。
- 返回的 HTML 是否真的进入浏览器。
- 真实应用有没有外层保护。
- 实际影响和可利用性。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| 一上来只复制 AI 答案 | 跳过了独立阅读 | 先关闭 AI 回答，完成自己的表格 |
| 把参数名当输入来源 | 没区分名称与调用方 | 写“函数参数；调用方未在此文件中显示” |
| 宣布 SQL 注入已成功 | 把构造字符串当成执行数据库 | 记录为风险，需要运行环境验证 |
| 说 `current_user` 做了检查 | 只看见变量名 | 查看它是否参与条件判断 |
| 找不到代码证据 | AI 结论太笼统 | 要求它引用函数名和表达式，再人工核对 |

## 成功标准

- [x] 自己先完成第一次阅读
- [x] 找到三个输入点和返回路径
- [x] AI 区分事实与假设
- [x] 每项判断都引用具体代码
- [x] 没把“可能的问题”写成“已经利用成功”

## 操作记录

```text
最容易看懂的函数：render_search；term 被放进 f-string，再返回一个 HTML 字符串。
最难理解的函数：build_product_query；一开始不熟悉 SELECT、FROM、WHERE 和字符串拼接。
AI 帮我发现的内容：三个函数分别存在直接拼接 SQL、未编码 HTML 输出、以及 current_user 未参与资料选择的风险写法。
我纠正 AI 的内容：不能把“返回 SQL 字符串”写成“已经执行 SQL”，也不能把“返回 HTML 字符串”写成“已经在浏览器显示”。
仍然需要运行验证的假设：这些函数在真实应用中的调用方式、外层保护、是否连接数据库或浏览器，以及实际影响。
```

## 思考题

为什么“AI 说这里有漏洞”还不等于漏洞已经被确认？

**回答：** AI 可以根据代码找出可疑的数据流和缺少的保护，但一小段文件通常看不到完整应用。这里没有数据库连接、Web 路由、浏览器渲染或调用方代码，所以不能确认字符串是否会被执行、谁能传入参数、外层是否已经保护，以及实际会产生什么影响。漏洞确认需要在明确授权的完整环境中，用具体证据验证；今天只能确认代码中存在风险写法。

## 今日一句话总结

今天我学会了追踪函数参数如何进入 SQL 字符串、HTML 字符串和字典索引，并把“代码能直接证明的风险写法”与“仍需要完整环境验证的实际影响”分开。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 23: review local code with AI"
```

# Day 25 — 人工验证 AI 的判断

## Mission

只在本地调用三个教学函数，用实际返回值支持、否定或限制 Day 24 的假设。

## 难度与时间

- 难度：⭐⭐⭐⭐☆
- 核心任务：35–55 分钟

## 安全范围

今天不连接数据库、不启动外部网站、不发送网络请求。只运行：

```text
Labs/CodeReview/profile_app.py
Scripts/day25_checks.py
```

## 验证原则

```text
一次只改一个变量
先保留基准结果
预期与实际分开写
失败也算有效证据
函数返回内容不等于真实系统已经产生影响
```

## Step 1 — 创建本地检查文件

在 VS Code 的 `Scripts` 目录新建：

```text
day25_checks.py
```

先输入导入：

```python
from Labs.CodeReview.profile_app import (
    SAMPLE_PROFILES,
    build_product_query,
    get_profile,
    render_search,
)
```

从 `AI-Hacker-Roadmap` 根目录把脚本作为模块运行，Python 才能找到 `Labs`：

```bash
python3 -m Scripts.day25_checks
```

不要使用 `python3 Scripts/day25_checks.py`。后一种写法会把 `Scripts` 当作导入起点，因此看不到同级的 `Labs` 文件夹。

## Step 2 — H1：比较 SQL 字符串

加入：

```python
print("H1 baseline:")
print(build_product_query("books"))

print("H1 changed:")
print(build_product_query("books'"))
```

今天只观察返回字符串。不要连接或执行数据库。

记录：

- 基准字符串是什么。
- 只增加一个单引号后，返回字符串哪里改变。
- 这支持“输入被直接拼接进字符串”。
- 这不能单独证明数据库已经执行或漏洞已被真实利用。

## Step 3 — H2：比较 HTML 字符串

加入：

```python
print("H2 baseline:")
print(render_search("hello"))

print("H2 changed:")
print(render_search("<b>hello</b>"))
```

只观察返回字符串有没有原样包含 `<b>hello</b>`。今天不把结果放入真实网站，也不讨论真实网站攻击。

## Step 4 — H3：比较资料选择

加入：

```python
print("H3 baseline:")
print(get_profile("alice", "alice", SAMPLE_PROFILES))

print("H3 changed:")
print(get_profile("bob", "alice", SAMPLE_PROFILES))
```

保持 `current_user` 为 `alice`，只把 `requested_user` 从 `alice` 改为 `bob`。

观察返回字典是否变成 Bob 的资料。这支持“函数内部没有根据 current_user 阻止这次选择”，但不证明外层程序一定没有其他权限检查。

## Step 5 — 运行并记录

在项目根目录运行：

```bash
python3 -m Scripts.day25_checks
```

把终端实际输出抄到验证表，不要把“预期”复制到“实际”一栏。

## Step 6 — 为每项写有限结论

使用三个结论词之一：

```text
支持：实际结果与假设一致
否定：实际结果与假设冲突
部分支持/需要限制：只证明了一部分，仍缺上下文
```

推荐句式：

```text
实际返回值显示 ______，因此支持/否定 ______。
这次测试只证明 ______，仍不能确认 ______。
```

## Step 7 — 让 AI 只复核推理

```text
下面是我的本地假设、基准输入、单一改动、预期和实际输出。
请检查我的结论是否由证据支持。
逐项指出：
1. 哪句话有直接证据
2. 哪句话超出证据
3. 还缺少什么上下文

不要替我宣布真实漏洞成立，不要提供范围外测试步骤。
```

AI 的复核仍然要由你对照终端输出。

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `No module named 'Labs'` | 用 `python3 Scripts/day25_checks.py` 直接运行时，Python 只从 Scripts 查找导入 | 在 `AI-Hacker-Roadmap` 根目录运行 `python3 -m Scripts.day25_checks` |
| 把预期写进实际栏 | 没运行代码就下结论 | 实际栏只能抄终端输出 |
| H3 同时改变两个用户参数 | 没控制变量 | 固定 `current_user` 为 `alice` |
| 宣布数据库已被攻击 | 测试只生成字符串 | 把结论限制在函数返回值 |
| HTML 标签出现在字符串就宣布执行 | 没有浏览器渲染证据 | 只记录未编码地进入返回字符串 |

## 验证表

| 编号 | 基准输入 | 单一改动 | 预期 | 实际 | 结论 |
|---|---|---|---|---|---|
| H1 | `category = "books"`；返回 `SELECT name FROM products WHERE category = 'books'` | 只把 category 改为 `"books'"` | 返回字符串会原样多出输入中的单引号。 | `SELECT name FROM products WHERE category = 'books''` | 支持：输入被直接拼接进返回字符串。限制：没有数据库连接或执行证据。 |
| H2 | `term = "hello"`；返回 `<p>You searched for: hello</p>` | 只把 term 改为 `<b>hello</b>` | 返回字符串会原样包含 `<b>hello</b>`。 | `<p>You searched for: <b>hello</b></p>` | 支持：此函数返回时未对 term 做 HTML 编码。限制：没有浏览器渲染证据。 |
| H3 | `requested_user = "alice"`、`current_user = "alice"`；返回 Alice 的本地字典。 | 只把 requested_user 改为 `"bob"`，current_user 保持 alice。 | 返回资料会变为 Bob 的本地字典。 | `{'display_name': 'Bob', 'plan': 'student'}` | 支持：函数内部没有用 current_user 阻止这次字典选择。限制：不能说明外层程序没有其他权限检查。 |

## 成功标准

- [x] 三项测试都只在本地运行
- [x] 保存基准与修改后结果
- [x] 一次只改变一个函数参数
- [x] 最终结论引用终端证据
- [x] 每个结论都写明限制

## 思考题

为什么“函数表现出危险的数据流”与“真实应用漏洞已经成立”是两个不同层次的结论？

**回答：** “函数表现出危险的数据流”是从本地代码和本次返回值能直接看到的事实：例如输入被拼进字符串，或 requested_user 决定字典选择。“真实应用漏洞已经成立”还需要更多证据，例如真实应用是否调用这个函数、输入是否真的来自用户、SQL 字符串是否被数据库执行、HTML 是否进入浏览器，以及外层是否有验证、编码或权限检查。本次测试没有数据库、Web 服务器或真实账号，所以只能确认函数行为，不能确认真实应用影响。

## 今日一句话总结

今天我用三个本地函数的实际返回值验证了 Day 24 的假设：输入会直接进入 SQL 和 HTML 返回字符串，requested_user 会决定本地资料选择；这些结果支持代码层面的判断，但不等于真实应用漏洞已经成立。

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 25: validate AI hypotheses"
```

# Day 8 — SQL 与 SQL Injection 基础

## Mission

运行一个本地 SQLite 程序，理解 `SELECT`、`FROM`、`WHERE`、参数和参数化查询。今天不向任何网站发送 SQL 内容。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：30–45 分钟

## 安全范围

只运行：

```text
Labs/SQLBasics/query_demo.py
```

程序使用内存数据库，关闭后数据消失，不连接网络。

## 今天需要理解

程序使用：

```sql
SELECT name FROM products WHERE category = ? AND released = ?
```

逐段含义：

```text
SELECT name       读取 name 列
FROM products     数据来自 products 表
WHERE             开始写筛选条件
category = ?      category 必须等于第一个参数
AND               两个条件都必须满足
released = ?      released 必须等于第二个参数
```

`?` 是占位符。SQL 模板和参数分开交给数据库。

## Part 1 — 确认终端位置

### Step 1 — 打开 VS Code 终端

终端应位于仓库根目录 `Study_Computer`。可以运行：

```bash
pwd
```

正常路径末尾应是：

```text
Study_Computer
```

### Step 2 — 确认 Python

运行：

```bash
python3 --version
```

只要能正常显示 Python 3 版本即可。

## Part 2 — 运行三个基准输入

### Step 3 — 输入 Gifts

运行：

```bash
python3 Cybersecurity/AI-Hacker-Roadmap/Labs/SQLBasics/query_demo.py
```

看到提示后输入：

```text
Gifts
```

按 Enter。预期看到：

```text
Parameters: ('Gifts', 1)
Results:
- Gift Card
```

`Prototype Gift` 不会出现，因为样例数据中它的 `released` 不是 `1`。

### Step 4 — 输入 Clothing

再次运行同一命令，输入：

```text
Clothing
```

预期结果：

```text
- T-Shirt
```

### Step 5 — 输入 Unknown

第三次运行，输入：

```text
Unknown
```

预期：

```text
(no rows)
```

没有结果不等于程序失败，只表示没有同时满足条件的数据。

## Part 3 — 阅读代码

### Step 6 — 打开脚本

在 VS Code 打开：

```text
Labs/SQLBasics/query_demo.py
```

先找到创建表和插入样例数据的位置，再找到：

```python
category = input(...).strip()
query = "SELECT name FROM products WHERE category = ? AND released = ?"
parameters = (category, 1)
cursor.execute(query, parameters)
```

### Step 7 — 追踪输入

按顺序说明：

```text
用户输入进入 category
→ category 放进 parameters
→ query 保持固定模板
→ execute 分别接收模板和参数
```

这里没有使用字符串加号把输入拼进 SQL。

## Part 4 — 只做纸面比较

观察下面的错误示范，但不要运行：

```python
query = "SELECT name FROM products WHERE category = '" + category + "'"
```

问题是：

```text
固定 SQL 结构
和
不可信输入
被拼成同一个字符串
```

如果输入改变了 SQL 字符串结构，数据库可能把数据误当成 SQL 语法。

今天只需要理解根本原因，不需要测试 SQL payload。

## 常见错误与处理

| 现象 | 原因 | 处理 |
|---|---|---|
| `No such file` | 终端路径不对 | 回到 `Study_Computer` 后使用完整命令 |
| 输入后没结果 | 输入了 Unknown 或拼写不同 | 对照大小写输入 `Gifts` |
| `Prototype Gift` 不显示 | 它未发布 | 这是 `released = 1` 条件的预期结果 |
| 把 `?` 当成查询字符串 | 混淆了 SQL 占位符和 URL 问号 | 这里的 `?` 位于 SQL 中，是参数占位符 |
| 想运行危险拼接 | 超出今天目标 | 只阅读，不执行 |

## 成功标准

- [ ] 成功运行三个输入
- [ ] Gifts 返回 Gift Card
- [ ] Clothing 返回 T-Shirt
- [ ] Unknown 返回 no rows
- [ ] 能解释 SELECT、FROM、WHERE
- [ ] 能指出 SQL 模板与参数是分开的
- [ ] 能解释字符串拼接的风险

## 操作记录

```text
Gifts 的结果：

Clothing 的结果：

Unknown 的结果：

SQL 模板：

第一个参数：

第二个参数：

为什么 Prototype Gift 没出现：

为什么参数化查询更安全：

我遇到的问题：
```

## 思考题

```text
1. `?` 在这个 SQL 中是什么？
2. 用户输入有没有直接出现在 query 字符串中？
3. no rows 和程序报错有什么区别？
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 8: learn SQL query basics"
```


# Day 9 — 第一个 SQL Injection Lab

## Mission

完成 PortSwigger 官方入门 SQL Injection 实验，比较正常分类条件与修改后的条件，并理解参数化查询这一修复方向。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：40–60 分钟

## 安全范围

只使用：

```text
https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data
```

下面的测试值只能用于这个官方实验实例。

## 实验目标

实验名称：

```text
SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
```

实验页面说明服务器概念上执行类似：

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

今天的目标是让实验页面显示未发布商品。

## Part 1 — 打开实验

### Step 1 — 从 Academy 进入

在 Burp 自带浏览器打开课程链接，点击：

```text
Access the lab
```

等待临时实验商店出现。不要在课程说明页上寻找商品分类。

### Step 2 — 建立正常行为

在实验商店选择一个商品分类，例如页面上实际存在的分类。

观察页面只显示该分类中的正常商品。

## Part 2 — 找到分类请求

### Step 3 — 打开 HTTP history

进入：

```text
Proxy → HTTP history
```

寻找包含：

```text
category=
```

的 GET 请求。路径可能包含 `/filter`，以你实际看到的请求为准。

### Step 4 — 保存基准

选中请求，查看：

```text
请求第一行
category 的原始值
响应状态码
页面中可见商品
```

右键选择：

```text
Send to Repeater
```

在 Repeater 中先不修改，点击 `Send`，保存基准响应。

## Part 3 — 修改 category

### Step 5 — 只替换参数值

只替换 `category=` 后面的值，不修改其他参数、Cookie、方法或路径。

便于理解的原始测试值是：

```text
' OR 1=1--
```

在原始 HTTP 请求行中使用 URL 编码形式更稳妥：

```text
%27+OR+1%3D1--
```

因此参数应类似：

```text
category=%27+OR+1%3D1--
```

不要使用中文弯引号 `‘’`，必须是英文单引号编码 `%27`。

### Step 6 — 理解三部分

```text
%27       解码后是英文单引号 '
+OR+      空格与 OR
1%3D1     解码后是 1=1
--        注释后面的实验查询内容
```

`1=1` 始终为真，因此条件范围发生变化。

### Step 7 — 发送

点击 `Send`，比较：

```text
状态码
响应长度
商品名称
是否出现基准中没有的商品
```

不要只看长度；商品内容才是关键证据。

## Part 4 — 确认完成

### Step 8 — 查看 Lab 状态

回到实验页面或刷新相应结果。成功时页面顶部应显示：

```text
Solved
```

### Step 9 — 保存脱敏记录

记录：

```text
实验名称
category 原始值
使用的编码值
修改前商品结果
修改后商品结果
根本原因
修复方向
```

删除 Cookie、实验临时域名和其他会话值。

## 根本原因与修复

根本原因：

```text
服务器把客户端 category 输入直接拼进 SQL
```

修复方向：

```text
使用参数化查询
让 SQL 结构固定
把 category 作为数据参数传入
```

## 常见错误与处理

| 现象 | 常见原因 | 处理 |
|---|---|---|
| 返回 400 | 请求行包含未编码空格 | 使用 `%27+OR+1%3D1--` |
| 页面结果没变化 | 改错参数或没点击 Send | 只检查 `category` 并重新发送 |
| 返回所有结果但 Lab 未 Solved | 没在当前实验实例中触发页面 | 回到实例确认状态 |
| 请求失败 | 实验实例过期 | 从 Academy 重新 Access the lab |
| 记录里有 Cookie | 复制了完整请求 | 删除 Cookie 值后再保存 |

## 成功标准

- [ ] 打开正确实验实例
- [ ] 找到带 category 的 GET 请求
- [ ] 保存正常基准
- [ ] 只修改 category
- [ ] 修改后出现额外商品
- [ ] Lab 显示 Solved
- [ ] 能解释 `OR 1=1`
- [ ] 能写出参数化查询修复方向

## 实验记录

```text
Lab 名称：

请求方法与路径：

category 原始值：

category 修改值：

修改前结果：

修改后结果：

为什么条件变成更宽：

根本原因：

修复方式：

我遇到的问题：
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete day 9 SQL injection lab"
```


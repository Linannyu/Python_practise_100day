# Day 7 — 第一个 PortSwigger 官方实验

## Mission

完成 PortSwigger Web Security Academy 的 `Excessive trust in client-side controls` 实验，把 Week 1 的抓包、参数和 Repeater 串起来。

## 难度与时间

- 难度：⭐⭐☆☆☆
- 核心任务：40–60 分钟

## 安全范围

只使用：

```text
https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls
```

实验中的账号、商品、余额和购买操作都是虚拟数据。不要在其他购物网站重复这些步骤。

## 今天需要理解

网页提交了商品价格，但服务器错误地信任了客户端提供的价格。

正确设计应该是：

```text
客户端提交商品 ID 和数量
→ 服务器从数据库查询真实价格
→ 服务器自己计算总价
```

## Part 1 — 启动实验

### Step 1 — 打开官方页面

使用 Burp 自带浏览器访问上面的课程链接。

在页面中点击：

```text
Access the lab
```

等待系统打开一个独立的实验实例。

如果要求登录 PortSwigger Academy，先完成平台登录，再重新点击 `Access the lab`。

### Step 2 — 识别实验实例

实验页面顶部应显示 Lab 状态。不要把 Academy 课程说明页误认为真正的实验商店。

实验实例通常有自己的临时域名。不要把这个域名写入公开笔记。

## Part 2 — 登录与建立基准

### Step 3 — 使用实验账号

点击：

```text
My account
```

使用实验说明提供的账号：

```text
Username: wiener
Password: peter
```

这些凭据只属于实验。

### Step 4 — 查看余额和商品

登录后查看账号余额，然后回到商店，打开：

```text
Lightweight "l33t" Leather Jacket
```

先点击加入购物车，不要修改请求。

### Step 5 — 查看正常购物车

打开购物车，观察正常价格和余额。记录：

```text
商品名称
正常价格
当前余额
为什么正常购买会失败
```

不要记录 Session Cookie。

## Part 3 — 找到关键请求

### Step 6 — 打开 HTTP history

进入：

```text
Proxy → HTTP history
```

寻找加入购物车时产生的：

```text
Method：POST
Path：/cart
```

如果有多个 `/cart`，选中请求正文包含商品参数的那一个。

### Step 7 — 识别参数

请求正文通常包含表示以下含义的参数：

```text
商品 ID
数量
价格
```

先不要修改。写下每个参数在请求中的名称和值。

右键选择：

```text
Send to Repeater
```

## Part 4 — 在 Repeater 验证

### Step 8 — 保存基准

在 Repeater 先不修改，查看请求结构。

注意：发送 `/cart` 会再次改变购物车状态。为了避免重复商品，基准可以使用 HTTP history 中已经产生的请求和响应，不必为了“看看”而多次点击 `Send`。

### Step 9 — 只修改价格

保持商品 ID 和数量不变，只修改价格参数，使实验商品总价低于实验账号余额。

只在这个 PortSwigger 实验实例中操作。

不要同时修改：

```text
商品 ID
数量
Cookie
请求方法
路径
```

### Step 10 — 发送并验证

点击 `Send` 一次。然后回到实验浏览器刷新购物车。

观察：

```text
商品是否仍然相同
数量是否仍然相同
价格是否变成客户端提交的值
```

如果购物车出现多个相同商品，是因为 `/cart` 请求被重复发送。清理多余条目后保留一个即可。

## Part 5 — 完成实验

### Step 11 — 结算

确认修改后的虚拟价格低于虚拟余额，再点击购买或结算。

完成后页面应显示：

```text
Solved
```

### Step 12 — 保存证据

保存一张 `Solved` 截图到：

```text
Images/day07-solved.png
```

截图和笔记中不要包含：

```text
Cookie
Session ID
实验临时域名
不必要的账号信息
```

## 常见错误与处理

| 现象 | 常见原因 | 处理 |
|---|---|---|
| 找不到 `/cart` | 没有实际点击加入购物车 | 回到商品页操作一次 |
| 请求里没有价格 | 选错 `/cart` 请求 | 查看请求正文，选择包含商品参数的记录 |
| 修改后商品重复 | 重复发送有状态的 POST | 清理购物车，只保留需要的条目 |
| 价格没变化 | 修改了响应而不是请求 | 在 Repeater 左侧请求区修改 |
| 实验突然打不开 | 临时实例过期 | 从 Academy 页面重新 `Access the lab` |
| 结算仍失败 | 修改价格仍高于余额或购物车有多项 | 检查购物车总价 |

## 成功标准

- [ ] 正确打开实验实例
- [ ] 使用实验账号登录
- [ ] 找到 POST `/cart`
- [ ] 找到价格参数
- [ ] 只修改价格
- [ ] 购物车显示修改后的虚拟价格
- [ ] Lab 显示 `Solved`
- [ ] 保存脱敏截图与记录

## 实验记录

```text
Lab 名称：

关键请求方法与路径：

商品 ID 参数：

数量参数：

价格参数：

修改前结果：

修改后结果：

服务器错误信任了什么：

正确修复方式：

我使用了哪一级提示：

我遇到的问题：
```

## Week 1 复盘

```text
1. Request 与 Response 的区别：
2. 参数与请求头的区别：
3. Cookie 与 Session 的区别：
4. Repeater 的用途：
5. 为什么服务器必须验证客户端数据：
```

## 今日一句话总结

```text
今天我学会了：
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete week 1 PortSwigger lab"
```

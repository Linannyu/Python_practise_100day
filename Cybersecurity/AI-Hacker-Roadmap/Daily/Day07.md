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

使用实验说明页提供的临时实验账号登录。

为避免把任何账号或密码提交到作品集，本项目不记录具体凭据。这些凭据只属于该官方实验，不能用于任何其他网站。

### Step 4 — 查看余额和商品

登录后查看账号余额，然后回到商店，打开：

```text
Lightweight "l33t" Leather Jacket
```

先点击加入购物车，不要修改请求。

### Step 5 — 查看正常购物车

打开购物车，观察正常价格和余额。记录：

```text
商品名称: Lightweight "l33t" Leather Jacket
正常价格: 1337.00
当前余额: 100
为什么正常购买会失败: 余额不足
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
商品 ID: 1
数量: 1
Cookie: session=[redacted]
请求方法: POST
路径: /cart
```

### Step 10 — 发送并验证

点击 `Send` 一次。然后回到实验浏览器刷新购物车。

观察：

```text
商品是否仍然相同: 商品相同
数量是否仍然相同：点击一次send，cart里面的数量就在原本的数量上增加
价格是否变成客户端提交的值： 价格变成客户端提交的值
```

如果购物车出现多个相同商品，是因为 `/cart` 请求被重复发送。清理多余条目后保留一个即可。

## Part 5 — 完成实验

### Step 11 — 结算

确认修改后的虚拟价格低于虚拟余额，再点击购买或结算。

完成后页面应显示：Your order is on its way!

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

- [x] 正确打开实验实例
- [x] 使用实验账号登录
- [x] 找到 POST `/cart`
- [x] 找到价格参数
- [x] 只修改价格
- [x] 购物车显示修改后的虚拟价格
- [x] Lab 显示 `Solved`
- [x] 保存脱敏截图与记录

## 实验记录

```text
Lab 名称：Excessive trust in client-side controls

关键请求方法与路径：POST /cart

商品 ID 参数：productId=1

数量参数：quantity=1

价格参数：price；修改后的请求值是 1700，对应实验中的 17.00。
修改前页面显示的正常价格是 1337.00，但没有把修改前请求中的 price
原始数值保存到记录中，所以不猜测该数值。

其他正文参数：redir=PRODUCT；本次实验没有修改它。

修改前结果：商品正常价格为 1337.00，实验账号余额为 100，
所以按照正常价格无法购买。

修改后结果：购物车显示了客户端提交的新价格；重复发送 POST /cart
会再次改变购物车状态，使原有商品数量增加。截图确认页面显示 Solved
和 Your order is on its way!。

服务器错误信任了客户端请求中提交的商品价格，没有只使用服务器端保存的
真实价格计算购物车总价。

正确修复方式：客户端只提交商品 ID 和数量；服务器根据商品 ID 查询真实
价格，并在服务器端计算总价，不接受客户端决定商品价格。

我使用了哪一级提示：无

我遇到的问题：重复发送会改变状态的 POST /cart 后，购物车中的商品数量
会继续增加，因此不能像普通 GET 请求一样反复发送而不检查状态。

截图检查：已经保存截图，但地址栏仍显示完整实验临时域名。需要先裁剪或
遮挡地址栏，才能把“保存脱敏截图与记录”标为完成。
```

## Week 1 复盘

```text
1. Request 与 Response 的区别：Request 是客户端发给服务器的请求，
Response 是服务器处理后返回给客户端的响应。

2. 参数与请求头的区别：参数通常表示这次操作使用的具体数据，例如商品
ID、数量或查询值；请求头通常描述请求本身，例如 Host、Content-Type 或
Cookie。它们都能随请求发送，但位置和用途不同。

3. Cookie 与 Session 的区别：Cookie 是浏览器保存并可通过请求头发送的
数据；Session 是服务器用来记住访问状态的机制。Cookie 可以携带 Session
标识，但 Cookie 不等于整个 Session。

4. Repeater 的用途：保存、修改并重新发送一条请求，方便保留基准，
每次只改变一个变量，再比较响应结果。

5. 为什么服务器必须验证客户端数据：因为客户端请求可以被用户修改，
包括隐藏字段、参数和请求头。重要价格、权限和业务规则必须由服务器检查。
```

## 今日一句话总结

```text
今天我学会了：网页提交的价格也属于可修改的客户端数据，服务器不能直接
相信它。对于会改变状态的 POST 请求，还要注意重复发送可能重复执行操作。
```

## Git Commit

```bash
git add Cybersecurity/AI-Hacker-Roadmap
git commit -m "Complete week 1 PortSwigger lab"
```

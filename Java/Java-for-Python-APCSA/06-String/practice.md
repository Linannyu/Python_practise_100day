# Day 06 Lab — Build a Username Inspector
# 第 06 天实验 — 构建用户名检查器

## 🎯 Lab Goal / 实验目标

Build a text-validation report using **String methods and loops**.  
使用 **String 方法和循环** 构建一个文本验证报告。

You will reuse conditionals and methods while practicing **safe indexing**.  
你会复用之前学过的条件判断和方法，同时练习**安全地访问字符串中的字符**。

### Today’s Java / 今天的 Java

- `length()` — 获取字符串长度
- `charAt()` — 获取指定位置的字符
- `substring()` — 截取字符串的一部分
- `indexOf()` — 查找字符或字符串的位置
- `equals()` — 比较两个字符串的内容
- Immutable Strings — 不可变字符串

### Reuse from Days 01–05 / 复习 Day 01–05

- methods — 方法
- boolean conditions — 布尔条件
- loops — 循环
- counters — 计数器
- early return values — 提前返回结果

---

# 🧩 Mission / 任务

Create a file named:

创建一个名为：

```text
UsernameInspector.java
```

Implement these three methods:

实现下面三个方法：

```java
public static boolean isValidUsername(String username)

public static int countDigits(String username)

public static String initials(String firstName, String lastName)
```

---

# 1. Valid Username Rules / 有效用户名规则

A username is valid **only if all rules are satisfied**.

一个用户名只有在**满足所有规则**的情况下才有效。

### Rule 1 — Length / 长度

The username must have **5–12 characters**, inclusive.

用户名长度必须是 **5–12 个字符**，包括 5 和 12。

```java
username.length()
```

For example:

```text
"abc"        → 3  → invalid
"lin2026"    → 7  → valid length
"1234567890123" → 13 → invalid
```

---

### Rule 2 — No spaces / 不能有空格

The username cannot contain spaces.

用户名不能包含空格。

You can check this with a loop and `charAt()`.

你需要使用循环和 `charAt()` 检查字符。

Example idea:

```java
if (username.charAt(i) == ' ') {
    return false;
}
```

---

### Rule 3 — Starts with a letter / 必须以字母开头

The first character must be a letter.

第一个字符必须是字母。

For this lab, you can check whether the character is between:

```text
'A'–'Z'
'a'–'z'
```

Example:

```java
char first = username.charAt(0);

boolean isLetter =
    (first >= 'A' && first <= 'Z') ||
    (first >= 'a' && first <= 'z');
```

If the first character is not a letter, return `false`.

如果第一个字符不是字母，就返回 `false`。

---

### Rule 4 — At least one digit / 至少包含一个数字

The username must contain at least one digit.

用户名至少需要包含一个数字。

A digit is:

```text
'0'–'9'
```

You should use a loop and `charAt()`.

你应该使用循环和 `charAt()`。

Example:

```java
if (character >= '0' && character <= '9') {
    // found a digit
}
```

---

# 2. Method 1 — isValidUsername / 方法 1

Implement:

实现：

```java
public static boolean isValidUsername(String username)
```

This method should return:

这个方法应该返回：

```text
true  → username is valid
false → username is invalid
```

```text
true  → 用户名有效
false → 用户名无效
```

### Suggested logic / 推荐逻辑

You can check the rules one by one:

你可以按照顺序检查每条规则：

```text
1. Check length
2. Check whether the first character is a letter
3. Loop through every character
4. Reject spaces
5. Look for at least one digit
6. Return true if everything passes
```

```text
1. 检查长度
2. 检查第一个字符是否为字母
3. 遍历每一个字符
4. 如果发现空格，返回 false
5. 寻找至少一个数字
6. 所有检查通过后返回 true
```

### Important / 注意

Before using:

```java
username.charAt(0)
```

make sure the string is not empty.

在使用：

```java
username.charAt(0)
```

之前，要确保字符串不是空字符串。

Otherwise, Java can throw:

```text
StringIndexOutOfBoundsException
```

This is part of practicing **safe indexing**.

这就是本次实验练习 **安全索引（safe indexing）** 的一部分。

---

# 3. Method 2 — countDigits / 方法 2

Implement:

实现：

```java
public static int countDigits(String username)
```

This method counts how many digits are inside the username.

这个方法用于计算用户名中有多少个数字。

Example:

```text
"lin2026" → 4
"abc123"  → 3
"student" → 0
```

### Suggested structure / 推荐结构

Start with a counter:

先创建一个计数器：

```java
int count = 0;
```

Then loop through the String:

然后遍历字符串：

```java
for (int i = 0; i < username.length(); i++) {
    char c = username.charAt(i);

    if (c >= '0' && c <= '9') {
        count++;
    }
}
```

Finally:

最后：

```java
return count;
```

---

# 4. Method 3 — initials / 方法 3

Implement:

实现：

```java
public static String initials(String firstName, String lastName)
```

The method should return the first letter of each name.

这个方法应该返回名字和姓氏的首字母。

For example:

```text
Lin + Zhang → L.Z.
```

You can use:

```java
char firstInitial = firstName.charAt(0);
char lastInitial = lastName.charAt(0);
```

Then construct a String:

然后组合成一个 String：

```java
return firstInitial + "." + lastInitial + ".";
```

Expected result:

```text
L.Z.
```

---

# 5. Required Report / 必须完成的报告

In `main`, inspect these usernames:

在 `main` 中检查以下用户名：

```text
"lin2026"
"ab 12"
"student"
```

For each username, print:

对于每一个用户名，打印：

1. the username — 用户名
2. whether it is valid — 是否有效
3. its digit count — 数字数量

### Example output / 输出示例

```text
Username: lin2026
Valid: true
Digits: 4

Username: ab 12
Valid: false
Digits: 2

Username: student
Valid: false
Digits: 0

Initials: L.Z.
```

Your exact formatting can be different.

你的具体输出格式可以不同。

---

# 6. Acceptance Checks / 验收检查

Your program must pass these tests.

你的程序必须通过以下测试。

### Test 1

```text
lin2026
```

Expected:

```text
Valid: true
Digits: 4
```

原因：

- length is 7
- starts with a letter
- contains no spaces
- contains 4 digits

---

### Test 2

```text
ab 12
```

Expected:

```text
Valid: false
```

原因：

```text
contains a space
包含空格
```

It has 2 digits, so:

```text
Digits: 2
```

---

### Test 3

```text
student
```

Expected:

```text
Valid: false
Digits: 0
```

原因：

```text
contains no digit
没有数字
```

---

### Test 4

Also test:

还要测试：

```text
1lin2026
```

Expected:

```text
Valid: false
```

原因：

```text
the first character is not a letter
第一个字符不是字母
```

---

# 7. Stretch Goal — maskUsername / 提升任务

Implement:

实现：

```java
public static String maskUsername(String username)
```

It should keep the first and last characters and replace everything between them with `*`.

它应该保留第一个和最后一个字符，并把中间的字符全部替换成 `*`。

Example:

```text
lin2026
```

becomes:

```text
l*****6
```

### Hint / 提示

You can use:

```java
char first = username.charAt(0);
char last = username.charAt(username.length() - 1);
```

Then build the middle part.

然后构造中间的 `*`。

One possible idea:

```text
first + "*" repeated several times + last
```

你可以理解为：

```text
第一个字符 + 若干个 * + 最后一个字符
```

Try to solve this yourself before looking for a more advanced Java solution.

建议先自己完成，不要马上使用更高级的 Java 方法。

---

# 8. Reflection / 思考题

### Why is this safer?

为什么下面这种写法更安全？

```java
username.equals("admin")
```

instead of:

```java
username == "admin"
```

### Think about / 思考

`==` is generally used to compare whether two references point to the same object.

`==` 通常用于比较两个引用是否指向同一个对象。

For Strings, you usually want to compare their **contents**.

而比较 String 时，我们通常真正想比较的是它们的**内容**。

Therefore:

```java
username.equals("admin")
```

checks whether the text inside the Strings is equal.

所以：

```java
username.equals("admin")
```

是在检查两个 String 的文本内容是否相同。

---

# 🧠 Key Concept / 核心概念

Remember:

记住：

```java
String a = "hello";
String b = "hello";
```

Do not think:

```java
a == b
```

means:

```text
"Do these two Strings contain the same text?"
```

不要把它理解成：

```text
“这两个 String 的内容是否相同？”
```

For content comparison, use:

比较 String 内容时使用：

```java
a.equals(b)
```

---

# 🔍 Useful String Methods / 有用的 String 方法

| Method | English | 中文 |
|---|---|---|
| `length()` | Get String length | 获取字符串长度 |
| `charAt(i)` | Get character at index `i` | 获取第 `i` 个字符 |
| `substring(a, b)` | Get part of a String | 截取字符串的一部分 |
| `indexOf()` | Find a character/String | 查找字符或字符串 |
| `equals()` | Compare String contents | 比较字符串内容 |

### Index reminder / 索引提醒

Java String indexes start at **0**.

Java 字符串的索引从 **0** 开始。

For:

```text
"lin2026"
```

the indexes are:

```text
 l  i  n  2  0  2  6
 0  1  2  3  4  5  6
```

So:

```java
username.charAt(0)
```

returns:

```text
'l'
```

And:

```java
username.charAt(username.length() - 1)
```

returns the last character:

```text
'6'
```

---

# 📝 Your Task / 你的任务

Complete `UsernameInspector.java`.

完成 `UsernameInspector.java`。

Before checking a solution, try to write the three required methods yourself:

在查看答案之前，先自己完成这三个方法：

```java
isValidUsername()
countDigits()
initials()
```

Then test:

然后测试：

```text
lin2026
ab 12
student
1lin2026
```

Finally, try the stretch goal:

最后尝试提升任务：

```java
maskUsername()
```

---

## Optional Focused Drills / 可选专项练习

See:

```text
./drills.md
```

查看：

```text
./drills.md
```

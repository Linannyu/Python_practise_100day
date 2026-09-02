# Chapter 03 — Conditionals

## 🎯 Learning Goals

- 用 boolean expression 写 `if`、`else if` 与 `else`；
- 正确安排互斥范围的顺序；
- 用逻辑运算符组合条件；
- 避开 assignment、dangling `else` 和 String 比较错误。

---

## 🐍 Python → ☕ Java

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

```java
if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else {
    System.out.println("C");
}
```

Java 使用 `else if`（两个词），条件必须是 `boolean`；不能像 Python 一样写 `if 1:`。

## 1. Conditions

| Python | Java | 结果 |
|---|---|---|
| `x == 4` | `x == 4` | boolean |
| `x != 4` | `x != 4` | boolean |
| `0 <= x <= 10` | `x >= 0 && x <= 10` | Java 要写两次 x |
| `name == "Lin"` | `name.equals("Lin")` | 比较 String 内容 |

## 2. Example

```java
public class Main {
    public static void main(String[] args) {
        int age = 12;
        if (age < 5) {
            System.out.println("free");
        } else if (age <= 12) {
            System.out.println("child");
        } else {
            System.out.println("standard");
        }
    }
}
```

先测试最具体或最高门槛的条件。`if (score >= 60)` 放在 `if (score >= 90)` 前会让 A 分支永远不可达。

## 3. Short circuit

`&&` 左侧为 false 时不计算右侧；所以 `i < arr.length && arr[i] > 0` 先检查下标，避免越界。

⚠️ **Common Mistakes**

- `if (score = 90)`：`=` 是赋值，不是 `==`；
- 在 `if (condition);` 后加分号；
- 写 `elif` 或冒号；
- 忽略大于等于/小于等于边界。

🧠 **AP CSA Notes**：FRQ 评分常在边界值（0、60、90、最大/最小）上区分正确代码。

✅ **Before Practice**

- 我能把 Python 范围判断翻成 Java。
- 我能读出任意 `else` 属于哪个 `if`。
- 我知道 String 内容比较用 `.equals()`。

📝 **Practice**：完成 [Chapter 03 Practice](./practice.md)。

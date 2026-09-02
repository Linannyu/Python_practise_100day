# Chapter 04 — Loops

## 🎯 Learning Goals

- 用 `while` 和三段式 `for` 重写 Python 循环；
- 选择普通 `for` 或 enhanced for；
- 用循环做累计、计数、搜索和修改；
- 避开 off-by-one、无限循环和错误的上界。

---

## 🐍 Python → ☕ Java

```python
for i in range(10):
    print(i)
```

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

`for (initialization; condition; update)` 的三个部分分别在开始一次、每轮前、每轮后执行。`range(10)` 对应 `i = 0; i < 10; i++`。

## 1. `while` 与 `for`

```java
int x = 0;
while (x < 3) {
    System.out.println(x);
    x++;
}
```

当未知重复次数时常用 `while`；计数、按下标遍历时常用 `for`。两个都必须让条件最终变为 false。

## 2. Enhanced for

```python
for value in numbers:
    print(value)
```

```java
for (int value : numbers) {
    System.out.println(value);
}
```

它适合读取每个元素；想访问 index、替换 array 元素或倒序时用普通 `for`。

## 3. Example

```java
public class Main {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; i <= 5; i++) {
            sum += i;
        }
        System.out.println(sum); // 15
    }
}
```

`break` 直接结束循环；`continue` 跳过当前轮的剩余代码。

⚠️ **Common Mistakes**

- `i <= arr.length` 导致访问 `arr[arr.length]`；
- 忘记 `i++`；
- 在 enhanced for 中改 `value`，以为原 array 会改变；
- 外层循环里忘记重置每行/每轮的累加变量。

🧠 **AP CSA Notes**：写循环时先说清楚不变量：`sum` 已累计哪些值、`i` 下一步会访问哪里。

✅ **Before Practice**

- 我能解释循环的开始、继续条件和更新。
- 我能在 `0..length-1` 的边界内遍历 array。
- 我能选择 `break`、`continue` 或无须它们的结构。

📝 **Practice**：完成 [Chapter 04 Practice](./practice.md)。

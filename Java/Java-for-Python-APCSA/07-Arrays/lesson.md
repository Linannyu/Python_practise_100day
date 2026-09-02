# Chapter 07 — Arrays

## 🎯 Learning Goals

- 创建、读取与修改固定长度的 array；
- 选择下标循环或 enhanced for；
- 写求和、计数、最大/最小和替换遍历；
- 安全处理 index 边界。

---

## 🐍 Python → ☕ Java

```python
numbers = [1, 2, 3, 4]
numbers[0] = 9
print(len(numbers))
```

```java
int[] numbers = {1, 2, 3, 4};
numbers[0] = 9;
System.out.println(numbers.length);
```

Python list 可以变长；Java array 创建后长度固定，且元素类型固定。

## 1. Create and access

```java
int[] scores = new int[3]; // {0, 0, 0}
scores[0] = 90;
```

合法 index 是 `0` 到 `scores.length - 1`。array 的长度是字段 `length`，不是方法。

## 2. Two traversal patterns

```java
for (int i = 0; i < scores.length; i++) {
    scores[i] += 5; // use i to modify
}

for (int score : scores) {
    System.out.println(score); // read each value
}
```

## 3. Example: maximum

```java
public class Main {
    public static void main(String[] args) {
        int[] values = {5, 2, 9, 4};
        int max = values[0];
        for (int value : values) {
            if (value > max) {
                max = value;
            }
        }
        System.out.println(max);
    }
}
```

⚠️ **Common Mistakes**

- `arr.length()`；array 是 `arr.length`；
- `i <= arr.length`；
- 以为 `for (int x : arr) { x = 0; }` 会改变 array；
- 以为 array 可以 `.add()`。

🧠 **AP CSA Notes**：array traversal 是核心 FRQ 技能。先判断题目是“读值”“改值”还是“返回计算结果”。

✅ **Before Practice**

- 我能创建 literal 与指定长度的 array。
- 我能写不会越界的 traversal。
- 我能解释为什么最大值通常从 `arr[0]` 开始。

📝 **Practice**：完成 [Chapter 07 Practice](./practice.md)。

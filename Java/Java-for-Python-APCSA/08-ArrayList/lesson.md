# Chapter 08 — ArrayList

## 🎯 Learning Goals

- 创建与导入 `ArrayList`；
- 用 `add/get/set/remove/size` 操作列表；
- 区分 array 和 ArrayList；
- 避开 `remove` overload 与循环删除下标陷阱。

---

## 🐍 Python → ☕ Java

```python
numbers = []
numbers.append(10)
numbers[0] = 20
len(numbers)
```

```java
ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(10);
numbers.set(0, 20);
numbers.size();
```

需要 `import java.util.ArrayList;`。泛型 `<Integer>` 说明元素类型；不能写 `<int>`。

## 1. Array vs ArrayList

| Operation | `int[]` | `ArrayList<Integer>` |
|---|---|---|
| length | `arr.length` | `list.size()` |
| get | `arr[i]` | `list.get(i)` |
| replace | `arr[i] = x` | `list.set(i, x)` |
| grow | impossible | `list.add(x)` |

## 2. Example

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Lin");
        names.add("Ada");
        names.remove(0);
        System.out.println(names.get(0));
    }
}
```

`remove(0)` removes index 0. For `ArrayList<Integer>`, use `remove(Integer.valueOf(5))` when you mean remove the value 5, not index 5.

## 3. Python vs Java

Python list 变量本身可引用混合类型；Java generic list has one declared element type. Java 会对 `int` 与 `Integer` 自动 boxing/unboxing，但类型仍重要。

⚠️ **Common Mistakes**

- 忘记 import；
- 写 `list[0]`、`list.length`；
- 误解 `remove(3)`；
- 正向循环删除元素后仍 `i++`，跳过移动过来的元素。

🧠 **AP CSA Notes**：删除符合条件的元素常倒序循环，或在删除后不增加 index。

✅ **Before Practice**

- 我能用五个核心方法操作 list。
- 我能解释 `Integer` 的作用。
- 我能选择安全的删除循环方向。

📝 **Practice**：完成 [Chapter 08 Practice](./practice.md)。

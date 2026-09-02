# Chapter 04 — Loops Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 04-01 — Zero to four

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) System.out.println(i);
    }
}
```

### Explanation

The strict upper bound makes 4 the last value.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-02 — Countdown

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int i = 5; while (i >= 1) { System.out.println(i); i--; }
    }
}
```

### Explanation

The update ensures the while condition eventually becomes false.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-03 — Even numbers

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        for (int i = 2; i <= 20; i += 2) System.out.println(i);
    }
}
```

### Explanation

The update itself moves only through even values.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-04 — Sum to n

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 5, sum = 0; for (int i = 1; i <= n; i++) sum += i; System.out.println(sum);
    }
}
```

### Explanation

`sum` is an accumulator updated once for each required value.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-05 — Repeated word

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Java"; int times = 3; for (int i = 0; i < times; i++) System.out.println(word);
    }
}
```

### Explanation

The loop runs exactly `times` times.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-06 — Count multiples

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 20, count = 0; for (int i = 1; i <= n; i++) if (i % 3 == 0) count++; System.out.println(count);
    }
}
```

### Explanation

A counter changes only when the condition is met.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-07 — Digit sum

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 407, sum = 0; while (n > 0) { sum += n % 10; n /= 10; } System.out.println(sum);
    }
}
```

### Explanation

Remainder gets the last digit; integer division removes it.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-08 — First multiple

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        for (int i = 1; ; i++) { if (i % 7 == 0 && i % 9 == 0) { System.out.println(i); break; } }
    }
}
```

### Explanation

The open-ended loop is safely terminated when the first match is found.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-09 — Skip negatives

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int[] values = {2, -1, 0, 5}; for (int value : values) { if (value < 0) continue; System.out.println(value); }
    }
}
```

### Explanation

`continue` skips remaining work for only the negative element.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-10 — Product

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 5, product = 1; for (int i = 2; i <= n; i++) product *= i; System.out.println(product);
    }
}
```

### Explanation

Starting at 1 preserves multiplication correctly.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-11 — Count digits

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 0, count = 1; if (n != 0) { count = 0; while (n > 0) { count++; n /= 10; } } System.out.println(count);
    }
}
```

### Explanation

Zero has one digit, so it needs a special starting case.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-12 — Largest even

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int[] values = {3, 8, 1, 6}; Integer best = null; for (int v : values) if (v % 2 == 0 && (best == null || v > best)) best = v; System.out.println(best == null ? "none" : best);
    }
}
```

### Explanation

`null` represents the fact that no even candidate has been seen yet.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-13 — Number pattern

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        for (int row = 1; row <= 5; row++) { for (int col = 1; col <= row; col++) System.out.print(col + (col == row ? "" : " ")); System.out.println(); }
    }
}
```

### Explanation

The inner loop restarts for every row and ends at that row number.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-14 — sumOdd method

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static int sumOdd(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i += 2) sum += i;
    return sum;
}

    public static void main(String[] args) {
        System.out.println(sumOdd(7));
    }
}
```

### Explanation

Starting at 1 and adding 2 visits each positive odd number once.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

## Problem 04-15 — Trace and repair

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int[] values = {4, 5, 6}; for (int i = 0; i < values.length; i++) System.out.println(values[i]);
    }
}
```

### Explanation

`values.length` is one past the final legal index, so the condition must be `<`.

### Python Comparison

Python `range` creates an iteration sequence; Java spells out initialization, continuation condition and update.

---

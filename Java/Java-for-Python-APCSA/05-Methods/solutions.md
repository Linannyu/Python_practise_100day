# Chapter 05 — Methods Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 05-01 — Greeting

**Level:** Level 1

### Solution

```java
public class Main {
    public static void greet(String name) { System.out.println("Hello, " + name + "!"); }

    public static void main(String[] args) {
        greet("Lin");
    }
}
```

### Explanation

The `void` method performs output but returns no value.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-02 — Double it

**Level:** Level 1

### Solution

```java
public class Main {
    public static int doubleIt(int n) { return 2 * n; }

    public static void main(String[] args) {
        System.out.println(doubleIt(7));
    }
}
```

### Explanation

The return expression has type int.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-03 — Absolute difference

**Level:** Level 1

### Solution

```java
public class Main {
    public static int difference(int a, int b) { return Math.abs(a - b); }

    public static void main(String[] args) {
        System.out.println(difference(3, 10));
    }
}
```

### Explanation

`Math.abs` makes the difference nonnegative.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-04 — Is positive

**Level:** Level 1

### Solution

```java
public class Main {
    public static boolean isPositive(int n) { return n > 0; }

    public static void main(String[] args) {
        System.out.println(isPositive(-1));
    }
}
```

### Explanation

The comparison already produces the required boolean.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-05 — First character

**Level:** Level 1

### Solution

```java
public class Main {
    public static char firstChar(String s) { return s.charAt(0); }

    public static void main(String[] args) {
        System.out.println(firstChar("Java"));
    }
}
```

### Explanation

The prompt guarantees a nonempty String, so index 0 is valid.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-06 — Average

**Level:** Level 2

### Solution

```java
public class Main {
    public static double average(int a, int b) { return (a + b) / 2.0; }

    public static void main(String[] args) {
        System.out.println(average(3, 4));
    }
}
```

### Explanation

`2.0` makes this floating-point division.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-07 — In range

**Level:** Level 2

### Solution

```java
public class Main {
    public static boolean inRange(int value, int low, int high) { return value >= low && value <= high; }

    public static void main(String[] args) {
        System.out.println(inRange(5, 0, 5));
    }
}
```

### Explanation

Both endpoints are included.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-08 — Repeat

**Level:** Level 2

### Solution

```java
public class Main {
    public static String repeat(String word, int times) { String result = ""; for (int i = 0; i < times; i++) result += word; return result; }

    public static void main(String[] args) {
        System.out.println(repeat("ha", 3));
    }
}
```

### Explanation

The accumulator begins empty and grows once per repetition.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-09 — Larger

**Level:** Level 2

### Solution

```java
public class Main {
    public static int larger(int a, int b) { return a > b ? a : b; }

    public static void main(String[] args) {
        System.out.println(larger(4, 9));
    }
}
```

### Explanation

The conditional expression selects one int.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-10 — Grade label

**Level:** Level 2

### Solution

```java
public class Main {
    public static String gradeLabel(int s) { if (s >= 90) return "A"; if (s >= 80) return "B"; if (s >= 70) return "C"; if (s >= 60) return "D"; return "F"; }

    public static void main(String[] args) {
        System.out.println(gradeLabel(82));
    }
}
```

### Explanation

Each return exits as soon as a range matches.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-11 — Digit count

**Level:** Level 3

### Solution

```java
public class Main {
    public static int digitCount(int n) { n = Math.abs(n); if (n == 0) return 1; int c = 0; while (n > 0) { c++; n /= 10; } return c; }

    public static void main(String[] args) {
        System.out.println(digitCount(-120));
    }
}
```

### Explanation

Absolute value handles negative input; zero needs one digit.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-12 — Square

**Level:** Level 3

### Solution

```java
public class Main {
    public static int square(int x) { return x * x; }

    public static void main(String[] args) {
        System.out.println(square(-3));
    }
}
```

### Explanation

Multiplying a number by itself also works for negative input.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-13 — Palindrome number

**Level:** Level 3

### Solution

```java
public class Main {
    public static boolean isPalindromeNumber(int n) { if (n < 0) return false; int original = n, reverse = 0; while (n > 0) { reverse = reverse * 10 + n % 10; n /= 10; } return original == reverse; }

    public static void main(String[] args) {
        System.out.println(isPalindromeNumber(1221));
    }
}
```

### Explanation

Reversing the digits and comparing primitive ints tests the palindrome condition.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-14 — Count multiples

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static int countMultiples(int start, int end, int divisor) { int count = 0; for (int i = start; i <= end; i++) if (i % divisor == 0) count++; return count; }

    public static void main(String[] args) {
        System.out.println(countMultiples(1, 10, 3));
    }
}
```

### Explanation

The inclusive loop exactly matches the requested interval.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

## Problem 05-15 — Overload design

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static String describe(int n) { return "number: " + n; }
public static String describe(String s) { return "word: " + s; }

    public static void main(String[] args) {
        System.out.println(describe(7)); System.out.println(describe("Java"));
    }
}
```

### Explanation

Same name with different parameter types is legal overloading.

### Python Comparison

Python functions infer return types; Java method signatures promise a return type to the caller.

---

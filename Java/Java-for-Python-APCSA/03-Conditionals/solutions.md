# Chapter 03 — Conditionals Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 03-01 — Sign

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = -4; if (n > 0) System.out.println("positive"); else if (n < 0) System.out.println("negative"); else System.out.println("zero");
    }
}
```

### Explanation

The three branches are mutually exclusive and cover every int.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-02 — Even label

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 7; if (n % 2 == 0) System.out.println("even"); else System.out.println("odd");
    }
}
```

### Explanation

A remainder of zero means evenly divisible by 2.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-03 — Pass or retry

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int score = 59; if (score >= 60) System.out.println("pass"); else System.out.println("retry");
    }
}
```

### Explanation

The comparison includes the passing boundary.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-04 — Teenager

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int age = 16; System.out.println(age >= 13 && age <= 19);
    }
}
```

### Explanation

Java writes both comparisons explicitly; it cannot chain them like Python.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-05 — Exact word

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String answer = "yes"; if (answer.equals("yes")) System.out.println("accepted"); else System.out.println("not accepted");
    }
}
```

### Explanation

`.equals` compares String characters rather than object identity.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-06 — Letter grade

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int score = 84; if (score >= 90) System.out.println("A"); else if (score >= 80) System.out.println("B"); else if (score >= 70) System.out.println("C"); else if (score >= 60) System.out.println("D"); else System.out.println("F");
    }
}
```

### Explanation

Highest thresholds must be checked first.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-07 — Ticket price

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int age = 70; int price; if (age < 5) price = 0; else if (age <= 12) price = 8; else if (age >= 65) price = 9; else price = 12; System.out.println(price);
    }
}
```

### Explanation

The branches assign exactly one price.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-08 — Valid rectangle

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int width = 3, height = 0; if (width > 0 && height > 0) System.out.println("valid"); else System.out.println("invalid");
    }
}
```

### Explanation

Both dimensions must be positive.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-09 — Largest of two

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int a = 4, b = 9; if (a > b) System.out.println(a); else System.out.println(b);
    }
}
```

### Explanation

With distinct inputs, one of the two branches selects the maximum.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-10 — Password gate

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String password = "java123"; if (password.equals("java123")) System.out.println("welcome"); else System.out.println("denied");
    }
}
```

### Explanation

Never use `==` for String content.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-11 — Median of three

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int a = 9, b = 2, c = 5; int mid; if ((a > b && a < c) || (a < b && a > c)) mid = a; else if ((b > a && b < c) || (b < a && b > c)) mid = b; else mid = c; System.out.println(mid);
    }
}
```

### Explanation

The median is the one value between the other two.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-12 — Leap year

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int year = 2024; boolean leap = year % 400 == 0 || (year % 4 == 0 && year % 100 != 0); System.out.println(leap ? "leap" : "common");
    }
}
```

### Explanation

Parentheses keep the 4-but-not-100 rule together.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-13 — Shipping

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        double subtotal = 42; boolean member = true; double shipping = (subtotal >= 50 || member) ? 0.0 : 6.99; System.out.println(shipping);
    }
}
```

### Explanation

The boolean condition directly chooses the correct price.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-14 — Season method

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static String season(int month) {
    if (month == 12 || month == 1 || month == 2) return "winter";
    if (month >= 3 && month <= 5) return "spring";
    if (month >= 6 && month <= 8) return "summer";
    if (month >= 9 && month <= 11) return "fall";
    return "invalid";
}

    public static void main(String[] args) {
        System.out.println(season(10));
    }
}
```

### Explanation

Every valid month belongs to one range; the final return handles invalid input.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

## Problem 03-15 — Code trace

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int x = 8; if (x > 5) { if (x < 8) x++; else x--; } System.out.println(x);
    }
}
```

### Explanation

The outer condition is true, inner condition false, so x becomes 7.

### Python Comparison

Python uses indentation and `elif`; Java needs a boolean inside parentheses, braces, and `else if`.

---

# Chapter 06 — String Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 06-01 — Length

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Java"; System.out.println(word.length());
    }
}
```

### Explanation

`length()` is a String method.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-02 — Last character

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Java"; System.out.println(word.charAt(word.length() - 1));
    }
}
```

### Explanation

Last index is length minus one.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-03 — First three

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Python"; System.out.println(word.substring(0, 3));
    }
}
```

### Explanation

The end index is excluded.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-04 — Uppercase

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Java"; System.out.println(word.toUpperCase()); System.out.println(word);
    }
}
```

### Explanation

String methods return a new String; the original binding stays unchanged.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-05 — Content match

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String command = "start"; System.out.println(command.equals("start") ? "go" : "wait");
    }
}
```

### Explanation

`.equals` is content comparison.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-06 — First occurrence

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String text = "computer", target = "put"; int i = text.indexOf(target); System.out.println(i < 0 ? "missing" : i);
    }
}
```

### Explanation

`indexOf` returns -1 when no match exists.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-07 — Initials

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String first = "Lin", last = "Ada"; System.out.println(first.charAt(0) + "." + last.charAt(0) + ".");
    }
}
```

### Explanation

Characters concatenate with Strings into the requested text.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-08 — Remove ends

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Java"; System.out.println(word.substring(1, word.length() - 1));
    }
}
```

### Explanation

The substring starts after the first and ends before the last.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-09 — Character counter

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "banana"; char target = 'a'; int count = 0; for (int i = 0; i < word.length(); i++) if (word.charAt(i) == target) count++; System.out.println(count);
    }
}
```

### Explanation

Use `==` for primitive chars, not for String objects.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-10 — Reverse

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String word = "Java", reverse = ""; for (int i = word.length() - 1; i >= 0; i--) reverse += word.charAt(i); System.out.println(reverse);
    }
}
```

### Explanation

The loop walks from the final legal index down to 0.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-11 — Vowel count

**Level:** Level 3

### Solution

```java
public class Main {
    public static int countVowels(String text) { int c = 0; text = text.toLowerCase(); for (int i = 0; i < text.length(); i++) if ("aeiou".indexOf(text.charAt(i)) >= 0) c++; return c; }

    public static void main(String[] args) {
        System.out.println(countVowels("Apples"));
    }
}
```

### Explanation

Lowercasing once makes the vowel test case-insensitive.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-12 — Palindrome

**Level:** Level 3

### Solution

```java
public class Main {
    public static boolean isPalindrome(String text) { for (int i = 0; i < text.length() / 2; i++) if (text.charAt(i) != text.charAt(text.length() - 1 - i)) return false; return true; }

    public static void main(String[] args) {
        System.out.println(isPalindrome("level"));
    }
}
```

### Explanation

Only symmetric pairs need comparison.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-13 — Word censor

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String text = "learn Java", banned = "Java"; System.out.println(text.indexOf(banned) >= 0 ? "blocked" : "allowed");
    }
}
```

### Explanation

Any nonnegative index means the target occurs.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-14 — Middle

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static String middle(String s) { int n = s.length(); return n % 2 == 1 ? s.substring(n / 2, n / 2 + 1) : s.substring(n / 2 - 1, n / 2 + 1); }

    public static void main(String[] args) {
        System.out.println(middle("javaa"));
    }
}
```

### Explanation

Integer division locates the central index; odd and even lengths need different slices.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

## Problem 06-15 — compareTo trace

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("apple".compareTo("banana") < 0 ? "before" : "after"); System.out.println("cat".compareTo("cat") == 0 ? "same" : "different");
    }
}
```

### Explanation

Use the sign of `compareTo`, not a particular numeric result.

### Python Comparison

Python string slicing and Java String methods both create text values; Java asks you to call the method explicitly.

---

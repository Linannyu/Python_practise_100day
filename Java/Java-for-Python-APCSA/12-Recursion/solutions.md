# Chapter 12 — Recursion Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 12-01 — Create / basic operation

**Level:** Level 1

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        countdown(3);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-02 — Read / inspect

**Level:** Level 1

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        countUp(3);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-03 — Modify safely

**Level:** Level 1

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(sumTo(5));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-04 — Count with a loop

**Level:** Level 1

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(factorial(5));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-05 — Return a result

**Level:** Level 1

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(power(2,5));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-06 — Combine two ideas

**Level:** Level 2

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(sumEvenTo(6));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-07 — Search or compute

**Level:** Level 2

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(digitSum(407));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-08 — Boundary-aware traversal

**Level:** Level 2

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(recursiveLength("Java"));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-09 — Transform data

**Level:** Level 2

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(countChar("banana", 'a'));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-10 — Design a helper

**Level:** Level 2

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        printReverse("Java");
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-11 — Challenge algorithm

**Level:** Level 3

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(isPalindrome("level"));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-12 — Challenge edge case

**Level:** Level 3

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(arraySum(new int[]{1,2,3},0));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-13 — Challenge composition

**Level:** Level 3

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(countBinaryDigits(8));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-14 — FRQ method

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        System.out.println(productTo(5));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

## Problem 12-15 — FRQ explanation

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static void countdown(int n){if(n==0)return;System.out.println(n);countdown(n-1);}
public static void countUp(int n){if(n==0)return;countUp(n-1);System.out.println(n);}
public static int sumTo(int n){return n==0?0:n+sumTo(n-1);}
public static int factorial(int n){return n==0?1:n*factorial(n-1);}
public static int power(int b,int e){return e==0?1:b*power(b,e-1);}
public static int sumEvenTo(int n){if(n<=0)return 0;return (n%2==0?n:0)+sumEvenTo(n-1);}
public static int digitSum(int n){return n<10?n:n%10+digitSum(n/10);}
public static int recursiveLength(String s){return s.equals("")?0:1+recursiveLength(s.substring(1));}
public static int countChar(String s,char t){return s.equals("")?0:(s.charAt(0)==t?1:0)+countChar(s.substring(1),t);}
public static void printReverse(String s){if(s.equals(""))return;printReverse(s.substring(1));System.out.print(s.charAt(0));}
public static boolean isPalindrome(String s){return s.length()<=1||(s.charAt(0)==s.charAt(s.length()-1)&&isPalindrome(s.substring(1,s.length()-1)));}
public static int arraySum(int[]a,int i){return i==a.length?0:a[i]+arraySum(a,i+1);}
public static int countBinaryDigits(int n){return n<2?1:1+countBinaryDigits(n/2);}
public static int productTo(int n){return n==0?1:n*productTo(n-1);}
public static void mystery(int n){if(n==0)return;System.out.print(n+" ");mystery(n-1);System.out.print(n+" ");}

    public static void main(String[] args) {
        mystery(3);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

The recursive idea is identical in Python and Java: stop at a base case, then call a strictly smaller version of the same problem.

---

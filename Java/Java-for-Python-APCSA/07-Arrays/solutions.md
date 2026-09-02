# Chapter 07 — Arrays Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 07-01 — Create / basic operation

**Level:** Level 1

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {2, 4, 6, 8}; for (int x : a) System.out.println(x);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-02 — Read / inspect

**Level:** Level 1

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {2, 4, 6}; System.out.println(a.length); System.out.println(a[0]); System.out.println(a[a.length - 1]);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-03 — Modify safely

**Level:** Level 1

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {1, 2, 3}; int sum = 0; for (int x : a) sum += x; System.out.println(sum);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-04 — Count with a loop

**Level:** Level 1

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {-1, 0, 2}; int c = 0; for (int x : a) if (x > 0) c++; System.out.println(c);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-05 — Return a result

**Level:** Level 1

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {1, 2, 3}; for (int i = 0; i < a.length; i++) a[i]++; for (int x : a) System.out.println(x);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-06 — Combine two ideas

**Level:** Level 2

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        System.out.println(max(new int[]{5, 2, 9}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-07 — Search or compute

**Level:** Level 2

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        System.out.println(firstIndex(new int[]{2, 7, 7}, 7));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-08 — Boundary-aware traversal

**Level:** Level 2

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {1, 2, 3}; for (int i = a.length - 1; i >= 0; i--) System.out.println(a[i]);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-09 — Transform data

**Level:** Level 2

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {1, 2, 3}; int t = a[0]; a[0] = a[a.length - 1]; a[a.length - 1] = t; for (int x : a) System.out.println(x);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-10 — Design a helper

**Level:** Level 2

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {1, 2, 6}; double avg = (double) (a[0] + a[1] + a[2]) / a.length; for (int x : a) if (x > avg) System.out.println(x);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-11 — Challenge algorithm

**Level:** Level 3

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        System.out.println(secondLargest(new int[]{3, 9, 7, 9}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-12 — Challenge edge case

**Level:** Level 3

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        System.out.println(adjacentIncreases(new int[]{1, 3, 2, 5}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-13 — Challenge composition

**Level:** Level 3

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        int[] a = {-2, 3, -1}; System.out.println(replaceNegatives(a));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-14 — FRQ method

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        System.out.println(sumPositive(new int[]{-2, 3, 4}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

## Problem 07-15 — FRQ explanation

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static int max(int[] a){int m=a[0];for(int x:a)if(x>m)m=x;return m;}
public static int firstIndex(int[] a,int t){for(int i=0;i<a.length;i++)if(a[i]==t)return i;return -1;}
public static int secondLargest(int[] a){int m=Integer.MIN_VALUE,s=Integer.MIN_VALUE;for(int x:a){if(x>m){s=m;m=x;}else if(x> s&&x<m)s=x;}return s;}
public static int adjacentIncreases(int[] a){int c=0;for(int i=0;i<a.length-1;i++)if(a[i]<a[i+1])c++;return c;}
public static int replaceNegatives(int[] a){int c=0;for(int i=0;i<a.length;i++)if(a[i]<0){a[i]=0;c++;}return c;}
public static int sumPositive(int[] a){int s=0;for(int x:a)if(x>0)s+=x;return s;}
public static boolean hasConsecutiveDuplicates(int[] a){for(int i=0;i<a.length-1;i++)if(a[i]==a[i+1])return true;return false;}

    public static void main(String[] args) {
        System.out.println(hasConsecutiveDuplicates(new int[]{1, 2, 2}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python lists grow; Java arrays have a fixed `length` and use an index when elements need modification.

---

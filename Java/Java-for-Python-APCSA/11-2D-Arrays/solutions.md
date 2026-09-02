# Chapter 11 — 2D Arrays Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 11-01 — Create / basic operation

**Level:** Level 1

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,4}}; System.out.println(g[1][1]);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-02 — Read / inspect

**Level:** Level 1

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,4}}; System.out.println(g.length); System.out.println(g[0].length);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-03 — Modify safely

**Level:** Level 1

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,4}}; for(int r=0;r<g.length;r++) for(int c=0;c<g[r].length;c++) System.out.println(g[r][c]);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-04 — Count with a loop

**Level:** Level 1

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        System.out.println(total(new int[][]{{1,2},{3,4}}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-05 — Return a result

**Level:** Level 1

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        System.out.println(countAbove(new int[][]{{0,1},{0,2}}, -1) - 2);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-06 — Combine two ideas

**Level:** Level 2

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,4}}; for(int r=0;r<g.length;r++){int s=0;for(int x:g[r])s+=x;System.out.println(s);}
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-07 — Search or compute

**Level:** Level 2

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        System.out.println(max2d(new int[][]{{1,8},{3,4}}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-08 — Boundary-aware traversal

**Level:** Level 2

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{-1,2},{-3,4}}; for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(g[r][c]<0)g[r][c]=0; System.out.println(g[0][0]);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-09 — Transform data

**Level:** Level 2

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,4}}; int s=0;for(int i=0;i<g.length;i++)s+=g[i][i];System.out.println(s);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-10 — Design a helper

**Level:** Level 2

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,2}}; for(int r=0;r<g.length;r++)for(int x:g[r])if(x==2){System.out.println(r);break;}
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-11 — Challenge algorithm

**Level:** Level 3

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2},{3,4}}; for(int c=0;c<g[0].length;c++){int s=0;for(int r=0;r<g.length;r++)s+=g[r][c];System.out.println(s);}
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-12 — Challenge edge case

**Level:** Level 3

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        System.out.println(neighborPairs(new int[][]{{1,1,2},{3,3}}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-13 — Challenge composition

**Level:** Level 3

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        System.out.println(total(new int[][]{{1,2,3},{4},{5,6}}));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-14 — FRQ method

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        System.out.println(countAbove(new int[][]{{1,7},{9,2}}, 5));
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

## Problem 11-15 — FRQ explanation

**Level:** AP CSA Style

### Solution

```java
public class Main {
    public static int total(int[][]g){int s=0;for(int[]r:g)for(int x:r)s+=x;return s;}
public static int max2d(int[][]g){int m=g[0][0];for(int[]r:g)for(int x:r)if(x>m)m=x;return m;}
public static int neighborPairs(int[][]g){int c=0;for(int[]r:g)for(int i=0;i<r.length-1;i++)if(r[i]==r[i+1])c++;return c;}
public static int countAbove(int[][]g,int t){int c=0;for(int[]r:g)for(int x:r)if(x>t)c++;return c;}
public static void makeBorderZero(int[][]g){for(int r=0;r<g.length;r++)for(int c=0;c<g[r].length;c++)if(r==0||r==g.length-1||c==0||c==g[r].length-1)g[r][c]=0;}

    public static void main(String[] args) {
        int[][] g={{1,2,3},{4,5,6},{7,8,9}}; makeBorderZero(g); for(int[] row:g)for(int x:row)System.out.println(x);
    }
}
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list-of-lists and Java 2D arrays both use `[row][column]`; Java asks for `.length` at each level.

---

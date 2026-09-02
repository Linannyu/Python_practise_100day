# Chapter 08 — ArrayList Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 08-01 — Create / basic operation

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(); a.add("Lin"); a.add("Ada"); a.add("Sam"); for (String s : a) System.out.println(s);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-02 — Read / inspect

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(); a.add("Lin"); System.out.println(a.size()); System.out.println(a.get(0));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-03 — Modify safely

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(); a.add("A"); a.add("B"); a.set(1, "Lin"); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-04 — Count with a loop

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(); a.add("A"); a.add("B"); a.add("C"); a.remove(2); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-05 — Return a result

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a = new java.util.ArrayList<>(); a.add(3); a.add(5); a.add(7); System.out.println(a.get(0) + a.get(1) + a.get(2));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-06 — Combine two ideas

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            System.out.println(countLong(java.util.Arrays.asList("cat", "apple", "pear")));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-07 — Search or compute

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a = new java.util.ArrayList<>(java.util.Arrays.asList(1, 2)); for (int i=0;i<a.size();i++) a.set(i,a.get(i)*2); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-08 — Boundary-aware traversal

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            System.out.println(find(java.util.Arrays.asList("a", "b"), "b"));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-09 — Transform data

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a = new java.util.ArrayList<>(java.util.Arrays.asList(1, -2, 3)); for (int i=a.size()-1;i>=0;i--) if(a.get(i)<0)a.remove(i); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-10 — Design a helper

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(); a.add("Lin"); if (!contains(a,"Ada")) a.add("Ada"); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-11 — Challenge algorithm

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a = new java.util.ArrayList<>(java.util.Arrays.asList(1,1,2,2)); removeNeighborDuplicates(a); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-12 — Challenge edge case

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a = new java.util.ArrayList<>(java.util.Arrays.asList(0,2,0,3)); moveZeros(a); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-13 — Challenge composition

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            System.out.println(longest(java.util.Arrays.asList("a", "pear", "cat")));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-14 — FRQ method

**Level:** AP CSA Style

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(java.util.Arrays.asList("a", "apple")); System.out.println(removeShortWords(a,2));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

## Problem 08-15 — FRQ explanation

**Level:** AP CSA Style

### Solution

```java
import java.util.*;
public class Main {
        public static int countLong(java.util.List<String> a){int c=0;for(String s:a)if(s.length()>=5)c++;return c;}
    public static int find(java.util.List<String>a,String t){for(int i=0;i<a.size();i++)if(a.get(i).equals(t))return i;return -1;}
    public static boolean contains(java.util.List<String>a,String t){return find(a,t)>=0;}
    public static void removeNeighborDuplicates(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>0;i--)if(a.get(i).equals(a.get(i-1)))a.remove(i);}
    public static void moveZeros(java.util.ArrayList<Integer>a){for(int i=a.size()-1;i>=0;i--)if(a.get(i)==0){a.remove(i);a.add(0);}}
    public static String longest(java.util.List<String>a){String best=a.get(0);for(String s:a)if(s.length()>best.length())best=s;return best;}
    public static int removeShortWords(java.util.ArrayList<String>a,int n){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i).length()<n){a.remove(i);c++;}return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a = new java.util.ArrayList<>(java.util.Arrays.asList(1,2,3,2)); a.remove(Integer.valueOf(2)); System.out.println(a);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Python list methods map most closely to Java `ArrayList`, but Java uses `get`, `set`, `size`, and a declared element type.

---

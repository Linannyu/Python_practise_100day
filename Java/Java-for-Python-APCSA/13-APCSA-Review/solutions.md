# Chapter 13 — AP CSA Review Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 13-01 — Create / basic operation

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            String s="hi"; int[] a={1}; java.util.ArrayList<Integer> l=new java.util.ArrayList<>(); l.add(1); System.out.println(s.length());System.out.println(a.length);System.out.println(l.size());
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-02 — Read / inspect

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(average(new int[]{1,2,4}));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-03 — Modify safely

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(isJava(null));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-04 — Count with a loop

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(new java.util.Random().nextInt(6)+1);
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-05 — Return a result

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            // compile: semicolon; runtime: bounds; logic: wrong result
        System.out.println("labels recorded");
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-06 — Combine two ideas

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(averagePositive(new int[]{-1,2,4}));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-07 — Search or compute

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Student> s=new java.util.ArrayList<>();s.add(new Student(70));s.add(new Student(50));System.out.println(countPassing(s));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-08 — Boundary-aware traversal

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(rowMax(new int[][]{{1,9},{2,3}},0));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-09 — Transform data

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(wordScore("cat"));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-10 — Design a helper

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a=new java.util.ArrayList<>(java.util.Arrays.asList(1,2));for(int i=0;i<a.size();i++)System.out.println(a.get(i));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-11 — Challenge algorithm

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(mostFrequent(new int[]{1,2,1,2,2}));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-12 — Challenge edge case

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Integer> a=new java.util.ArrayList<>(java.util.Arrays.asList(50,60,40));System.out.println(removeFailing(a));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-13 — Challenge composition

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(recursiveVowelCount("Java"));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-14 — FRQ method

**Level:** AP CSA Style

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            System.out.println(longestIncreasingRun(new int[]{1,2,1,2,3}));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

## Problem 13-15 — FRQ explanation

**Level:** AP CSA Style

### Solution

```java
import java.util.*;
public class Main {
        public static double average(int[]a){int s=0;for(int x:a)s+=x;return(double)s/a.length;}
    public static boolean isJava(String s){return "Java".equals(s);}
    public static double averagePositive(int[]a){int s=0,c=0;for(int x:a)if(x>0){s+=x;c++;}return c==0?0.0:(double)s/c;}
    public static class Student{int score;Student(int s){score=s;}}
    public static int countPassing(java.util.ArrayList<Student>a){int c=0;for(Student s:a)if(s.score>=60)c++;return c;}
    public static int rowMax(int[][]g,int r){int m=g[r][0];for(int x:g[r])if(x>m)m=x;return m;}
    public static int wordScore(String s){int t=0;for(int i=0;i<s.length();i++)t+="aeiouAEIOU".indexOf(s.charAt(i))>=0?2:1;return t;}
    public static int mostFrequent(int[]a){int best=a[0],bc=0;for(int x:a){int c=0;for(int y:a)if(y==x)c++;if(c>bc){bc=c;best=x;}}return best;}
    public static int removeFailing(java.util.ArrayList<Integer>a){int c=0;for(int i=a.size()-1;i>=0;i--)if(a.get(i)<60){a.remove(i);c++;}return c;}
    public static int recursiveVowelCount(String s){if(s.equals(""))return 0;return("aeiouAEIOU".indexOf(s.charAt(0))>=0?1:0)+recursiveVowelCount(s.substring(1));}
    public static int longestIncreasingRun(int[]a){if(a.length==0)return 0;int best=1,run=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1])run++;else run=1;if(run>best)best=run;}return best;}
    public static class Task{String d;boolean complete;Task(String x){d=x;}void markComplete(){complete=true;}boolean isComplete(){return complete;}}
    public static int countIncomplete(java.util.ArrayList<Task>a){int c=0;for(Task t:a)if(!t.isComplete())c++;return c;}

        public static void main(String[] args) {
            java.util.ArrayList<Task> t=new java.util.ArrayList<>();t.add(new Task("read"));t.add(new Task("code"));t.get(0).markComplete();System.out.println(countIncomplete(t));
        }
    }
```

### Explanation

This complete reference follows the prompt's stated algorithm and keeps bounds explicit.

### Python Comparison

Java makes types, object references and loop bounds explicit, so trace them alongside values before deciding the algorithm.

---

# DSA Python - To Remember

Python provides **many built-in modules and functions** that can help you **optimize and simplify** your code—especially useful in competitive coding and interviews.

Here’s a curated list of commonly used **performance-oriented built-in modules/functions** like `bisect_right`:

---

## 🔍 **1. `bisect` module**

Efficient binary search tools on sorted lists (O(log n))

```python
from bisect import bisect_left, bisect_right, insort_left, insort_right

bisect_left(arr, x)    # insertion index before x
bisect_right(arr, x)   # insertion index after x
insort_left(arr, x)    # insert x at correct sorted position (left bias)
```

---

## 📊 **2. `collections` module**

Optimized data structures

```python
from collections import deque, Counter, defaultdict

deque()        # Fast appends/pops from both ends (O(1))
Counter()      # Count frequencies of elements
defaultdict()  # Dictionary with default factory (like 0 or list)
```

---

## 🛠️ **3. `heapq` module**

Efficient priority queue (min-heap)

```python
import heapq

heapq.heappush(heap, x)
heapq.heappop(heap)
heapq.heapify(arr)
```

Use `-x` for max-heap simulation.

---

## ⏱️ **4. `math` module**

Optimized math functions

```python
import math

math.gcd(a, b)
math.lcm(a, b)
math.isqrt(n)        # Integer square root
math.comb(n, k)      # nCk
```

---

## 🧠 **5. `itertools` module**

Fast and memory-efficient looping tools

```python
from itertools import combinations, permutations, product, accumulate

combinations(arr, 2)
accumulate(arr)  # prefix sums
```

---

## ⚡ **6. `functools` module**

Higher-order utilities and memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):  # Fast memoized recursion
    return fib(n-1) + fib(n-2)
```

---

## 📦 **7. `array` module**

Space-efficient numeric arrays (faster than lists for numbers)

```python
from array import array
arr = array('i', [1, 2, 3])  # 'i' = int
```

---

## 🧮 **8. `operator` module**

Faster function equivalents of basic operators

```python
import operator

operator.add(a, b)
operator.itemgetter(1)  # for sorting by second item
```

---

## 🏁 Handy Built-ins (no import needed)

```python
sorted(), min(), max(), sum(), any(), all(), zip(), enumerate()
map(), filter(), set(), list(), dict(), range()
```

---

### 🧠 Pro Tip:

Use `timeit` or `cProfile` to measure and compare performance:

```python
import timeit
timeit.timeit("sorted([3,1,2])", number=10000)
```

---

# Opposite of optimizations

The **opposite of optimizations** in programming are **anti-patterns or inefficiencies** that lead to **slower, memory-heavy, or more complex code**.

Here’s a list of common things that **de-optimize** your Python code — whether in interviews, competitive programming, or real-world apps.

---

## 🚫 Common **De-Optimizations / Anti-Patterns** in Python

---

### 1. **Using Linear Search on Sorted Data**

```python
for x in arr:     # BAD if arr is sorted
    if x == target:
        ...
```

🔁 Instead, use `bisect.bisect_left` for **O(log n)** search on sorted arrays.

---

### 2. **Repeatedly Appending to List in Front**

```python
my_list = []
for i in range(n):
    my_list.insert(0, i)  # O(n) every time — slow!
```

✅ Use `collections.deque` instead, which supports `appendleft()` in O(1).

---

### 3. **Recalculating Values Repeatedly**

```python
# Inefficient
for i in range(n):
    for j in range(i, n):
        sum = sum(arr[i:j])  # Recalculates every time
```

✅ Use `prefix sums` instead.

---

### 4. **Deep Recursion Without Memoization**

```python
def fib(n):
    return fib(n-1) + fib(n-2)  # Exponential time!
```

✅ Use `@lru_cache` or dynamic programming for O(n).

---

### 5. **Unnecessary Use of `for` with `.index()`**

```python
for x in arr:
    if arr.index(x) % 2 == 0:  # `.index()` is O(n)
        ...
```

✅ Use `for i, x in enumerate(arr):` for O(1) access to index.

---

### 6. **Repeated `.append()` Inside Loops to Strings**

```python
s = ""
for word in words:
    s += word + " "  # O(n^2)
```

✅ Use `''.join()` instead:

```python
s = ' '.join(words)
```

---

### 7. **Using Lists Instead of Sets for Membership Tests**

```python
if x in my_list:  # O(n)
```

✅ Use:

```python
if x in my_set:  # O(1)
```

---

### 8. **Sorting Inside a Loop**

```python
for item in data:
    sorted_data = sorted(data)  # Re-sorting every time
```

✅ Move sort **outside** the loop.

---

### 9. **Using Global Variables Unnecessarily**

* Makes code less readable and harder to debug.
* Also prevents proper use of functions and recursion.

---

### 10. **Calling Functions in Loop Headers**

```python
for i in range(len(my_func())):  # Recomputes every iteration
```

✅ Cache the result:

```python
vals = my_func()
for i in range(len(vals)):
```

---

## 🧠 TL;DR — Things that *de-optimize*:

| Category   | Bad Practice                 | Better Alternative      |
| ---------- | ---------------------------- | ----------------------- |
| Search     | Linear search on sorted list | `bisect`, binary search |
| Looping    | `insert(0, val)` in list     | `deque.appendleft()`    |
| Recursion  | No memoization               | `@lru_cache`, DP        |
| String ops | `+=` in loop                 | `''.join()`             |
| Membership | `x in list`                  | `x in set`              |
| Sorting    | Inside loop                  | Do it once before       |

---


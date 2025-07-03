Here's a compact **Python DSA Function Cheat Sheet** covering the most useful **built-ins** and **standard library modules**:

---

## 🧠 **Python DSA Function Cheat Sheet** 🔍

### 🔤 Built-in Functions (No Import Needed)

| Function        | Purpose                     | Example                         |
| --------------- | --------------------------- | ------------------------------- |
| `sorted()`      | Sort iterable               | `sorted(arr, reverse=True)`     |
| `min()`/`max()` | Find smallest/largest value | `min(arr)`                      |
| `sum()`         | Total of elements           | `sum(arr)`                      |
| `any()`/`all()` | Logical checks              | `any(x > 5 for x in arr)`       |
| `zip()`         | Combine multiple iterables  | `zip(arr1, arr2)`               |
| `enumerate()`   | Index + value in loop       | `for i, v in enumerate(arr)`    |
| `map()`         | Apply function to items     | `map(int, arr)`                 |
| `filter()`      | Filter based on condition   | `filter(lambda x: x%2==0, arr)` |
| `set()`         | Unique values, fast lookup  | `set(arr)`                      |
| `range()`       | Sequence of numbers         | `range(n)`                      |

---

### 📐 `math` Module

| Function       | Use Case                |
| -------------- | ----------------------- |
| `gcd(a, b)`    | Greatest common divisor |
| `lcm(a, b)`    | Least common multiple   |
| `factorial(n)` | Combinatorics (n!)      |
| `comb(n, r)`   | nCr (combinations)      |
| `sqrt(x)`      | Square root (float)     |
| `isqrt(x)`     | Integer square root     |

---

### 🧰 `collections` Module

| Structure       | Purpose                                |
| --------------- | -------------------------------------- |
| `deque()`       | Fast queue/stack                       |
| `Counter()`     | Count elements/frequencies             |
| `defaultdict()` | Auto-init dictionary for graphs/groups |

---

### 🔁 `itertools` Module

| Function         | Use Case                 |
| ---------------- | ------------------------ |
| `combinations()` | Generate all subsets     |
| `permutations()` | Generate all orderings   |
| `product()`      | Cartesian product        |
| `accumulate()`   | Prefix sum/max           |
| `groupby()`      | Group consecutive values |

---

### 🔺 `heapq` Module (Min Heap)

| Function            | Purpose                  |
| ------------------- | ------------------------ |
| `heapify()`         | Convert list to min-heap |
| `heappush()`        | Push into heap           |
| `heappop()`         | Pop smallest             |
| `nlargest(k, iter)` | Top k largest            |

---

### 🔍 `bisect` Module

| Function         | Purpose                          |
| ---------------- | -------------------------------- |
| `bisect_left()`  | Insert point (before duplicates) |
| `bisect_right()` | Insert point (after duplicates)  |
| `insort_left()`  | Insert while maintaining order   |

---

### 🧩 `functools` Module

| Function       | Use Case                          |
| -------------- | --------------------------------- |
| `lru_cache()`  | Memoize recursive functions (DP)  |
| `reduce()`     | Collapse iterable to single value |
| `cmp_to_key()` | Custom comparator sorting         |

---

### ➗ `operator` Module

| Function          | Equivalent Operator |
| ----------------- | ------------------- |
| `add(x, y)`       | `x + y`             |
| `mul(x, y)`       | `x * y`             |
| `lt(x, y)`        | `x < y`             |
| `itemgetter(i)`   | `x[i]` as key func  |
| `attrgetter('a')` | `x.a` as key func   |

---

### 🔢 `array` Module

| Type Code    | Description        | Use Case                   |
| ------------ | ------------------ | -------------------------- |
| `'i'`        | Integer array      | Segment tree, XOR, prefix  |
| `'f'`, `'d'` | Float/double array | Space-saving math problems |

---

Here's a compact **Cheat Sheet with Time and Space Complexity** for each of the **built-ins and standard modules used in DSA**, including the ones from our previous cheat sheet.

---

# 📈 Python DSA Function Cheat Sheet (With Time & Space Complexity)

---

## 🔤 **Built-in Functions**

| Function        | Time Complexity | Space Complexity | Notes                                               |
| --------------- | --------------- | ---------------- | --------------------------------------------------- |
| `sorted()`      | O(n log n)      | O(n)             | Timsort (stable sort)                               |
| `min()`/`max()` | O(n)            | O(1)             | Linear scan                                         |
| `sum()`         | O(n)            | O(1)             | Linear accumulation                                 |
| `any()`/`all()` | O(n)            | O(1)             | Stops early if possible                             |
| `zip()`         | O(n)            | O(n)             | Pairs elements up to shortest iterable              |
| `enumerate()`   | O(n)            | O(n)             | Adds index wrapper to iterable                      |
| `map()`         | O(n)            | O(n)             | Applies function lazily (wrapped in list for eager) |
| `filter()`      | O(n)            | O(n)             | Lazy filter (wrapped in list for eager eval)        |
| `set()`         | O(n)            | O(n)             | Hash-based, duplicates removed                      |
| `range(n)`      | O(1)            | O(1)             | Lazy generator (like `xrange` in Python 2)          |

---

## 📐 **math Module**

| Function       | Time Complexity  | Space Complexity | Notes                   |
| -------------- | ---------------- | ---------------- | ----------------------- |
| `gcd(a, b)`    | O(log min(a, b)) | O(1)             | Euclidean algorithm     |
| `lcm(a, b)`    | O(log min(a, b)) | O(1)             | Uses gcd internally     |
| `factorial(n)` | O(n)             | O(1)             |                         |
| `comb(n, r)`   | O(r)             | O(1)             | Uses efficient math ops |
| `sqrt(x)`      | O(1)             | O(1)             | Returns float           |
| `isqrt(x)`     | O(log x)         | O(1)             | Returns integer root    |

---

## 🧰 **collections Module**

| Structure       | Time Complexity             | Space | Notes                |
| --------------- | --------------------------- | ----- | -------------------- |
| `deque()`       | O(1) append/pop (both ends) | O(n)  | Doubly linked list   |
| `Counter()`     | O(n) for construction       | O(n)  | Builds frequency map |
| `defaultdict()` | O(1) for access/insert      | O(k)  | Auto-init keys       |

---

## 🔁 **itertools Module**

| Function         | Time       | Space | Notes                         |
| ---------------- | ---------- | ----- | ----------------------------- |
| `combinations()` | O(nCr × r) | O(r)  | Each combination is size r    |
| `permutations()` | O(nPr × r) | O(r)  | All orderings of r elements   |
| `product()`      | O(kⁿ)      | O(n)  | Cartesian product (expensive) |
| `accumulate()`   | O(n)       | O(n)  | Running total, min, or max    |
| `groupby()`      | O(n)       | O(n)  | Requires sorted input         |

---

## 🔺 **heapq Module**

| Function     | Time       | Space | Notes                  |
| ------------ | ---------- | ----- | ---------------------- |
| `heapify()`  | O(n)       | O(1)  | Builds min-heap        |
| `heappush()` | O(log n)   | O(1)  | Insert into heap       |
| `heappop()`  | O(log n)   | O(1)  | Remove min element     |
| `nlargest()` | O(n log k) | O(k)  | Top K largest elements |

---

## 🔍 **bisect Module**

| Function         | Time     | Space | Notes                            |
| ---------------- | -------- | ----- | -------------------------------- |
| `bisect_left()`  | O(log n) | O(1)  | Returns leftmost insertion point |
| `bisect_right()` | O(log n) | O(1)  | After duplicates                 |
| `insort_left()`  | O(n)     | O(1)  | Inserts and maintains sort       |

---

## 🧩 **functools Module**

| Function       | Time              | Space | Notes                               |
| -------------- | ----------------- | ----- | ----------------------------------- |
| `lru_cache()`  | O(1) cache lookup | O(n)  | Speeds up recursive DP              |
| `reduce()`     | O(n)              | O(1)  | Fold/reduce an iterable             |
| `cmp_to_key()` | O(n log n)        | O(1)  | Used with `sorted()` and custom cmp |

---

## ➗ **operator Module**

| Function          | Time | Space | Notes                         |
| ----------------- | ---- | ----- | ----------------------------- |
| `add`, `mul`, etc | O(1) | O(1)  | Function version of basic ops |
| `itemgetter(i)`   | O(1) | O(1)  | Faster than `lambda x: x[i]`  |
| `attrgetter('a')` | O(1) | O(1)  | For object sorting/filtering  |

---

## 🔢 **array Module**

| Operation       | Time           | Space | Notes                            |
| --------------- | -------------- | ----- | -------------------------------- |
| `append()`      | O(1) amortized | O(n)  | Like list, more memory efficient |
| `pop()`         | O(1)           | O(n)  |                                  |
| Access by index | O(1)           | O(n)  |                                  |

---

## 🧮 **NumPy (for advanced use)**

| Operation         | Time      | Space | Notes                       |
| ----------------- | --------- | ----- | --------------------------- |
| `np.array([...])` | O(n)      | O(n)  | Fast numeric array          |
| Element-wise ops  | O(n)      | O(n)  | Vectorized, fast            |
| `dot()`           | O(n³)     | O(n²) | Matrix multiplication       |
| Slicing/filtering | O(1) view | O(1)  | Efficient compared to lists |

---

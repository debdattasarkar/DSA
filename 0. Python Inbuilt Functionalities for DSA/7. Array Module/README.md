The **`array` module** in Python is a **memory-efficient** alternative to lists, especially when you're storing **only numbers** of the same type (like integers or floats).

---

## 📦 What is the `array` module?

The `array` module provides a **compact**, **typed**, and **efficient array data structure** — similar to C-style arrays.

Unlike Python lists, `array.array` stores values more **compactly** (in fixed-size C types).

---

## ✅ Syntax

```python
from array import array

a = array(typecode, initializer)
```

### 📘 Common Typecodes:

| Typecode | C Type       | Python Type | Example                  |
| -------- | ------------ | ----------- | ------------------------ |
| `'i'`    | signed int   | int         | `array('i', [1, 2])`     |
| `'f'`    | float        | float       | `array('f', [1.2, 3.4])` |
| `'d'`    | double float | float       | `array('d', [3.14])`     |

---

## 🧠 Why use `array` in DSA?

* Faster than lists for **numeric data**
* Lower memory footprint
* Efficient when working with large numeric datasets (like prefix sums, bit manipulation)

---

## ✅ DSA Example 1: Prefix Sum of Integer Array

```python
from array import array

def prefix_sum(arr):
    n = len(arr)
    psum = array('i', [0] * n)
    psum[0] = arr[0]
    for i in range(1, n):
        psum[i] = psum[i - 1] + arr[i]
    return psum

a = array('i', [1, 2, 3, 4])
result = prefix_sum(a)
print(result.tolist())  # Output: [1, 3, 6, 10]
```

---

## ✅ DSA Example 2: Bitwise XOR Array

```python
from array import array

def xor_array(arr):
    result = 0
    for val in arr:
        result ^= val
    return result

nums = array('i', [1, 2, 3, 2, 1])
print(xor_array(nums))  # Output: 3 (only element without a duplicate)
```

---

## 🔁 Dry Run (XOR Example):

Array: \[1, 2, 3, 2, 1]

XOR step-by-step:

```
1 ^ 2 = 3  
3 ^ 3 = 0  
0 ^ 2 = 2  
2 ^ 1 = 3
```

Final answer = **3**

---

## 🔄 Common Operations

```python
arr = array('i', [1, 2, 3])
arr.append(4)
arr.insert(1, 99)
arr.remove(2)
arr.pop()
arr.reverse()
```

---

## 🧠 When to prefer `array` over `list`:

| If You Want...                   | Use          |
| -------------------------------- | ------------ |
| Typed numeric efficiency         | ✅ `array`    |
| Mixed data types or flexibility  | ❌ Use `list` |
| Fixed-type operations (DSP, DSA) | ✅ `array`    |

---

## ⚠️ Limitation

* Cannot store mixed data types
* No direct slicing with step
* Slower for general-purpose than `numpy`

---

## 🧩 Real Use Case: Counting XOR from 1 to N

```python
from array import array

def xor_to_n(n):
    a = array('i', range(n + 1))
    result = 0
    for num in a:
        result ^= num
    return result

print(xor_to_n(5))  # Output: 1 (0^1^2^3^4^5 = 1)
```

---
# Comparison with NumPy, or want to see array used in segment tree or sieve algorithms:

---

## ✅ Part 1: `array` vs `NumPy` — When to Use What

| Feature              | `array` (from array module)          | `NumPy` array                         |
| -------------------- | ------------------------------------ | ------------------------------------- |
| Memory efficiency    | ✅ Very efficient                     | ✅ Very efficient                      |
| Speed for math ops   | ❌ Manual loop required               | ✅ Vectorized (fast)                   |
| Data types supported | Only basic numeric types             | Many: int, float, bool, complex, etc. |
| Multi-dimensional    | ❌ Not supported                      | ✅ Fully supported                     |
| Broadcasting         | ❌ Not available                      | ✅ Powerful                            |
| Used in CP/DSA?      | ✅ Yes (small problems, simple types) | ✅ Yes (large arrays, matrix ops)      |
| Library size         | Lightweight (standard lib)           | Requires external install             |

---

## 🔍 When to use which?

| Situation                                  | Choose                       |
| ------------------------------------------ | ---------------------------- |
| Simple 1D numeric array (e.g., prefix sum) | `array`                      |
| Large-scale vector ops or matrices         | `NumPy`                      |
| In coding interviews / contests            | `array` (fast import, small) |
| In ML/AI or numerical simulations          | `NumPy`                      |

---

## ✅ Part 2: Using `array` in Segment Tree (DSA)

### Problem: Build a segment tree for range sum queries

```python
from array import array

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = array('i', [0] * (2 * self.n))
        self.build(data)

    def build(self, data):
        # Fill leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Fill internal nodes
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r):
        # Query sum from l to r-1
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

# Test
arr = array('i', [1, 3, 5, 7, 9, 11])
st = SegmentTree(arr)
print(st.query(1, 4))  # Output: 3 + 5 + 7 = 15
```

---

## ✅ Part 3: Using `array` in Sieve of Eratosthenes

### Problem: Count primes ≤ n

```python
from array import array

def sieve(n):
    is_prime = array('b', [1] * (n + 1))  # byte array for memory efficiency
    is_prime[0] = is_prime[1] = 0

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = 0

    return sum(is_prime)

print(sieve(30))  # Output: 10 → primes are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## 🧠 Summary

* Use `array` when:

  * You're in **DSA/interview mode**
  * You want **fast integer/bit-level structures**
  * You don't need 2D arrays or broadcasting

* Use `NumPy` when:

  * You work on **large datasets, matrix math, AI/ML**
  * You need **powerful indexing and ops**

---

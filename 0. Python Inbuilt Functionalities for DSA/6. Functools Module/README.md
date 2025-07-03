The **`functools` module** is one of Python’s most powerful built-in tools for **functional-style programming** and **DSA optimization**.

---

## 📦 What is `functools`?

The `functools` module provides **higher-order functions** that act on or return other functions.
It includes tools like **memoization**, **function composition**, and **custom sorting** — all very useful in DSA.

---

## 🔧 Key `functools` Tools for DSA

| Function              | Use Case                          |
| --------------------- | --------------------------------- |
| `@lru_cache`          | Memoization for recursive DP      |
| `cmp_to_key()`        | Custom sorting with comparators   |
| `partial()`           | Fix arguments of a function       |
| `reduce()`            | Collapse list into a single value |
| `cache` (Python 3.9+) | Modern alias of `lru_cache`       |

---

## ✅ 1. `@lru_cache` — Memoization Decorator

### 💡 DSA Use Case: Fibonacci with memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Output: 55
```

### 🔁 Dry Run:

Without memoization → exponential
With `lru_cache` → only computes each `fib(i)` once!

---

## ✅ 2. `cmp_to_key()` — Custom Comparator for Sorting

### 💡 DSA Use Case: Largest Number from Array of Strings

```python
from functools import cmp_to_key

def compare(a, b):
    return (int(b + a) > int(a + b)) - (int(b + a) < int(a + b))

nums = ["3", "30", "34", "5", "9"]
nums.sort(key=cmp_to_key(compare))
print("".join(nums))  # Output: 9534330
```

### 🧠 Logic:

* Custom compare ensures correct concatenation order

---

## ✅ 3. `partial()` — Pre-fill Function Arguments

### 💡 DSA Use Case: Use fixed comparator

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(4))  # Output: 16
```

---

## ✅ 4. `reduce()` — Collapse iterable into a single value

### 💡 DSA Use Case: Product of all elements

```python
from functools import reduce

nums = [2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
```

---

## 🧩 Full DSA Example: Climbing Stairs with Memoization

> Given `n` steps, you can take 1 or 2 steps. How many distinct ways to climb?

```python
from functools import lru_cache

@lru_cache(None)
def climb(n):
    if n <= 1:
        return 1
    return climb(n-1) + climb(n-2)

print(climb(5))  # Output: 8
```

---

## 🧠 Summary Table

| Tool           | Purpose                            | Use In DSA Example           |
| -------------- | ---------------------------------- | ---------------------------- |
| `@lru_cache`   | Recursive DP memoization           | Fibonacci, Climb stairs      |
| `cmp_to_key()` | Custom sorting with comparator     | Largest number arrangement   |
| `partial()`    | Pre-filling function args          | Currying function usage      |
| `reduce()`     | Collapse iterable (like sum, prod) | Product, prefix calculations |

---

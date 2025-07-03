The **`math` module** in Python provides fast, pre-compiled **mathematical functions and constants** — essential for many **DSA problems**, especially those involving:

* Number theory
* Geometry
* Combinatorics
* Optimization

---

## 📦 What is `math` module?

`math` is a standard Python library that offers **precise and optimized** math functions, avoiding the need to reimplement common logic like GCD, square roots, factorials, etc.

---

## 🔧 Key `math` functions for DSA:

| Function                         | Use Case                            |
| -------------------------------- | ----------------------------------- |
| `math.gcd(a, b)`                 | Greatest common divisor (GCD)       |
| `math.lcm(a, b)`                 | Least common multiple (Python 3.9+) |
| `math.sqrt(x)`                   | Square root (returns float)         |
| `math.isqrt(x)`                  | Integer square root (Python 3.8+)   |
| `math.factorial(n)`              | Computes `n!`                       |
| `math.comb(n, r)`                | Computes `nCr` (combinations)       |
| `math.log(x, base)`              | Logarithm base `b`                  |
| `math.ceil(x)` / `math.floor(x)` | Round up/down                       |
| `math.inf` / `math.pi`           | Infinity / π constant               |

---

Let’s explore each with a DSA-relevant **example, dry run, and full code**.

---

## ✅ 1. `math.gcd(a, b)`

### 💡 Use Case: Check if a fraction is irreducible

```python
import math

def is_irreducible(a, b):
    return math.gcd(a, b) == 1

print(is_irreducible(8, 9))  # ✅ True
print(is_irreducible(6, 9))  # ❌ False (GCD=3)
```

---

## ✅ 2. `math.lcm(a, b)`

### 💡 Use Case: Find first common time two machines meet

```python
import math

a, b = 4, 6
print(math.lcm(a, b))  # Output: 12
```

📌 Dry run:
Multiples of 4: 4, 8, 12
Multiples of 6: 6, 12 ✅

---

## ✅ 3. `math.isqrt(n)` — Integer square root

### 💡 Use Case: Count perfect squares in a range

```python
import math

def count_perfect_squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)

print(count_perfect_squares(1, 16))  # Output: 4 → 1, 4, 9, 16
```

---

## ✅ 4. `math.factorial(n)`

### 💡 Use Case: Compute permutations `n!`

```python
import math

n = 5
print(math.factorial(n))  # Output: 120
```

📌 Used in:

* Permutation/combination problems
* Backtracking bounds

---

## ✅ 5. `math.comb(n, r)`

### 💡 Use Case: Find number of ways to choose r items from n

```python
import math

print(math.comb(5, 2))  # Output: 10
```

📌 Equivalent to: `5! / (2! * 3!) = 10`

---

## ✅ 6. `math.log(x, base)`

### 💡 Use Case: Find number of digits in a number (log base 10)

```python
import math

def num_digits(n):
    return math.floor(math.log10(n)) + 1

print(num_digits(12345))  # Output: 5
```

---

## ✅ 7. `math.ceil` & `math.floor`

### 💡 Use Case: Split items into pages

```python
import math

def num_pages(items, per_page):
    return math.ceil(items / per_page)

print(num_pages(25, 10))  # Output: 3
```

---

## ✅ 8. `math.inf`, `math.pi`

### 💡 Use Case: Dijkstra’s algorithm initialization

```python
import math

dist = [math.inf] * 5  # Initial distances: [∞, ∞, ∞, ∞, ∞]
```

---

## 🧠 Summary Table

| Task                         | Function                  | Time     |
| ---------------------------- | ------------------------- | -------- |
| Simplify ratios, GCD-related | `math.gcd()`              | O(log n) |
| Common repeat intervals      | `math.lcm()`              | O(log n) |
| Square root in integers      | `math.isqrt()`            | O(1)     |
| Factorials, permutations     | `math.factorial()`        | O(n)     |
| Combinations nCr             | `math.comb()`             | O(r)     |
| Logarithmic calculations     | `math.log()`              | O(1)     |
| Rounding values              | `math.ceil()` / `floor()` | O(1)     |

---

## 🧩 Full DSA Problem Example Using Multiple `math` Functions

> **Problem**: Count how many numbers from 1 to `N` are divisible by **a OR b**

```python
import math

def count_multiples(n, a, b):
    lcm_ab = math.lcm(a, b)
    count = n // a + n // b - n // lcm_ab
    return count

# Test
print(count_multiples(20, 4, 6))  # 20//4 + 20//6 - 20//12 = 5 + 3 - 1 = 7
```

---

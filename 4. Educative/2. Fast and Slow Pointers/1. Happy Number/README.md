
---

# 🧠 Leetcode Pattern: Happy Number (Using Fast & Slow Pointers)

## 📝 Problem Statement

Given a number `n`, determine if it's a **happy number**.

> A happy number is a number that eventually reaches `1` when replaced by the **sum of the squares of its digits** repeatedly. If it loops endlessly in a cycle that **does not include 1**, it's not a happy number.

### The process:

1. Start with `n`.
2. Replace `n` with the **sum of squares of its digits**.
3. Repeat until:

   * You reach `1` (✅ Happy number).
   * Or, a **cycle** is detected (❌ Not a happy number).

---

## ✅ Constraints

* $1 \leq n \leq 2^{31} - 1$

---

## 📊 Example

### Input:

```
n = 7
```

### Process:

```
7 → 49 → 97 → 130 → 10 → 1 ✅
```

### Output:

```
TRUE
```

---

## 🧠 Pattern Recognition: Fast & Slow Pointers

To detect a cycle (like detecting cycles in linked lists), we apply the **Floyd’s Tortoise and Hare** algorithm:

* `slow`: advances one step (sum of squares once)
* `fast`: advances two steps (sum of squares twice)

If there's a cycle, `slow` will eventually meet `fast`. If any of them becomes `1`, return `True`.

---

## 🔄 Steps Summary

1. Define a helper `get_next(n)` to return the sum of squares of digits of `n`.
2. Initialize two variables: `slow` and `fast` to `n`.
3. Loop:

   * Update `slow` by one step: `slow = get_next(slow)`
   * Update `fast` by two steps: `fast = get_next(get_next(fast))`
   * If `fast == 1`, return `True`
   * If `slow == fast`, return `False` (cycle detected)

---

## ✅ Python Code

```python
def is_happy_number(n):
    def get_next(x):
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x //= 10
        return total

    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1
```

---

## 🕒 Time Complexity

* **O(log n)** per digit transformation.
* Because values shrink fast, total steps are limited (at most \~243 per cycle).
* Overall: `O(1)` bounded by cycle length.

## 🧠 Space Complexity

* `O(1)` — no extra space other than integer vars.

---

# 🧮 Problem: Happy Number

### 📜 Statement

Determine whether a given number `n` is a **happy number**.

A number is happy if:

* You repeatedly replace it by the **sum of squares of its digits**.
* This process either:

  * Ends at `1`, marking it a **happy number**.
  * Falls into a **cycle**, never reaching `1`, marking it **not happy**.

---

## 🔁 Process

1. Start with number `n`.
2. Replace it by the sum of the squares of its digits.
3. Repeat the process until:

   * `n == 1`: return `True`
   * A **cycle** is detected: return `False`

---

## 🧠 Approaches

### 🔹 Naive Approach using HashSet

* Store all seen numbers in a set.
* If a number repeats, it is a cycle → not happy.
* If you reach 1, it is a happy number.

```python
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1
```

### 🔹 Optimized Approach using Fast and Slow Pointers

* Detect cycle using Floyd’s Tortoise and Hare (like Linked List Cycle Detection).
* Uses two pointers:

  * `slow` moves one step (sum of squares once).
  * `fast` moves two steps (sum of squares twice).

```python
def get_next(n):
    return sum(int(d)**2 for d in str(n))

def is_happy(n):
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1
```

---

## 📊 Dry Run Example (Input: `19`)

```
19 → 1² + 9² = 82
82 → 8² + 2² = 68
68 → 6² + 8² = 100
100 → 1² + 0² + 0² = 1 ✅
```

Output: `True`

---

## 🕒 Time Complexity

* **O(log n)** per iteration since we sum digits' squares.
* At most **log n** digits → converges quickly.
* Floyd's cycle detection also runs in linear steps before convergence.

Total: **O(log n)**

---

## 🧮 Space Complexity

* **O(1)** using two pointers (`fast`, `slow`).
* **O(n)** if using a `set` for cycle detection (naive approach).

---

## ✅ Conclusion

The **fast and slow pointer** approach is both optimal and elegant:

* Detects cycles efficiently.
* Saves memory over naive set-based tracking.
* Cleanly solves the problem using constant space.

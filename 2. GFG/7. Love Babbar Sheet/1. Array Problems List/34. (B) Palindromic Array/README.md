Here’s the **full README-style version** of the image — with every detail preserved 👇

---

# 🔁 Palindromic Array

**Difficulty:** Basic
**Accuracy:** 58.62%
**Submissions:** 192K+
**Points:** 1
**Average Time:** 15m

---

## 📘 Problem Statement

Given an array `arr[]` of positive integers.
Return **true** if all the array elements are palindrome numbers; otherwise, return **false**.

---

## 💡 Examples

### Example 1

**Input:**
`arr[] = [111, 222, 333, 444, 555]`

**Output:**
`true`

**Explanation:**

* `arr[0] = 111`, which is a palindrome number.
* `arr[1] = 222`, which is a palindrome number.
* `arr[2] = 333`, which is a palindrome number.
* `arr[3] = 444`, which is a palindrome number.
* `arr[4] = 555`, which is a palindrome number.

As all numbers are palindrome numbers, this will return **true**.

---

### Example 2

**Input:**
`arr[] = [121, 131, 20]`

**Output:**
`false`

**Explanation:**
`20` is not a palindrome; hence the output is **false**.

---

## ⚙️ Expected Complexities

* **Time Complexity:** O(n log n)
* **Space Complexity:** O(1)

---

## 🔢 Constraints

```
1 ≤ arr.size ≤ 20  
1 ≤ arr[i] ≤ 10^5
```

---

## 🏷️ Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* [*Check if All Elements of the Array Are Palindrome or Not*](https://www.geeksforgeeks.org/check-if-all-elements-of-the-array-are-palindrome-or-not/)

---

---

awesome — let’s make **Palindromic Array** crisp and interview-ready.

---

## 2) Explanation + step-by-step dry run

**Problem**
Given an array of positive integers, return **True** if **every** element is a palindrome (reads the same forward and backward), else **False**.

**Key idea**
A number `x` is a palindrome iff its string form equals its reverse, **or** the number you get by mathematically reversing its digits equals `x`. We must check this for **each** element; if any fails, return `False`.

### Dry run 1

`arr = [111, 222, 333, 444, 555]`

* 111 → "111" == "111" ✅
* 222 → "222" == "222" ✅
* 333 → ✅
* 444 → ✅
* 555 → ✅
  All pass → **True**

### Dry run 2

`arr = [121, 131, 20]`

* 121 → palindrome ✅
* 131 → palindrome ✅
* 20  → "20" != "02", reverse(20)=02 → 2 ≠ 20 ❌
  Fail fast → **False**

---

## 3) Python solutions (optimized + alternatives)

### A) Clean & most expected: string reverse (readable, fast in Python)

```python
# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    """
    Check each number's string representation equals its reverse.
    Time  : O(n * d) where d is average digit count (<= 6 given constraints)
    Space : O(1) extra (ignoring small temporary strings per number)
    Short-circuits on first non-palindrome.
    """
    for num in arr:
        s = str(num)           # O(d)
        if s != s[::-1]:       # O(d)
            return False
    return True
```

### B) Math-only reverse (language-agnostic, no strings)

```python
def isPalinArray(arr):
    """
    Reverse digits numerically and compare.
    Time  : O(n * d)
    Space : O(1)
    """
    for num in arr:
        original = num
        rev = 0
        while num > 0:                  # O(d)
            rev = rev * 10 + (num % 10)
            num //= 10
        if rev != original:
            return False
    return True
```

### C) Early-optimized with small micro checks (optional)

* Any single-digit ⇒ palindrome.
* Ending with 0 but not zero ⇒ **not** palindrome (e.g., 20, 120), can short-circuit.

```python
def isPalinArray(arr):
    for num in arr:
        if num < 10:              # 0..9
            continue
        if num % 10 == 0:         # ends with 0 and >0 -> can't be palindrome
            return False
        s = str(num)
        if s != s[::-1]:
            return False
    return True
```

> In Python interviews, variant **A** is usually acceptable and the most succinct;
> in C++/Java, they often prefer **B** (math) to avoid string conversions.

---

## 4) Interview quick-recall + expected Q&A

### 10-second memory hook

> “**All numbers palindromes?** Check each: `s == s[::-1]` (or reverse digits).
> Fail fast on first mismatch.”

### Likely follow-ups (concise answers)

**Q1. Complexity?**
`O(n * d)` where `d` is digits per number (≤ 6 for `arr[i] ≤ 1e5`). Space `O(1)`.

**Q2. Can we avoid strings?**
Yes—reverse digits mathematically (multiply by 10 and add last digit). Same asymptotic complexity.

**Q3. Any edge cases?**

* Single-digit numbers are palindromes by definition.
* Numbers ending with zero (and nonzero) cannot be palindromes (e.g., 20).
* Input size up to 20 → trivial for performance.

**Q4. What if negatives appear?**
Problem states **positive integers**. If negatives were allowed, typical convention: they are **not** palindromes unless you define otherwise (because of the minus sign).

**Q5. Could we precompute?**
Given small bounds, unnecessary. But you could memoize repeated values if array had many duplicates.

---

### Tiny 5-line pseudo-code you can say before coding

```
for x in arr:
    s = str(x)
    if s != reverse(s): return False
return True
```

That’s the whole solution you can write in under 30 seconds.

---

---

awesome — here are the last two parts for **Palindromic Array** 👇

---

## 5) Real-World Use Cases (short & relatable)

* **Data validation / identifiers:** ensure every ID in a batch matches a palindromic rule (e.g., special promo codes or vanity numbers).
* **Symmetry checks in logs/telemetry:** detect “mirrored” numeric patterns (palindromic timestamps like 12:21:21) for feature flags or easter-egg analytics.
* **Number formatting pipelines:** filter/whitelist only palindromic values for a game/quiz or numerology-style features.

---

## 6) Full Python Program

Includes:

* Two implementations (string-based & math-based) with **inline time/space notes**.
* A simple **test harness** with inputs & outputs.
* **Timing** using `timeit` on random data.

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# Approach A: Pythonic string reverse (most concise for interviews)
# ------------------------------------------------------------
def isPalinArray_str(arr):
    """
    Check if every integer in arr is a palindrome using string reverse.
    Time  : O(n * d) where d is number of digits (<= 6 given arr[i] <= 1e5)
            Each element creates a string (O(d)) and a reversed slice (O(d)).
    Space : O(1) extra, ignoring transient strings of length d.
    """
    for num in arr:                 # O(n)
        s = str(num)                # O(d)
        if s != s[::-1]:            # O(d)
            return False            # short-circuit on first failure
    return True


# ------------------------------------------------------------
# Approach B: Math-only digit reverse (language-agnostic)
# ------------------------------------------------------------
def isPalinArray_math(arr):
    """
    Reverse digits numerically, no strings.
    Time  : O(n * d)  (extract digits)
    Space : O(1)
    """
    for num in arr:
        original = num
        rev = 0
        while num > 0:              # O(d)
            rev = rev * 10 + (num % 10)
            num //= 10
        if rev != original:
            return False
    return True


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Palindromic Array ===\n")

    # Example cases from prompt + extras
    examples = [
        ("All Palindromes", [111, 222, 333, 444, 555], True),
        ("Has Non-Palindrome", [121, 131, 20], False),
        ("Single Element", [7], True),
        ("Mixed small", [1, 22, 303, 44, 9], True),
    ]

    for name, arr, expected in examples:
        res_a = isPalinArray_str(arr[:])
        res_b = isPalinArray_math(arr[:])
        print(f"{name}: arr={arr}")
        print(f"  String method: {res_a}")
        print(f"  Math   method: {res_b}")
        print(f"  Expected     : {expected}")
        print(f"  Match?       : {res_a == res_b == expected}\n")

    # ----------------- Timing section -----------------
    seed(42)
    n = 200_000
    # Make numbers within constraint (<= 1e5) and mostly palindromic-ish
    big = [randint(1, 99_999) for _ in range(n)]

    t_str = timeit(lambda: isPalinArray_str(big), number=3)
    t_math = timeit(lambda: isPalinArray_math(big), number=3)

    print("=== Timing (seconds) ===")
    print(f"Input size n={n}, runs=3 each")
    print(f"String reverse  (O(n*d)): total {t_str:.4f}s | avg {(t_str/3):.4f}s/run")
    print(f"Math-only reverse(O(n*d)): total {t_math:.4f}s | avg {(t_math/3):.4f}s/run")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For each sample, both methods agree with **Expected** and `Match? True`.
* The timing section shows practical performance; both are **O(n · digits)** and fast for the given constraints.

---

### 10-second recall (before coding)

> “Loop all numbers → palindrome test per number: `s == s[::-1]` (or reverse digits).
> Short-circuit on first miss. Time O(n·d), Space O(1).”

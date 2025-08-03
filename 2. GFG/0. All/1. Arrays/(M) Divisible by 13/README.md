
---

# 📘 Problem: Divisible by 13

**Difficulty:** Medium
**Accuracy:** 56.69%
**Submissions:** 8K+
**Points:** 4

---

## 🔍 Problem Statement

Given a number represented as a string `s` (which may be very large), check whether it is divisible by **13** or not.

---

## 💡 Examples

### Example 1

**Input:**
`s = "2911285"`

**Output:**
`true`

**Explanation:**
2911285 ÷ 13 = 223945, which is a whole number with no remainder.

---

### Example 2

**Input:**
`s = "27"`

**Output:**
`false`

**Explanation:**
27 ÷ 13 ≈ 2.0769… which is not a whole number (there is a remainder).

---

## 📏 Constraints

* 1 ≤ `s.size()` ≤ 10⁵

---

## 📈 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Mathematical

---

## 📚 Related Articles

* [Check Large Number Divisible by 13 or Not](#)

---

---

Let's go step-by-step for the problem **"Divisible by 13"**.

---

## ✅ 2. Explanation & Step-by-Step Dry Run

### 🔸 Goal:

Check whether a **very large number (as a string)** is divisible by **13**.

---

### 🔹 Key Insight:

We **cannot convert the whole string to an integer** directly (for very large inputs), so instead we build the number **digit by digit**, taking the **modulus at each step**:

$$
\text{If } ((...(((((0 \times 10 + d_1) \mod 13) \times 10 + d_2) \mod 13)...)) \mod 13) = 0 \Rightarrow \text{divisible by 13}
$$

---

### 🔸 Dry Run for Input: `"2911285"`

```
We process digit by digit and keep track of num % 13

Initial: remainder = 0

Step 1: '2' -> (0 * 10 + 2) % 13 = 2
Step 2: '9' -> (2 * 10 + 9) % 13 = 3
Step 3: '1' -> (3 * 10 + 1) % 13 = 5
Step 4: '1' -> (5 * 10 + 1) % 13 = 11
Step 5: '2' -> (11 * 10 + 2) % 13 = 7
Step 6: '8' -> (7 * 10 + 8) % 13 = 3
Step 7: '5' -> (3 * 10 + 5) % 13 = 0 ✅

Since remainder is 0 → **It is divisible by 13**
```

---

## ✅ 3. Optimized Python Codes (Interview Friendly)

### 🔹 Brute (but works for small inputs only — NOT recommended for 10⁵ digits)

```python
class Solution:
    def divby13(self, s):
        return int(s) % 13 == 0  # ❌ Not safe for huge inputs
```

---

### 🔹 Optimal and Safe for Very Large Strings

```python
class Solution:
    def divby13(self, s):
        remainder = 0
        for digit in s:
            remainder = (remainder * 10 + int(digit)) % 13
        return remainder == 0
```

### 🔸 Time and Space Complexity:

* **Time Complexity:** O(n) where `n = len(s)`
* **Space Complexity:** O(1) — only one integer used for remainder

---

### 🔹 Full Main Program with `timeit` Benchmark

```python
import timeit

class Solution:
    def divby13(self, s):
        # Initialize remainder
        remainder = 0
        for digit in s:
            # Update remainder using digit
            remainder = (remainder * 10 + int(digit)) % 13
        # Final result
        return remainder == 0

# Input string (can be very large)
s = "2911285"  # True

# Benchmark the solution
start = timeit.default_timer()

sol = Solution()
result = sol.divby13(s)
print("Is divisible by 13:", result)

end = timeit.default_timer()
print("Execution Time:", end - start, "seconds")
```

---

## ✅ 4. Common Interview Questions and Expected Answers

| ❓ Question                                   | ✅ Expected Answer                                                                               |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Why store number as a string?                | Because it may be too large to fit in standard integer types.                                   |
| Why not just do `int(s) % 13`?               | This will fail for huge values (e.g., 10⁵ digits) and may cause overflow or performance issues. |
| How do you check divisibility in such cases? | Use digit-by-digit modular construction: `(prev_remainder * 10 + digit) % divisor`              |
| Can this be extended to other divisors?      | Yes, this modular approach works for any base-10 divisibility check.                            |
| Time and space complexity?                   | O(n) time and O(1) space                                                                        |

---


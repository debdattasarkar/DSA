# Sum of two large numbers 🧮

**Difficulty:** Medium
**Accuracy:** 22.58%
**Submissions:** 129K+
**Points:** 4
**Average Time:** 20m

---

Given two strings denoting non-negative numbers `s1` and `s2`. **Calculate the sum** of `s1` and `s2`.

---

## Examples

### Example 1

**Input:** `s1 = "25", s2 = "23"`
**Output:** `"48"`
**Explanation:** The sum of 25 and 23 is 48.

### Example 2

**Input:** `s1 = "2500", s2 = "23"`
**Output:** `"2523"`
**Explanation:** The sum of 2500 and 23 is 2523.

### Example 3

**Input:** `s1 = "2", s2 = "3"`
**Output:** `"5"`
**Explanation:** The sum of 2 and 3 is 5.

---

## Constraints

* `1 ≤ |s1|, |s2| ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Zoho
* Amazon
* Microsoft

---

## Topic Tags

* Strings
* Data Structures

---

## Related Interview Experiences

* Microsoft Interview Experience Set 129 Campus Internship
* Amazon Interview Experience for SDE 1 FTE 6 Months Internship Amazewow

---

## Related Articles

* **Sum Two Large Numbers**

---

---

Below is everything you’d typically give in a neat interview solution set: a crisp explanation, a fully-worked dry run, multiple Python solutions in the requested format (with the right comments interviewers expect), and some quick Q\&A.

---

# 2) Problem explanation + step-by-step dry run

## What we need

You’re given two **non-negative integers as strings** `s1` and `s2`. Return their **sum as a string**.
Numbers can be up to `1e5` digits → we **cannot** rely on native integer conversion (and in many interviewers’ eyes, we shouldn’t).

## Key idea (grade-school addition)

Add from the least significant digits (rightmost) to the left, keep a `carry`, and build the answer.

* Use two pointers `i = len(s1)-1`, `j = len(s2)-1`
* While `i >= 0 or j >= 0 or carry`:

  * `d1 = int(s1[i]) if i>=0 else 0`
  * `d2 = int(s2[j]) if j>=0 else 0`
  * `total = d1 + d2 + carry`
  * Push `total % 10` to result
  * `carry = total // 10`
  * `i -= 1; j -= 1`
* Reverse the collected digits (or build from left using a deque)

Also strip *leading zeros in the final result* (unless the result is exactly `"0"`).

### Dry run: `s1 = "2500"`, `s2 = "23"`

```
i=3 (0), j=1 (3), carry=0 → total=0+3+0=3 → push '3' → carry=0
i=2 (0), j=0 (2), carry=0 → total=0+2=2 → push '2' → carry=0
i=1 (5), j=-1(0), carry=0 → total=5+0=5 → push '5' → carry=0
i=0 (2), j=-1(0), carry=0 → total=2+0=2 → push '2' → carry=0
i=-1, j=-1, carry=0 → stop
Collected (reversed order): ['3','2','5','2'] → reverse → "2523"
```

### Edge cases to watch

* One of the strings is `"0"` or has leading zeros (e.g., `"000123"`).
* Carry remains after the last step (e.g., `"999" + "1" → "1000"`).
* Very different lengths (e.g., `"1" + "99999"`).

---

# 3) Optimized Python codes (interview-friendly)

Both are linear `O(n)` time and `O(n)` extra space (for the output). The second variant avoids reversing a big list by using a deque.

## A) Two-pointers, collect then reverse (simple & clear)

```python
class Solution:
    def findSum(self, s1, s2):
        """
        Add two non-negative integers given as decimal strings.
        Time:  O(n) where n = max(len(s1), len(s2))
        Space: O(n) for the output string
        
        Logic:
        - Start from the right end of both strings, add digit by digit with carry.
        - Build digits in reverse order, then reverse once at the end.
        - Strip leading zeros from final result unless the entire result is '0'.
        """
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        out = []  # collect digits in reverse

        while i >= 0 or j >= 0 or carry:
            d1 = ord(s1[i]) - 48 if i >= 0 else 0  # faster than int(s1[i])
            d2 = ord(s2[j]) - 48 if j >= 0 else 0
            total = d1 + d2 + carry
            out.append(chr((total % 10) + 48))
            carry = total // 10
            i -= 1
            j -= 1

        # reverse to normal order
        res = "".join(reversed(out))

        # remove leading zeros, but keep at least one '0'
        # (input assures non-negative numbers; both can be "0...0")
        k = 0
        while k + 1 < len(res) and res[k] == '0':
            k += 1
        return res[k:]
```

## B) Two-pointers + deque (avoid reversing a huge list)

```python
from collections import deque

class Solution:
    def findSum(self, s1, s2):
        """
        Same logic as A but uses a deque to appendleft each digit,
        avoiding a full reverse at the end (good when strings are huge).
        Time:  O(n)
        Space: O(n)
        """
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        dq = deque()

        while i >= 0 or j >= 0 or carry:
            d1 = ord(s1[i]) - 48 if i >= 0 else 0
            d2 = ord(s2[j]) - 48 if j >= 0 else 0
            total = d1 + d2 + carry
            dq.appendleft(chr((total % 10) + 48))
            carry = total // 10
            i -= 1
            j -= 1

        res = "".join(dq)

        # Strip leading zeros but keep one zero if all zeros
        k = 0
        while k + 1 < len(res) and res[k] == '0':
            k += 1
        return res[k:]
```

> Why not use Python’s big integers (`str(int(s1) + int(s2))`)?
> With constraints up to `1e5` digits, converting to `int` is impractical/forbidden and undermines the intention of the problem. Interviewers typically expect the manual addition approach.

---

# 4) Quick interviewer Q\&A

**Q1. Why can’t we simply convert to integers and add?**
**A.** The strings can be up to `10^5` digits; conversion is memory/time heavy and often disallowed. The goal is to implement big-integer addition.

**Q2. What’s the time and space complexity?**
**A.** `O(n)` time where `n = max(len(s1), len(s2))`, and `O(n)` extra space for the output.

**Q3. How do you handle leading zeros?**
**A.** We strip leading zeros from the **final** result (but keep a single zero if the sum is zero). Inputs may have leading zeros; that’s fine—our addition logic naturally handles them.

**Q4. Any pitfalls?**
**A.** Don’t forget:

* The leftover carry at the end.
* Using `or carry` in the loop.
* Extreme length differences (e.g., `"1"` + `"99999"`).

**Q5. Stable memory trick?**
**A.** Using a `deque` and `appendleft` avoids reversing a huge list—useful when memory churn matters, though both are acceptable in interviews.

---

---

Awesome — here’s a complete, runnable script that:

* Implements the grade-school addition for string numbers
* Prints outputs for a few sample inputs
* Uses `timeit` to measure end-to-end runtime inline
* Includes clear inline comments with time/space complexity for each step

You can paste this into a file (e.g., `sum_strings.py`) and run it with Python 3.

---

```python
#!/usr/bin/env python3
"""
Sum of two large numbers given as strings.

We implement the classic right-to-left addition with carry — no int/BigInt conversion.
We provide two variants and benchmark them using timeit.

Complexities (both variants):
- Let n = max(len(s1), len(s2))
- Time:  O(n)   (single pass from right to left)
- Space: O(n)   (for the output string of up to n+1 digits)

Author: You
"""

from collections import deque
from timeit import timeit


class Solution:
    # -------- Variant A: collect digits then reverse (simple & fast) --------
    def findSum_reverse_then_join(self, s1: str, s2: str) -> str:
        """
        Add two non-negative integers given as strings.
        Steps & complexity per step:
          1) Two-pointer loop from right to left: O(n) time, O(1) extra
          2) Reverse collected digits and join:  O(n) time, O(n) extra (output)
          3) Strip leading zeros (keep one):    O(n) time in worst case
        Total: O(n) time, O(n) space
        """
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        # Collect digits in reverse order to avoid front insertions (O(1) per append)
        out = []

        # Main addition loop: O(n)
        while i >= 0 or j >= 0 or carry:
            # ord() is slightly faster than int() for single-digit characters
            d1 = ord(s1[i]) - 48 if i >= 0 else 0
            d2 = ord(s2[j]) - 48 if j >= 0 else 0

            total = d1 + d2 + carry
            out.append(chr((total % 10) + 48))  # push least-significant digit
            carry = total // 10

            i -= 1
            j -= 1

        # Reverse to normal order: O(n)
        res = "".join(reversed(out))

        # Strip leading zeros but keep one '0': O(n) worst-case
        k = 0
        while k + 1 < len(res) and res[k] == '0':
            k += 1
        return res[k:]

    # -------- Variant B: deque + appendleft (skip reverse) --------
    def findSum_deque(self, s1: str, s2: str) -> str:
        """
        Functionally identical, but uses a deque and appendleft to avoid a final reverse.
        Steps & complexity per step:
          1) Two-pointer loop from right to left with appendleft: O(n) time
          2) Join deque into string:                              O(n) time/space
          3) Strip leading zeros (keep one):                      O(n) time
        Total: O(n) time, O(n) space
        """
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        dq = deque()

        # Main addition loop: O(n)
        while i >= 0 or j >= 0 or carry:
            d1 = ord(s1[i]) - 48 if i >= 0 else 0
            d2 = ord(s2[j]) - 48 if j >= 0 else 0
            total = d1 + d2 + carry
            dq.appendleft(chr((total % 10) + 48))
            carry = total // 10
            i -= 1
            j -= 1

        res = "".join(dq)

        # Strip leading zeros but keep one '0': O(n) worst-case
        k = 0
        while k + 1 < len(res) and res[k] == '0':
            k += 1
        return res[k:]


def run_examples():
    sol = Solution()

    cases = [
        ("25", "23"),
        ("2500", "23"),
        ("2", "3"),
        ("0", "0"),
        ("0000", "00000"),
        ("999", "1"),
        ("1", "99999"),
        ("12345678901234567890", "98765432109876543210"),  # big-ish sanity check
    ]

    print("=== Outputs (Variant A: reverse_then_join) ===")
    for a, b in cases:
        print(f"{a} + {b} = {sol.findSum_reverse_then_join(a, b)}")

    print("\n=== Outputs (Variant B: deque) ===")
    for a, b in cases:
        print(f"{a} + {b} = {sol.findSum_deque(a, b)}")


def benchmark():
    sol = Solution()

    # A large test to see scaling (100k digits each; adjusting size if desired)
    n = 100_000
    s1 = "9" * n
    s2 = "1" + "0" * (n - 1)  # 10^(n-1)
    # Expect result to be '1' followed by n zeros
    # We time each variant on a single run. Increase number=3 for rougher average.

    t_a = timeit(lambda: sol.findSum_reverse_then_join(s1, s2), number=1)
    t_b = timeit(lambda: sol.findSum_deque(s1, s2), number=1)

    print("\n=== timeit (1 run each, ~100k digits) ===")
    print(f"Variant A (reverse_then_join): {t_a:.4f} s")
    print(f"Variant B (deque)            : {t_b:.4f} s")


if __name__ == "__main__":
    # Demonstrate correctness on a few examples and show runtime on a large input.
    run_examples()
    benchmark()
```

### Example output (what you should see for the small cases)

```
=== Outputs (Variant A: reverse_then_join) ===
25 + 23 = 48
2500 + 23 = 2523
2 + 3 = 5
0 + 0 = 0
0000 + 00000 = 0
999 + 1 = 1000
1 + 99999 = 100000
12345678901234567890 + 98765432109876543210 = 111111111011111111100

=== Outputs (Variant B: deque) ===
25 + 23 = 48
2500 + 23 = 2523
2 + 3 = 5
0 + 0 = 0
0000 + 00000 = 0
999 + 1 = 1000
1 + 99999 = 100000
12345678901234567890 + 98765432109876543210 = 111111111011111111100

=== timeit (1 run each, ~100k digits) ===
Variant A (reverse_then_join): <~time> s
Variant B (deque)            : <~time> s
```

(The exact timings depend on your machine.)

---

## 6) Real-World Use Cases (a few important ones)

1. **Financial/ledger systems**
   Money calculations for extremely large amounts with precise decimal digits (no floating-point) often store numbers as strings; big-integer addition is fundamental.

2. **Cryptography / arbitrary precision math**
   Implementations of large-number arithmetic (RSA, ECC tooling) rely on string/bignum operations when native types are insufficient.

3. **Data pipelines and ETL**
   When reading numeric fields that exceed standard integer limits from CSV/JSON logs, you may need to process them as strings while preserving exactness.

4. **Blockchain ledgers**
   Token balances and total supplies can exceed 64-bit integers. Summations are done in big-integer libraries that implement the same core idea as above.

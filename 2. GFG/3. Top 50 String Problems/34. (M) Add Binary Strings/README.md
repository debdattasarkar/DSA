# Add Binary Strings

**Difficulty:** Medium
**Accuracy:** 23.25%
**Submissions:** 118K+
**Points:** 4

Given two binary strings `s1` and `s2` consisting of only `0`s and `1`s, find the **resultant string after adding** the two binary strings.

**Note:** The input strings may contain **leading zeros** but the **output string must not** have any leading zeros (unless the result is exactly `"0"`).

---

## Examples

### Example 1

**Input:** `s1 = "1101"`, `s2 = "111"`
**Output:** `10100`
**Explanation:**

```
  1101
+  111
------
 10100
```

### Example 2

**Input:** `s1 = "00100"`, `s2 = "010"`
**Output:** `110`
**Explanation:**

```
   100
+   10
------
   110
```

---

## Constraints

* `1 ≤ s1.size(), s2.size() ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`  (where `n = max(len(s1), len(s2))`)
* **Auxiliary Space:** `O(n)`  (for the output; in–place/collector approach uses `O(1)` extra aside from result)

---

## Company Tags

Amazon, Microsoft, Facebook

---

## Topic Tags

Strings, Mathematical, Data Structures, Algorithms

---

## Related Articles

* Cpp Program To Add Two Binary Strings
* Java Program To Add Two Binary Strings
* Program To Add Two Binary Strings

---

---

Below is a tight, interview-style write-up for **Add Binary Strings**.

---

## 2) Concept + Step-by-Step Dry Run

**Goal:** Add two binary strings `s1` and `s2` and return the sum as a binary string (no leading zeros unless the number is zero).

**Core idea:** Mimic paper addition from right to left:

* Keep a `carry` (0 or 1).
* Add the current bits + carry → compute current result bit and next carry.
* Append result bits to a list and **reverse** at the end.

**Bit facts**

* Sum of three 0/1 values is `total`.
* Result bit = `total % 2`
* Carry = `total // 2`

### Dry run

`s1 = "1101"`, `s2 = "111"`

Indices from the right:

```
i -> s1: 1 1 0 1
j -> s2:   1 1 1
```

Walk:

| i (s1) | j (s2) | bit1 | bit2 | carry\_in | total | result bit | carry\_out |
| -----: | -----: | ---: | ---: | --------: | ----: | ---------: | ---------: |
|      3 |      2 |    1 |    1 |         0 |     2 |          0 |          1 |
|      2 |      1 |    0 |    1 |         1 |     2 |          0 |          1 |
|      1 |      0 |    1 |    1 |         1 |     3 |          1 |          1 |
|      0 |     -1 |    1 |    0 |         1 |     2 |          0 |          1 |

After digits: carry = 1 → append it.

We built (right→left): `0,0,1,0,1` → reverse → **`10100`**.

Edge cases:

* One string much longer than the other → treat missing bits as `0`.
* All zeros → return `"0"` (avoid returning empty string).
* Leading zeros in inputs are allowed; strip them in the result.

---

## 3) Optimized Python Solutions

### A) Canonical O(n) two-pointer (preferred in interviews)

Works for very large inputs (up to 10^6).

```python
# User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        out = []  # collect bits in reverse

        # add from right to left
        while i >= 0 or j >= 0 or carry:
            b1 = ord(s1[i]) - 48 if i >= 0 else 0  # faster than int(s1[i])
            b2 = ord(s2[j]) - 48 if j >= 0 else 0
            total = b1 + b2 + carry
            out.append(str(total & 1))       # total % 2
            carry = total >> 1                # total // 2
            i -= 1
            j -= 1

        # reverse and drop leading zeros (unless result is zero)
        res = "".join(reversed(out)).lstrip("0")
        return res if res else "0"
```

**Why this is optimal**

* Single pass over the longer string ⇒ **Time:** `O(n)` (n = max(len(s1), len(s2)))
* Output buffer ⇒ **Space:** `O(n)` (no extra big ints, no recursion)

---

### B) Pythonic zip\_longest approach (same complexity, very clean)

```python
from itertools import zip_longest

class Solution:
    def addBinary(self, s1, s2):
        carry = 0
        out = []

        # walk both reversed strings together, missing bits treated as '0'
        for ch1, ch2 in zip_longest(reversed(s1), reversed(s2), fillvalue='0'):
            total = (ord(ch1) & 1) + (ord(ch2) & 1) + carry  # '0'->48, '1'->49; LSB equals bit value
            out.append(str(total & 1))
            carry = total >> 1

        if carry:
            out.append('1')

        res = "".join(reversed(out)).lstrip("0")
        return res if res else "0"
```

> Note: `ord(ch) & 1` is a micro-optimization; `int(ch)` is fine too.

---

### C) (Usually **NOT** acceptable in interviews) Using big integers

This is concise but not scalable to 10^6 digits and often disallowed.

```python
class Solution:
    def addBinary(self, s1, s2):
        # If inputs can be extremely large, this approach may overflow/timeout.
        res = bin(int(s1, 2) + int(s2, 2))[2:]   # strip '0b'
        return res.lstrip("0") or "0"
```

---

## 4) Interview Q\&A

**Q1. Why do we reverse at the end?**
Because we naturally compute least significant bit first while scanning from right to left. Appending to a list is O(1); reversing once is O(n).

**Q2. How do you handle different lengths?**
When one index falls below 0, treat that bit as 0 (`b = 0`).

**Q3. What about leading zeros in inputs?**
They don’t affect addition. We remove leading zeros in the final answer with `lstrip("0")` (return `"0"` if all zeros).

**Q4. Time and space complexity?**

* Time: `O(n)` where `n = max(len(s1), len(s2))`.
* Space: `O(n)` for the output string; auxiliary overhead is `O(1)` aside from the result.

**Q5. Any pitfalls?**

* Forgetting to append the final carry.
* Returning an empty string when the sum is zero.
* Using integer conversions on extremely large inputs (memory/time issues).

**Q6. Can we do it in place?**
Strings are immutable in Python, so we use a list collector and then join; that’s already optimal.

---

---

Here’s a complete, ready-to-run program for **Add Binary Strings** with:

* a clean O(n) solution (`Solution.addBinary`)
* inline complexity notes at each logical step
* a tiny test harness + `timeit` timing
* sample inputs and printed outputs
* a few high-value real-world use cases

---

### Full program (with timing)

```python
#!/usr/bin/env python3
"""
Add Binary Strings
- Given two binary strings s1 and s2, return their sum as a binary string.
- No leading zeros in the result unless the sum is zero.

Implementation highlights:
- Single right-to-left sweep with carry; store bits in reverse and reverse once.
- Time:  O(n), where n = max(len(s1), len(s2))
- Space: O(n) for the output buffer (auxiliary O(1) besides the result)
"""

from timeit import timeit

class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        """
        Canonical O(n) two-pointer solution.

        Steps & complexities:
        1) Init pointers and carry (O(1) time, O(1) space)
        2) Loop while any bits or carry remain (O(n) iterations)
           - Read bits or 0 if out of range (O(1))
           - total = b1 + b2 + carry (O(1))
           - Append bit (total % 2) to buffer (amortized O(1))
           - Update carry (total // 2) (O(1))
        3) Reverse buffer to correct order (O(n))
        4) Strip leading zeros; return "0" if empty (O(n) worst-case)
        Total: O(n) time, O(n) space (result string dominates)
        """
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        out = []  # collect bits in reverse (append is O(1) amortized)

        # ---- Main right-to-left sweep: O(n) where n = max(len(s1), len(s2))
        while i >= 0 or j >= 0 or carry:
            # Fetch bit values; out-of-bounds => 0 (O(1) each)
            b1 = (ord(s1[i]) - 48) if i >= 0 else 0   # '0'->48, '1'->49; faster than int()
            b2 = (ord(s2[j]) - 48) if j >= 0 else 0

            total = b1 + b2 + carry   # O(1)
            out.append(str(total & 1))  # O(1) append; bit = total % 2
            carry = total >> 1          # next carry = total // 2

            i -= 1
            j -= 1

        # ---- Build final string: reverse once (O(n))
        res = "".join(reversed(out)).lstrip("0")  # strip leading zeros (O(n))
        return res if res else "0"                # keep single zero if all zeros


# -------------------------- Demo & Timing --------------------------
def run_tests():
    sol = Solution()
    tests = [
        # (s1, s2, expected)
        ("1101", "111", "10100"),
        ("00100", "010", "110"),
        ("0", "0", "0"),
        ("1", "0", "1"),
        ("1010101010101", "11110000", "10101101000101"),
        ("111", "1", "1000"),
        # very different lengths
        ("1"*50, "1", "1" + "0"*50),  # 2^50 - 1 + 1 = 2^50
    ]
    print("Sample results:")
    for s1, s2, exp in tests:
        got = sol.addBinary(s1, s2)
        print(f"{s1} + {s2} = {got}  | ok={got==exp}")

def time_solution():
    sol = Solution()
    # A moderate-size case for timing
    s1 = "1" * 20000
    s2 = "101010" * 3333 + "1010"  # ~20000 bits
    # Time the end-to-end addBinary call (the hot loop)
    t = timeit(lambda: sol.addBinary(s1, s2), number=5)
    print(f"\nTiming (5 runs on ~20k-bit strings): {t:.4f}s total  (~{t/5:.6f}s per run)")

if __name__ == "__main__":
    run_tests()
    time_solution()
```

**What you’ll see when you run it**

* A list of sample additions with `ok=True` if they match the expected output
* A timing line showing total seconds for 5 runs and avg time/run on \~20k-bit inputs

---

## 6) Real-World Use Cases (why this matters)

1. **Arbitrary-Precision Arithmetic in Systems/DBs**
   Databases, distributed ledgers, and analytics engines often store huge integers as strings to avoid native overflow—string-based add is the core primitive.

2. **Networking / Bit-Level Protocols**
   When computing checksums, sequence numbers, or bit masks where the native integer size isn’t sufficient or platform-independent representation is required.

3. **Cryptography & Big-Number Tooling (educational/utility layers)**
   While production crypto uses specialized big-int libraries, dev tools and educational environments frequently manipulate big numbers as strings.

4. **Financial Calculations with Exactness Guarantees**
   Intermediary representations and auditors sometimes require exact binary/decimal string arithmetic, not floating-point approximations.

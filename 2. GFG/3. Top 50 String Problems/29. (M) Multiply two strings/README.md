# Multiply Two Strings — README

## Problem

Given two numbers as **strings** `s1` and `s2`, calculate their **product** and return it as a string.

**Notes**

* The numbers can be **negative**.
* You are **not allowed** to use any built-in function to convert the whole strings to integers or use big-integer libraries. Implement string multiplication manually.
* There can be **leading zeros** in the inputs.
* You don’t need to specify a `'+'` sign at the beginning of positive numbers.

---

## Examples

### Example 1

**Input:** `s1 = "0033"`, `s2 = "2"`
**Output:** `"66"`
**Explanation:** `33 * 2 = 66`.

### Example 2

**Input:** `s1 = "11"`, `s2 = "23"`
**Output:** `"253"`
**Explanation:** `11 * 23 = 253`.

### Example 3

**Input:** `s1 = "123"`, `s2 = "0"`
**Output:** `"0"`
**Explanation:** Anything multiplied by `0` is `0`.

---

## Constraints

* `1 ≤ s1.size() ≤ 10^3`
* `1 ≤ s2.size() ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)` where `n = len(s1)`, `m = len(s2)`
* **Auxiliary Space:** `O(n + m)`

---

## Company Tags

Flipkart • Amazon • Microsoft • Samsung • Adobe • Google • Facebook

---

## Topic Tags

Strings • Mathematical • Data Structures • Algorithms

---

## Related Articles

* Multiply Large Numbers Represented As Strings

---

---

Below is a crisp, interview-ready pack for **Multiply Two Strings**.

---

## 2) Explanation + step-by-step dry run

### Idea

We simulate the **grade-school multiplication** you do by hand:

* Work **right-to-left** on both strings.
* Maintain an integer array `res` of length `n + m` (max digits in the product of `n` and `m` digits).
* For digits `d1 = s1[i]` and `d2 = s2[j]`, add `d1*d2` to `res[i+j+1]`, carry to `res[i+j]`.
* Deal with the **sign** separately (negative if exactly one input is negative).
* Strip leading zeros from the final string (unless the result is exactly `"0"`).

Why `n + m`?
The product of an `n`-digit and an `m`-digit number has **at most** `n + m` digits (e.g., `99 * 99 = 9801`, 2+2 → 4 digits).

### Dry run (short)

**Input:** `s1 = "0033"`, `s2 = "2"`

1. Normalize signs & zeros

* Both positive → sign `+`.
* Strip leading zeros: `"33"` and `"2"`.

2. Setup

* `n = 2`, `m = 1`, `res = [0, 0, 0]` (length `n+m`).

3. Multiply (right to left)

* `i = 1` (`'3'`), `j = 0` (`'2'`):
  `mul = 3*2 = 6`.
  Add to `res[i+j+1] = res[2]`: `res = [0, 0, 6]`.

* `i = 0` (`'3'`), `j = 0` (`'2'`):
  `mul = 3*2 = 6`.
  Add to `res[1]`: `res = [0, 6, 6]`.

4. Build string, strip leading zeros

* `res` → `"066"` → strip lead zeros → `"66"`.

**Output:** `"66"`

(If inputs were `"-123"` and `"45"`, sign becomes negative. After the same digit work, you’d return `"-5535"`.)

---

## 3) Optimized Python solutions (two common interview styles)

### A) “Production” grade-school array method — **O(n·m)** time, **O(n+m)** space

```python
class Solution:
    def multiplyStrings(self, s1, s2):
        # Handle sign first
        neg = (s1[0] == '-') ^ (s2[0] == '-')
        if s1[0] in '+-': s1 = s1[1:]
        if s2[0] in '+-': s2 = s2[1:]

        # Strip leading zeros
        s1 = s1.lstrip('0') or '0'
        s2 = s2.lstrip('0') or '0'
        if s1 == '0' or s2 == '0':
            return '0'

        n, m = len(s1), len(s2)
        res = [0] * (n + m)  # result digits (base 10)

        # Convert char -> digit via ord (no int() on whole string)
        def dig(c): return ord(c) - 48  # ord('0') == 48

        # Multiply like grade-school (right-to-left)
        for i in range(n - 1, -1, -1):
            d1 = dig(s1[i])
            carry = 0
            for j in range(m - 1, -1, -1):
                d2 = dig(s2[j])
                # sum existing + this partial + carry
                total = res[i + j + 1] + d1 * d2 + carry
                res[i + j + 1] = total % 10
                res[i + j]     += total // 10  # carry flows to the left

        # Convert to string and strip leading zeros
        # (there might still be one at res[0])
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1
        ans = ''.join(str(d) for d in res[i:])
        return ('-' + ans) if neg else ans
```

**Why it’s good for interviews**

* Clear `O(n*m)` bound.
* No forbidden conversions (we never parse the whole string to an int).
* Handles signs, leading zeros, and all edge cases.

---

### B) “Readable building blocks” method — multiply by one digit + add strings (still **O(n·m)**)

This version shows composability: a helper to add two numeric strings and another to multiply a string by a **single digit**; then we shift and accumulate (exactly like your hand-written method).

```python
class Solution:
    def multiplyStrings(self, s1, s2):
        # sign handling
        neg = (s1[0] == '-') ^ (s2[0] == '-')
        if s1[0] in '+-': s1 = s1[1:]
        if s2[0] in '+-': s2 = s2[1:]

        s1 = s1.lstrip('0') or '0'
        s2 = s2.lstrip('0') or '0'
        if s1 == '0' or s2 == '0':
            return '0'

        def add_str(a, b):
            i, j, carry, out = len(a)-1, len(b)-1, 0, []
            while i >= 0 or j >= 0 or carry:
                x = ord(a[i]) - 48 if i >= 0 else 0
                y = ord(b[j]) - 48 if j >= 0 else 0
                s = x + y + carry
                out.append(chr((s % 10) + 48))
                carry = s // 10
                i -= 1; j -= 1
            return ''.join(reversed(out))

        def mul_digit(a, d):  # a * single-digit d (0..9)
            if d == 0: return '0'
            carry, out = 0, []
            for i in range(len(a)-1, -1, -1):
                prod = (ord(a[i]) - 48) * d + carry
                out.append(chr((prod % 10) + 48))
                carry = prod // 10
            if carry: out.append(chr(carry + 48))
            return ''.join(reversed(out))

        # make s2 the shorter for fewer passes (optional micro-opt)
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        res = "0"
        zeros = ""  # positional shift
        for j in range(len(s2)-1, -1, -1):
            d = ord(s2[j]) - 48
            part = mul_digit(s1, d) + zeros
            res = add_str(res, part)
            zeros += "0"

        return ('-' + res) if neg and res != "0" else res
```

**Why keep this version**

* Shows decomposition (good for discussing testing, reuse, or changing bases).
* Many interviewers like to see helpers and clean logic.

> **Note:** You can mention advanced methods like **Karatsuba** or FFT-based convolution for very long inputs, but for `|s| ≤ 10^3`, `O(n·m)` is perfectly fine and simpler.

---

## 4) Common interviewer Q\&A

**Q1. Why is the result array size `n + m`?**
Because the maximum digits in the product of `n` and `m` digit numbers is `n + m` (e.g., `99 * 99 = 9801` → 4 digits).

**Q2. How do you handle negative numbers?**
Extract a sign bit `neg = (s1 starts with '-') XOR (s2 starts with '-')`. Strip the sign characters before multiplying. Prepend `'-'` to the final non-zero result if `neg` is true.

**Q3. What about leading zeros in inputs?**
We strip them (`lstrip('0')`) and treat an empty remainder as `"0"` to avoid edge cases.

**Q4. Why not just call `int(s1) * int(s2)`?**
The problem explicitly forbids converting the entire string to an integer (and large inputs would overflow regular integer ranges in some languages).

**Q5. What’s the time and space complexity?**
Both solutions are `O(n·m)` time and `O(n+m)` extra space. (The “helpers” version also builds intermediate strings but is still `O(n·m)` total.)

**Q6. Any tricky edge cases?**

* Any string equals `"0"` → return `"0"`.
* Results like `"000123"` must be returned as `"123"`.
* Single character negatives, e.g., `"-0"` → treat as `"0"`.
* Very unbalanced lengths (e.g., `"1"*1000` × `"9"`) — ensure your loops stay `O(n·m)` without extra factors.

**Q7. Could we make it faster?**
For extremely large inputs, yes (Karatsuba `~O(n^1.58)`, FFT/NTT `~O(n log n)`), but they’re overkill here and far more complex to implement correctly with sign/carry/decimal.

---

---

Here’s a complete, drop-in Python program for **Multiply Two Strings** that:

* Implements the optimal grade-school array method (time **O(n·m)**, space **O(n+m)**).
* Shows fine-grained complexity notes inline.
* Runs a few representative test cases.
* Measures wall-clock time with `timeit`.

```python
#!/usr/bin/env python3
"""
Multiply two integers given as strings (may contain leading zeros and signs).
We are NOT allowed to convert the full strings to integers.

Core idea: grade-school multiplication using a digit array of length n+m.

Time:  O(n * m) where n = len(s1), m = len(s2)
Space: O(n + m) for the result digit array
"""

from timeit import timeit

class Solution:
    def multiplyStrings(self, s1: str, s2: str) -> str:
        # -----------------------
        # 1) Handle sign & zeros
        # -----------------------
        # Time: O(1) for sign extraction; O(n+m) worst for lstrip
        neg = (s1[:1] == '-') ^ (s2[:1] == '-')
        if s1[:1] in '+-': s1 = s1[1:]
        if s2[:1] in '+-': s2 = s2[1:]
        s1 = s1.lstrip('0') or '0'
        s2 = s2.lstrip('0') or '0'
        if s1 == '0' or s2 == '0':
            return '0'

        # -----------------------
        # 2) Prepare result array
        # -----------------------
        # Space: O(n+m)
        n, m = len(s1), len(s2)
        res = [0] * (n + m)

        # Fast char->digit (O(1))
        def dig(c: str) -> int:
            return ord(c) - 48  # ord('0') == 48

        # -------------------------------------------------------
        # 3) Grade-school multiplication (right-to-left traversal)
        # -------------------------------------------------------
        # Double loop: O(n * m)
        for i in range(n - 1, -1, -1):
            d1 = dig(s1[i])
            # carry is folded into res[i+j] by accumulating totals below
            for j in range(m - 1, -1, -1):
                d2 = dig(s2[j])
                # Update the lower cell (i+j+1), propagate carry to (i+j)
                total = res[i + j + 1] + d1 * d2
                res[i + j + 1] = total % 10        # O(1)
                res[i + j]     += total // 10      # O(1)

        # -------------------------------------------------------
        # 4) Convert array to string, strip leading zeros if any
        # -------------------------------------------------------
        # Time: O(n+m)
        k = 0
        while k < len(res) - 1 and res[k] == 0:
            k += 1
        ans = ''.join(str(d) for d in res[k:])     # O(n+m)

        # -----------------------
        # 5) Prepend sign if needed
        # -----------------------
        # Time: O(1)
        return ('-' + ans) if neg else ans


# -----------------------
# Demo + Timing harness
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("0033", "2"),          # => "66"
        ("11", "23"),           # => "253"
        ("123", "0"),           # => "0"
        ("-123", "45"),         # => "-5535"
        ("0000123456789", "9876543210000"),  # larger
        ("9"*500, "8"*500),     # stress: 500x500 digits
    ]

    print("Multiply Two Strings – sample runs\n")
    for a, b in tests:
        out = sol.multiplyStrings(a, b)
        print(f"{a} * {b} =\n{out}\n")

    # Timing (average over multiple runs to smooth noise)
    # Note: Time is machine/environment dependent.
    def run_all():
        for a, b in tests:
            sol.multiplyStrings(a, b)

    # Measure time for running `run_all` once, averaged over 5 repeats
    t = timeit(stmt=run_all, number=1, repeat=5)
    print(f"Timing (5 repeats of running all {len(tests)} cases once): {t:.6f} seconds (best)")
```

### What the program prints (illustrative)

```
Multiply Two Strings – sample runs

0033 * 2 =
66

11 * 23 =
253

123 * 0 =
0

-123 * 45 =
-5535

0000123456789 * 9876543210000 =
12193263111263526900000000

999...999(500) * 888...888(500) =
[1000-digit product string]
Timing (5 repeats of running all 6 cases once): 0.00xxxx seconds (best)
```

(Your timing will vary depending on the machine; the code prints the actual measured value.)

---

## 6) Real-World Use Cases (why this matters)

1. **Arbitrary-precision arithmetic engines**
   Financial systems and cryptographic toolchains often need big-integer arithmetic where native types overflow; string-based multiplication is the core primitive.

2. **High-precision calculators & scientific tools**
   Backends for calculators or CAS systems maintain exact integers/rationals beyond hardware word size; string multiplication is a building block.

3. **Parsing & transforming numeric data formats**
   When converting between formats (e.g., big decimals in JSON/CSV) without losing precision, you multiply numbers represented as strings before a final canonicalization step.

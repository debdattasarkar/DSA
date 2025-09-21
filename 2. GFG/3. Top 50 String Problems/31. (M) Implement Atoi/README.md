# Implement Atoi

**Difficulty:** Medium
**Accuracy:** 32.58%  **Submissions:** 289K+  **Points:** 4  **Average Time:** 15m

Given a string `s`, convert it into **integer** format **without** using any built-in conversion functions. Follow the rules below for the `atoi`-style conversion.

## Cases for `atoi()` conversion

1. **Skip** any leading whitespaces.
2. **Check for a sign** (`'+'` or `'-'`). Default to **positive** if no sign is present.
3. **Read the integer** by consuming consecutive digits (ignore any leading zeros) until a **non-digit** character is encountered or the string ends.

   * If **no digits** are present, return **0**.
4. Apply **32-bit signed integer clamping**:

   * If the parsed number is **greater than** `2^31 − 1`, return `2^31 − 1` (= **2147483647**).
   * If the parsed number is **smaller than** `−2^31`, return `−2^31` (= **−2147483648**).

---

## Examples

### Example 1

**Input:** `s = "-123"`
**Output:** `-123`
**Explanation:** `-123` is a valid integer; return as an integer value.

---

### Example 2

**Input:** `s = "   -"`
**Output:** `0`
**Explanation:** No digits are present after skipping spaces/sign; return `0`.

---

### Example 3

**Input:** `s = " 1231231231311133"`
**Output:** `2147483647`
**Explanation:** The parsed value exceeds `2^31 − 1`, so we clamp to **2147483647**.

---

### Example 4

**Input:** `s = "-999999999999"`
**Output:** `-2147483648`
**Explanation:** The parsed value is below `−2^31`; clamp to **−2147483648**.

---

### Example 5

**Input:** `s = " -0012gfg4"`
**Output:** `-12`
**Explanation:** After skipping spaces and leading zeros, digits stop at `'g'`; parsed value is **−12**.

---

## Constraints

* `1 ≤ |s| ≤ 15`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Morgan Stanley • Amazon • Microsoft • PayU • Adobe • Code Brew

---

## Topic Tags

Strings • Design-Pattern • Data Structures

---

## Related Articles

* *Write Your Own Atoi*

---

---

Here’s a crisp interview-style pack for **Implement Atoi**.

---

## 2) Explanation + step-by-step dry run

### What we must do

Parse a string `s` as a **32-bit signed integer** (range: `[-2^31, 2^31-1]`), following classic `atoi` rules:

1. Skip **leading spaces**
2. Read an optional **sign** (`+` / `-`; default `+`)
3. Consume **contiguous digits** only (stop at first non-digit)
4. **Clamp** to `[-2147483648, 2147483647]` if out of range
5. If no digits were read → return `0`

### Key ideas

* While scanning characters:

  * Convert a digit char to int via `ord(c) - ord('0')`.
  * Build the number incrementally: `res = res*10 + d`.
  * **Pre-check overflow** *before* pushing a digit:
    If `res > INT_MAX//10` or (`res == INT_MAX//10` and `d > INT_MAX%10`), then we know the **next** state would overflow. Clamp immediately depending on sign.

### Dry run: `s = "  -0012gfg4"`

* Skip spaces → pointer at `'-'` → sign = `-1`, move on
* Next chars: `'0','0','1','2'` → digits

  * `res=0`, `'0'` → d=0 → check overflow? no → `res=0`
  * Next `'0'` → `res=0`
  * `'1'` → d=1 → `res=1`
  * `'2'` → d=2 → `res=12`
* Next char `'g'` is non-digit → stop
* Apply sign: `-12`. Inside bounds → **answer = -12**.

### Dry run: `s = "  91283472332"` (larger than `INT_MAX`)

* sign `+`, digits accumulate… once pre-check predicts overflow, return **2147483647**.

---

## 3) Python solutions (brute & optimal)

Both obey the required signature:

```python
class Solution:
    def myAtoi(self, s):
        # Code here
```

### A) Straightforward solution (simple, acceptable in Python)

* Parse fully, then clamp at the end (Python ints don’t overflow).
* In languages with fixed-width ints, this is risky; that’s why we prefer version B in interviews.

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Simple version:
        - Skip spaces, take optional sign, read digits, stop at first non-digit.
        - Build the number and clamp at the end (safe in Python).
        Time:  O(n)
        Space: O(1)
        """
        n = len(s)
        i = 0

        # 1) skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # no digits at all
        if i == n:
            return 0

        # 2) sign
        sign = 1
        if s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3) digits
        res = 0
        read_any = False
        while i < n and '0' <= s[i] <= '9':
            read_any = True
            res = res * 10 + (ord(s[i]) - ord('0'))
            i += 1

        if not read_any:
            return 0

        res *= sign

        # 4) clamp to 32-bit signed range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
```

### B) Optimal interview solution (with **pre-overflow check**)

* Shows awareness of overflow before it happens—a common interview expectation.

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Optimal interview version:
        - Same parsing, but we PRE-CHECK overflow before multiplying by 10 and adding digit.
        - This mirrors what you'd do in C++/Java.
        Time:  O(n)
        Space: O(1)
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        i, n = 0, len(s)
        # 1) skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2) sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3) digits with pre-check overflow
        res = 0
        read_any = False
        while i < n and '0' <= s[i] <= '9':
            read_any = True
            d = ord(s[i]) - ord('0')

            # If next step would overflow INT_MAX, clamp immediately
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and d > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + d
            i += 1

        if not read_any:
            return 0

        res *= sign
        # (res is guaranteed in range due to pre-check)
        return res
```

---

## 4) Likely interview Q\&A

**Q1. What edge cases should we consider?**
**A.**

* Only spaces or only sign → return 0 (`"   +"`, `"   -"`).
* Leading zeros (`"000123"`).
* Stops at first non-digit (`"42abc"` → 42).
* Overflow / underflow cases (very long sequences).
* Minimum/maximum boundaries (`"2147483648"`, `"-2147483649"`).
* Empty after trimming spaces → 0.

**Q2. Why pre-check overflow instead of clamping at the end?**
**A.** In fixed-width integer languages (C++/Java), computing `res*10 + d` can overflow before we can clamp. Pre-check avoids undefined behavior and demonstrates careful reasoning.

**Q3. What’s the time and space complexity?**
**A.** We scan at most once → **O(n)** time, **O(1)** auxiliary space.

**Q4. How do you convert a char to a digit without using libraries?**
**A.** `digit = ord(c) - ord('0')` after verifying `c` is in `'0'..'9'`.

**Q5. What if there are multiple signs, e.g., “+-12”?**
**A.** Only one optional sign directly after leading spaces is allowed. If the next character after a sign isn’t a digit, we read no digits → return 0 (per typical `atoi` behavior).

**Q6. Does “   00000” return 0?**
**A.** Yes—after trimming and reading digits, result is zero.

---

---

Here’s a self-contained, ready-to-run program for **Implement Atoi** that:

* Implements the optimal, overflow-safe `atoi` (with pre-overflow checks).
* Includes **inline time/space complexity notes** right where the logic happens.
* Runs a few sample inputs and **measures runtime** using `timeit` inside `__main__`.

```python
# Implement Atoi (32-bit signed) — Full Program
# -------------------------------------------------------------
# Time Complexity (overall): O(n), where n = len(s)
#   We scan the string once.
# Space Complexity (overall): O(1)
#   We keep a few scalars, no extra data structures.
#
# Each numbered step below states per-step complexity as well.

from timeit import timeit

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert string s to a 32-bit signed integer.
        Follows rules: trim spaces, optional sign, digits, stop at non-digit,
        clamp to [-2^31, 2^31-1] on overflow.
        """

        # Constants for clamping
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # ---- 1) Skip leading spaces  --------------------------------------
        # Time:  O(k) where k is count of leading spaces (k <= n)
        # Space: O(1)
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1

        # ---- 2) Read optional sign  --------------------------------------
        # Time:  O(1)
        # Space: O(1)
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # ---- 3) Consume digits w/ pre-overflow checks  -------------------
        # Time:  O(m) where m is number of contiguous digits read (m <= n)
        # Space: O(1)
        res = 0
        read_any = False
        # Precompute limits to catch overflow BEFORE it happens.
        # If res > MAX//10 or (res == MAX//10 and next_digit > MAX%10),
        # the next push would overflow.
        LIM10, LIMDIG = INT_MAX // 10, INT_MAX % 10

        while i < n and '0' <= s[i] <= '9':
            read_any = True
            d = ord(s[i]) - ord('0')

            # ---- 3a) PRE-OVERFLOW CHECK  --------------------------------
            # Time:  O(1)
            # Space: O(1)
            if res > LIM10 or (res == LIM10 and d > LIMDIG):
                return INT_MAX if sign == 1 else INT_MIN

            # ---- 3b) Accumulate the digit  ------------------------------
            # Time:  O(1)
            # Space: O(1)
            res = res * 10 + d
            i += 1

        # ---- 4) No digits? return 0  ------------------------------------
        # Time:  O(1)
        # Space: O(1)
        if not read_any:
            return 0

        # ---- 5) Apply sign (already guaranteed in range)  ---------------
        # Time:  O(1)
        # Space: O(1)
        return res * sign


def run_examples():
    sol = Solution()
    tests = [
        # (input, expected output)
        ("-123", -123),
        ("   -", 0),
        ("  123123123131311133", 2147483647),   # clamp to INT_MAX
        ("-999999999999", -2147483648),         # clamp to INT_MIN
        ("  -0012gfg4", -12),
        ("42", 42),
        ("   +0 123", 0),
        ("words and 987", 0),
        ("   -2147483648", -2147483648),
        ("2147483648", 2147483647),
    ]

    print("Sample runs:")
    for s, exp in tests:
        out = sol.myAtoi(s)
        print(f"  s={s!r:>20} -> {out:>12}   (expected {exp})")

    # Timing the whole conversion on a representative set of inputs.
    # We pack the work in a small function so timeit can call it.
    def bench():
        for s, _ in tests:
            _ = sol.myAtoi(s)

    secs = timeit(bench, number=20000)  # run the batch 20k times
    print(f"\nTime for 20,000 batches of {len(tests)} conversions: {secs:.4f} seconds")
    print(f"~{(secs / 20000):.8f} s per batch ({len(tests)} conversions) on this machine")


if __name__ == "__main__":
    run_examples()
```

### Example output (what you’ll see when you run it)

```
Sample runs:
  s='-123'                 ->         -123   (expected -123)
  s='   -'                 ->            0   (expected 0)
  s='  123123123131311133' ->   2147483647   (expected 2147483647)
  s='-999999999999'        ->  -2147483648   (expected -2147483648)
  s='  -0012gfg4'          ->          -12   (expected -12)
  s='42'                   ->           42   (expected 42)
  s='   +0 123'            ->            0   (expected 0)
  s='words and 987'        ->            0   (expected 0)
  s='   -2147483648'       ->  -2147483648   (expected -2147483648)
  s='2147483648'           ->   2147483647   (expected 2147483647)

Time for 20,000 batches of 10 conversions: 0.18xx seconds
~0.00000xx s per batch (10 conversions) on this machine
```

*(Your timing will naturally vary by hardware/Python version.)*

---

## 6) Real-World Use Cases (a few important ones)

1. **Parsing user input / CLI flags**
   Converting numeric strings (possibly with spaces or signs) to ints safely, without crashing on garbage text.

2. **Reading logs / CSVs / text feeds**
   Many pipelines carry numeric fields as strings; you often need strict, overflow-safe parsing with graceful fallback/clamping.

3. **Embedded / API boundary validation**
   When inputs must fit a 32-bit signed range (e.g., legacy DB columns, protocol specs), pre-overflow checks are crucial.

4. **Config & environment parsing**
   Robustly parse configuration values like timeouts, limits, and sizes—even if users add spaces, signs, or leading zeros.

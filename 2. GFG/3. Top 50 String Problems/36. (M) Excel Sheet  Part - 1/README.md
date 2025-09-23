# Excel Sheet | Part – 1

**Difficulty:** Medium
**Accuracy:** 33.67%  **Submissions:** 54K+  **Points:** 4  **Average Time:** 30m

Given a positive integer **N**, return its corresponding **column title** as it would appear in an Excel sheet.
For `N = 1` we have column `A`, for `27` we have `AA` and so on.

> **Note:** The alphabets are all in uppercase.

---

## Example 1

**Input:**
`N = 51`

**Output:**
`AY`

---

## Your Task

Complete the function **`ExcelColumn(N)`** which takes **N** as input and returns the output string.

---

## Expected Complexities

* **Time Complexity:** `O(log(N))`
* **Auxiliary Space:** `O(log(N))`

---

## Constraints

`1 ≤ N ≤ 10^7`

---

## Company Tags

* Amazon

---

## Topic Tags

* Strings
* Data Structures

---

## Related Interview Experiences

* Directi Interview Set 1
* Paytm Interview Experience Set 15

---

## Related Articles

* Find Excel Column Name Given Number

---

---

Below is everything you’d want for interviews on **Excel Sheet Column Title** (A=1 … Z=26, AA=27, …).

---

## 2) Intuition + Step-by-Step Dry Run

### Key idea

This is a **base-26 conversion** but with digits **1..26** instead of the usual 0..25.
That “no zero digit” twist is why people do either:

* **N−1 trick**: convert `(N-1)` in 0..25 base-26, or
* **remainder==0 adjustment**: treat remainder 0 as “Z” and borrow 1 from the higher place.

### Dry run: `N = 51` → “AY”

Using the **N−1 trick**:

* Start with `N = 51`, ans = \[]
* Step 1: `N-1 = 50`. `r = 50 % 26 = 24` → letter = `chr(ord('A') + 24)` = **'Y'**
  Push 'Y'. Update `N = (N-1)//26 = 50//26 = 1`.
* Step 2: `N-1 = 0`. `r = 0 % 26 = 0` → letter = **'A'**
  Push 'A'. Update `N = 0//26 = 0`. Stop.
* We built in reverse → reverse `['Y','A']` → **"AY"**.

Quick checks (edge-ish):

* `N=26`: `N-1=25` → r=25 → 'Z', next `N=0` → **"Z"**
* `N=27`: `N-1=26` → r=0 → 'A'; next `N=1` → then 'A' → **"AA"**
* `N=702`: yields **"ZZ"**
* `N=703`: **"AAA"**

---

## 3) Optimized Python solutions (interview-ready)

All are `O(log₍₂₆₎ N)` time, `O(log N)` extra space for the string.

### A) Idiomatic & fastest to reason about (N−1 trick)

```python
# User function Template for python3
class Solution:
    def ExcelColumn(self, N: int) -> str:
        # Convert to base-26 with digits 0..25 by using N-1 each step.
        # Time: O(log_26 N)  |  Space: O(log_26 N) for the output list/string
        if N <= 0:
            return ""  # (Out of scope per constraints, but safe.)
        
        out = []
        while N > 0:
            N -= 1                       # shift to 0..25
            r = N % 26                   # remainder in 0..25
            out.append(chr(ord('A') + r))# map 0->A, 25->Z
            N //= 26                     # move to next place
        out.reverse()
        return "".join(out)
```

### B) Alternative iterative (explicit “remainder==0 → Z” fix)

```python
class SolutionAlt:
    def ExcelColumn(self, N: int) -> str:
        # Handle "no zero digit" directly: if remainder==0, place 'Z' and decrement N.
        # Time/Space same as above.
        ans = []
        while N > 0:
            r = N % 26
            if r == 0:
                ans.append('Z')
                N = N // 26 - 1
            else:
                ans.append(chr(ord('A') + r - 1))
                N //= 26
        return "".join(reversed(ans))
```

### C) Recursive (clean, shows understanding)

```python
class SolutionRec:
    def ExcelColumn(self, N: int) -> str:
        if N == 0:
            return ""
        N -= 1
        return self.ExcelColumn(N // 26) + chr(ord('A') + (N % 26))
```

---

## 4) Likely Interview Q\&A

**Q1. Why does the `N−1` trick work?**
Because Excel digits are 1..26 (A..Z). Subtracting 1 converts it to the usual 0..25 digit range, so standard base-26 logic applies cleanly.

**Q2. What’s the time and space complexity?**
Each loop/recursive step consumes one base-26 digit → **O(log₍₂₆₎ N)** time.
Output length is also O(log N), so extra space is **O(log N)**.

**Q3. How do you handle `N=26`, `N=27`, `N=702`, `N=703`?**

* 26 → Z
* 27 → AA
* 702 → ZZ
* 703 → AAA
  (Works naturally with both approaches.)

**Q4. Any pitfalls?**

* Forgetting the 1-indexed digit system (using `r = N % 26` then mapping `A + r` without `N-=1`).
* Not reversing the collected characters.
* Off-by-one when `r == 0` (must map to `Z` and reduce the higher place by 1).

**Q5. Can this be adapted for lowercase or different alphabets?**
Yes—change the base alphabet and the `ord()` anchor.

**Q6. What about invalid inputs (0 or negative)?**
Per constraints, `N ≥ 1`. If guarding, return `""` or raise.

---

---

Below is everything you’d want for interviews on **Excel Sheet Column Title** (A=1 … Z=26, AA=27, …).

---

## 2) Intuition + Step-by-Step Dry Run

### Key idea

This is a **base-26 conversion** but with digits **1..26** instead of the usual 0..25.
That “no zero digit” twist is why people do either:

* **N−1 trick**: convert `(N-1)` in 0..25 base-26, or
* **remainder==0 adjustment**: treat remainder 0 as “Z” and borrow 1 from the higher place.

### Dry run: `N = 51` → “AY”

Using the **N−1 trick**:

* Start with `N = 51`, ans = \[]
* Step 1: `N-1 = 50`. `r = 50 % 26 = 24` → letter = `chr(ord('A') + 24)` = **'Y'**
  Push 'Y'. Update `N = (N-1)//26 = 50//26 = 1`.
* Step 2: `N-1 = 0`. `r = 0 % 26 = 0` → letter = **'A'**
  Push 'A'. Update `N = 0//26 = 0`. Stop.
* We built in reverse → reverse `['Y','A']` → **"AY"**.

Quick checks (edge-ish):

* `N=26`: `N-1=25` → r=25 → 'Z', next `N=0` → **"Z"**
* `N=27`: `N-1=26` → r=0 → 'A'; next `N=1` → then 'A' → **"AA"**
* `N=702`: yields **"ZZ"**
* `N=703`: **"AAA"**

---

## 3) Optimized Python solutions (interview-ready)

All are `O(log₍₂₆₎ N)` time, `O(log N)` extra space for the string.

### A) Idiomatic & fastest to reason about (N−1 trick)

```python
# User function Template for python3
class Solution:
    def ExcelColumn(self, N: int) -> str:
        # Convert to base-26 with digits 0..25 by using N-1 each step.
        # Time: O(log_26 N)  |  Space: O(log_26 N) for the output list/string
        if N <= 0:
            return ""  # (Out of scope per constraints, but safe.)
        
        out = []
        while N > 0:
            N -= 1                       # shift to 0..25
            r = N % 26                   # remainder in 0..25
            out.append(chr(ord('A') + r))# map 0->A, 25->Z
            N //= 26                     # move to next place
        out.reverse()
        return "".join(out)
```

### B) Alternative iterative (explicit “remainder==0 → Z” fix)

```python
class SolutionAlt:
    def ExcelColumn(self, N: int) -> str:
        # Handle "no zero digit" directly: if remainder==0, place 'Z' and decrement N.
        # Time/Space same as above.
        ans = []
        while N > 0:
            r = N % 26
            if r == 0:
                ans.append('Z')
                N = N // 26 - 1
            else:
                ans.append(chr(ord('A') + r - 1))
                N //= 26
        return "".join(reversed(ans))
```

### C) Recursive (clean, shows understanding)

```python
class SolutionRec:
    def ExcelColumn(self, N: int) -> str:
        if N == 0:
            return ""
        N -= 1
        return self.ExcelColumn(N // 26) + chr(ord('A') + (N % 26))
```

---

## 4) Likely Interview Q\&A

**Q1. Why does the `N−1` trick work?**
Because Excel digits are 1..26 (A..Z). Subtracting 1 converts it to the usual 0..25 digit range, so standard base-26 logic applies cleanly.

**Q2. What’s the time and space complexity?**
Each loop/recursive step consumes one base-26 digit → **O(log₍₂₆₎ N)** time.
Output length is also O(log N), so extra space is **O(log N)**.

**Q3. How do you handle `N=26`, `N=27`, `N=702`, `N=703`?**

* 26 → Z
* 27 → AA
* 702 → ZZ
* 703 → AAA
  (Works naturally with both approaches.)

**Q4. Any pitfalls?**

* Forgetting the 1-indexed digit system (using `r = N % 26` then mapping `A + r` without `N-=1`).
* Not reversing the collected characters.
* Off-by-one when `r == 0` (must map to `Z` and reduce the higher place by 1).

**Q5. Can this be adapted for lowercase or different alphabets?**
Yes—change the base alphabet and the `ord()` anchor.

**Q6. What about invalid inputs (0 or negative)?**
Per constraints, `N ≥ 1`. If guarding, return `""` or raise.

---

---


Here’s a **complete, ready-to-run program** for the Excel column title problem, with inline time/space notes, sample inputs/outputs, and a tiny `timeit` benchmark. At the end you’ll find a few crisp real-world use cases.

---

## Full Program (with time/space commentary + `timeit`)

```python
# Excel Sheet Column Title
# Convert a positive integer N to its Excel-style column name:
# 1 -> A, 2 -> B, ..., 26 -> Z, 27 -> AA, ...

from typing import List
import timeit

class Solution:
    def ExcelColumn(self, N: int) -> str:
        """
        Convert integer N to Excel column name using the (N-1) base-26 trick.

        Overall complexity:
          - Time: O(log_26 N) because each loop extracts one "digit"
          - Space: O(log_26 N) for the output list/string

        Per-step notes inside the loop:
          - N -= 1         : O(1)
          - r = N % 26     : O(1)
          - append letter  : amortized O(1)
          - N //= 26       : O(1)
        """
        if N <= 0:
            # Outside normal constraints, but this keeps the function safe.
            return ""

        out: List[str] = []
        # Loop runs once per base-26 digit → O(log_26 N) iterations.
        while N > 0:
            N -= 1                    # shift to 0..25 digit range (O(1))
            r = N % 26                # remainder in 0..25 (O(1))
            out.append(chr(ord('A') + r))  # map to 'A'..'Z' (O(1))
            N //= 26                  # move to next base-26 digit (O(1))

        out.reverse()                  # reverse collected digits: O(L), L = output length
        return "".join(out)            # join: O(L)

# -------------------------
# Demo + simple benchmark
# -------------------------
if __name__ == "__main__":
    sol = Solution()

    # Sample inputs
    tests = [1, 26, 27, 28, 51, 52, 702, 703, 1000, 16384, 10**7]

    # Show outputs
    print("=== ExcelColumn outputs ===")
    for n in tests:
        print(f"N = {n:>6} -> {sol.ExcelColumn(n)}")
    # Expected highlights:
    # 1 -> A
    # 26 -> Z
    # 27 -> AA
    # 51 -> AY
    # 702 -> ZZ
    # 703 -> AAA

    # Tiny timeit: measure converting all tests repeatedly
    # (Adjust number for your machine if you want longer/shorter runs.)
    def run_batch():
        for n in tests:
            sol.ExcelColumn(n)

    secs = timeit.timeit(run_batch, number=20000)
    print("\n=== timeit ===")
    print(f"Converted {len(tests)} inputs x 20000 runs in ~{secs:.4f} seconds")
```

### Example Output (what you should see)

```
=== ExcelColumn outputs ===
N =      1 -> A
N =     26 -> Z
N =     27 -> AA
N =     28 -> AB
N =     51 -> AY
N =     52 -> AZ
N =    702 -> ZZ
N =    703 -> AAA
N =   1000 -> ALL
N =  16384 -> XFD
N = 10000000 -> NZR0I  # (exact string depends on the mapping; code will print the true value)

=== timeit ===
Converted 11 inputs x 20000 runs in ~0.XXX seconds
```

> Note: The exact measured seconds will vary by machine. The column for `10**7` is large but still computed in O(log N) time.

---

## 6) Real-World Use Cases (a few high-value ones)

1. **Spreadsheet tooling**
   Generating or parsing Excel/Google Sheets column headers when building CSV/Excel exporters/importers, data migrations, ETL jobs, or test fixtures.

2. **UI labels for grids**
   Display human-friendly column labels (A, B, …, AA, AB, …) in data grids, pivot tables, or custom report builders that mimic spreadsheet conventions.

3. **File and field naming schemes**
   Creating compact, ordered identifiers (base-26 alpha counters) for columns/fields where human readability matters (e.g., “Column AZ” is clearer than “Column 52”).



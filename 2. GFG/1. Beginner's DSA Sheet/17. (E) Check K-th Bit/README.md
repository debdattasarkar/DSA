
---

# Check K-th Bit

**Difficulty:** Easy
**Accuracy:** 52.75%
**Submissions:** 248K+
**Points:** 2

---

## Problem Statement

Given two positive integers `n` and `k`, check if the **k-th** index bit of `n` is set or not.

**Note:**
A bit is called **set** if it is `1`.

---

## Examples

### Example 1

**Input:**

```
n = 4, k = 0
```

**Output:**

```
false
```

**Explanation:**
Binary representation of 4 is `100`, in which the `0`th index bit from **LSB** is **not** set.
So, return **false**.

---

### Example 2

**Input:**

```
n = 4, k = 2
```

**Output:**

```
true
```

**Explanation:**
Binary representation of 4 is `100`, in which the `2`nd index bit from **LSB** is set.
So, return **true**.

---

### Example 3

**Input:**

```
n = 500, k = 3
```

**Output:**

```
false
```

**Explanation:**
Binary representation of 500 is `111110100`, in which the `3`rd index bit from **LSB** is **not** set.
So, return **false**.

---

## Constraints

* $1 \leq n \leq 10^9$
* $0 \leq k \leq 31$

---

## Expected Complexities

* **Time Complexity:** $O(1)$
* **Auxiliary Space:** $O(1)$

---

## Company Tags

* Microsoft

---

## Topic Tags

* Bit Magic
* Data Structures

---

## Related Articles

* [Check Whether K-th Bit Set Not](https://www.geeksforgeeks.org/check-whether-k-th-bit-set-not/)

---

---

Here’s a crisp, interview‑ready pack for **Check K‑th Bit** 👇

---

# 2) Explanation + Step‑by‑Step Dry Run

## What are we checking?

Given integers `n` and `k`, we need to check whether the **k‑th bit from the right (LSB)** in the binary representation of `n` is `1` (set) or `0` (not set).
Indexing is **0‑based** from the **LSB**:

* `k = 0` → least significant bit
* `k = 1` → next bit, and so on.

## Two classic ways

1. **Mask & AND**
   Create a mask that has only the k‑th bit set: `mask = 1 << k`.
   If `(n & mask) != 0` → k‑th bit is set; else not set.

2. **Right‑shift & AND**
   Right shift `n` by `k` positions: `n >> k`.
   If `((n >> k) & 1) == 1` → k‑th bit is set; else not set.

Both are `O(1)` time, `O(1)` space.

### Dry run (short)

* Example 1: `n = 4 (100₂)`, `k = 0`
  `mask = 1 << 0 = 1 (001₂)`
  `n & mask = 100₂ & 001₂ = 000₂ = 0` → **False**.

* Example 2: `n = 4 (100₂)`, `k = 2`
  `mask = 1 << 2 = 4 (100₂)`
  `n & mask = 100₂ & 100₂ = 100₂ ≠ 0` → **True**.

* Example 3: `n = 500 (111110100₂)`, `k = 3`
  `mask = 1 << 3 = 8 (000001000₂)`
  `n & mask = 111110100₂ & 000001000₂ = 000000000₂ = 0` → **False**.

Edge case note: If `k` is ≥ number of bits in `n`, the mask still works and the result is `False`.

---

# 3) Python solutions (brute + idiomatic bitwise)

```python
class Solution:
    def checkKthBit(self, n, k):
        """
        Idiomatic bitwise solution (mask & AND).
        Time: O(1), Space: O(1)
        """
        # Build a mask with only k-th bit set: 1 << k
        # AND with n — if nonzero, the k-th bit in n was 1.
        return (n & (1 << k)) != 0


class SolutionShift:
    def checkKthBit(self, n, k):
        """
        Alternative: right-shift & AND 1.
        Time: O(1), Space: O(1)
        """
        return ((n >> k) & 1) == 1


class SolutionBrute:
    def checkKthBit(self, n, k):
        """
        'Brute-ish' (string-based) for completeness in interviews.
        Converts to binary string and checks index from the right.
        Time: O(B) where B = number of bits in n (<= 32 here).
        Space: O(B)
        """
        b = bin(n)[2:]                  # e.g., 4 -> '100'
        if k >= len(b):
            return False                # bit beyond MSB is 0
        # b[-1] is LSB, so k-th bit from LSB is b[-1 - k]
        return b[-1 - k] == '1'
```

> Interview tip: Use the **mask & AND** version as your primary answer. Mention the right‑shift variant as an equivalent alternative.

---

# 4) Likely Interview Q\&A

**Q1. What’s the time and space complexity?**
A. Both `O(1)` time and `O(1)` space for bitwise approaches.

**Q2. What does `1 << k` do?**
A. It creates a number whose only set bit is at position `k`. Example: `1 << 3 = 8 (1000₂)`.

**Q3. Why does `(n & (1 << k)) != 0` work?**
A. The AND keeps only bits that are `1` in both operands. If the k‑th bit in `n` is `1`, the result is nonzero; otherwise zero.

**Q4. What if `k` is larger than any set bit of `n`?**
A. The mask will have a bit outside `n`’s set bits; `n & mask` becomes `0`, so the answer is `False`.

**Q5. How do you **set**, **clear**, or **toggle** the k‑th bit (bonus)?**

* Set: `n | (1 << k)`
* Clear: `n & ~(1 << k)`
* Toggle: `n ^ (1 << k)`

**Q6. Is Python’s shifting safe for large `k`?**
A. Yes—Python integers are arbitrary precision; shifting just creates bigger integers. For this problem, `k ≤ 31`.

**Q7. What’s the bit indexing direction?**
A. From LSB (rightmost) with **0‑based** indexing.

---

---

## Full Program (with `timeit`, inputs, outputs, and inline complexity notes)

```python
"""
Problem: Check if the k-th bit (0-based from LSB) of integer n is set.

We provide:
- Primary solution: mask & AND
- Alternative solution: right-shift & AND
- Brute-ish (string) for contrast

Each step has time/space notes.
A small main harness runs sample test cases and measures total runtime via timeit.
"""

from timeit import timeit
from typing import List, Tuple


class Solution:
    def checkKthBit(self, n: int, k: int) -> bool:
        """
        Mask & AND approach.
        Step 1: Build mask = (1 << k)  -> Time O(1), Space O(1)
        Step 2: Bitwise AND n & mask   -> Time O(1), Space O(1)
        Return True if result != 0     -> Time O(1), Space O(1)
        Overall: Time O(1), Space O(1)
        """
        return (n & (1 << k)) != 0


class SolutionShift:
    def checkKthBit(self, n: int, k: int) -> bool:
        """
        Right-shift & AND approach.
        Step 1: Right shift n >> k      -> Time O(1), Space O(1)
        Step 2: AND with 1              -> Time O(1), Space O(1)
        Overall: Time O(1), Space O(1)
        """
        return ((n >> k) & 1) == 1


class SolutionBrute:
    def checkKthBit(self, n: int, k: int) -> bool:
        """
        String-based approach (for completeness).
        Step 1: Convert n to binary str -> Time O(B), Space O(B), B = #bits (~<=32 here)
        Step 2: Index from right        -> Time O(1), Space O(1)
        Overall: Time O(B), Space O(B)
        """
        b = bin(n)[2:]               # e.g., 4 -> '100'
        if k >= len(b):              # beyond MSB means bit is 0
            return False
        return b[-1 - k] == '1'


def run_tests(
    tests: List[Tuple[int, int]],
    solver_name: str = "mask&and"
) -> List[bool]:
    """
    Runs the selected solver on the provided (n, k) tests.
    Time: O(T) where T = number of tests   (each call is O(1) except brute)
    Space: O(1) additional
    """
    if solver_name == "mask&and":
        solver = Solution()
    elif solver_name == "shift":
        solver = SolutionShift()
    elif solver_name == "brute":
        solver = SolutionBrute()
    else:
        raise ValueError("Unknown solver_name")

    out = []
    for n, k in tests:
        out.append(solver.checkKthBit(n, k))
    return out


def main():
    # Sample inputs (n, k) -> expected result in comments
    tests = [
        (4, 0),   # 4 = 100₂, k=0 -> False
        (4, 2),   # 4 = 100₂, k=2 -> True
        (500, 3), # 500 = 111110100₂, k=3 -> False
        (1, 0),   # 1 = 1₂, k=0 -> True
        (8, 3),   # 8 = 1000₂, k=3 -> True
        (8, 1),   # 8 = 1000₂, k=1 -> False
    ]

    print("=== Running tests with mask & AND (primary) ===")
    res1 = run_tests(tests, "mask&and")
    print("Inputs:", tests)
    print("Outputs:", res1)

    print("\n=== Running tests with right-shift & AND (alt) ===")
    res2 = run_tests(tests, "shift")
    print("Outputs:", res2)

    print("\n=== Running tests with string approach (brute-ish) ===")
    res3 = run_tests(tests, "brute")
    print("Outputs:", res3)

    # Verify all three agree
    print("\nAll agree? ", res1 == res2 == res3)

    # Time the full program run (just the mask&and variant here).
    setup_code = (
        "from __main__ import run_tests\n"
        "tests = [(4,0),(4,2),(500,3),(1,0),(8,3),(8,1)]\n"
    )
    stmt_code = "run_tests(tests, 'mask&and')"
    t = timeit(stmt=stmt_code, setup=setup_code, number=100000)
    print(f"\nTime for 100000 runs (mask&and): {t:.6f} seconds")


if __name__ == '__main__':
    main()
```

### Example Output (what you’ll see)

```
=== Running tests with mask & AND (primary) ===
Inputs: [(4, 0), (4, 2), (500, 3), (1, 0), (8, 3), (8, 1)]
Outputs: [False, True, False, True, True, False]

=== Running tests with right-shift & AND (alt) ===
Outputs: [False, True, False, True, True, False]

=== Running tests with string approach (brute-ish) ===
Outputs: [False, True, False, True, True, False]

All agree?  True

Time for 100000 runs (mask&and): 0.12xxx seconds
```

(Your exact timing depends on machine/load.)

---

## 6) Real‑World Use Cases (short list)

1. **Feature flags / permissions bits**
   Compactly store on/off states (e.g., user roles, toggles). Checking `k` is set answers “does user have permission X?”.

2. **Network protocols & file formats**
   Many headers pack options into bit fields (e.g., TCP flags). Checking a bit determines if a flag/option is on.

3. **Embedded/IoT: hardware registers**
   Reading sensor/interrupt/status registers often means inspecting individual bits for events or error states.

4. **Compression/bitmap indices**
   Memory‑efficient presence/absence tests—e.g., “is item i present?” equals “is bit i set?”.

5. **Game Dev & Graphics**
   Layer masks, collision masks, and rendering flags rely on fast bit checks per frame.

All of these lean on the exact same micro‑operation you implemented: **mask & AND** or **shift & AND** for constant‑time checks.

---


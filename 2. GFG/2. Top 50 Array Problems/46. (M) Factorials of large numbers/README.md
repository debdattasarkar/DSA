# Factorials of large numbers

**Difficulty:** Medium
**Accuracy:** 36.57%
**Submissions:** 172K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an integer `n`, find its factorial. Return a **list of integers** denoting the **digits** that make up the factorial of `n`.

---

## Examples

### Example 1

**Input:** `n = 5`
**Output:** `[1, 2, 0]`
**Explanation:** `5! = 1*2*3*4*5 = 120`

### Example 2

**Input:** `n = 10`
**Output:** `[3, 6, 2, 8, 8, 0, 0]`
**Explanation:** `10! = 1*2*3*4*5*6*7*8*9*10 = 3628800`

### Example 3

**Input:** `n = 1`
**Output:** `[1]`
**Explanation:** `1! = 1`

---

## Constraints

* `1 ≤ n ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Morgan Stanley, Microsoft, Samsung, MakeMyTrip, MAQ Software, Adobe, Philips, BrowserStack

---

## Topic Tags

number-theory, Strings, Combinatorial, Data Structures

---

## Related Interview Experiences

* Makemytrip Interview Experience Set 2 Campus

---

## Related Articles

* Cpp Program To Find Factorial Of A Large Number Using Recursion
* Factorial Large Number


---

---

Here’s a tidy, interview-ready pack for **“Factorials of large numbers”** (return the **digits** of `n!` as a list, most-significant digit first).

---

## 2) Explanation + step-by-step dry run

### What’s tricky?

For `n` as large as `1000`, `n!` has **thousands of digits** (≈ `log10(n!)` ≈ `n log10 n − 0.434n + …`). We can’t fit it in fixed-width integer types.
So we simulate **schoolbook multiplication** on a **digit array**:

* Keep the number as digits in **reverse** (least significant digit first) so multiplication/carry flows left→right in the list.
* For each multiplier `x` in `2..n`:

  * For every digit `d` in the array: `prod = d*x + carry`, write back `prod % 10`, update `carry = prod // 10`.
  * When digits end, append remaining carry digits.
* At the end, **reverse** to get most-significant first.

This is the classic GFG approach (expected in interviews).

### Dry run (`n = 5`)

Start: `res = [1]`  (represents 1)

* ×2:

  * 1×2 + 0 = 2 → digit 2, carry 0 → `res = [2]`
* ×3:

  * 2×3 + 0 = 6 → digit 6, carry 0 → `res = [6]`
* ×4:

  * 6×4 + 0 = 24 → digit 4, carry 2 → append carry 2 → `res = [4,2]` (represents 24)
* ×5:

  * 4×5 + 0 = 20 → digit 0, carry 2
  * 2×5 + 2 = 12 → digit 2, carry 1
  * append carry 1 → `res = [0,2,1]` (represents 120)

Reverse → `[1,2,0]`.

---

## 3) Python solutions (several ways)

### (A) Schoolbook digit-array (most expected in interviews)

```python
# User function Template for python3

class Solution:
    def factorial(self, n):
        """
        Build n! as a list of base-10 digits (MSD first).
        Representation: store digits LSB-first while multiplying, then reverse.

        Time:  O(n * D) where D ~ number of digits of n!  (≈ Θ(n log n)).
               For GFG constraints it's often summarized as O(n^2).
        Space: O(D) for the output digits (auxiliary outside result is O(1)).

        Returns: list[int] of digits, most-significant first.
        """
        # res holds digits least-significant-first during computation
        res = [1]  # 0! and 1! = 1

        # multiply res by every x in [2..n]
        for x in range(2, n + 1):
            carry = 0
            for i in range(len(res)):                  # O(current_digits)
                prod = res[i] * x + carry
                res[i] = prod % 10                     # write current digit
                carry = prod // 10                     # propagate carry
            while carry > 0:                            # append remaining carry
                res.append(carry % 10)
                carry //= 10

        res.reverse()  # convert to MSB-first for the return format
        return res
```

### (B) Python big-int (simple, if allowed)

Python integers are arbitrary precision; compute the factorial then convert to digits.

```python
import math

class SolutionBigInt:
    def factorial(self, n):
        """
        Uses Python's big integer to compute n! directly.
        Time:  dominated by big-int multiplication; practically very fast for n<=1000
        Space: O(D) to store the number and digit list.
        """
        val = math.factorial(n)             # big-int factorial
        return list(map(int, str(val)))     # convert to list of decimal digits
```

### (C) Chunked base (faster constant factors)

Use a larger base (e.g., 10^4 or 10^9) to reduce the array length; convert to digits at the end.

```python
class SolutionChunkBase:
    def factorial(self, n):
        """
        Multiply in base B=10^4 to reduce digit array length; convert to decimal digits at end.
        Time:  still O(n * blocks) but with a smaller constant.
        Space: O(blocks), then O(D) when expanding to digits.
        """
        B = 10_000             # each block stores 4 decimal digits
        res = [1]              # blocks LSB-first

        for x in range(2, n + 1):
            carry = 0
            for i in range(len(res)):
                prod = res[i] * x + carry
                res[i] = prod % B
                carry = prod // B
            while carry:
                res.append(carry % B)
                carry //= B

        # Convert block representation to exact decimal digits (MSD-first)
        # Last block has no left-padding; earlier blocks padded to width=4.
        digits = []
        if res:
            # most significant block
            digits.extend(map(int, str(res[-1])))
            # remaining blocks (pad to 4 digits each)
            for b in reversed(res[:-1]):
                digits.extend(map(int, f"{b:04d}"))
        return digits
```

> For interviews, implement **(A)**. Mention **(C)** as an optimization idea and **(B)** if language/library allows big integers.

---

## 4) Interviewer-style Q\&A

**Q1. Why store digits LSB-first during multiplication?**
Because schoolbook multiplication with carry naturally processes from least to most significant digit. Writing back at `res[i]` and moving the carry forward is straightforward.

**Q2. What are the time and space complexities?**
Let `D` be the number of digits of `n!` (≈ `Θ(n log n)`).

* Time ≈ `Σ i=2..n O(current_digits)` ⇒ `O(n * D)`; often summarized as **O(n²)** for this problem’s constraints.
* Space is **O(D)** for the output number. (Auxiliary besides the output is `O(1)`.)

**Q3. Why not use multiplication of strings?**
It’s equivalent in complexity to the digit-array method and more cumbersome in Python. The digit list is clearer.

**Q4. Can we do sub-quadratic multiplication?**
Yes (Karatsuba/FFT/Toom-Cook), but that’s overkill for `n ≤ 1000`. Interviews expect the schoolbook approach.

**Q5. How large is `1000!`?**
Digits ≈ `floor(log10(1000!)) + 1 ≈ 2568`. Our array can easily hold that.

**Q6. Why does chunk base (10^k) help?**
It reduces the number of “digits” (blocks), so inner loops run fewer iterations. You pay a final cost to expand to base-10 digits for output.

**Q7. Any edge cases?**

* `n = 1` or `n = 0` → `[1]`.
* Carry spilling across multiple extra digits (handled by while-carry loop).
* Leading zeros: none, because we never append zero blocks/digits at the MSB unless the result is exactly zero (which factorial isn’t).

---

---

Here’s a **full, runnable Python program** for **Factorials of large numbers** that:

* implements the classic **digit-array (schoolbook) multiplication**,
* prints **inputs and outputs** for sample `n`,
* and **benchmarks** the implementation with `timeit`.

```python
#!/usr/bin/env python3
"""
Factorials of large numbers -> return the digits of n! as a list (MSD first)

Approach used below: schoolbook multiplication on a digit array.
We store digits **LSB-first** while multiplying (natural for carry propagation),
then reverse once at the end for the required MSD-first output.

Big-O summary:
  - Let D = number of decimal digits of n! (≈ Θ(n log n)).
  - Each multiply by x in [2..n] touches every current digit once:
        Time ≈ Σ O(current_digits)  =>  O(n * D)  (often summarized as ~O(n^2) here)
  - Extra space is O(D) for the output number; only O(1) auxiliary beyond that.
"""

from __future__ import annotations
import math
import timeit
from typing import List


# -----------------------------------------------------------------------------
# User function template
# -----------------------------------------------------------------------------
class Solution:
    def factorial(self, n: int) -> List[int]:
        """
        Return the digits of n! as a list (most-significant digit first).

        Steps
          A) Initialize result as [1] (represents 1)              -> O(1) time/space
          B) For each multiplier x in [2..n]:
               - multiply each digit by x with carry              -> O(current_digits)
               - append remaining carry digits                    -> amortized O(1) per carry digit
          C) Reverse digits to MSD-first and return               -> O(D) time, O(1) extra

        Overall:
          Time  : O(n * D)  (D ~ digits in n!)
          Space : O(D)      (for the output number)
        """
        if n <= 1:
            return [1]

        # Store digits LSB-first during computation to make carry natural.
        res = [1]  # represents 1

        # B) Multiply by every x in 2..n
        for x in range(2, n + 1):
            carry = 0
            # multiply current big number by x (digit-wise)
            for i in range(len(res)):               # O(current_digits)
                prod = res[i] * x + carry
                res[i] = prod % 10                  # write new digit (LSB at index 0)
                carry = prod // 10                  # carry forward
            # append any remaining carry as new higher digits
            while carry > 0:
                res.append(carry % 10)
                carry //= 10

        # C) Convert to MSD-first
        res.reverse()
        return res


# ---------- Optional: Python big-int for sanity/contrast ----------
class SolutionBigInt:
    def factorial(self, n: int) -> List[int]:
        """
        Uses Python's arbitrary-precision math.factorial.
        Time/space dominated by big-int operations; fast for n <= 1000.
        """
        val = math.factorial(n)
        return list(map(int, str(val)))


# ----------------------------- Utilities -----------------------------
def digits_to_str(digs: List[int]) -> str:
    """Render a digit list as a contiguous decimal string. O(D) time/space."""
    return ''.join(map(str, digs))


def demo_on_samples() -> None:
    """
    Show outputs for several small inputs (prints input -> output exactly).
    Time here: sum over cases of O(n * D). Space: O(D) per case.
    """
    samples = [1, 5, 10]  # from prompt/examples
    sol = Solution()
    print("=== Sample Runs (n -> digits of n!) ===")
    for n in samples:
        digits = sol.factorial(n)              # O(n * D)
        print(f"n = {n}")
        print(f"Output list: {digits}")
        print(f"As number : {digits_to_str(digits)}")
        print("-" * 60)


def _bench_once(n: int) -> None:
    """
    Helper for timeit: compute digits of n! once.
    This times the full algorithm: O(n * D).
    """
    Solution().factorial(n)


def benchmark() -> None:
    """
    Benchmark with timeit. We use n=1000 (typical upper constraint).
    Prep cost is tiny; the timed region is exactly the factorial computation.
    """
    N = 1000
    runs = 1  # 1000! is heavy enough; 1 run is informative and safe
    total = timeit.timeit(lambda: _bench_once(N), number=runs)

    print("=== Benchmark (Schoolbook digit-array) ===")
    print(f"n       : {N}")
    print(f"runs    : {runs}")
    print(f"total s : {total:.6f}")
    print(f"avg s   : {total / runs:.6f}")
    print("-" * 60)


def main() -> None:
    # 1) Demo on sample inputs with outputs
    demo_on_samples()

    # 2) Benchmark the full algorithm with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Arbitrary-precision math engines**
   Large factorials appear in combinatorics (nCr, permutations), high-precision probability, and analytic computations. Digit-array big-integer arithmetic is the foundation for these systems in languages without built-in big ints.

2. **Cryptography & number theory tooling**
   While raw factorials aren’t used in ciphers, implementing **big-number primitives** (multiply, add, pow) is essential for RSA/EC and contests; the same techniques power those libraries.

3. **Scientific computing / combinatorial counting**
   Computing exact counts for states, permutations, and partitions often requires precise, very large integers (no floating point). Returning digits is a common judge/platform format.

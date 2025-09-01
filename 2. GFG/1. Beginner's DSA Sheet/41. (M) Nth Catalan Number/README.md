# Nth Catalan Number

**Difficulty:** Medium
**Accuracy:** 31.06%
**Submissions:** 138K+
**Points:** 4

---

## Problem Statement

Given a number **n**, the task is to find the **nᵗʰ Catalan number**.

The first few Catalan numbers for `n = 0, 1, 2, 3, ...` are
`1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...`

**Definition:**
Catalan Number for `n` is equal to the number of expressions containing **n pairs of parenthesis** that are correctly matched, i.e., for each of the `n` `'('` there exist `n` `')'` on their right and vice versa.

**Note:** Positions start from `0` as shown above.

---

## Examples

### Example 1

**Input:** `n = 3`
**Output:** `5`
**Explanation:** Possible expressions are:

```
((())), (()()), (())(), ()(()), ()()()
```

(Any ordering is acceptable; there are exactly 5 valid parenthesis strings for 3 pairs.)

### Example 2

**Input:** `n = 4`
**Output:** `14`
**Explanations:** There are total **14** valid combinations which can be formed using 4 parenthesis.

---

## Constraints

* `1 <= n <= 19`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Amazon

---

## Topic Tags

* Dynamic Programming
* Mathematical
* Algorithms

---

## Related Articles

* [Program Nth Catalan Number](https://www.geeksforgeeks.org/program-nth-catalan-number/)

---

---

Here’s an interview-friendly guide to the **nᵗʰ Catalan number**.

---

## 2) Intuition + step-by-step dry run

Catalan numbers satisfy the classic DP recurrence:

* Base: `C0 = 1`, `C1 = 1`
* For `n ≥ 2`:
  `Cn = Σ_{i=0..n-1} (Ci * C(n-1-i))`

This counts, e.g., the number of **valid parenthesis strings** with `n` pairs. Think of splitting by the position of the first matching `)` that closes the first `(`: left side contributes `Ci`, right side contributes `C(n−1−i)`.

They also have a **closed form**:

```
Cn = (1 / (n + 1)) * binom(2n, n)
```

### Dry run (n = 3)

* `C0 = 1`
* `C1 = C0*C0 = 1`
* `C2 = C0*C1 + C1*C0 = 1 + 1 = 2`
* `C3 = C0*C2 + C1*C1 + C2*C0 = 2 + 1 + 2 = 5` ✅

### Dry run (n = 4)

* Already have `C0..C3 = 1, 1, 2, 5`
* `C4 = C0*C3 + C1*C2 + C2*C1 + C3*C0 = 5 + 2 + 2 + 5 = 14` ✅

---

## 3) Python solutions (brute → optimized), interview-style

### A) DP (expected in many interviews) — `O(n^2)` time, `O(n)` space

```python
class Solution:
    def findCatalan(self, n):
        """
        DP recurrence:
          C[0] = 1
          C[k] = sum_{i=0..k-1} C[i] * C[k-1-i]   for k >= 1

        Time:  O(n^2)   (double loop)
        Space: O(n)     (array of C[0..n])
        """
        if n <= 1:
            return 1

        C = [0] * (n + 1)
        C[0] = 1
        C[1] = 1

        for k in range(2, n + 1):            # O(n)
            s = 0
            for i in range(k):               # sum k terms -> O(k)
                s += C[i] * C[k - 1 - i]
            C[k] = s
        return C[n]
```

### B) Closed-form via binomial — `O(n)` time, `O(1)` space (uses integer math)

Two flavors:

#### (i) Using `math.comb` (clean & exact)

```python
import math

class Solution:
    def findCatalan(self, n):
        # Cn = comb(2n, n) // (n + 1)
        return math.comb(2 * n, n) // (n + 1)
```

#### (ii) Multiplicative product (no factorials; good to show you know the trick)

```python
class Solution:
    def findCatalan(self, n):
        """
        Build binom(2n, n) multiplicatively:
          binom(2n, n) = Π_{k=1..n} (n + k) / k
        Then divide by (n+1).
        Time:  O(n), Space: O(1)
        """
        if n == 0:
            return 1
        c = 1
        for k in range(1, n + 1):
            c = c * (n + k) // k     # exact division each step in integers
        return c // (n + 1)
```

### C) Recursive + memoization (educational) — `O(n^2)` time

```python
from functools import lru_cache

class Solution:
    def findCatalan(self, n):
        @lru_cache(maxsize=None)
        def C(k):
            if k <= 1:
                return 1
            return sum(C(i) * C(k - 1 - i) for i in range(k))
        return C(n)
```

> Avoid **naïve recursion without memoization** (`O(2^n)`); mention it only to contrast why DP/memoization are required.

**What to present?**

* Lead with the **DP** method (fits the “Expected Complexity: `O(n^2)`/`O(n)`”).
* If the platform allows, mention the **binomial** approach for an `O(n)` one-liner.

---

## 4) Likely interviewer Q\&A

**Q1. Why does the DP recurrence make sense?**
We partition by the pair that closes the first `(`. The inside contributes `Ci`, the remainder contributes `C(n−1−i)`. Summing over all `i` covers all valid splits exactly once.

**Q2. Complexity of the DP approach?**
Two nested loops → `O(n^2)` time; storing `C[0..n]` → `O(n)` space.

**Q3. When to use the closed form?**
If exact integers are fine (Python big ints) and **no modulo**, `Cn = comb(2n, n) // (n+1)` is the fastest and simplest. Under **modulo arithmetic**, use DP or use factorials with modular inverses (typically when `mod` is prime, e.g., `1e9+7`).

**Q4. Common combinatorial interpretations of Catalan numbers?**

* Valid parentheses strings of `n` pairs
* Number of **BSTs** with `n` distinct keys
* Ways to triangulate a convex `(n+2)`-gon
* Dyck paths of length `2n`
* Non-crossing handshakes of `n` pairs around a circle

**Q5. Any pitfalls?**

* Off-by-one in the convolution (`i` vs `n−1−i`)
* Overflow in languages without big ints (not a Python issue); prefer multiplicative or modular arithmetic there
* Mixing the “index starts at 0” notion: `C0 = 1` corresponds to **zero** pairs of parentheses

**Q6. Which approach would you choose given `1 ≤ n ≤ 19`?**
Either DP `O(n^2)` or the closed form—both are instantaneous for `n ≤ 19`. In competitive programming with a modulus, prefer DP or factorial+inverse.

---

---

I’ve run a complete, inline Python program that:

* Implements `findCatalan(n)` using the **DP O(n²)** method (matches the expected complexity).
* Also includes two **optimized O(n)** variants (binomial and multiplicative).
* Prints **inputs and outputs** for `n = 3, 4, 10` and shows per-method timings.
* Prints the **TOTAL MAIN RUNTIME** using `timeit.default_timer()`.

```python

# Nth Catalan Number — full inline Python program with complexity notes and timing
from functools import lru_cache
import math, timeit

# ----------------------- User Function Template -----------------------
class Solution:
    def findCatalan(self, n: int) -> int:
        """
        DP recurrence (convolution) for Catalan numbers:
          C[0] = 1
          C[k] = sum_{i=0..k-1} C[i] * C[k-1-i] for k >= 1

        Complexity by step:
          - Building C array of length n+1: O(n) memory
          - For each k, the inner sum has k terms: total work sum_{k=1..n} k = O(n^2)
        Overall:
          Time  = O(n^2)
          Space = O(n)
        """
        if n <= 1:
            return 1
        C = [0] * (n + 1)      # O(n) space
        C[0] = 1
        C[1] = 1
        for k in range(2, n + 1):           # O(n)
            s = 0
            for i in range(k):              # O(k) per k
                s += C[i] * C[k - 1 - i]
            C[k] = s
        return C[n]

    # --- Alternative 1: closed form via binomial coefficient ---
    def findCatalan_binom(self, n: int) -> int:
        """
        Cn = comb(2n, n) // (n + 1)
        Using Python's big integers and exact binomial.
        Time  = O(n) (comb uses efficient algorithm)
        Space = O(1) auxiliary
        """
        return math.comb(2 * n, n) // (n + 1)

    # --- Alternative 2: multiplicative product for binomial (no factorials) ---
    def findCatalan_mult(self, n: int) -> int:
        """
        Compute comb(2n, n) multiplicatively:
          comb(2n, n) = Π_{k=1..n} (n + k) / k
        Then divide by (n + 1).
        Time  = O(n)
        Space = O(1)
        """
        if n == 0:
            return 1
        c = 1
        for k in range(1, n + 1):
            c = c * (n + k) // k
        return c // (n + 1)


# ------------------------------ Demo / Main ------------------------------
def main():
    sol = Solution()
    print("=== Catalan Number — Demo & Timing ===\n")

    tests = [3, 4, 10]  # includes prompt examples and one larger value
    for n in tests:
        # Time each method once; overhead is small for these n
        t0 = timeit.default_timer()
        dp_val = sol.findCatalan(n)             # O(n^2)
        t1 = timeit.default_timer()
        bin_val = sol.findCatalan_binom(n)      # O(n)
        t2 = timeit.default_timer()
        mul_val = sol.findCatalan_mult(n)       # O(n)
        t3 = timeit.default_timer()

        # Print inputs and outputs
        print(f"Input: n = {n}")
        print("  DP (O(n^2))        ->", dp_val, f"(time {(t1 - t0):.6f}s)")
        print("  Binomial (O(n))    ->", bin_val, f"(time {(t2 - t1):.6f}s)")
        print("  Multiplicative (O(n)) ->", mul_val, f"(time {(t3 - t2):.6f}s)")
        print()

if __name__ == "__main__":
    # Time the *entire* main program run (I/O + computations + prints)
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-value)

* **Counting valid parenthesizations / parsing**: number of ways to insert parentheses in expressions (e.g., `n` binary operations) or the number of parse trees in ambiguous grammars (e.g., Dyck language).
* **Binary Search Trees**: number of distinct BSTs that can be formed with `n` distinct keys is `Cₙ`.
* **Triangulations**: number of ways to triangulate a convex polygon with `n+2` vertices equals `Cₙ`.
* **Non-crossing structures**: non-crossing handshakes among `n` pairs around a circle; non-crossing matchings, stack-sortable permutations.
* **Lattice/Dyck paths**: monotone paths along a grid that do not cross a diagonal (Catalan counts Dyck paths of semilength `n`).

Here’s the full problem converted into a clean README-style statement, with nothing omitted.

---

# **All Subsets Xor Sum**

**Difficulty:** Medium
**Accuracy:** 66.8%
**Submissions:** 7K+
**Points:** 4

---

## **Problem Statement**

Given an array `arr[]`, return the **sum of the XOR of all elements** for every possible **subset** of the array.
Subsets with the same elements should be counted multiple times.

An array `a` is a subset of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

> **Note:** The answer is guaranteed to fit within a **32-bit integer**.

---

## **Examples**

---

### **Example 1**

**Input:**

```text
arr[] = [7, 2]
```

**Output:**

```text
14
```

**Explanation:**
Subsets are:

```text
[], [7], [2], [7, 2]
```

Sum of all XOR’s:

```text
= 7 + 2 + (7 ^ 2)
= 14
```

---

### **Example 2**

**Input:**

```text
arr[] = [1, 2, 3]
```

**Output:**

```text
12
```

**Explanation:**
Subsets are:

```text
[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
```

Sum of all XOR’s:

```text
= 1 + 2 + 3 + (1 ^ 2) + (1 ^ 3) + (2 ^ 3) + (1 ^ 2 ^ 3)
= 12
```

---

## **Constraints**

* `1 ≤ arr.size() ≤ 30`
* `1 ≤ arr[i] ≤ 10^3`

---

## **Expected Complexities**

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## **Company Tags**

* Adobe
* Amazon
* Apple
* Google

---

## **Topic Tags**

* Bit Magic
* Data Structures
* Algorithms

---

## **Related Articles**

* [*Sum Xor Possible Subsets*](https://www.geeksforgeeks.org/sum-xor-possible-subsets/)

---

---

Let’s crack this one cleanly and make it interview-proof 😊

---

## 2. Intuition + Step-by-Step Explanation

### Problem recap

Given `arr`, we must:

1. Consider **all subsets** of `arr` (including empty subset).
2. Compute XOR of each subset.
3. Return the **sum** of all those XOR values.

Example: `arr = [1, 2, 3]` → answer = 12.

---

### Brute-force thinking (exhaust all subsets)

For `n` elements, there are `2^n` subsets.

For `arr = [1, 2, 3]`, subsets and XORs:

1. `[]` → XOR = 0  (often they don’t show it, but it exists)
2. `[1]` → 1
3. `[2]` → 2
4. `[3]` → 3
5. `[1, 2]` → `1 ^ 2 = 3`
6. `[1, 3]` → `1 ^ 3 = 2`
7. `[2, 3]` → `2 ^ 3 = 1`
8. `[1, 2, 3]` → `1 ^ 2 ^ 3 = 0`

Sum of XORs:
`0 + 1 + 2 + 3 + 3 + 2 + 1 + 0 = 12`.

Brute-force is fine conceptually, but `2^n` grows fast. With `n ≤ 30`, `2^n ≈ 1e9` → too big in Python for tight constraints, so we want an O(n) trick.

---

### Bitwise pattern trick (the O(n) solution)

We use the fact that **XOR is bitwise and linear over bits**.

Idea:

1. Look at each **bit position** independently (0th bit, 1st bit, etc).
2. For each bit position `b`:

   * Suppose **at least one array element** has this bit = 1.
   * Then in the sum of all subset XORs, that bit contributes a fixed value.

Key fact:

> Each element’s bits appear in **exactly half** of the subset XORs.

Why?

* For every subset, there is a unique corresponding subset where you flip “include / don’t include” a particular element.
* So among all `2^n` subsets:

  * For a fixed element, it is **present** in `2^(n-1)` subsets and **absent** in `2^(n-1)` subsets.
* For a given bit:

  * If the bit is set in **at least one element**, then across all subsets, **half of the XOR results** for that bit are 1 and half are 0.

Important observation (proven / well-known result):

> The XOR of all subset XORs equals:
> [
> (\text{bitwise OR of all elements}) \times 2^{n-1}
> ]

Reasoning:

* For each bit `b`:

  * If no element has bit `b` set, that bit contributes nothing to any XOR → contribution 0.
  * If **some element** has bit `b` set:

    * Across all subset XORs, bit `b` is 1 in exactly `2^{n-1}` of them.
    * So total contribution of this bit to the sum is:
      [
      2^{n-1} \times (1 << b)
      ]
* The OR of all elements tells us exactly which bits have **at least one 1**.
* Multiply that OR by `2^{n-1}`, we effectively sum contributions for all set bits.

So:

```python
subset_xor_sum = (arr[0] | arr[1] | ... | arr[n-1]) * (1 << (n-1))
```

---

### Dry Run with `arr = [1, 2, 3]`

Binary:

```text
1 = 001
2 = 010
3 = 011
OR = 011 (which is 3)
n = 3 → 2^(n-1) = 2^2 = 4
Answer = OR * 4 = 3 * 4 = 12
```

Matches the brute-force result.

---

### Dry Run with `arr = [7, 2]`

Binary:

```text
7 = 111
2 = 010
OR = 111 (7)
n = 2 → 2^(2-1) = 2
Answer = 7 * 2 = 14
```

Matches the example.

---

## 3. Python Codes (Brute & Optimized) in Your Format

### 3.1 Brute-force (backtracking) – for understanding

```python
class SolutionBrute:
    def subsetXORSum(self, arr):
        """
        Brute-force: generate all subsets with backtracking,
        compute XOR for each, and sum them.

        Time Complexity:
            O(2^n * n) in the simplest form (if we recompute XOR per subset).
            With running XOR (as below), each subset is O(1) → O(2^n).
        Space Complexity:
            O(n) recursion depth, plus O(1) extra.
        """
        n = len(arr)
        total_sum = 0

        def backtrack(index, current_xor):
            nonlocal total_sum

            if index == n:
                # Reached end; count this subset's XOR
                total_sum += current_xor
                return

            # Choice 1: exclude arr[index]
            backtrack(index + 1, current_xor)

            # Choice 2: include arr[index]
            backtrack(index + 1, current_xor ^ arr[index])

        backtrack(0, 0)
        return total_sum
```

This is nice to explain, but too slow for large n. Now the optimized one.

---

### 3.2 Optimized O(n) solution (using OR * 2^(n-1))

```python
class Solution:
    def subsetXORSum(self, arr):
        """
        Optimized solution using bitwise properties.

        Idea:
        -----
        - For each bit position, consider whether at least one element has that bit set.
        - If no element has the bit, it never appears in any subset XOR contribution.
        - If at least one element has the bit set:
              -> This bit appears as '1' in exactly 2^(n-1) subset XORs.
        - So the total sum over all subsets equals:
              (bitwise OR of all elements) * 2^(n-1)

        Implementation Steps:
        ---------------------
        1) Compute bitwise OR of all values in arr.
        2) Compute factor = 1 << (n - 1).
        3) Return OR_value * factor.

        Time Complexity:
            O(n)  - single pass to compute OR.
        Space Complexity:
            O(1)  - just a few integer variables.
        """
        n = len(arr)

        # Step 1: Compute OR of all elements
        or_all = 0
        for value in arr:        # O(n)
            or_all |= value      # O(1) per step

        # Step 2: Each set bit contributes in exactly 2^(n-1) subsets
        factor = 1 << (n - 1)    # 2^(n-1)

        # Step 3: Final answer
        return or_all * factor
```

This is the version you should present as the **main solution**.

---

## 4. Interview Memory Tricks + Q&A

### Quick memory hook (10 seconds)

> **“Sum of XORs of all subsets = OR of all elements × 2^(n−1)”**

Super short formula:

```text
answer = (a0 | a1 | ... | an-1) << (n - 1)
```

---

### One-line mental explanation

> “Each bit that appears in at least one element contributes in half of all subsets; bits that never appear contribute nothing.”

---

### Likely Interview Questions & Solid Answers

---

**Q1. How did you get from 2^n subsets to an O(n) solution?**

> Instead of enumerating subsets, I reasoned bitwise.
> XOR is bitwise and each bit position behaves independently.
> For a given bit, I only care if it appears in any element at that position.
> If it doesn’t appear in any element, it never contributes.
> If it does appear, then across all subsets that bit is 1 in exactly half of the subset XORs.
> That gives a closed-form sum equal to OR-of-all-elements times 2^(n-1).

---

**Q2. Why exactly 2^(n−1) subsets for each bit?**

> For any fixed element (or bit), for each subset where it is included, there is a partner subset where it’s excluded (just flip that choice).
> Total subsets = 2^n; each element is included in exactly half → 2^(n-1) subsets.
> For a bit that’s set in any element, you can reason similarly: the number of subset XORs where that bit ends up 1 is 2^(n-1).

---

**Q3. What is the time and space complexity of your optimized solution?**

> * Time: O(n). I scan the array once to compute the OR. Computing 2^(n−1) is O(1) via bit shift.
> * Space: O(1). Only a few integer variables; no extra arrays or recursion.

---

**Q4. Can you describe the brute-force approach and why it’s not ideal?**

> Brute force uses backtracking or bitmask enumeration to generate all 2^n subsets, compute XOR for each, and sum them.
> Even with an efficient running XOR, we do O(2^n) subset generations.
> For n up to 30, 2^30 ≈ 1e9, which is too large for tight time limits, especially in Python.
> That’s why we need the bitwise formula.

---

**Q5. Is this trick specific to XOR or can it generalize?**

> The trick heavily relies on XOR properties:
>
> * It’s bitwise and symmetric.
> * It behaves linearly: each bit is independent and we can count contributions per bit.
>   For sum or product, such a clean “OR × 2^(n−1)” formula doesn’t hold.
>   So this is specific to XOR and other linear-like bitwise operations.

---

---

Awesome, let’s finish this problem properly.

---

## 5. Real-World Use Cases (easy to talk about in interviews)

Remember: this function computes the **sum of XORs of all subsets** of an array.

### a) Feature-Flag / Configuration Exploration

* Imagine each element is a **bitmask of enabled features** (e.g., A/B testing flags).
* Every subset of these masks represents a **possible configuration**.
* The XOR of a subset tells you the **combined effect** of those toggles.
* Summing all subset XORs gives a single aggregated measure of how “volatile” or “diverse” the feature combinations are.
* In interviews, you can say:
  *“If each bit represents a feature, OR×2^(n−1) gives a compact summary of how often each feature toggles across all configurations.”*

---

### b) Security / Key-Material Diagnostics

* Each array element is a **key fragment** or **round key** (bitmask).
* All subsets correspond to all combinations of fragments.
* XOR is widely used in stream ciphers and one-time pads.
* Sum of all subset XORs can be used as a **sanity check** / diagnostic metric:

  * If some bits are never set in any fragment (OR is 0 there), they **never contribute** → suspicious / low entropy.
* Easy interview line:
  *“We can quickly check which key bits ever participate in any subset combination via OR, then scale by 2^(n−1).”*

---

### c) Combinational Hardware Test Patterns

* Bits represent **signals/wires**; each array element is a pattern vector.
* Subsets of patterns correspond to combining different test vectors.
* XOR over patterns is common for parity / error detection.
* Sum of all subset XORs tells how each signal line behaves across all combined tests — which lines flip often vs never.

---

## 6. Full Python Program (Optimized) with Timing & Complexity Comments

This is a complete, ready-to-run script:

```python
"""
All Subsets XOR Sum - Full Program

We need:
    sum_{S subset of arr} XOR(S)

Key bit-trick:
---------------
XOR is bitwise. Consider each bit position independently.

For a given bit b:
    - If no element has bit b set -> it never appears in any subset XOR.
    - If at least one element has bit b set:
         bit b ends up as 1 in exactly 2^(n-1) subset XORs.

Why 2^(n-1)?
    Each element (and each bit inside it) is included in exactly half
    of the 2^n subsets (because for every subset without that element,
    there's a twin subset with it).

Therefore:
    Let OR_all = a0 | a1 | ... | a_(n-1)
    For each set bit b in OR_all:
        contribution = (1 << b) * 2^(n-1)
    So total sum is:
        OR_all * 2^(n-1)

Final formula:
    answer = (a0 | a1 | ... | an-1) << (n - 1)

Complexities:
-------------
Time  : O(n)   (single pass to compute OR_all)
Space : O(1)   (few integer variables)
"""

from timeit import default_timer as timer
from typing import List


class Solution:
    def subsetXORSum(self, arr: List[int]) -> int:
        """
        Optimized computation of sum of XORs of all subsets.

        Parameters
        ----------
        arr : List[int]
            Input array of integers.

        Returns
        -------
        int
            Sum of XOR values of all possible subsets of arr.

        Time Complexity:
            - One pass over array to compute OR_all: O(n)
            - Constant-time arithmetic for shift and multiply.
            => Overall: O(n)
        Space Complexity:
            - O(1) extra space (only OR_all, factor, and loop vars).
        """
        n = len(arr)

        # Step 1: compute bitwise OR of all elements
        # Time: O(n), Space: O(1)
        or_all = 0
        for value in arr:
            or_all |= value  # OR accumulates bits that appear in any element

        # Step 2: each set bit appears in exactly 2^(n-1) subset XORs
        # We compute 2^(n-1) as a left shift: 1 << (n - 1)
        factor = 1 << (n - 1)  # O(1) time, O(1) space

        # Step 3: final answer = OR_all * factor
        # Multiplication is O(1) for 32-bit guaranteed result.
        return or_all * factor


# ----------------------------------------------------------------------
# Example usage + timing
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Example 1 from the statement
    arr1 = [7, 2]      # Expected answer: 14

    # Example 2 from the statement
    arr2 = [1, 2, 3]   # Expected answer: 12

    solver = Solution()

    # Measure execution time for a couple of calls
    start_time = timer()

    result1 = solver.subsetXORSum(arr1)
    result2 = solver.subsetXORSum(arr2)

    end_time = timer()
    elapsed = end_time - start_time

    print("Input arr1:", arr1)
    print("All subsets XOR sum for arr1:", result1)
    print()
    print("Input arr2:", arr2)
    print("All subsets XOR sum for arr2:", result2)
    print()
    print("Total execution time for both calls (seconds):", elapsed)
```

Typical output (numbers may differ slightly in timing):

```text
Input arr1: [7, 2]
All subsets XOR sum for arr1: 14

Input arr2: [1, 2, 3]
All subsets XOR sum for arr2: 12

Total execution time for both calls (seconds): 1.8e-05
```

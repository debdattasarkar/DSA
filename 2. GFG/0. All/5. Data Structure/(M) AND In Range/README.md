
---

# **AND In Range**

**Difficulty:** Medium
**Accuracy:** 37.46%
**Submissions:** 6K+
**Points:** 4

---

## **Problem Statement**

You are given two integers **l** and **r**.
Find the result after applying the series of **Bitwise AND (&)** operation on **every natural number between the range l to r** (including both).

---

## **Examples**

---

### **Example 1**

**Input:**

```
l = 8, r = 13
```

**Output:**

```
8
```

**Explanation:**

```
8 AND 9 AND 10 AND 11 AND 12 AND 13 = 8
```

---

### **Example 2**

**Input:**

```
l = 2, r = 3
```

**Output:**

```
2
```

**Explanation:**

```
2 AND 3 = 2
```

---

## **Constraints**

```
1 ≤ l ≤ r ≤ 10^9
```

---

## **Expected Complexities**

* **Time Complexity:** `O(log l)`
* **Auxiliary Space:** `O(1)`

---

## **Topic Tags**

* Bit Magic
* Data Structures

---

## **Related Articles**

* [*Bitwise AND Or Of A Range*](https://www.geeksforgeeks.org/bitwise-and-or-of-a-range/)

---

---

I’ll go in order: explanation + dry run → brute & optimized Python → interview memory + Q&A.

---

## 2. Intuition + Step-by-Step Explanation

### Problem restatement

Compute:

```text
l & (l+1) & (l+2) & ... & r
```

for `1 ≤ l ≤ r ≤ 10^9`.

Brute force is too slow if `(r - l)` is huge, so we need a bit trick.

---

### Bitwise AND over a range – key idea

Look at **binary**.

Example 1: `l = 8`, `r = 13`

```text
8  = 01000
9  = 01001
10 = 01010
11 = 01011
12 = 01100
13 = 01101
```

If we AND all these:

* Any bit position that becomes **0 in any number** from l..r will be **0 in the final answer**.
* Only bits that are the **same (and 1)** in *every* number survive.

Notice:

* The leftmost 3 bits: `01`…? change?

  * From 01000 to 01101 we cross from `010xx` to `011xx` → some numbers have that bit 0, others 1 → final bit becomes 0.
* The only stable part is the **common prefix** of `l` and `r`.

**Core fact:**

> Bitwise AND over all integers in `[l, r]` is equal to the **common binary prefix** of `l` and `r`, with the rest of the bits set to 0.

So we just need to extract the common prefix.

---

### How to get common prefix efficiently

Method: **shift both numbers right until they become equal.**

1. Initialize `shift = 0`.
2. While `l < r`:

   * `l >>= 1`
   * `r >>= 1`
   * `shift += 1`
3. Now `l == r` and equals the **common prefix**.
4. Answer is `l << shift` (put zeroes back in the trimmed bits).

Time complexity: `O(log(max(l, r)))` because we shift at most number-of-bits times.

---

### Dry run 1 – Example: `l = 8, r = 13`

Binary:

```text
l = 01000
r = 01101
```

Start: `shift = 0`

* Iteration 1:

  * `l < r` → yes
  * `l >>= 1` → `00100` (4)
  * `r >>= 1` → `00110` (6)
  * `shift = 1`

* Iteration 2:

  * `l = 4`, `r = 6`, `l < r`
  * `l >>= 1` → `00010` (2)
  * `r >>= 1` → `00011` (3)
  * `shift = 2`

* Iteration 3:

  * `l = 2`, `r = 3`, `l < r`
  * `l >>= 1` → `00001` (1)
  * `r >>= 1` → `00001` (1)
  * `shift = 3`

* Now `l == r == 1`, stop.

Common prefix in shifted form: `1 (binary)`

Restore by left shifting back:

```text
answer = 1 << 3 = 8 (1000₂)
```

Matches the example: `8 & 9 & 10 & 11 & 12 & 13 = 8`.

---

### Dry run 2 – Example: `l = 2, r = 3`

Binary:

```text
l = 10
r = 11
```

`shift = 0`

* Iteration 1:

  * `l < r`
  * `l >>= 1` → `1`
  * `r >>= 1` → `1`
  * `shift = 1`

Now `l == r == 1`.

Answer = `1 << 1 = 2` → `2 & 3 = 2`.

---

## 3. Python Solutions

### 3.1 Brute Force (for understanding, not for constraints)

```python
class SolutionBrute:
    def andInRange(self, l: int, r: int) -> int:
        """
        Brute-force: compute l & (l+1) & ... & r directly.

        Time  : O(r - l + 1)  -> too slow if range is big (up to 1e9).
        Space : O(1)
        """
        result = l
        for x in range(l + 1, r + 1):
            result &= x
        return result
```

Good to understand the operation but unusable for large ranges.

---

### 3.2 Optimized (common-prefix / shift method) – what interviewers expect

```python
class Solution:
    def andInRange(self, l: int, r: int) -> int:
        """
        Compute bitwise AND of all integers from l to r inclusive.

        Core idea:
        ----------
        - Over a continuous range, bits that flip (0→1 or 1→0) at any point
          become 0 in the final AND.
        - The only bits that survive are the leading bits where l and r
          have the SAME value (the common prefix).
        - We repeatedly right-shift l and r until they are equal, counting
          how many times we shifted. This removes the non-common suffix.
        - When l == r, that value is exactly the common prefix.
        - Shift it back left by 'shift' places (filling with zeroes) to get
          the final AND result.

        Time Complexity:
            O(log(max(l, r)))  -- we shift at most the bit-length times.
        Space Complexity:
            O(1)  -- just a few integer variables.
        """
        shift = 0

        # Keep trimming least-significant bits until l and r converge.
        # Each step:
        #   l >>= 1, r >>= 1  -> O(1)
        # Loop runs at most ~30 times for l,r <= 1e9.
        while l < r:
            l >>= 1
            r >>= 1
            shift += 1

        # l (or r) now holds the common prefix; restore zeros on the right.
        return l << shift
```

This is the clean, easy-to-remember solution.

---

## 4. Interview Memory + Q&A

### Quick mental template (10 seconds)

> “Answer is the **common prefix** of l and r in binary.
> Keep right-shifting l and r until they become equal, count shifts,
> then left-shift back. That’s the range AND.”

That’s literally your 3-line mental algorithm.

---

### 5-line pseudo-code you can recreate fast

```text
shift = 0
while l < r:
    l = l >> 1
    r = r >> 1
    shift += 1
return l << shift
```

---

### Likely interview questions & good answers

---

**Q1. Why does bitwise AND over a range equal the common prefix of l and r?**

> Because whenever any bit position changes from 0 to 1 or 1 to 0 within the range `[l, r]`, there exists at least one number in the range with that bit 0.
> In an AND across all numbers, that bit becomes 0.
> The only bits that can stay 1 are those which never change across the entire range, i.e., the common leading bits of l and r.
> That prefix is exactly what we get after repeatedly shifting l and r right until they match.

---

**Q2. Why do we stop when `l == r` in the loop?**

> At that point, we’ve shifted away all differing lower bits.
> The remaining value is the longest common prefix of l and r in binary.
> Any bits below that prefix must be 0 in the final result, so we just left-shift to reattach zeroes.

---

**Q3. What’s the time and space complexity?**

> Each loop iteration right-shifts both numbers by one bit.
> Since l and r are at most 10⁹, they have at most 30 bits, so the loop runs at most ~30 times.
> Time complexity is `O(log(max(l, r)))`.
> Space is `O(1)` because we use a constant number of integer variables.

---

**Q4. Could you describe a brute-force approach and its complexity?**

> Brute force would compute `ans = l & (l+1) & … & r` directly in a loop.
> That takes O(r−l+1) time, which can be up to 10⁹ operations for worst-case inputs, so it’s too slow.
> The bit-prefix trick reduces that to about 30 operations regardless of the gap.

---

**Q5. Is there an alternative way to think about this, without shifting both?**

> Yes. Another common pattern is:
>
> ```
> while l < r:
>     r = r & (r - 1)    # clear least significant set bit of r
> ```
>
> This progressively removes bits from r until it falls into the same prefix as l.
> The idea is similar: we zero differing lower bits until the range no longer covers both 0 and 1 in any position.

---

---

Nice, this is a great one to talk about in interviews 👍

---

## 5. Real-World Use Cases (easy to explain)

Think of **bitwise AND over a consecutive ID / address range**. It essentially keeps only the **common prefix bits** across that range.

### a) Network / IP Address Range Mask

* Suppose IP addresses are represented as integers.
* You have a **range of IPs from l to r** and want to know the **largest shared network mask** for them.
* Bitwise AND of all addresses in the range gives you the **common prefix**—exactly the part that can be treated as the “fixed” network part.
* This is conceptually similar to how routers reason about **common prefixes in CIDR blocks**.

---

### b) File-System or Memory Alignment

* Block IDs or memory addresses are consecutive integers.
* When you AND an entire range:

  * All bits that differ anywhere in the range go to 0.
  * You’re left with the highest-order bits that are common to every block.
* This can represent the **largest aligned base address** that still covers the whole range—useful for allocating or locking a region with consistent alignment constraints.

---

### c) Permission / Feature Flags Over a Range of Users

* Each ID in `[l, r]` represents a **user** or **object**, and its integer value encodes bit flags.
* `AND` over the range gives you the set of **flags that are enabled for *all* users/objects** in that ID range.
* This tells you the **intersection of capabilities** across that segment.

These stories are simple enough to say in 20 seconds and show you understand the “common prefix” idea.

---

## 6. Full Python Program with Timing & Complexity Comments

This script:

* Uses the **common-prefix / right-shift** trick (O(log n)).
* Follows your required `class Solution` format.
* Includes:

  * Example inputs,
  * Output printing,
  * `timeit` timing for the whole function call.

```python
"""
AND In Range - Full Program

We need to compute:
    l & (l+1) & (l+2) & ... & r

Key observation:
----------------
Bits that differ anywhere in [l, r] will become 0 in the final AND.
Only the leading bits that are the SAME for every number in the range
(the common binary prefix of l and r) survive.

Algorithm:
----------
1. Repeatedly right-shift l and r until they become equal.
   - Each shift removes one least-significant bit.
   - When l == r, we've stripped off all differing suffix bits.
   - The remaining value is their common prefix.
2. Count how many times we shifted (say 'shift').
3. Left-shift the common prefix back by 'shift' bits to restore position,
   filling zeros in the lower bits.

Complexities:
-------------
- Time:  O(log(max(l, r)))  (bounded by number of bits, ~30 for 1e9)
- Space: O(1)  (only a few integers)
"""

from timeit import default_timer as timer
from typing import List


class Solution:
    def andInRange(self, l: int, r: int) -> int:
        """
        Compute bitwise AND of all integers from l to r inclusive.

        Parameters
        ----------
        l : int
            Left bound of the range.
        r : int
            Right bound of the range (r >= l).

        Returns
        -------
        int
            Result of l & (l+1) & ... & r.

        Time Complexity:
            - The while-loop shifts l and r right until they match.
            - Each iteration is O(1).
            - For 32-bit ints, at most 32 iterations.
            => O(log(max(l, r))).
        Space Complexity:
            - O(1) extra space (just shift counter and variables).
        """
        shift = 0  # number of bits we have shifted off

        # While there exists at least one differing bit, right-shift both.
        # This gradually removes non-common suffix bits.
        while l < r:
            l >>= 1   # O(1) bit shift
            r >>= 1   # O(1) bit shift
            shift += 1

        # Now l == r and equal to the common prefix.
        # Shift back left by 'shift' bits, lower bits become 0.
        return l << shift


# ---------------------------------------------------------------------
# Example usage + timing
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Example 1 from the problem
    l1, r1 = 8, 13   # Expected result: 8

    # Example 2 from the problem
    l2, r2 = 2, 3    # Expected result: 2

    solver = Solution()

    # Measure total time for two calls to andInRange
    start_time = timer()

    result1 = solver.andInRange(l1, r1)
    result2 = solver.andInRange(l2, r2)

    end_time = timer()
    elapsed = end_time - start_time

    print(f"Input: l = {l1}, r = {r1}")
    print("AND in range result:", result1)
    print()
    print(f"Input: l = {l2}, r = {r2}")
    print("AND in range result:", result2)
    print()
    print("Total execution time for both calls (seconds):", elapsed)
```

Typical output when you run this:

```text
Input: l = 8, r = 13
AND in range result: 8

Input: l = 2, r = 3
AND in range result: 2

Total execution time for both calls (seconds): 1.5e-05
```

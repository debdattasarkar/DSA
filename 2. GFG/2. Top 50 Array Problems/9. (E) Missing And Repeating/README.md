# Missing And Repeating

**Difficulty:** Easy
**Accuracy:** 24.83%
**Submissions:** 637K+
**Points:** 2
**Average Time:** 30m

---

## Problem Statement

Given an unsorted array `arr[]` of size `n`, containing elements from the range `1` to `n`, it is known that **one number in this range is missing**, and **another number occurs twice** in the array. Find both the **duplicate** number and the **missing** number.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 2]`
**Output:** `[2, 1]`
**Explanation:** Repeating number is `2` and the missing number is `1`.

### Example 2

**Input:** `arr[] = [1, 3, 3]`
**Output:** `[3, 2]`
**Explanation:** Repeating number is `3` and the missing number is `2`.

### Example 3

**Input:** `arr[] = [4, 3, 6, 2, 1, 1]`
**Output:** `[1, 5]`
**Explanation:** Repeating number is `1` and the missing number is `5`.

---

## Constraints

* `2 ≤ n ≤ 10^6`
* `1 ≤ arr[i] ≤ n`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Arrays
* Mathematical

---

## Related Articles

* [Find A Repeating And A Missing Number](https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/)

---

---

Here’s an interview-ready guide to **Missing and Repeating** (find the value that appears twice and the value that’s missing from `1..n`).

---

## 2) Intuition + step-by-step dry run

### Key facts

* Array of size `n` holds numbers from `1..n`.
* Exactly **one number repeats** (call it `R`) and **one number is missing** (call it `M`).

### Optimized idea (math, O(1) extra)

Let

* `S = 1 + 2 + ... + n = n(n+1)/2`
* `SS = 1² + 2² + ... + n² = n(n+1)(2n+1)/6`
* `s = sum(arr)` and `ss = sum(x*x for x in arr)`

Then:

```
s - S       = R - M          …… (1)
ss - SS     = R² - M²
            = (R - M)(R + M) …… (2)
```

From (1) and (2):

```
R + M = (ss - SS) / (s - S)
R     = ((R + M) + (R - M)) / 2
M     = (R + M) - R
```

All integer arithmetic; no precision issues.

### Dry run

`arr = [4, 3, 6, 2, 1, 1]`, `n = 6`

* `S  = 6*7/2 = 21`
* `SS = 6*7*13/6 = 91`
* `s  = 4+3+6+2+1+1 = 17` → `Δ = s - S = -4 = R - M`
* `ss = 16+9+36+4+1+1 = 67` → `Δ2 = ss - SS = -24 = (R - M)(R + M)`
* `R + M = Δ2 / Δ = (-24)/(-4) = 6`
* `R = ( (R+M) + (R-M) )/2 = (6 + (-4))/2 = 1`
* `M = 6 - 1 = 5`

**Answer:** repeating `1`, missing `5`.

---

## 3) Python solutions (brute & optimized), with interview-style comments

### A) Optimized math (most common in interviews)

```python
class Solution:
    def findTwoElement(self, arr):
        """
        Return [repeating, missing]
        Math approach using sums and sum of squares.
        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)

        # Expected sums for 1..n
        S = n * (n + 1) // 2
        SS = n * (n + 1) * (2 * n + 1) // 6

        # Actual sums from array
        s = 0
        ss = 0
        for x in arr:
            s += x          # O(n)
            ss += x * x

        diff = s - S        # = R - M
        sqdiff = ss - SS    # = (R - M)(R + M)

        # Avoid division by zero theoretically; per problem guarantees diff != 0
        sum_rm = sqdiff // diff   # = R + M

        R = (sum_rm + diff) // 2
        M = sum_rm - R

        return [R, M]
```

### B) XOR partition (also O(n)/O(1); excellent follow-up)

```python
class Solution:
    def findTwoElement(self, arr):
        """
        XOR trick to split into two buckets by rightmost set bit.
        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)

        # xor of all numbers 1..n and array -> xor = R ^ M
        xo = 0
        for x in arr:
            xo ^= x
        for v in range(1, n + 1):
            xo ^= v

        # Rightmost set bit distinguishes R and M
        rsb = xo & -xo

        bucket1 = 0
        bucket2 = 0

        # Partition arr by rsb
        for x in arr:
            if x & rsb:
                bucket1 ^= x
            else:
                bucket2 ^= x
        # Partition 1..n by rsb
        for v in range(1, n + 1):
            if v & rsb:
                bucket1 ^= v
            else:
                bucket2 ^= v

        # bucket1 and bucket2 are R and M in some order.
        # Count to decide which repeats.
        count1 = 0
        for x in arr:
            if x == bucket1:
                count1 += 1

        if count1 == 2:
            return [bucket1, bucket2]   # [R, M]
        else:
            return [bucket2, bucket1]
```

### C) In-place marking (O(n)/O(1), but **modifies array**)

```python
class Solution:
    def findTwoElement(self, arr):
        """
        Use sign marking: visit index |x|-1 and flip sign; if already negative, 'x' is repeating.
        Then the remaining index i with positive value indicates missing = i+1.
        Time:  O(n)
        Space: O(1)
        NOTE: modifies the array (restoration optional).
        """
        n = len(arr)
        repeat = -1
        for x in arr:
            idx = abs(x) - 1
            if arr[idx] < 0:
                repeat = abs(x)       # seen before -> repeating
            else:
                arr[idx] = -arr[idx]  # mark
        miss = -1
        for i in range(n):
            if arr[i] > 0:
                miss = i + 1          # never visited -> missing
                break
        return [repeat, miss]
```

### D) Brute (counting map; simplest to explain)

```python
from collections import Counter

class Solution:
    def findTwoElement(self, arr):
        """
        Count frequencies; missing is value with freq 0; repeating has freq 2.
        Time:  O(n)
        Space: O(n)
        """
        n = len(arr)
        freq = Counter(arr)
        repeat = miss = -1
        for v in range(1, n + 1):
            c = freq.get(v, 0)
            if c == 2:
                repeat = v
            elif c == 0:
                miss = v
        return [repeat, miss]
```

---

## 4) Likely interviewer Q\&A

**Q1. Why does the math approach work?**
Because the array differs from `1..n` only by swapping one number `M` with a duplicate `R`. That shifts the **sum** by `R − M` and the **sum of squares** by `R² − M² = (R − M)(R + M)`. Solving these two equations yields `R` and `M`.

**Q2. Any risk of overflow?**
In some languages yes; use 64-bit integers. In Python ints are arbitrary-precision, so you’re safe.

**Q3. When would you prefer XOR over the sum method?**
XOR is also O(1) space and avoids big integer arithmetic in languages where overflow is risky. It’s a great alternative and a nice way to show bit-manipulation skills.

**Q4. Does the in-place marking method alter the array?**
Yes—it flips signs. That’s O(1) space and very fast, but it **mutates input**. If mutation isn’t allowed, prefer math/XOR.

**Q5. Can there be cases where `s − S = 0`?**
Not under the given guarantees (exactly one missing and one duplicate). If `s − S = 0`, it would imply `R = M`, which is impossible.

**Q6. Complexity of each method?**

* **Math**: O(n) time, O(1) space.
* **XOR**: O(n) time, O(1) space.
* **Marking**: O(n) time, O(1) space, but mutates array.
* **Counter**: O(n) time, O(n) space.

**Q7. What if input might be invalid (e.g., values outside 1..n or multiple repeats)?**
Problem constraints rule that out. If needed, add validation or fall back to counting and verify exactly one `freq==2` and one `freq==0`.

---

### Ready-to-submit (math) in the requested format

```python
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        S = n * (n + 1) // 2
        SS = n * (n + 1) * (2 * n + 1) // 6
        s = 0
        ss = 0
        for x in arr:
            s += x
            ss += x * x
        diff = s - S                    # R - M
        sum_rm = (ss - SS) // max(diff, 1 if diff == 0 else diff)  # safe div; diff!=0 per constraints
        R = (sum_rm + diff) // 2
        M = sum_rm - R
        return [R, M]
```

---

---

Done — I executed a **complete inline Python program** that:

* Implements four approaches: **Math (default), XOR, In-place marking, Counting**.
* Prints outputs for the given examples, an edge case, and a **large benchmark (n=200,000)** with `timeit` timings.
* Shows that Math and XOR both recover the correct `[repeating, missing]` and gives you a sense of performance.

You can copy the code from the output cell to run locally.

---

## 6) Real-World Use Cases (why this pattern matters)

* **Data integrity checks:** Detect a duplicated record ID and identify the missing ID when a batch ingest should contain a consecutive range.
* **Ticketing/Invoice systems:** When exactly one invoice got double-inserted and another is missing, quickly pinpoint both IDs.
* **Manufacturing/Logistics:** In serialized tracking (1..n), find which serial was printed twice and which label never got printed.
* **Assessment systems:** In exam seating or roll numbers, locate a repeated seat/roll and the absent one to fix allocations.
* **Telemetry counters:** When a run should emit counters 1..n exactly once, identify the duplicated/missing emission for debugging.


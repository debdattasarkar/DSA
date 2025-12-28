# K-th element of two Arrays

**Difficulty:** Medium
**Accuracy:** 37.4%
**Submissions:** 382K+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

Given **two sorted arrays** `a[]` and `b[]` and an integer **k**, the task is to **find the element that would be at the k-th position** in the **combined sorted array** formed by merging `a[]` and `b[]`.

> The arrays are already sorted individually, but **you must not actually merge them** to solve the problem efficiently.

---

## Examples

### Example 1

**Input:**

```
a[] = [2, 3, 6, 7, 9]
b[] = [1, 4, 8, 10]
k = 5
```

**Output:**

```
6
```

**Explanation:**
The combined sorted array would be:

```
[1, 2, 3, 4, 6, 7, 8, 9, 10]
```

The **5th element** in this array is **6**.

---

### Example 2

**Input:**

```
a[] = [1, 4, 8, 10, 12]
b[] = [5, 7, 11, 15, 17]
k = 6
```

**Output:**

```
10
```

**Explanation:**
The combined sorted array would be:

```
[1, 4, 5, 7, 8, 10, 11, 12, 15, 17]
```

The **6th element** in this array is **10**.

---

## Constraints

* 1 ≤ `a.size()`, `b.size()` ≤ 10<sup>6</sup>
* 1 ≤ `k` ≤ `a.size() + b.size()`
* 0 ≤ `a[i]`, `b[i]` ≤ 10<sup>8</sup>

---

## Expected Complexities

* **Time Complexity:** `O(log(min(a, b)))`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Flipkart
* Microsoft

---

## Topic Tags

* Arrays
* Divide and Conquer
* Data Structures
* Algorithms
* Binary Search

---

## Related Interview Experiences

* Flipkart Interview Experience Set 26

---

## Related Articles

* **K Th Element Two Sorted Arrays**

---

---

## 2) Explanation (what’s the trick?)

If we literally merge two sorted arrays, we can get the k-th element easily, but merge costs **O(n+m)** which is too slow for `10^6`.

Instead, use the **partition idea**:

Pick `cutA` elements from `a` and `cutB = k - cutA` from `b` such that:

* Left side has exactly `k` elements total
* And **every element on left ≤ every element on right**

Let:

* `leftA = a[cutA-1]` (max on left from a)
* `rightA = a[cutA]` (min on right from a)
* `leftB = b[cutB-1]`
* `rightB = b[cutB]`

Valid partition condition:

* `leftA <= rightB` AND `leftB <= rightA`

Then answer (k-th element) is:

* `max(leftA, leftB)`  ✅

We binary search `cutA` over the smaller array to get `O(log(min(n,m)))`.

---

## Step-by-step Dry Run (Example 1)

**a = [2, 3, 6, 7, 9]**
**b = [1, 4, 8, 10]**
**k = 5**

We want **5 elements on the left**.

Always binary search on smaller array → `b` is smaller (size 4), but we can also do on `a`.
Let’s do on `a` (works same). (In code we’ll swap to ensure smaller.)

`n=5, m=4`

We choose `cutA`, then `cutB = k - cutA`

Bounds for cutA:

* minimum `cutA = max(0, k-m) = max(0, 5-4)=1`
* maximum `cutA = min(k, n) = min(5,5)=5`

So `cutA ∈ [1..5]`

### Try cutA = 3

Then cutB = 2

Left parts:

* a left: [2,3,6] → leftA=6
* b left: [1,4]   → leftB=4

Right parts:

* a right starts at 7 → rightA=7
* b right starts at 8 → rightB=8

Check:

* leftA <= rightB? 6 <= 8 ✅
* leftB <= rightA? 4 <= 7 ✅

Partition valid → k-th element = max(leftA,leftB) = max(6,4) = **6**

✅ Answer = 6

---

## 3) Python Codes (Brute + Optimized)

### A) Brute (merge-like two pointers) — easy & interview-friendly baseline

**Time:** O(k) (we only walk until k)
**Space:** O(1)

```python
class Solution:
    def kthElement(self, a, b, k):
        i = 0  # pointer in a
        j = 0  # pointer in b
        current = -1

        # Time: O(k) because we advance exactly k times
        for _ in range(k):
            # pick smaller current element among a[i], b[j]
            if j >= len(b) or (i < len(a) and a[i] <= b[j]):
                current = a[i]
                i += 1
            else:
                current = b[j]
                j += 1

        return current
```

---

### B) Optimized (Most expected): Binary search on partition

**Time:** O(log(min(n,m)))
**Space:** O(1)

```python
class Solution:
    def kthElement(self, a, b, k):
        # Ensure 'a' is the smaller array to minimize binary search range
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        m = len(b)

        # cutA can’t be less than k-m (otherwise cutB would exceed m)
        # cutA can’t exceed k or n
        low = max(0, k - m)
        high = min(k, n)

        NEG_INF = float("-inf")
        POS_INF = float("inf")

        # Binary search for correct cutA
        while low <= high:
            cutA = (low + high) // 2
            cutB = k - cutA

            leftA = a[cutA - 1] if cutA > 0 else NEG_INF
            rightA = a[cutA] if cutA < n else POS_INF

            leftB = b[cutB - 1] if cutB > 0 else NEG_INF
            rightB = b[cutB] if cutB < m else POS_INF

            # Check if partition is valid
            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)

            # Too many taken from a -> move left
            if leftA > rightB:
                high = cutA - 1
            else:
                # Too few taken from a -> move right
                low = cutA + 1

        # Should never reach here if inputs are valid
        return -1
```

---

### C) “Pythonic” alternative (not allowed in interviews if constraints huge)

Using sorting on combined array is **O((n+m) log(n+m))** and memory heavy, so not recommended.
(Just mentioning: don’t do it.)

---

## 4) Interview recall + expected Q&A

### 5-line recall template (say this)

1. “We need k-th in merged sorted order without merging.”
2. “Use partition: pick `cutA`, `cutB=k-cutA`.”
3. “Condition: `leftA<=rightB` and `leftB<=rightA`.”
4. “Binary search `cutA` on smaller array.”
5. “Answer is `max(leftA,leftB)`.”

### Mnemonic

**“CUT → CHECK → SHIFT → MAX”**

* CUT the arrays
* CHECK boundary order
* SHIFT binary search left/right
* MAX of lefts is answer

---

### Interviewer Q&A (common)

**Q1. Why is answer `max(leftA, leftB)`?**
A. Left side contains exactly `k` smallest elements. The k-th is the largest in left side → `max(leftA,leftB)`.

**Q2. Why do we binary search only one array?**
A. Because `cutB = k - cutA` is forced once we choose `cutA`, so only one degree of freedom.

**Q3. Why swap to make `a` smaller?**
A. Complexity depends on the searched array length → `O(log(min(n,m)))`.

**Q4. How do you handle edge cases like cut=0 or cut=n?**
A. Use sentinels: `-inf` for missing left, `+inf` for missing right.

**Q5. What’s the brute force alternative and complexity?**
A. Two-pointer merge until k → `O(k)` time, `O(1)` space.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Database / Search “Top-K across two shards”**
   Two sorted result lists (by timestamp/score) coming from two servers. Need the **k-th** item without merging full lists (saves time + memory).

2. **Streaming analytics (percentiles / order statistics)**
   Two sorted batches of measurements (e.g., latencies from two regions). Find the **k-th smallest** (or percentile) quickly for dashboards.

3. **Merging logs (incident timelines)**
   Two sorted log streams (by time). Find the event at the **k-th** position in the combined timeline without building the full merged list.

4. **Finance / Trading (two venues)**
   Two sorted price/volume ladders from two exchanges. Query the **k-th** best price level overall without full merge.

---

## 6) Full Program (timed end-to-end + sample input/output + inline complexity)

**Input format supported (simple + practical):**

* Line 1: array `a` elements space-separated
* Line 2: array `b` elements space-separated
* Line 3: `k`

If **no stdin**, it runs the sample:
`a=[2,3,6,7,9]`, `b=[1,4,8,10]`, `k=5` → output `6`.

```python
import sys
import time


class Solution:
    def kthElement(self, a, b, k):
        """
        Optimized (most expected): Binary search on partition.
        Time: O(log(min(len(a), len(b))))
        Space: O(1)
        """

        # Always binary search on the smaller array
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        m = len(b)

        # Bounds for cutA so that cutB = k - cutA is valid within [0..m]
        # Time: O(1)
        low = max(0, k - m)
        high = min(k, n)

        NEG_INF = float("-inf")
        POS_INF = float("inf")

        # Binary search over cutA
        # Time: O(log(min(n, m))), Space: O(1)
        while low <= high:
            cutA = (low + high) // 2
            cutB = k - cutA

            leftA = a[cutA - 1] if cutA > 0 else NEG_INF
            rightA = a[cutA] if cutA < n else POS_INF

            leftB = b[cutB - 1] if cutB > 0 else NEG_INF
            rightB = b[cutB] if cutB < m else POS_INF

            # Valid partition: all left elements <= all right elements
            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)

            # If leftA is too big, we took too many from a -> move left
            if leftA > rightB:
                high = cutA - 1
            else:
                # We took too few from a -> move right
                low = cutA + 1

        # Should not happen for valid k and sorted arrays
        return -1


def main():
    # Measure the full program runtime (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        a = [2, 3, 6, 7, 9]
        b = [1, 4, 8, 10]
        k = 5

        ans = solver.kthElement(a, b, k)

        print("Input:")
        print("a =", a)
        print("b =", b)
        print("k =", k)
        print("\nOutput:")
        print(ans)

    else:
        # ---------------- INPUT MODE ----------------
        # Expected format:
        # line1: a elements
        # line2: b elements
        # line3: k
        lines = [line.strip() for line in data.splitlines() if line.strip()]

        a = list(map(int, lines[0].split()))
        b = list(map(int, lines[1].split()))
        k = int(lines[2])

        ans = solver.kthElement(a, b, k)
        print(ans)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Example (Demo Mode) Output

For `a=[2,3,6,7,9]`, `b=[1,4,8,10]`, `k=5` → **6** (+ runtime)


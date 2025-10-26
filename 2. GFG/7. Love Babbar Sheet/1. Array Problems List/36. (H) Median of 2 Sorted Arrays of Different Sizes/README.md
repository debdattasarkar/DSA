
---

# 🧮 Median of 2 Sorted Arrays of Different Sizes

**Difficulty:** Hard
**Accuracy:** 28.4%
**Submissions:** 140K+
**Points:** 8
**Average Time:** 35m

---

## 📘 Problem Statement

Given two **sorted arrays** `a[]` and `b[]`, find and return the **median** of the combined array **after merging** them into a single sorted array.

---

## 💡 Examples

### Example 1

**Input:**
`a[] = [3, 5, 6, 12, 15], b[] = [3, 4, 6, 10, 10, 12]`

**Output:**
`6`

**Explanation:**
The merged array is `[3, 3, 4, 5, 6, 6, 10, 10, 12, 12, 15]`.
So the median of the merged array is **6**.

---

### Example 2

**Input:**
`a[] = [2, 3, 5, 8], b[] = [10, 12, 14, 16, 18, 20]`

**Output:**
`11`

**Explanation:**
The merged array is `[2, 3, 5, 8, 10, 12, 14, 16, 18, 20]`.
So the median of the merged array is **(10 + 12) / 2 = 11**.

---

### Example 3

**Input:**
`a[] = [], b[] = [2, 4, 5, 6]`

**Output:**
`4.5`

**Explanation:**
The merged array is `[2, 4, 5, 6]`.
So the median of the merged array is **(4 + 5) / 2 = 4.5**.

---

## ⚙️ Constraints

```
1 ≤ a.size(), b.size() ≤ 10^6  
1 ≤ a[i], b[i] ≤ 10^9  
a.size() + b.size() > 0
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(log(min(n, m)))
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

`Amazon` · `Microsoft` · `Samsung` · `Google`

---

## 🏷️ Topic Tags

* Arrays
* Data Structures
* Algorithms
* Binary Search

---

## 📚 Related Articles

* [*Median of Two Sorted Arrays of Different Sizes*](https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/)

---

---

awesome — let’s make **Median of Two Sorted Arrays (possibly different sizes)** interview-ready.

---

## 2) Concept + step-by-step dry run

### Core idea (what is the median here?)

If we conceptually merge two already **sorted** arrays `a` and `b`, the median is the central value:

* If `N = len(a)+len(b)` is **odd** → element at index `N//2` (0-based).
* If `N` is **even** → average of elements at indices `N//2 - 1` and `N//2`.

We can:

1. **Brute** merge in O(n+m) then pick middle(s), or
2. **Binary-search** a cut (partition) in O(log(min(n,m))) *without* merging — the classic interview solution.

### Partition insight (optimized)

Choose a split `i` in `a` and `j` in `b` so that the **left side** has `(N+1)//2` elements:

```
i in [0..n], j = (N+1)//2 - i
```

It’s a **valid partition** if:

```
a_left_max <= b_right_min   and   b_left_max <= a_right_min
```

Then the median is:

* **odd N**: max(left_maxes)
* **even N**: (max(left_maxes) + min(right_mins))/2

We binary search `i` to make the inequalities true. Use sentinels:

```
a_left_max  = -inf if i==0 else a[i-1]
a_right_min =  inf if i==n else a[i]
(similarly for b with j)
```

### Dry run (Example 1)

`a=[3,5,6,12,15] (n=5)`, `b=[3,4,6,10,10,12] (m=6)`, `N=11`, target left = `(11+1)//2=6`.

We binary-search `i` in `a`:

* `i=2` ⇒ `j=4`.
  `a_left_max=5`, `a_right_min=6`; `b_left_max=10`, `b_right_min=10`.
  Check: `a_left_max(5) <= b_right_min(10)` ✓, `b_left_max(10) <= a_right_min(6)` ✗ → `i` too small → move right.

* `i=4` ⇒ `j=2`.
  `a_left_max=12`, `a_right_min=15`; `b_left_max=4`, `b_right_min=6`.
  Check: `a_left_max(12) <= 6` ✗ → `i` too big → move left.

* `i=3` ⇒ `j=3`.
  `a_left_max=6`, `a_right_min=12`; `b_left_max=6`, `b_right_min=10`.
  Both checks pass → valid partition.
  `N` odd ⇒ median = `max(6,6) = 6`. ✅

---

## 3) Python solutions (interview-style)

### A) Optimized O(log(min(n,m))) — Binary Search on smaller array

```python
class Solution:
    def medianOf2(self, a, b):
        """
        Median of two sorted arrays (possibly different sizes).
        Binary-search a partition on the smaller array.

        Time  : O(log(min(n, m)))
        Space : O(1)
        Returns a float median.
        """
        # Ensure 'a' is the smaller array to minimize the search space
        if len(a) > len(b):
            a, b = b, a

        n, m = len(a), len(b)
        if n == 0 and m == 0:
            raise ValueError("Both arrays are empty")

        total = n + m
        left_target = (total + 1) // 2  # size of left partition

        lo, hi = 0, n  # 'i' ranges from 0..n
        INF_POS = float('inf')
        INF_NEG = float('-inf')

        while lo <= hi:
            i = (lo + hi) // 2
            j = left_target - i

            a_left  = INF_NEG if i == 0 else a[i - 1]
            a_right = INF_POS if i == n else a[i]
            b_left  = INF_NEG if j == 0 else b[j - 1]
            b_right = INF_POS if j == m else b[j]

            # Valid partition?
            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return float(max(a_left, b_left))
                left_max = max(a_left, b_left)
                right_min = min(a_right, b_right)
                return (left_max + right_min) / 2.0

            # Need to shift 'i'
            if a_left > b_right:
                # too many from 'a' on the left, move left
                hi = i - 1
            else:
                # too few from 'a' on the left, move right
                lo = i + 1

        # Should never reach here if inputs are sorted and total > 0
        raise RuntimeError("No valid partition found")
```

### B) Brute/Easy O(n+m) — Merge until the middle (two pointers)

```python
class SolutionMerge:
    def medianOf2(self, a, b):
        """
        Merge-like walk (without building the full array).
        Time  : O(n + m)
        Space : O(1)
        """
        n, m = len(a), len(b)
        total = n + m
        if total == 0:
            raise ValueError("Both arrays are empty")

        i = j = 0
        prev = curr = None
        steps = total // 2  # number of pops to reach the middle

        for _ in range(steps + 1):  # walk until we step onto the middle item
            prev = curr
            if i < n and (j >= m or a[i] <= b[j]):
                curr = a[i]; i += 1
            else:
                curr = b[j]; j += 1

        if total % 2 == 1:
            return float(curr)
        else:
            return (prev + curr) / 2.0
```

> In most interviews: if they say “arrays are already **sorted**”, they expect **binary partition** (solution A). If they’re fine with `O(n+m)`, solution B is perfectly acceptable and quick to code.

---

## 4) Interview quick-recall + likely Q&A

### 10-second memory hook

* **Mantra:** “**Partition** the two arrays so *left size* = (N+1)//2 and **left_max ≤ right_min**. Then take middle(s).”
* **Return:** odd → `max(left_maxes)`; even → `(max(left_maxes)+min(right_mins))/2`.

### Common follow-ups (crisp answers)

**Q1. Why binary search on the smaller array?**
To keep the search space `O(log(min(n,m)))` and to avoid out-of-range partitions.

**Q2. What about empty arrays?**
Handled naturally with ±∞ sentinels. If one is empty, the median is just the median of the other.

**Q3. Stability / duplicates?**
No issue — inequalities handle equals (≤). Duplicates are fine.

**Q4. Edge cases you watch for?**

* One array much smaller (even size 0).
* All elements of `a` on one side of `b` (e.g., `a`’s max ≤ `b`’s min).
* Even vs odd total length.

**Q5. Why `(N+1)//2` for left size?**
It makes the odd case simple: the extra one sits on the left; the median is `max(left_maxes)`.

**Q6. Complexity?**
Binary partition: **O(log(min(n,m)))** time, **O(1)** space.
Merge walk: **O(n+m)** time, **O(1)** space.

---

### 5-line pseudo-code you can say before coding

```
if len(a) > len(b): swap
lo=0; hi=len(a); L=(n+m+1)//2
while lo<=hi:
  i=(lo+hi)//2; j=L-i
  aL=a[i-1] or -inf; aR=a[i] or +inf
  bL=b[j-1] or -inf; bR=b[j] or +inf
  if aL<=bR and bL<=aR: return odd? max(aL,bL) : (max(aL,bL)+min(aR,bR))/2
  elif aL>bR: hi=i-1
  else: lo=i+1
```

That’s the entire algorithm you can reconstruct in **under 30 seconds** during an interview.

---

---

awesome — wrapping up **Median of Two Sorted Arrays (different sizes)** with the last two parts 👇

---

## 5) Real-World Use Cases (short & relatable)

* **Telemetry/latency analytics across shards:** each shard already keeps a sorted sample; compute the **overall median** quickly without re-sorting all events.
* **Salary benchmarking by region:** HR exports per-region salaries sorted; find the **global median** by combining two regions efficiently.
* **Distributed databases / map-reduce:** reducers output sorted runs; a coordinator can binary-search partitions across two runs to get the **global median** in **O(log(min(n,m)))**.

All of these map directly to: two sorted lists, minimal extra memory, fast central statistic.

---

## 6) Full Python Program (optimized + brute, with timing)

```python
from timeit import timeit
import random

# ------------------------------------------------------------
# Optimized solution: Binary search on smaller array
# ------------------------------------------------------------
class Solution:
    def medianOf2(self, a, b):
        """
        Median of two sorted arrays (possibly different sizes).
        Binary-search a partition on the smaller array.

        Time  : O(log(min(n, m)))  -- binary search range is size of smaller array
        Space : O(1)               -- constant extra variables
        Returns: float (median)
        """
        # Ensure a is the smaller array to keep search space minimal
        if len(a) > len(b):
            a, b = b, a

        n, m = len(a), len(b)
        if n + m == 0:
            raise ValueError("Both arrays are empty")

        total = n + m
        left_target = (total + 1) // 2  # how many elements should be on the LEFT

        lo, hi = 0, n
        NEG, POS = float("-inf"), float("inf")

        while lo <= hi:
            i = (lo + hi) // 2          # cut index in a
            j = left_target - i         # cut index in b so left sizes add up

            aL = NEG if i == 0 else a[i - 1]
            aR = POS if i == n else a[i]
            bL = NEG if j == 0 else b[j - 1]
            bR = POS if j == m else b[j]

            # Valid partition if all left <= all right
            if aL <= bR and bL <= aR:
                if total % 2 == 1:
                    return float(max(aL, bL))  # odd -> the extra element sits on the left
                left_max = max(aL, bL)
                right_min = min(aR, bR)
                return (left_max + right_min) / 2.0

            # Adjust partition
            if aL > bR:
                hi = i - 1               # too many from a on the left -> move left
            else:
                lo = i + 1               # too few from a on the left -> move right

        # Shouldn't reach here if inputs are valid sorted arrays
        raise RuntimeError("No valid partition found")

# ------------------------------------------------------------
# Brute/Easy: Merge-walk without building array (O(n+m))
# ------------------------------------------------------------
class SolutionMerge:
    def medianOf2(self, a, b):
        """
        Two-pointer merge until the middle position(s).
        Time  : O(n + m)
        Space : O(1)
        """
        n, m = len(a), len(b)
        if n + m == 0:
            raise ValueError("Both arrays are empty")

        i = j = 0
        prev = curr = None
        steps = (n + m) // 2  # how many pops until we reach the middle
        for _ in range(steps + 1):
            prev = curr
            if i < n and (j >= m or a[i] <= b[j]):
                curr = a[i]; i += 1
            else:
                curr = b[j]; j += 1

        if (n + m) % 2 == 1:
            return float(curr)
        return (prev + curr) / 2.0

# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Median of Two Sorted Arrays (different sizes) ===\n")

    cases = [
        # (a, b, expected)
        ([3, 5, 6, 12, 15], [3, 4, 6, 10, 10, 12], 6.0),
        ([2, 3, 5, 8],      [10, 12, 14, 16, 18, 20], 11.0),
        ([],                [2, 4, 5, 6], 4.5),
        ([1],               [2, 3, 4], 2.5),
        ([1, 2],            [3, 4, 5], 3.0),
    ]

    opt = Solution()
    brute = SolutionMerge()

    for a, b, expected in cases:
        r1 = opt.medianOf2(a[:], b[:])
        r2 = brute.medianOf2(a[:], b[:])
        print(f"a={a}, b={b}")
        print(f"  Optimized O(log(min)) : {r1}")
        print(f"  Merge-walk  O(n+m)    : {r2}")
        print(f"  Expected              : {expected}")
        print(f"  Match?                : {abs(r1-expected)<1e-9 and abs(r2-expected)<1e-9}\n")

    # -------- Timing on large random sorted inputs --------
    random.seed(7)
    n, m = 2_000_00, 3_000_00  # 200k and 300k (total 500k)
    A = sorted(random.randint(1, 10**9) for _ in range(n))
    B = sorted(random.randint(1, 10**9) for _ in range(m))

    t_opt = timeit(lambda: Solution().medianOf2(A, B), number=3)
    # Merge-walk is linear; still fast but much heavier -> compare once
    t_brute = timeit(lambda: SolutionMerge().medianOf2(A, B), number=1)

    print("=== Timing (seconds) ===")
    print(f"Optimized O(log(min(n,m)))  runs=3: total {t_opt:.4f}s  | avg {(t_opt/3):.4f}s/run")
    print(f"Merge-walk O(n+m)            run=1: {t_brute:.4f}s")

if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For sample cases, **both** methods match the expected medians (`Match? True`).
* Timing shows the **binary-partition** approach scales with the *logarithm of the smaller array*, whereas the merge walk is linear in the total size.

---

### 10-second recall (before coding)

> **“Partition so left size = (n+m+1)//2 and left_max ≤ right_min;
> odd → max(left); even → (max(left)+min(right))/2; search i on the smaller array.”**


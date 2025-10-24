
---

# 🧩 Overlapping Intervals

**Difficulty:** Medium
**Accuracy:** 57.41%
**Submissions:** 103K+
**Points:** 4

---

## 📝 Problem Statement

Given an array of intervals `arr[][]`, where `arr[i] = [startᵢ, endᵢ]`,
the task is to **merge all of the overlapping intervals**.

---

## 🧮 Examples

### Example 1

**Input:**

```
arr = [[1,3], [2,4], [6,8], [9,10]]
```

**Output:**

```
[[1,4], [6,8], [9,10]]
```

**Explanation:**
In the given intervals, there are only two overlapping intervals:

* `[1,3]` and `[2,4]` overlap and merge into `[1,4]`.

So the final list of merged intervals becomes `[[1,4], [6,8], [9,10]]`.

---

### Example 2

**Input:**

```
arr = [[6,8], [1,9], [2,4], [4,7]]
```

**Output:**

```
[[1,9]]
```

**Explanation:**
In this case, all the intervals overlap with `[1,9]`,
so merging all of them gives one single interval — `[1,9]`.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10⁵  
0 ≤ startᵢ ≤ endᵢ ≤ 10⁵
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log n) |
| **Auxiliary Space** | O(1)       |

---

## 🏢 Company Tags

Amazon · Microsoft · Google · Nutanix · Zoho

---

## 🧠 Topic Tags

Arrays · Hash · Sorting · Data Structures · Algorithms

---

## 🔗 Related Articles

* [Merging Intervals](https://www.geeksforgeeks.org/merging-intervals/)

---

---

Let’s make **Overlapping Intervals** interview-ready: quick intuition + dry runs, then clean Python in the exact signature you asked for, plus what to say when you’re in the room.

---

## 2) Intuition + step-by-step dry run

### Core idea (why it works)

1. **Sort** intervals by start time.
2. Walk left→right, keep a **current merged interval** `[curL, curR]`.
3. For each next `[L, R]`:

   * If it **overlaps** (`L ≤ curR`) → extend: `curR = max(curR, R)`.
   * Else → push `[curL, curR]` to the answer and start a new current interval.
4. Push the last current interval.

Sorting ensures that when you see a new interval, any possible overlap is **only with the interval you’re currently building**, never with something earlier already finalized.

> Overlap rule used here: **closed intervals** (touching counts as overlap), i.e., `[a,b]` overlaps `[c,d]` when `c ≤ b`.
> (If your interviewer wants “touching is not overlap”, change the check to `c < b` → `c ≤ b - 1` or simply `c > b` for non-overlap.)

---

### Dry runs

#### Example 1

```
arr = [[1,3], [2,4], [6,8], [9,10]]
(sort by start → already sorted)

current = [1,3]
next [2,4] : 2 ≤ 3 ⇒ overlap → current = [1, max(3,4)] = [1,4]
next [6,8] : 6 ≤ 4 ? no  ⇒ output [1,4], current = [6,8]
next [9,10]: 9 ≤ 8 ? no  ⇒ output [6,8], current = [9,10]
end → output [9,10]
Answer = [[1,4], [6,8], [9,10]]
```

#### Example 2

```
arr = [[6,8], [1,9], [2,4], [4,7]]
sort → [[1,9], [2,4], [4,7], [6,8]]

current = [1,9]
[2,4] : 2 ≤ 9  → current = [1, max(9,4)]=[1,9]
[4,7] : 4 ≤ 9  → current = [1, max(9,7)]=[1,9]
[6,8] : 6 ≤ 9  → current = [1, max(9,8)]=[1,9]
end → output [1,9]
Answer = [[1,9]]
```

---

## 3) Python solutions (brute + optimal), interview-style comments

Your required signature:

```python
class Solution:
    def mergeOverlap(self, arr):
        # Code here
```

### A) Optimal & standard: sort + linear merge (O(n log n), O(1) extra if sorting in place)

```python
class Solution:
    def mergeOverlap(self, arr):
        """
        Merge overlapping (closed) intervals.
        - Overlap rule: [L1,R1] overlaps [L2,R2] iff L2 <= R1
        Time  : O(n log n) due to sort
        Space : O(1) extra (aside from output) if in-place sort is allowed
        """
        if not arr:
            return []

        # 1) Sort by start (then by end for determinism)
        arr.sort(key=lambda it: (it[0], it[1]))  # O(n log n)

        merged = []
        curL, curR = arr[0][0], arr[0][1]       # current merged interval

        # 2) Scan left → right, merging on the fly
        for i in range(1, len(arr)):
            L, R = arr[i]
            if L <= curR:                       # overlap → extend current
                curR = max(curR, R)
            else:                               # no overlap → flush current
                merged.append([curL, curR])
                curL, curR = L, R

        # 3) Push the final interval
        merged.append([curL, curR])
        return merged
```

### B) Simple “brute-ish” insertion style (O(n²) worst-case), no pre-sort

For each interval, insert it into the result list and **re-merge** overlaps within result. Clearer than building an interval graph, but far less efficient than sorting.

```python
class Solution:
    def mergeOverlap(self, arr):
        """
        Brute / insertion-style:
        - For each interval, insert into result then merge any overlaps in result.
        - No initial sort; worst-case O(n^2).
        Useful to discuss as a baseline; not preferred in production.
        """
        res = []
        for L, R in arr:
            self._insert_and_merge(res, [L, R])
        # Optional: return sorted by start for determinism
        res.sort(key=lambda it: (it[0], it[1]))
        return res

    def _insert_and_merge(self, res, newI):
        """Insert newI into res and merge overlaps (in-place)."""
        L, R = newI
        out = []
        placed = False
        for a, b in sorted(res + [newI], key=lambda it: (it[0], it[1])):
            if not out or a > out[-1][1]:   # no overlap with last
                out.append([a, b])
            else:                            # merge with last
                out[-1][1] = max(out[-1][1], b)
        res.clear()
        res.extend(out)
```

> In interviews, use A (sort+merge). Mention B only as a conceptual baseline.

---

## 4) Interview quick-recall + common Q&A

### 5-Line Pseudocode (the muscle memory)

```
sort intervals by start
cur = first
for each next:
    if next.start <= cur.end: cur.end = max(cur.end, next.end)
    else: output cur, cur = next
output cur
```

**Mnemonic:** **“Sort → Sweep → Merge/Flush → Done.”**

---

### Quick Q&A you may be asked

* **Why do we sort by start?**
  After sorting, any interval can only overlap with the **currently open** merged interval. We never need to look back beyond it → one linear pass.

* **What’s the overlap condition?**
  With **closed intervals**, `[a,b]` overlaps `[c,d]` iff `c ≤ b`.
  If the problem defines “touching not overlapping”, change to `c > b` for non-overlap.

* **Time and space complexity?**
  `O(n log n)` to sort, `O(n)` scan afterwards. Extra space `O(1)` if sorting in place (output `O(k)` for k merged intervals).

* **Do we ever need to look more than one interval back?**
  No. Sorting guarantees that once an interval doesn’t overlap with `cur`, it won’t overlap with anything earlier.

* **Edge cases?**
  Empty list, single interval, fully nested intervals, duplicates, already disjoint, already merged, very large endpoints — all naturally handled.

* **Stability / order of output?**
  By sorting by start (and end as tiebreaker), the output is deterministic.

---

### One-liner you can say before you code

> “I’ll **sort** by start and scan once, keeping a running interval.
> If the next interval starts **before or at** the current end, I **merge** by extending the end; otherwise I **flush** the current interval and start a new one.
> That’s **O(n log n)** time and **O(1)** extra space.”

---

---

Awesome—let’s wrap **Overlapping Intervals** with real-world motivation and a clean, runnable program you can drop into any editor.

---

## 5) Real-World Use Cases (easy to relate)

* **Calendar / meeting scheduling:** merge overlapping meeting slots to find free time or total busy duration.
* **Booking systems (rooms, flights):** coalesce overlapping reservations to prevent double-counting capacity.
* **Log compaction / monitoring windows:** merge alert windows to compute total downtime.
* **IP/network ranges & firewall rules:** merge overlapping ranges to minimize rule count.
* **Genomics:** merge overlapping genomic intervals (exons/peaks) to compute coverage.

---

## 6) Full Program (runnable)

* Implements the optimal **sort + sweep** solution.
* Lots of inline comments calling out **time/space complexity** of each step.
* Includes sample inputs, outputs, and timing with `perf_counter` and `timeit`.

```python
#!/usr/bin/env python3
"""
Overlapping Intervals — Merge all overlapping closed intervals.
Strategy: sort by start, sweep once, extend current interval or flush to output.

Complexities:
- Sorting: O(n log n) time, O(1) extra if in-place (Python's Timsort uses O(n) aux on worst cases; we ignore that here).
- Single pass merge: O(n) time.
- Output: O(k) intervals (k <= n).
Overall: O(n log n) time, O(1) extra beyond output.
"""

from time import perf_counter
import timeit
from typing import List


class Solution:
    def mergeOverlap(self, arr: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals (closed intervals).
        Overlap rule: [a,b] overlaps [c,d] iff c <= b.

        Parameters
        ----------
        arr : List[List[int]]
            List of [start, end], may be unsorted.

        Returns
        -------
        List[List[int]] : merged, non-overlapping intervals sorted by start.
        """
        # Edge case: empty input → O(1)
        if not arr:
            return []

        # 1) SORT by start (then end for determinism)
        #    Time: O(n log n). Space: O(1) extra (conceptually).
        arr.sort(key=lambda it: (it[0], it[1]))

        # 2) SWEEP once left→right; keep current merged interval
        #    Time: O(n). Space: O(1) beyond result.
        merged: List[List[int]] = []
        curL, curR = arr[0]

        for i in range(1, len(arr)):
            L, R = arr[i]
            if L <= curR:                 # Overlap → extend
                # O(1) update
                if R > curR:
                    curR = R
            else:
                # No overlap → flush current interval
                merged.append([curL, curR])  # Amortized O(1)
                curL, curR = L, R            # Start new

        # 3) Push the tail interval — O(1)
        merged.append([curL, curR])
        return merged


# -------------------------- Demonstration & Timing --------------------------

def demo():
    cases = [
        # From prompt style
        ([[1,3], [2,4], [6,8], [9,10]],
         [[1,4], [6,8], [9,10]]),

        ([[6,8], [1,9], [2,4], [4,7]],
         [[1,9]]),

        # More edge-ish cases
        ([], []),
        ([[1,5]], [[1,5]]),
        ([[1,2], [3,4]], [[1,2], [3,4]]),             # disjoint
        ([[1,10], [2,3], [4,5], [6,7], [8,9]], [[1,10]]),  # nested
        ([[1,2], [2,3], [3,4]], [[1,4]]),             # touching (closed intervals → merge)
    ]

    sol = Solution()
    print("=== Sample I/O ===")
    for arr, expected in cases:
        start = perf_counter()
        out = sol.mergeOverlap([x[:] for x in arr])  # copy for safety
        dur = (perf_counter() - start) * 1e6
        print(f"Input : {arr}")
        print(f"Output: {out}   (took {dur:.1f} µs)")
        if expected is not None:
            print(f"Expect: {expected}")
        print("-" * 50)

    # Timing on a larger random case
    import random
    random.seed(7)
    n = 200_000
    # Create random intervals with start<=end
    big = []
    for _ in range(n):
        a = random.randint(0, 1_000_000)
        b = a + random.randint(0, 1000)
        big.append([a, b])

    sol = Solution()
    avg = timeit.timeit("sol.mergeOverlap(big[:])", number=3, globals={"sol": sol, "big": big}) / 3
    print(f"\nAverage time on n={n} intervals over 3 runs: {avg:.3f} s")

    print("\nComplexity recap:")
    print("  Sort  : O(n log n)")
    print("  Sweep : O(n)")
    print("  Extra : O(1) beyond the output list")


if __name__ == "__main__":
    demo()
```

### Example Output (illustrative)

```
=== Sample I/O ===
Input : [[1, 3], [2, 4], [6, 8], [9, 10]]
Output: [[1, 4], [6, 8], [9, 10]]   (took 85.7 µs)
Expect: [[1, 4], [6, 8], [9, 10]]
--------------------------------------------------
Input : [[6, 8], [1, 9], [2, 4], [4, 7]]
Output: [[1, 9]]   (took 92.3 µs)
Expect: [[1, 9]]
--------------------------------------------------
...
Average time on n=200000 intervals over 3 runs: 0.4xx s

Complexity recap:
  Sort  : O(n log n)
  Sweep : O(n)
  Extra : O(1) beyond the output list
```

---

### What to say in the interview (10 seconds)

> “I’ll **sort by start**, then do a **single sweep** keeping a running interval. If the next starts **≤ current end**, **extend**; otherwise, **flush** current and start a new one. That’s **O(n log n)** time and **O(1)** extra space.”

Here’s your image content fully converted into a **README.md** format — preserving every part, including problem description, examples, constraints, and complexity.

---

# 🧮 Find K Smallest Sum Pairs

**Difficulty:** Medium
**Accuracy:** 62.51%
**Submissions:** 7K+
**Points:** 4

---

## 📘 Problem Statement

Given two integer arrays `arr1[]` and `arr2[]` sorted in ascending order and an integer `k`, your task is to find **k pairs with the smallest sums**, such that one element of each pair belongs to `arr1[]` and the other belongs to `arr2[]`.

Return the list of these **k pairs**, where each pair is represented as `[arr1[i], arr2[j]]`.

> **Note:** You can return any possible `k` pairs with the smallest sums; the driver code will print `true` if it is correct, else it will print `false`.

---

## 🧩 Examples

### Example 1:

**Input:**

```
arr1[] = [1, 7, 11], arr2[] = [2, 4, 6], k = 3
```

**Output:**

```
true
```

**Explanation:**
All possible combinations of elements from the two arrays are:
`[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [7, 6], [11, 2], [11, 4], [11, 6]`.

Among these, the three pairs with the minimum sums are:
`[1, 2], [1, 4], [1, 6]`.

---

### Example 2:

**Input:**

```
arr1[] = [1, 3], arr2[] = [2, 4], k = 2
```

**Output:**

```
true
```

**Explanation:**
All possible combinations are:
`[1, 2], [1, 4], [3, 2], [3, 4]`.

Among these, the two pairs with the minimum sums are:
`[1, 2], [3, 2]`.

---

## ⚙️ Constraints

```
1 ≤ arr1.size(), arr2.size() ≤ 5 * 10^4  
1 ≤ arr1[i], arr2[j] ≤ 10^9  
1 ≤ k ≤ 10^3
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** `O(k * log k)`
* **Auxiliary Space:** `O(k)`

---

## 🧠 Topic Tags

* Priority Queue
* Heap
* Data Structures

---

## 🔗 Related Articles

* [Find K Pairs Smallest Sums Two Arrays](https://www.geeksforgeeks.org/find-k-pairs-smallest-sums-two-arrays/)

---

---

Alright—before we dive in: are you prepping for interviews (DSA level), and are you comfortable with heaps/priority queues? I’ll teach assuming late–intermediate (LeetCode Medium) level. If you want me to slow down or switch gears, say the word.

---

# 2) Text explanation + step-by-step dry run

## Core idea (what we’re optimizing)

All pairs look like `(arr1[i], arr2[j])`. Because both arrays are sorted ascending:

* For a **fixed** `i`, the sums with `arr2` increase as `j` grows.
* So the smallest pair overall must be among the pairs that use the **smallest elements** of each array.
* We can “grow” pairs in ascending order of sum using a **min-heap** (best-first search), instead of generating all `n*m` pairs.

### Min-heap strategy (classic)

1. Start by pairing the smallest of `arr1` with the smallest of `arr2`: `(0,0)`.
2. When you pop `(i, j)` from the heap, you’ve found the next smallest pair.
3. From `(i, j)`, the **next candidates** are:

   * `(i, j+1)` (same `arr1[i]`, next in `arr2`)
   * If `j == 0` (first time we touch row `i`), also push `(i+1, 0)` (next `arr1` with smallest `arr2`).
     This ensures we don’t push duplicates and we keep the heap to about `O(k)` size.

This yields at most `k` pops, each `O(log k)` → `O(k log k)` time, `O(k)` extra space.

---

## Dry run (quick and visual)

**Input:**
`arr1 = [1, 7, 11]`
`arr2 = [2, 4, 6]`
`k = 3`

We’ll store heap entries as `(sum, i, j)`.

**Init**

* Push `(1+2=3, 0, 0)`
* Heap: `[(3,0,0)]`
* Result: `[]`

**Pop #1**

* Pop `(3,0,0)` → pair `[1,2]` added.
* Push neighbors:

  * `(0,1)` because `j==0` → push `(7+2=9, 1,0)`
  * `(0,1)` for same row? Careful—this means `(i, j+1)` → `(0,1)` is `(1+4=5, 0,1)`
* Heap: `[(5,0,1), (9,1,0)]`
* Result: `[[1,2]]`

**Pop #2**

* Pop `(5,0,1)` → pair `[1,4]` added.
* Push neighbors:

  * `(0,2)` (same row next col): `(1+6=7, 0,2)`
  * `j==1`, so we **don’t** push `(1,0)` again (we already handled the new row when we first touched row 0).
* Heap: `[(7,0,2), (9,1,0)]`
* Result: `[[1,2],[1,4]]`

**Pop #3**

* Pop `(7,0,2)` → pair `[1,6]` added.
* Push neighbors:

  * `(0,3)` doesn’t exist (arr2 exhausted)
* Heap still has `(9,1,0)` but we already have `k=3` pairs.

**Answer:** `[[1,2], [1,4], [1,6]]` (any order that’s the first 3 sums is acceptable)

---

# 3) Python solutions (brute force and optimized)

I’ll give you two approaches that are common in interviews.

* Use **meaningful variable names** and **inline comments** so you can repeat them under pressure.

## A) Optimized (Min-Heap, expected in interviews) — `O(k log k)` time, `O(k)` space

```python
class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        """
        Optimized: best-first search using a min-heap.
        Time:  O(k log k)   | Space: O(k)
        Assumes arr1 and arr2 are sorted ascending.
        Returns a list of k pairs [arr1[i], arr2[j]] with smallest sums.
        """
        import heapq

        n, m = len(arr1), len(arr2)
        if n == 0 or m == 0 or k <= 0:
            return []

        # Each heap item: (sum, i, j)
        min_heap = []
        result_pairs = []

        # Seed with the first pair (0,0)
        heapq.heappush(min_heap, (arr1[0] + arr2[0], 0, 0))

        # To avoid pushing the same (i, j) more than once, we track visited states.
        # (For this specific pattern of pushes, visited isn’t strictly necessary,
        #  but we include it to be robust and interview-friendly.)
        visited = set()
        visited.add((0, 0))

        while min_heap and len(result_pairs) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            result_pairs.append([arr1[i], arr2[j]])

            # Candidate 1: move right in arr2 (same i, j+1)
            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (arr1[i] + arr2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            # Candidate 2: move down in arr1 (i+1, same j) — only when j == 0
            # This ensures each row i is introduced exactly once (at column 0).
            if j == 0 and i + 1 < n and (i + 1, 0) not in visited:
                heapq.heappush(min_heap, (arr1[i + 1] + arr2[0], i + 1, 0))
                visited.add((i + 1, 0))

        return result_pairs
```

### Why this version is “interview-friendly”

* Uses a clear invariant: we expand from the smallest sum outward.
* Heap stays small (~`k`) instead of `n*m`.
* Simple, repeatable neighbor logic:

  * Always push `(i, j+1)`.
  * Only push `(i+1, 0)` when `j == 0`.

---

## B) Brute force (easy to explain) — `O(n*m log(n*m))` time, `O(n*m)` space

Use when constraints are tiny or as a warm-up explanation.

```python
class SolutionBrute:
    def kSmallestPair(self, arr1, arr2, k):
        """
        Brute force: generate all pairs, sort by sum, take first k.
        Time:  O(n*m log(n*m)) | Space: O(n*m)
        """
        all_pairs = []

        # Generate every pair and store (sum, i, j) or directly the pair
        for i, x in enumerate(arr1):
            for j, y in enumerate(arr2):
                all_pairs.append((x + y, x, y))  # keep sum for sorting

        # Sort by sum then by values (not strictly required for this problem)
        all_pairs.sort(key=lambda t: t[0])

        # Pick first k pairs
        result = []
        for idx in range(min(k, len(all_pairs))):
            _, x, y = all_pairs[idx]
            result.append([x, y])

        return result
```

---

# 4) Interview quick-recall + Q&A

### How to remember quickly

* **Picture the grid:** rows = `arr1[i]`, cols = `arr2[j]`, sums increase to the right and downward.
* **Rule of thumb:** push two directions from each popped cell:

  * Right: `(i, j+1)` (same row, next column)
  * Down: `(i+1, 0)` **only when** `j == 0`
* **Stop condition:** after collecting `k` pops.
* **Complexities mantra:** Heap → `k` pops × `log(heap_size)` ⇒ `O(k log k)` time, `O(k)` space.

### Common interviewer questions (with sharp answers)

**Q1. Why can we avoid generating all pairs?**
*A1.* Arrays are sorted, so for each `i`, the sequence `(i, 0), (i, 1), …` is non-decreasing in sum. A best-first (min-heap) expansion visits pairs in ascending sum order without enumerating all `n*m`.

**Q2. Why only push `(i+1, 0)` when `j == 0`?**
*A2.* When we first pop a pair from row `i`, we introduce the next row with its smallest column to keep candidates minimal. If we pushed `(i+1, 0)` for every `(i, j)`, we’d duplicate work and blow up the heap.

**Q3. Do we need a `visited` set?**
*A3.* With the “push right” + “push next row only when `j==0`” pattern, duplicates don’t arise, so it’s optional. I add `visited` to be safe and to show awareness of duplicate-state pitfalls.

**Q4. What are time and space complexities?**
*A4.* At most `k` extractions and `≤2k` insertions; heap size `O(k)`. → `O(k log k)` time, `O(k)` space.

**Q5. What if arrays aren’t sorted?**
*A5.* Sort them first (`O(n log n + m log m)`), then apply the same heap method.

**Q6. Can we stream/early-stop without building the whole answer?**
*A6.* Yes—just stop popping after `k` pairs. You never need all pairs.

**Q7. Edge cases to mention?**
*A7.* Empty arrays, `k <= 0`, `k > n*m` (just return all possible pairs), large values (sum fits in Python int), duplicates in arrays (allowed—pairs can repeat values).

---

---

Great—let’s round this out with a few crisp, interview-friendly bits.

---

## 5) Real-World Use Cases (easy to relate)

1. **Top-K product bundles**
   Combine cheapest item from list A with shipping/packaging option from list B to get the **k** lowest total costs quickly (no full cross-join).

2. **Flight + hotel combos**
   Given sorted prices for flights and hotels on a date, return the **k** cheapest trip packages.

3. **Recommendation candidates (cross features)**
   Pick **k** user–item candidate pairs with the smallest “distance” (e.g., user embedding norm + item price penalty), before running heavier re-ranking.

4. **Alert matching by time proximity**
   Match events from two sorted timestamp lists where `gap_cost = |t1 - t2|`; find **k** smallest gaps to triage likely correlations.

5. **Ad serving: segment × creative**
   Choose **k** segment–creative pairs minimizing `(bid_cost + predicted_penalty)` without enumerating all pairs.

---

## 6) Full program (brute + optimized) with inline complexity notes and timing

* Uses your requested class/method signature.
* Very explicit comments on **time/space** at each key step.
* A small **`main`** runs both methods on sample inputs, prints outputs, and times them using both `time.perf_counter()` and `timeit.timeit`.

```python
from typing import List
import heapq
import time
import timeit


class Solution:
    def kSmallestPair(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        """
        Optimized min-heap (best-first) solution.
        Assumes arr1 and arr2 are sorted ascending.

        Overall complexity:
          - Time:  O(k log k) because we do at most k pops and ~2k pushes; heap size <= O(k)
          - Space: O(k) for the heap + visited (result is O(k) too)

        Returns: list of k pairs [arr1[i], arr2[j]] with the smallest sums.
        """
        n, m = len(arr1), len(arr2)

        # Guard cases — O(1) time, O(1) space
        if n == 0 or m == 0 or k <= 0:
            return []

        # Min-heap storing tuples: (sum, i, j)
        # Build initial heap with the very smallest pair (0,0) — O(log 1) ~ O(1)
        min_heap = [(arr1[0] + arr2[0], 0, 0)]

        # Visited coordinates to avoid duplicates — at most O(k) elements
        visited = {(0, 0)}

        result_pairs: List[List[int]] = []

        # Main loop runs at most k iterations — O(k)
        while min_heap and len(result_pairs) < k:
            # Pop smallest sum so far — O(log heap) = O(log k)
            current_sum, i, j = heapq.heappop(min_heap)
            # Append to result — O(1)
            result_pairs.append([arr1[i], arr2[j]])

            # Candidate 1: move right in arr2 (same i, j+1)
            if j + 1 < m and (i, j + 1) not in visited:
                # Push — O(log k); visited insert — O(1) avg
                heapq.heappush(min_heap, (arr1[i] + arr2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            # Candidate 2: introduce next row only once (i+1, 0) when we are at j == 0
            if j == 0 and i + 1 < n and (i + 1, 0) not in visited:
                # Push — O(log k); visited insert — O(1) avg
                heapq.heappush(min_heap, (arr1[i + 1] + arr2[0], i + 1, 0))
                visited.add((i + 1, 0))

        return result_pairs


class SolutionBrute:
    def kSmallestPair(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        """
        Brute-force solution: generate all pairs, sort by sum, take first k.

        Complexity:
          - Generate all n*m pairs — Time: O(n*m), Space: O(n*m)
          - Sort by sum — Time: O(n*m log(n*m))
          - Slice first k — O(k)

        Use only when n and m are very small.
        """
        all_pairs = []

        # Generate pairs — O(n*m) time, O(n*m) space
        for x in arr1:
            for y in arr2:
                all_pairs.append((x + y, x, y))

        # Sort by sum — O(n*m log(n*m))
        all_pairs.sort(key=lambda t: t[0])

        # Take the first k — O(k)
        k = min(k, len(all_pairs))
        return [[all_pairs[i][1], all_pairs[i][2]] for i in range(k)]


def run_and_time(arr1, arr2, k):
    """
    Helper to run both methods once and report wall-clock time via perf_counter,
    and an averaged timing via timeit (to smooth noise).
    """
    print("\n=== Input ===")
    print("arr1 =", arr1)
    print("arr2 =", arr2)
    print("k    =", k)

    # Optimized
    sol = Solution()
    t0 = time.perf_counter()
    out_opt = sol.kSmallestPair(arr1, arr2, k)
    t1 = time.perf_counter()
    elapsed_opt = (t1 - t0) * 1e6  # microseconds

    # Brute
    sol_b = SolutionBrute()
    t2 = time.perf_counter()
    out_brute = sol_b.kSmallestPair(arr1, arr2, k)
    t3 = time.perf_counter()
    elapsed_brute = (t3 - t2) * 1e6  # microseconds

    print("\n--- Outputs (single run) ---")
    print("Optimized:", out_opt)
    print("Brute    :", out_brute)

    print("\n--- Timing: perf_counter (single run) ---")
    print(f"Optimized: {elapsed_opt:.2f} µs")
    print(f"Brute    : {elapsed_brute:.2f} µs")

    # timeit on small repetitions (adjust number if arrays are large)
    reps = 200

    def call_opt():
        sol.kSmallestPair(arr1, arr2, k)

    def call_brute():
        sol_b.kSmallestPair(arr1, arr2, k)

    avg_opt = timeit.timeit(call_opt, number=reps) / reps
    avg_brute = timeit.timeit(call_brute, number=reps) / reps

    print("\n--- Timing: timeit (average over", reps, "runs) ---")
    print(f"Optimized avg: {avg_opt * 1e6:.2f} µs/run")
    print(f"Brute avg    : {avg_brute * 1e6:.2f} µs/run")


if __name__ == "__main__":
    # Example 1 from the prompt
    run_and_time(arr1=[1, 7, 11], arr2=[2, 4, 6], k=3)

    # Example 2 from the prompt
    run_and_time(arr1=[1, 3], arr2=[2, 4], k=2)

    # You can add your own quick checks here:
    # run_and_time(arr1=[1,1,2], arr2=[1,2,3], k=5)
```

**What you’ll see when you run it locally**

* Both outputs printed (they should match the expected `k` smallest pairs).
* Timing for a single run via `perf_counter`, and an averaged microseconds-per-run via `timeit`.

---

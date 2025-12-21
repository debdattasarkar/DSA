Below is a **complete, interview-ready, README-style explanation** for the problem **“Count X in Range of a Sorted Array”**, followed by **step-by-step dry run**, **multiple Python solutions**, **interview Q&A**, **real-world use cases**, **full runnable program with timing**, **5-line memorisable pseudocode**, and finally a **visual sketch-note** to lock the idea in memory.

---

# 📘 Count X in Range of a Sorted Array

## 🧩 Problem Statement

You are given:

* A **sorted array** `arr[]`
* A list of queries `queries[][]`, where each query is of the form **[l, r, x]**

For **each query**, count how many times the number **x** appears in the subarray
`arr[l…r]` (both indices inclusive).

---

## 🔍 Key Insight

Because the array is **sorted**, we can use **Binary Search** to efficiently find:

* The **first occurrence** of `x`
* The **last occurrence** of `x`

The count is simply:

```
last_index - first_index + 1
```

If `x` does not exist → answer is `0`.

---

## 📌 Examples

### Example 1

```
Input:
arr = [1, 2, 2, 4, 5, 5, 5, 8]
queries = [[0, 7, 5], [1, 2, 2], [0, 3, 7]]

Output:
[3, 2, 0]
```

### Example 2

```
Input:
arr = [1, 3, 3, 3, 6, 7, 8]
queries = [[0, 3, 3], [4, 6, 3], [1, 5, 6]]

Output:
[3, 0, 1]
```

---

## ⏱ Expected Complexity

| Metric | Value            |
| ------ | ---------------- |
| Time   | **O(q · log n)** |
| Space  | **O(1)**         |

---

## 🏷 Topic Tags

* Binary Search
* Arrays
* Data Structures
* Algorithms

---

## 🧠 Step-by-Step Explanation (Dry Run)

### Example Query: `[0, 7, 5]`

Array:

```
Index:  0 1 2 3 4 5 6 7
Value:  1 2 2 4 5 5 5 8
```

We want to count how many times **5** appears between index **0 and 7**.

1. Binary search for **first occurrence of 5** → index **4**
2. Binary search for **last occurrence of 5** → index **6**
3. Count = `6 - 4 + 1 = 3`

✔️ Answer = **3**

---

## 🧪 Python Implementations

## 2. Text explanation (with step-by-step dry run)

### Problem in one line

For each query `[l, r, x]`, count how many times `x` occurs in the **sorted** subarray `arr[l..r]`.

### Key observation

Because `arr` is **sorted**, all occurrences of the same value `x` are in one contiguous block.
So for a range `[l, r]`, the count of `x` is:

> `count = (first index > x in [l..r]) - (first index >= x in [l..r])`

This is exactly **upper_bound - lower_bound** (a.k.a. `bisect_right - bisect_left`).

---

### Dry Run (Example 1)

`arr = [1, 2, 2, 4, 5, 5, 5, 8]`
`queries = [[0, 7, 5], [1, 2, 2], [0, 3, 7]]`

#### Query 1: `[0, 7, 5]`

Subarray = whole array.

* `lower_bound(5)` = first index where value >= 5 → index **4**
* `upper_bound(5)` = first index where value > 5 → index **7**
  Count = `7 - 4 = 3`

✅ answer = 3

#### Query 2: `[1, 2, 2]`

Subarray indices 1..2 → `[2, 2]`

* `lower_bound(2, in [1..2])` → index **1**
* `upper_bound(2, in [1..2])` → index **3** (right boundary is exclusive, so it returns 3)
  Count = `3 - 1 = 2`

✅ answer = 2

#### Query 3: `[0, 3, 7]`

Subarray `[1, 2, 2, 4]`

* `lower_bound(7)` → index **4**
* `upper_bound(7)` → index **4**
  Count = `4 - 4 = 0`

✅ answer = 0

Final output: **[3, 2, 0]**

---

## 3. Python Solutions (Brute + Interview-Expected Optimized)

### 3.1 Brute Force (simple, but too slow)

For each query, scan the range and count matches.

```python
class Solution:
    def countXInRange_bruteforce(self, arr, queries):
        """
        Brute force:
        For each query [l, r, x], scan arr[l..r] and count x.

        Time:  O(q * (r-l+1)) worst ~ O(q*n)
        Space: O(1)
        """
        answers = []

        for left, right, target in queries:
            count = 0
            for i in range(left, right + 1):
                if arr[i] == target:
                    count += 1
            answers.append(count)

        return answers
```

---

### 3.2 Optimized (Expected in interviews): `bisect_left` + `bisect_right`

This is the cleanest and fastest expected approach: **O(q log n)**.

```python
from bisect import bisect_left, bisect_right

class Solution:
    def countXInRange(self, arr, queries):
        """
        Optimized using binary search (lower_bound & upper_bound).

        For each query [l, r, x]:
            left_index  = first position of x in arr[l..r]  (lower_bound)
            right_index = first position > x in arr[l..r]   (upper_bound)
            count = right_index - left_index

        Time:  O(q * log n)
        Space: O(1)
        """
        answers = []

        for left, right, target in queries:
            # bisect functions allow searching within a subrange:
            # lo = left, hi = right+1 (because hi is exclusive)
            first_ge = bisect_left(arr, target, left, right + 1)
            first_gt = bisect_right(arr, target, left, right + 1)

            answers.append(first_gt - first_ge)

        return answers
```

---

### 3.3 Optimized without bisect (manual lower/upper bound)

If interviewer asks “don’t use library”, implement binary search yourself.

```python
class Solution:
    def _lower_bound(self, arr, target, left, right):
        """
        First index in [left..right+1) where arr[idx] >= target
        """
        lo, hi = left, right + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _upper_bound(self, arr, target, left, right):
        """
        First index in [left..right+1) where arr[idx] > target
        """
        lo, hi = left, right + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def countXInRange(self, arr, queries):
        """
        Manual lower_bound + upper_bound.

        Time:  O(q * log n)
        Space: O(1)
        """
        answers = []

        for left, right, target in queries:
            first_ge = self._lower_bound(arr, target, left, right)
            first_gt = self._upper_bound(arr, target, left, right)

            answers.append(first_gt - first_ge)

        return answers
```

---

## 4. Interview: How to remember fast + Expected Q&A

### Quick memory trick (super easy)

Think:

> **“COUNT in sorted range = UpperBound - LowerBound”**

Mnemonic:

> ✅ **“LB = start, UB = stop, answer = UB - LB”**

---

### 60-second recall script (say to interviewer)

> “Array is sorted, so all x’s are contiguous.
> For each query [l, r, x], I binary-search inside that index window.
> lower_bound gives first index where value >= x, upper_bound gives first index where value > x.
> Their difference is the count. Complexity is O(q log n).”

---

### Expected interviewer questions & crisp answers

**Q1. Why does `upper_bound - lower_bound` give the count?**
Because all `x` occur in one block: `[first_x ... last_x]`.
`lower_bound` points to `first_x`, `upper_bound` points to `last_x + 1`. Difference = number of x’s.

**Q2. What if x is not present?**
Then both bounds return the same index → difference = 0.

**Q3. Why not scan each range?**
Because q and n can be up to 1e5 → scanning is too slow (O(nq)). Binary search gives O(q log n).

**Q4. Why do we use `hi = r+1`?**
Because Python bisect and the clean [lo, hi) binary-search pattern uses **exclusive high**.

**Q5. Can we preprocess to answer faster than log n per query?**
Yes: store positions of each value in a hashmap (value → sorted list of indices), then for each query do 2 bisections on that index list. Still O(log occurrences), usually very fast. (Optional enhancement.)

---

---

## 5. Real-World Use Cases (few, very relatable)

1. **Log / Event Analytics (time-window counts)**

   * Logs are often stored sorted by some key (timestamp, status code).
   * Query: “How many times error code `500` occurred between time `l` and `r`?”
   * Same idea: count occurrences in a sorted range using bounds.

2. **Trading / Order Book & Tick Data**

   * Trades can be stored sorted by price or timestamp buckets.
   * Query: “How many trades happened at price `x` between indices/time range `[l, r]`?”
   * Use lower/upper bound to count quickly.

3. **Database Index / Search Index**

   * Index pages are sorted.
   * Query: “How many records with key = `x` fall inside a range of rows?”
   * `upper_bound - lower_bound` is the exact counting primitive in many index structures.

---

## 6. Full Program (with timing + inline time/space comments)

This program:

* reads `n`, the sorted array
* reads `q`, and the queries `[l r x]`
* prints counts for each query
* prints total runtime (algorithm execution only)

```python
import time
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countXInRange(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        For each query [l, r, x], count occurrences of x in arr[l..r] (inclusive).
        Since arr is sorted, occurrences are contiguous.

        Use:
            left_idx  = lower_bound(x) in [l, r]
            right_idx = upper_bound(x) in [l, r]
            count = right_idx - left_idx

        Time per query: O(log n)
        Total time:     O(q log n)
        Space:          O(1) extra (excluding output list)
        """
        answers = []  # Space: O(q) for output (required)

        for left, right, target in queries:
            # bisect uses [lo, hi) so hi = right + 1
            # Time: O(log n)
            first_ge = bisect_left(arr, target, left, right + 1)
            first_gt = bisect_right(arr, target, left, right + 1)

            # Count occurrences in the range
            answers.append(first_gt - first_ge)

        return answers


def main():
    """
    Input format:
        n
        a1 a2 ... an        (sorted array)
        q
        l r x              (q lines)

    Example Input:
        8
        1 2 2 4 5 5 5 8
        3
        0 7 5
        1 2 2
        0 3 7

    Expected Output:
        3
        2
        0
        TimeTaken: <seconds>
    """

    print("Enter n:")
    n = int(input().strip())

    print(f"Enter {n} sorted integers:")
    arr = list(map(int, input().split()))
    arr = arr[:n]  # defensive trim if extra provided

    print("Enter q:")
    q = int(input().strip())

    print("Enter queries (l r x), one per line:")
    queries = []
    for _ in range(q):
        l, r, x = map(int, input().split())
        queries.append([l, r, x])

    solver = Solution()

    # Timing only the algorithm section (not user typing time)
    start_time = time.perf_counter()

    # Core computation: O(q log n) time, O(1) extra space
    answers = solver.countXInRange(arr, queries)

    end_time = time.perf_counter()

    # Print outputs (each count on new line, typical judge format)
    print("\nOutputs:")
    for ans in answers:
        print(ans)

    print(f"\nTimeTaken (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

### Sample Run

**Input**

```text
8
1 2 2 4 5 5 5 8
3
0 7 5
1 2 2
0 3 7
```

**Output**

```text
3
2
0
TimeTaken (seconds): 0.0000xx
```

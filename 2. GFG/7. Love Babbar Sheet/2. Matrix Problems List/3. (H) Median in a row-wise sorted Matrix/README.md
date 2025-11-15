
---

# 📊 Median in a Row-Wise Sorted Matrix

**Difficulty:** Hard
**Accuracy:** 55.05%
**Submissions:** 160K+
**Points:** 8

---

## 🧠 Problem Statement

Given a **row-wise sorted matrix** `mat[][]` of size **n × m**, where the number of rows and columns is always **odd**,
return the **median** of the matrix.

---

## 🧩 Examples

### Example 1

**Input:**

```
mat[][] = [
  [1, 3, 5],
  [2, 6, 9],
  [3, 6, 9]
]
```

**Output:**

```
5
```

**Explanation:**
Sorting all elements of the matrix gives:
`[1, 2, 3, 3, 5, 6, 6, 9, 9]`
Hence, the **median = 5**.

---

### Example 2

**Input:**

```
mat[][] = [
  [2, 4, 9],
  [3, 6, 7],
  [4, 7, 10]
]
```

**Output:**

```
6
```

**Explanation:**
Sorting all matrix elements gives:
`[2, 3, 4, 4, 6, 7, 7, 9, 10]`
Hence, **6 is the median**.

---

### Example 3

**Input:**

```
mat[][] = [
  [3],
  [4],
  [8]
]
```

**Output:**

```
4
```

**Explanation:**
Sorting all matrix elements gives:
`[3, 4, 8]`
Hence, the **median = 4**.

---

## ⚙️ Constraints

* ( 1 \leq n, m \leq 400 )
* ( 1 \leq mat[i][j] \leq 2000 )

---

## ⏱️ Expected Complexities

| Complexity Type     | Value                               |
| ------------------- | ----------------------------------- |
| **Time**            | O(n × log m × log(maxVal – minVal)) |
| **Auxiliary Space** | O(1)                                |

---

## 🧩 Topic Tags

* Matrix
* Binary Search
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Find Median Row Wise Sorted Matrix](https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/)

---

---

Awesome — let’s nail **Median in a Row-wise Sorted Matrix** like an interview champ.

---

## 2) Explanation + step-by-step dry run

### Problem in one line

Each row is sorted (but the whole matrix isn’t necessarily globally sorted). Find the **median** of all `n*m` numbers. (In the problem, `n` and `m` are odd so `n*m` is odd → a unique median exists.)

### Two ways to think about it

1. **Brute**: flatten → sort → pick middle.
   Simple but costs `O(nm log(nm))`.

2. **Optimal (value-space binary search)**:
   Use the fact that rows are individually sorted. We can **binary search on the value** (between global min and max) and, for a candidate value `mid`, count how many elements are `<= mid` using `bisect_right` in each row (because each row is sorted).

   * If `count(<= mid) < K`, go **right** (need a bigger value).
   * Else go **left** (mid is big enough to be a median).
     Here `K = (n*m + 1)//2` (the position of the median in 1-based indexing).

**Why it works:**
The predicate “`count(<= v) >= K`” is monotonic in `v`, so classic binary search applies.

---

### Dry run (Example 1)

```
mat = [[1, 3, 5],
       [2, 6, 9],
       [3, 6, 9]]

n=3, m=3, K=(9+1)//2=5
low = min(first of each row)  = min(1,2,3) = 1
high= max(last  of each row)  = max(5,9,9) = 9
```

Binary search on value:

* mid = (1+9)//2 = 5
  count(<=5):

  * row1: [1,3,5] → 3
  * row2: [2,6,9] → 1 (only 2)
  * row3: [3,6,9] → 1 (only 3)
    total = 3+1+1=5 ≥ K(5) → move **left**: high = 5
* mid = (1+5)//2 = 3
  count(<=3):

  * r1: 2  (1,3)
  * r2: 1  (2)
  * r3: 1  (3) → total=4 < 5 → move **right**: low = 4
* mid = (4+5)//2 = 4
  count(<=4):

  * r1: 2 (1,3)
  * r2: 1 (2)
  * r3: 1 (3) → total=4 < 5 → right: low = 5

Now `low == high == 5` → **median = 5** ✅

---

## 3) Python solutions (brute → optimal)

### Signature to use

```python
class Solution:
    def median(self, mat):
        # code here
```

### A) Brute force (clear baseline)

```python
class Solution:
    def median(self, mat):
        """
        Flatten + sort + pick middle.
        Time : O(n*m * log(n*m))
        Space: O(n*m) (for the flattened list)
        """
        if not mat or not mat[0]:
            raise ValueError("matrix is empty")
        flat = [x for row in mat for x in row]         # collect all
        flat.sort()                                    # O(N log N)
        N = len(flat)
        return flat[N // 2]                            # N is odd per problem
```

### B) Optimal — Binary search on value (uses row-wise order)

```python
from bisect import bisect_right

class Solution:
    def median(self, mat):
        """
        Value-space binary search + per-row upper_bound count.
        Time : O(n * log(maxVal - minVal) * log m)
               (for each value guess, do n times bisect_right on length-m rows)
        Space: O(1)
        """
        if not mat or not mat[0]:
            raise ValueError("matrix is empty")

        n, m = len(mat), len(mat[0])

        # global min and max using row-wise facts
        low  = min(row[0]   for row in mat)
        high = max(row[-1]  for row in mat)
        K = (n * m + 1) // 2                         # 1-based median position

        # Binary search smallest value v such that count(<=v) >= K
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid using bisect_right in each row
            cnt = 0
            for row in mat:
                # number of elements <= mid in this row
                cnt += bisect_right(row, mid)

            if cnt < K:                # not enough small elements, go right
                low = mid + 1
            else:                      # mid is large enough, go left
                high = mid

        return low                     # or high; both equal here
```

> In interviews, write version **B** (short + optimal). Mention **A** as baseline.

---

## 4) Interview “how to remember” + Q&A

### 5-line pseudo you can say out loud

```
low = min(first of each row); high = max(last of each row)
K = (n*m + 1)//2
while low < high:
  mid = (low+high)//2
  cnt = sum(upper_bound(row, mid) for each row)
  if cnt < K: low = mid + 1
  else:       high = mid
return low
```

**Mnemonic:**
**“Value-search, Count with upper_bound, K-th small → squeeze range.”**

### Likely interviewer questions (and crisp answers)

* **Q:** Why binary search on value instead of flattening?
  **A:** Each row is sorted, so we can count `<= mid` in `O(log m)` per row using `upper_bound`. This gives **O(n log m log value_range)** vs `O(nm log(nm))` if we flatten.

* **Q:** What’s `upper_bound`?
  **A:** Position of the first element `> mid` → the count of elements `<= mid`. In Python: `bisect_right(row, mid)`.

* **Q:** Why does the predicate work?
  **A:** `count(<= v)` is monotonic in `v`. If it’s ≥ `K` for `v`, it’s also ≥ `K` for any larger value → perfect for binary search.

* **Q:** What is `K` and why `(n*m + 1)//2`?
  **A:** The median is the `K`-th smallest; for odd `N=n*m`, `K=(N+1)//2`. (If even, this picks the lower median — you can adapt per requirements.)

* **Q:** Edge cases?
  **A:** Duplicates are fine. Single row/column works. Empty matrix should be guarded.

* **Q:** Complexity?
  **A:** `O(n log m log V)` where `V = maxVal - minVal`. Space `O(1)`.

---

### Quick comparison

| Approach                      | Time                 | Space    | When                            |
| ----------------------------- | -------------------- | -------- | ------------------------------- |
| Flatten + sort                | O(nm log(nm))        | O(nm)    | Simple baseline                 |
| **Value-space binary search** | **O(n log m log V)** | **O(1)** | **Preferred** (row-wise sorted) |

You’re ready: explain the monotone count + `bisect_right` trick, write the compact code, and you’ll ace it.

---

---

Great—let’s wrap “Median in a Row-wise Sorted Matrix” with practical context and a ready-to-run, timed program.

---

## 5) Real-World Use Cases (short & relatable)

* **Telemetry/storage shards:** Each shard (row) stores readings in ascending order; shards are ingested sequentially. To compute a global median quickly without loading/merging all data, binary-search the value space and count with per-shard upper bounds.
* **Paginated search indexes:** Each page is sorted and pages are appended over time. Median of all keys (for balancing/thresholding) can be found by value-space search across pages.
* **Streaming histogram approximation:** Buckets (rows) store sorted partial samples. Median across all buckets is computed by asking, “How many values ≤ mid in each bucket?”—exactly the `bisect_right` counting step.

All rely on: rows sorted individually → we can count `≤ mid` in `O(log m)` per row and binary-search the answer in the value domain.

---

## 6) Full Python Program (timed, with complexity notes inline)

```python
"""
Median in a Row-wise Sorted Matrix
----------------------------------
We have an n x m matrix where each row is sorted ascending (rows may overlap).
Goal: return the median of all n*m values (n and m are odd → unique median).

Approach used below: VALUE-SPACE BINARY SEARCH
  - Let low  = min(row[0]   for row in mat)         # O(n)
  - Let high = max(row[-1]  for row in mat)         # O(n)
  - K = (n*m + 1)//2  (1-based index of the median)
  - While low < high:
        mid = (low + high)//2
        cnt = sum( number of elements <= mid in each row )    # per row upper_bound
        If cnt < K: low = mid + 1
        else:        high = mid
  - Answer is low (== high)

Complexities:
  - Each count uses bisect_right on a length-m row: O(log m)
  - For n rows: O(n log m) per mid
  - Number of mids ≈ log2(maxVal - minVal + 1)
  => Time:  O(n * log m * log(value_range))
  => Space: O(1) extra
"""

from bisect import bisect_right
import timeit
from typing import List


class Solution:
    def median(self, mat: List[List[int]]) -> int:
        """
        Returns the median of a row-wise sorted matrix.

        Step-by-step complexities:
          - Guard checks: O(1)
          - Compute low/high via row endpoints: O(n)
          - Binary search loop: O(log(value_range)) iterations
              * Each iteration: sum of bisect_right over n rows → O(n log m)
          - Space: O(1) beyond input
        """
        if not mat or not mat[0]:
            raise ValueError("Empty matrix")

        n, m = len(mat), len(mat[0])

        # Global min & max leveraging row-sort order: O(n)
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        # 1-based index of the median among N = n*m values (odd by problem)
        K = (n * m + 1) // 2

        # Binary search on value domain
        while low < high:
            mid = (low + high) // 2

            # Count how many values <= mid across all rows
            # Each row contributes upper_bound(mid) = index of first element > mid
            cnt = 0
            for row in mat:                   # O(n)
                cnt += bisect_right(row, mid) # O(log m) per row

            if cnt < K:
                low = mid + 1   # not enough smalls → need larger median
            else:
                high = mid      # enough or too many → median is <= mid

        return low


# ------------------------------- Demo & Timing -------------------------------
if __name__ == "__main__":
    tests = [
        # (matrix, expected_median)
        ([[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]], 5),

        ([[2, 4, 9],
          [3, 6, 7],
          [4, 7, 10]], 6),

        ([[3],
          [4],
          [8]], 4),

        # some additional checks
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]], 5),

        ([[1, 2, 2],
          [2, 2, 3],
          [3, 3, 3]], 2),
    ]

    solver = Solution()
    print("Median in a Row-wise Sorted Matrix (value-space binary search)\n")

    for mat, expected in tests:
        # Time a single full run (includes all work)
        elapsed = timeit.timeit(lambda: solver.median(mat), number=1)
        ans = solver.median(mat)
        print(f"mat={mat}\n -> median={ans} (expected {expected}), time={elapsed:.6f}s\n")
```

### Example Output (illustrative)

```
Median in a Row-wise Sorted Matrix (value-space binary search)

mat=[[1, 3, 5], [2, 6, 9], [3, 6, 9]]
 -> median=5 (expected 5), time=0.0000xxs

mat=[[2, 4, 9], [3, 6, 7], [4, 7, 10]]
 -> median=6 (expected 6), time=0.0000xxs

mat=[[3], [4], [8]]
 -> median=4 (expected 4), time=0.0000xxs
...
```

**Interview recap you can say after coding:**

> “I binary-search the value range `[minRowFirst, maxRowLast]`. For a guess `mid`, I count `≤ mid` using `bisect_right` per row. If count `< K`, median is larger; else it’s smaller or equal. Time is `O(n log m log Δ)`, space `O(1)`.”

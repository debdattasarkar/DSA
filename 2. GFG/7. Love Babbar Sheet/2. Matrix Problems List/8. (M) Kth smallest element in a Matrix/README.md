
---

# 🔢 Kth Smallest Element in a Matrix

**Difficulty:** Medium
**Accuracy:** 61.42%
**Submissions:** 78K+
**Points:** 4
**Average Time:** 35m

---

## 🧠 Problem Statement

Given a matrix **mat[][]** of size **n × n**, where each row and column is sorted in **non-decreasing order**, find the **k-th smallest element** in the matrix.

---

## 🧩 Examples

### Example 1

**Input:**

```
mat[][] = [
  [16, 28, 60, 64],
  [22, 41, 63, 91],
  [27, 50, 87, 93],
  [36, 78, 87, 94]
],
k = 3
```

**Output:**

```
27
```

**Explanation:**
27 is the **3rd smallest** element.

---

### Example 2

**Input:**

```
mat[][] = [
  [10, 20, 30, 40],
  [15, 25, 35, 45],
  [24, 29, 37, 48],
  [32, 33, 39, 50]
],
k = 7
```

**Output:**

```
30
```

**Explanation:**
30 is the **7th smallest** element.

---

## ⚙️ Constraints

* (1 \leq n \leq 500)
* (1 \leq mat[i][j] \leq 10^4)
* (1 \leq k \leq n \times n)

---

## ⏱ Expected Complexities

* **Time Complexity:**
  [
  O\left(n \times \log(\text{max(mat)} - \text{min(mat)})\right)
  ]
* **Auxiliary Space:**
  [
  O(1)
  ]

---

## 🏢 Company Tags

* Accolite
* Amazon
* Samsung

---

## 🧩 Topic Tags

* Matrix
* Heap
* Data Structures
* Binary Search

---

## 📝 Related Interview Experiences

* Accolite Interview Set 2 Campus

---

## 📚 Related Articles

* [**K-th Smallest Element in a Row-wise and Column-wise Sorted 2D Array**](https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/)

---

---

Let’s turn this into an easy-to-remember interview pattern.

---

## 2. Explanation + Step-by-step Dry Run

### Problem recap

We have an **n×n** matrix `mat` where:

* Each **row** is sorted in non-decreasing order.
* Each **column** is sorted in non-decreasing order.

We must find the **k-th smallest element** in the whole matrix.

---

### Approaches (high level)

1. **Brute-force**

   * Flatten all `n*n` elements to a list.
   * Sort the list.
   * Return `flat[k-1]`.
   * Time: `O(n² log n²)` = `O(n² log n)`; Space: `O(n²)`.

2. **Min-heap (k-way merge)**

   * The matrix is like `n` sorted lists (each row).
   * Use a min-heap of size at most `n`:

     * Start with first element of each row.
     * Pop smallest `k-1` times, pushing the next element from the same row each time.
   * Time: `O(k log n)`, Space: `O(n)`.

3. **Binary search on value (expected by problem statement)** ✅

   * All values are between `minVal = mat[0][0]` and `maxVal = mat[n-1][n-1]`.
   * For any candidate value `mid`, we can count **how many elements ≤ mid** using each row’s sorted order (upper_bound / `bisect_right`).
   * If `count(≤ mid) < k`, we need a **bigger** value → move `low = mid + 1`.
   * Else, `mid` is big enough (at least k elements ≤ mid) → move `high = mid`.
   * Finally, `low` is the k-th smallest.

This matches the expected complexity: `O(n log(max-min))` with `O(1)` extra space (ignoring recursion/stack).

---

### Dry run – Example 2

Matrix:

```text
mat = [
  [10, 20, 30, 40],
  [15, 25, 35, 45],
  [24, 29, 37, 48],
  [32, 33, 39, 50]
]
k = 7
n = 4
```

Bounds:

```text
low  = mat[0][0]     = 10
high = mat[n-1][n-1] = 50
```

We want the **7th smallest**.

#### Iteration 1

`mid = (10 + 50) // 2 = 30`

Count how many elements ≤ 30 row by row (using `bisect_right`):

* Row1 `[10,20,30,40]` → index of first >30 is 3 → **3** elements ≤30
* Row2 `[15,25,35,45]` → index 2 → **2** elements ≤30
* Row3 `[24,29,37,48]` → index 2 → **2** elements ≤30
* Row4 `[32,33,39,50]` → index 0 → **0** elements ≤30

Total `count = 3+2+2+0 = 7`.

`count (7) >= k (7)` → k-th smallest is **≤ 30**, so we move `high`:

```text
high = mid = 30
```

#### Iteration 2

`mid = (10 + 30) // 2 = 20`

Count ≤20:

* Row1 `[10,20,30,40]` → index 2 → **2** elements
* Row2 `[15,25,35,45]` → index 1 → **1**
* Row3 `[24,29,37,48]` → index 0 → **0**
* Row4 `[32,33,39,50]` → index 0 → **0**

Total `count = 3`.

`3 < 7` → we need a **larger** value:

```text
low = mid + 1 = 21
```

#### Iteration 3

`mid = (21 + 30) // 2 = 25`

Count ≤25:

* Row1 → `[10,20,30,40]` → index 2 → **2**
* Row2 → `[15,25,35,45]` → index 2 → **2**
* Row3 → index 0 → **0**
* Row4 → index 0 → **0**

Total `count = 4 < 7` → still too small:

```text
low = mid + 1 = 26
```

#### Iteration 4

`mid = (26 + 30) // 2 = 28`

Count ≤28:

* Row1: index 2 → **2**
* Row2: index 1 → **1**
* Row3: `[24,29,37,48]` → index 2 → **2** (24,29)
* Row4: index 0 → **0**

Total `count = 5 < 7` → still too small:

```text
low = mid + 1 = 29
```

#### Iteration 5

`mid = (29 + 30) // 2 = 29`

Count ≤29:

* Row1: index 2 → **2**
* Row2: index 1 → **1**
* Row3: `[24,29,37,48]` → index 2 → **2** (24,29)
* Row4: index 0 → **0**

Total `count = 5 < 7` → still too small:

```text
low = mid + 1 = 30
```

Now `low == high == 30`.
That is the **7th smallest** element. ✅

---

## 3. Python Implementations

Signature:

```python
class Solution:
    def kthSmallest(self, mat, k):
        # code here
```

---

### 3.1 Brute Force – Flatten & Sort (for understanding)

```python
class Solution:
    def kthSmallest(self, mat, k):
        """
        Brute force:
        1) Flatten all elements.
        2) Sort them.
        3) Return (k-1)-th element.

        Time  : O(n^2 * log(n^2)) = O(n^2 log n)
        Space : O(n^2) extra
        """
        n = len(mat)
        flat = []

        # Collect all elements: O(n^2)
        for r in range(n):
            for c in range(n):
                flat.append(mat[r][c])

        # Sort the flattened array: O(n^2 log n^2)
        flat.sort()

        # k is 1-based index
        return flat[k - 1]
```

---

### 3.2 Min-Heap (k-way merge of rows)

```python
import heapq

class Solution:
    def kthSmallest(self, mat, k):
        """
        Use a min-heap to merge n sorted rows, like merging k sorted lists.

        Steps:
          - Push (value, row_index, col_index) for the first element of each row.
          - Repeat k-1 times:
              pop smallest
              push next element from that row (if any)
          - The next popped element is the k-th smallest.

        Time  : O(k log n)   (heap size at most n)
        Space : O(n)         (heap storage)
        """
        n = len(mat)
        if n == 0:
            return None

        min_heap = []

        # Initialize heap with first element of each row: O(n log n)
        for r in range(n):
            heapq.heappush(min_heap, (mat[r][0], r, 0))

        # Pop k-1 elements
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            # Push next element from the same row, if exists
            if c + 1 < n:
                heapq.heappush(min_heap, (mat[r][c + 1], r, c + 1))

        # The root now is the k-th smallest
        return heapq.heappop(min_heap)[0]
```

This is a very common interview solution too (especially on LeetCode).

---

### 3.3 Optimal (Expected) – Binary Search on Value + Row-wise Count

```python
from bisect import bisect_right

class Solution:
    def kthSmallest(self, mat, k):
        """
        Binary search in VALUE space.
        Each row and column are sorted in non-decreasing order.

        Idea:
          - Let low = smallest element, high = largest element.
          - While low < high:
              mid = (low + high) // 2
              count how many elements <= mid
              if count < k:    # not enough small elements
                  low = mid + 1
              else:            # mid is large enough / maybe too large
                  high = mid
          - low (== high) is the k-th smallest element.

        Counting:
          Since each row is sorted, we can use bisect_right(row, mid)
          to get the number of elements <= mid in that row.

        Time  : O(n * log(maxVal - minVal) * log n)  (or O(n log n log V))
        Space : O(1) extra
        """
        n = len(mat)
        if n == 0:
            return None

        # Global minimum and maximum (top-left and bottom-right)
        low = mat[0][0]
        high = mat[-1][-1]

        # Binary search over the value domain
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid
            count = 0
            for row in mat:
                # bisect_right returns index of first element > mid,
                # which is also count of elements <= mid.
                count += bisect_right(row, mid)

            if count < k:
                # Not enough elements <= mid, need larger values
                low = mid + 1
            else:
                # There are at least k elements <= mid,
                # so k-th smallest is <= mid. Shrink the high bound.
                high = mid

        return low
```

This one matches the GFG “Expected Time Complexity” note and is often the **model solution**.

---

## 4. Interview: How to Remember & What They May Ask

### 5-line pseudo-code for binary-search approach

```text
low = mat[0][0]; high = mat[n-1][n-1]
while low < high:
    mid = (low + high) // 2
    cnt = sum( upper_bound(row, mid) for each row )
    if cnt < k: low = mid + 1
    else: high = mid
return low
```

**Mnemonic:**

> **“Value Range → Count ≤ mid → Adjust Bound → Answer = low.”**

---

### Likely Interview Questions & Good Answers

**Q1. Why not just flatten and sort?**

> That works in `O(n² log n)` time and `O(n²)` space.
> But we can exploit the **sorted rows** (and columns) to do better using either a heap `O(k log n)` or binary search on value (`O(n log n log V)` and `O(1)` space). The problem’s expected complexity hints strongly at the value-space binary search.

---

**Q2. How do you count elements ≤ mid efficiently?**

> Because each row is sorted, for each row we can binary search for the first position where `row[pos] > mid` — that index is exactly the number of elements `≤ mid` in that row. In Python, this is `bisect_right(row, mid)`.

---

**Q3. Why does binary search on the value range work?**

> Define `f(x) = # of elements ≤ x`.
> As `x` increases, `f(x)` is **monotonic non-decreasing**.
> We want the smallest `x` such that `f(x) ≥ k`.
> That’s a perfect scenario for binary search:
> if `f(mid) < k` → we move `low` up; otherwise we move `high` down.

---

**Q4. Complexity?**

> Each iteration:
>
> * We compute `f(mid)` by scanning all `n` rows and doing a `log n` binary search in each → `O(n log n)`.
> * The number of iterations is `O(log (maxVal - minVal))`.
>   So total time is `O(n log n log V)`; space is `O(1)` beyond the input.

---

**Q5. Compare heap approach vs binary search in value?**

> * **Heap**: `O(k log n)` time, `O(n)` space; simple and intuitive.
> * **Value-binary-search**: `O(n log n log V)` time, `O(1)` space; uses sorted rows more directly and satisfies the GFG expected complexity.
>   In many practical cases, heap is simpler; in tight space constraints or when `k` is large, value-binary-search is competitive.

---

### 60-second recall before an interview

1. **Recognize pattern**: “Matrix sorted row & column wise, kth smallest.”
2. **Two main options**:

   * Min-heap on rows (k-way merge).
   * Binary search on **value** + count ≤ mid.
3. **Say out loud**:

   > “minVal = mat[0][0], maxVal = mat[n-1][n-1]; mid; `cnt = sum(upper_bound(row, mid))`; if `cnt < k` go right, else left.”
4. Mention complexity:

   > “O(n log n log V), O(1) space.”
5. Optionally mention heap variant and its complexity.

You’re now fully armed to explain, implement, and defend this problem in an interview.

---

---

Great follow-up. Let’s finalize this problem in a “plug-and-play + interview” way.

---

## 5) Real-World Use Cases (short, relatable)

Think of the matrix as **sorted in both directions**, like a “2D sorted table”.

1. **Database / Dashboard Grids (sorted rows & columns)**

   * A 2D table showing metrics (e.g., latency, scores, prices) sorted by row and column.
   * “k-th smallest element” = **k-th cheapest price / k-th lowest latency value** across all cells.
   * Instead of flattening huge tables, we binary-search the **value space** and use sorted rows to count efficiently.

2. **Heatmaps / Sensor Grids**

   * Sensors arranged in a grid; readings sorted by calibration (e.g., row by one dimension, column by another, both non-decreasing).
   * k-th smallest reading corresponds to a **threshold** where exactly k positions are below/at that level (for alarms, thresholds).

3. **2D Rank Queries in Recommendation Systems**

   * Each cell could be a combined score between user-groups and item-groups, sorted in both directions.
   * k-th smallest or k-th largest score is used to **decide a global threshold** for recommendations or alerts.

These examples match the pattern: *sorted 2D data, need global k-th order statistic*.

---

## 6) Full Python Program with Timing

We’ll implement the **binary search on value** method (matches expected complexity) inside `class Solution`, then add a small driver with sample inputs and `timeit` measurement.

```python
"""
K-th Smallest Element in a Sorted Matrix
----------------------------------------
Matrix mat is n x n, rows and columns sorted in non-decreasing order.
Find the k-th smallest element.

We use "binary search on value":

  low  = min element  = mat[0][0]
  high = max element  = mat[n-1][n-1]

For any candidate mid:
  count(mid) = number of elements <= mid
             = sum over all rows of upper_bound(row, mid)

If count(mid) < k    -> too few small elements, need larger numbers
                       => low = mid + 1
Else                 -> mid is large enough, maybe too large
                       => high = mid

When low == high, this value is the smallest number such that
count(value) >= k, i.e., the k-th smallest.

Complexities:
  Let n be matrix size, value range V = max(mat) - min(mat) + 1
  - Each count(mid) scan: O(n * log n) using binary search per row.
  - Binary search over value range: O(log V) iterations.
  => Time  : O(n * log n * log V)
  => Space : O(1) extra (no extra data structures apart from a few ints)
"""

from bisect import bisect_right
import timeit
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        Return the k-th smallest element in the matrix.

        Step-wise complexity:
          - Compute low, high : O(1), since matrix is sorted.
          - While loop:
              * Each iteration computes count of <= mid: O(n log n)
              * Number of iterations: O(log V)
          - Space: only a few scalar variables (O(1)).
        """
        n = len(mat)
        if n == 0:
            raise ValueError("Matrix must be non-empty")
        # Because matrix is n x n sorted both ways:
        low = mat[0][0]        # smallest value in matrix
        high = mat[-1][-1]     # largest value in matrix

        # Binary search on value range [low, high]
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid across all rows
            # Using bisect_right (upper_bound)
            count = 0
            for row in mat:                            # O(n)
                count += bisect_right(row, mid)        # O(log n) per row

            # Adjust search range based on count
            if count < k:
                # Too few elements <= mid, k-th smallest is bigger
                low = mid + 1
            else:
                # There are at least k elements <= mid,
                # so k-th smallest is <= mid
                high = mid

        # low == high is the k-th smallest
        return low


# ------------------------- Demo & Timing ------------------------- #
if __name__ == "__main__":
    solver = Solution()

    # Test cases: (matrix, k, expected_answer, description)
    tests = [
        (
            [
                [16, 28, 60, 64],
                [22, 41, 63, 91],
                [27, 50, 87, 93],
                [36, 78, 87, 94],
            ],
            3,
            27,
            "Example 1: 3rd smallest in 4x4"
        ),
        (
            [
                [10, 20, 30, 40],
                [15, 25, 35, 45],
                [24, 29, 37, 48],
                [32, 33, 39, 50],
            ],
            7,
            30,
            "Example 2: 7th smallest in 4x4"
        ),
        (
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15],
            ],
            5,
            11,
            "Custom: 5th smallest in 3x3"
        ),
    ]

    for mat, k, expected, note in tests:
        print(f"\n--- {note} ---")
        print("Matrix:")
        for row in mat:
            print(row)
        print(f"k = {k}")

        # Measure time for a single run of kthSmallest on this input
        elapsed = timeit.timeit(lambda: solver.kthSmallest(mat, k), number=1)
        result = solver.kthSmallest(mat, k)

        print(f"\nResult: {result} (expected: {expected})")
        print(f"Time taken for this run: {elapsed:.8f} seconds")
```

### What you’ll see when you run it (sample style)

```text
--- Example 1: 3rd smallest in 4x4 ---
Matrix:
[16, 28, 60, 64]
[22, 41, 63, 91]
[27, 50, 87, 93]
[36, 78, 87, 94]
k = 3

Result: 27 (expected: 27)
Time taken for this run: 0.0000xxxx seconds
```

This gives you:

* A clean `Solution.kthSmallest` that matches the expected complexity.
* Clear comments about **time and space** at each major step.
* A small main driver that runs multiple examples and shows the runtime using `timeit`.

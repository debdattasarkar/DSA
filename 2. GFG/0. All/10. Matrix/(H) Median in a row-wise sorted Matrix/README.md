
---

# Median in a row-wise sorted Matrix

**Difficulty:** Hard
**Accuracy:** 55.05%
**Submissions:** 160K+
**Points:** 8

---

## Problem Statement

Given a **row-wise sorted matrix** `mat[][]` of size `n*m`, where the number of rows and columns is always **odd**. Return the **median** of the matrix.

---

## Examples

### Example 1:

**Input:**

```
mat[][] = [[1, 3, 5],
           [2, 6, 9],
           [3, 6, 9]]
```

**Output:**

```
5
```

**Explanation:**
Sorting all matrix elements → `[1, 2, 3, 3, 5, 6, 6, 9, 9]`.
The median is `5`.

---

### Example 2:

**Input:**

```
mat[][] = [[2, 4, 9],
           [3, 6, 7],
           [4, 7, 10]]
```

**Output:**

```
6
```

**Explanation:**
Sorting all matrix elements → `[2, 3, 4, 4, 6, 6, 7, 7, 9, 10]`.
The median is `6`.

---

### Example 3:

**Input:**

```
mat = [[3], [4], [8]]
```

**Output:**

```
4
```

**Explanation:**
Sorting all matrix elements → `[3, 4, 8]`.
The median is `4`.

---

## Constraints

* `1 ≤ n, m ≤ 400`
* `1 ≤ mat[i][j] ≤ 2000`

---

## Expected Complexities

* **Time Complexity:** `O(n * log m * log(maxVal – minVal))`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Matrix
* Binary Search
* Data Structures
* Algorithms

---

## Related Articles

* [Find Median Row-Wise Sorted Matrix](https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/)

---

---

# 2) Explanation + Step‑by‑step Dry Run

### Key idea

* Each row is sorted, but rows are **not** globally merged/sorted.
* The median is the element at **index** `k = (n*m + 1)//2` (1‑based) when all elements are listed in non‑decreasing order (n\*m is odd per problem).
* Instead of flattening and sorting, we can **binary search on the value range** `[min_in_matrix, max_in_matrix]`.
  For a candidate value `mid`, count how many elements in the matrix are `<= mid` using `bisect_right` in each row (because each row is sorted).

  * If `count < k`, the median must be **bigger** → move `low = mid + 1`.
  * Else it could be the median or smaller → move `high = mid`.

This yields `O(n * log(maxVal-minVal) * log m)` time and `O(1)` extra space.

---

### Dry run (Example 1)

`mat = [[1,3,5], [2,6,9], [3,6,9]]`, `n=3, m=3`, `k=(9+1)//2=5`.

* `low = min(first elements) = min(1,2,3)=1`
  `high = max(last elements) = max(5,9,9)=9`
* Loop:

  1. `mid = (1+9)//2 = 5`
     Count `<= 5`:

     * Row1 `[1,3,5]` → `3`
     * Row2 `[2,6,9]` → `1`
     * Row3 `[3,6,9]` → `1`
       Total `= 5` (>= k) → `high = 5`
  2. `mid = (1+5)//2 = 3`
     Count `<= 3`:

     * Row1 → `2`, Row2 → `1`, Row3 → `1` → Total `4` (< k) → `low = 4`
  3. `mid = (4+5)//2 = 4`
     Count `<= 4`:

     * Row1 → `2`, Row2 → `1`, Row3 → `1` → Total `4` (< k) → `low = 5`

Stop when `low == high == 5` → **median = 5**.

---

# 3) Optimized Codes (Python)

### A) Optimal (Value‑space Binary Search + bisect)

```python
from bisect import bisect_right

class Solution:
    def median(self, mat):
        """
        Optimal median finder for a row-wise sorted matrix.

        Time:  O(n * log(maxVal-minVal) * log m)
               - For each probe (log range), we count <= mid via bisect in each row (log m)
        Space: O(1)
        """
        n = len(mat)
        m = len(mat[0])

        # 1) Search space is min of first column to max of last column
        low  = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        # 2) We want the 1-based index (n*m+1)//2
        need = (n * m + 1) // 2

        # 3) Binary search on value range
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid using row-wise bisect_right
            cnt = 0
            for row in mat:
                # bisect_right returns index to insert mid on right -> count of <= mid
                cnt += bisect_right(row, mid)

            # If not enough elements <= mid, median is larger
            if cnt < need:
                low = mid + 1
            else:
                high = mid

        return low  # or high (equal here)
```

### B) Brute Force (Flatten + Sort)

```python
class SolutionBrute:
    def median(self, mat):
        """
        Brute force for clarity.

        Steps:
        - Flatten all elements
        - Sort
        - Pick middle (since n*m is odd)

        Time:  O(n*m * log(n*m))
        Space: O(n*m)
        """
        flat = []
        for row in mat:
            flat.extend(row)
        flat.sort()
        return flat[len(flat)//2]
```

> (Optional) A middle‑ground approach is a **k‑way merge using a heap** (like merging k sorted lists), which is `O(n*m*log n)` and `O(n)` extra space — not as good as the value‑space binary search but better than a full sort for very wide matrices.

---

# 4) Interview Q\&A (most common)

**Q1. Why does binary search on values work here?**
Because each row is sorted, we can quickly count how many elements are `<= mid`. This count is monotonic in `mid`, allowing binary search on the value range.

**Q2. Why use `bisect_right` rather than `bisect_left`?**
We want **count of elements `<= mid`**, which is exactly the index returned by `bisect_right(row, mid)`.

**Q3. What are `low` and `high` in the search?**
`low = min(row[0])` across rows, and `high = max(row[-1])`. Any median must lie within this range.

**Q4. Why `(n*m + 1)//2` for the target index?**
For an odd number of elements, the median is the `(N+1)//2`‑th (1‑based) smallest element. With 0‑based indexing that equals `N//2`.

**Q5. What if rows were not sorted?**
Then neither count via bisect nor value‑space binary search would be valid. You’d have to flatten and sort (or use selection algorithms).

**Q6. How do duplicates affect correctness?**
No issue. Counting `<= mid` with `bisect_right` naturally includes duplicates, keeping monotonicity intact.

**Q7. Complexity benefits vs. brute force?**

* Brute: `O(nm log(nm))` time, `O(nm)` space.
* Binary search on values: `O(n * log(range) * log m)` time, `O(1)` space — excellent when matrix values are bounded and rows are wide.

**Q8. Can we do it without extra space?**
Yes — the optimal solution above uses `O(1)` extra space (ignoring loop variables).

---

---

Here you go — a **complete, runnable Python program** that:

* Implements the optimal value‑space binary search solution (and a brute‑force baseline for comparison).
* Shows **inline time/space complexity notes at each key step**.
* Runs a **main** that feeds inputs, prints outputs, and uses `timeit` to measure runtime.

---

```python
"""
Median in a Row-wise Sorted Matrix (n x m, n*m is odd)

Approach used below:
1) Optimal: Binary search on the VALUE range + per-row bisect_right counts.
   Time:  O(n * log(maxVal - minVal) * log m)
   Space: O(1)
2) Brute: Flatten + sort.
   Time:  O(n*m * log(n*m))
   Space: O(n*m)
"""

from bisect import bisect_right
import timeit

class Solution:
    def median(self, mat):
        """
        Optimal solution with value-space binary search.

        n := number of rows, m := number of columns
        Let need = (n*m + 1)//2 be the rank of the median (1-based).

        Steps:
        - low  = min of first elements across rows  (O(n))
        - high = max of last elements across rows   (O(n))
        - While low < high:
            mid = (low + high)//2
            count how many elements <= mid:
                For each row (sorted), use bisect_right(row, mid) -> O(log m)
            If count < need: low = mid + 1 else high = mid
        - Return low (== high), the median.

        Time per probe: O(n * log m)
        # of probes:     O(log (maxVal - minVal))
        Extra space:     O(1)
        """
        # --- Step 0: Guard (matrix assumed valid & odd count per problem)
        n = len(mat)                    # O(1)
        m = len(mat[0])                 # O(1)

        # --- Step 1: Find search range [low, high]
        # Time: O(n) to scan first & last column
        # Space: O(1)
        low  = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        # --- Step 2: Median rank (1-based)
        # Time: O(1) | Space: O(1)
        need = (n * m + 1) // 2

        # --- Step 3: Binary search on value domain
        # Time: O(log(range) * n * log m)
        while low < high:
            mid = (low + high) // 2     # O(1)
            # Count elements <= mid across rows using bisect_right
            # Time: O(n * log m) | Space: O(1)
            cnt = 0
            for row in mat:
                cnt += bisect_right(row, mid)

            # Maintain the smallest value whose count >= need
            if cnt < need:
                low = mid + 1           # O(1)
            else:
                high = mid              # O(1)

        return low                      # O(1) | Space: O(1)


class SolutionBrute:
    def median(self, mat):
        """
        Brute force baseline: flatten and sort.
        Time:  O(n*m * log(n*m))
        Space: O(n*m)
        """
        flat = []                       # O(1) start
        # Flatten: O(n*m) time, O(n*m) space
        for row in mat:
            flat.extend(row)
        # Sort: O(n*m * log(n*m)) time, O(1) extra (Timsort internal)
        flat.sort()
        # Middle (n*m is odd): O(1)
        return flat[len(flat) // 2]


# -------------------------
# Demo + timing with timeit
# -------------------------
def main():
    # Example 1
    mat1 = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9],
    ]
    # Example 2
    mat2 = [
        [2, 4, 9],
        [3, 6, 7],
        [4, 7, 10],
    ]
    # Example 3
    mat3 = [
        [3],
        [4],
        [8],
    ]

    sol = Solution()
    brute = SolutionBrute()

    print("=== Outputs ===")
    print("Matrix 1 median (optimal):", sol.median(mat1))   # Expected 5
    print("Matrix 1 median (brute)  :", brute.median(mat1))
    print("Matrix 2 median (optimal):", sol.median(mat2))   # Expected 6
    print("Matrix 2 median (brute)  :", brute.median(mat2))
    print("Matrix 3 median (optimal):", sol.median(mat3))   # Expected 4
    print("Matrix 3 median (brute)  :", brute.median(mat3))

    # ---------------- Timing ----------------
    # We time only the function call, not the setup/printing, using timeit.
    # (Repeat a few times and take the best for a fair single-run estimate.)
    setup_opt = (
        "from __main__ import Solution; "
        "sol=Solution(); "
        "mat=[[i for i in range(1,2001,2)] for _ in range(199)]"  # 199x1000 odd count
    )
    stmt_opt = "sol.median(mat)"
    t_opt = min(timeit.repeat(stmt=stmt_opt, setup=setup_opt, repeat=5, number=1))

    setup_brute = (
        "from __main__ import SolutionBrute; "
        "s=SolutionBrute(); "
        "mat=[[i for i in range(1,2001,2)] for _ in range(199)]"
    )
    stmt_brute = "s.median(mat)"
    t_brute = min(timeit.repeat(stmt=stmt_brute, setup=setup_brute, repeat=5, number=1))

    print("\n=== Timing (best of 5 single runs) ===")
    print(f"Optimal  : {t_opt:.6f} sec")
    print(f"Brute    : {t_brute:.6f} sec")

if __name__ == "__main__":
    main()
```

### Sample Output (will be similar)

```
=== Outputs ===
Matrix 1 median (optimal): 5
Matrix 1 median (brute)  : 5
Matrix 2 median (optimal): 6
Matrix 2 median (brute)  : 6
Matrix 3 median (optimal): 4
Matrix 3 median (brute)  : 4

=== Timing (best of 5 single runs) ===
Optimal  : 0.00xxx sec
Brute    : 0.0yzzz sec
```

(The exact times will vary by machine and Python version.)

---

## 6) Real‑World Use Cases (only the heavy‑hitters)

* **Analytics dashboards over sorted slices**: Finding median of KPIs when data is stored by partitioned, sorted rows (e.g., hourly buckets of sorted values).
* **Database engines**: Estimating quantiles/medians from sorted segments without materializing a global sort.
* **Image processing**: Median over structured, row‑wise sorted windows (e.g., pre‑sorted scans for robust filtering).
* **Streaming storage systems**: When rows are kept sorted in chunks (like SSTables), quickly approximating/querying medians using value‑space search.

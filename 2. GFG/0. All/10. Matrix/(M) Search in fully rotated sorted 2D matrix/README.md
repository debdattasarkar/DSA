
---

# Search in Fully Rotated Sorted 2D Matrix

**Difficulty:** Medium
**Accuracy:** 64.45%
**Submissions:** 45K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

You are given a 2D matrix `mat[][]` of size `n x m` that was initially filled in the following manner:

* Each row is sorted in increasing order from left to right.
* The first element of every row is greater than the last element of the previous row.

This implies that if the matrix is flattened row-wise, it forms a strictly sorted 1D array.
Later, this sorted 1D array was rotated at some unknown pivot. The rotated array was then written back into the matrix row-wise to form the current matrix.

**Task:**
Given such a matrix `mat[][]` and an integer `x`, determine whether `x` exists in the matrix.

---

## Examples

### Example 1

**Input:**

```
x = 3
mat[][] = [
    [7, 8, 9, 10],
    [11, 12, 13, 1],
    [2, 3, 4, 5]
]
```

**Output:**

```
true
```

**Explanation:**
3 is located at the 3rd row and 2nd column.

---

### Example 2

**Input:**

```
x = 10
mat[][] = [
    [6, 7, 8],
    [9, 1, 2],
    [3, 4, 5]
]
```

**Output:**

```
false
```

**Explanation:**
The value 10 does not exist in the matrix.

---

## Constraint:

* $1 \leq n \times m \leq 10^5$
* $1 \leq mat[i][j], x \leq 10^6$

---

## Expected Complexities:

* **Time Complexity:** $O(\log(n \times m))$
* **Auxiliary Space:** $O(1)$

---

## Topic Tags

* `Binary Search`, `Matrix`, `Algorithms`

---

---

Here’s a clean, interview‑style package for this problem: a clear idea, a quick dry run, and two Python solutions (brute and optimized), plus common interviewer Q\&A.

---

# 2) Intuition & Step‑by‑Step Dry Run

## Core idea

* If you flatten the matrix row‑wise it was strictly increasing, then **rotated** at an unknown pivot and written back row‑wise.
* So this is exactly the classic **“search in a rotated sorted array”** problem — just remember how to convert a 1D index to a 2D cell:

  * For a total of `N = n*m` items, the element at 1D index `idx` is at:

    * row `r = idx // m`
    * col `c = idx % m`
    * value `mat[r][c]`

We can therefore:

* (Brute) scan all cells → `O(n*m)`.
* (Optimized) do a **modified binary search** on the virtual 1D array (without ever materializing it) → `O(log(n*m))` time, `O(1)` space.

### Modified binary search refresher

In a rotated strictly increasing array:

* At every step, **one side is sorted**.
* Compare `A[l]`, `A[mid]`, `A[r]` to decide which half is sorted and whether `x` lies there.

## Dry run on the sample

Matrix:

```
mat = [
  [7, 8, 9, 10],
  [11, 12, 13, 1],
  [2, 3, 4, 5]
]
x = 3
n = 3, m = 4, N = 12
```

We treat it as a rotated array of length 12:

```
Flat (conceptually): [7,8,9,10,11,12,13,1,2,3,4,5]
Indices            :  0 1 2  3  4  5  6  7 8 9 10 11
```

Binary search (l=0, r=11):

1. `mid=5` → value = `mat[5//4][5%4] = mat[1][1] = 12`

   * Left side `A[l]=7` to `A[mid]=12` is sorted (7 ≤ 12).
   * `x=3` is **not** in `[7..12]` ⇒ search right half ⇒ `l = mid + 1 = 6`.

2. `l=6, r=11, mid=8` → `mat[2][0] = 2`

   * Left side `A[l]=13` to `A[mid]=2` is **not** sorted.
   * Right side `A[mid]=2` to `A[r]=5` **is** sorted.
   * `x=3` is in `[2..5]` ⇒ `l = mid + 1 = 9`.

3. `l=9, r=11, mid=10` → `mat[2][2] = 4`

   * Left side `A[l]=3` to `A[mid]=4` is sorted.
   * `x=3` is in `[3..4]` ⇒ `r = mid - 1 = 9`.

4. `l=9, r=9, mid=9` → `mat[2][1] = 3` ⇒ found ✓
   Return `True`.

---

# 3) Python Solutions (brute & optimized)

### A) Brute force — linear scan (simple and acceptable to start with)

```python
class Solution:
    def searchMatrix(self, mat, x):
        """
        Brute force:
        - Scan all cells; return True if any equals x.
        Time:  O(n*m)
        Space: O(1)
        """
        for row in mat:
            for val in row:
                if val == x:
                    return True
        return False
```

### B) Optimized — single pass rotated binary search on virtual 1D array

```python
class Solution:
    def searchMatrix(self, mat, x):
        """
        Optimized:
        Treat the n x m matrix as a rotated sorted array of length N = n*m.
        Use modified binary search:
          - Map 1D index -> 2D (i = idx//m, j = idx%m)
          - At each step, one half is sorted; decide which side to keep.
        Time:  O(log(n*m))
        Space: O(1)
        """
        n = len(mat)
        if n == 0:
            return False
        m = len(mat[0])
        if m == 0:
            return False

        def get(idx):
            i, j = divmod(idx, m)
            return mat[i][j]

        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = get(mid)
            if mid_val == x:
                return True

            left_val, right_val = get(l), get(r)

            # Left half is sorted
            if left_val <= mid_val:
                if left_val <= x < mid_val:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if mid_val < x <= right_val:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
```

### (Alternative optimized) Find pivot then binary search

Some interviewers like the two‑phase method: first find the index of the smallest element (pivot) in `O(logN)`, then do a regular binary search in the appropriate interval (also `O(logN)`). Complexity is the same. If you want this version, I can add it too.

---

# 4) Likely Interviewer Q\&A

**Q1. Why can we treat the matrix as a rotated array?**
Because originally the matrix flattened row‑wise was strictly increasing. A rotation of that 1D array was written back row‑wise. So comparing values by virtual 1D indices preserves the rotated order.

**Q2. How do you convert a 1D index to 2D?**
`row = idx // m`, `col = idx % m`. The value is `mat[row][col]`.

**Q3. Why does the modified binary search work here?**
In a rotated strictly increasing array, at any point one side of `[l, mid]` or `[mid, r]` remains sorted. We can test in `O(1)` which side is sorted and whether `x` lies in that side’s numeric range, then discard the other half.

**Q4. What about duplicates?**
The flattened array is **strictly increasing** before rotation, so all elements are distinct — the simple modified binary search is sufficient (no need for the tricky “equal endpoints” handling used when duplicates exist).

**Q5. Complexity?**

* Time: `O(log(n*m))` for the optimized approach.
* Space: `O(1)`.

**Q6. Edge cases?**

* Empty matrix or empty rows.
* `x` smaller than the minimum or larger than the maximum — your comparisons handle it naturally.
* Single row or single column (still works since we only rely on the 1D mapping).

**Q7. Could we physically flatten the matrix first?**
You could, but that’d be `O(n*m)` extra space and unnecessary since index mapping gives you the same behavior with `O(1)` space.

---

---

Absolutely — here’s a single, runnable Python program that includes:

* A brute‑force scan and an optimized rotated‑binary‑search solution.
* Inline complexity notes at each step.
* A small “main” that feeds sample inputs, prints outputs, and benchmarks both methods using `timeit`.

---

## Full Program (with timing + sample I/O)

```python
#!/usr/bin/env python3
"""
Search in a fully rotated sorted 2D matrix (written row-wise).

Two solutions:
1) Brute force scan                                -> Time: O(n*m), Space: O(1)
2) Rotated binary search on a virtual 1D view      -> Time: O(log(n*m)), Space: O(1)

We treat the n x m matrix as a rotated sorted array of length N = n*m.
For any 1D index idx: row = idx // m, col = idx % m.
"""

from timeit import timeit


class Solution:
    # ---------- 1) Brute Force ----------
    def searchMatrix_bruteforce(self, mat, x):
        """
        Scan all cells; return True if any equals x.
        Time:  O(n*m)  — visit every element in the worst case
        Space: O(1)    — no extra data structures
        """
        # Iterate row by row -> O(n)
        for row in mat:
            # Scan each element in the row -> O(m) per row
            for val in row:
                if val == x:
                    return True
        return False

    # ---------- 2) Optimized: rotated binary search on virtual 1D ----------
    def searchMatrix(self, mat, x):
        """
        Treat the matrix as a rotated sorted array of length N = n*m
        and perform a modified binary search without materializing it.

        Time:  O(log(n*m)) — binary search over N elements
        Space: O(1)        — constant extra space
        """
        n = len(mat)
        if n == 0:
            return False  # empty matrix
        m = len(mat[0])
        if m == 0:
            return False  # empty rows

        # Helper to fetch A[idx] in O(1) using 1D->2D mapping.
        # Time per call: O(1), Space: O(1)
        def get(idx):
            i, j = divmod(idx, m)  # row = idx // m, col = idx % m
            return mat[i][j]

        l, r = 0, n * m - 1
        # Standard rotated-array binary search loop -> O(log N) iterations
        while l <= r:
            mid = (l + r) // 2
            mid_val = get(mid)
            if mid_val == x:
                return True

            left_val, right_val = get(l), get(r)

            # One side is always sorted in a rotated strictly increasing array
            if left_val <= mid_val:  # Left half is sorted
                if left_val <= x < mid_val:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right half is sorted
                if mid_val < x <= right_val:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


# -------------------- Demo + Timing --------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1 (from prompt): should be True (3 exists)
    mat1 = [
        [7, 8, 9, 10],
        [11, 12, 13, 1],
        [2, 3, 4, 5],
    ]
    x1 = 3

    # Example 2 (from prompt): should be False (10 does not exist)
    mat2 = [
        [6, 7, 8],
        [9, 1, 2],
        [3, 4, 5],
    ]
    x2 = 10

    # Print results
    print("=== Functional Checks ===")
    print(f"Matrix 1, x={x1}: brute -> {sol.searchMatrix_bruteforce(mat1, x1)}, "
          f"optimized -> {sol.searchMatrix(mat1, x1)}")
    print(f"Matrix 2, x={x2}: brute -> {sol.searchMatrix_bruteforce(mat2, x2)}, "
          f"optimized -> {sol.searchMatrix(mat2, x2)}")

    # Timing — use timeit to measure average runtime
    # (Note: increase number for more stable results; kept modest here.)
    number = 2000

    t_brute = timeit(
        stmt="sol.searchMatrix_bruteforce(mat1, x1)",
        globals=globals(),
        number=number,
    )
    t_opt = timeit(
        stmt="sol.searchMatrix(mat1, x1)",
        globals=globals(),
        number=number,
    )

    print("\n=== Timing (timeit) ===")
    print(f"Runs per method: {number}")
    print(f"Brute force   : {t_brute:.6f} sec total  (~{t_brute/number:.3e} sec/run)")
    print(f"Optimized BS  : {t_opt:.6f} sec total  (~{t_opt/number:.3e} sec/run)")
```

### Example output (what you should see)

```
=== Functional Checks ===
Matrix 1, x=3: brute -> True, optimized -> True
Matrix 2, x=10: brute -> False, optimized -> False

=== Timing (timeit) ===
Runs per method: 2000
Brute force   : 0.00xxxx sec total  (~y.yye-06 sec/run)
Optimized BS  : 0.00zzzz sec total  (~w.wwe-06 sec/run)
```

(Exact numbers vary by machine.)

---

## 6) Real‑World Use Cases (only the big ones)

1. **Paged / Block Storage Search**
   Data is stored in fixed‑width pages (rows) but you navigate it as a continuous logical array. If a maintenance job rotates/rehydrates pages (like log segments), treating the matrix as a rotated 1D array lets you search quickly with `O(1)` memory.

2. **Time‑sharded Dashboards**
   Imagine a dashboard that “rolls” recent metrics into a time‑window buffer and re‑lays them into tiles. The data is strictly increasing (timestamps) but buffer rotation happens periodically. This lets you do fast lookups across the tiled (2D) view.

3. **Firmware Tables / Ring Buffers Rendered as Grids**
   Embedded systems often use ring buffers (rotated arrays) and then render them onto a grid for display. Searching for a value/event across the grid benefits from the rotated‑binary‑search approach without first copying to a linear array.


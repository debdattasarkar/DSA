# Sorted Matrix

**Difficulty:** Basic
**Accuracy:** 63.49%
**Submissions:** 60K+
**Points:** 1

---

## 🧩 Problem Statement

Given an NxN matrix **Mat**, sort all elements of the matrix in ascending order.

---

## 🧠 Examples

### Example 1

**Input:**

```
N = 4  
Mat = [
  [10, 20, 30, 40],
  [15, 25, 35, 45],
  [27, 29, 37, 48],
  [32, 33, 39, 50]
]
```

**Output:**

```
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
```

**Explanation:**
Sorting all elements of the matrix gives the above result.

---

### Example 2

**Input:**

```
N = 3  
Mat = [
  [1, 5, 3],
  [2, 8, 7],
  [4, 6, 9]
]
```

**Output:**

```
1 2 3
4 5 6
7 8 9
```

**Explanation:**
Sorting all elements of the matrix gives this result.

---

## 🎯 Your Task

You don't need to read input or print anything.
Your task is to complete the function **`sortedMatrix()`**,
which takes the integer **N** and the matrix **Mat** as input parameters
and returns the sorted matrix.

---

## ⏱️ Expected Complexities

| Metric              | Complexity  |
| ------------------- | ----------- |
| **Time Complexity** | O(N² log N) |
| **Auxiliary Space** | O(N²)       |

---

## ⚙️ Constraints

* 1 ≤ N ≤ 1000
* 1 ≤ Mat[i][j] ≤ 10⁵

---

## 🏢 Company Tags

Amazon, FactSet

---

## 🧱 Topic Tags

Matrix, Data Structures

---

## 📘 Related Articles

* Print Elements Sorted Order Row Wise Column Wise Sorted Matrix
* Sort Given Matrix

---

---

Got it! Let’s make “Sorted Matrix” interview-ready.

---

## 2) Intuition + step-by-step dry run

### Goal

Given an `N x N` matrix `Mat`, return a matrix where **all N² elements are in ascending order row-wise**, i.e., after sorting the entire collection of values, we refill the matrix row by row.

### Most direct idea (what interviewers expect)

1. **Flatten** all elements into a list of length `N²`.
2. **Sort** that list.
3. **Refill** the matrix row by row from the sorted list.

This hits the expected bounds: **Time O(N² log N)**, **Aux space O(N²)**.

### Dry run (Example 2)

```
N = 3
Mat =
[
  [1, 5, 3],
  [2, 8, 7],
  [4, 6, 9]
]
```

1. Flatten → `arr = [1,5,3,2,8,7,4,6,9]`
2. Sort   → `arr = [1,2,3,4,5,6,7,8,9]`
3. Refill row-wise:

```
row 0: 1 2 3
row 1: 4 5 6
row 2: 7 8 9
```

Done.

---

## 3) Python solutions (brute/simple + alternatives)

All solutions fit your required signature.

### A) ✅ Canonical solution (flatten → sort → refill)

* Easiest to write and reason about.
* Matches the problem’s expected complexity.

```python
# User function Template for python3
class Solution:
    def sortedMatrix(self, N, Mat):
        """
        Flatten all N^2 elements, sort them, and refill row-wise.
        Time  : O(N^2 log N)          (sorting N^2 numbers)
        Space : O(N^2)                (flattened array)
        """
        # 1) Flatten
        flat = []
        for r in range(N):
            # append row to flat; each push is O(1)
            flat.extend(Mat[r])

        # 2) Sort the whole list
        flat.sort()  # Timsort: O(N^2 log N)

        # 3) Refill row-wise
        idx = 0
        for r in range(N):
            for c in range(N):
                Mat[r][c] = flat[idx]
                idx += 1

        return Mat
```

---

### B) Counting/Bucket approach (when values are small & bounded)

* Constraint: `1 ≤ Mat[i][j] ≤ 1e5`.
* Theoretical complexity: **O(N² + U)** where `U` is value range.
* In Python, a dense list of size `1e5+1` is fine, but uses memory; still ok for this constraint.

```python
class SolutionCounting:
    def sortedMatrix(self, N, Mat):
        """
        Counting/bucket style when values are bounded (1..1e5).
        Time  : O(N^2 + U)   (U = 1e5)
        Space : O(U)
        """
        MAXV = 10**5
        cnt = [0] * (MAXV + 1)  # O(U) memory

        # Count frequencies: O(N^2)
        for r in range(N):
            for v in Mat[r]:
                cnt[v] += 1

        # Refill the matrix from counts: O(N^2 + U)
        r = c = 0
        for val in range(1, MAXV + 1):
            freq = cnt[val]
            while freq > 0:
                Mat[r][c] = val
                c += 1
                if c == N:
                    c = 0
                    r += 1
                freq -= 1
        return Mat
```

> Use this only if interviewer **explicitly** wants to exploit bounded values. Otherwise, stick to the simple flatten-sort.

---

### C) Min-heap of all elements (not preferred here, but instructive)

* Push all N² elements into a min-heap, then pop back into matrix.
* Complexity **O(N² log N²)** ~ **O(N² log N)** same as sorting, but with larger constants than Timsort.

```python
import heapq

class SolutionHeapAll:
    def sortedMatrix(self, N, Mat):
        """
        Heapify all elements then pop in order.
        Time  : O(N^2 log N) (actually log(N^2) = 2 log N)
        Space : O(N^2)
        """
        heap = []
        for r in range(N):
            for v in Mat[r]:
                heapq.heappush(heap, v)
        for r in range(N):
            for c in range(N):
                Mat[r][c] = heapq.heappop(heap)
        return Mat
```

> If the matrix had a **special structure** (e.g., rows and columns individually sorted), you’d use a **k-way merge** heap of size `N` (better than heap of N²). But this problem statement doesn’t assume that.

---

## 4) Interview cheat-sheet + Q&A

### 10-second game plan (say this out loud)

> “I’ll flatten all N² elements, sort once (O(N² log N)), and write back row-wise. Space is O(N²) for the flat list. If we must use O(1) extra space, we can do an in-place sort of the flattened view, but Python lists already sort in place.”

### Likely questions

**Q1. Why not sort each row/column individually?**
Because the problem wants all N² elements globally sorted. Sorting per row/column doesn’t guarantee global order.

**Q2. Can you do better than O(N² log N)?**
If values are small/bounded, counting sort can do **O(N² + U)**. If the matrix were already row/col sorted, a **k-way merge** heap of size N would be **O(N² log N)** but with better constants than pushing N² items.

**Q3. Space optimization?**
You can conceptually flatten indices and sort “in place” (treat `Mat[i][j]` as a single array via index math). In Python, simplest is still flatten to a list and sort; in C++ you could do true in-place with index mapping.

**Q4. Stability needed?**
Not relevant; we’re sorting numbers and only the final order matters.

**Q5. Why choose sorting over heap?**
Timsort is extremely optimized in Python; `flat.sort()` is simple and fast with the same big-O but smaller constants than pushing N² heap operations.

---

### Mini mnemonic

> **“Flat → Sort → Fill.”**
> Flatten the matrix, sort the flat list, fill back row-wise.

---

---

Awesome—let’s wrap this up with (5) tight, interview-friendly **real-world use cases**, then (6) a **complete, runnable Python program** that solves *Sorted Matrix*, prints results for sample inputs, and measures runtime using `timeit`.

---

## 5) Real-World Use Cases (easy to relate)

* **Heatmaps / dashboards:**
  You’ve got an (N \times N) grid of KPI values. To show ranks or to normalize thresholds, you first **sort all cells globally** and then map percentiles back to the grid.

* **Image / raster preprocessing:**
  For grayscale image tiles (pixel intensities in a tile), global sort supports contrast-stretching or quantile binning before further analytics.

* **Geo-grids (spatial analytics):**
  Each cell is a region’s metric (e.g., demand/sales). Sorting the entire grid globally helps compute **cutoffs** (top-k%, quartiles) and then refilling row-wise for visualization/serialization.

* **Batch ranking for resource allocation:**
  Matrix encodes (team × project) scores. A full global sort yields a **priority queue** of all opportunities; after sorting you can refill to keep a canonical, row-wise order for storage or export.

> Sound bite to say: **“When I need global order across a 2-D grid—percentiles, cutoffs, or canonical serialization—I just flatten → sort → refill.”**

---

## 6) Full Program (with inline complexity notes + timing)

This script:

* Implements the canonical **flatten → sort → refill** solution (`O(N^2 log N)` time, `O(N^2)` space).
* Also shows a **counting/bucket** variant useful when values are bounded.
* Runs the **two sample test cases** from the prompt.
* Measures runtime using both `perf_counter` (single run) and `timeit` (average of 5 runs).

> Run it as-is with Python 3.

```python
#!/usr/bin/env python3
"""
Sorted Matrix
-------------
Given an N x N matrix, sort *all* N^2 elements and write them back row-wise.

Core approach (interview-standard):
  1) Flatten all elements to a list                -> O(N^2) time, O(N^2) space
  2) Sort the list                                  -> O(N^2 log N)
  3) Refill the matrix row-wise                    -> O(N^2)

Total complexity:
  Time  : O(N^2 log N)
  Space : O(N^2)   (for the flattened list)
"""

from time import perf_counter
import timeit
from copy import deepcopy

# ------------------ Solution (flatten -> sort -> refill) ------------------ #
class Solution:
    def sortedMatrix(self, N, Mat):
        """
        Flatten all elements, sort once, refill row-wise.

        Time  : O(N^2 log N)  (sorting N^2 items)
        Space : O(N^2)        (aux list with N^2 elements)
        """
        # 1) Flatten: O(N^2) time, O(N^2) space
        flat = []
        for r in range(N):
            flat.extend(Mat[r])  # appends row items; each append is O(1) amortized

        # 2) Sort: O(N^2 log N) time, in-place list sort (Timsort)
        flat.sort()

        # 3) Refill: O(N^2) time, O(1) extra
        idx = 0
        for r in range(N):
            for c in range(N):
                Mat[r][c] = flat[idx]
                idx += 1

        return Mat


# --------------- Optional: Counting/bucket (bounded values) --------------- #
class SolutionCounting:
    def sortedMatrix(self, N, Mat, max_value=10**5):
        """
        Counting style when values are bounded in [0..max_value] or [1..max_value].

        Time  : O(N^2 + U)   where U = max_value
        Space : O(U)
        """
        # Count: O(N^2)
        freq = [0] * (max_value + 1)
        for r in range(N):
            for v in Mat[r]:
                freq[v] += 1

        # Refill: O(N^2 + U)
        r = c = 0
        for val in range(max_value + 1):
            f = freq[val]
            while f > 0:
                Mat[r][c] = val
                c += 1
                if c == N:
                    c = 0
                    r += 1
                f -= 1
        return Mat


# ------------------------------ Utilities --------------------------------- #
def print_matrix(M):
    for row in M:
        print(*row)

def solve_and_time(solver, N, Mat):
    """Run once with perf_counter; return result and elapsed time."""
    mat_copy = deepcopy(Mat)  # keep original for fair timing
    t0 = perf_counter()
    out = solver.sortedMatrix(N, mat_copy)
    t1 = perf_counter()
    return out, (t1 - t0)

def avg_time(solver, N, Mat, runs=5):
    """Average time using timeit; rebuild inputs per run to be fair."""
    def run_once():
        m = deepcopy(Mat)
        solver.sortedMatrix(N, m)
    return timeit.timeit(run_once, number=runs) / runs


# --------------------------------- Main ----------------------------------- #
if __name__ == "__main__":
    # -------- Example 1 (from prompt) --------
    N1 = 4
    Mat1 = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]

    # -------- Example 2 (from prompt) --------
    N2 = 3
    Mat2 = [
        [1, 5, 3],
        [2, 8, 7],
        [4, 6, 9]
    ]

    sol = Solution()

    # --- Example 1: single-run timing + output ---
    out1, t1 = solve_and_time(sol, N1, Mat1)
    print("Example 1 output:")
    print_matrix(out1)
    print(f"Single-run time: {t1:.6f} s")

    # --- Example 1: average over 5 runs ---
    avg1 = avg_time(sol, N1, Mat1, runs=5)
    print(f"Avg over 5 runs: {avg1:.6f} s\n")

    # --- Example 2: single-run timing + output ---
    out2, t2 = solve_and_time(sol, N2, Mat2)
    print("Example 2 output:")
    print_matrix(out2)
    print(f"Single-run time: {t2:.6f} s")

    # --- Example 2: average over 5 runs ---
    avg2 = avg_time(sol, N2, Mat2, runs=5)
    print(f"Avg over 5 runs: {avg2:.6f} s\n")

    # Complexity recap (nice to print for interviews)
    print("Complexity:")
    print("  Time  : O(N^2 log N)")
    print("  Space : O(N^2)")
```

### Expected outputs (from the prompt)

**Example 1**

```
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
```

**Example 2**

```
1 2 3
4 5 6
7 8 9
```

*(The exact times depend on your machine; the script prints both a single run and the average of 5 runs.)*

---

### Interview mini-recall (to say before coding)

* **Plan:** “I’ll **flatten → sort → refill**. That’s (O(N^2 \log N)) time and (O(N^2)) space. If values are bounded, a **counting/bucket** approach is (O(N^2 + U)).”
* **Why sorting (not heap)?** Python’s Timsort is highly optimized; sorting once has the same big-O as pushing/popping (N^2) elements into a heap but with smaller constants and cleaner code.


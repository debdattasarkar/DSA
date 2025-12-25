# Find the Peak Element in a 2D Matrix

**Difficulty:** Medium
**Accuracy:** 36.8%
**Submissions:** 3K+
**Points:** 4

---

## Problem Statement

Given a 2D matrix `mat[][]`, identify any **peak element** within the matrix.

An element is considered a **peak** if it is **greater than or equal to** its **four immediate neighbors**: **top, bottom, left, and right**. For **corner and edge** elements, any **missing neighbors** are treated as having a value of **negative infinity**.

---

## Note

* A peak element is **not necessarily** the global maximum; it only needs to satisfy the condition relative to its **adjacent** elements.
* **Multiple peak elements** may exist, return **any one** of them.
* Note that the **driver code** will print **true** if you return the correct **position** of peak element, else it will print **false**.

---

## Examples

### Example 1

**Input:**
`mat[][] = [[10, 20, 15],               [21, 30, 14],               [7, 16, 32]]`

**Output:** `true`

**Explanation:**
One of the peak element is `30` at index `(1, 1)`, which is greater than or equal to all its valid neighbors:
`Left = 21, Right = 14, Top = 20, Bottom = 16`.
So, it satisfies the peak condition. Alternatively, `(2, 2)` with value `32` also qualifies as a peak.

---

### Example 2

**Input:**
`mat[][] = [[17, 7],               [11, 10]]`

**Output:** `true`

**Explanation:**
`17` is the only peak element at index `(0, 0)`. Its neighbors are: `Right = 7, Bottom = 11`.
Since `17` is greater than or equal to both (and top/left are out of bounds), it qualifies as a peak element.

---

## Constraint

* `1 ≤ n × m ≤ 10^6`
* `-10^6 ≤ mat[i][j] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n log m)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Binary Search
* Matrix
* Algorithms

---

## Related Articles

* Find Peak Element 2d Array

---

---

## 2) Text explanation + step-by-step dry run

### What is a “peak” here?

Cell `(r, c)` is a **peak** if:

`mat[r][c] >=` its **top**, **bottom**, **left**, **right** neighbors.

If a neighbor is out of bounds (edge/corner), treat it as `-∞` (so edges can be peaks easily).

---

## Key interview idea (optimized)

### Column Binary Search (Expected: `O(n log m)`)

We do binary search on **columns**:

1. Pick middle column `mid_col`.
2. Find the **row index of the maximum element** in that column (scan all rows).

   * Let it be `best_row`.
   * Now `mat[best_row][mid_col]` is **>= top and bottom neighbors** automatically (because it’s the max in that column).
3. Compare only **left** and **right** neighbors:

   * If it’s `>= left` and `>= right` → it’s a peak ✅
   * Else move to the side that has the **strictly bigger** neighbor:

     * If `right > current` → search right half
     * Else if `left > current` → search left half

This works because if a neighbor is larger, a peak must exist in that direction (classic 2D peak argument).

---

## Dry run (Example 1)

Matrix:

```
[ [10, 20, 15],
  [21, 30, 14],
  [ 7, 16, 32] ]
```

`n=3, m=3`

### Step 1

* `left_col=0, right_col=2`
* `mid_col = (0+2)//2 = 1` (middle column is col=1)

Column 1 values: `[20, 30, 16]`

* Max is `30` at `best_row=1`

Current = `mat[1][1] = 30`

* left neighbor = `mat[1][0] = 21`
* right neighbor = `mat[1][2] = 14`

Check:

* `30 >= 21` ✅
* `30 >= 14` ✅
  And since it’s max in the column:
* `30 >= top(20)` ✅
* `30 >= bottom(16)` ✅

So `(1,1)` is a peak → return `[1, 1]`.

Done.

---

# 3) Python codes (brute + interview-expected optimized)

### A) Brute force (easy, very clear) — `O(n*m)`

Scan every cell and check its 4 neighbors.

```python
class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # Helper to safely get value or -infinity if out of bounds
        def get_value(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return mat[r][c]
            return float("-inf")
        
        for r in range(rows):
            for c in range(cols):
                current = mat[r][c]
                top = get_value(r - 1, c)
                bottom = get_value(r + 1, c)
                left = get_value(r, c - 1)
                right = get_value(r, c + 1)
                
                # Peak condition (>= all four neighbors)
                if current >= top and current >= bottom and current >= left and current >= right:
                    return [r, c]
        
        # Problem guarantees existence of a peak in typical settings,
        # but return something safe if needed.
        return [-1, -1]
```

---

### B) Optimized (most expected in interviews): Column Binary Search — `O(n log m)`

```python
class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        left_col = 0
        right_col = cols - 1
        
        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            
            # 1) Find the row having maximum value in mid_col
            best_row = 0
            for r in range(1, rows):
                if mat[r][mid_col] > mat[best_row][mid_col]:
                    best_row = r
            
            current = mat[best_row][mid_col]
            
            # 2) Compare with left and right neighbors (out of bounds => -inf)
            left_neighbor = mat[best_row][mid_col - 1] if mid_col - 1 >= 0 else float("-inf")
            right_neighbor = mat[best_row][mid_col + 1] if mid_col + 1 < cols else float("-inf")
            
            # 3) If current is >= both, it's a peak
            if current >= left_neighbor and current >= right_neighbor:
                return [best_row, mid_col]
            
            # 4) Move towards the bigger neighbor
            if right_neighbor > current:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1
        
        return [-1, -1]
```

---

### C) Same optimized idea, but choose direction to minimize work (binary search on smaller dimension)

This can be handy in interviews to show “extra thought”:

* If `cols` is smaller → binary search columns (scan rows each step)
* If `rows` is smaller → binary search rows (scan cols each step)

Worst-case becomes `O(min(rows, cols) * log(max(rows, cols)))`.

```python
class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # If columns are fewer, do column-binary-search (scan rows).
        if cols <= rows:
            left_col, right_col = 0, cols - 1
            while left_col <= right_col:
                mid_col = (left_col + right_col) // 2
                
                # max in mid_col
                best_row = 0
                for r in range(1, rows):
                    if mat[r][mid_col] > mat[best_row][mid_col]:
                        best_row = r
                
                current = mat[best_row][mid_col]
                left_neighbor = mat[best_row][mid_col - 1] if mid_col > 0 else float("-inf")
                right_neighbor = mat[best_row][mid_col + 1] if mid_col + 1 < cols else float("-inf")
                
                if current >= left_neighbor and current >= right_neighbor:
                    return [best_row, mid_col]
                
                if right_neighbor > current:
                    left_col = mid_col + 1
                else:
                    right_col = mid_col - 1
        else:
            # Row-binary-search (scan cols)
            top_row, bottom_row = 0, rows - 1
            while top_row <= bottom_row:
                mid_row = (top_row + bottom_row) // 2
                
                # max in mid_row
                best_col = 0
                for c in range(1, cols):
                    if mat[mid_row][c] > mat[mid_row][best_col]:
                        best_col = c
                
                current = mat[mid_row][best_col]
                up_neighbor = mat[mid_row - 1][best_col] if mid_row > 0 else float("-inf")
                down_neighbor = mat[mid_row + 1][best_col] if mid_row + 1 < rows else float("-inf")
                
                if current >= up_neighbor and current >= down_neighbor:
                    return [mid_row, best_col]
                
                if down_neighbor > current:
                    top_row = mid_row + 1
                else:
                    bottom_row = mid_row - 1
        
        return [-1, -1]
```

---

# 4) Interview: how to remember + expected Q&A

## How to remember quickly (mental script)

Think:

**“Binary search on columns. In mid column, pick the max row. Compare left/right. Move to bigger side.”**

Shortcut mantra:
**“Mid column → column max → check sides → go bigger side.”**

Why column max?
Because it automatically beats **top/bottom**, so only **left/right** matter.

---

## Common interviewer questions + strong answers

### Q1. What is a peak in 2D?

**A.** A cell that is `>=` its immediate neighbors: top, bottom, left, right. Missing neighbors are treated as `-∞`.

---

### Q2. Why does picking the maximum in the middle column help?

**A.** If the chosen cell is the maximum in its column, then it is already `>=` its top and bottom neighbors. So we only need to compare with left and right to decide if it’s a peak.

---

### Q3. Why is binary search valid here?

**A.** If the right neighbor is bigger than the current candidate, then there must exist a peak in the right half (values are “rising” in that direction). Similarly, if left neighbor is bigger, a peak exists in the left half. So we can safely discard half the columns each step.

---

### Q4. What’s the time complexity of the optimized approach?

**A.**

* Each iteration: scan `n` rows to find max in a column → `O(n)`
* Number of iterations: `log m`
  So total: **`O(n log m)`**, space **`O(1)`**.

---

### Q5. What about edges/corners?

**A.** Missing neighbors are treated as `-∞`, so comparisons work naturally. In code we handle out-of-bounds by using `-inf`.

---

### Q6. What if there are equal values (plateaus)?

**A.** Condition is `>=`, so equal neighbors are fine. In movement step, we only move when a neighbor is **strictly greater**; otherwise current qualifies as peak.

---

### Q7. Can there be multiple peaks? Which one do we return?

**A.** Yes, multiple peaks may exist; return **any** one. The algorithm returns the first peak it finds by its search path.

---

---

## 5) Real-world use cases (few, high-signal)

1. **Heatmaps / monitoring dashboards (CPU, latency, traffic grids)**
   Finding a *local hotspot* (peak) in a 2D heatmap of server racks, microservices, or geo-traffic without scanning the entire grid repeatedly.

2. **Image processing (bright spot / blob detection)**
   In an intensity matrix (grayscale image), a peak corresponds to a local maximum—useful for detecting highlights, stars in astronomy images, microscope bright regions, etc.

3. **Terrain / elevation grids (GIS)**
   A peak element is a local “hilltop” in a digital elevation model—useful for ridge detection, watershed computations, or navigation heuristics.

4. **Sensor arrays (thermal cameras, pressure mats)**
   Spot the maximum response region (hot object on thermal grid, pressure point on a mat) quickly as data streams in.

---

## 6) Full Python program (with inline complexity notes + timed run)

* Uses the **optimized column binary search** (`O(n log m)` time, `O(1)` extra space).
* Reads input in a common competitive format:

  * Either:

    * `T` testcases
    * For each testcase: `n m` then `n*m` integers
  * Or if `T` is not present, it also works with a single testcase `n m` then matrix.

> Note: Printing runtime is great for demos/interviews. In actual online judges, you’d remove the runtime print.

```python
import sys
import time

class Solution:
    def findPeakGrid(self, mat):
        """
        Optimized approach: Binary search on columns
        Overall Time: O(rows * log(cols))
        Extra Space: O(1)
        """
        rows = len(mat)
        cols = len(mat[0])

        left_col = 0
        right_col = cols - 1

        # While loop runs O(log cols) times (binary search on columns)
        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2  # O(1)

            # Step 1: find row index of maximum element in mid_col
            # Time: O(rows) for scanning all rows in this column
            best_row = 0
            for r in range(1, rows):
                if mat[r][mid_col] > mat[best_row][mid_col]:
                    best_row = r

            current = mat[best_row][mid_col]  # O(1)

            # Step 2: compare with left and right neighbors
            # Out-of-bounds treated as -inf => handled with float("-inf")
            left_neighbor = mat[best_row][mid_col - 1] if mid_col > 0 else float("-inf")   # O(1)
            right_neighbor = mat[best_row][mid_col + 1] if mid_col + 1 < cols else float("-inf")  # O(1)

            # Step 3: if current >= left and >= right, it's a peak
            # (Since it's max in column => automatically >= top and bottom)
            if current >= left_neighbor and current >= right_neighbor:
                return [best_row, mid_col]  # O(1)

            # Step 4: move towards the larger neighbor
            # O(1) decision, reduces search space by half
            if right_neighbor > current:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1

        # Theoretical fallback (usually not reached with typical constraints)
        return [-1, -1]


def read_all_ints():
    """Read all integers from stdin fast. Time: O(total_tokens). Space: O(total_tokens)."""
    data = sys.stdin.buffer.read().split()
    return list(map(int, data))


def parse_input(tokens):
    """
    Supports two formats:
    1) T, then for each test: n m, then n*m values
    2) Single test: n m, then n*m values
    """
    idx = 0
    if len(tokens) < 2:
        return []

    # Try interpret first number as T if it matches remaining structure.
    # If not, treat as single test.
    possible_t = tokens[idx]
    idx += 1

    tests = []

    def can_parse_t_tests(t, start_idx):
        j = start_idx
        for _ in range(t):
            if j + 1 >= len(tokens):
                return False
            n = tokens[j]; m = tokens[j + 1]
            j += 2
            need = n * m
            if j + need > len(tokens):
                return False
            j += need
        return j == len(tokens)

    # Decide format
    if possible_t >= 1 and can_parse_t_tests(possible_t, idx):
        t = possible_t
        for _ in range(t):
            n = tokens[idx]; m = tokens[idx + 1]
            idx += 2
            flat = tokens[idx: idx + n * m]
            idx += n * m
            mat = [flat[r * m:(r + 1) * m] for r in range(n)]
            tests.append(mat)
    else:
        # single test: first number was actually n
        n = possible_t
        m = tokens[idx]
        idx += 1
        flat = tokens[idx: idx + n * m]
        mat = [flat[r * m:(r + 1) * m] for r in range(n)]
        tests.append(mat)

    return tests


def main():
    # Full program timing start
    program_start = time.perf_counter()

    tokens = read_all_ints()
    tests = parse_input(tokens)

    solver = Solution()

    # Process each test case
    # Total time across tests: sum of O(rows * log(cols)) per test
    outputs = []
    for mat in tests:
        peak_pos = solver.findPeakGrid(mat)
        outputs.append(peak_pos)

    # Print outputs (one line per test)
    for pos in outputs:
        print(pos[0], pos[1])

    # Full program timing end
    program_end = time.perf_counter()
    total_ms = (program_end - program_start) * 1000.0

    # Runtime print (great for demo; remove for online judges)
    print(f"TotalRuntimeMs: {total_ms:.3f}", file=sys.stderr)


if __name__ == "__main__":
    main()
```

### Sample Input

```
2
3 3
10 20 15
21 30 14
7 16 32
2 2
17 7
11 10
```

### Sample Output (one valid possibility)

```
1 1
0 0
```

(Your output may differ but should still be a valid peak position.)

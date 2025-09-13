
# Spirally traversing a matrix

**Difficulty:** Medium
**Accuracy:** 35.2%
**Submissions:** 331K+
**Points:** 4

---

You are given a rectangular matrix `mat[][]` of size `n x m`, and your task is to return an array while **traversing the matrix in spiral form**.

---

## Examples

### Example 1

**Input:**
`mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]`
**Output:**
`[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]`
**Explanation:** Spiral order as shown in the diagram: right → down → left → up, shrinking the boundaries each layer.

---

### Example 2

**Input:**
`mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]`
**Output:**
`[1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]`
**Explanation:** Apply the same spiral technique.

---

### Example 3

**Input:**
`mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]`
**Output:**
`[32, 44, 27, 23, 62, 50, 28, 54]`
**Explanation:** Apply the same spiral technique.

---

## Constraints

* `1 ≤ n, m ≤ 1000`
* `0 ≤ mat[i][j] ≤ 100`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)` (for the returned traversal list)

---

## Company Tags

Paytm, Flipkart, Morgan Stanley, Microsoft, OYO Rooms, Snapdeal, D-E-Shaw, MakeMyTrip, Oracle, MAQ Software, Adobe, nearby, Nagarro, BrowserStack, Salesforce, Zoho

---

## Topic Tags

Arrays, Matrix, Data Structures

---

## Related Interview Experiences

* Paytm Interview Experience Set 14 For Senior Android Developer
* Makemytrip Interview Experience Set 6 Online Coding
* Microsoft Interview Experience For SDE 1/2
* Adobe Interview Experience SheCodes Software Engineer
* Adobe Interview Questions Computer Scientist

---

## Related Articles

* [Print A Given Matrix In Spiral Form](https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/)


---

---

Here’s the clean, interview-ready package for **Spiral Traversal of a Matrix**.

---

## 2) Intuition + Step-by-Step Dry Run

### Core idea (layer/peel technique)

Keep four boundaries:

* `top` (first row not yet traversed),
* `bottom` (last row not yet traversed),
* `left` (first column not yet traversed),
* `right` (last column not yet traversed).

Traverse:

1. Left → Right along `top`, then `top += 1`
2. Top → Bottom along `right`, then `right -= 1`
3. Right → Left along `bottom` (only if `top ≤ bottom`), then `bottom -= 1`
4. Bottom → Top along `left` (only if `left ≤ right`), then `left += 1`
   Repeat while `top ≤ bottom` and `left ≤ right`.

This peels the matrix one rectangular “ring” at a time.

### Dry run on

```
mat = [
  [ 1,  2,  3,  4],
  [ 5,  6,  7,  8],
  [ 9, 10, 11, 12],
  [13, 14, 15, 16]
]
```

Initialize: `top=0, bottom=3, left=0, right=3`, `ans=[]`

* Row `top=0` L→R: 1,2,3,4 → ans=\[1,2,3,4], `top=1`
* Col `right=3` T→B: 8,12,16 → ans=\[1,2,3,4,8,12,16], `right=2`
* Row `bottom=3` R→L (top≤bottom): 15,14,13 → ans=\[1,2,3,4,8,12,16,15,14,13], `bottom=2`
* Col `left=0` B→T (left≤right): 9,5 → ans=\[1,2,3,4,8,12,16,15,14,13,9,5], `left=1`

Next ring (`top=1, bottom=2, left=1, right=2`):

* Row `top=1` L→R: 6,7 → ans=…,\[6,7], `top=2`
* Col `right=2` T→B: 11 → ans=…,\[6,7,11], `right=1`
* Row `bottom=2` R→L: 10 → ans=…,\[6,7,11,10], `bottom=1`
* Col `left=1` B→T: (now `bottom<top`, skip)

Loop ends (boundaries crossed).
Result: `[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]`.

---

## 3) Python solutions (optimized + simple alternative)

### A) Optimized O(n·m) time, O(1) extra space (most expected)

```python
class Solution:
    def spirallyTraverse(self, mat):
        """
        Layer-by-layer traversal using four shrinking boundaries.

        Time:  O(n * m) — each cell is visited once
        Space: O(1)     — ignoring the result array we must return
        """
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        res = []

        while top <= bottom and left <= right:
            # 1) left -> right on the top row
            for j in range(left, right + 1):
                res.append(mat[top][j])
            top += 1

            # 2) top -> bottom on the right column
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1

            # 3) right -> left on the bottom row (if still valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(mat[bottom][j])
                bottom -= 1

            # 4) bottom -> top on the left column (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1

        return res
```

**Why those boundary checks?**
When the matrix has a single row or a single column left, without the checks you would double-count that row/column.

---

### B) Simple alternative using “visited + directions” (clear, a bit more space)

* Keep a `visited` boolean grid.
* Move in one of 4 directions (`right, down, left, up`).
* If the next cell is out of bounds or already visited, turn right (change direction).
* Stop after visiting `n*m` cells.

```python
class SolutionVisited:
    def spirallyTraverse(self, mat):
        """
        Direction-walk with a visited matrix.

        Time:  O(n * m)
        Space: O(n * m) for visited
        """
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        visited = [[False] * m for _ in range(n)]
        total = n * m
        res = []

        # directions:     right     down      left      up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r = c = 0

        for _ in range(total):
            res.append(mat[r][c])
            visited[r][c] = True

            nr, nc = r + dirs[d][0], c + dirs[d][1]
            # turn if next is invalid/visited
            if not (0 <= nr < n and 0 <= nc < m and not visited[nr][nc]):
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]

            r, c = nr, nc

        return res
```

Both are $O(nm)$. The boundary method uses constant extra space and is the preferred interview solution.

---

## 4) Common Interview Q\&A

**Q1. Why do we need the boundary checks (`if top <= bottom` / `if left <= right`)?**
To avoid re-traversing the same row/column when only a single row or column is left. Without the checks, you’ll append duplicates.

**Q2. What are the time and space complexities?**

* Time: $O(n \cdot m)$, every element is visited exactly once.
* Space: $O(1)$ extra for the boundary approach (plus the output list), $O(n \cdot m)$ for the visited-grid variant.

**Q3. How would you handle an empty matrix or jagged rows?**

* Empty: return `[]`.
* Jagged rows: classical spiral assumes a proper rectangle. For jagged input, you’d need extra boundary logic per row (generally not asked for this problem).

**Q4. Can this be done in-place?**
We don’t modify the matrix; we only produce the traversal order. If you had to mark visited in-place, you could temporarily mutate entries (e.g., sentinel), but that’s not standard for this question.

**Q5. What are typical pitfalls?**

* Missing boundary checks (duplicates).
* Incorrect boundary increments/decrements order.
* Not handling single row or single column matrices correctly.

**Q6. How do you verify correctness quickly in an interview?**
Test with:

* 1×1, 1×N, N×1 matrices,
* A square and a rectangular matrix,
* Odd and even dimensions,
* Cases where the last layer is a single row/column.

---

---

Below is a **complete, runnable Python program** for **Spiral Traversal of a Matrix** that:

* Implements the standard **O(n·m) time / O(1) extra space** solution,
* Prints **inputs and outputs** for several example cases,
* Uses `timeit` to report **elapsed time** for each run and the **total program time**, and
* Includes **inline comments** describing the **time/space complexity** of each step.

```python
from typing import List
import timeit

class Solution:
    def spirallyTraverse(self, mat: List[List[int]]) -> List[int]:
        """
        Return the elements of 'mat' in spiral order.

        Complexity overview:
          - Let n = number of rows, m = number of columns.
          - Every element is appended exactly once.
          - Time  : O(n * m)
          - Space : O(1) extra (ignoring the returned list of size n*m)
        """
        # Guard: empty matrix -> O(1) time, O(1) space
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])  # O(1)
        top, bottom = 0, n - 1        # O(1)
        left, right = 0, m - 1        # O(1)
        res = []                      # O(n*m) space for the output, required by problem

        # The loop continues while there is at least one valid row and column.
        # Each boundary update reduces the unvisited region; each cell visited once.
        # Overall O(n*m) time.
        while top <= bottom and left <= right:
            # 1) Traverse the current 'top' row from left -> right
            #    Visits (right - left + 1) elements; across the whole algorithm this sums to O(n*m).
            for j in range(left, right + 1):
                res.append(mat[top][j])
            top += 1  # O(1)

            # 2) Traverse the current 'right' column from top -> bottom
            #    Visits (bottom - top + 1) elements; sums to O(n*m) over all iterations.
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1  # O(1)

            # 3) Traverse the current 'bottom' row from right -> left (if still valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(mat[bottom][j])
                bottom -= 1  # O(1)

            # 4) Traverse the current 'left' column from bottom -> top (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1  # O(1)

        return res


# --------------------------- Demo & Timing Harness ---------------------------

def run_case(name: str, mat: List[List[int]], solver: Solution) -> None:
    """
    Runs a single test case, prints input, output, and per-case time.

    Complexity of this wrapper is dominated by solver.spirallyTraverse => O(n*m).
    """
    start = timeit.default_timer()
    out = solver.spirallyTraverse(mat)
    end = timeit.default_timer()
    print(f"{name}:")
    print("  Input matrix:")
    for row in mat:
        print("   ", row)
    print("  Spiral traversal:", out)
    print(f"  Elapsed: {(end - start):.6f}s\n")


def main():
    print("=== Spiral Traversal — Examples, Outputs & Timing ===\n")
    solver = Solution()

    # Example cases (including edge-ish shapes) -------------------------------
    mat1 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13,14, 15, 16]
    ]  # Expected: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

    mat2 = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9,10,11,12],
        [13,14,15,16,17,18]
    ]  # Expected: [1,2,3,4,5,6,12,18,17,16,15,14,13,7,8,9,10,11]

    mat3 = [
        [32, 44, 27, 23],
        [54, 28, 50, 62]
    ]  # Expected: [32,44,27,23,62,50,28,54]

    mat4 = [[1,2,3,4]]          # Single row
    mat5 = [[1],[2],[3],[4],[5]]# Single column
    mat6 = [[7]]                # 1x1

    # Run cases and time each
    run_case("Case 1 (4x4)", mat1, solver)
    run_case("Case 2 (3x6)", mat2, solver)
    run_case("Case 3 (2x4)", mat3, solver)
    run_case("Case 4 (1x4)", mat4, solver)
    run_case("Case 5 (5x1)", mat5, solver)
    run_case("Case 6 (1x1)", mat6, solver)


if __name__ == "__main__":
    program_start = timeit.default_timer()
    main()
    program_end = timeit.default_timer()
    print("==== TOTAL PROGRAM TIME ====")
    print(f"{(program_end - program_start):.6f}s")
```

---

## 6) Real-World Use Cases (a few important ones)

* **Image/Matrix “Peeling” Operations:** Reading or processing pixels in concentric layers (e.g., decorative rendering, border erode/dilate passes).
* **3D Printing / CNC Path Planning (2D layer):** Traversing toolpaths from the outside in, ensuring minimal repositioning.
* **UI/Grid Animations:** Reveal or highlight dashboard tiles/raster data in spiral order for visual effects.
* **Data Dumping from 2D Buffers:** Streaming out a rectangular buffer in a spiral pattern (e.g., for diagnostics or demos).
* **Game/Map Mechanics:** Spiral discovery or item placement expanding from a center or from a frame inward.


# Max rectangle

**Difficulty:** Hard
**Accuracy:** 36.43%    **Submissions:** 118K+    **Points:** 8    **Average Time:** 35m

---

You are given a 2D binary matrix `mat[][]`, where each cell contains either `0` or `1`. Your task is to find the **maximum area** of a rectangle that can be formed using **only `1`s** within the matrix.

---

## Examples

### Example 1

**Input:**
`mat[][] = [[0, 1, 1, 0],                [1, 1, 1, 1],                [1, 1, 1, 1],                [1, 1, 0, 0]]`

**Output:** `8`

**Explanation:**
The largest rectangle with only `1`s is from `(1, 0)` to `(2, 3)` which is

```
[1, 1, 1, 1]
[1, 1, 1, 1]
```

and area is `4 * 2 = 8`.

---

### Example 2

**Input:**
`mat[][] = [[0, 1, 1],                [1, 1, 1],                [0, 1, 1]]`

**Output:** `6`

**Explanation:**
The largest rectangle with only `1`s is from `(0, 1)` to `(2, 2)` which is

```
[1, 1]
[1, 1]
[1, 1]
```

and area is `2 * 3 = 6`.

---

## Constraints

* `1 ≤ mat.size(), mat[0].size() ≤ 1000`
* `0 ≤ mat[i][j] ≤ 1`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(m)`

---

## Company Tags

Flipkart, Amazon, Microsoft, Samsung, MakeMyTrip, Directi, Intuit, Google

---

## Topic Tags

Dynamic Programming, Stack, Matrix, Data Structures, Algorithms

---

## Related Interview Experiences

* Directi Interview Experience Set 15 On Campus
* Intuit Interview Experience Set 11 On Campus
* Samsung R\&D Bangalore Internship Experience 2018

---

## Related Articles

* Maximum Size Rectangle Binary Sub Matrix 1s

---

---

Great pick — this one is a classic “reduce 2-D to 1-D” problem that shows up a lot. I’ll walk you through the core idea, do a small dry run, then give you two Python solutions (a clear optimal one and a slower-but-simple baseline), and finish with interview Q\&A.

---

## 2) Idea + step-by-step dry run

### Core idea (build on what you know)

* If you look at each row as the **base** of a histogram, and count **consecutive 1s going upward** as the height for each column, then the problem becomes:

  > For each row, compute the **largest rectangle in a histogram** using those heights; the answer is the max over all rows.

* So we maintain an array `heights` of length `m` (columns).
  For row `r` and column `c`:

  ```
  if mat[r][c] == 1: heights[c] += 1
  else:              heights[c] = 0
  ```

* For each updated `heights`, we compute “largest rectangle in histogram” in **O(m)** with a **monotonic stack**.

### Dry run on a small matrix

```
mat =
[0, 1, 1, 0]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 0, 0]
```

Initialize `heights = [0,0,0,0]`, `best = 0`

Row 0 → heights:

* \[0,1,1,0]
  Largest-rectangle-in-histogram(\[0,1,1,0]) = 2  (two 1’s side-by-side)
  `best = 2`

Row 1 → heights:

* mat\[1] is \[1,1,1,1] so heights becomes \[1,2,2,1]
  Largest rectangle:
* The two middle bars of height 2 with width 2 → area 4
* The four bars (1,2,2,1) don’t beat 4
  `best = 4`

Row 2 → heights:

* add another row of 1s: heights = \[2,3,3,2]
  Largest rectangle:
* The middle two bars height=3, width=2 → area = 6
* The middle four bars can give height=2, width=4 → area = 8  ← bigger
  `best = 8`

Row 3 → heights:

* row is \[1,1,0,0] so heights = \[3,4,0,0]
  Largest rectangle here is height 4, width 1 → 4 (or 3×1=3).
  `best` stays **8**.

Answer: **8**.

---

## 3) Python solutions

### A. Optimal (O(n·m) time, O(m) space)

Monotonic increasing stack for “largest rectangle in histogram” per row.

```python
class Solution:
    def maxArea(self, mat):
        """
        Time  : O(n * m) — each row builds a histogram; each histogram solved in O(m)
        Space : O(m)     — the heights array + stack
        """
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m
        best = 0

        for r in range(n):
            # 1) Build histogram for this row (consecutive 1s upward)
            for c in range(m):
                if mat[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0

            # 2) Compute largest rectangle in current histogram (monotonic stack)
            best = max(best, self._largestRectangleArea(heights))

        return best

    def _largestRectangleArea(self, heights):
        """
        Standard LC84 solution.
        Stack holds indices of bars in increasing height.
        When we see a shorter bar, we 'resolve' rectangles with bars taller than it.
        """
        stack = []          # indices of increasing heights
        max_area = 0
        # sentinel trick: process all bars by appending a 0 at the end
        for i, h in enumerate(heights + [0]):
            # resolve rectangles that end before 'i'
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                # width: if stack is empty, rectangle extends from 0..i-1
                # else from stack[-1]+1 .. i-1
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
```

**Why the stack works:** it keeps indices in strictly increasing height; when you hit a bar shorter than the top, that top bar’s maximal width ends at the current index, so you can compute its area.

---

### B. Simpler baseline (slower) — O(n·m²)

For each row’s histogram, for every index expand using precomputed **nearest smaller to left/right**. Still linear per row, but you can also do a very naive per-index expansion which is O(m²). Here’s a clear variant using NSL/NSR (still O(m)) to illustrate another common pattern:

```python
class SolutionBaseline:
    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0
        n, m = len(mat), len(mat[0])
        heights = [0] * m
        best = 0

        for r in range(n):
            for c in range(m):
                heights[c] = heights[c] + 1 if mat[r][c] == 1 else 0
            best = max(best, self._maxRectByNSLR(heights))
        return best

    def _maxRectByNSLR(self, heights):
        # nearest smaller to left
        n = len(heights)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # nearest smaller to right
        right = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # compute best area with heights[i] as the limiting height
        best = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            best = max(best, heights[i] * width)
        return best
```

> In interviews, either the **stack sweep** or the **NSL/NSR** approach is considered the expected optimal solution.

---

## 4) Interviewer-style Q\&A

**Q1. Why does turning rows into histograms solve the 2-D rectangle problem?**
**A.** Any rectangle of 1s ending at row `r` has a height equal to the number of consecutive 1s above each column inside it. By accumulating column heights row by row, the “largest all-1s rectangle ending at row r” is exactly the largest rectangle in that histogram. Taking the max over all rows covers all possible bottom edges.

**Q2. What is the time complexity?**
**A.** O(n·m). We update `heights` in O(m) per row and compute largest rectangle in histogram in O(m). Total O(n·m).

**Q3. Why do we add a trailing 0 in the stack method?**
**A.** The sentinel (0 height) forces the stack to flush, ensuring we compute areas for bars that “run to the end.”

**Q4. What edge cases should we care about?**

* Empty matrix or empty row → return 0.
* Rows/columns with all zeros → heights reset to 0; area 0 for that row.
* Single row/column → reduces to the histogram problem directly.

**Q5. Can you do it without extra O(m) stack?**
**A.** Not in worst-case O(n·m) time with a clean approach. The stack or NSL/NSR arrays are the standard linear-time tools. Any alternative that avoids them typically worsens complexity.

**Q6. Differences between NSL/NSR and single-pass stack version?**
**A.** Both achieve O(m). The single-pass “push indices, pop when decreasing” pattern avoids storing NSL/NSR explicitly, using the stack’s content to derive widths on the fly. NSL/NSR is often more explicit/readable.

---

---

Awesome—let’s put everything together as a **complete, runnable program** with clear complexity notes, example I/O, and a tiny time measurement.

---

## 5) Full Python program (with inline complexity notes + timing)

```python
#!/usr/bin/env python3
"""
Max rectangle of 1s in a binary matrix

Approach
--------
Reduce each row to a histogram of consecutive 1s going upward.
For every row, compute the Largest Rectangle in Histogram (LRH) in O(m) via a
monotonic increasing stack. Take the maximum area over all rows.

Complexities
------------
Let n = number of rows, m = number of columns.

- Building/Updating histogram per row:       O(m) time, O(m) space (heights)
- LRH via stack per row:                     O(m) time, O(m) space (stack)
- For all rows:                              O(n*m) time, O(m) auxiliary space
"""

from timeit import default_timer as timer

class Solution:
    def maxArea(self, mat):
        """
        Overall Time:  O(n * m)
        Overall Space: O(m)

        n passes over rows; per row:
          - Update heights: O(m)
          - Largest rectangle in histogram: O(m)
        """
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m   # O(m) space
        best = 0

        for r in range(n):  # O(n)
            # ---- Build/Update histogram for this row: O(m) time, O(1) extra space
            for c in range(m):
                heights[c] = heights[c] + 1 if mat[r][c] == 1 else 0

            # ---- Compute LRH in O(m) time, O(m) stack space
            best = max(best, self._largestRectangleArea(heights))

        return best

    def _largestRectangleArea(self, heights):
        """
        Largest Rectangle in Histogram (LC-84 classic).
        Time:  O(m)
        Space: O(m) for the stack

        Stack keeps indices of bars in strictly increasing height.
        When a shorter bar arrives, we resolve rectangles that end before it.
        """
        stack = []          # indices with increasing heights
        max_area = 0

        # Sentinel: process all bars by appending a zero height
        for i, h in enumerate(heights + [0]):
            # While current height h is less than the height at stack top,
            # we have found the right boundary of those taller bars.
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


# ------------------------------
# Demo / Simple correctness tests
# ------------------------------
def run_demo():
    sol = Solution()

    tests = [
        (
            [[0, 1, 1, 0],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 0, 0]],
            8
        ),
        (
            [[0, 1, 1],
             [1, 1, 1],
             [0, 1, 1]],
            6
        ),
        (
            [[1, 0, 1, 1, 1],
             [1, 1, 1, 1, 0],
             [1, 1, 1, 1, 0]],
            9  # 3 rows x 3 cols block of 1s
        ),
        (
            [[0,0],[0,0]],
            0
        ),
        (
            [[1,1,1]],
            3
        ),
        (
            [[1],[1],[1]],
            3
        ),
    ]

    for i, (mat, expected) in enumerate(tests, 1):
        got = sol.maxArea(mat)
        print(f"Test {i}: got={got}, expected={expected}, {'OK' if got == expected else 'FAIL'}")

# ------------------------------
# Micro timing (for the whole run)
# ------------------------------
def main():
    # Example input:
    mat = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
    ]

    sol = Solution()

    # Warm-up (good practice for more stable timing)
    _ = sol.maxArea(mat)

    # Time the main call once. For more stable numbers, loop a few times.
    start = timer()
    ans = sol.maxArea(mat)
    end = timer()

    print("\n=== Example Run ===")
    print("Input matrix:")
    for row in mat:
        print(row)
    print(f"Output (max rectangle area of 1s): {ans}")
    print(f"Elapsed time: {(end - start)*1e6:.1f} µs (single run on this machine)\n")

    # Run small demo suite
    run_demo()

if __name__ == "__main__":
    main()
```

### Example output (will vary slightly by machine)

```
=== Example Run ===
Input matrix:
[0, 1, 1, 0]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 0, 0]
Output (max rectangle area of 1s): 8
Elapsed time: 140.2 µs (single run on this machine)

Test 1: got=8, expected=8, OK
Test 2: got=6, expected=6, OK
Test 3: got=9, expected=9, OK
Test 4: got=0, expected=0, OK
Test 5: got=3, expected=3, OK
Test 6: got=3, expected=3, OK
```

> Notes:
>
> * The timing is just to give you a sense of performance. For robust benchmarking use multiple iterations and average.

---

## 6) Real-World Use Cases (why this matters)

1. **Image processing / document analysis**
   Finding the largest axis-aligned block of foreground pixels (e.g., largest table region or filled block) in a binary image/grid.

2. **Seating / facility layouts**
   In a 2D layout where cells are usable (`1`) or blocked (`0`), quickly determine the largest rectangular usable zone to place equipment, kiosks, or allocate seating.

3. **Memory / storage allocation on grids**
   When modeling allocation on a block grid (e.g., SSD flash pages, FPGA grids), determine the largest contiguous rectangular block of “available” cells.

4. **Game maps & path planning**
   For tiled maps (walkable vs. blocked), identify the largest rectangular region to spawn events, build structures, or place AOEs.

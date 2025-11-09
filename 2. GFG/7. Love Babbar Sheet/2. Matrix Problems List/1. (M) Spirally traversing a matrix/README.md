
Here’s the **complete README-style conversion** of your provided image — nothing omitted:

---

# 🌀 Spirally Traversing a Matrix

### Difficulty: Medium

**Accuracy:** 35.2%
**Submissions:** 331K+
**Points:** 4

---

## 🧠 Problem Statement

You are given a rectangular matrix **mat[][]** of size **n × m**, and your task is to return an array while traversing the matrix in **spiral form**.

---

## 🧩 Examples

### Example 1

**Input:**

```
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
```

**Output:**

```
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
```

**Explanation:**
Example of matrix in spiral form

```
Matrix:
1  →  2  →  3  →  4
↓              ↓
5  →  6  →  7  →  8
↓              ↓
9  → 10 → 11 → 12
↓              ↓
13 → 14 → 15 → 16
↑              ↑
```

Output sequence:
`1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10`

---

### Example 2

**Input:**

```
mat = [[1, 2, 3, 4, 5, 6],
       [7, 8, 9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18]]
```

**Output:**

```
[1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
```

**Explanation:**
Applying same technique as above.

---

### Example 3

**Input:**

```
mat = [[32, 44, 27, 23],
       [54, 28, 50, 62]]
```

**Output:**

```
[32, 44, 27, 23, 62, 50, 28, 54]
```

**Explanation:**
Applying same spiral traversal technique, output is `[32, 44, 27, 23, 62, 50, 28, 54]`.

---

## ⚙️ Constraints

* ( 1 \leq n, m \leq 1000 )
* ( 0 \leq mat[i][j] \leq 100 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n × m)
* **Auxiliary Space:** O(n × m)

---

## 🏢 Company Tags

**Paytm**, **Flipkart**, **Morgan Stanley**, **Microsoft**, **OYO Rooms**, **Snapdeal**, **D-E-Shaw**, **MakeMyTrip**, **Oracle**, **MAQ Software**, **Adobe**, **nearbuy**, **Nagarro**, **BrowserStack**, **Salesforce**, **Zoho**

---

## 🧩 Topic Tags

* Arrays
* Matrix
* Data Structures

---

## 💬 Related Interview Experiences

* Paytm Interview Experience Set 14 for Senior Android Developer
* MakeMyTrip Interview Experience Set 6 Online Coding
* Microsoft Interview Experience for SDE 1 2
* Adobe Interview Experience SheCodes Software Engineer
* Adobe Interview Questions Computer Scientist

---

## 📚 Related Articles

* [Print A Given Matrix In Spiral Form](https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/)


---

---

awesome — here’s a tight, interview-ready kit for **Spiral Traversal of a Matrix**.

---

# 2) Explanation + step-by-step dry run

## Problem in one line

Given an `n × m` matrix, return the elements in **clockwise spiral order** starting from the top-left cell.

## Core idea (boundaries / “peel the onion”)

Keep four boundaries and shrink them as you traverse layers:

* `top` (first unprinted row)
* `bottom` (last unprinted row)
* `left` (first unprinted column)
* `right` (last unprinted column)

Loop while `top ≤ bottom` and `left ≤ right`, printing:

1. **Left → Right** along row `top`, then `top += 1`
2. **Top → Bottom** along column `right`, then `right -= 1`
3. **Right → Left** along row `bottom` (if `top ≤ bottom`), then `bottom -= 1`
4. **Bottom → Top** along column `left`   (if `left ≤ right`), then `left += 1`

These checks prevent double-printing the middle row/column for odd dimensions.

### Dry run (3×4)

```
mat =
[ [ 1,  2,  3,  4],
  [ 5,  6,  7,  8],
  [ 9, 10, 11, 12] ]
top=0, bottom=2, left=0, right=3

1) row top=0, L→R: 1,2,3,4        top=1
2) col right=3, T→B: 8,12         right=2
3) row bottom=2, R→L: 11,10,9     bottom=1
4) col left=0, B→T: 5             left=1
Loop again (top=1,bottom=1,left=1,right=2):
1) row 1, L→R: 6,7                top=2
Checks fail (top>bottom). Done.

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

Edge cases handled naturally:

* Single row or single column
* Non-square matrices
* Empty matrix (return `[]`)

---

# 3) Python solutions (brute ➜ simple optimal ➜ alternative)

All match your required signature:

```python
class Solution:
    def spirallyTraverse(self, mat):
        # code here
```

## A) Brute (simulate directions with `visited`) — clear but uses O(n*m) extra space

```python
class Solution:
    def spirallyTraverse(self, mat):
        """
        Simulate movement with direction vectors and a visited set.
        Time:  O(n*m)
        Space: O(n*m) (visited)
        """
        if not mat or not mat[0]:
            return []
        n, m = len(mat), len(mat[0])

        # right, down, left, up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0                       # current direction index
        r = c = 0                   # current position
        visited = [[False]*m for _ in range(n)]
        out = []

        for _ in range(n*m):
            out.append(mat[r][c])
            visited[r][c] = True
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            # if next step is invalid or visited, turn right
            if not (0 <= nr < n and 0 <= nc < m and not visited[nr][nc]):
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]
            r, c = nr, nc
        return out
```

## B) **Optimal & interview-standard (boundary peel)** — O(n*m) time, **O(1) extra space**

```python
class Solution:
    def spirallyTraverse(self, mat):
        """
        Boundary 'peel the onion' approach.
        Time:  O(n*m)  (each cell visited once)
        Space: O(1)    (aside from output)
        """
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result = []

        while top <= bottom and left <= right:
            # 1) Left -> Right on current top row
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1

            # 2) Top -> Bottom on current right column
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1

            # 3) Right -> Left on current bottom row (guard to avoid re-traversal)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1

            # 4) Bottom -> Top on current left column (guard again)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1

        return result
```

## C) Recursive layer peeling (for completeness)

```python
class Solution:
    def spirallyTraverse(self, mat):
        """
        Recursively peel outer ring; elegant but same O(n*m) time/aux stack O(min(n,m)).
        """
        if not mat or not mat[0]:
            return []

        res = []
        def peel(top, left, bottom, right):
            if top > bottom or left > right:
                return
            # top row
            for c in range(left, right + 1):
                res.append(mat[top][c])
            # right col
            for r in range(top + 1, bottom + 1):
                res.append(mat[r][right])
            if top < bottom and left < right:
                # bottom row
                for c in range(right - 1, left, -1):
                    res.append(mat[bottom][c])
                # left col
                for r in range(bottom, top, -1):
                    res.append(mat[r][left])
            peel(top + 1, left + 1, bottom - 1, right - 1)

        peel(0, 0, len(mat) - 1, len(mat[0]) - 1)
        return res
```

> In interviews, version **B** is the expected one: clean, O(1) space, no visited grid.

---

# 4) Interview quick-recall + expected Q&A

## 5-line pseudo you can memorize

```
top=0; bottom=n-1; left=0; right=m-1
while top<=bottom and left<=right:
  L→R over row top;   top++
  T→B over col right; right--
  if top<=bottom: R→L over row bottom; bottom--
  if left<=right: B→T over col left;   left++
return result
```

**Mnemonic:** **“Peel the Onion: Top→Right→Bottom→Left, then shrink.”**

## Likely Questions (with crisp answers)

**Q1. Why the two `if` guards?**
To avoid double-printing the center line when one dimension becomes exhausted (e.g., odd rows/cols).

**Q2. Time/space complexity?**
Each element is appended once → **O(n·m)** time; only a few indices stored → **O(1)** extra space.

**Q3. How do you handle non-square matrices?**
The boundary checks make it generic; no special casing needed.

**Q4. Alternative approach?**
Direction simulation with a `visited` matrix (clean but uses O(n·m) space). Or recursive layer peeling (same complexity, uses call stack).

**Q5. Edge cases you’d test?**
`1×1`, `1×k`, `k×1`, empty matrix, rectangular (e.g., `2×5`, `5×2`), and matrices with repeated numbers.

---

---

perfect — here are the last two pieces for **Spiral Traversal**.

# 5) Real-World Use Cases (short & relatable)

* **Image/Screen buffer scanning:** Reading pixels layer-by-layer to apply vignette/border effects or to preview “peeling” animations.
* **Matrix–based hardware diagnostics:** Probing sensors/LEDs arranged in a grid from the outside in (spiral route minimizes wire crossing).
* **Robotics floor coverage in tight areas:** A cleaning bot sweeping a rectangular room by spiraling inwards (simple boundary logic, no revisit storage).
* **Data visualization widgets:** Rendering table cells as a spiral for “time-lapse” reveal or heat-map storytelling.

All of these map to the same boundary-shrink (“peel the onion”) traversal.

---

# 6) Full Python Program (with inline time/space notes + timing)

```python
"""
Spiral Traversal of a Matrix — Full Program
-------------------------------------------
Return elements of an n x m matrix in clockwise spiral order.

Approach:
- Maintain 4 boundaries: top, bottom, left, right.
- Traverse Top row (L->R), Right column (T->B), Bottom row (R->L),
  Left column (B->T). After each pass, shrink the corresponding boundary.
- Guards avoid double visiting when a middle row/column remains.

Complexities:
- Each element is read exactly once  -> Time  : O(n * m)
- Only indices + output list stored -> Space : O(1) extra (excluding output)
"""

import timeit

class Solution:
    def spirallyTraverse(self, mat):
        """
        Boundary 'peel the onion' traversal.

        Time step-by-step:
            - Outer while loop shrinks bounds; each inner for-loop
              visits disjoint cells -> total visits = n*m -> O(n*m).
        Space step-by-step:
            - top/bottom/left/right + loop vars -> O(1) auxiliary.
            - result list holds n*m values      -> O(n*m) output.

        Args:
            mat: List[List[int]] (n x m matrix)
        Returns:
            List[int]: elements in clockwise spiral order
        """
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result = []

        # Loop until the boundaries cross
        while top <= bottom and left <= right:
            # 1) Left -> Right over the top row
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1  # shrink the top boundary

            # 2) Top -> Bottom over the right column
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1  # shrink the right boundary

            # 3) Right -> Left over the bottom row (guard prevents re-traverse)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1  # shrink the bottom boundary

            # 4) Bottom -> Top over the left column (guard prevents re-traverse)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1  # shrink the left boundary

        return result


# ------------------------------ Demo + Timing ------------------------------
if __name__ == "__main__":
    samples = [
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]],

        [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]],

        [[32, 44, 27, 23],
         [54, 28, 50, 62]],
    ]

    sol = Solution()

    for idx, mat in enumerate(samples, 1):
        # Measure time for one full call (includes all traversal work)
        elapsed = timeit.timeit(lambda: sol.spirallyTraverse(mat), number=1)
        output = sol.spirallyTraverse(mat)
        print(f"Input {idx}: {mat}")
        print(f"Output {idx}: {output}")
        print(f"Execution Time {idx}: {elapsed:.8f} seconds\n")
```

### What the run looks like

```
Input 1: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output 1: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Execution Time 1: 0.00000xx seconds

Input 2: [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output 2: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
Execution Time 2: 0.00000xx seconds

Input 3: [[32, 44, 27, 23], [54, 28, 50, 62]]
Output 3: [32, 44, 27, 23, 62, 50, 28, 54]
Execution Time 3: 0.00000xx seconds
```

You now have: relatable use cases, the optimal O(n·m) / O(1) approach, and a complete, timed main program you can paste into any judge or IDE.


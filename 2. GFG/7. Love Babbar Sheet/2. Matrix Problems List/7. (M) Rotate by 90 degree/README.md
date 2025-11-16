
---

# 🌀 Rotate by 90 Degrees (Clockwise)

**Difficulty:** Medium
**Accuracy:** 66.8%
**Submissions:** 67K+
**Points:** 4
**Average Time:** 20 minutes

---

## 🧠 Problem Statement

Given a square matrix **mat[][]**, the task is to **rotate it by 90 degrees in clockwise direction** **without using any extra space** (i.e., in-place rotation).

---

## 📘 Examples

### Example 1

**Input:**

```
mat[][] = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:**

```
7 4 1
8 5 2
9 6 3
```

---

### Example 2

**Input:**

```
mat[][] = [
  [1, 2],
  [3, 4]
]
```

**Output:**

```
3 1
4 2
```

---

### Example 3

**Input:**

```
mat[][] = [[1]]
```

**Output:**

```
1
```

---

## 📌 Constraints

* (1 \leq mat.size() \leq 1000)
* (1 \leq mat[i][j] \leq 100)

---

## ⏱ Expected Complexities

* **Time Complexity:** ( O(n^2) )
* **Auxiliary Space:** ( O(1) ) (in-place rotation)

---

## 🏢 Company Tags

* Paytm
* Zoho
* Morgan Stanley
* Amazon
* Microsoft
* Samsung
* Snapdeal
* D-E-Shaw

---

## 🧩 Topic Tags

* Matrix
* Data Structures

---

## 🔍 Related Interview Experiences

* Microsoft Interview Experience Set 102 On Campus For IDC
* Samsung R&D Interview Questions
* Samsung R&D Bangalore Freshers Full Time Internship

---

## 📚 Related Articles

* [**Rotate a Matrix by 90 Degree in Clockwise Direction Without Using Any Extra Space**](https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/)

---

---

Let’s make this matrix-rotation problem muscle memory. 💪

---

## 2. Explanation + Step-by-step Dry Run

### Goal

Given an **n × n** matrix `mat`, rotate it **90° clockwise in-place** (no extra matrix).

### Key idea (most common in interviews)

**Rotate 90° clockwise = Transpose + Reverse each row**

1. **Transpose** the matrix (swap `mat[i][j]` with `mat[j][i]` for `i < j`)

   * This mirrors the matrix over its main diagonal.
2. **Reverse every row**

   * This turns the transposed matrix into the 90° clockwise rotated matrix.

Mathematically, clockwise rotation maps `(r, c) → (c, n-1-r)`.
Transposing gives `(r, c) → (c, r)`, reversing rows gives `(c, r) → (c, n-1-r)` → same final position. ✅

---

### Dry run on 3×3 example

```text
mat =
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]
```

#### Step 1: Transpose (swap across diagonal)

Pairs we swap:

* (0,1) ↔ (1,0)  → 2 ↔ 4
* (0,2) ↔ (2,0)  → 3 ↔ 7
* (1,2) ↔ (2,1)  → 6 ↔ 8

Result:

```text
[ [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9] ]
```

#### Step 2: Reverse each row

Row 0: `[1, 4, 7]` → `[7, 4, 1]`
Row 1: `[2, 5, 8]` → `[8, 5, 2]`
Row 2: `[3, 6, 9]` → `[9, 6, 3]`

Final matrix:

```text
[ [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3] ]
```

Which is exactly the required output. 🎯

---

## 3. Python Codes (Brute + Optimal)

Signature to follow:

```python
# User function Template for python3
def rotate(mat):
    # code here
```

---

### A) Brute force (using extra matrix) – for understanding

> ❗ Not allowed by “no extra space” constraint, but good for intuition.

```python
#User function Template for python3

def rotate(mat):
    """
    Brute force: use an extra n x n matrix, then copy back.
    Time  : O(n^2)
    Space : O(n^2) extra (NOT allowed in the problem, but good mental model)
    """

    n = len(mat)
    # Create an empty n x n matrix
    rotated = [[0] * n for _ in range(n)]

    # Map each cell (r, c) to (c, n-1-r)
    for r in range(n):          # O(n)
        for c in range(n):      # O(n)
            rotated[c][n - 1 - r] = mat[r][c]

    # Copy back to mat to keep the interface same
    for r in range(n):
        for c in range(n):
            mat[r][c] = rotated[r][c]
```

---

### B) Optimal: Transpose + Reverse rows (in-place, O(1) space)

This is the **expected interview solution**.

```python
#User function Template for python3

def rotate(mat):
    """
    Rotate the square matrix by 90 degrees clockwise IN-PLACE.

    Idea:
      1) Transpose the matrix: mat[i][j] <-> mat[j][i] for i < j
      2) Reverse every row.

    Time  : O(n^2)  (we touch each cell constant times)
    Space : O(1)    (in-place, only a few temp variables)
    """
    n = len(mat)
    if n == 0:
        return

    # 1) Transpose: swap elements across the main diagonal
    for i in range(n):            # O(n)
        for j in range(i + 1, n): # only upper triangle, also O(n)
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # 2) Reverse each row
    for i in range(n):            # O(n)
        mat[i].reverse()          # O(n) per row, still overall O(n^2)
```

---

### C) Alternative Optimal: Layer-by-layer 4-way swap

Some interviewers like this explicit rotation.

```python
def rotate(mat):
    """
    Alternative O(1) space method:
    Rotate layer by layer using 4-way swaps.
    Time  : O(n^2)
    Space : O(1)
    """
    n = len(mat)
    if n == 0:
        return

    # We rotate each "ring" or "layer" from outer to inner
    for layer in range(n // 2):           # number of layers ~ n/2
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Save top
            top = mat[first][i]

            # left -> top
            mat[first][i] = mat[last - offset][first]

            # bottom -> left
            mat[last - offset][first] = mat[last][last - offset]

            # right -> bottom
            mat[last][last - offset] = mat[i][last]

            # top -> right
            mat[i][last] = top
```

Both B and C satisfy the in-place, O(1) requirement, but **B (transpose + reverse)** is usually easier to implement and remember.

---

## 4. Interview Memory Tricks + Q&A

### 5-line pseudo-code (transpose + reverse)

```text
n = len(mat)
for i in 0..n-1:
    for j in i+1..n-1:
        swap(mat[i][j], mat[j][i])    # transpose
for i in 0..n-1:
    reverse(mat[i])                   # reverse each row
```

### Mnemonic: **“Flip then Flip”**

* **Flip over diagonal** → transpose
* **Flip each row** → reverse rows

Say: **“Diagonal flip, row flip → 90° clockwise.”**

---

### Likely Interview Questions & Good Answers

**Q1. Why does transpose + row-reverse equal a 90° clockwise rotation?**

> Rotation sends `(r, c) → (c, n-1-r)`.
> Transpose: `(r, c) → (c, r)`
> Then reverse row: `(c, r) → (c, n-1-r)`
> Composition equals the rotation mapping, so this gives correct result.

---

**Q2. What is the time and space complexity?**

> * Transpose: about `n*(n-1)/2` swaps → `O(n^2)`
> * Reversing each row: `n` rows × `O(n)` each → `O(n^2)`
>   Overall time: **O(n^2)**, Extra space: **O(1)**.

---

**Q3. Can you rotate anti-clockwise with a similar trick?**
Yes, two common patterns:

* **Transpose + reverse each column**, or
* **Reverse each row + transpose**
  Both effectively map `(r, c) → (n-1-c, r)` (which is 90° anticlockwise).

---

**Q4. What would be the naive approach and why is it not acceptable here?**

> Naive: create a new matrix `B`, set `B[c][n-1-r] = A[r][c]`.
> Time: O(n^2), but **extra space O(n^2)**, which violates “no extra space” requirement.

---

**Q5. Any special edge cases?**

> * `n = 1`: single element; after transpose & reverse row, still `[ [x] ]`.
> * Already symmetric matrices (like identity) remain structured; rotation still correct.
> * Empty matrix → often ignored by constraints but handle safely in code.

---

### 60-second recall script before an interview

1. **Recognize**: “Square matrix, 90° clockwise, in-place → transpose+reverse trick.”
2. **Say to yourself**: “Diagonal flip, row flip.”
3. **Write pseudo-code**:

   * for `i` in 0..n-1, `j` in `i+1..n-1`: swap `mat[i][j]` with `mat[j][i]`
   * for each row: reverse the row
4. **Mention complexity**: “O(n²) time, O(1) space.”
5. **Optional**: “Alternative is 4-way layer rotation, same complexity, more code.”

You’ll look very confident and structured if you present it this way.

---

---

Nice, let’s make this both practical and runnable.

---

## 5. Real-World Use Cases (short & relatable)

1. **Image Rotation (90° thumbnails)**

   * A grayscale image can be represented as an `n×n` matrix of pixel intensities.
   * Rotating it 90° clockwise to show orientation changes or generate thumbnails is exactly this operation.

2. **Game Boards (Tetris / puzzles / Rubik-like grids)**

   * Board states are often stored as matrices.
   * Rotating the board (or a piece) quickly during simulation or AI search uses this same in-place matrix rotation.

3. **2D Data Visualization / Heatmaps**

   * Sometimes you need to rotate heatmaps or matrices to align axes or match coordinate systems (e.g., rotating sensor grid data coming from hardware).

4. **Matrix-Based Algorithms / Linear Algebra**

   * Some numerical methods explicitly store data in small square matrices and need fast in-place rotations (e.g., transforming coordinates, basis changes in 2D).

5. **UI Layouts / Dashboards**

   * Grid layouts of widgets or tiles can be rotated to change orientation (e.g., rotating layout between landscape and portrait modes) by rotating the underlying matrix.

These are all easy to explain in an interview: “think of rotating a square image / board in-place.”

---

## 6. Full Python Program (with timing + complexity comments)

We’ll implement the **transpose + reverse rows** method (optimal: O(n²) time, O(1) space) and add a small driver plus `timeit` so you can see runtime.

```python
"""
Rotate Matrix by 90 Degrees Clockwise (In-Place)
------------------------------------------------
Approach:
  1) Transpose the square matrix.
  2) Reverse each row.

Let n = len(mat)
Time:
  - Transpose touches each (i,j) once:  O(n^2)
  - Reversing each row: n rows * O(n) each = O(n^2)
  => Overall: O(n^2)

Space:
  - Only a few temporary variables for swaps.
  => O(1) extra space (in-place)
"""

from typing import List
import timeit


# User function Template for python3
def rotate(mat: List[List[int]]) -> None:
    """
    Rotate the matrix mat (n x n) by 90 degrees clockwise, in-place.

    Parameters:
        mat: List[List[int]] - square matrix to be rotated

    This function modifies mat directly and returns None.
    """
    n = len(mat)

    if n == 0:
        return  # nothing to do (O(1))

    # ---- Step 1: Transpose the matrix ----
    # Complexity: O(n^2) time, O(1) extra space
    # We only swap for j > i to avoid double-swapping.
    for i in range(n):
        for j in range(i + 1, n):
            # Swap across the diagonal
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # ---- Step 2: Reverse each row ----
    # Each reverse is O(n), repeated n times => O(n^2)
    for i in range(n):
        mat[i].reverse()  # in-place, O(n) for this row


# ------------------------ Demo + Timing ------------------------ #
if __name__ == "__main__":
    # Sample test matrices
    tests = [
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            "3x3 example"
        ),
        (
            [[1, 2],
             [3, 4]],
            "2x2 example"
        ),
        (
            [[1]],
            "1x1 example"
        ),
    ]

    for mat, label in tests:
        print(f"\n=== {label} ===")
        print("Original matrix:")
        for row in mat:
            print(row)

        # Measure time for a single rotation run
        elapsed = timeit.timeit(lambda: rotate(mat), number=1)

        print("\nRotated matrix (90° clockwise):")
        for row in mat:
            print(row)

        print(f"\nTime taken for rotate(): {elapsed:.8f} seconds")
```

### What this program does

* Defines `rotate(mat)` with the **in-place** optimal algorithm.
* For each sample matrix:

  * Prints the **original** matrix.
  * Rotates it once.
  * Prints the **rotated** matrix.
  * Shows the time taken for that call using `timeit`.

You can drop this into any Python environment (or GFG custom input environment with minimal tweaks) and see both correctness and performance.
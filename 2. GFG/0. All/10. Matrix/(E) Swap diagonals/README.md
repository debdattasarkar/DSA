# Swap diagonals 🔁

**Difficulty:** Easy  
**Accuracy:** 82.28%  
**Submissions:** 6K+  
**Points:** 2  
**Average Time:** 9m  

---

## Problem Statement

Given a square matrix `mat[][]`, the task is to **swap** the elements of the **major** and **minor** diagonals.

- **Major Diagonal:** Elements that lie from the **top-left** corner to the **bottom-right** corner of the matrix (i.e., where row index equals column index).
- **Minor Diagonal:** Elements that lie from the **top-right** corner to the **bottom-left** corner (i.e., where the sum of row and column indices equals `n - 1`).

---

## Examples

### Example 1

**Input:**  
`mat[][] = [[0, 1, 2],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[3, 4, 5],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[6, 7, 8]]`

**Output:**  
`[[2, 1, 0],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[3, 4, 5],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[8, 7, 6]]`

**Explanation:**  
Major Diagonal = `[0, 4, 8]`, Minor Diagonal = `[2, 4, 6]`.  
We are required to swap the diagonal elements of the same row; thus after doing so, major diagonal will become minor and vice versa.

---

### Example 2

**Input:**  
`mat[][] = [[2, 3],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[5, 4]]`

**Output:**  
`[[3, 2],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[4, 5]]`

**Explanation:**  
Major Diagonal = `[2, 4]`, Minor Diagonal = `[3, 5]`.  
We are required to swap the diagonal elements of the same row; thus after doing so, major diagonal will become minor and vice versa.

---

## Constraints

- \( 1 \le \text{mat.size()} \le 500 \)  
- \( 1 \le \text{mat}[i][j] \le 10^6 \)

---

## Expected Complexities

- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Matrix  

---

## Related Articles

- Swap Major Minor Diagonals Square Matrix  

---

---

Let’s tackle this step by step.

---

## 2. Explanation + Step-by-step dry run

### Problem in simple words

You are given a **square matrix** `mat` of size `n x n`.

* **Major (primary) diagonal**: cells where `row == col`
  → positions `(0,0), (1,1), (2,2), ...`

* **Minor (secondary) diagonal**: cells where `row + col == n - 1`
  → positions `(0,n-1), (1,n-2), (2,n-3), ...`

**Task**: For every row `i`, **swap** the element on the major diagonal with the element on the minor diagonal:

```text
swap(mat[i][i], mat[i][n-1-i])
```

If `n` is odd, the middle cell `(mid, mid)` lies on **both** diagonals; swapping it with itself does nothing (which is fine).

Time and space goals:

* Time: **O(n)** (we only visit each row once).
* Extra Space: **O(1)** (in-place).

---

### Indexing logic

For row `i`:

* Major diagonal column = `i`
* Minor diagonal column = `n-1-i`

So we just loop `i = 0 .. n-1` and swap those two positions.

---

### Dry run (3×3 example)

Input:

```text
mat = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
]
n = 3
```

We do for each row `i`:

#### Row i = 0

* Major index: `(0,0)` → value `0`
* Minor index: `(0, n-1-0) = (0,2)` → value `2`

Swap them:

```text
mat[0][0] ↔ mat[0][2]
```

Matrix becomes:

```text
[
  [2, 1, 0],
  [3, 4, 5],
  [6, 7, 8]
]
```

#### Row i = 1

* Major index: `(1,1)` → value `4`
* Minor index: `(1, n-1-1) = (1,1)` → same cell (center)

Swap them (no real change):

```text
mat[1][1] ↔ mat[1][1]   # 4 ↔ 4
```

Matrix stays:

```text
[
  [2, 1, 0],
  [3, 4, 5],
  [6, 7, 8]
]
```

#### Row i = 2

* Major index: `(2,2)` → value `8`
* Minor index: `(2, 0)` → value `6`

Swap:

```text
mat[2][2] ↔ mat[2][0]
```

Matrix becomes:

```text
[
  [2, 1, 0],
  [3, 4, 5],
  [8, 7, 6]
]
```

Which matches the expected output.

---

## 3. Python solutions

We’ll write two versions:

1. **Brute / simple**: create a new matrix and fill it with swapped diagonals.
2. **Optimized in-place**: swap directly in the original matrix (what interviewers expect).

Your required signature:

```python
class Solution:
    def swapDiagonal(self, mat):
        # code here
```

### 3.1 Brute / simple (extra matrix)

```python
from typing import List

class Solution:
    def swapDiagonal_bruteforce(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Brute/simple approach:
        - Create a new matrix result same size as mat.
        - Copy all elements.
        - Then for each row, swap the diagonal entries in the result.

        Time  : O(n^2)  (copying all n^2 elements)
        Space : O(n^2)  (extra matrix)
        """
        n = len(mat)
        if n == 0:
            return mat

        # Create deep copy of mat -> O(n^2) time & space
        result = [row[:] for row in mat]

        # Now just swap diagonals in 'result'
        for i in range(n):          # O(n) rows
            j_major = i            # major diagonal column
            j_minor = n - 1 - i    # minor diagonal column

            # Swap the two entries for this row
            result[i][j_major], result[i][j_minor] = \
                result[i][j_minor], result[i][j_major]

        return result
```

Good for understanding, but not optimal in space.

---

### 3.2 Optimized in-place O(n), O(1)

```python
from typing import List

class Solution:
    def swapDiagonal(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Optimized in-place solution.

        For each row i:
            - major diagonal index  = (i, i)
            - minor diagonal index  = (i, n-1-i)
            Swap mat[i][i] with mat[i][n-1-i].

        Because we only touch two cells per row:
            Time  : O(n)
            Space : O(1) extra (we modify mat in place).

        If n is odd, the middle cell (i == n//2) is on both diagonals.
        Our swap still works: we swap the cell with itself, no issue.
        """
        n = len(mat)
        if n == 0:
            return mat  # nothing to do

        for i in range(n):           # O(n) iterations
            j_major = i             # column of major diagonal
            j_minor = n - 1 - i     # column of minor diagonal

            # Swap values on the same row between the two diagonals
            mat[i][j_major], mat[i][j_minor] = mat[i][j_minor], mat[i][j_major]

        return mat
```

This is the solution you’d show in an interview.

---

## 4. Interview notes: memory trick + likely Q&A

### Quick memory hook

Think:

> **“For row i, swap column i with column n−1−i.”**

or as a chant:

> **“i with n-1-i on each row.”**

If you remember just that, the implementation is trivial.

---

### 5-line pseudo-code skeleton

```text
n = size of matrix
for i from 0 to n-1:
    j_major = i
    j_minor = n-1-i
    swap(mat[i][j_major], mat[i][j_minor])
return mat
```

You can recreate full Python/C++/Java from this in seconds.

---

### Typical interview questions & answers

**Q1: How do you identify major and minor diagonal indices?**

* Major diagonal: `i == j`
* Minor diagonal: `i + j == n - 1`
* For row `i`, those positions are `(i, i)` and `(i, n-1-i)`.

---

**Q2: What’s the time and space complexity of your in-place solution?**

* Time: We loop over `i = 0..n-1` and do O(1) work each time → **O(n)**.
* Space: Only a few variables (`i`, `j_major`, `j_minor`) → **O(1)** extra space.

---

**Q3: What happens when the matrix size `n` is odd? Do you double-swap the center element?**

For the middle row `i = n//2`:

* `j_major = i`
* `j_minor = n-1-i = n-1-(n//2) = n//2` (same index)

So you swap `mat[i][i]` with itself. No problem; the center element remains unchanged, which is exactly what we want (it belongs to both diagonals).

---

**Q4: Could you write a version that doesn’t modify the matrix in place?**

Yes — you can create a new matrix, copy all elements, and perform diagonal swaps only in the result. That uses **O(n²)** extra space and **O(n²)** time, but might be acceptable if in-place mutations aren’t allowed. (That’s essentially our `swapDiagonal_bruteforce`.)

---

**Q5: How would you test this function quickly?**

* Small cases:

  * `1x1` → same matrix.
  * `2x2` → easy to see diagonals swap.
  * `3x3` → like the sample `[0..8]`.
* Check odd `n` specifically to ensure center is unchanged.
* Check with negative numbers or large values; swapping is index-based, so values don’t matter.

---

If you keep in mind:

> **“Square matrix; for each row i, swap mat[i][i] with mat[i][n−1−i].”**

you’ll easily remember both the logic and the code during an interview.

---

---

Got it — let’s finish this one nicely.

---

## 5. Real-World Use Cases (easy to mention in an interview)

This operation sounds “toy”, but you can map it to real scenarios:

1. **Image / Grid Visualization Effects**

   * A square image (or heatmap) is stored as a matrix of pixels/values.
   * Swapping major & minor diagonals is a simple transformation used in:

     * debugging (to visually mark diagonals),
     * making symmetric test patterns,
     * or checking graphics pipelines (if diagonals move correctly, indexing is right).

2. **Board Games / Simulation Grids**

   * Think of a square game board (chess/checkers-like) stored as a matrix.
   * Swapping diagonals is a quick way to:

     * generate symmetric variations of a board position,
     * test AI invariance to certain transformations,
     * or mirror pieces relative to the center.

3. **Matrix-based Test / Sanity Checks**

   * In numerical code, you might deliberately swap diagonals to:

     * verify that diagonal operations (like extracting / modifying them) are correct,
     * or stress-test algorithms that are supposed to be invariant to symmetric transforms.

When asked “Where would you use this?” you can say:

> “Anywhere we represent a square grid — images, game boards, or numerical matrices — and we want a quick symmetric transformation for testing, visualization or generating variants.”

---

## 6. Full Python Program with Timing + Complexity Comments

This script:

* Implements `Solution.swapDiagonal` (in-place, O(n) / O(1)).
* Has a `main()` that:

  * reads `n` and the matrix,
  * calls `swapDiagonal`,
  * prints the resulting matrix,
  * prints total runtime using `time.perf_counter()`.

```python
import time
from typing import List


class Solution:
    def swapDiagonal(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Swap major and minor diagonal elements of a square matrix in-place.

        Let n = number of rows (and columns).

        For each row i:
            - Major diagonal index: (i, i)
            - Minor diagonal index: (i, n-1-i)
            Swap mat[i][i] with mat[i][n-1-i].

        Complexity analysis:
            - Loop over i from 0 to n-1             -> O(n) iterations
            - Each iteration does a constant-time swap -> O(1)
            => Time  : O(n)
            - No extra data structures; just a few variables
            => Space : O(1) auxiliary (matrix modified in-place)
        """
        n = len(mat)
        # If the matrix is empty or 1x1, nothing really to do.
        # Time: O(1), Space: O(1)
        if n <= 1:
            return mat

        # Iterate over each row index i
        # Time of this loop: O(n)
        for i in range(n):
            j_major = i           # column index on the major diagonal
            j_minor = n - 1 - i   # column index on the minor diagonal

            # Swap the elements on the same row but different diagonals.
            # This swap is O(1) time.
            mat[i][j_major], mat[i][j_minor] = mat[i][j_minor], mat[i][j_major]

        # Matrix 'mat' has been modified in-place and returned for convenience.
        return mat


# --------------------------- Driver with timing --------------------------- #

def main():
    """
    Driver function to:
      - Read matrix size and elements from input.
      - Call Solution.swapDiagonal().
      - Print the resulting matrix.
      - Print total execution time.

    Input format (for this standalone program):

        n
        row0_col0 row0_col1 ... row0_col(n-1)
        row1_col0 row1_col1 ... row1_col(n-1)
        ...
        row(n-1)_col0 ... row(n-1)_col(n-1)

    Example:
        3
        0 1 2
        3 4 5
        6 7 8

    Complexity of main (excluding the algorithm):
        - Reading all n^2 entries: O(n^2)
        - Printing the matrix:     O(n^2)
        Time dominates in I/O, not in the O(n) diagonal swap.
    """
    print("Enter matrix size n (for an n x n matrix):")
    line = input().strip()
    if not line:
        print("No input provided.")
        return

    n = int(line)

    print(f"Enter the {n}x{n} matrix (each row on a new line):")
    mat: List[List[int]] = []
    for _ in range(n):
        # Reading each row: O(n) per row, O(n^2) total.
        row = list(map(int, input().split()))
        # Trim or pad defensively if the user doesn't give exactly n numbers.
        if len(row) < n:
            row += [0] * (n - len(row))
        elif len(row) > n:
            row = row[:n]
        mat.append(row)

    solver = Solution()

    # Start the timer right before the algorithm call.
    start_time = time.perf_counter()

    # Core algorithm: O(n) time, O(1) extra space.
    result = solver.swapDiagonal(mat)

    # Stop the timer right after.
    end_time = time.perf_counter()

    print("\nMatrix after swapping major and minor diagonals:")
    for row in result:
        # Printing each row: O(n) per row, O(n^2) for full matrix.
        print(" ".join(map(str, row)))

    print(f"\nTotal elapsed time (seconds): {end_time - start_time:.6f}")


if __name__ == "__main__":
    main()
```

### Example run (conceptual)

Input:

```text
3
0 1 2
3 4 5
6 7 8
```

Output:

```text
Enter matrix size n (for an n x n matrix):
3
Enter the 3x3 matrix (each row on a new line):
0 1 2
3 4 5
6 7 8

Matrix after swapping major and minor diagonals:
2 1 0
3 4 5
8 7 6

Total elapsed time (seconds): 0.0000xx
```

You can paste this into a `.py` file and run it directly.
In an interview or on a platform, you’d typically only submit the `Solution` class with `swapDiagonal`, but this full program is useful for practicing, testing, and seeing actual runtime.

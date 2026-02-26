Here is the complete **README conversion** of the problem exactly as shown in the image, without omitting any part.

---

# 📌 Number of submatrix have sum X

**Difficulty:** Hard
**Accuracy:** 74.57%
**Submissions:** 722+
**Points:** 8

---

## 📝 Problem Statement

Given a matrix `mat[][]` of size `n × m` and an integer `x`, find the number of **square submatrices** whose **sum of elements** is equal to `x`.

---

## 📚 Examples

### Example 1

```
Input:
mat[][] = [
  [2, 4, 7, 8, 10],
  [3, 1, 1, 1, 1],
  [9, 11, 1, 2, 1],
  [12, -17, 1, 1, 1]
]
x = 10

Output: 3
```

**Explanation:**
The sub-squares whose sum of elements = 10 are colored in the matrix.

---

### Example 2

```
Input:
mat[][] = [
  [3, 3, 5, 3],
  [2, 2, 2, 6],
  [11, 2, 2, 4]
]
x = 1

Output: 0
```

**Explanation:**
There is no sub-squares whose sum of elements is 1.

---

## 🔒 Constraints

* `1 ≤ n, m ≤ 100`
* `-10^3 ≤ mat[i][j] ≤ 10^3`
* `-10^9 ≤ x ≤ 10^9`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n * m * min(n, m))`
* **Auxiliary Space:** `O(n * m)`

---

## 🏷 Topic Tags

* prefix-sum
* Data Structures
* Matrix
* Algorithms

---

## 📖 Related Articles

* Count Of Submatrix With Sum X In A Given Matrix

---

---

## 2) Text Explanation (2D Prefix Sum for Square Submatrices)

We need to count **square** submatrices (size `k×k`) whose **sum = x**.

### Brute idea (too slow)

For every top-left `(r,c)` and every size `k`, compute sum by looping all `k*k` cells ⇒ expensive.

### ✅ Optimize with 2D Prefix Sum

Build `prefix[r+1][c+1]` = sum of rectangle from `(0,0)` to `(r,c)`.

Formula:

```
prefix[i+1][j+1] = mat[i][j]
                 + prefix[i][j+1]
                 + prefix[i+1][j]
                 - prefix[i][j]
```

Then any rectangle sum in O(1):

For rectangle with corners:

* top-left `(r1,c1)`
* bottom-right `(r2,c2)`  (inclusive)

```
sum = prefix[r2+1][c2+1]
    - prefix[r1][c2+1]
    - prefix[r2+1][c1]
    + prefix[r1][c1]
```

A **k×k square** starting at `(r,c)` ends at `(r+k-1, c+k-1)`, so we can compute each square sum in **O(1)** and count equals `x`.

Total work:

* sizes `k = 1..min(n,m)`
* top-left positions for each size
  ⇒ `O(n*m*min(n,m))` which matches expected.

---

## Step-by-step Dry Run (small demo)

Take a tiny matrix (easy to see):

```
mat =
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
x = 12
```

### Step 1: Build prefix (4x4, with zero border)

(You don’t need to memorize all values—just the idea.)

### Step 2: Check square sizes

**k = 1**: every single cell sum equals itself → none equals 12

**k = 2**: possible top-left positions: (0,0), (0,1), (1,0), (1,1)

* Square (0,0) covers:

  ```
  1 2
  4 5  sum=12 ✅
  ```

So count = 1 (others won’t match 12 in this example)

That’s how we count using O(1) square sum queries.

---

## 3) Python Codes (Brute + Interview-Expected)

### A) Brute Force (slow but straightforward)

**Time:** `O(n*m*min(n,m)^3)` (because each k×k sum costs k²)
**Space:** `O(1)`

```python
class Solution:
    def countSquare(self, mat, x):
        # Brute force:
        # For every top-left and size k, compute sum by iterating all cells in kxk.
        # Time: O(n*m*sum(k^2)) ~ O(n*m*min(n,m)^3)
        # Space: O(1)

        n = len(mat)
        m = len(mat[0])
        max_size = min(n, m)

        count = 0

        for size in range(1, max_size + 1):
            for top_row in range(0, n - size + 1):
                for left_col in range(0, m - size + 1):
                    square_sum = 0
                    # sum all cells inside the size x size square
                    for r in range(top_row, top_row + size):
                        for c in range(left_col, left_col + size):
                            square_sum += mat[r][c]
                    if square_sum == x:
                        count += 1

        return count
```

---

### B) Optimized (Most Expected): 2D Prefix Sum + enumerate squares ✅

**Time:** `O(n*m*min(n,m))`
**Space:** `O(n*m)`

```python
class Solution:
    def countSquare(self, mat, x):
        # 2D Prefix Sum approach
        # Time: O(n*m) to build prefix + O(n*m*min(n,m)) to count squares
        # Space: O(n*m)

        n = len(mat)
        m = len(mat[0])
        max_size = min(n, m)

        # Build prefix sum array with extra row+col of zeros
        # prefix[r+1][c+1] stores sum of mat[0..r][0..c]
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        # Build prefix
        # Time: O(n*m), Space already allocated
        for r in range(n):
            row_running = 0
            for c in range(m):
                row_running += mat[r][c]
                prefix[r + 1][c + 1] = prefix[r][c + 1] + row_running

        # Helper to get sum of rectangle in O(1)
        def rect_sum(r1, c1, r2, c2):
            # sum of mat[r1..r2][c1..c2] inclusive
            return (prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1])

        # Count all kxk squares
        # Time: O(n*m*min(n,m))
        count = 0
        for size in range(1, max_size + 1):
            for top_row in range(0, n - size + 1):
                bottom_row = top_row + size - 1
                for left_col in range(0, m - size + 1):
                    right_col = left_col + size - 1
                    if rect_sum(top_row, left_col, bottom_row, right_col) == x:
                        count += 1

        return count
```

---

### C) Variant (still prefix sum, slightly cleaner build formula)

Same complexity; some interviewers like the explicit formula:

```python
class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        max_size = min(n, m)

        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        # prefix[i][j] uses 1-based indexing relative to mat
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = (mat[i - 1][j - 1]
                                + prefix[i - 1][j]
                                + prefix[i][j - 1]
                                - prefix[i - 1][j - 1])

        def rect_sum(r1, c1, r2, c2):
            return (prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1])

        count = 0
        for size in range(1, max_size + 1):
            for r in range(n - size + 1):
                for c in range(m - size + 1):
                    if rect_sum(r, c, r + size - 1, c + size - 1) == x:
                        count += 1
        return count
```

---

## 4) Interview Recall + Expected Q&A

### 5-line pseudo-code template (memorize)

```text
build 2D prefix sums P
ans = 0
for size = 1..min(n,m):
  for each top-left (r,c) of size:
     if sumSquare(r,c,size) via P == x: ans++
return ans
```

### Mnemonic

**“Prefix → O(1) Sum → Try all sizes”**

* Prefix makes rectangle sum O(1)
* Square is just a rectangle with equal sides
* Enumerate all square sizes and positions

---

## Common Interview Questions & Answers

**Q1. Why do we need 2D prefix sum?**
A1. To compute any square sum in O(1) instead of O(k²). This reduces total from ~O(min³) to O(min).

**Q2. How do you compute a k×k square sum quickly?**
A2. Using rectangle sum formula on prefix:
`(r,c)` to `(r+k-1, c+k-1)`.

**Q3. Time and space complexity?**
A3. Build prefix: O(n*m). Counting: O(n*m*min(n,m)). Space: O(n*m).

**Q4. Why expected time isn’t O(n²m²)?**
A4. Because we only consider **squares**, not all rectangles, and each sum is O(1) with prefix.

**Q5. Any edge cases?**
A5. Negative values in matrix are allowed (prefix still works). Also x can be negative/large. n or m can be 1.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Image processing / computer vision (sliding square window)**

* Count how many `k×k` pixel blocks have a specific intensity sum (used in feature detection / threshold-based region finding).

2. **Heatmap / sensor grid anomaly detection**

* In a 2D grid of readings, find/count square regions whose total equals a target (e.g., energy/temperature budget hit exactly).

3. **Game boards / grids (pattern scoring)**

* Count square zones on a board whose score sum matches a target (bonus region detection, balancing/analysis).

4. **Finance / analytics on 2D matrices**

* For time×category matrices, detect square windows with a specific aggregate (when a fixed-size window constraint matters).

---

## 6) Full Program (timed end-to-end + sample input/output)

* Uses **2D Prefix Sum + enumerate all square sizes** (expected)
* Prints answer per test case
* Prints total runtime using `time.perf_counter()`

### ✅ Input Format (for this program)

```
t
n m x
row1 values...
row2 values...
...
rown values...
(repeat for t test cases)
```

### ✅ Sample Input

```
2
4 5 10
2 4 7 8 10
3 1 1 1 1
9 11 1 2 1
12 -17 1 1 1
3 4 1
3 3 5 3
2 2 2 6
11 2 2 4
```

### ✅ Sample Output

```
3
0
Total runtime (seconds): 0.0000xxxx
```

---

```python
import time

class Solution:
    def countSquare(self, mat, x):
        """
        Count square submatrices whose sum equals x.

        Approach: 2D Prefix Sum + enumerate all square sizes

        Time Complexity:
          - Build prefix: O(n*m)
          - For each square size s (1..min(n,m)), check all top-left positions:
              O((n-s+1)*(m-s+1)) each in O(1) using prefix
            Total across all sizes: O(n*m*min(n,m))  (matches expected)

        Auxiliary Space:
          - Prefix matrix: O(n*m)
        """

        n = len(mat)
        m = len(mat[0])
        max_size = min(n, m)

        # Step 1: Build prefix sum array with extra border
        # Space: O(n*m)
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        # Step 2: Fill prefix sums
        # Time: O(n*m)
        for r in range(n):
            row_running_sum = 0
            for c in range(m):
                row_running_sum += mat[r][c]
                prefix[r + 1][c + 1] = prefix[r][c + 1] + row_running_sum

        # Step 3: O(1) rectangle sum helper using prefix
        # Time per query: O(1)
        def rect_sum(r1, c1, r2, c2):
            return (prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1])

        # Step 4: Enumerate all square sizes and positions
        # Time: O(n*m*min(n,m))
        count = 0
        for size in range(1, max_size + 1):
            for top_row in range(0, n - size + 1):
                bottom_row = top_row + size - 1
                for left_col in range(0, m - size + 1):
                    right_col = left_col + size - 1

                    # Compute square sum in O(1)
                    if rect_sum(top_row, left_col, bottom_row, right_col) == x:
                        count += 1

        return count


def main():
    # Measure full program runtime (I/O + computation)
    program_start = time.perf_counter()  # Time: O(1)

    t = int(input().strip())  # Time: O(1)
    solver = Solution()

    # Process each test case
    # Total time across tests: Σ O(n*m*min(n,m))
    for _ in range(t):
        # Read dimensions and target sum
        # Time: O(1)
        n, m, x = map(int, input().split())

        # Read matrix
        # Time: O(n*m), Space: O(n*m)
        mat = []
        for _ in range(n):
            mat.append(list(map(int, input().split())))

        # Compute answer
        # Time: O(n*m*min(n,m))
        result = solver.countSquare(mat, x)

        # Output result
        print(result)

    program_end = time.perf_counter()
    print(f"Total runtime (seconds): {program_end - program_start:.8f}")


if __name__ == "__main__":
    main()
```


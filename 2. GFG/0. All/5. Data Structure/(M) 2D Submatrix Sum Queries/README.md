# 2D Submatrix Sum Queries 🧮

**Difficulty:** Medium  
**Accuracy:** 72.23%  
**Submissions:** 914+  
**Points:** 4  
**Average Time:** 20m  

---

## Problem Statement

Given a 2D integer matrix `mat[][]` and a list of queries `queries[][]`, your task is to answer a series of **submatrix sum queries**.

Each query is represented as a list `[r1, c1, r2, c2]`, where:

- `(r1, c1)` is the **top-left** coordinate of the submatrix  
- `(r2, c2)` is the **bottom-right** coordinate of the submatrix (both inclusive)

Your task is to return a list of integers, the **sum of elements** within the specified **submatrix** for each query.

---

## Examples

### Example 1

**Input:**  
`mat[][] = [[1, 2, 3],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1, 1, 0],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[4, 2, 2]]`  

`queries[][] = [[0, 0, 1, 1], [1, 0, 2, 2]]`

**Output:**  
`[5, 10]`

**Explanation:**  

- Query 1 selects submatrix `[[1, 2], [1, 1]]` → sum = `5`.  
- Query 2 selects submatrix `[[1, 1, 0], [4, 2, 2]]` → sum = `10`.

---

### Example 2

**Input:**  
`mat[][] = [[1, 1, 1],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1, 1, 1],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1, 1, 1]]`

`queries[][] = [[1, 1, 2, 2], [0, 0, 2, 2], [0, 2, 2, 2]]`

**Output:**  
`[4, 9, 3]`

**Explanation:**  

- Query 1 selects submatrix `[[1, 1], [1, 1]]` → sum = `4`.  
- Query 2 selects submatrix `[[1, 1, 1], [1, 1, 1], [1, 1, 1]]` → sum = `9`.  
- Query 3 selects submatrix `[[1], [1], [1]]` → sum = `3`.

---

## Constraints

- \(1 \le n \times m, q \le 10^5\)  
- \(0 \le \text{mat}[i][j] \le 10^4\)  
- \(0 \le r1 \le r2 \le n - 1\)  
- \(0 \le c1 \le c2 \le m - 1\)

---

## Expected Complexities

- **Time Complexity:** `O(n × m + q)`  
- **Auxiliary Space:** `O(1)`  

---

## Topic Tags

- prefix-sum  
- Data Structures  
- Algorithms  

---

## Related Articles

- Prefix Sum 2D Array  

---

---

I’ll follow your numbering: explanation + dry run → Python (brute + optimized) → interview memory + Q&A.

---

## 2. Explanation + Step-by-step Dry Run

### Problem recap

* You’re given an `n x m` integer matrix `mat`.
* You’re given `q` queries.
  Each query = `[r1, c1, r2, c2]` (0-based indices).

For each query, you must return:

> Sum of all `mat[i][j]` where `r1 ≤ i ≤ r2` and `c1 ≤ j ≤ c2`.

Naive way: For each query, loop the whole submatrix and add up → **O(area)** per query → worst case `O(q * n * m)` (too slow when both are up to 1e5).

The expected solution: **2D Prefix Sum**.

---

### 2D Prefix Sum Idea

We precompute a helper matrix `pref` where:

> `pref[i][j]` = sum of all elements in rectangle from `(0,0)` to `(i,j)` inclusive.

Visually (top-left anchored):

```
(0,0) ------- (0,j)
  |             |
  |             |
(i,0) ------- (i,j)
```

To build `pref` efficiently:

```text
pref[i][j] = mat[i][j]
             + pref[i-1][j]   (sum above)
             + pref[i][j-1]   (sum to the left)
             - pref[i-1][j-1] (overlap added twice, so subtract once)
```

Handle boundaries (`i == 0` or `j == 0`) by treating missing terms as 0.

Once we have `pref`, we can get any submatrix sum in **O(1)** using inclusion–exclusion.

For query `[r1, c1, r2, c2]`:

Let `S(x, y) = pref[x][y]` be sum from `(0,0)` to `(x,y)`.

Then sum of submatrix `(r1,c1)` to `(r2,c2)` is:

```text
total = S(r2, c2)
        - S(r1-1, c2)       if r1 > 0
        - S(r2, c1-1)       if c1 > 0
        + S(r1-1, c1-1)     if r1 > 0 and c1 > 0
```

This is the 2D version of 1D prefix sum subtraction.

---

### Dry run with Example 1

`mat =`

```text
[
  [1, 2, 3],
  [1, 1, 0],
  [4, 2, 2]
]
```

Queries:

1. `[0, 0, 1, 1]`  → submatrix = top-left 2×2.
2. `[1, 0, 2, 2]`  → submatrix from row 1 to 2, col 0 to 2.

#### Step 1 – Build 2D prefix sum matrix `pref`

We’ll build a **new** matrix `pref` of same size.

Row 0:

* `pref[0][0] = mat[0][0] = 1`
* `pref[0][1] = mat[0][1] + pref[0][0] = 2 + 1 = 3`
* `pref[0][2] = mat[0][2] + pref[0][1] = 3 + 3 = 6`

Row 1:

* `pref[1][0] = mat[1][0] + pref[0][0] = 1 + 1 = 2`
* `pref[1][1] = mat[1][1] + pref[0][1] + pref[1][0] - pref[0][0]`
  = `1 + 3 + 2 - 1 = 5`
* `pref[1][2] = mat[1][2] + pref[0][2] + pref[1][1] - pref[0][1]`
  = `0 + 6 + 5 - 3 = 8`

Row 2:

* `pref[2][0] = mat[2][0] + pref[1][0] = 4 + 2 = 6`
* `pref[2][1] = mat[2][1] + pref[1][1] + pref[2][0] - pref[1][0]`
  = `2 + 5 + 6 - 2 = 11`
* `pref[2][2] = mat[2][2] + pref[1][2] + pref[2][1] - pref[1][1]`
  = `2 + 8 + 11 - 5 = 16`

So:

```text
pref =
[
  [1, 3,  6],
  [2, 5,  8],
  [6,11, 16]
]
```

Check: `pref[2][2] = 16` is the sum of **all** 9 elements → correct.

#### Step 2 – Answer Query 1: `[0,0,1,1]`

Submatrix from `(0,0)` to `(1,1)`.

Using formula:

```text
S(r2,c2) = pref[1][1] = 5
top      = r1 > 0 ? pref[-1][1] : 0 = 0
left     = c1 > 0 ? pref[1][-1] : 0 = 0
overlap  = 0
sum = 5 - 0 - 0 + 0 = 5
```

Matches example (4 cells: 1+2+1+1).

#### Step 3 – Answer Query 2: `[1,0,2,2]`

Submatrix rows 1..2, cols 0..2 (the bottom 2 rows):

```text
S(r2,c2) = pref[2][2] = 16
top      = pref[0][2] = 6        (r1-1 = 0)
left     = c1 > 0 ? ... : 0  ->  0 (since c1=0)
overlap  = 0                     (r1>0 but c1=0 -> no overlap term)

sum = 16 - 6 - 0 + 0 = 10
```

Matches example 2nd answer (sum of `[1,1,0,4,2,2]` = 10).

---

## 3. Python Solutions

We’ll give:

1. A **brute-force** solution: loop each submatrix → easy, but slower.
2. An **optimized 2D prefix** solution (what interviewers expect).

Signature:

```python
class Solution:
    def prefixSum2D(self, mat, queries):
        # code here
```

Returns a list of sums, one per query.

---

### 3.1 Brute-force solution (O(q * area))

```python
from typing import List

class Solution:
    def prefixSum2D_bruteforce(self, mat: List[List[int]],
                               queries: List[List[int]]) -> List[int]:
        """
        Brute-force submatrix sum.

        For each query [r1, c1, r2, c2], we iterate over all i in [r1..r2],
        j in [c1..c2] and sum mat[i][j].

        Let:
            - n, m = dimensions of the matrix
            - q    = number of queries

        Time:
            Worst case, each query covers the whole matrix: O(n*m)
            => total time O(q * n * m).

        Space:
            O(1) extra (besides output).
        """
        n = len(mat)
        if n == 0:
            return []
        m = len(mat[0])

        result = []
        for r1, c1, r2, c2 in queries:
            sub_sum = 0
            # Loop over submatrix rows
            for i in range(r1, r2 + 1):
                # Loop over columns
                for j in range(c1, c2 + 1):
                    sub_sum += mat[i][j]
            result.append(sub_sum)

        return result
```

This is fine conceptually, but too slow for large input.

---

### 3.2 Optimized 2D Prefix Sum (O(n*m + q))

We compute a 2D prefix array once, then answer each query in O(1).

I’ll show a version that **builds a separate `pref`** (so we don’t mutate `mat`). You can easily adapt to in-place if required.

```python
from typing import List

class Solution:
    def prefixSum2D(self, mat: List[List[int]],
                    queries: List[List[int]]) -> List[int]:
        """
        Optimized solution using a 2D prefix sum array.

        Steps:
            1. Precompute prefix sums:
                   pref[i][j] = sum of mat[x][y] for 0 <= x <= i, 0 <= y <= j
               Using recurrence:
                   pref[i][j] = mat[i][j]
                                + (pref[i-1][j]   if i > 0 else 0)
                                + (pref[i][j-1]   if j > 0 else 0)
                                - (pref[i-1][j-1] if i > 0 and j > 0 else 0)

            2. For each query [r1, c1, r2, c2], compute:
                   total = pref[r2][c2]
                           - (pref[r1-1][c2]   if r1 > 0 else 0)
                           - (pref[r2][c1-1]   if c1 > 0 else 0)
                           + (pref[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0)

        Complexity:
            Let n = number of rows, m = number of columns, q = number of queries.

            Building pref: O(n * m)
            Answering queries: O(q) (each is O(1))
            -> Total Time: O(n * m + q)
            Auxiliary Space: O(n * m) for pref.
                (If we overwrite mat with prefix sums, extra space can be O(1).)
        """
        n = len(mat)
        if n == 0:
            return []
        m = len(mat[0])

        # 1) Build 2D prefix sum matrix 'pref'
        pref = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                top = pref[i - 1][j] if i > 0 else 0
                left = pref[i][j - 1] if j > 0 else 0
                diag = pref[i - 1][j - 1] if i > 0 and j > 0 else 0
                pref[i][j] = mat[i][j] + top + left - diag

        # 2) Answer each query in O(1) using the prefix sums.
        answers: List[int] = []
        for r1, c1, r2, c2 in queries:
            total = pref[r2][c2]

            if r1 > 0:
                total -= pref[r1 - 1][c2]
            if c1 > 0:
                total -= pref[r2][c1 - 1]
            if r1 > 0 and c1 > 0:
                total += pref[r1 - 1][c1 - 1]

            answers.append(total)

        return answers
```

If a problem insists on **O(1) auxiliary** space, you can store prefix sums **in-place** inside `mat` instead of in a new `pref` matrix (the formula is the same, just write back into `mat[i][j]`).

---

## 4. Interview Memory Aid + Expected Q&A

### 4.1 Quick “mental hook”

Think:

> **“2D prefix: build top-left sums; query = inclusion–exclusion.”**

Even shorter:

> **“pref[i][j] = self + top + left – diag;
> sum(r1..r2, c1..c2) = S22 − S12 − S21 + S11.”**

(where `S22 = pref[r2][c2]`, etc.)

---

### 4.2 5-line pseudo-code template

Memorize this skeleton:

```text
build pref:
    pref[i][j] = mat[i][j] + top + left - diag
for each query (r1,c1,r2,c2):
    ans = pref[r2][c2]
    if r1>0: ans -= pref[r1-1][c2]
    if c1>0: ans -= pref[r2][c1-1]
    if r1>0 and c1>0: ans += pref[r1-1][c1-1]
return all answers
```

From that, you can re-derive full code very quickly.

---

### 4.3 Likely Interview Questions & Answers

---

**Q1: What is the brute-force approach and its complexity?**

**A:**
For each query `[r1,c1,r2,c2]`, loop over all `i` in `[r1..r2]`, `j` in `[c1..c2]` and add `mat[i][j]`.
If the average submatrix is large, each query costs O(n*m) in the worst case. With q queries, this is `O(q * n * m)`. Too slow when `q` and `n*m` are up to 1e5.

---

**Q2: What is a 2D prefix sum, and how do you compute it?**

**A:**
A 2D prefix sum `pref[i][j]` is the sum of all elements in the rectangle from `(0,0)` to `(i,j)` inclusive.
We compute it with the recurrence:

```text
pref[i][j] = mat[i][j]
             + (pref[i-1][j]   if i > 0 else 0)
             + (pref[i][j-1]   if j > 0 else 0)
             - (pref[i-1][j-1] if i > 0 and j > 0 else 0)
```

This avoids recomputing sums and can be built in O(n*m).

---

**Q3: How do you get a submatrix sum from the prefix sums?**

**A:**
For `r1,c1,r2,c2`:

```text
sum = pref[r2][c2]
      - (pref[r1-1][c2]   if r1 > 0 else 0)
      - (pref[r2][c1-1]   if c1 > 0 else 0)
      + (pref[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0)
```

This is inclusion–exclusion: total rectangle minus the extra strips plus the overlapping corner.

---

**Q4: What are the time and space complexities of your optimized solution?**

**A:**

* Building the prefix sum: `O(n * m)`.
* Each query: `O(1)` (constant number of operations).
* Total: `O(n * m + q)`.

Space:

* If I store prefix in a separate matrix: `O(n * m)` extra.
* If I overwrite `mat` with prefix sums: `O(1)` auxiliary space besides the input.

---

**Q5: How is this related to 1D prefix sums?**

**A:**
It’s the straightforward 2D generalization:

* In 1D: `pref[i] = pref[i-1] + arr[i]`; subarray sum = `pref[r] - pref[l-1]`.
* In 2D, we extend to both dimensions and use inclusion–exclusion to avoid double-counting.

---

If you remember:

> **“pref[i][j] = self + top + left – diag; query = S22 − S12 − S21 + S11”**

you’ll be able to reconstruct the whole logic and code quickly and explain it confidently in an interview.

---

---

Great, let’s close this problem out properly.

---

## 5. Real-World Use Cases (easy to explain to an interviewer)

Think of **any 2D grid of numbers** where you often need **sum over rectangles**:

1. **Image Processing / Computer Vision**

   * Grayscale / color images are just 2D arrays of pixel intensities.
   * Common tasks: “What’s the total brightness in this rectangular patch?”, “What’s the average color of this region?”
   * 2D prefix sums (often called *integral images*) let you answer these region-sum queries in O(1) no matter how big the patch is.
   * Directly related to algorithms like Haar features, fast box filters, etc.

2. **Heatmaps & Analytics Dashboards**

   * Web/app analytics may store a click heatmap as an `n x m` grid over the screen.
   * Questions like: “How many clicks were in this UI area?”, “How many events in this region of the map?” → rectangular sum queries.
   * A 2D prefix sum structure makes such dashboards respond instantly even with huge logs.

3. **Geospatial / Population Density Queries**

   * Divide a city/country into a grid; each cell holds population, pollution, or traffic count.
   * Queries like “What is the total population inside this bounding box?” translate to submatrix sum queries.
   * 2D prefix sums let city planners or routing systems answer such questions very quickly.

4. **Game Maps / Simulation Grids**

   * In strategy games or simulations, a 2D grid can store resources, elevation, units, etc.
   * You might need: “What’s the total resource in this rectangular area?” or “Total damage in this AoE rectangle?”
   * Again, that’s exactly submatrix sums.

Or in a sentence you can tell the interviewer:

> “Whenever we maintain a 2D grid — images, heatmaps, GIS grids, or game maps — and we need fast aggregate over rectangles, we use a 2D prefix-sum structure like this.”

---

## 6. Full Python Program with Timing & Complexity Comments

Below is a complete, runnable Python script:

* Implements the optimized 2D prefix sum solution.
* Reads `n, m` (matrix size), then the matrix, then `q` (number of queries) and the queries.
* Calls `prefixSum2D`, prints each query’s sum, and prints total runtime.

```python
import time
from typing import List


class Solution:
    def prefixSum2D(self, mat: List[List[int]],
                    queries: List[List[int]]) -> List[int]:
        """
        Optimized 2D prefix-sum solution.

        mat:     n x m matrix of integers
        queries: list of [r1, c1, r2, c2] (0-based, inclusive)

        IDEA:
            1) Precompute a 2D prefix sum matrix 'pref'
               where pref[i][j] stores sum of elements in rectangle
               (0,0) to (i,j), both inclusive.

            2) Use inclusion–exclusion to answer each submatrix query in O(1):
               sum(r1..r2, c1..c2) =
                     pref[r2][c2]
                   - pref[r1-1][c2]     if r1 > 0
                   - pref[r2][c1-1]     if c1 > 0
                   + pref[r1-1][c1-1]   if r1 > 0 and c1 > 0

        COMPLEXITY:
            Let n = number of rows, m = number of columns, q = queries count.

            - Building 'pref':
                * We touch each cell once and do O(1) work per cell
                * Time  : O(n * m)
                * Space : O(n * m) extra for 'pref' (auxiliary space)

            - Answering queries:
                * Each query uses a constant number of operations on 'pref'
                * Time  : O(q)
                * Space : O(1) extra beyond outputs

            -> Overall Time  : O(n * m + q)
               Overall Space : O(n * m)
        """
        n = len(mat)
        if n == 0:
            # Empty matrix: every query sum is 0.
            return []
        m = len(mat[0])

        # ------------------ 1) Build 2D prefix sum matrix ------------------ #
        # Allocate pref with same shape as mat.
        # Time:  O(n * m) for allocation
        # Space: O(n * m) extra
        pref = [[0] * m for _ in range(n)]

        # Fill pref using the recurrence.
        # Outer loop: n iterations, inner loop: m iterations => O(n * m) time.
        for i in range(n):
            for j in range(m):
                # sum of rectangle above current cell: O(1)
                top = pref[i - 1][j] if i > 0 else 0
                # sum of rectangle to the left: O(1)
                left = pref[i][j - 1] if j > 0 else 0
                # overlap (top-left sub-rectangle) counted twice, subtract once: O(1)
                diag = pref[i - 1][j - 1] if i > 0 and j > 0 else 0

                # current prefix sum: O(1) operation
                pref[i][j] = mat[i][j] + top + left - diag

        # ------------------ 2) Answer each query in O(1) ------------------ #
        answers: List[int] = []

        # Loop over all queries: O(q)
        for r1, c1, r2, c2 in queries:
            # Start with sum of (0,0) to (r2,c2) : O(1)
            total = pref[r2][c2]

            # Subtract the part above r1 if needed: O(1)
            if r1 > 0:
                total -= pref[r1 - 1][c2]

            # Subtract the part left of c1 if needed: O(1)
            if c1 > 0:
                total -= pref[r2][c1 - 1]

            # Add back the top-left overlapping area if both r1>0 and c1>0: O(1)
            if r1 > 0 and c1 > 0:
                total += pref[r1 - 1][c1 - 1]

            answers.append(total)

        return answers


# --------------------------- Driver with timing --------------------------- #

def main():
    """
    Driver for local testing / demonstration.

    Input format (simple, interactive style):

        n m
        mat[0][0] mat[0][1] ... mat[0][m-1]
        ...
        mat[n-1][0] ...       mat[n-1][m-1]
        q
        r1 c1 r2 c2   (q lines of queries)

    Example input:
        3 3
        1 2 3
        1 1 0
        4 2 2
        2
        0 0 1 1
        1 0 2 2

    Example output:
        Submatrix sums for each query:
        5
        10

        Total elapsed time (seconds): 0.0000xx
    """

    print("Enter n (rows) and m (cols):")
    first_line = input().strip()
    if not first_line:
        print("No input provided.")
        return
    n, m = map(int, first_line.split())

    print(f"Enter the {n}x{m} matrix rows:")
    mat: List[List[int]] = []
    # Read n rows; each row reading is O(m) => O(n * m) input time.
    for _ in range(n):
        row = list(map(int, input().split()))
        # Simple safety: trim or pad to length m
        if len(row) < m:
            row += [0] * (m - len(row))
        elif len(row) > m:
            row = row[:m]
        mat.append(row)

    print("Enter number of queries q:")
    q_line = input().strip()
    if not q_line:
        print("No queries.")
        return
    q = int(q_line)

    print(f"Enter {q} queries (r1 c1 r2 c2):")
    queries: List[List[int]] = []
    # Reading q queries -> O(q) input time.
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        queries.append([r1, c1, r2, c2])

    solver = Solution()

    # Start timing just before running the core algorithm.
    start_time = time.perf_counter()

    # Core algorithm: O(n * m + q) time, O(n * m) extra space for prefix matrix.
    answers = solver.prefixSum2D(mat, queries)

    # Stop timing right after.
    end_time = time.perf_counter()

    print("\nSubmatrix sums for each query:")
    for ans in answers:
        print(ans)

    print(f"\nTotal elapsed time (seconds): {end_time - start_time:.6f}")


if __name__ == "__main__":
    main()
```

### How a sample run looks (mentally)

Input:

```text
3 3
1 2 3
1 1 0
4 2 2
2
0 0 1 1
1 0 2 2
```

Output:

```text
Enter n (rows) and m (cols):
3 3
Enter the 3x3 matrix rows:
1 2 3
1 1 0
4 2 2
Enter number of queries q:
2
Enter 2 queries (r1 c1 r2 c2):
0 0 1 1
1 0 2 2

Submatrix sums for each query:
5
10

Total elapsed time (seconds): 0.0000xx
```

You can paste this file into a Python interpreter and run it directly.
In an interview or on a coding site, you’d normally only submit the `Solution` class with `prefixSum2D`, but this full script is handy for practice, testing, and understanding performance.

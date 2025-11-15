Here’s the **complete README-style conversion** of your uploaded image — **nothing omitted**:

---

# 🔍 Search in a Sorted Matrix

**Difficulty:** Medium
**Accuracy:** 56.27%
**Submissions:** 147K+
**Points:** 4

---

## 🧠 Problem Statement

Given a strictly sorted 2D matrix **mat[][]** of size **n × m** and a number **x**, find whether the number **x** is present in the matrix or not.

**Note:**
In a strictly sorted matrix,

* each row is sorted in **strictly increasing order**, and
* the first element of the *i-th* row (i ≠ 0) is greater than the **last element** of the *(i−1)-th* row.

---

## 🧩 Examples

### Example 1

**Input:**

```
mat[][] = [[1, 5, 9],
           [14, 20, 21],
           [30, 34, 43]],
x = 14
```

**Output:**

```
true
```

**Explanation:**
14 is present in the matrix, so output is `true`.

---

### Example 2

**Input:**

```
mat[][] = [[1, 5, 9, 11],
           [14, 20, 21, 26],
           [30, 34, 43, 50]],
x = 42
```

**Output:**

```
false
```

**Explanation:**
42 is not present in the matrix.

---

### Example 3

**Input:**

```
mat[][] = [[87, 96, 99],
           [101, 103, 111]],
x = 101
```

**Output:**

```
true
```

**Explanation:**
101 is present in the matrix.

---

## ⚙️ Constraints

* ( 1 \leq n, m \leq 1000 )
* ( 1 \leq mat[i][j] \leq 10^9 )
* ( 1 \leq x \leq 10^9 )

---

## ⏱️ Expected Complexities

| Type                | Complexity    |
| ------------------- | ------------- |
| **Time Complexity** | O(log(n × m)) |
| **Auxiliary Space** | O(1)          |

---

## 🏢 Company Tags

* Paytm
* Accolite
* MakeMyTrip
* Ola Cabs
* Oracle
* Visa
* Goldman Sachs
* Directi
* Groupon
* InMobi
* One97
* Polycom
* TinyOwl

---

## 🧩 Topic Tags

* Searching
* Matrix
* Data Structures
* Algorithms

---

## 💼 Related Interview Experiences

* Accolite Interview Experience Set 16 Campus
* Paytm Interview Experience Set 8 Hiring Drive For Backend Engineer

---

## 📚 Related Articles

* [Search Element in a Sorted Matrix](https://www.geeksforgeeks.org/search-element-sorted-matrix/)

---

---

Awesome — let’s turn **Search in a Sorted Matrix** into an interview slam-dunk.

---

## 2) Explanation + step-by-step dry run

### Problem in one line

Matrix `mat` is **row-wise strictly increasing**, and **the first element of each row > last of previous row**. Given `x`, decide if it exists.

That property means the entire matrix acts like **one sorted 1-D array** of length `n*m`.
So we can do **Binary Search** on indices `0..n*m-1` and map:

* `row = mid // m`
* `col = mid % m`

### Dry run (Example 1)

```
mat = [[1, 5, 9],
       [14, 20, 21],
       [30, 34, 43]]
x = 14,  n=3, m=3  → total = 9

l=0, r=8
mid=4 → (4//3,4%3)=(1,1) → mat[1][1]=20 > 14 → r=3
mid=(0+3)//2=1 → (0,1)=5 < 14 → l=2
mid=(2+3)//2=2 → (0,2)=9 < 14 → l=3
mid=3 → (1,0)=14 == x  → return True
```

---

## 3) Python solutions (brute → linear “staircase” → optimal binary search)

Use your required signature:

```python
class Solution:
    def searchMatrix(self, mat, x):
        # code here
```

### A) Brute force (teaching baseline)

```python
class Solution:
    def searchMatrix(self, mat, x):
        """
        Scan every cell.
        Time:  O(n*m)
        Space: O(1)
        """
        if not mat or not mat[0]:
            return False
        for row in mat:
            for val in row:
                if val == x:
                    return True
        return False
```

### B) “Staircase” search from top-right (O(n+m))

Works because rows & columns are increasing.

```python
class Solution:
    def searchMatrix(self, mat, x):
        """
        Start at top-right. If current > x -> move left; if current < x -> move down.
        Time:  O(n + m)
        Space: O(1)
        """
        if not mat or not mat[0]:
            return False
        n, m = len(mat), len(mat[0])
        r, c = 0, m - 1
        while r < n and c >= 0:
            cur = mat[r][c]
            if cur == x:
                return True
            if cur > x:
                c -= 1      # move left to smaller numbers
            else:
                r += 1      # move down to larger numbers
        return False
```

### C) Optimal Binary Search on the “flattened” matrix (O(log(n*m)))

This is the most expected answer given the problem’s special note.

```python
class Solution:
    def searchMatrix(self, mat, x):
        """
        Binary search treating matrix as 1-D sorted array.
        Map mid -> (mid//m, mid%m).
        Time:  O(log(n*m))
        Space: O(1)
        """
        if not mat or not mat[0]:
            return False
        n, m = len(mat), len(mat[0])

        left, right = 0, n * m - 1
        while left <= right:
            mid = (left + right) // 2
            r, c = divmod(mid, m)       # r=mid//m, c=mid%m
            val = mat[r][c]
            if val == x:
                return True
            if val < x:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

**Edge cases**: empty matrix; `n*m==1`; values near bounds (`1` and `1e9`). Binary search handles all.

---

## 4) Interview “how to remember” + Q&A

### 5-line pseudo you can say out loud

```
n=len(mat); m=len(mat[0])
l=0; r=n*m-1
while l<=r:
  mid=(l+r)//2; (i,j)=(mid//m, mid%m)
  if mat[i][j]==x: return True
  elif mat[i][j]<x: l=mid+1
  else: r=mid-1
return False
```

**Mnemonic:** **“Think 1-D** → left/right/mid → **mid→(row,col)** with `//` and `%`.”

### Likely interviewer questions (and crisp answers)

* **Q:** Why binary search?
  **A:** Because the matrix is globally sorted when flattened (each row sorted and row₍i₎[0] > row₍i−1₎[m−1]). So it’s a single increasing array of size `n*m`.

* **Q:** Time & space?
  **A:** `O(log(n*m))` time, `O(1)` space.

* **Q:** What if rows are sorted but the “first of next row > last of previous” is **not** guaranteed?
  **A:** Then we can’t flatten globally; use the **staircase** method `O(n+m)` starting from top-right (or binary search each row with `O(n*log m)`).

* **Q:** Any pitfalls?
  **A:** Be careful with **index mapping** (`i=mid//m`, `j=mid%m`) and **bounds** (`left<=right`). Handle empty matrix.

* **Q:** Why not convert to a real 1-D list?
  **A:** Extra space is unnecessary; mapping is `O(1)` and avoids copying `O(n*m)` data.

---

### Quick comparison

| Approach                    | Time            | Space    | When to use                                            |
| --------------------------- | --------------- | -------- | ------------------------------------------------------ |
| Brute scan                  | O(n·m)          | O(1)     | Baseline / sanity                                      |
| Staircase                   | O(n+m)          | O(1)     | When only rows & cols are increasing (no global order) |
| **Binary search (flatten)** | **O(log(n·m))** | **O(1)** | **When note’s global-order property holds** ✅          |

You’re set: pick **Binary Search on flattened** as your primary solution; mention **Staircase** as the alternative when the global-order note doesn’t hold.

---

---

## 5) Real-World Use Cases (short & relatable)

* **Database sharding index lookup:** Shards (rows) are sorted and non-overlapping; within each shard keys are sorted. Checking if a key exists maps directly to “flattened binary search”.
* **Time-series block search:** Data is stored in time-ordered blocks; each block’s earliest timestamp is greater than the previous block’s last timestamp. Finding a timestamp → matrix search.
* **Paged file/SSD directory:** Pages (rows) in ascending order, and entries inside each page sorted. Presence check can be done with the same mapping.

All rely on: *row-wise sorted + each row’s first > previous row’s last* ⇒ the matrix behaves like **one big sorted array**.

---

## 6) Full Program (with timing + inline complexity notes)

```python
"""
Search in a Sorted Matrix
-------------------------
Property:
  - Each row is strictly increasing
  - First element of row i (i>0) > last element of row i-1
Consequence: The matrix flattened row-major is globally sorted.

Preferred solution: Binary Search over the virtual 1-D array of length n*m.
Time:  O(log(n*m))
Space: O(1)
"""

import timeit
from typing import List


class Solution:
    # ---------- Optimal: Binary Search on virtual 1-D array ----------
    def searchMatrix(self, mat: List[List[int]], x: int) -> bool:
        """
        Steps & complexity:
          - Guard checks: O(1)
          - Binary search over [0..n*m-1]: O(log(n*m)) iterations
          - Index map mid -> (r, c) using divmod: O(1) per iteration
          - Space: O(1)
        """
        if not mat or not mat[0]:
            return False

        n, m = len(mat), len(mat[0])  # O(1)
        left, right = 0, n * m - 1    # virtual 1-D indices

        while left <= right:          # O(log(n*m)) iterations
            mid = (left + right) // 2
            r, c = divmod(mid, m)     # r = mid // m, c = mid % m
            val = mat[r][c]           # O(1)

            if val == x:
                return True
            if val < x:
                left = mid + 1
            else:
                right = mid - 1

        return False

    # ---------- Alternative: Staircase search (when only rows & cols are sorted) ----------
    def searchMatrixStaircase(self, mat: List[List[int]], x: int) -> bool:
        """
        Works if each row & column is increasing (no global order required).
        Start top-right; move left if current > x, else move down.
        Time:  O(n + m)
        Space: O(1)
        """
        if not mat or not mat[0]:
            return False

        n, m = len(mat), len(mat[0])
        r, c = 0, m - 1
        while r < n and c >= 0:
            cur = mat[r][c]
            if cur == x:
                return True
            if cur > x:
                c -= 1
            else:
                r += 1
        return False


# ------------------------------- Demo & Timing -------------------------------
if __name__ == "__main__":
    tests = [
        # (matrix, x, expected)
        (
            [[1, 5, 9],
             [14, 20, 21],
             [30, 34, 43]],
            14, True
        ),
        (
            [[1, 5, 9, 11],
             [14, 20, 21, 26],
             [30, 34, 43, 50]],
            42, False
        ),
        (
            [[87, 96, 99],
             [101, 103, 111]],
            101, True
        ),
        (
            [[1]], 1, True
        ),
    ]

    sol = Solution()
    print("Search in a Sorted Matrix — Binary Search (O(log(n*m)))\n")

    for mat, x, expected in tests:
        # Time the single call (includes the full binary search work)
        elapsed = timeit.timeit(lambda: sol.searchMatrix(mat, x), number=1)
        ans = sol.searchMatrix(mat, x)
        print(f"matrix={mat}, x={x} -> {ans} (expected {expected}), time={elapsed:.6f}s")

    # Optional: show staircase on a matrix where rows/cols are increasing (works too)
    print("\nStaircase method on the first test (O(n+m)):")
    mat0, x0, exp0 = tests[0]
    elapsed2 = timeit.timeit(lambda: sol.searchMatrixStaircase(mat0, x0), number=1)
    ans2 = sol.searchMatrixStaircase(mat0, x0)
    print(f"matrix={mat0}, x={x0} -> {ans2} (expected {exp0}), time={elapsed2:.6f}s")
```

### Sample Output

```
Search in a Sorted Matrix — Binary Search (O(log(n*m)))

matrix=[[1, 5, 9], [14, 20, 21], [30, 34, 43]], x=14 -> True (expected True), time=0.0000xxs
matrix=[[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x=42 -> False (expected False), time=0.0000xxs
matrix=[[87, 96, 99], [101, 103, 111]], x=101 -> True (expected True), time=0.0000xxs
matrix=[[1]], x=1 -> True (expected True), time=0.0000xxs

Staircase method on the first test (O(n+m)):
matrix=[[1, 5, 9], [14, 20, 21], [30, 34, 43]], x=14 -> True (expected True), time=0.0000xxs
```

**Interview recap**

* With the given global-order property, treat matrix as **one sorted array**.
* Compute `(row, col)` from `mid` using `divmod(mid, m)`.
* Complexity: **O(log(n*m))** time, **O(1)** space.
* If that global property is missing (only row & column increasing), mention the **staircase** method `O(n+m)` as a robust alternative.

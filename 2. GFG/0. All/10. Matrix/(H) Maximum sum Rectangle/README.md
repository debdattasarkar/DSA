
---

# 🟩 Maximum Sum Rectangle in a 2D Matrix

**Difficulty:** Hard
**Accuracy:** 49.78%
**Submissions:** 45K+
**Points:** 8
**Average Time:** —

---

## 🧾 Problem Statement

Given a 2D matrix `mat[][]` with dimensions `n x m`, your task is to **find the maximum possible sum of any submatrix** (i.e., a rectangular section of the matrix).

---

## ✍️ Input

* A matrix of integers of dimensions `n x m`

---

## ✅ Output

* Return the **maximum sum** obtainable by any rectangular submatrix within the matrix.

---

## 🔍 Examples

### Example 1

```python
Input:
mat[][] = [[ 1,  2, -1, -4, -20],
           [-8, -3,  4,  2,   1],
           [ 3,  8, 10,  1,   3],
           [-4, -1,  1,  7,  -6]]

Output: 29
```

#### Explanation:

* The green highlighted submatrix is:

```
-3  4  2
 8 10  1
-1  1  7
```

* The sum of the rectangle is `29`, which is the maximum.

---

### Example 2

```python
Input:
mat[][] = [[-1, -2],
           [-3, -4]]

Output: -1
```

#### Explanation:

* The optimal submatrix is just `[-1]` (the highest value in the matrix).

---

## 🔒 Constraints

```
1 ≤ n, m ≤ 300
-1000 ≤ mat[i][j] ≤ 1000
```

---

## 📊 Expected Time and Space Complexity

* **Time Complexity:** O(n × m²)
* **Auxiliary Space:** O(n)

---

## 💼 Company Tags

> Flipkart, Accolite, Amazon, Samsung, D-E Shaw, FactSet, Walmart

---

## 🧠 Topic Tags

> prefix-sum, Matrix, Kadane, Data Structures, Algorithms

---

## 📌 Related Interview Experiences

* Amazon Interview Experience Set 355 | 1 Year Experience
* Accolite Interview Experience Set 15 | Campus
* Samsung R\&D Bangalore Internship Experience 2018

---

## 📚 Related Articles

* Maximum Sum Rectangle In A 2D Matrix – DP 27

---

---


Here is the detailed breakdown for the **“Maximum Sum Rectangle in a 2D Matrix”** problem:

---

### ✅ **2. Text Explanation with Step-by-Step Dry Run**

#### Problem:

Given an `n x m` matrix `mat[][]`, find the **maximum sum of any submatrix** (i.e., any contiguous rectangle inside the matrix).

---

#### 💡 Key Idea:

We reduce this **2D problem into a series of 1D Kadane’s problems**:

* Fix two rows (start\_row and end\_row)
* Collapse all columns between these rows into a 1D array of cumulative sums
* Run Kadane’s algorithm on this 1D array to find the max subarray sum (which is the max rectangle sum for those rows)
* Repeat for all pairs of rows.

---

#### 📘 Example Input:

```python
mat = [
    [1,  2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3,  8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
```

---

#### 🔁 Dry Run:

Let’s take rows from `0` to `2`:

* Compress columns:

```python
temp = [ (1 + -8 + 3), (2 + -3 + 8), (-1 + 4 + 10), (-4 + 2 + 1), (-20 + 1 + 3) ]
     = [ -4, 7, 13, -1, -16 ]
```

* Apply Kadane’s Algorithm on this:

  * Max subarray sum = `7 + 13 = 20`

Repeat for all pairs → max overall = `29`

---

### ✅ **3. Optimized Python Code**

```python
class Solution:
    def maxRectSum(self, mat):
        n = len(mat)
        m = len(mat[0])

        max_sum = float('-inf')

        # Loop over all pairs of rows
        for top in range(n):
            temp = [0] * m
            for bottom in range(top, n):

                # Add current row to the temp array (column-wise sum)
                for col in range(m):
                    temp[col] += mat[bottom][col]

                # Apply Kadane's Algorithm on temp
                curr_sum = temp[0]
                max_ending_here = temp[0]

                for i in range(1, m):
                    max_ending_here = max(temp[i], max_ending_here + temp[i])
                    curr_sum = max(curr_sum, max_ending_here)

                max_sum = max(max_sum, curr_sum)

        return max_sum
```

---

### 🧪 Sample Driver Program

```python
mat = [
    [1,  2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3,  8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

sol = Solution()
print("Maximum Rectangular Sum:", sol.maxRectSum(mat))
```

---

### ⏱ Time and Space Complexity

| Component         | Complexity     |
| ----------------- | -------------- |
| Time              | **O(n² \* m)** |
| Space (auxiliary) | **O(m)**       |

Where `n = number of rows`, `m = number of columns`.

---

### ✅ **4. Expected Interview Questions and Answers**

| Question                                          | Answer                                                                                             |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Q1:** What's the brute-force approach?          | Check all `O(n⁴)` submatrices by computing sum for each — very slow.                               |
| **Q2:** How did you optimize it?                  | Reduced the 2D sum to 1D by fixing two rows and using Kadane’s algorithm.                          |
| **Q3:** What is Kadane’s algorithm?               | It finds the maximum sum contiguous subarray in O(n).                                              |
| **Q4:** Can we reduce space further?              | Yes, we use only `O(m)` extra space with `temp[]`.                                                 |
| **Q5:** Does this work for all negative elements? | Yes. Kadane handles this by considering max of current element or extending the previous subarray. |

---

Here's the **full Python program** with:

* ✅ Inline comments explaining every logic step
* ✅ Time & space complexity breakdown
* ✅ Sample input and output
* ✅ Timing using `time` module for performance measurement

---

### ✅ Full Program

```python
import time

class Solution:
    def maxRectSum(self, mat):
        # Time Complexity: O(n * n * m), where n = rows, m = cols
        # Space Complexity: O(m) for the temporary array used in Kadane's
        n = len(mat)
        m = len(mat[0])

        max_sum = float('-inf')

        # Step 1: Fix top row and iterate all possible bottom rows
        for top in range(n):
            # Create a temporary 1D array to hold column-wise sums
            temp = [0] * m

            for bottom in range(top, n):
                # Step 2: Accumulate row values into temp[]
                for col in range(m):
                    temp[col] += mat[bottom][col]

                # Step 3: Apply Kadane's algorithm to temp[] for max 1D subarray sum
                curr_sum = max_ending_here = temp[0]
                for i in range(1, m):
                    max_ending_here = max(temp[i], max_ending_here + temp[i])
                    curr_sum = max(curr_sum, max_ending_here)

                # Update global maximum
                max_sum = max(max_sum, curr_sum)

        return max_sum

# ---------------- Main Program with Timing ----------------

if __name__ == "__main__":
    mat = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]

    print("Input Matrix:")
    for row in mat:
        print(row)

    start_time = time.time()

    sol = Solution()
    result = sol.maxRectSum(mat)

    end_time = time.time()

    print("\n✅ Maximum Sum of Any Submatrix:", result)
    print("⏱️ Time taken to run (in seconds):", end_time - start_time)
```

---

### 🔍 Output for Given Input

```
Input Matrix:
[1, 2, -1, -4, -20]
[-8, -3, 4, 2, 1]
[3, 8, 10, 1, 3]
[-4, -1, 1, 7, -6]

✅ Maximum Sum of Any Submatrix: 29
⏱️ Time taken to run (in seconds): ~0.00004s
```

---

### ⏳ Complexity Recap

* **Time:** `O(n^2 * m)`
  → Two nested loops for row pairs (`n^2`) and Kadane's for `m` columns.

* **Space:** `O(m)`
  → Only a temp array for column compression.

----

# 🌍 Real-World Use Cases

Here are **key real-world use cases** where the **Maximum Sum Rectangle in a 2D Matrix** (also known as the **Kadane’s 2D extension**) is highly relevant:

---

### ✅ 1. **Image Processing & Computer Vision**

* **Use case:** Identifying the brightest (or darkest) region in a grayscale image.
* **Explanation:** Each pixel's intensity is treated as a matrix cell. You want the **region (submatrix)** with maximum (or minimum) total brightness.
* **Example:** Heatmaps from thermal cameras.

---

### ✅ 2. **Financial Analytics**

* **Use case:** Identifying the most profitable period for multi-dimensional trading data.
* **Explanation:** Rows represent time, columns represent assets. Finding the submatrix with the maximum net profit across multiple assets and periods.

---

### ✅ 3. **Geospatial Analysis**

* **Use case:** Finding the most fertile region or region with highest rainfall in a map grid.
* **Explanation:** Environmental or sensor readings stored in 2D matrix form; maximum sum submatrix identifies ideal zones for agriculture or hydrology.

---

### ✅ 4. **Game Development & AI**

* **Use case:** Locating the most valuable zone in a grid-based game (e.g., strategy or resource collection).
* **Explanation:** Game maps may use 2D scores or threat levels. Submatrix with max score indicates optimal attack/defense zone.

---

### ✅ 5. **Data Center Load Balancing**

* **Use case:** Identifying peak load regions in CPU/GPU temperature or power matrices.
* **Explanation:** Servers are mapped in 2D racks. Finding max heat or energy consumption zone helps in thermal/power optimization.

---

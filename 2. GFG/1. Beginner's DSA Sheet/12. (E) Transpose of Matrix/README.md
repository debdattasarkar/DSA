Got it — here’s the **README** conversion for your "Transpose of Matrix" problem, preserving all details.

---

# Transpose of Matrix

**Difficulty:** Easy
**Accuracy:** 66.5%
**Submissions:** 113K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

You are given a square matrix of size `n x n`. Your task is to find the **transpose** of the given matrix.

The **transpose** of a matrix is obtained by converting all the rows to columns and all the columns to rows.

---

## Examples

### Example 1

**Input:**

```
mat = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]
```

**Output:**

```
[
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]
```

**Explanation:** Converting rows into columns and columns into rows.

---

### Example 2

**Input:**

```
mat = [
    [1, 2],
    [9, -2]
]
```

**Output:**

```
[
    [1, 9],
    [2, -2]
]
```

**Explanation:** Converting rows into columns and columns into rows.

---

## Constraints

* $1 \leq n \leq 10^3$
* $-10^9 \leq \text{mat}[i][j] \leq 10^9$

---

## Expected Complexities

* **Time Complexity:** $O(n^2)$
* **Auxiliary Space:** $O(1)$

---

## Company Tags

* MakeMyTrip
* InfoEdge
* Bloomberg

---

## Topic Tags

* Matrix
* Data Structures

---

## Related Interview Experiences

* Makemytrip Interview Experience Set 10 On Campus

---

## Related Articles

* [Program To Find Transpose Of A Matrix](https://www.geeksforgeeks.org/program-to-find-transpose-of-a-matrix/)

---

---

Got it — here’s the **full program** for the **Transpose of Matrix** problem with:

* **In-place version** (most expected in interviews for square matrices)
* **Full inline comments** explaining complexity step-by-step
* **Sample input/output**
* **`timeit` usage** to measure runtime of the complete program

---

```python
import timeit

class Solution:
    def transpose(self, mat):
        """
        Transpose a square matrix in-place.

        Parameters:
        mat (List[List[int]]): The square matrix to be transposed.

        Returns:
        List[List[int]]: The transposed matrix (same object as input).

        Time Complexity:
        ----------------
        O(n^2) — Because we iterate over roughly half of the matrix's elements
                 (upper triangle excluding diagonal), but asymptotically this is still O(n^2).

        Space Complexity:
        -----------------
        O(1) — In-place swapping; no extra matrix is used.
        """
        n = len(mat)  # number of rows = number of columns (square matrix)

        # Outer loop runs O(n) times
        for i in range(n):
            # Inner loop runs O(n - i - 1) times on average, total O(n^2) across all iterations
            for j in range(i + 1, n):
                # Swap element at (i, j) with element at (j, i)
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat


# ==============================
# Main driver with input/output
# ==============================
def main():
    # Example input
    mat = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]
    ]

    print("Original Matrix:")
    for row in mat:
        print(row)

    # Create object of Solution class
    obj = Solution()

    # Call transpose
    transposed = obj.transpose(mat)

    print("\nTransposed Matrix:")
    for row in transposed:
        print(row)


# ==============================
# Timing the full program
# ==============================
# Using timeit to measure the runtime of main() function
execution_time = timeit.timeit(main, number=1)
print(f"\nTotal Execution Time: {execution_time:.6f} seconds")
```

---

### **Sample Run**

**Input:**

```
[
 [1, 1, 1, 1],
 [2, 2, 2, 2],
 [3, 3, 3, 3],
 [4, 4, 4, 4]
]
```

**Output:**

```
Original Matrix:
[1, 1, 1, 1]
[2, 2, 2, 2]
[3, 3, 3, 3]
[4, 4, 4, 4]

Transposed Matrix:
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]

Total Execution Time: 0.0000xx seconds
```

---

---

Here are a few **very important real-world use cases** of the **Transpose of Matrix** operation:

---

# 🌍 Real-World Use Cases

### **1. Linear Algebra & Scientific Computing**

* **Use:** Transpose is fundamental in solving systems of linear equations, eigenvalue problems, and matrix decompositions.
* **Example:** In **machine learning** and **physics simulations**, transposes are often used for matrix multiplication adjustments (e.g., computing $A^T \cdot A$ in least squares regression).

---

### **2. Graphics & Image Processing**

* **Use:** Transpose is part of many **image rotation** operations.
* **Example:** Rotating an image 90° clockwise can be done by **transpose + reversing rows** — this is a common optimization in image editors and OpenCV.

---

### **3. Machine Learning & Neural Networks**

* **Use:** Many deep learning frameworks need transposes to match **tensor shapes** for matrix multiplications in forward/backward propagation.
* **Example:** In **backpropagation**, the gradient with respect to weights often requires multiplying by the **transpose of the input matrix**.

---

### **4. Data Storage Optimization**

* **Use:** Transpose helps when switching between **row-major** and **column-major** data layouts for cache optimization.
* **Example:** In **HPC** (High-Performance Computing), transposing improves **memory access patterns** for parallel algorithms.

---

### **5. Network Analysis (Graph Theory)**

* **Use:** In adjacency matrix representation of a graph, the transpose can reverse all edges (used in algorithms like **Kosaraju's for Strongly Connected Components**).

---


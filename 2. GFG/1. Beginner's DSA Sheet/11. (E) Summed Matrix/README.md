
---

# 🧮 Summed Matrix

### Difficulty: Easy

**Accuracy**: 46.76%
**Submissions**: 53K+
**Points**: 2
**Average Time**: 15 mins

---

## 🧾 Problem Statement

A matrix is constructed of size `n × n` and given an integer `q`.
The value at every cell of the matrix is defined as:

```
M(i, j) = i + j
```

Where:

* `M(i, j)` is the value of the cell,
* `i` is the **row number**,
* `j` is the **column number**.

Return the number of cells having **value exactly equal to `q`**.

> 🔔 **Note**: The matrix uses **1-based indexing** (i.e., rows and columns start from 1).

---

## 📥 Input

* Two integers: `n` and `q`

  * `n` → size of the matrix (n × n)
  * `q` → target value to search in matrix

---

## 📤 Output

* Return an integer: total count of cells in the matrix where `M(i, j) = i + j = q`.

---

## 💡 Examples

### Example 1

```
Input:  n = 4,  q = 7

Matrix:
  2 3 4 5
  3 4 5 6
  4 5 6 7
  5 6 7 8

Output: 2
Explanation: Values equal to 7 are present at positions (3,4) and (4,3)
```

---

### Example 2

```
Input:  n = 5,  q = 4

Matrix:
  2 3 4 5 6
  3 4 5 6 7
  4 5 6 7 8
  5 6 7 8 9
  6 7 8 9 10

Output: 3
Explanation: Values equal to 4 are at positions (1,3), (2,2), (3,1)
```

---

## 🧠 Constraints

```
1 ≤ n, q ≤ 10^18
```

---

## ⏱️ Expected Complexities

| Metric          | Value |
| --------------- | ----- |
| Time Complexity | O(1)  |
| Auxiliary Space | O(1)  |

---

## 🏷️ Tags

* number-theory
* mathematical
* matrix
* data structures
* algorithms

---

---

Sure! Here's a complete breakdown of the **Summed Matrix** problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### Problem Summary:

Given a square matrix of size `n × n` where each element is defined as:

```
M(i, j) = i + j  (1-based index)
```

We need to count how many cells in the matrix have a value equal to a given number `q`.

---

### Key Observations:

* The **minimum value** in the matrix is at cell (1,1): `1 + 1 = 2`
* The **maximum value** is at cell (n,n): `n + n = 2n`
* Any value `q` must lie in the range `[2, 2n]` to be present in the matrix. If it doesn't, the answer is `0`.

---

### What values of (i, j) will satisfy `i + j = q`?

We want to count **how many pairs (i, j)** satisfy:

* `1 ≤ i ≤ n`
* `1 ≤ j ≤ n`
* `i + j = q`

That means:

* For a given `i`, `j = q - i` must also lie in `[1, n]`
* So, count valid `i` where `1 ≤ i ≤ n` and `1 ≤ q - i ≤ n`

This translates to:

```
max(1, q - n) ≤ i ≤ min(n, q - 1)
```

Hence, count of valid (i, j) pairs =

```
max(0, min(n, q - 1) - max(1, q - n) + 1)
```

---

### Dry Run Example

#### Input:

```
n = 4, q = 7
```

#### Matrix:

|   | 1 | 2 | 3 | 4 |
| - | - | - | - | - |
| 1 | 2 | 3 | 4 | 5 |
| 2 | 3 | 4 | 5 | 6 |
| 3 | 4 | 5 | 6 | 7 |
| 4 | 5 | 6 | 7 | 8 |

All values = i + j

We want cells where value = 7

Check positions:

* (3,4) → 3+4 = 7 ✅
* (4,3) → 4+3 = 7 ✅

So, output = 2

---

## ✅ 3. Optimized Python Code

### Optimal O(1) Time and O(1) Space Solution

```python
#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # Calculate the lower and upper bounds for valid i
        low = max(1, q - n)
        high = min(n, q - 1)
        
        # Total valid pairs is high - low + 1 (only if range is valid)
        count = max(0, high - low + 1)
        
        return count
```

---

## 🧪 Sample Input/Output

```python
n = 4
q = 7
# Output: 2 (positions: (3,4), (4,3))
```

---

## ✅ 4. Interview Questions & Answers

### Q1: Why is the matrix value defined as `M(i,j) = i + j`?

**A:** This simplifies cell values to a predictable pattern. It helps in reducing matrix traversal to a pure mathematical range problem.

---

### Q2: What are the constraints you must consider?

**A:** Since `n` can go up to 10^18, **we cannot construct the matrix**. We must compute the answer in O(1) time without loops or memory usage.

---

### Q3: How did you derive the formula for counting?

**A:** For `i + j = q` to be valid:

* `1 ≤ i ≤ n`
* `1 ≤ j = q - i ≤ n`
  So, the range of valid `i` is `i ∈ [max(1, q - n), min(n, q - 1)]`
  The count is `max(0, high - low + 1)`

---

### Q4: Why use `max(0, ...)`?

**A:** The bounds might not overlap (e.g., if `q < 2` or `q > 2n`), which results in a negative count. `max(0, ...)` ensures we return 0 in that case.

---

---

Here is the **full Python program** for the **"Summed Matrix"** problem using optimal O(1) solution — with:

* ✅ Inline comments explaining each step
* ✅ Time and space complexity annotations
* ✅ `timeit` module usage to time the full program run
* ✅ Input/output sample

---

### ✅ Full Python Program with Input, Output, Time Measurement

```python
import timeit

# Class to solve the Summed Matrix problem
class Solution:
    def sumMatrix(self, n, q):
        """
        Returns the number of cells (i,j) such that i + j = q,
        where 1 <= i,j <= n and matrix is based on M(i,j) = i + j.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Valid i range for which (q - i) is also within [1, n]
        low = max(1, q - n)
        high = min(n, q - 1)

        # Count of valid (i, j) pairs
        return max(0, high - low + 1)


# -------------------------------
# Main function to run the code
# -------------------------------
def main():
    # Sample Input
    n = 4
    q = 7

    # Print input values
    print(f"Input: n = {n}, q = {q}")

    # Create object and call function
    sol = Solution()
    result = sol.sumMatrix(n, q)

    # Output
    print(f"Output: {result}")  # Expected Output: 2

# -------------------------------
# Time the execution of the main
# -------------------------------
execution_time = timeit.timeit(main, number=1)
print(f"\n⏱️ Execution Time: {execution_time:.6f} seconds")
```

---

### ✅ Sample Output

```
Input: n = 4, q = 7
Output: 2

⏱️ Execution Time: 0.00000x seconds
```

---

### 🔍 Time & Space Complexity

* **Time Complexity:** `O(1)`
  Just a few arithmetic calculations — no loops or recursion.

* **Space Complexity:** `O(1)`
  Only constant space used — no data structures.

---

---

# 🌍 Real-World Use Cases

Here are a **few very important real-world use cases** of the **“Summed Matrix”** style problems — specifically where you are counting how many elements in a grid (constructed with a formula like `i + j`) satisfy a condition like summing to a target value `q`:

---

### ✅ 1. **Image Processing (Pixel Sums)**

* In digital images, pixel locations are often accessed using (row, column) pairs.
* You might want to find how many pixel positions add up to a particular intensity or diagonal index (since `i + j` = constant defines diagonals).
* Use Case: Fast algorithms for feature extraction or pattern alignment.

---

### ✅ 2. **Diagonal Traversals in Matrix-Based Algorithms**

* In algorithms like **dynamic programming**, **graph traversal**, or **matrix transformations**, diagonals (`i + j = constant`) have special significance.
* This logic is used in **wavefront scheduling**, **parallel algorithms**, and **anti-diagonal matrix operations**.

---

### ✅ 3. **Optimizing Sparse Matrix Access**

* In sparse matrices stored implicitly (e.g., as functions of row & column indices), identifying cells with certain values (like `i + j = q`) is common for optimization.
* Use Case: Saving memory or pre-fetching rows/columns in memory-constrained systems.

---

### ✅ 4. **Scheduling & Resource Allocation**

* In some scheduling models, task duration or cost is modeled as a function of time slot + resource index (`i + j`).
* Querying how many combinations result in a given cost can help in resource balancing.

---

### ✅ 5. **Mathematical Puzzle Games & Grid Simulations**

* Grid-based logic puzzle games (like Sudoku variants, or simulation tools) use constraints involving sums along rows, columns, or diagonals.
* Use Case: Game AI, automated puzzle generation.

---

# Kth Element in a Sorted Matrix

## 📘 Problem Statement

Given an `n x n` matrix `mat[][]` where each row and column is **sorted in non-decreasing order**, find the **kth smallest** element in the matrix.

---

## 📥 Input

* An integer `n` representing the matrix size.
* A matrix `mat[][]` of size `n x n` with each row and column sorted.
* An integer `k` where `1 <= k <= n * n`.

---

## 📤 Output

* Return the `k`th smallest element in the matrix.

---

## 💡 Examples

### Example 1

```
Input: 
n = 4 
mat = [[16, 28, 60, 64], 
       [22, 41, 63, 91], 
       [27, 50, 87, 93], 
       [36, 78, 87, 94]]
k = 3

Output: 
27

Explanation: 
27 is the 3rd smallest element.
```

### Example 2

```
Input: 
n = 4 
mat = [[10, 20, 30, 40], 
       [15, 25, 35, 45], 
       [24, 29, 37, 48], 
       [32, 33, 39, 50]]
k = 7

Output: 
30

Explanation: 
30 is the 7th smallest element.
```

---

## 🧠 Constraints

* `1 <= n <= 500`
* `1 <= mat[i][j] <= 10000`
* `1 <= k <= n * n`

---

## ⏱️ Expected Time & Space Complexity

* **Time Complexity**: `O(n * log(mat[i][j]))`
* **Auxiliary Space**: `O(1)`

---

## 🏢 Company Tags

* Accolite
* Amazon
* Samsung

---

## 🏷️ Topic Tags

* Matrix
* Heap
* Data Structures

---

## 📚 Related Articles

* [Kth Smallest Element in a Row-wise and Column-wise Sorted 2D Array](https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/)

---

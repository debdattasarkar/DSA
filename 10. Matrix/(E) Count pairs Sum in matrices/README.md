# 🧮 Count Pairs Sum in Matrices

**Difficulty**: Easy
**Accuracy**: 45.66%
**Submissions**: 52K+
**Points**: 2

---

## 📘 Problem Statement

Given two matrices `mat1[][]` and `mat2[][]` of size `n x n`, where:

* Each matrix is **strictly sorted in ascending order**:

  * Each row is sorted from **left to right**.
  * The last element of a row is **smaller** than the first element of the next row.

You're also given a target value `x`.
Your task is to **find and count** all pairs **{a, b}** such that:

* `a` is from `mat1`
* `b` is from `mat2`
* The sum `a + b == x`

---

## ✨ Examples

### Example 1:

**Input**:

```
n = 3, x = 21  
mat1 = [[1, 5, 6], [8, 10, 11], [15, 16, 18]]  
mat2 = [[2, 4, 7], [9, 10, 12], [13, 16, 20]]
```

**Output**: `4`

**Explanation**:
The pairs that sum to 21 are:

* (1, 20),
* (5, 16),
* (8, 13),
* (11, 10)

---

### Example 2:

**Input**:

```
n = 2, x = 10  
mat1 = [[1, 2], [3, 4]]  
mat2 = [[4, 5], [6, 7]]
```

**Output**: `2`

**Explanation**:
The pairs are (4, 6) and (3, 7)

---

## 🧠 Approach

* Flatten both matrices into 1D arrays.
* Use a **hash set** for efficient lookup of complementary values.
* For each element `a` in `mat1`, check if `x - a` exists in `mat2`.

---

## 🧩 Constraints

* `1 ≤ n ≤ 100`
* `1 ≤ x ≤ 10⁵`
* `1 ≤ mat1[i][j], mat2[i][j] ≤ 10⁵`

---

## 🕒 Expected Time and Space Complexity

* **Time Complexity**: O(n²)
* **Auxiliary Space**: O(1) *(if hashset not considered extra)*

---

## 🏷️ Tags

* Hash
* Sorting
* Matrix
* Algorithms
* Data Structures

---

## 🏢 Company Tags

* FactSet

---

## 📚 Related Articles

* [Count Pairs Two Sorted Matrices Given Sum](https://www.geeksforgeeks.org/count-pairs-two-sorted-matrices-given-sum/)

---

Let me know if you’d like a code implementation in Python, C++, or JavaScript for this problem!

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

Here’s a complete solution with **text explanation**, **step-by-step dry run**, and **code implementations** in **Python**, **C++**, and **JavaScript**, all with **inline comments**.

---

## ✅ Problem Summary

Given two matrices `mat1[][]` and `mat2[][]` of size `n x n`:

* Each row is sorted in ascending order.
* The last element of a row is smaller than the first element of the next row.

Find the number of **pairs {a, b}** such that:

* `a` belongs to `mat1`
* `b` belongs to `mat2`
* `a + b == x`

---

## 🔍 Step-by-Step Explanation

1. **Flatten** both matrices into one-dimensional lists.
2. **Insert all elements of `mat2` into a set** for O(1) lookup.
3. For every element `a` in `mat1`, check if `x - a` exists in the set.
4. Count such pairs.

---

## 🧪 Dry Run

**Input:**

```python
mat1 = [[1, 2], [3, 4]]
mat2 = [[4, 5], [6, 7]]
x = 10
```

**Flattened Lists:**

* `mat1`: \[1, 2, 3, 4]
* `mat2`: {4, 5, 6, 7}

**Check:**

* 10 - 1 = 9 ❌
* 10 - 2 = 8 ❌
* 10 - 3 = 7 ✅ ➝ (3, 7)
* 10 - 4 = 6 ✅ ➝ (4, 6)

**Result**: 2 pairs

---

## 🐍 Python Code

```python
class Solution:
    def countPairs(self, mat1, mat2, x):
        # Flatten mat2 into a set for O(1) lookups
        mat2_values = set()
        for row in mat2:
            mat2_values.update(row)

        count = 0
        # Check for each element in mat1 if x - element exists in mat2
        for row in mat1:
            for val in row:
                if (x - val) in mat2_values:
                    count += 1

        return count
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    int countPairs(vector<vector<int>> &mat1, vector<vector<int>> &mat2, int x) {
        unordered_set<int> mat2_set;
        // Insert all values from mat2 into a set
        for (auto &row : mat2) {
            for (int val : row) {
                mat2_set.insert(val);
            }
        }

        int count = 0;
        // For each value in mat1, check if x - val exists in mat2_set
        for (auto &row : mat1) {
            for (int val : row) {
                if (mat2_set.find(x - val) != mat2_set.end()) {
                    count++;
                }
            }
        }

        return count;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    countPairs(mat1, mat2, x) {
        // Flatten mat2 and put in a Set
        const mat2Set = new Set();
        for (const row of mat2) {
            for (const val of row) {
                mat2Set.add(val);
            }
        }

        let count = 0;
        // Check for each value in mat1 if x - val is in mat2Set
        for (const row of mat1) {
            for (const val of row) {
                if (mat2Set.has(x - val)) {
                    count++;
                }
            }
        }

        return count;
    }
}
```

---

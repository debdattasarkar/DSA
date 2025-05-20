# 📘 Kth Smallest Number in Multiplication Table

**Difficulty**: Hard
**Accuracy**: 44.33%
**Submissions**: 5K+
**Points**: 8

---

## 🧩 Problem Statement

Given three integers `m`, `n`, and `k`. Consider a grid of `m * n`, where:

```
mat[i][j] = i * j (1-based indexing)
```

The task is to return the **k<sup>th</sup> smallest element** in the `m * n` multiplication table.

---

## 🔍 Examples

### Example 1:

**Input**:
`m = 3`, `n = 3`, `k = 5`
**Output**: `3`
**Explanation**:

```
Multiplication Table:
1 2 3
2 4 6
3 6 9

Sorted elements: [1, 2, 2, 3, 3, 4, 6, 6, 9]
5th smallest = 3
```

---

### Example 2:

**Input**:
`m = 2`, `n = 3`, `k = 6`
**Output**: `6`
**Explanation**:

```
Multiplication Table:
1 2 3
2 4 6

Sorted elements: [1, 2, 2, 3, 4, 6]
6th smallest = 6
```

---

## ✅ Constraints

* 1 ≤ m, n ≤ 3 × 10⁴
* 1 ≤ k ≤ m × n

---

## 🧠 Approach

We can’t construct the entire matrix because of its potential size. Instead, we use **Binary Search** to find the kth smallest number.

### Binary Search Logic:

* Range is from `1` to `m*n`.
* For a mid value, count how many numbers are ≤ `mid` in the table.
* For a fixed row `i`, number of elements ≤ `mid` is `min(mid // i, n)`.

---

## 🧮 Expected Time and Space Complexity

* **Time Complexity**: O(m \* log(m × n))
* **Auxiliary Space**: O(1)

---

## 🏷️ Tags

* Binary Search
* Algorithms

---

## 🏢 Company Tags

* No specific company listed

---

## 📚 Related Articles

* [Kth Smallest Number In Multiplication Table](https://www.geeksforgeeks.org/kth-smallest-number-in-multiplication-table/)

---

Here’s the **step-by-step explanation**, dry run, and full **Python, C++, and JavaScript code** for the **“Kth Smallest Number in Multiplication Table”** problem from GeeksforGeeks.

---

## 🔍 Problem Summary

You're given `m`, `n`, and `k`, and need to return the **k<sup>th</sup> smallest element** in the `m x n` multiplication table `mat[i][j] = i * j`.

---

## 🧠 Explanation (with Binary Search)

Instead of building the full matrix, we use **Binary Search** over the value range.

### 💡 Binary Search Idea:

* The smallest number is `1`, and the largest is `m * n`.
* For a mid value, count how many numbers in the multiplication table are `<= mid`.
* If that count is `< k`, go right (increase mid); otherwise, go left.

### 📊 Counting Elements ≤ mid:

For each row `i` (1-indexed), the count is `min(mid // i, n)`.

---

## 🧪 Dry Run

### Input:

```
m = 3, n = 3, k = 5
```

Multiplication Table:

```
1 2 3
2 4 6
3 6 9
```

Sorted elements: `[1, 2, 2, 3, 3, 4, 6, 6, 9]`

### Step-by-step:

1. `left = 1`, `right = 9`
2. mid = 5
   Count of elements ≤ 5:

   * Row 1: min(5//1, 3) = 3
   * Row 2: min(5//2, 3) = 2
   * Row 3: min(5//3, 3) = 1
     Total = 6 ≥ k → move left: `right = 5`
3. mid = 3
   Count = 5 == k → move left: `right = 3`
4. mid = 2
   Count = 3 < k → move right: `left = 3`

At the end, `left = 3` → 5th smallest = **3**

---

## 🐍 Python Code

```python
class Solution(object):
    def kthSmallest(self, m, n, k):
        def countLessEqual(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int kthSmallest(int m, int n, int k) {
        auto countLessEqual = [&](int x) {
            int count = 0;
            for (int i = 1; i <= m; ++i)
                count += min(x / i, n);
            return count;
        };
        
        int left = 1, right = m * n;
        while (left < right) {
            int mid = (left + right) / 2;
            if (countLessEqual(mid) < k)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    /**
     * @param {number} m
     * @param {number} n
     * @param {number} k
     * @returns {number}
     */
    kthSmallest(m, n, k) {
        const countLessEqual = (x) => {
            let count = 0;
            for (let i = 1; i <= m; i++) {
                count += Math.min(Math.floor(x / i), n);
            }
            return count;
        };

        let left = 1, right = m * n;
        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (countLessEqual(mid) < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

---

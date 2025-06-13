# 📊 Subarrays Product Less Than K

## 📝 Problem Statement

Given an array of positive integers, the task is to find the number of **contiguous subarrays** whose product of elements is **strictly less than** a given number `k`.

---

## 🧠 Explanation

We aim to count all possible subarrays such that the product of elements in each subarray is less than `k`.

### 💡 Key Insight:

Use the **sliding window** technique to efficiently calculate the number of valid subarrays in **O(n)** time.

### 🧮 Formula:

For each valid window `(start to end)`, we add `(end - start + 1)` valid subarrays ending at index `end`.

---

## 🔍 Example Walkthrough

### Example 1:

**Input:**

```
n = 4, k = 10
a[] = [1, 2, 3, 4]
```

**Output:**

```
7
```

**Explanation:**

Valid subarrays:
`[1], [2], [3], [4], [1, 2], [2, 3], [3, 4]`

Invalid:
`[2, 3, 4]` → 2×3×4 = 24 ≥ 10

---

### Example 2:

**Input:**

```
n = 7, k = 100
a[] = [1, 9, 2, 8, 6, 4, 3]
```

**Output:**

```
16
```

---

## 🔐 Constraints

* 1 ≤ n ≤ 10⁶
* 1 ≤ k ≤ 10¹⁵
* 1 ≤ a\[i] ≤ 10⁵

---

## ⚙️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🚀 Algorithm (Step-by-Step)

1. Initialize `start = 0`, `prod = 1`, `count = 0`.
2. Iterate `end` from 0 to `n-1`:

   * Multiply `prod` by `a[end]`.
   * While `prod >= k` and `start <= end`, divide `prod` by `a[start]` and increment `start`.
   * Add `(end - start + 1)` to `count`.
3. Return `count`.

---

## 🧪 Dry Run

**For a\[] = \[1, 2, 3, 4], k = 10:**

| end | a\[end] | prod | start | count added |
| --- | ------- | ---- | ----- | ----------- |
| 0   | 1       | 1    | 0     | 1           |
| 1   | 2       | 2    | 0     | 2           |
| 2   | 3       | 6    | 0     | 3           |
| 3   | 4       | 24   | 1     | 1           |

**Total:** 7

---

## 💻 Code Implementations

### Python

```python
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        if k <= 1:
            return 0
        
        prod = 1
        result = 0
        start = 0

        for end in range(n):
            prod *= a[end]
            while prod >= k:
                prod //= a[start]
                start += 1
            result += end - start + 1
        
        return result
```

---

### C++

```cpp
class Solution {
public:
    int countSubArrayProductLessThanK(vector<int>& a, int n, int k) {
        if (k <= 1) return 0;

        int prod = 1, result = 0, start = 0;

        for (int end = 0; end < n; end++) {
            prod *= a[end];
            while (prod >= k && start <= end)
                prod /= a[start++];
            result += end - start + 1;
        }

        return result;
    }
};
```

---

### JavaScript

```javascript
class Solution {
    countSubArrayProductLessThanK(a, n, k) {
        if (k <= 1) return 0;

        let prod = 1, result = 0, start = 0;

        for (let end = 0; end < n; end++) {
            prod *= a[end];
            while (prod >= k && start <= end) {
                prod /= a[start++];
            }
            result += end - start + 1;
        }

        return result;
    }
}
```

---

## 🏢 Company Tags

* Goldman Sachs
* Facebook
* Amazon
* Microsoft
* Uber
* Walmart
* Yatra.com
* LinkedIn

---

## 🏷️ Topic Tags

* Arrays
* Data Structures
* Algorithms
* Sliding Window

---

## 📚 Related Articles

* [Number Subarrays Product Less K](https://www.geeksforgeeks.org/number-subarrays-product-less-k/)

---

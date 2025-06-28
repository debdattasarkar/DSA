
---

# 📊 Counting Elements in Two Arrays

**Difficulty:** Medium
**Accuracy:** 37.12%
**Points:** 4
**Average Time:** 20m
**Submissions:** 88K+

---

## 🧩 Problem Statement

You are given two unsorted arrays `a[]` and `b[]`. Both arrays may contain duplicate elements.

For **each element** in array `a[]`, your task is to count how many elements in `b[]` are **less than or equal to that element**.

---

## ✨ Examples

### Example 1:

```
Input:
a[] = [4, 8, 7, 5, 1]
b[] = [4, 48, 3, 0, 1, 1, 5]

Output: [5, 6, 6, 6, 3]

Explanation: 
For a[0] = 4 → elements in b ≤ 4 are [4, 3, 0, 1, 1] → count = 5  
For a[1] = 8 → elements in b ≤ 8 are [4, 3, 0, 1, 1, 5] → count = 6  
For a[2] = 7 → same as above → count = 6  
For a[3] = 5 → elements in b ≤ 5 are [4, 3, 0, 1, 1, 5] → count = 6  
For a[4] = 1 → elements in b ≤ 1 are [0, 1, 1] → count = 3  
```

### Example 2:

```
Input:
a[] = [10, 20]
b[] = [30, 40, 50]

Output: [0, 0]

Explanation:
There are no elements in b[] less than or equal to 10 or 20.
```

---

## 📚 Constraints

* 1 ≤ `a.size()`, `b.size()` ≤ 10⁵
* 0 ≤ `a[i]`, `b[i]` ≤ 10⁵

---

## 📈 Expected Complexities

* **Time Complexity:** O(n + m + max(b\[i]))
* **Auxiliary Space:** O(max(b\[i]))

---

## 🏢 Company Tags

* Amazon

---

## 🏷️ Topic Tags

* Arrays
* Searching
* Binary Search
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Element 1st Array Count Elements Less Equal 2nd Array](#)

---

Sure! Here's the detailed breakdown:

---

## ✅ 1. Text Explanation + Step-by-Step Dry Run

### **Problem Summary:**

You're given two unsorted arrays `a[]` and `b[]`. For every element in `a[]`, count how many elements in `b[]` are **less than or equal to** that value.

---

### ✅ **Optimized Approach (O(m log m + n log m)) using Binary Search:**

1. **Sort array `b`** to allow binary search.
2. For each element `x` in `a`, use `bisect_right` (in Python) or `upper_bound` (in C++) to find how many elements in `b` are ≤ `x`.

---

### 🔍 Dry Run Example:

```python
a = [4, 8, 7, 5, 1]
b = [4, 48, 3, 0, 1, 1, 5]
```

Step 1: Sort `b` → `[0, 1, 1, 3, 4, 5, 48]`

Step 2: For each element in `a`:

* `4` → upper\_bound = 5 → `[0, 1, 1, 3, 4]` → 5 elements
* `8` → upper\_bound = 6 → `[0, 1, 1, 3, 4, 5]` → 6 elements
* `7` → upper\_bound = 6 → same
* `5` → upper\_bound = 6 → same
* `1` → upper\_bound = 3 → `[0, 1, 1]` → 3 elements

✅ Output: `[5, 6, 6, 6, 3]`

---

## 🧠 2. Code in Python, C++, and JavaScript

---

### 🔹 Python (Using `bisect`)

```python
from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        # code here
        b.sort()  # Sort b once
        na = len(a)
        nb = len(b)
        freq = [0] * na
        i = 0
        for val in a:
            # bisect_right returns the number of elements ≤ val
            freq[i] = bisect_right(b, val)
            i += 1
            
        return freq
```

```python
from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        b.sort()  # Sort b for binary search
        res = []
        for num in a:
            # Find index of first element greater than num (count of <= num)
            count = bisect_right(b, num)
            res.append(count)
        return res
```

---

### 🔹 C++ (Using `upper_bound`)

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
  public:
    vector<int> countLessEq(vector<int>& a, vector<int>& b) {
        sort(b.begin(), b.end());  // Sort b for binary search
        vector<int> res;
        for (int x : a) {
            // upper_bound returns iterator to the first element > x
            int count = upper_bound(b.begin(), b.end(), x) - b.begin();
            res.push_back(count);
        }
        return res;
    }
};
```

---

### 🔹 JavaScript (Custom Binary Search)

```javascript
class Solution {
    countLessEq(a, b) {
        b.sort((x, y) => x - y);  // Sort b
        const res = [];

        const upperBound = (arr, target) => {
            let low = 0, high = arr.length;
            while (low < high) {
                let mid = Math.floor((low + high) / 2);
                if (arr[mid] <= target) low = mid + 1;
                else high = mid;
            }
            return low;
        };

        for (let x of a) {
            res.push(upperBound(b, x));
        }
        return res;
    }
}
```

---

## ❓ 3. Interview Questions & Answers

### 🔸 Q1. Why do we sort array `b`?

**A:** Sorting `b` allows us to use binary search (`O(log m)`) for each `a[i]`, reducing total time from O(n \* m) to O(n log m).

---

### 🔸 Q2. Why use `upper_bound` / `bisect_right`?

**A:** It returns the index of the first element greater than `x`, which equals the number of elements ≤ `x`.

---

### 🔸 Q3. Can we solve this in O(n + m + maxVal)?

**A:** Yes, using **counting sort** technique with frequency and prefix sum. It's optimal when range of values is small.

---

### 🔸 Q4. What if `b[]` is very large, say size > 1e7?

**A:** Sorting will still take `O(m log m)`. To handle extreme values, we can use prefix count arrays.

---

Here's the **O(n + m + maxVal)** version using **counting sort and prefix sum**, which is optimal when the range of elements is small (like ≤ 10⁵):

---

## ✅ Optimized Version Using Prefix Sum (O(n + m + maxVal))

### 🧠 **Idea**:

1. Count frequency of each element in array `b`.
2. Build a **prefix sum array** that tells how many elements in `b` are ≤ `i`.
3. For each element in `a`, simply look up the prefix sum to get the answer.

---

### 🔍 Dry Run:

```python
a = [4, 8, 7, 5, 1]
b = [4, 48, 3, 0, 1, 1, 5]
```

1. Count frequency of `b`:

```python
freq = [0] * (max_val + 1)
# freq[0] = 1, freq[1] = 2, freq[3] = 1, freq[4] = 1, freq[5] = 1, freq[48] = 1
```

2. Compute prefix sum:

```python
prefix[i] = prefix[i-1] + freq[i]
# prefix[4] = number of elements in b <= 4 = 1+2+0+1 = 4
```

3. For `a[i] = 4` → answer is `prefix[4] = 5`, for `a[i] = 1` → `prefix[1] = 3`

✅ Output: `[5, 6, 6, 6, 3]`

---

## 🐍 Python Code

```python
class Solution:
    def countLessEq(self, a, b):
        max_val = 10**5  # Constraint from problem
        freq = [0] * (max_val + 2)

        # Count frequencies in b
        for num in b:
            freq[num] += 1

        # Prefix sum: prefix[i] = how many numbers <= i in b
        for i in range(1, max_val + 2):
            freq[i] += freq[i - 1]

        # Build result using prefix
        return [freq[num] for num in a]
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    vector<int> countLessEq(vector<int>& a, vector<int>& b) {
        const int MAX = 1e5 + 2;
        vector<int> freq(MAX, 0);

        for (int x : b)
            freq[x]++;

        for (int i = 1; i < MAX; ++i)
            freq[i] += freq[i - 1];

        vector<int> res;
        for (int x : a)
            res.push_back(freq[x]);
        return res;
    }
};
```

---

## 🔷 JavaScript Code

```javascript
class Solution {
    countLessEq(a, b) {
        const MAX = 100002;
        const freq = new Array(MAX).fill(0);

        for (let x of b) freq[x]++;

        for (let i = 1; i < MAX; i++) {
            freq[i] += freq[i - 1];
        }

        return a.map(x => freq[x]);
    }
}
```

---

## ✅ Time and Space

* **Time:** `O(n + m + maxVal)`
* **Space:** `O(maxVal)`

---

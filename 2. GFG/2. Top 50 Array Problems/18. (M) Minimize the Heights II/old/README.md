
---

# Minimize the Heights II

**Difficulty**: Medium
**Accuracy**: 15.06%
**Submissions**: 714K+
**Points**: 4
**Average Time**: 25m

---

## 🧩 Problem Statement

Given an array `arr[]` denoting heights of `N` towers and a positive integer `K`.
For each tower, you must perform **exactly one** of the following operations **exactly once**:

* **Increase** the height of the tower by `K`
* **Decrease** the height of the tower by `K`

Find out the **minimum** possible difference between the height of the shortest and tallest towers after you have modified each tower.

📌 **Note:**

* A slight modification of the problem can be found [here](https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1).
* It is **compulsory** to increase or decrease the height by `K` for each tower.
* **After** the operation, the resultant array **should not contain any negative integers**.

---

## 💡 Examples

### Example 1:

```
Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation:
The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.
The difference between the largest and the smallest is 8 - 3 = 5.
```

### Example 2:

```
Input: k = 3, arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation:
The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.
The difference between the largest and the smallest is 17 - 6 = 11.
```

---

## 🧱 Constraints

* 1 ≤ k ≤ 10⁷
* 1 ≤ n ≤ 10⁵
* 1 ≤ arr\[i] ≤ 10⁷

---

## ⏱ Expected Complexities

* **Time Complexity**: O(n log n)
* **Auxiliary Space**: O(1)

---

## 🏢 Company Tags

`Microsoft` `Adobe`

---

## 🏷 Topic Tags

`Arrays` `Greedy` `Data Structures` `Algorithms`

---

## 📚 Related Articles

* [Minimize The Maximum Difference Between The Heights](https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/)

---

## 🔍 Problem Understanding

Given an array `arr[]` of size `n` representing the height of towers and an integer `k`, we are allowed to either add or subtract `k` from every element **exactly once**, such that the **maximum difference** between the tallest and shortest towers is minimized.

### Constraints:

* All modified heights must be **non-negative**.
* You **must** apply the operation to every element.

---

## 🧠 Key Idea

1. Sort the array.
2. The **initial difference** is `arr[n-1] - arr[0]`.
3. After modifying elements:

   * Add `k` to the **smaller elements**
   * Subtract `k` from the **larger elements**
4. For each split point `i` (from `0` to `n-2`), calculate:

   * `min_height = min(arr[0] + k, arr[i+1] - k)`
   * `max_height = max(arr[i] + k, arr[n-1] - k)`
   * Update the minimum difference `min_diff = min(min_diff, max_height - min_height)`

---

## 🧪 Dry Run

**Input**: `arr = [1, 5, 8, 10], k = 2`

1. Sort: `[1, 5, 8, 10]`
2. Initial diff: `10 - 1 = 9`

**Try splits:**

* i = 0 → min = min(1+2, 5−2) = 3, max = max(1+2, 10−2) = 8 → diff = 5 ✅
* i = 1 → min = min(1+2, 8−2) = 3, max = max(5+2, 10−2) = 8 → diff = 5
* i = 2 → min = min(1+2, 10−2) = 3, max = max(8+2, 10−2) = 10 → diff = 7

**Answer**: `5`

---

## ✅ Python Implementation

```python
#User function Template for python3

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        diff = arr[-1] - arr[0]

        for i in range(n - 1):
            min_elem = min(arr[0] + k, arr[i + 1] - k)
            max_elem = max(arr[i] + k, arr[-1] - k)
            if min_elem < 0:
                continue
            diff = min(diff, max_elem - min_elem)
        
        return diff
```

---

## ✅ C++ Implementation

```cpp
// User function template for C++

class Solution {
  public:
    int getMinDiff(vector<int>& arr, int k) {
        int n = arr.size();
        if (n == 1) return 0;
        
        sort(arr.begin(), arr.end());
        int diff = arr[n-1] - arr[0];

        for (int i = 0; i < n - 1; ++i) {
            int min_elem = min(arr[0] + k, arr[i+1] - k);
            int max_elem = max(arr[i] + k, arr[n-1] - k);
            if (min_elem < 0) continue;
            diff = min(diff, max_elem - min_elem);
        }
        
        return diff;
    }
};
```

---

## ✅ JavaScript Implementation

```javascript
// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */

class Solution {
    getMinDiff(arr, k) {
        const n = arr.length;
        if (n === 1) return 0;

        arr.sort((a, b) => a - b);
        let diff = arr[n - 1] - arr[0];

        for (let i = 0; i < n - 1; i++) {
            let min_elem = Math.min(arr[0] + k, arr[i + 1] - k);
            let max_elem = Math.max(arr[i] + k, arr[n - 1] - k);
            if (min_elem < 0) continue;
            diff = Math.min(diff, max_elem - min_elem);
        }

        return diff;
    }
}
```

---

## 🧠 Interview-Focused Points

* **Why is sorting required?**

  * It allows us to easily reason about which values to increment or decrement.
* **What if negative heights are generated?**

  * Skip those combinations (check `min_elem < 0`).
* **Time Complexity**: `O(n log n)` due to sorting.
* **Space Complexity**: `O(1)`.


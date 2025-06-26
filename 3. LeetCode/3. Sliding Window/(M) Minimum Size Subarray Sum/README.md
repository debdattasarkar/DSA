
---

# 209. Minimum Size Subarray Sum

**Difficulty:** Medium
**Tags:** Array, Binary Search, Sliding Window, Prefix Sum
**Companies:** 🔶

---

## 🧾 Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a **subarray** whose sum is **greater than or equal to** `target`. If there is no such subarray, return `0` instead.

---

## 🧪 Examples

### Example 1:

**Input:**
`target = 7`, `nums = [2,3,1,2,4,3]`
**Output:**
`2`
**Explanation:**
The subarray `[4,3]` has the minimal length under the problem constraint.

---

### Example 2:

**Input:**
`target = 4`, `nums = [1,4,4]`
**Output:**
`1`

---

### Example 3:

**Input:**
`target = 11`, `nums = [1,1,1,1,1,1,1,1]`
**Output:**
`0`
**Explanation:**
There is no subarray with sum ≥ 11.

---

## 📋 Constraints

* `1 <= target <= 10⁹`
* `1 <= nums.length <= 10⁵`
* `1 <= nums[i] <= 10⁴`

---

## 💡 Follow-up

If you have figured out the **O(n)** solution (using sliding window), try coding another solution of which the time complexity is **O(n log n)** (using binary search and prefix sums).

---

## 🏷️ Topics

* Array
* Binary Search
* Sliding Window
* Prefix Sum

---

Here's the **Prefix Sum + Binary Search** solution to **Leetcode 209: Minimum Size Subarray Sum**, with:

1. ✅ Step-by-step explanation
2. 🧪 Dry run
3. 🧠 Code for Python, C++, and JavaScript

---

## ✅ Prefix Sum + Binary Search Logic

### 🔍 Intuition:

1. Build a **prefix sum array**, where `prefix[i]` is the sum of the first `i` elements.
2. For every index `i`, use **binary search** to find the smallest `j > i` such that `prefix[j] - prefix[i] ≥ target`.
3. Track the minimum `j - i` that satisfies this.

### 🔁 Time Complexity:

* Prefix sum: `O(n)`
* Binary search for each index: `O(log n)`
* Total: **`O(n log n)`**

---

## 🧪 Dry Run

**Input:**
`target = 7`
`nums = [2,3,1,2,4,3]`

### Step 1: Compute Prefix Sum

| Index | Prefix Sum |
| ----- | ---------- |
| 0     | 0          |
| 1     | 2          |
| 2     | 5          |
| 3     | 6          |
| 4     | 8          |
| 5     | 12         |
| 6     | 15         |

(`prefix[i]` = sum of first `i` numbers)

### Step 2: For each `i`, binary search for smallest `j` such that:

`prefix[j] - prefix[i] >= 7`

Example:

* `i = 0` → find smallest `j` with `prefix[j] >= 7` → j = 4 (prefix\[4]=8) → length = 4
* `i = 3` → prefix\[5]-prefix\[3]=12-6=6 < 7 → continue
* `i = 4` → prefix\[5]-prefix\[4]=12-8=4 < 7 → continue
* `i = 2` → prefix\[5]-5=12-5=7 → j = 5 → length = 3

**Minimum length = 2** (subarray `[4,3]`)

---

## 🧠 Python Code

```python
import bisect
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        # Build prefix sum
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        min_len = float('inf')

        # Binary search for each prefix[i]
        for i in range(n):
            required = target + prefix[i]
            bound = bisect.bisect_left(prefix, required)
            if bound <= n:
                min_len = min(min_len, bound - i)

        return 0 if min_len == float('inf') else min_len
```

---

## 🧠 C++ Code

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);

        // Build prefix sum
        for (int i = 0; i < n; ++i)
            prefix[i + 1] = prefix[i] + nums[i];

        int minLen = INT_MAX;

        // Binary search for each prefix[i]
        for (int i = 0; i < n; ++i) {
            int required = target + prefix[i];
            auto bound = lower_bound(prefix.begin(), prefix.end(), required);
            if (bound != prefix.end())
                minLen = min(minLen, (int)(bound - prefix.begin()) - i);
        }

        return minLen == INT_MAX ? 0 : minLen;
    }
};
```

---

## 🧠 JavaScript Code

```javascript
/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    const n = nums.length;
    const prefix = Array(n + 1).fill(0);

    for (let i = 0; i < n; i++)
        prefix[i + 1] = prefix[i] + nums[i];

    let minLen = Infinity;

    for (let i = 0; i < n; i++) {
        let required = target + prefix[i];

        // Binary search
        let left = i + 1, right = n;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (prefix[mid] >= required) {
                minLen = Math.min(minLen, mid - i);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }

    return minLen === Infinity ? 0 : minLen;
};
```

---

## 🧠 Expected Interview Questions & Answers

### Q1. Why does this approach work?

It leverages cumulative sums to avoid repeated summation and binary search to efficiently find bounds.

---

### Q2. Why is prefix sum better than brute-force?

Brute-force recomputes sums for each subarray (O(n²)), while prefix sum lets you compute any subarray sum in O(1) time.

---

### Q3. When is binary search better than sliding window?

If the array can include **zeros**, **negatives**, or you're doing repeated queries on prefix sums (e.g., follow-up with multiple queries), binary search offers flexibility.

---

Here's a **full comparison** between the two primary methods for solving **Leetcode 209 – Minimum Size Subarray Sum**:

---

## 🧩 Problem Recap:

> Given an array of **positive integers** `nums` and a **positive integer** `target`, return the **minimum length** of a **contiguous subarray** of which the sum is **greater than or equal to target**. If there is no such subarray, return 0.

---

## ✅ Method 1: **Sliding Window** (Two Pointers)

### 🔧 How it works:

* Use two pointers (`left`, `right`) to create a **sliding window**.
* Expand the window by moving `right` to include more elements until the sum is ≥ `target`.
* Once valid, move `left` to reduce the size while maintaining the condition.

### 📈 Time Complexity:

* **O(n)**: Each pointer moves at most `n` times.

### 📦 Space Complexity:

* **O(1)**: Only variables for window bounds and sum are used.

### ✅ Pros:

* Very efficient and elegant.
* Handles the problem in a single linear pass.

### ❌ Cons:

* Only works when all elements are **positive**.
* Not easily adaptable if the array includes **negative numbers**.

---

## 🧠 Method 2: **Prefix Sum + Binary Search**

### 🔧 How it works:

* Compute a prefix sum array `prefix[i] = sum(nums[0]..nums[i-1])`.
* For each starting index `i`, use **binary search** to find the smallest `j` such that:

  ```python
  prefix[j] - prefix[i] >= target
  ```

### 📈 Time Complexity:

* Prefix sum construction: **O(n)**
* Binary search for each prefix index: **O(log n)**
* Total: **O(n log n)**

### 📦 Space Complexity:

* **O(n)**: To store the prefix sum array.

### ✅ Pros:

* Works even if array has **negative numbers**.
* Can be adapted to solve the **follow-up problem** (multiple queries).

### ❌ Cons:

* Slightly more complex than sliding window.
* Needs binary search logic or `bisect` module.

---

## 🧪 Example: `target = 7`, `nums = [2,3,1,2,4,3]`

### 🔁 Sliding Window Steps:

1. `[2]` → sum = 2
2. `[2,3]` → sum = 5
3. `[2,3,1]` → sum = 6
4. `[2,3,1,2]` → sum = 8 → valid → shrink
5. `[3,1,2]` → sum = 6
6. `[1,2,4]` → sum = 7 → valid → min length = 3
7. `[4,3]` → sum = 7 → valid → min length = 2 ✅

### 🔁 Prefix Sum + Binary Search:

* `prefix = [0,2,5,6,8,12,15]`
* For `i = 0`, find smallest `j` where `prefix[j] ≥ 7 + prefix[0] = 7` → `j = 4`
* `j - i = 4`
* Try for every `i`, best result is `j=6, i=4` → length = 2 ✅

---

## 📊 Summary Comparison

| Feature                          | Sliding Window | Prefix Sum + Binary Search |
| -------------------------------- | -------------- | -------------------------- |
| Time Complexity                  | O(n)           | O(n log n)                 |
| Space Complexity                 | O(1)           | O(n)                       |
| Handles Negative Numbers         | ❌ No           | ✅ Yes                      |
| Suitable for Repeated Queries    | ❌ No           | ✅ Yes                      |
| Implementation Simplicity        | ✅ Easy         | ❌ Moderate                 |
| Optimal for Positive-only Arrays | ✅ Yes          | ✅ Yes                      |
| Adaptable to Follow-ups          | ❌ No           | ✅ Yes                      |

---

## 📝 When to Use Which?

| Situation                            | Recommended Method         |
| ------------------------------------ | -------------------------- |
| Single query, positive integers      | Sliding Window             |
| Multiple queries on the same array   | Prefix Sum + Binary Search |
| Array might include negative numbers | Prefix Sum + Binary Search |
| Time-optimized for large datasets    | Sliding Window             |

---

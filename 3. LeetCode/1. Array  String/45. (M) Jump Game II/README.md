
---

# 🏃‍♂️ Jump Game II (Leetcode #45)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Greedy`, `Dynamic Programming`

---

## 📘 Problem Statement

You are given a **0-indexed** array `nums` where each element `nums[i]` represents the **maximum jump length** from that index.

Return the **minimum number of jumps** required to reach the **last index**.

You can **always reach** the last index.

---

## 🧪 Examples

### Example 1

```
Input:  nums = [2,3,1,1,4]
Output: 2
Explanation: 
- Jump from index 0 → 1 (3 steps possible)
- Then jump from index 1 → 4
```

### Example 2

```
Input:  nums = [2,3,0,1,4]
Output: 2
Explanation: Same logic — reach last index in 2 jumps.
```

---

## ⚙️ Constraints

* `1 <= nums.length <= 10⁴`
* `0 <= nums[i] <= 1000`
* It is **guaranteed** you can reach `nums[n-1]`.

---

## 💡 Greedy Approach (Optimal)

Track three values:

* `jumps`: number of jumps taken so far
* `end`: the **end of current jump's range**
* `farthest`: the farthest index we can reach in the current scan

At each index `i`:

* Update `farthest = max(farthest, i + nums[i])`
* If `i == end`, we need to jump: `jumps += 1`, and set `end = farthest`

---

## 🧪 Dry Run

**Input:** `[2,3,1,1,4]`

| i | nums\[i] | farthest | end | jumps                                |
| - | -------- | -------- | --- | ------------------------------------ |
| 0 | 2        | 2        | 0   | 0      → end reached → jump=1, end=2 |
| 1 | 3        | 4        | 2   | 1                                    |
| 2 | 1        | 4        | 2   | 1 → end reached → jump=2, end=4 ✅    |
| 3 | -        | -        | -   | -                                    |
| 4 | -        | -        | -   | 2      ✅ Done                        |

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # Time to jump to the next range
            if i == end:
                jumps += 1
                end = farthest

        return jumps
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0, end = 0, farthest = 0;

        for (int i = 0; i < nums.size() - 1; ++i) {
            farthest = max(farthest, i + nums[i]);

            if (i == end) {
                ++jumps;
                end = farthest;
            }
        }

        return jumps;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let jumps = 0, end = 0, farthest = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        farthest = Math.max(farthest, i + nums[i]);

        if (i === end) {
            jumps++;
            end = farthest;
        }
    }

    return jumps;
};
```

---

## ✅ Summary

| Metric           | Value                                          |
| ---------------- | ---------------------------------------------- |
| Time Complexity  | `O(n)`                                         |
| Space Complexity | `O(1)`                                         |
| Strategy         | Greedy (track farthest & jump at end of range) |
| Edge Cases       | Handled due to guaranteed reachability         |

---

Certainly! Here's a **DP (Dynamic Programming)** solution for **Leetcode 45 – Jump Game II**. While the **greedy solution** is optimal (`O(n)`), the **DP version** is useful for building intuition and transitioning to more complex jump problems.

---

# 📊 DP Table – Jump Game II

---

## 🧠 Idea

Let `dp[i]` be the **minimum number of jumps required to reach index `i`**.

* Initialize `dp[0] = 0` (starting point needs 0 jumps)
* For every index `i`, loop through all previous positions `j` and:

  * If `j + nums[j] >= i`, update `dp[i] = min(dp[i], dp[j] + 1)`

---

## ⏱️ Time Complexity

* Time: `O(n^2)`
* Space: `O(n)`

---

## 🧪 Dry Run

**Input:** `[2, 3, 1, 1, 4]`
**Goal:** Fill `dp[]` array.

| i | Reachable from | dp\[i] updated from        |
| - | -------------- | -------------------------- |
| 1 | 0              | dp\[1] = dp\[0] + 1 = 1    |
| 2 | 0, 1           | dp\[2] = min(∞, 1+1) = 1   |
| 3 | 1, 2           | dp\[3] = min(∞, 1+1) = 2   |
| 4 | 1, 2, 3        | dp\[4] = min(∞, 2+1) = 2 ✅ |

Result: `dp[n-1] = 2`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0  # Start point

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:  # Can reach i from j
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, INT_MAX);
        dp[0] = 0;

        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (j + nums[j] >= i) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }

        return dp[n - 1];
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    const n = nums.length;
    const dp = new Array(n).fill(Infinity);
    dp[0] = 0;

    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (j + nums[j] >= i) {
                dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        }
    }

    return dp[n - 1];
};
```

---

## ✅ Summary

| Metric              | Value          |
| ------------------- | -------------- |
| Time Complexity     | `O(n^2)`       |
| Space Complexity    | `O(n)`         |
| Good for Learning   | ✅ Yes          |
| Optimal in Practice | ❌ (use Greedy) |

---

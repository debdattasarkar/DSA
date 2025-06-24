
---

# 🏃‍♂️ Jump Game (Leetcode #55)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Greedy`, `Dynamic Programming`

---

## 📘 Problem Statement

You are given an array `nums` where `nums[i]` represents the **maximum jump length** from that index.

You start at index `0` and must determine:
🔹 **Can you reach the last index?**

---

## 🧪 Examples

### Example 1

```
Input:  nums = [2,3,1,1,4]
Output: true
Explanation: 
- Jump 1 step from index 0 → index 1
- Jump 3 steps from index 1 → index 4 ✅
```

### Example 2

```
Input:  nums = [3,2,1,0,4]
Output: false
Explanation:
- You get stuck at index 3 (0 steps) ❌
```

---

## ⚙️ Constraints

* `1 <= nums.length <= 10⁴`
* `0 <= nums[i] <= 10⁵`

---

## ✅ Greedy Approach (Optimal)

### Intuition:

Track the **farthest index** you can reach while moving forward.

### Logic:

* At each index `i`, update `farthest = max(farthest, i + nums[i])`
* If `i > farthest`, you’re stuck — return `False`
* If `farthest >= last index`, return `True`

---

## 🧪 Dry Run

**Input:** `[2,3,1,1,4]`

| i | nums\[i] | i + nums\[i] | farthest |
| - | -------- | ------------ | -------- |
| 0 | 2        | 0 + 2 = 2    | 2        |
| 1 | 3        | 1 + 3 = 4    | **4** ✅  |
| 2 | 1        | 2 + 1 = 3    | 4        |
| 3 | 1        | 3 + 1 = 4    | 4        |
| 4 | 4        | 4 + 4 = 8    | 8        |

`farthest (≥ 4)` ⇒ ✅ Reachable

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # Stuck before reaching i
            farthest = max(farthest, i + nums[i])  # Extend range
        return True
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int farthest = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > farthest) return false;
            farthest = max(farthest, i + nums[i]);
        }
        return true;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let farthest = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > farthest) return false;
        farthest = Math.max(farthest, i + nums[i]);
    }
    return true;
};
```

---

## ✅ Summary

| Metric           | Value                                   |
| ---------------- | --------------------------------------- |
| Time Complexity  | `O(n)`                                  |
| Space Complexity | `O(1)`                                  |
| Strategy         | Greedy (track farthest reachable index) |
| Edge Case        | `nums[i] == 0` and you’re stuck         |

---

Great! Let’s explore the **Dynamic Programming (DP) version** of **Leetcode 55 – Jump Game**. While it’s **not as optimal as the greedy approach**, it’s a useful way to understand the problem from a bottom-up reachability standpoint.

---

# 📊 DP Table – Jump Game

---

## 🧠 Intuition

We track whether each index is **reachable** using a DP table (or array of booleans).
We start from index 0 (which is always reachable) and use `nums[i]` to mark future reachable positions.

---

## 🧮 State Definition

Let:

* `dp[i] = True` if index `i` is reachable
* Initially: `dp[0] = True` (you start at index 0)

### Transition:

* For every `i`, if `dp[i] == True`, then mark all positions `i+1` to `i + nums[i]` as `True`

---

## 🧪 Dry Run

**Input:** `[2,3,1,1,4]`

| i | nums\[i] | dp\[i] | Update                 | dp after            |
| - | -------- | ------ | ---------------------- | ------------------- |
| 0 | 2        | ✅      | dp\[1], dp\[2]         | `[T, T, T, F, F]`   |
| 1 | 3        | ✅      | dp\[2], dp\[3], dp\[4] | `[T, T, T, T, T]` ✅ |
| 2 | 1        | ✅      | dp\[3] (already T)     | no change           |

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True  # Start point is reachable

        for i in range(n):
            if not dp[i]:
                continue  # Skip unreachable index
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = True

        return dp[-1]  # Can we reach the last index?
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<bool> dp(n, false);
        dp[0] = true;

        for (int i = 0; i < n; ++i) {
            if (!dp[i]) continue;
            for (int j = 1; j <= nums[i] && i + j < n; ++j) {
                dp[i + j] = true;
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
 * @return {boolean}
 */
var canJump = function(nums) {
    const n = nums.length;
    const dp = new Array(n).fill(false);
    dp[0] = true;

    for (let i = 0; i < n; i++) {
        if (!dp[i]) continue;
        for (let j = 1; j <= nums[i]; j++) {
            if (i + j < n) dp[i + j] = true;
        }
    }

    return dp[n - 1];
};
```

---

## 📌 Summary

| Technique        | Value                                                               |
| ---------------- | ------------------------------------------------------------------- |
| Time Complexity  | `O(n²)` (in worst case)                                             |
| Space Complexity | `O(n)`                                                              |
| In-place?        | ❌ (extra DP array)                                                  |
| Usefulness       | Great for building toward more advanced variations (e.g. min jumps) |

---

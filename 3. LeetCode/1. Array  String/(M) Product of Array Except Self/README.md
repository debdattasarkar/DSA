Here’s a full README-style explanation and solution for **Leetcode 238 – Product of Array Except Self**, including a dry run and full implementations in **Python**, **C++**, and **JavaScript**.

---

# ✨ Product of Array Except Self (Leetcode #238)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Prefix Product`, `Space Optimization`

---

## 📘 Problem Statement

Given an integer array `nums`, return an array `answer` such that:

* `answer[i] = product of all elements in nums except nums[i]`

### Constraints:

* **Do NOT use division**
* Must run in **O(n)** time
* Use only **O(1)** extra space (excluding `answer` array)

---

## 🔍 Key Insight

We compute the product of all elements **except self** using two passes:

* **Left pass**: product of elements to the **left** of `i`
* **Right pass**: product of elements to the **right** of `i`

---

## 🧪 Dry Run

**Input:** `nums = [1, 2, 3, 4]`

### Step 1: Left product pass

```text
Initialize answer = [1, 1, 1, 1]
Fill:
answer[1] = 1 * nums[0] = 1
answer[2] = 1 * nums[1] = 2
answer[3] = 2 * nums[2] = 6
→ answer = [1, 1, 2, 6]
```

### Step 2: Right product pass (with running product `R`)

```text
R = 1
i = 3 → answer[3] *= R = 6*1 = 6; R *= nums[3] = 4
i = 2 → answer[2] *= R = 2*4 = 8; R *= nums[2] = 12
i = 1 → answer[1] *= R = 1*12 = 12; R *= nums[1] = 24
i = 0 → answer[0] *= R = 1*24 = 24
→ Final = [24, 12, 8, 6]
```

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Left products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Right products and combine
        R = 1
        for i in reversed(range(n)):
            answer[i] *= R
            R *= nums[i]

        return answer
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);

        for (int i = 1; i < n; ++i)
            answer[i] = answer[i - 1] * nums[i - 1];

        int R = 1;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] *= R;
            R *= nums[i];
        }

        return answer;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    const answer = new Array(n).fill(1);

    // Left product
    for (let i = 1; i < n; i++) {
        answer[i] = answer[i - 1] * nums[i - 1];
    }

    // Right product and combine
    let R = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= R;
        R *= nums[i];
    }

    return answer;
};
```

---

## ✅ Summary

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(1) extra |
| Uses division?   | ❌ No       |

This is the **optimal solution** for the problem constraints.

---

You're right to be curious — even though your solution is **optimal in complexity** (`O(n)` time, `O(1)` space), your **runtime is only better than \~36%** of submissions. Let’s analyze what might be happening and how to improve:

---

## 🔍 Possible Reasons for Suboptimal Runtime

### 1. **Platform Runtime Variability**

* LeetCode runtime can vary based on server load, submission time, or language internals.
* A 30ms result is **not bad**, even if percentile seems low.

---

### 2. **Code Implementation Nuances**

Although your logic is optimal, **micro-optimizations** can still improve speed.

### Python Example Optimizations:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
```

🔸 Improvements:

* Avoids extra indexing (e.g., `range(1, n)` → `range(n)` with manual update)
* Uses fewer array writes

---

### 3. **Language Choice**

* C++ usually has better runtime percentiles than Python due to compilation and lower-level control.
* For the same logic, Python often shows lower percentiles but it **does not mean the code is inefficient**.

---

### 4. **Avoid Built-in Functions in Tight Loops**

If you're using operations like `reversed(range(...))` or `list.insert`, they can be slightly slower. Manual loops are sometimes faster in high-performance situations.

---

## ✅ Summary

| Factor               | Suggestion                      |
| -------------------- | ------------------------------- |
| Platform Variability | Ignore if under 50ms            |
| Algorithm Complexity | ✅ Already optimal (`O(n)`)      |
| Python Overhead      | Consider trying in C++          |
| Micro-optimization   | Refactor loop/indexing patterns |

---

### Do You Need to Worry?

💡 **No**, unless you're competing in runtime contests. Your solution is:

* Fast ✅
* Space-optimal ✅
* Correct ✅

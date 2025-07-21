
---

## 🧩 Leetcode 410: Split Array Largest Sum

🔗 [Leetcode Link](https://leetcode.com/problems/split-array-largest-sum)

### 🧠 Problem Statement:

Given an array `nums` of non-negative integers and an integer `k`, split the array into `k` or fewer **non-empty subarrays**, so that the **maximum sum among these subarrays is minimized**.

Return that **minimum possible largest sum**.

---

### 📌 Example:

```python
Input: nums = [7,2,5,10,8], k = 2  
Output: 18

Explanation:
Split into [7,2,5] and [10,8] → max sum = 14, 18 → min of those = 18
```

---

## 🚀 Strategy: Binary Search on Answer

We are minimizing the **largest subarray sum** — so we apply **binary search on the answer space**:

* Lower bound: `max(nums)` → smallest possible largest sum (one number per split)
* Upper bound: `sum(nums)` → worst case: 1 partition

---

### ✅ Core Idea

Try a value `mid` as the **maximum allowed subarray sum**:

* Traverse the array.
* Greedily form subarrays without exceeding `mid`.
* Count how many subarrays we form.

→ If count > `k` → `mid` is **too small**, increase `left`
→ Else → it’s **feasible**, try to minimize it → `right = mid - 1`

---

## ✅ Python Code

```python
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(max_sum_allowed):
            subarrays = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > max_sum_allowed:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return subarrays <= k

        left, right = max(nums), sum(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
```

---

## 🧮 Time & Space Complexity

| Metric | Complexity              |
| ------ | ----------------------- |
| Time   | `O(n × log(sum - max))` |
| Space  | `O(1)`                  |

---

## 🔁 Dry Run for `nums = [7,2,5,10,8], k = 2`

* left = 10, right = 32
* Try mid = 21 → can split into \[7,2,5,10] and \[8] → valid
* Try mid = 15 → need 3 splits → invalid
* Narrow search to find min possible largest sum = **18**

---

## 💬 Common Interview Questions

1. **Why binary search on the answer?**
   Because the feasibility function (can split within `k`) is **monotonic**.

2. **Why greedy subarray formation works?**
   Because we are checking **feasibility** for a fixed limit — greedily starting a new subarray only when needed ensures minimum subarrays.

3. **Can you get the actual subarrays?**
   Yes — but you'd need to backtrack or construct them during the feasibility check.

4. **What if elements are negative?**
   The problem assumes non-negative integers. If negatives are allowed, greedy feasibility breaks — different strategy needed.

---

---

# 🌍 Real-World Use Cases

Here are a few **very important real-world use cases** of the **Split Array Largest Sum** problem pattern:

---

### ✅ 1. **File or Data Sharding (e.g., Cloud Storage, Hadoop)**

* Split a large file or dataset into **`k` chunks** so that the **largest chunk is minimized** for load balancing across servers.

---

### ✅ 2. **Workload Balancing in Distributed Systems**

* Assign tasks (with varying durations) to **`k` machines** such that **maximum processing time per machine is minimized**.

---

### ✅ 3. **Video/Game Level Loading**

* Divide content into **evenly balanced segments** to minimize max memory or CPU usage per loading stage.

---


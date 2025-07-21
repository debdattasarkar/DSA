
---

## 🧩 Problem Summary:

🔗 [Leetcode 1802](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/)

Given:

* An array of length `n`
* You must maximize `nums[index]` (value at a specific index)
* All elements of the array must be:

  * **positive integers**
  * total **sum ≤ maxSum**
  * adjacent difference **≤ 1** (i.e., array forms a "hill")

---

### ✨ Goal:

Find the **maximum value** you can put at `nums[index]` such that:

* Total sum of array ≤ `maxSum`
* Difference between adjacent elements ≤ 1
* All elements are ≥ 1

---

## ✅ Approach: Binary Search on Answer

We **binary search on possible values** of `nums[index]`.

### 🎯 Why Binary Search?

The higher you set `nums[index]`, the more array sum it costs.
✅ This relationship is **monotonic**, so binary search works.

---

## 🔧 Key Insight: Total Cost for a Given Peak

For a peak value `x` at position `index`, we compute:

* Cost to build **left slope** from `index-1` to `0`
* Cost to build **right slope** from `index+1` to `n-1`

We define:

```python
def total(x):
    sum = x
    sum += sum_of_slope(x-1, index)         # left
    sum += sum_of_slope(x-1, n - index - 1) # right
    return sum
```

Where `sum_of_slope(val, len)` builds a decreasing slope of length `len` starting from `val`.

---

### ✅ Python Code

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc_sum(x: int, cnt: int) -> int:
            # Calculates the total sum needed for cnt elements starting from x going down
            if x >= cnt:
                # Complete decreasing slope down to 1 (no flat tail)
                return (x + x - cnt + 1) * cnt // 2
            else:
                # Incomplete slope; tail is filled with 1s
                return (x + 1) * x // 2 + (cnt - x)

        def is_valid(x: int) -> bool:
            # Checks if a peak of x at index can be built within maxSum
            left_sum = calc_sum(x - 1, index)
            right_sum = calc_sum(x - 1, n - index - 1)
            total = left_sum + right_sum + x
            return total <= maxSum

        # Binary search to maximize nums[index]
        left, right = 1, maxSum
        result = 1

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
```

---

## 🧪 Example

```python
Input: n = 6, index = 1, maxSum = 10
Output: 3
Explanation:
nums = [2,3,2,1,1,1] has peak 3 at index 1, and total sum = 10
```

---

## ⏱️ Time & Space Complexity

| Complexity | Value            |
| ---------- | ---------------- |
| Time       | `O(log(maxSum))` |
| Space      | `O(1)`           |

---

## 💬 Interview Q\&A

**Q: Why binary search on `nums[index]`?**
A: Because increasing the peak always increases the cost — monotonic relation ⇒ binary search works.

**Q: What does `calc_sum` do?**
A: Computes the total needed for one side (left/right) of the mountain based on decreasing sequence rules.

**Q: What if adjacent differences > 1 were allowed?**
A: Then greedy or DP would be needed — this specific hill constraint enables binary search.

---

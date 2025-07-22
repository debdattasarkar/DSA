
# **Leetcode 643: Max Average Subarray I** using the **Fixed Sliding Window** technique 

---

## 🔍 Problem Summary

> Given an array of integers `nums` and an integer `k`, find the **maximum average** of any contiguous subarray of length `k`.

---

### 🧪 Example:

```python
Input: nums = [1,12,-5,-6,50,3], k = 4  
Output: 12.75  
Explanation: Subarray [12, -5, -6, 50] has the maximum average = (12 - 5 - 6 + 50)/4 = 51/4 = 12.75
```

---

## ✅ Approach: Fixed Sliding Window

This is a **fixed-size window** problem because the subarray must be **exactly of size `k`**.

---

## 🧑‍💻 Python Code with Inline Comments

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Sum the first window of size k
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Slide the window through the array
        for i in range(k, len(nums)):
            # Remove the element leaving the window and add the new element
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Step 3: Compute average
        return max_sum / k
```

---

## ⏱ Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧠 Dry Run Example

```python
nums = [1,12,-5,-6,50,3], k = 4

Initial window: 1 + 12 + (-5) + (-6) = 2
→ max_sum = 2

Next window:
12 + (-5) + (-6) + 50 → (2 - 1 + 50) = 51 → max_sum = 51

Next window:
-5 + (-6) + 50 + 3 → (51 - 12 + 3) = 42 → max_sum = 51

Answer: 51 / 4 = 12.75
```

✅ Output: `12.75`

---

## ❓ Interview Questions You May Face

| Question                                        | Answer                                    |
| ----------------------------------------------- | ----------------------------------------- |
| Why is this not brute force?                    | We reuse previous window’s sum in O(1)    |
| Can this be extended to variable-length window? | No — window size is strictly `k`          |
| What if k = n?                                  | Just take the average of the entire array |
| What if negatives are allowed?                  | Still valid — no restriction on values    |

---

## 📚 Related Problems (All Fixed-Window)

* **[LC 1456](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)** – Max number of vowels in substring of length k
* **[LC 1839](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/)** – Special substrings, fixed window validation
* **GFG** – First negative number in every window of size k

---

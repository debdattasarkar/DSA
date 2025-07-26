**Leetcode 1004 – Max Consecutive Ones III** is one of the most popular problems to **master the Variable Sliding Window technique with at most `k` violations**.

---

## 🔍 Problem Statement

> Given a binary array `nums` and an integer `k`, return the **maximum number of consecutive 1s** in the array if you can flip at most `k` 0s.

---

### 🧪 Example:

```python
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: Flip the two 0s at positions 3 and 4 to get [1,1,1,1,1,1], length = 6
```

---

## ✅ Approach: Variable Sliding Window with Count of Zeros

### 💡 Strategy:

* Maintain a window (`left` to `right`) such that **number of 0s in the window ≤ k**
* If the number of 0s exceeds `k`, **shrink the window from the left**
* Track the **maximum window length** that satisfies the condition

---

## 🧑‍💻 Python Code (Efficient & Interview-Ready)

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            # Expand window by including nums[right]
            if nums[right] == 0:
                zeros += 1

            # Shrink window until zero count ≤ k
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

## ⏱ Time & Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧠 Dry Run Example

### Input:

```python
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
```

| Step | Left | Right | Zeros | Window                | MaxLen  |
| ---- | ---- | ----- | ----- | --------------------- | ------- |
| 0-2  | 0    | 2     | 0     | \[1,1,1]              | 3       |
| 3    | 0    | 3     | 1     | \[1,1,1,0]            | 4       |
| 4    | 0    | 4     | 2     | \[1,1,1,0,0]          | 5       |
| 5    | 0→1  | 5     | 3→2   | \[1,1,0,0,0] → shrink | 5       |
| 6-9  | 2    | 6→9   | ≤ 2   | \[0,0,1,1,1,1]        | **6** ✅ |
| 10   | 3    | 10    | 3     | Exceeds → shrink      |         |

✅ Final `max_len = 6`

---

## ❓ Interview Q\&A

| Question                                         | Answer                                    |
| ------------------------------------------------ | ----------------------------------------- |
| Why do we shrink the window only if zeros > k?   | To ensure we never flip more than allowed |
| Can this solve similar problems with 1s instead? | Yes — invert the logic                    |
| What if k = 0?                                   | It becomes a pure max-1s subarray         |
| Can this be done with prefix sum?                | Not as clean as sliding window            |

---


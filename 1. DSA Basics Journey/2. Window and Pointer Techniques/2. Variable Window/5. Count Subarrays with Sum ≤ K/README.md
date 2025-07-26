Let's dive into the classic problem from **GFG**:

---

# ✅ **Count Subarrays with Sum ≤ K**

> Given an array `arr[]` of integers and an integer `k`, **count the number of contiguous subarrays** such that the sum of elements in the subarray is **less than or equal to `k`**.

---

## 🧠 Concept

This is a **Variable Sliding Window** problem, especially useful when:

* Array contains only **non-negative integers**
* You're working with **subarray sums** and need to maintain constraints

---

## 📌 Key Observations

* Only works with **non-negative** numbers — because sliding window assumes adding more elements will **not decrease** sum.
* If at any point sum > k, we **shrink the window** from the left.

---

## 🧑‍💻 Python Code (Sliding Window)

```python
def countSubarrays(arr, k):
    n = len(arr)
    left = 0
    current_sum = 0
    count = 0

    for right in range(n):
        current_sum += arr[right]

        # Shrink window until valid
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        # All subarrays ending at `right` and starting from `left` to `right` are valid
        count += (right - left + 1)

    return count
```

---

## ⏱ Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧪 Dry Run

### Input:

```python
arr = [1, 2, 1, 0, 1], k = 4
```

| Step | Left | Right | Current Sum | Valid Subarrays                    | Total Count |
| ---- | ---- | ----- | ----------- | ---------------------------------- | ----------- |
| 0    | 0    | 0     | 1           | \[1]                               | 1           |
| 1    | 0    | 1     | 3           | \[1,2], \[2]                       | 3           |
| 2    | 0    | 2     | 4           | \[1,2,1], \[2,1], \[1]             | 6           |
| 3    | 0    | 3     | 4           | \[1,2,1,0], \[2,1,0], \[1,0], \[0] | 10          |
| 4    | 0    | 4     | 5 → shrink  | \[2,1,0,1], \[1,0,1], \[0,1], \[1] | 14          |

✅ Final `count = 14`

---

## ❓ Interview Questions & Clarifications

| Question                                         | Answer                                                      |
| ------------------------------------------------ | ----------------------------------------------------------- |
| Why does it only work for non-negative integers? | Because with negatives, shrinking may **increase** sum      |
| What if array has negative numbers?              | Use prefix sum + two pointers (offline), not sliding window |
| Why count += (right - left + 1)?                 | That’s how many valid subarrays end at `right`              |
| What if exact `sum == k` is needed?              | The same logic works as long as condition is `≤ k`          |

---

## 📦 Real-World Applications

* Find **# of valid transaction windows** under a credit limit
* Detect how many **time spans** had CPU usage ≤ threshold
* Count **valid energy usage windows** for optimization

---

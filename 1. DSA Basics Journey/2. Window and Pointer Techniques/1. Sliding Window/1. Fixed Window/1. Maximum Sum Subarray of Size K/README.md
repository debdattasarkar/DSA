
---

## 🔍 Problem Statement

**Leetcode Variant:**
(Also on [GFG](https://www.geeksforgeeks.org/window-sliding-technique/))

> Given an array of integers `arr[]` and an integer `k`, find the **maximum sum of any contiguous subarray** of size `k`.

---

### 🧪 Example:

```python
Input: arr = [2, 1, 5, 1, 3, 2], k = 3  
Output: 9  
Explanation: Subarray [5, 1, 3] has the maximum sum = 9
```

---

## ✅ Optimal Solution Using Sliding Window

### 📌 Core Idea:

Instead of summing each subarray of size `k` repeatedly (O(n·k)), we:

* Keep a **running sum** of the current `k` elements
* Slide the window forward by **removing the first element and adding the next**

---

### 🧑‍💻 Python Code with Comments

```python
def max_sum_subarray_k(arr, k):
    n = len(arr)

    if n < k:
        return -1  # Not enough elements

    # Step 1: Calculate sum of first 'k' elements
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2: Slide the window
    for i in range(k, n):
        # Subtract element going out, add element coming in
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

---

### ⏱ Time & Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧠 Dry Run

```python
arr = [2, 1, 5, 1, 3, 2], k = 3

Initial sum: 2 + 1 + 5 = 8
i = 3 → window = [1, 5, 1] → sum = 7 → max = 8
i = 4 → window = [5, 1, 3] → sum = 9 → max = 9 ✅
i = 5 → window = [1, 3, 2] → sum = 6
```

**Result: 9**

---

## 🔄 Brute Force (for comparison)

```python
def brute_force(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr) - k + 1):
        curr_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

**Time:** O(n·k)

---

## ❓ Follow-Up Interview Questions

| Question                                       | Expected Answer                    |
| ---------------------------------------------- | ---------------------------------- |
| Can we solve it in less than O(n·k)?           | Yes, O(n) using sliding window     |
| What if array contains negatives?              | Still works, no issue              |
| Can this be extended to variable window size?  | Yes — variable-size sliding window |
| Can this solve max average of subarray size k? | Yes — just divide result by `k`    |

---

## 🔗 Similar Problems

* [Leetcode 643 – Max Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
* [GFG – First Negative Integer in Every Window of Size K](https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/)
* [Leetcode 1456 – Max Number of Vowels in Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

---

---

**The solution to “Maximum Sum Subarray of Size K” is a classic example of the *Fixed Sliding Window* technique.**

---

## 🔍 Why is it a **Fixed Window**?

Because:

* The size of the window is **exactly `k`**, and
* It **doesn’t change** throughout the traversal.

### 🔁 What happens in the loop?

* You keep a sum of `k` elements.
* Every iteration, you **slide the window by one**:

  * Remove the first element (i−k)
  * Add the new element (i)

This maintains a **fixed-size window** as you move forward.

---

## 🧠 Comparison

| Feature         | Fixed Window               | Variable Window                      |
| --------------- | -------------------------- | ------------------------------------ |
| Window Size     | Constant (e.g. `k = 3`)    | Expands or shrinks based on logic    |
| Use Case        | Max sum, averages, counts  | Conditions like ≤ target, no repeats |
| Example Problem | Max sum subarray of size k | Longest substring without repeating  |

---

If you’re ready, I can show you a **variable-size version** of a similar problem next — or build a comparison of fixed vs variable window templates.

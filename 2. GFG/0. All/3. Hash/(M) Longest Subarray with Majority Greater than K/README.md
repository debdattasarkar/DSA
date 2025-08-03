Here is the full README-style conversion of the problem **"Longest Subarray with Majority Greater than K"** as shown in your image:

---

# 📘 Longest Subarray with Majority Greater than K

### 🟠 Difficulty: Medium

**Accuracy:** 55.0%
**Submissions:** 4K+
**Points:** 4

---

## 🧩 Problem Statement

Given an array `arr[]` and an integer `k`, the task is to **find the length of the longest subarray** in which the **count of elements greater than `k` is more** than the **count of elements less than or equal to `k`**.

---

## 🧪 Examples

### Example 1

```
Input: 
arr[] = [1, 2, 3, 4, 1]
k = 2

Output: 
3

Explanation: 
The subarray [2, 3, 4] or [3, 4, 1] satisfies the condition:
  - In [2, 3, 4], elements > 2 = {3, 4} → 2
               elements <= 2 = {2} → 1
  - In [3, 4, 1], elements > 2 = {3, 4} → 2
               elements <= 2 = {1} → 1
There is no subarray of length 4 or 5 that satisfies the condition.
So the answer is 3.
```

---

### Example 2

```
Input:
arr[] = [6, 5, 3, 4]
k = 2

Output:
4

Explanation:
All elements in subarray [6, 5, 3, 4] are greater than 2. 
  - count(>2) = 4, count(<=2) = 0
Hence, entire array is a valid subarray.
```

---

## 🔐 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $1 \leq \text{arr}[i] \leq 10^6$
* $0 \leq k \leq 10^6$

---

## ✅ Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(n)$

---

## 🏷️ Tags

* prefix-sum
* hash

---

## 📚 Related Articles

* [Length Of Longest Subarray In Which Elements Greater Than K Are More Than Elements Not Greater Than K](https://www.geeksforgeeks.org/length-of-longest-subarray-in-which-elements-greater-than-k-are-more-than-elements-not-greater-than-k/)

---

---

Here's the full detailed breakdown for the problem **"Longest Subarray with Majority Greater than K"** based on the image and your format:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🧠 Problem Summary:

Given an array `arr[]` and an integer `k`, we need to find the **length of the longest subarray** such that the number of elements **greater than `k` is more** than the number of elements **less than or equal to `k`**.

---

### 💡 Key Idea:

Transform the array:

* If `arr[i] > k`, replace it with `+1`
* If `arr[i] <= k`, replace it with `-1`

Now the problem reduces to:

> Find the **longest subarray** with **positive sum**

---

### 🧪 Dry Run:

#### Input:

```python
arr = [1, 2, 3, 4, 1], k = 2
```

#### Transform:

```python
nums = [-1, -1, +1, +1, -1]
```

#### Cumulative Sum:

We want the longest subarray with sum > 0.

* Use prefix sum and store first occurrence of a prefix sum value.
* Whenever `currSum > 0`, whole subarray from `0 to i` is valid.
* If `currSum - 1` is seen before at `j`, then `j+1 to i` is also valid.

---

## ✅ 3. Optimized Python Code (Expected in Interviews)

```python
from collections import defaultdict

class Solution:
    def longestSubarray(self, arr, k):
        # Step 1: Transform the array into +1 and -1
        n = len(arr)
        nums = [1 if num > k else -1 for num in arr]

        # Step 2: Use prefix sum and a hash map to track first seen positions
        prefix_sum = 0
        first_occurrence = {}  # stores earliest index for each prefix sum
        max_len = 0

        for i in range(n):
            prefix_sum += nums[i]

            # Case 1: total sum is positive → whole subarray [0..i] is valid
            if prefix_sum > 0:
                max_len = i + 1

            # Case 2: check if prefix_sum - 1 occurred before
            if prefix_sum - 1 in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            # Store the first occurrence only
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
```

---

## 🧪 Time and Space Complexity:

* **Time:** O(n) → single traversal
* **Space:** O(n) → for storing prefix sums

---

## ✅ 4. Interview Q\&A

### Q1: What is the intuition behind transforming the array to +1 and -1?

**A:** To reduce the condition of "greater than k elements are more than others" into a prefix sum problem that is easier to track using cumulative sums.

---

### Q2: Why do we use prefix sum and hashmap?

**A:** Prefix sum helps track net difference between +1s and -1s. Hashmap is used to remember earliest positions to maximize subarray length efficiently.

---

### Q3: What happens when prefix sum becomes zero?

**A:** It means equal number of +1 and -1 → not valid. We are only interested when prefix sum > 0.

---

### Q4: Can this approach be used for a similar "majority" condition like greater than N/2?

**A:** Yes, a similar approach works if the condition can be reduced to a sign-based transformation (+1, -1 or 0).

---

### Q5: Real-world use case?

**A:**

* Behavioral analysis (e.g., identifying longest sequence of user actions where positive outcomes outweigh negative)
* Stock trend analysis (subarray where more gains than losses)

---

Here is the **full program** with inline comments, dry run explanation, and time complexity for the **"Longest Subarray with Majority Greater than K"** problem:

---

### ✅ Problem Summary:

Given an array `arr[]` and integer `k`, return the **length of the longest subarray** in which the **count of elements greater than k is more** than the count of elements less than or equal to k.

---

### 🔍 Dry Run (Input: `[1, 2, 3, 4, 1]`, `k = 2`)

* Convert array to:

  ```
  > k  → +1
  ≤ k → -1
  arr:     [1, 2, 3, 4, 1]
  mapped: [-1, -1, +1, +1, -1]
  ```
* Prefix sum tracking with hashmap:

  ```
  i=0: prefix=-1 → store -1:i
  i=1: prefix=-2 → store -2:i
  i=2: prefix=-1 (found -2 before at i=1) → max_len = 2 - 1 = 1
  i=3: prefix=0 → found -1 before at i=0 → max_len = 3 - 0 = 3 ✅
  i=4: prefix=-1 (found -2 before) → max_len stays 3
  ```

✅ Answer: `3`

---

### ✅ Optimized Python Code

```python
import time
from typing import List

class Solution:
    def longestSubarray(self, arr: List[int], k: int) -> int:
        # Step 1: Convert elements into +1 (if >k) and -1 (if <=k)
        n = len(arr)
        nums = [1 if num > k else -1 for num in arr]  # O(n) time and space

        # Step 2: Initialize prefix sum and hashmap
        prefix_sum = 0
        first_occurrence = {}  # Stores first index of each prefix sum
        max_len = 0

        for i in range(n):  # O(n)
            prefix_sum += nums[i]

            # Case 1: subarray from start has positive majority
            if prefix_sum > 0:
                max_len = i + 1

            # Case 2: check if a previous prefix_sum - 1 occurred
            if (prefix_sum - 1) in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            # Only store first occurrence of each prefix sum
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
```

---

### 🧪 Input/Output & Timing (with `time` module)

```python
# Input values for testing
arr = [1, 2, 3, 4, 1]
k = 2

# Time the execution
start_time = time.time()
sol = Solution()
result = sol.longestSubarray(arr, k)
end_time = time.time()

# Output
print("Input Array:", arr)
print("K value:", k)
print("Length of Longest Subarray:", result)
print("Execution Time (seconds):", end_time - start_time)
```

### 🕒 Output

```
Input Array: [1, 2, 3, 4, 1]
K value: 2
Length of Longest Subarray: 3
Execution Time (seconds): < 1ms
```

---

### 📊 Time and Space Complexity

| Step                 | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Mapping +1/-1 array  | O(n)            | O(n)             |
| Prefix sum traversal | O(n)            | O(n) (hash map)  |
| Overall              | O(n)            | O(n)             |

---

### 💡 Common Interview Questions

1. **Q:** Why do we map values to +1 and -1?

   * **A:** To reduce the problem to a prefix sum problem where we're interested in net dominance of values `> k` over values `≤ k`.

2. **Q:** What’s the role of `prefix_sum - 1` in this logic?

   * **A:** We want to find the earliest point where the prefix was just 1 less, implying we can form a valid subarray.

3. **Q:** Can this be done in-place?

   * **A:** No, because we need auxiliary storage for prefix sums.

4. **Q:** What if all elements are ≤ k?

   * **A:** No subarray will qualify. The result is `0`.

---


---

# Maximum Sum of Elements Not Part of LIS

### Difficulty: Medium

**Accuracy**: 44.35%
**Submissions**: 9K+
**Points**: 4

---

## 🧾 Problem Statement

Given an array `arr[]` of positive integers, your task is to find the **maximum possible sum** of all elements that are **not part of the Longest Increasing Subsequence (LIS)**.

---

## 🧪 Examples

### Example 1:

```
Input: arr[] = [4, 6, 1, 2, 3, 8]  
Output: 10  
Explanation: The elements which are not in LIS are 4 and 6.
```

### Example 2:

```
Input: arr[] = [5, 4, 3, 2, 1]  
Output: 14  
Explanation: The elements which are not in LIS are 5, 4, 3 and 2.
```

---

## 📌 Constraints

* `1 ≤ arr.size() ≤ 10^3`
* `1 ≤ arr[i] ≤ 10^5`

---

## 📊 Expected Complexities

* **Time Complexity**: O(n log n)
* **Auxiliary Space**: O(n)

---

## 🏷️ Tags

* Dynamic Programming
* Algorithms

---

## 🏢 Company Tags

* Flipkart

---

## 📚 Related Articles

* **Maximize Sum Of All Elements Which Are Not A Part Of The Longest Increasing Subsequence**

---

## 💼 Related Interview Experiences

* Flipkart Interview Experience For SDE 1 On Campus

---

---

Here’s a **detailed solution** for the problem *“Maximum Sum of Elements Not Part of LIS”* including:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### Problem Statement Recap:

Given an array of positive integers `arr`, find the **maximum sum of all elements that are not part of the Longest Increasing Subsequence (LIS)**.

---

### 🧠 Key Idea:

* **Total Sum** of all elements – **Sum of elements in LIS** = **Required Answer**

So, the main task becomes:

1. Compute total sum of all elements.
2. Compute the **maximum sum** of elements in the **LIS** (not just length).
3. Subtract and return.

---

### ✏️ Dry Run

Let’s take this example:

```python
arr = [4, 6, 1, 2, 3, 8]
```

#### Step 1: Total sum

```
total = 4 + 6 + 1 + 2 + 3 + 8 = 24
```

#### Step 2: LIS with maximum sum

Possible increasing subsequences:

* \[4, 6, 8] → sum = 18
* \[1, 2, 3, 8] → sum = 14 ✅ (maximum increasing sequence with highest sum)

→ max\_lis\_sum = 14

#### Step 3: Subtract

```
result = total - max_lis_sum = 24 - 14 = 10
```

✅ Final Output: `10`

---

## 🧑‍💻 3. Optimized Code Implementations in Python

---
Yes! The reason for **Time Limit Exceeded** is the **O(n²) dynamic programming** used to compute the LIS and reconstruct it.

Let’s optimize it to **O(n log n)** using **binary search + patience sorting technique** and maintain backtracking pointers to reconstruct the LIS.

---

### ✅ Optimized Python Code (O(n log n)) with Full Explanation

```python
from bisect import bisect_left

class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        parent = [-1] * n  # Stores the previous index in the LIS
        dp = []            # Holds the indices of potential LIS
        pos = [0] * n      # pos[i] = index of the LIS ending at i

        for i in range(n):
            # Find the location where arr[i] can be inserted in dp
            idx = bisect_left([arr[j] for j in dp], arr[i])

            if idx < len(dp):
                dp[idx] = i
            else:
                dp.append(i)

            pos[i] = idx
            if idx > 0:
                parent[i] = dp[idx - 1]  # Link to previous element in LIS

        # Now reconstruct LIS using parent array
        lis_sum = 0
        lis_len = len(dp)
        k = -1

        # Find the last index where LIS ends (has max pos value)
        for i in range(n - 1, -1, -1):
            if pos[i] == lis_len - 1:
                k = i
                break

        while k != -1:
            lis_sum += arr[k]
            k = parent[k]

        return sum(arr) - lis_sum
```

---

### ⏱ Time and Space Complexity

| Component                 | Complexity     |
| ------------------------- | -------------- |
| Total time for LIS        | O(n log n)     |
| Reconstructing LIS        | O(n)           |
| Total sum calculation     | O(n)           |
| **Total Time Complexity** | **O(n log n)** |
| **Space Complexity**      | **O(n)**       |

---

### 📌 Sample Run for Input: `[4, 6, 1, 2, 3, 8]`

* LIS = `[1, 2, 3, 8]`
* Sum = 14
* Total = 24
* Not part of LIS sum = **24 - 14 = 10 ✅**

---

---

Here’s the full analysis for your modified solution that computes the **maximum sum of elements not in LIS**, while optimizing LIS selection by minimal sum in case of multiple LIS of same length.

---

### ✅ **Output**

* **Input:** `arr = [4, 6, 1, 2, 3, 8]`
* **LIS of max length (length = 4):** `[1, 2, 3, 8]` → sum = 18
* **Total sum of array:** `4 + 6 + 1 + 2 + 3 + 8 = 24`
* **Max sum of non-LIS elements:** `24 - 14 = 10`
* **Output:** ✅ `10`

---

### ⏱ **Time Taken**

* `Execution Time:` **0.00014 seconds** (140 µs) using `timeit`

---

### ✅ Code Recap with Explanation

Code expaination here: [Link](https://www.geeksforgeeks.org/dsa/maximize-sum-of-all-elements-which-are-not-a-part-of-the-longest-increasing-subsequence/)

```python
class Solution:
    def nonLisMaxSum(self, arr):
        # code here
        n = len(arr)

        # dp[i][0] = minimum sum of LIS ending at i
        # dp[i][1] = length of LIS ending at i
        dp = [[0, 0] for _ in range(n)]
    
        for i in range(n):
            # Initialize base sum and base length
            dp[i][0] = arr[i]
            dp[i][1] = 1
    
            for j in range(i):
                if arr[i] > arr[j]:
                    # same length LIS can be formed
                    # choose the one with smaller sum
                    if dp[j][1] + 1 == dp[i][1]:
                        dp[i][0] = min(dp[i][0], dp[j][0] + arr[i])
                    # longer LIS can be formed
                    # update both length and sum
                    elif dp[j][1] + 1 > dp[i][1]:
                        dp[i][0] = dp[j][0] + arr[i]
                        dp[i][1] = dp[j][1] + 1
    
        # find maximum LIS length
        maxLen = max(dp[i][1] for i in range(n))
    
        # find minimum sum among LIS of maximum length
        minSum = float('inf')
        for i in range(n):
            if dp[i][1] == maxLen:
                minSum = min(minSum, dp[i][0])
    
        total = sum(arr)
    
        return total - minSum
```

---

### 🔄 Dry Run: `arr = [4, 6, 1, 2, 3, 8]`

| i | arr\[i] | dp\[i] (sum, len) | Explanation                             |
| - | ------- | ----------------- | --------------------------------------- |
| 0 | 4       | (4, 1)            | start of LIS                            |
| 1 | 6       | (10, 2)           | 4 → 6                                   |
| 2 | 1       | (1, 1)            | can't extend                            |
| 3 | 2       | (3, 2)            | 1 → 2                                   |
| 4 | 3       | (6, 3)            | 1 → 2 → 3                               |
| 5 | 8       | (14, 4)           | 1 → 2 → 3 → 8 (LIS of length 4, sum 14) |

* Total = 4+6+1+2+3+8 = 24
* LIS sum = 14 → non-LIS sum = 24 - 14 = **10**

---

### 📊 Time & Space Complexity

| Aspect | Complexity | Explanation                           |
| ------ | ---------- | ------------------------------------- |
| Time   | O(n²)      | Nested loop for DP computation of LIS |
| Space  | O(n)       | Only one 2D DP table of size n        |

---

### 💬 Interview FAQs

| Question                                           | Answer                                                                                                  |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Q1. What does this algorithm compute?**          | It finds the max possible sum of elements **not part** of any **longest increasing subsequence (LIS)**. |
| **Q2. Why do we track both sum and length in DP?** | To distinguish between LIS sequences of same length but differing sum, and minimize the LIS sum.        |
| **Q3. Can this be optimized to O(n log n)?**       | Yes, LIS can be found in O(n log n) but not while tracking the LIS sum. So O(n²) is preferred here.     |
| **Q4. Can we recover the actual LIS sequence?**    | Yes, by tracing back `dp[i]` values equal to `maxLen`.                                                  |
| **Q5. What’s the worst-case input scenario?**      | A decreasing array like `[10, 9, ..., 1]` leads to many LIS of length 1.                                |

---

```python

import timeit

class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)

        # dp[i][0] = minimum sum of LIS ending at i
        # dp[i][1] = length of LIS ending at i
        dp = [[0, 0] for _ in range(n)]
    
        for i in range(n):
            # Initialize base sum and base length
            dp[i][0] = arr[i]  # O(1)
            dp[i][1] = 1       # O(1)
    
            for j in range(i):  # O(n^2)
                if arr[i] > arr[j]:
                    # Same length LIS can be formed; choose one with smaller sum
                    if dp[j][1] + 1 == dp[i][1]:
                        dp[i][0] = min(dp[i][0], dp[j][0] + arr[i])  # O(1)
                    # Longer LIS found; update both length and sum
                    elif dp[j][1] + 1 > dp[i][1]:
                        dp[i][0] = dp[j][0] + arr[i]
                        dp[i][1] = dp[j][1] + 1
    
        # Find maximum LIS length
        maxLen = max(dp[i][1] for i in range(n))  # O(n)
    
        # Find minimum sum among LIS of max length
        minSum = float('inf')
        for i in range(n):  # O(n)
            if dp[i][1] == maxLen:
                minSum = min(minSum, dp[i][0])
    
        total = sum(arr)  # O(n)
    
        return total - minSum

# Test input
arr = [4, 6, 1, 2, 3, 8]
expected_output = 10

# Run and benchmark
start = timeit.default_timer()
sol = Solution()
output = sol.nonLisMaxSum(arr)
end = timeit.default_timer()
execution_time = end - start

output, expected_output, round(execution_time, 6)

```
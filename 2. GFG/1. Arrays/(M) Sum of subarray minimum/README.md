
---

# 🧮 Sum of Subarray Minimums

**Difficulty:** Medium
**Accuracy:** 46.92%
**Submissions:** 16K+
**Points:** 4
**Average Time:** 30m

---

## 📝 Problem Statement

Given an array `arr[]` of positive integers, find the **total sum of the minimum elements** of every possible **subarray**.

> **Note:** It is guaranteed that the total sum will fit within a 32-bit unsigned integer.

---

## 📊 Examples

### Example 1

```
Input:  arr[] = [3, 1, 2, 4]
Output: 17
```

**Explanation:**

All possible subarrays and their minimums:

```
Subarrays are:        [3], [1], [2], [4],
                      [3, 1], [1, 2], [2, 4],
                      [3, 1, 2], [1, 2, 4],
                      [3, 1, 2, 4]

Minimums are:          3,   1,   2,   4,
                       1,   1,   2,
                       1,   1,
                       1

Sum of all these = 17
```

---

### Example 2

```
Input:  arr[] = [71, 55, 82, 55]
Output: 593
```

**Explanation:**

The sum of the minimum of all the subarrays is 593.

---

## 📌 Constraints

* `1 ≤ arr.size() ≤ 3 * 10⁴`
* `1 ≤ arr[i] ≤ 10³`

---

## ⏱️ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## 🧠 Topic Tags

* Arrays
* Stack
* Data Structures

---

## 📚 Related Articles

* **[Sum Of Minimum Elements Of All Subarrays](https://www.geeksforgeeks.org/sum-of-minimum-elements-of-all-subarrays/)**

---

---

Here’s the complete solution for the **"Sum of Subarray Minimums"** problem, including explanation, dry run, multiple Python implementations, and interview Q\&A.

---

## 📘 2. Text Explanation

You're given an array `arr[]` of positive integers. You must find the **total sum** of the **minimum elements** of all possible **subarrays**.

---

### ✅ Core Idea

For every element `arr[i]`, we want to count **how many subarrays** exist where `arr[i]` is the **minimum** element. We can do this efficiently using **monotonic stacks** to find:

* **Previous Less Element (PLE)**: closest index to the **left** of `i` where `arr[j] < arr[i]`
* **Next Less Element (NLE)**: closest index to the **right** of `i` where `arr[j] < arr[i]`

Then the contribution of `arr[i]` is:

```
arr[i] * (i - PLE[i]) * (NLE[i] - i)
```

Total answer is the sum of contributions of all elements.

---

## 🔍 Dry Run

### Input:

```python
arr = [3, 1, 2, 4]
```

### Step 1: Find PLE and NLE

| i | arr\[i] | PLE index | NLE index | Contribution                   |
| - | ------- | --------- | --------- | ------------------------------ |
| 0 | 3       | -1        | 1         | 3 \* (0 - (-1)) \* (1 - 0) = 3 |
| 1 | 1       | -1        | 4         | 1 \* (1 - (-1)) \* (4 - 1) = 6 |
| 2 | 2       | 1         | 4         | 2 \* (2 - 1) \* (4 - 2) = 4    |
| 3 | 4       | 2         | 4         | 4 \* (3 - 2) \* (4 - 3) = 4    |

### Total: 3 + 6 + 4 + 4 = **17**

---

## ✅ 3. Python Implementations

---

### 🔹 Brute Force (O(n²)) — Not suitable for large inputs

```python
class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        total = 0

        for i in range(n):
            min_val = arr[i]
            for j in range(i, n):
                min_val = min(min_val, arr[j])
                total += min_val

        return total
```

* ⏱ Time: O(n²)
* 🧠 Space: O(1)

---

### 🔸 Optimized Stack-Based (O(n)) — Interview Preferred

```python
class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7
        stack = []
        ple = [-1] * n  # Previous Less Element
        nle = [n] * n   # Next Less Element

        # Find PLE for each element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Find NLE for each element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate contribution of each element
        result = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            result += arr[i] * left * right
            result %= mod

        return result
```

* ✅ Time: O(n)
* ✅ Space: O(n)

---

Here’s the **complete Python program** for the **Sum of Subarray Minimums** using the **PLE + NLE monotonic stack method**, including:

* ✅ Inline comments for logic and complexity at each step
* ✅ Sample input and output
* ✅ Execution time measurement using `time.time()`

---

```python
import time

class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7

        # Step 1: Initialize Previous and Next Less Element arrays
        # Time: O(n)
        ple = [-1] * n   # PLE[i]: index of previous less element
        nle = [n] * n    # NLE[i]: index of next less element
        stack = []

        # Step 2: Compute Previous Less Element (PLE)
        # Time: O(n), each element is pushed/popped once
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # Clear stack for NLE computation
        stack.clear()

        # Step 3: Compute Next Less Element (NLE)
        # Time: O(n), same as PLE
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # Step 4: Compute final result using contribution of each element
        # Time: O(n)
        result = 0
        for i in range(n):
            left = i - ple[i]       # Elements to the left where arr[i] is min
            right = nle[i] - i      # Elements to the right where arr[i] is min
            result += arr[i] * left * right
            result %= mod           # To avoid overflow

        return result


# ------------------------ Driver with Timing ------------------------

if __name__ == "__main__":
    arr = [3, 1, 2, 4]  # Example input
    print("Input:", arr)

    start_time = time.time()

    sol = Solution()
    output = sol.sumSubMins(arr)

    end_time = time.time()
    elapsed = end_time - start_time

    print("Sum of Subarray Minimums:", output)
    print("Execution Time: {:.6f} seconds".format(elapsed))
```

---

### ✅ Sample Output

```
Input: [3, 1, 2, 4]
Sum of Subarray Minimums: 17
Execution Time: 0.0000XX seconds
```

---

### 📊 Time and Space Complexity

| Step            | Time Complexity | Space Complexity |
| --------------- | --------------- | ---------------- |
| PLE computation | O(n)            | O(n)             |
| NLE computation | O(n)            | O(n)             |
| Final summation | O(n)            | O(1)             |
| **Total**       | **O(n)**        | **O(n)**         |

---

## 🧠 4. Interview Questions & Answers

---

### ❓ Q1: Why can’t we use brute force?

**A:** It leads to O(n²) time complexity which is too slow for n up to 30,000. Interviewers expect O(n) solutions using monotonic stacks.

---

### ❓ Q2: What is the logic behind `(i - PLE[i]) * (NLE[i] - i)`?

**A:** This gives the number of subarrays where `arr[i]` is the minimum — all possible subarrays starting between `PLE[i]+1` and `i`, and ending between `i` and `NLE[i]-1`.

---

### ❓ Q3: Why use `>` in PLE and `>=` in NLE?

**A:** This avoids double-counting equal elements:

* Use `>` for PLE to ensure previous smaller elements are truly smaller.
* Use `>=` for NLE to push the current to the correct side (monotonicity in ascending order).

---

### ❓ Q4: Why modulo $10^9 + 7$?

**A:** The sum can become very large. The problem typically restricts the final output to within 32-bit or 64-bit unsigned integer using a modulo.

---

### ❓ Q5: Can there be duplicates?

**A:** Yes. That's why we use strict and non-strict comparisons in the stack logic.

---

# 🤺 Monotonic stack optimization

```python
class Solution:
    def sumSubMins(self, arr):
        # Code here
        n = len(arr)
        left = [0] * n
        right = [0] * n
    
        s1 = []  
        s2 = []  
    
        # Count elements greater 
        # than arr[i] on the left
        for i in range(n):
            
            # get elements from stack until element 
            # greater to arr[i] found
            count = 1
            while s1 and s1[-1][0] > arr[i]:
                count += s1.pop()[1]
            s1.append((arr[i], count))
            left[i] = count
    
        # Count elements greater than 
        # or equal to arr[i] on the right
        for i in range(n - 1, -1, -1):
            
            # get elements from stack until element 
            # greater or equal to arr[i] found
            count = 1
            while s2 and s2[-1][0] >= arr[i]:
                count += s2.pop()[1]
            s2.append((arr[i], count))
            right[i] = count
    
        result = 0
        for i in range(n):
            result += arr[i] * left[i] * right[i]
    
        return result
```

✅ This is a **very efficient and elegant solution** for the **"Sum of Subarray Minimums"** problem — it's actually the **multiplicative span-based approach**, and **equivalent in performance** to the PLE/NLE method but with a slightly different counting style.

Let’s break it down:

---

## ✅ What This Approach Does

It computes:

* `left[i]`: **number of subarrays ending at i** where `arr[i]` is the minimum.
* `right[i]`: **number of subarrays starting at i** where `arr[i]` is the minimum.

Then multiplies:

```python
arr[i] * left[i] * right[i]
```

to get the total contribution of `arr[i]` as minimum across all such subarrays.

---

## 🔁 Key Differences From PLE/NLE

* Instead of storing indices and calculating span using index differences (`i - PLE[i]`, etc.), this code uses **counts directly** by popping from the stack while tracking how many elements it collapsed.

* The **left** span uses `>` (strictly greater)

* The **right** span uses `>=` (non-strictly greater)

This combination **avoids double-counting** for duplicate elements and ensures **uniqueness** in subarray combinations.

---

## ✅ Complexity

| Component        | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Left Count Pass  | O(n)            | O(n)             |
| Right Count Pass | O(n)            | O(n)             |
| Final Sum Loop   | O(n)            | O(1)             |
| **Total**        | **O(n)**        | **O(n)**         |

---

## ✅ Updated Code With Comments and Timing

```python
import time

class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7

        left = [0] * n  # Number of elements >= arr[i] to the left
        right = [0] * n  # Number of elements >= arr[i] to the right

        s1 = []  # Stack for left span
        s2 = []  # Stack for right span

        # Left span (count elements greater than arr[i] to the left)
        # Time: O(n)
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > arr[i]:
                count += s1.pop()[1]
            s1.append((arr[i], count))
            left[i] = count

        # Right span (count elements >= arr[i] to the right)
        # Time: O(n)
        for i in range(n - 1, -1, -1):
            count = 1
            while s2 and s2[-1][0] >= arr[i]:
                count += s2.pop()[1]
            s2.append((arr[i], count))
            right[i] = count

        # Final calculation using contributions
        # Time: O(n)
        result = 0
        for i in range(n):
            result += arr[i] * left[i] * right[i]
            result %= mod

        return result


# --------------- Execution with Input & Timer ---------------

if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    print("Input:", arr)

    start_time = time.time()
    
    sol = Solution()
    output = sol.sumSubMins(arr)
    
    end_time = time.time()
    elapsed = end_time - start_time

    print("Sum of Subarray Minimums:", output)
    print("Execution Time: {:.6f} seconds".format(elapsed))
```

---

## ✅ Sample Output

```
Input: [3, 1, 2, 4]
Sum of Subarray Minimums: 17
Execution Time: 0.0000XX seconds
```

---

## 🧠 Summary

* ✅ Uses multiplicative span logic.
* ✅ Time-efficient: O(n)
* ✅ Space-efficient: O(n)
* ✅ Accepted in interviews and competitions.

---

---

# 🥸 Dynamic Programming Approach

```python
class Solution:
    def sumSubMins(self, arr):
        # Code here
        n = len(arr)
        dp = [0] * n
        right = [i for i in range(n)]
        stack = []
    
        # Find index of next 
        # smaller element on the right
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)
    
        # Fill dp[] from right to left
        dp[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            r = right[i]
            if r == i:
                dp[i] = (n - i) * arr[i]
            else:
                dp[i] = (r - i) * arr[i] + dp[r]
    
        return sum(dp)
```

✅ This approach is a **variation using dynamic programming + next smaller element (NSE)**. It’s elegant and effective — although **less intuitive** than the standard PLE/NLE or span approaches, it achieves the same **O(n)** time complexity.

---

## 🔍 How This Approach Works

1. **`right[i]`** stores the index of the **next smaller element** to the right of `arr[i]`.

   * If none exists, we assume it's the end (`n`).
   * This is computed using a monotonic **increasing stack**.

2. **`dp[i]`** stores the sum of minimums of all subarrays **starting** at index `i`.

   If `right[i] == i` → no smaller value after `i` → use the full length to the end.
   Else → break the problem into:

   ```
   (r - i) * arr[i] + dp[r]
   ```

   Where:

   * `(r - i) * arr[i]` is the total contribution of `arr[i]` as minimum from `i` to `r - 1`
   * `dp[r]` recursively adds contributions for subarrays starting from `r`

3. Finally, `sum(dp)` gives the total sum of subarray minimums.

---

## ✅ Complexity

| Step      | Time     | Space    |
| --------- | -------- | -------- |
| NSE Stack | O(n)     | O(n)     |
| DP Fill   | O(n)     | O(n)     |
| Final Sum | O(n)     | O(1)     |
| **Total** | **O(n)** | **O(n)** |

---

## ✅ Full Code with Comments & Timing

```python
import time

class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        dp = [0] * n           # dp[i]: sum of mins of subarrays starting at i
        right = [i for i in range(n)]  # right[i]: next smaller element index
        stack = []

        # Step 1: Find next smaller element to the right
        # Time: O(n), Space: O(n)
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)

        # Step 2: Fill dp from right to left
        # Time: O(n)
        dp[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            r = right[i]
            if r == i:
                dp[i] = (n - i) * arr[i]
            else:
                dp[i] = (r - i) * arr[i] + dp[r]

        return sum(dp) % (10**9 + 7)  # Add mod if needed for large outputs


# ------------------ Example Run & Timing ------------------

if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    print("Input:", arr)

    start_time = time.time()

    sol = Solution()
    result = sol.sumSubMins(arr)

    end_time = time.time()

    print("Sum of Subarray Minimums:", result)
    print("Execution Time: {:.6f} seconds".format(end_time - start_time))
```

---

## ✅ Sample Output

```
Input: [3, 1, 2, 4]
Sum of Subarray Minimums: 17
Execution Time: 0.0000XX seconds
```

---

## 🧠 Pros & Considerations

✅ **Pros:**

* Efficient O(n)
* Avoids needing both left and right span calculations
* Neat recursion-like reuse with `dp[i] = ... + dp[r]`

⚠️ **Considerations:**

* A bit harder to reason about during an interview (vs PLE/NLE)
* You must ensure `right[i] == i` is correctly handled

---

### ✅ Summary

| Approach                    | Time | Space | Intuition              |
| --------------------------- | ---- | ----- | ---------------------- |
| PLE/NLE (span)              | O(n) | O(n)  | Very intuitive         |
| Stack + Multiplicative Span | O(n) | O(n)  | Elegant                |
| This DP + NSE method        | O(n) | O(n)  | Efficient but trickier |

---

---

Here's a **comprehensive comparison** of all major approaches for solving the **"Sum of Subarray Minimums"** problem:

---

## ✅ Problem Recap

Given an array `arr[]`, compute the sum of the **minimum** elements of **every possible subarray**.

---

## ✅ Approaches Compared

|  # | Approach                               | Time Complexity | Space Complexity | Interview Suitability | Intuition         | Highlights                    |
| -: | -------------------------------------- | --------------- | ---------------- | --------------------- | ----------------- | ----------------------------- |
|  1 | **Brute Force (Nested loops)**         | O(n²)           | O(1)             | ❌ Low                 | ✅ Easy to grasp   | Too slow for `n > 10⁴`        |
|  2 | **Monotonic Stack (PLE/NLE)**          | O(n)            | O(n)             | ✅ High                | ✅ Very intuitive  | Industry-standard             |
|  3 | **Multiplicative Span (Left × Right)** | O(n)            | O(n)             | ✅ High                | ✅ Clean logic     | Elegant, readable             |
|  4 | **DP + NSE (Right only)**              | O(n)            | O(n)             | ✅ Medium              | ⚠️ Less intuitive | Efficient, but trickier logic |

---

### 🔹 1. Brute Force Approach

```python
for i in range(n):
    min_val = arr[i]
    for j in range(i, n):
        min_val = min(min_val, arr[j])
        total += min_val
```

* ✅ Simple logic
* ❌ Inefficient for large `n`
* ❌ Not acceptable in interviews for this problem

---

### 🔹 2. Monotonic Stack (PLE + NLE)

* Use stack to compute:

  * `PLE[i]` = index of previous less-than element
  * `NLE[i]` = index of next less-than element
* Contribution: `arr[i] * (i - PLE[i]) * (NLE[i] - i)`

```python
contribution = arr[i] * left_count * right_count
```

* ✅ Time: O(n)
* ✅ Intuitive, widely used
* ✅ Gold standard for interviews

---

### 🔹 3. Multiplicative Span Method (Using Stack)

```python
left[i] = count of > arr[i] to left (strictly greater)
right[i] = count of ≥ arr[i] to right (greater or equal)
contribution = arr[i] * left[i] * right[i]
```

* Stack holds `(value, count)`

* Easy to implement

* Matches intuition of how many subarrays include `arr[i]` as the minimum

* ✅ O(n) time and space

* ✅ Slightly shorter than PLE/NLE version

* ✅ Frequently used in coding rounds

---

### 🔹 4. DP + Next Smaller Element (Right-only)

```python
# dp[i] = sum of mins for subarrays starting at i
dp[i] = (r - i) * arr[i] + dp[r]
```

* `right[i]`: index of next smaller element

* Works in reverse using DP

* Avoids computing PLE (left) altogether

* ✅ O(n) time

* ✅ Compact

* ⚠️ Less intuitive for new learners

* ⚠️ Needs careful handling of edge cases (`right[i] == i`)

---

## 🏆 Summary Table

| Feature / Approach          | Brute Force | Stack (PLE/NLE) | Span (Left × Right) | DP + NSE (Right) |
| --------------------------- | ----------- | --------------- | ------------------- | ---------------- |
| Time Complexity             | ❌ O(n²)     | ✅ O(n)          | ✅ O(n)              | ✅ O(n)           |
| Space Complexity            | ✅ O(1)      | ⚠️ O(n)         | ⚠️ O(n)             | ⚠️ O(n)          |
| Stack Usage                 | ❌           | ✅               | ✅                   | ✅                |
| DP Involved                 | ❌           | ❌               | ❌                   | ✅                |
| Intuitiveness               | ✅✅✅         | ✅✅              | ✅✅✅                 | ⚠️               |
| Interview Recommended       | ❌           | ✅✅✅             | ✅✅✅                 | ✅                |
| Handles duplicates properly | ❌           | ✅               | ✅                   | ✅                |
| Modulo Handling             | ⚠️ (manual) | ✅               | ✅                   | ✅                |

---

## ✅ Final Verdict

| Use This When...                             | Best Choice                            |
| -------------------------------------------- | -------------------------------------- |
| You're in an interview                       | **Stack (PLE/NLE)** or **Span Method** |
| You want clean, short code                   | **Span (Left × Right)**                |
| You want to avoid both PLE and span tracking | **DP + NSE**                           |
| Just learning the problem                    | **Brute force**, then **Span/Stack**   |

---

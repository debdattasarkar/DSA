
---

# ❓Next Element with Greater Frequency

**Difficulty:** Medium
**Accuracy:** 60.4%
**Submissions:** 16K+
**Points:** 4

---

## 🧠 Problem Statement

Given an array `arr[]` of integers, for each element, find the **closest** (distance-wise) element **to its right** that has a **higher frequency** than the current element.

If no such element exists, return `-1` for that position.

---

## ✨ Examples

### Example 1:

**Input:**

```
arr[] = [2, 1, 1, 3, 2, 1]
```

**Output:**

```
[1, -1, -1, 2, 1, -1]
```

**Explanation:**
Frequencies:

* 1 → 3 times
* 2 → 2 times
* 3 → 1 time

Analysis:

* For `arr[0] = 2`, the next element **1** has higher frequency → `1`
* For `arr[1]` and `arr[2]` = 1, no right element has higher frequency → `-1`
* For `arr[3] = 3`, the next element **2** has higher frequency → `2`
* For `arr[4] = 2`, the next element **1** has higher frequency → `1`
* For `arr[5] = 1`, no elements to the right → `-1`

---

### Example 2:

**Input:**

```
arr[] = [5, 1, 5, 6, 6]
```

**Output:**

```
[-1, 5, -1, -1, -1]
```

**Explanation:**
Frequencies:

* 1 → 1 time
* 5 → 2 times
* 6 → 2 times

Analysis:

* For `arr[0] = 5`, no right element has higher frequency → `-1`
* For `arr[1] = 1`, the next element **5** has higher frequency → `5`
* For `arr[2] = 5`, no right element has higher frequency → `-1`
* For `arr[3] = 6` and `arr[4] = 6`, no right elements with higher frequency → `-1`

---

## ✅ Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr}[i] \leq 10^5$

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏷 Topic Tags

* Hash
* Stack
* Data Structures

---

## 📄 Related Articles

* [Next Greater Frequency Element](https://www.geeksforgeeks.org/next-greater-frequency-element/)

---

---

# 🅰️Solution

Here’s a complete breakdown for **"Next Element with Greater Frequency"** in Python, covering explanation, dry run, brute/optimized solutions, and interview Q\&A.

---

## 📘 2. Text Explanation

You are given an array of integers `arr[]`.

For each element `arr[i]`, you must find the **first element to the right** that has a **strictly higher frequency** than `arr[i]`.
If no such element exists, return `-1` for that index.

---

### ✅ Approach Summary:

1. Count the frequency of each number using a hash map.
2. Use a **monotonic stack** to track indices whose next greater frequency element is not yet found.
3. Traverse the array **from right to left**:

   * While the stack has elements **less than or equal** in frequency, pop them.
   * If stack is not empty, top of the stack is the next greater frequency element.
   * Push the current index onto the stack.

---

## 🔍 Step-by-Step Dry Run

### Input:

```python
arr = [2, 1, 1, 3, 2, 1]
```

### Step 1: Frequency map:

```
freq = {1: 3, 2: 2, 3: 1}
```

### Step 2: Traverse right to left:

| i | arr\[i] | freq | Stack              | Result |
| - | ------- | ---- | ------------------ | ------ |
| 5 | 1       | 3    | \[]                | -1     |
| 4 | 2       | 2    | \[5] (1)           | 1      |
| 3 | 3       | 1    | \[4] (2), \[5] (1) | 2      |
| 2 | 1       | 3    | \[3] (3)           | -1     |
| 1 | 1       | 3    | \[2] (1)           | -1     |
| 0 | 2       | 2    | \[1] (1)           | 1      |

✅ Final Output: `[1, -1, -1, 2, 1, -1]`

---

## ✅ 3. Python Implementations

---

### 🔹 Brute Force (O(n²)) — for understanding only

```python
class Solution:
    def findGreater(self, arr):
        from collections import Counter

        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n

        for i in range(n):
            for j in range(i + 1, n):
                if freq[arr[j]] > freq[arr[i]]:
                    res[i] = arr[j]
                    break

        return res
```

* ⏱ Time: O(n²)
* 🧠 Space: O(n)

---

### 🔸 Optimized Stack + HashMap (O(n)) — Interview standard

```python
class Solution:
    def findGreater(self, arr):
        from collections import Counter

        n = len(arr)
        freq = Counter(arr)          # Step 1: Count frequencies
        result = [-1] * n            # Step 2: Initialize result
        stack = []                   # Stack will hold indices

        # Step 3: Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop while stack top has frequency <= current
            while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
                stack.pop()

            # If stack not empty, it's the next greater freq element
            if stack:
                result[i] = arr[stack[-1]]

            # Push current index for future comparisons
            stack.append(i)

        return result
```

* ✅ Time: O(n)
* ✅ Space: O(n)

---

## 🧠 4. Interview Q\&A

---

### ❓ Q1: Why do we need a frequency map?

**A:** Because we compare **frequencies**, not actual values. We need fast access to how often each element occurs — hence, a hash map (dictionary).

---

### ❓ Q2: Why process from right to left?

**A:** We’re looking for the **next** element to the right with higher frequency. By traversing right to left, we ensure we already know future options.

---

### ❓ Q3: Why use a stack?

**A:** Stack helps in maintaining a **monotonic structure** — we pop elements that are not useful and retain only possible future NGEF (Next Greater Frequency) candidates.

---

### ❓ Q4: When is the result `-1`?

**A:** If there is **no element to the right** with a **higher frequency**, we leave that index as `-1`.

---

### ❓ Q5: Can there be multiple valid answers?

**A:** No. We want the **first one to the right** (closest), not just any.

---

---

# 👨‍💻Here is the **full Python program** for **Next Element with Greater Frequency**, including:

* ✅ Inline comments with **time and space complexity**
* ✅ Example **input/output**
* ✅ Execution timing using `time.time()`

---

```python
import time
from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)

        # Step 1: Count frequencies of each element
        # Time: O(n)
        # Space: O(n) for frequency map
        freq = Counter(arr)

        # Step 2: Initialize result with -1 (default)
        # Time: O(n)
        # Space: O(n) for result array
        result = [-1] * n

        # Step 3: Monotonic Stack to track indices
        # Time: Overall O(n), each index is pushed/popped once
        # Space: O(n) for the stack
        stack = []

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop stack while frequency at top is <= current
            while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
                stack.pop()

            # If stack not empty, top is the next greater frequency element
            if stack:
                result[i] = arr[stack[-1]]

            # Push current index to stack for future use
            stack.append(i)

        return result


# ------------------------- Execution + Timing -------------------------

if __name__ == "__main__":
    # Example input
    arr = [2, 1, 1, 3, 2, 1]
    print("Input:", arr)

    # Start time
    start_time = time.time()

    # Run solution
    sol = Solution()
    output = sol.findGreater(arr)

    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Output result
    print("Next Element with Greater Frequency:", output)
    print("Execution Time: {:.6f} seconds".format(elapsed_time))
```

---

### ✅ Sample Output:

```
Input: [2, 1, 1, 3, 2, 1]
Next Element with Greater Frequency: [1, -1, -1, 2, 1, -1]
Execution Time: 0.0000XX seconds
```

---

### 📊 Time & Space Complexity Summary

| Component             | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Frequency Count       | O(n)            | O(n)             |
| Result Initialization | O(n)            | O(n)             |
| Stack Traversal       | O(n)            | O(n)             |
| **Total**             | **O(n)**        | **O(n)**         |

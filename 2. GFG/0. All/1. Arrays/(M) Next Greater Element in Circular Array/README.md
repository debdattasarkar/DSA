
---

# Next Greater Element in Circular Array

**Difficulty:** Medium
**Accuracy:** 56.97%
**Submissions:** 48K+
**Points:** 4

---

## 🧠 Problem Statement

Given a **circular integer array** `arr[]`, the task is to determine the **Next Greater Element (NGE)** for each element in the array.

The **next greater element** of an element `arr[i]` is the **first element** that is greater than `arr[i]` when traversing **circularly**.
If no such element exists, return **-1** for that position.

---

## 🔁 Circular Property

Since the array is **circular**, after reaching the last element, the search continues from the **beginning** until all elements are checked **once**.

---

## ✨ Examples

### Example 1:

**Input:**

```
arr[] = [1, 3, 2, 4]
```

**Output:**

```
[3, 4, 4, -1]
```

**Explanation:**

* The next greater element for **1** is **3**
* The next greater element for **3** is **4**
* The next greater element for **2** is **4**
* The next greater element for **4** does not exist → `-1`

---

### Example 2:

**Input:**

```
arr[] = [0, 2, 3, 1, 1]
```

**Output:**

```
[2, 3, -1, 2, 2]
```

**Explanation:**

* The next greater element for **0** is **2**
* The next greater element for **2** is **3**
* The next greater element for **3** does not exist → `-1`
* The next greater element for **1** is **2** (from circular traversal)
* The next greater element for **1** is **2** (from circular traversal)

---

## ✅ Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $0 \leq \text{arr}[i] \leq 10^6$

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏷 Topic Tags

* Stack
* Data Structures

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft

---

## 📚 Related Interview Experiences

* [Flipkart Interview Experience For SDE Internship 2021](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-internship-2021/)

---

## 📄 Related Articles

* [Find The Next Greater Element In A Circular Array](https://www.geeksforgeeks.org/next-greater-element/)
* [Next Greater Element](https://leetcode.com/problems/next-greater-element-ii/)

---

Here’s a complete guide for the **Next Greater Element in Circular Array** problem, covering all four parts:

---

## 📘 2. Text Explanation

Given a circular array `arr[]`, the task is to find the **Next Greater Element (NGE)** for each element.

* The **NGE** for `arr[i]` is the **first element** that is **strictly greater than `arr[i]`**, when traversing **rightward circularly**.
* If no such element exists, return `-1` for that position.

---

### 🔁 Key Idea: Stack + 2n Traversal

* To simulate the circular nature, we loop through the array **twice (2n)**.
* We use a **monotonic decreasing stack** to keep track of **indices** whose NGE hasn't been found yet.
* For each element from right to left (index `2n-1` to `0`), we:

  1. Pop smaller/equal elements from the stack.
  2. If stack is not empty, the top is the NGE.
  3. Push the current element’s index on the stack.

---

## 🔍 Step-by-Step Dry Run

Input:

```python
arr = [1, 3, 2, 4]
```

Simulate circularity by traversing from index `7` to `0` (2n–1 to 0):

| i | i % n | arr\[i % n] | Stack      | Result                |
| - | ----- | ----------- | ---------- | --------------------- |
| 7 | 3     | 4           | \[]        | -1 (nothing in stack) |
| 6 | 2     | 2           | \[3]       | 4                     |
| 5 | 1     | 3           | \[3]       | 4                     |
| 4 | 0     | 1           | \[1, 3]    | 3                     |
| 3 | 3     | 4           | \[0, 1, 3] | -1                    |
| 2 | 2     | 2           | \[3]       | 4                     |
| 1 | 1     | 3           | \[3]       | 4                     |
| 0 | 0     | 1           | \[1, 3]    | 3                     |

Final Output: `[3, 4, 4, -1]`

---

---

## ✅ 3. Python Implementations

---

### 🔹 Brute Force (O(n²)) — Not Optimal but Good for Understanding

```python
class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n

        for i in range(n):
            for j in range(1, n):
                idx = (i + j) % n
                if arr[idx] > arr[i]:
                    res[i] = arr[idx]
                    break
        return res
```

* 🔸 **Time:** O(n²)
* 🔸 **Space:** O(1) extra

---

### 🔸 Optimized Stack-Based (O(n)) — Interview Preferred

```python
class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []  # Stack stores indices

        # Traverse array twice in reverse to simulate circularity
        for i in range(2 * n - 1, -1, -1):
            cur = arr[i % n]
            
            # Pop all smaller or equal elements
            while stack and arr[stack[-1]] <= cur:
                stack.pop()
            
            if i < n:
                # Only fill result in the first pass
                if stack:
                    res[i] = arr[stack[-1]]
                # Else, default is -1 (no greater)
            
            # Push index for future comparisons
            stack.append(i % n)

        return res
```

* ✅ **Time Complexity:** O(n)
* ✅ **Space Complexity:** O(n)

---

## 🧠 4. Interview Questions & Answers

---

### ❓ Q1: Why do we simulate circular traversal using `2n` loop?

**A:** It ensures that for every element, we look at all possible successors in a circular fashion.

---

### ❓ Q2: Why use stack instead of nested loops?

**A:** Stack gives us an efficient way (O(n)) to track the next greater element using a **monotonic structure**.

---

### ❓ Q3: What does the stack store?

**A:** It stores **indices** of elements for which we haven’t found a next greater value yet.

---

### ❓ Q4: Why traverse from right to left?

**A:** This helps maintain a **monotonic decreasing stack**, where the top is the smallest greater candidate.

---

### ❓ Q5: Can there be multiple next greater elements?

**A:** Yes, but we return only the **first** greater one (circularly) to the right.

---

---

Here’s the **complete Python program** for **Next Greater Element in Circular Array**, using your provided solution:

✔️ Includes:

* Full inline comments explaining logic and complexities
* Input/output printing
* `time.time()` to measure runtime
* Stack-based approach (expected in interviews)

---

```python
import time

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)

        # Step 1: Initialize result array with -1
        # Time: O(n)
        res = [-1] * n

        # Step 2: Stack to store indices of next greater candidates
        # Space: O(n) in worst case
        stack = []

        # Step 3: Traverse the array in reverse (2n - 1 to 0)
        # to simulate circular array behavior
        # Time: O(2n) = O(n), each element pushed/popped at most once
        for i in range(2 * n - 1, -1, -1):
            cur = arr[i % n]

            # Pop smaller/equal elements from the stack
            while stack and arr[stack[-1]] <= cur:
                stack.pop()

            # Fill result only in the first n indices
            if i < n:
                if stack:
                    res[i] = arr[stack[-1]]
                # If no greater element found, result[i] remains -1

            # Push current index modulo n to stack
            stack.append(i % n)

        return res

# ---------- 🧪 Example Run and Timing ----------

if __name__ == "__main__":
    arr = [1, 3, 2, 4]  # Example input
    print("Input:", arr)

    start_time = time.time()

    sol = Solution()
    result = sol.nextLargerElement(arr)

    end_time = time.time()
    elapsed = end_time - start_time

    print("Next Greater Elements:", result)
    print("Execution Time: {:.6f} seconds".format(elapsed))
```

---

### ✅ Sample Output:

```
Input: [1, 3, 2, 4]
Next Greater Elements: [3, 4, 4, -1]
Execution Time: 0.0000XX seconds
```

---

### 📊 Time & Space Complexity Summary

| Step                       | Time Complexity | Space Complexity |
| -------------------------- | --------------- | ---------------- |
| Initialize result array    | O(n)            | O(n)             |
| Stack-based traversal (2n) | O(n)            | O(n)             |
| **Total**                  | **O(n)**        | **O(n)**         |

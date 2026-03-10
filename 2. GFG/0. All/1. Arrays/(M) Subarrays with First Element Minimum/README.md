
---

# **Subarrays with First Element Minimum**

**Difficulty:** Medium  
**Accuracy:** 56.75%  
**Submissions:** 15K+  
**Points:** 4  

---

## 📘 **Problem Statement**

Given an array `arr[]`, count the number of **subarrays** in which the **first element is the minimum element** of that subarray.

A subarray is considered **valid** if:

- The **first element** is **not greater than any other element** in that subarray.

---

## 📝 **Examples**

### **Example 1**

**Input:**  
`arr[] = [1, 2, 1]`

**Output:**  
`5`

**Explanation:**  
All possible subarrays:  
- `[1]`  
- `[1, 2]`  
- `[1, 2, 1]`  
- `[2]`  
- `[2, 1]`  
- `[1]`

Valid subarrays (first element is minimum):  
- `[1]`  
- `[1, 2]`  
- `[1, 2, 1]`  
- `[2]`  
- `[1]`

Total valid = **5**

---

### **Example 2**

**Input:**  
`arr[] = [1, 3, 5, 2]`

**Output:**  
`8`

**Explanation:**  
Valid subarrays:  
- `[1]`  
- `[1, 3]`  
- `[1, 3, 5]`  
- `[1, 3, 5, 2]`  
- `[3]`  
- `[3, 5]`  
- `[5]`  
- `[2]`

Total valid = **8**

---

## 📏 **Constraints**

- `1 ≤ arr.size() ≤ 5 * 10^4`
- `1 ≤ arr[i] ≤ 10^5`

---

## ⏱️ **Expected Complexity**

| Type | Complexity |
|------|------------|
| **Time** | `O(n)` |
| **Auxiliary Space** | `O(n)` |

---

## 🏷️ **Topic Tags**

- Stack  
- Arrays  
- Data Structures  

---

## 📚 **Related Articles**

- *Count Of Subarrays Whose First Element Is The Minimum*

---

---

Debdatta, let’s turn this into a crisp, interview‑ready master guide.  
I’ll give you:

1. **Crystal‑clear explanation of the logic**  
2. **Step‑by‑step dry run**  
3. **Brute‑force + Optimized Python solutions** (interview‑friendly, with clean variable names + inline comments)  
4. **Interview cheat‑sheet: what to say, how to think, what interviewers expect**

Let’s dive in.

---

# ⭐ 2. Text Explanation (Concept + Intuition)

The problem asks:

> Count subarrays where the **first element is the minimum** in that subarray.

Meaning:

For a subarray starting at index `i`, we can extend it to the right **as long as no element is smaller than arr[i]**.

So for each index `i`:

- We want to know:  
  **How far to the right can we go before we hit a smaller element?**

This is a classic **Next Smaller Element (NSE)** problem.

If the next smaller element is at index `j`, then:

- Valid subarrays starting at `i` = `j - i`
- If no smaller element exists → extend till end → `(n - i)`

This gives an **O(n)** solution using a **monotonic increasing stack**.

---

# ⭐ Step-by-Step Dry Run  
Let’s dry‑run the optimized logic on:

```
arr = [1, 3, 5, 2]
```

### Step 1 — Find Next Smaller Element (NSE)

We traverse from right to left using a stack that keeps elements in **increasing order**.

| Index | Value | Stack State | NSE |
|-------|--------|--------------|------|
| 3 | 2 | [] → push 2 | NSE = 4 (no smaller) |
| 2 | 5 | [2] → 2 < 5 → NSE = 3 | push 5 |
| 1 | 3 | [2,5] → 2 < 3 → NSE = 3 | push 3 |
| 0 | 1 | [2,5,3] → 2 < 1? No → 1 < 2 → pop 2 → stack empty → NSE = 4 | push 1 |

Final NSE array (index of next smaller element):

```
NSE = [4, 3, 3, 4]
```

### Step 2 — Count valid subarrays

Formula:

```
valid_subarrays[i] = NSE[i] - i
```

| i | arr[i] | NSE[i] | Count |
|---|--------|--------|--------|
| 0 | 1 | 4 | 4 |
| 1 | 3 | 3 | 2 |
| 2 | 5 | 3 | 1 |
| 3 | 2 | 4 | 1 |

Total = 4 + 2 + 1 + 1 = **8**

Matches expected output.

---

# ⭐ 3. Python Solutions (Brute → Optimized)

---

# ✅ **Solution 1: Brute Force (O(n²))**  
Good for explaining logic in interviews.

```python
class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        total_valid = 0
        
        # For every starting index
        for start in range(n):
            min_value = arr[start]
            
            # Extend subarray to the right
            for end in range(start, n):
                if arr[end] < min_value:
                    break  # invalid, stop extending
                
                total_valid += 1
        
        return total_valid
```

---

# ✅ **Solution 2: Optimized Using Next Smaller Element (O(n))**

This is the expected interview solution.

```python
class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        next_smaller_index = [n] * n  # default: no smaller element
        stack = []  # monotonic increasing stack
        
        # Step 1: Compute Next Smaller Element (NSE)
        for i in range(n - 1, -1, -1):
            # Maintain increasing stack
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            # If stack not empty, top is next smaller
            if stack:
                next_smaller_index[i] = stack[-1]
            
            stack.append(i)
        
        # Step 2: Count valid subarrays
        total_valid = 0
        for i in range(n):
            total_valid += next_smaller_index[i] - i
        
        return total_valid
```

---

# ⭐ 4. Interview Cheat‑Sheet  
Here’s how to sound sharp and structured in an interview.

---

## 🎤 **Q1. What is the problem asking?**

**A:**  
We must count subarrays where the first element is the minimum.  
For each index `i`, we extend the subarray to the right until we hit a smaller element.

---

## 🎤 **Q2. What is the brute‑force approach?**

**A:**  
Try all subarrays starting at each index and stop when a smaller element appears.  
Time complexity: **O(n²)**.

---

## 🎤 **Q3. Can we optimize it?**

**A:**  
Yes.  
We only need to know **how far each index can extend before a smaller element appears**.  
This is exactly the **Next Smaller Element** problem.

---

## 🎤 **Q4. What data structure helps here?**

**A:**  
A **monotonic increasing stack**.  
It gives NSE for all elements in **O(n)**.

---

## 🎤 **Q5. How do you compute the final answer?**

**A:**  
If the next smaller element for index `i` is at `j`, then:

```
valid_subarrays = j - i
```

If no smaller element exists, we use `n`.

---

## 🎤 **Q6. Why does this work?**

**A:**  
Because the first element must be the minimum.  
The moment we hit a smaller element, the subarray becomes invalid.

---

## 🎤 **Q7. What is the final time complexity?**

**A:**  
`O(n)` time, `O(n)` space.

---

# ⭐ How to Remember This in Interviews

Here’s the mental shortcut:

### **“First element must stay minimum → stop when smaller appears → NSE.”**

Or even shorter:

### **“Minimum at start → Next Smaller Element.”**

If you say this confidently, interviewers immediately know you understand the pattern.

---

---

# ⭐ 5. Real‑World Use Cases (Only the most relatable ones)

These are the kind of examples interviewers *love* because they connect algorithms to real systems.

---

## **📌 Use Case 1 — Stock Market Trend Analysis**
When analyzing stock prices, you often want to find:

> “How long does the price stay above a certain threshold before dropping?”

This is identical to:

- Treat each price as the first element of a subarray.
- Extend until a smaller price appears.

This is exactly the **Next Smaller Element** logic.

---

## **📌 Use Case 2 — Quality Control in Manufacturing**
Imagine a conveyor belt where each product has a “defect score”.

You want to know:

> “For each product, how many subsequent products have equal or worse defect scores?”

Again:

- First element = reference product
- Subarray extends until a smaller score appears

Perfect match.

---

## **📌 Use Case 3 — Website Performance Monitoring**
Suppose you track server response times.

You want to know:

> “For how long does the server maintain a response time that is not worse than the current reading?”

This is literally:

- First element = current response time
- Extend until a smaller (faster) response time appears

---

## **📌 Use Case 4 — Customer Queue Priority**
In a queue with priority numbers:

> “How many customers after this one have equal or lower priority?”

Same logic: extend until a smaller priority number appears.

---

These examples show the interviewer that you understand the *pattern*, not just the code.

---

# ⭐ 6. Full Python Program  
With:

- Inline comments  
- Time & space complexity notes  
- Sample input/output  
- Timing using `time` module  

---

# ✅ **Full Program (Optimized O(n) + Timing + Example Run)**

```python
import time

class Solution:
    def countSubarrays(self, arr):
        """
        Time Complexity:
            - Building Next Smaller Element (NSE): O(n)
            - Counting valid subarrays: O(n)
            Total: O(n)

        Space Complexity:
            - Stack + NSE array: O(n)
        """

        n = len(arr)
        next_smaller_index = [n] * n  # default: no smaller element found
        stack = []  # monotonic increasing stack

        # -----------------------------
        # Step 1: Compute Next Smaller Element (NSE)
        # -----------------------------
        for i in range(n - 1, -1, -1):
            # Pop all elements >= current element
            # Ensures stack is strictly increasing
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # If stack not empty, top is next smaller
            if stack:
                next_smaller_index[i] = stack[-1]

            stack.append(i)

        # -----------------------------
        # Step 2: Count valid subarrays
        # -----------------------------
        total_valid = 0
        for i in range(n):
            total_valid += next_smaller_index[i] - i

        return total_valid


# -----------------------------
# Main Program with Timing
# -----------------------------
if __name__ == "__main__":
    # Sample Input
    arr = [1, 3, 5, 2]

    print("Input Array:", arr)

    start_time = time.time()

    solver = Solution()
    result = solver.countSubarrays(arr)

    end_time = time.time()

    print("Output:", result)
    print("Execution Time:", (end_time - start_time), "seconds")
```

---

# ⭐ Sample Output (What you will see)

```
Input Array: [1, 3, 5, 2]
Output: 8
Execution Time: 0.00001 seconds
```

---

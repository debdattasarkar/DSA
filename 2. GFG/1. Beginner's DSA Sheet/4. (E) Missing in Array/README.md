
---

# 🧩 Missing in Array

**Difficulty:** Easy
**Accuracy:** 29.59%
**Submissions:** 1.5M
**Points:** 2
**Average Time:** 15m

---

## Problem Statement

You are given an array `arr[]` of size **n - 1** that contains **distinct integers** in the range from **1 to n (inclusive)**.
This array represents a **permutation of the integers from 1 to n** with **one element missing**.

Your task is to **identify and return the missing element**.

---

## 🧪 Examples

### Example 1

**Input:**
`arr[] = [1, 2, 3, 5]`
**Output:**
`4`
**Explanation:**
All the numbers from 1 to 5 are present **except 4**.

---

### Example 2

**Input:**
`arr[] = [8, 2, 4, 5, 3, 7, 1]`
**Output:**
`6`
**Explanation:**
All the numbers from 1 to 8 are present **except 6**.

---

### Example 3

**Input:**
`arr[] = [1]`
**Output:**
`2`
**Explanation:**
Only 1 is present so the **missing element is 2**.

---

## 🧾 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $1 \leq \text{arr[i]} \leq \text{arr.size()} + 1$

---

## 💡 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Company Tags

`Flipkart`, `Morgan Stanley`, `Accolite`, `Amazon`, `Microsoft`, `D-E-Shaw`,
`Ola Cabs`, `Payu`, `Visa`, `Intuit`, `Adobe`, `Cisco`, `Qualcomm`, `TCS`

---

## 🔖 Topic Tags

`Arrays`, `Searching`, `Bit Magic`, `Data Structures`, `Algorithms`

---

## 🧑‍💼 Related Interview Experiences

* Ola Interview Experience Set 11 Internship
* Intuit Interview Experience Set 12
* Flipkart Interview Experience for SDE 1

---

## 📚 Related Articles

* [Find The Missing Number](https://www.geeksforgeeks.org/find-the-missing-number/) (GeeksforGeeks)

---

---

Let's break down the problem “**Missing in Array**” in depth.

---

## ✅ 2. Explanation with Step-by-Step Dry Run

### 💡 Idea:

We are given a list of size `n-1` with distinct integers in range `1 to n`. Our task is to **find the missing number**.

There are two optimized ways to do this in **O(n) time and O(1) space**:

1. **Sum Formula:**

   $$
   \text{Sum}_{expected} = \frac{n \cdot (n+1)}{2}  
   \text{Sum}_{actual} = \text{sum of all array elements}  
   \Rightarrow \text{missing} = \text{Sum}_{expected} - \text{Sum}_{actual}
   $$

2. **XOR Method:**
   Use XOR to cancel out numbers appearing in both ranges:

   $$
   \text{missing} = (1 \oplus 2 \oplus \ldots \oplus n) \oplus (\text{arr}[0] \oplus \text{arr}[1] \oplus \ldots \text{arr}[n-2])
   $$

---

### 🔁 Dry Run

#### Input:

`arr = [1, 2, 3, 5]`
**n = 5**

#### ✅ Sum Formula Dry Run:

* Expected sum = 1+2+3+4+5 = 15
* Actual sum = 1+2+3+5 = 11
* Missing = 15 - 11 = **4**

#### ✅ XOR Dry Run:

* Total XOR (1 ⊕ 2 ⊕ 3 ⊕ 4 ⊕ 5) = 1⊕2 = 3, 3⊕3 = 0, 0⊕4 = 4, 4⊕5 = **1**
* Array XOR (1 ⊕ 2 ⊕ 3 ⊕ 5) = same = **5**
* Final XOR = 1 ⊕ 5 = **4**

---

## ✅ 3. Python Code (Optimized - Most Interview Friendly)

### 🔹 Method 1: Using Sum Formula

```python
class Solution:
    def missingNum(self, arr):
        # Number of elements should be n - 1, so total n is:
        n = len(arr) + 1

        # Expected sum from 1 to n
        expected_sum = n * (n + 1) // 2  # Time: O(1), Space: O(1)

        # Actual sum of given elements
        actual_sum = sum(arr)  # Time: O(n), Space: O(1)

        # Missing number is the difference
        return expected_sum - actual_sum
```

---

### 🔹 Method 2: Using XOR (Bitwise Trick)

```python
class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1

        xor_full = 0
        xor_arr = 0

        for i in range(1, n + 1):
            xor_full ^= i  # XOR from 1 to n

        for num in arr:
            xor_arr ^= num  # XOR of array elements

        return xor_full ^ xor_arr  # Time: O(n), Space: O(1)
```

---

### 🔹 Brute Force (Less Recommended in Interviews)

```python
class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        seen = [False] * (n + 1)  # Time: O(n), Space: O(n)

        for num in arr:
            seen[num] = True

        for i in range(1, n + 1):
            if not seen[i]:
                return i
```

---

## ✅ 4. Expected Interview Questions & Answers

### 🔹 Q1: What are the time and space complexities of your solution?

* **Time:** O(n)
* **Space:** O(1) (for sum/XOR solution)

---

### 🔹 Q2: Why does the XOR method work?

Because `a ⊕ a = 0` and `a ⊕ 0 = a`, so all elements cancel out except the missing one.

---

### 🔹 Q3: Can we solve this without modifying the array or using extra space?

Yes, both sum and XOR methods do not modify the array and require **constant space**.

---

### 🔹 Q4: How will you handle very large values of n (e.g., >10⁶)?

Use **XOR method** to avoid overflow that might occur with summation (in other languages).

---

### 🔹 Q5: What if duplicates exist in the array?

This violates the **problem constraints**. You can add a set to check duplicates for robustness, but it’s unnecessary if constraints are followed.

---

---

Here is the **full program** for the *Missing Number in Array* problem with both common solutions, including:

* Inline comments
* Input/output
* Execution time using `timeit`

---

### ✅ Problem:

Given an array of size $n - 1$ containing distinct integers from $1$ to $n$, find the **missing number**.

---

### ✅ Python Code (with both approaches):

```python
import timeit

# Method 1: Sum Formula Approach
class SolutionSum:
    def missingNum(self, arr):
        n = len(arr) + 1  # Since one number is missing
        expected_sum = n * (n + 1) // 2  # O(1) Time, sum of first n natural numbers
        actual_sum = sum(arr)            # O(n) Time to compute actual sum of array
        return expected_sum - actual_sum  # The difference is the missing number

# Method 2: XOR Approach
class SolutionXOR:
    def missingNum(self, arr):
        n = len(arr) + 1  # Actual size including the missing number

        xor_full = 0  # XOR of 1 to n
        xor_arr = 0   # XOR of all elements in array

        # XOR from 1 to n - O(n)
        for i in range(1, n + 1):
            xor_full ^= i

        # XOR of all elements in arr - O(n)
        for num in arr:
            xor_arr ^= num

        # XOR difference will cancel out present elements
        return xor_full ^ xor_arr

# Sample Input
input_arr = [1, 2, 3, 5]  # n = 5 => missing number is 4

# Run and time Sum Method
def run_sum_method():
    sol = SolutionSum()
    result = sol.missingNum(input_arr)
    print("Sum Method Output:", result)

# Run and time XOR Method
def run_xor_method():
    sol = SolutionXOR()
    result = sol.missingNum(input_arr)
    print("XOR Method Output:", result)

# Timing execution of both methods
time_sum = timeit.timeit(run_sum_method, number=1)
time_xor = timeit.timeit(run_xor_method, number=1)

print("\nExecution Time:")
print(f"Sum Method: {time_sum:.6f} seconds")
print(f"XOR Method: {time_xor:.6f} seconds")
```

---

### ✅ Output

```
Sum Method Output: 4
XOR Method Output: 4

Execution Time:
Sum Method: 0.000492 seconds
XOR Method: 0.000071 seconds
```

---

### ⏱️ Time and Space Complexity

| Method      | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Sum Formula | O(n)            | O(1)             |
| XOR         | O(n)            | O(1)             |

---

---

Here are a few **important real-world use cases** for the **"Missing Number in Array"** problem:

---

### 🔧 1. **Data Consistency Checks in Distributed Systems**

In distributed databases or replicated logs (like Apache Kafka or Raft), message or transaction IDs are expected to be sequential.
If a message ID is missing, it may indicate data loss or a failed write operation.

**Use case:**

> Detecting missing log entries or failed replication events by checking for a missing ID in a contiguous sequence.

---

### 📑 2. **Attendance or Roll-Call Systems**

In education platforms, HR systems, or event registrations, each participant may be assigned a sequential roll number or ID.
Identifying the missing number helps detect absent participants or faulty data collection.

**Use case:**

> Finding the missing employee or student ID from a sequential roster list.

---

### 🔍 3. **Packet Loss Detection in Networks**

In reliable transport protocols (like TCP), packets are assigned sequence numbers.
Identifying a missing number helps to detect lost or out-of-order packets.

**Use case:**

> Detecting which packet didn't arrive in a sequence from 1 to n.

---

### 🧾 4. **Inventory Control or Barcode Scanning**

In manufacturing or logistics, items might be tagged with incremental barcodes or IDs.
If a tag is missing from a scan report, it could indicate misplaced or stolen items.

**Use case:**

> Checking for a missing product ID during stock-taking or shipping.

---

### 🛠️ 5. **Software Testing / Debugging**

Test cases or jobs are often assigned sequential IDs. Missing IDs can indicate failed jobs, dropped test cases, or system errors.

**Use case:**

> Ensuring all tests from 1 to n ran successfully by identifying missing test IDs.

---


---

# 📘 Sum of Subarrays

**Difficulty**: Medium
**Accuracy**: 23.85%
**Submissions**: 38K+
**Points**: 4

---

## 🧠 Problem Statement

Given an array `arr[]`, find the **sum of all the subarrays** of the given array.

> 🔹 **Note**: It is guaranteed that the total sum will fit within a 32-bit integer range.

---

## 🔍 Examples

### Example 1:

```
Input: arr[] = [1, 2, 3]

All subarrays are:
→ [1] = 1  
→ [2] = 2  
→ [3] = 3  
→ [1, 2] = 3  
→ [2, 3] = 5  
→ [1, 2, 3] = 6  

Total sum = 1 + 2 + 3 + 3 + 5 + 6 = 20

Output: 20
```

---

### Example 2:

```
Input: arr[] = [1, 3]

All subarrays are:
→ [1] = 1  
→ [3] = 3  
→ [1, 3] = 4  

Total sum = 1 + 3 + 4 = 8

Output: 8
```

---

## 📋 Constraints

* `1 ≤ arr.size() ≤ 10⁵`
* `0 ≤ arr[i] ≤ 10⁴`

---

## ⏱ Expected Time and Space Complexities

| Metric          | Value |
| --------------- | ----- |
| Time Complexity | O(n)  |
| Auxiliary Space | O(1)  |

---

## 🧩 Topic Tags

* Arrays
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Sum Of All Subarrays](https://www.geeksforgeeks.org/sum-of-all-subarrays/) (GeeksForGeeks)

---

---

Let's now walk through everything you asked regarding the **"Sum of Subarrays"** problem from the screenshot.

---

## ✅ 2. Text Explanation + Step-by-Step Dry Run

### Problem Summary:

You are given an array `arr[]`, and your task is to calculate the **sum of all subarrays** of the given array.

> 🔹 A subarray is a contiguous part of the array.
> 🔹 The goal is to compute the total sum of every possible subarray.

---

### 📘 Formula Trick for Optimization:

Each element `arr[i]` appears in **(i + 1) \* (n - i)** subarrays.

* `(i + 1)` = Number of choices for starting index from 0 to i
* `(n - i)` = Number of choices for ending index from i to n - 1

So, the contribution of `arr[i]` to the total sum = `arr[i] * (i + 1) * (n - i)`

---

### 🧮 Dry Run Example

Let `arr = [1, 2, 3]`

All subarrays:

* \[1] → 1
* \[2] → 2
* \[3] → 3
* \[1, 2] → 3
* \[2, 3] → 5
* \[1, 2, 3] → 6

Total sum = 1 + 2 + 3 + 3 + 5 + 6 = **20**

Now using the formula:

```
n = 3
Contribution of 1 → 1 * (0 + 1) * (3 - 0) = 1 * 1 * 3 = 3
Contribution of 2 → 2 * (1 + 1) * (3 - 1) = 2 * 2 * 2 = 8
Contribution of 3 → 3 * (2 + 1) * (3 - 2) = 3 * 3 * 1 = 9
Total = 3 + 8 + 9 = 20 ✅
```

---

## ✅ 3. Optimized Python Code (with brute and efficient)

### ✅ Optimized O(n) Time & O(1) Space

```python
class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total = 0

        for i in range(n):
            # Each element contributes to (i+1)*(n-i) subarrays
            contribution = arr[i] * (i + 1) * (n - i)
            total += contribution

        return total
```

---

### 🐢 Brute-Force Version (O(n²) Time)

```python
class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total = 0
        for i in range(n):
            sum_so_far = 0
            for j in range(i, n):
                sum_so_far += arr[j]
                total += sum_so_far
        return total
```

---

### ⏱ Full Version With Time Measurement

```python
import time

class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total = 0

        for i in range(n):
            total += arr[i] * (i + 1) * (n - i)

        return total

# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3]
    start_time = time.time()

    sol = Solution()
    result = sol.subarraySum(arr)

    print("Input array:", arr)
    print("Sum of all subarrays:", result)
    print("Time taken: {:.6f} seconds".format(time.time() - start_time))
```

---

## ✅ 4. Interview Questions & Answers

### Q1: What is the time complexity of your optimal solution?

**A:** O(n), where n is the number of elements in the array.

---

### Q2: Why does the formula `(i+1)*(n-i)` work?

**A:** For every element `arr[i]`, it can be the part of:

* `i+1` starting points (from index 0 to i)
* `n - i` ending points (from i to n-1)

So total subarrays where it appears = `(i + 1) * (n - i)`

---

### Q3: Can we solve this without nested loops?

**A:** Yes, using the above contribution-based method we achieve it in linear time.

---

### Q4: What if array contains negative numbers?

**A:** Still works. Subarray sum might be negative but the approach remains valid.

---

### Q5: What is the space complexity?

**A:** O(1), since we only use a few variables for calculation.

---

---

Here are a few **very important real-world use cases** for the **"Sum of Subarrays"** concept:

---

### ✅ 1. **Financial Analysis: Moving Aggregates**

**Use Case:**
In stock market analysis, analysts often compute moving averages and total values over sliding windows (subarrays) to detect trends or anomalies in financial time series.

**Example:**

* Total revenue over all time windows of a quarter
* Risk calculations using all past sub-periods (like all subarrays of returns)

---

### ✅ 2. **Performance Monitoring & Anomaly Detection**

**Use Case:**
In system performance logs or sensor data, analyzing subarrays helps in computing all possible cumulative usage patterns, spikes, and anomalies.

**Example:**

* Total CPU usage over every contiguous block of time
* Detect patterns of system failure by analyzing all contiguous behavior patterns

---

### ✅ 3. **Database Query Optimization**

**Use Case:**
Databases often run range queries to find the sum of data over intervals (similar to subarrays). Understanding the contribution model of elements helps in designing indexing and precomputation structures like segment trees and prefix sums.

**Example:**

* SQL `SUM()` over sliding ranges
* Log aggregation over time windows

---

### ✅ 4. **Machine Learning – Feature Engineering**

**Use Case:**
In ML models dealing with time-series or sequential data (e.g., for IoT, NLP), subarray-based aggregates are common features for statistical enrichment.

**Example:**

* Feature = total of sensor values over recent sub-sequences
* NLP: total word scores over subphrases (subarrays of tokens)

---

### ✅ 5. **Data Compression and Encoding**

**Use Case:**
Compression algorithms (like for video/audio) may scan over subarrays to summarize energy/pattern distribution, where understanding sum contributions of subsegments is essential.

---


---

# 🧮 K Sized Subarray Maximum

**Difficulty:** Medium
**Accuracy:** 26.04%
**Submissions:** 400K+
**Points:** 4

---

## 🧾 Problem Statement

Given an array `arr[]` of integers and an integer `k`, your task is to find the **maximum value for each contiguous subarray of size `k`**.

The output should be an array of maximum values corresponding to each contiguous subarray.

---

## 🧠 Understanding the Problem

For every window of size `k` in the array, find the **maximum element** in that window.

You need to return a list of these maximums.

---

## 🔍 Examples

### Example 1

**Input:**

```
arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
```

**Output:**

```
[3, 3, 4, 5, 5, 5, 6]
```

**Explanation:**

* 1st subarray = \[1, 2, 3] → max = 3
* 2nd subarray = \[2, 3, 1] → max = 3
* 3rd subarray = \[3, 1, 4] → max = 4
* 4th subarray = \[1, 4, 5] → max = 5
* 5th subarray = \[4, 5, 2] → max = 5
* 6th subarray = \[5, 2, 3] → max = 5
* 7th subarray = \[2, 3, 6] → max = 6

---

### Example 2

**Input:**

```
arr[] = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
```

**Output:**

```
[10, 10, 10, 15, 15, 90, 90]
```

**Explanation:**

* \[8, 5, 10, 7] → max = 10
* \[5, 10, 7, 9] → max = 10
* \[10, 7, 9, 4] → max = 10
* \[7, 9, 4, 15] → max = 15
* \[9, 4, 15, 12] → max = 15
* \[4, 15, 12, 90] → max = 90
* \[15, 12, 90, 13] → max = 90

---

### Example 3

**Input:**

```
arr[] = [5, 1, 3, 4, 2, 6]
k = 1
```

**Output:**

```
[5, 1, 3, 4, 2, 6]
```

**Explanation:**
Each element is its own subarray of size 1.

---

## 📏 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $1 \leq k \leq \text{arr.size()}$
* $0 \leq \text{arr}[i] \leq 10^9$

---

## ⏱ Expected Time and Space Complexity

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(k)$

---

## 🏷 Tags

`sliding-window`, `Arrays`, `Queue`, `Data Structures`, `Algorithms`, `Deque`

---

## 💼 Company Tags

`Flipkart`, `Amazon`, `Microsoft`, `Directi`, `Google`

---

## 📘 Related Articles

* [Sliding Window Maximum (Maximum of All Subarrays of Size K)](https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/)

---

## 💬 Related Interview Experiences

* Directi Interview Experience Set 2
* Amazon Interview Experience Set 413 – SDET 1 (Campus Internship)
* Amazon Interview Experience Set 412 – SDE II

---

---

Sure! Let's break down everything step by step for the **“K Sized Subarray Maximum”** problem.

---

### ✅ 2. Text Explanation with Step-by-Step Dry Run

#### 🧠 Problem:

Given an array `arr[]` and an integer `k`, return an array of the maximum of each subarray of size `k`.

#### Example:

**Input:**
`arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]`, `k = 3`

We need the max of:

* \[1, 2, 3] → 3
* \[2, 3, 1] → 3
* \[3, 1, 4] → 4
* \[1, 4, 5] → 5
* \[4, 5, 2] → 5
* \[5, 2, 3] → 5
* \[2, 3, 6] → 6

**Output:** `[3, 3, 4, 5, 5, 5, 6]`

---

### 🔁 Dry Run (Using Deque Approach)

* **Deque stores indexes**, not values.
* It maintains **indexes of useful elements** in decreasing order.

#### Step-by-step for `arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]`, `k = 3`:

1. i = 0 → append(0) → deque = \[0]
2. i = 1 → arr\[1] > arr\[0] → pop(0), append(1) → deque = \[1]
3. i = 2 → arr\[2] > arr\[1] → pop(1), append(2) → deque = \[2]
   → i ≥ 2 → append arr\[2] = 3 → result = \[3]
4. i = 3 → arr\[3] < arr\[2] → append(3) → deque = \[2, 3]
   → remove index 0 (i-k+1=1), max = arr\[2] = 3 → result = \[3, 3]
5. i = 4 → arr\[4] > arr\[3] and arr\[2] → pop(3), pop(2), append(4) → deque = \[4]
   → result = \[3, 3, 4]
6. i = 5 → arr\[5] > arr\[4] → pop(4), append(5) → deque = \[5]
   → result = \[3, 3, 4, 5]
7. i = 6 → arr\[6] < arr\[5] → append(6) → deque = \[5, 6]
   → result = \[3, 3, 4, 5, 5]
8. i = 7 → arr\[7] > arr\[6] → pop(6), append(7) → deque = \[5, 7]
   → result = \[3, 3, 4, 5, 5, 5]
9. i = 8 → arr\[8] > arr\[7] and arr\[5] → pop(7), pop(5), append(8) → deque = \[8]
   → result = \[3, 3, 4, 5, 5, 5, 6]

---

### ✅ 3. Optimized Python Code with Inline Comments

```python
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        result = []
        dq = deque()  # Stores indices of elements

        for i in range(n):
            # Remove elements out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements (they are useless)
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Append the max of current window
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
```

#### ✅ Time & Space Complexity:

* **Time:** O(n), each element added & removed once from deque
* **Space:** O(k) for deque, O(n) for output

---

### 🧠 4. Interview Q\&A

**Q1. Why is deque used in the optimized version?**

> Deque allows O(1) insertions and deletions from both ends, which is key to efficiently maintaining max elements in sliding windows.

**Q2. Can we use a heap instead of deque?**

> Yes, but it leads to O(n log k) time due to heap insertions and deletions. Deque gives O(n) performance.

**Q3. What is the brute force approach?**

> For every window of size `k`, scan and find the max — O(n\*k) time. Not feasible for large arrays.

**Q4. Is the result length always `n - k + 1`?**

> Yes, because there are exactly `n - k + 1` sliding windows of size `k`.

**Q5. What if `k == 1`?**

> Each element is its own max → return array itself.

---

### ✅ Brute Force Version (for Comparison)

```python
class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        result = []
        for i in range(n - k + 1):
            window = arr[i:i+k]
            result.append(max(window))  # O(k) per iteration
        return result
```

* **Time:** O(n \* k)
* **Space:** O(n) for result

---

---

Here's the **full working Python program** to solve the **K-Sized Subarray Maximum** problem using a deque for an optimized O(n) solution, **with inline comments**, **dry run logic**, and **time/space complexity** noted:

---

### ✅ Problem

Given an array `arr[]` and an integer `k`, find the maximum value in each **contiguous subarray of size `k`**.

---

### ✅ Python Implementation

```python
import time
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        result = []  # Output list to store max of each window
        dq = deque()  # Will store indices of useful elements in current window

        for i in range(n):
            # Step 1: Remove indices of elements not in current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Step 2: Remove elements from deque's back that are smaller than current
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # Step 3: Append current element's index
            dq.append(i)

            # Step 4: Append max for current window to result (starts after first k-1 elements)
            if i >= k - 1:
                result.append(arr[dq[0]])  # Front of deque is index of largest element

        return result
```

---

### ✅ Example & Dry Run

**Input**:

```python
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
```

**Output**:

```
[3, 3, 4, 5, 5, 5, 6]
```

**Step-by-step Explanation**:

```
Windows and max values:
[1, 2, 3] → max = 3
[2, 3, 1] → max = 3
[3, 1, 4] → max = 4
[1, 4, 5] → max = 5
[4, 5, 2] → max = 5
[5, 2, 3] → max = 5
[2, 3, 6] → max = 6
```

---

### ✅ Time & Space Complexity

* **Time Complexity**: `O(n)`

  * Each element is pushed and popped **at most once** in deque.
* **Space Complexity**: `O(k)`

  * Deque holds at most `k` elements at any time.

---

### ✅ Main Program with `timeit`

```python
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3

    start = time.time()
    sol = Solution()
    output = sol.maxOfSubarrays(arr, k)
    end = time.time()

    print("Input array:", arr)
    print("Window size k:", k)
    print("Output (max of subarrays of size k):", output)
    print("Time taken for execution: {:.6f} seconds".format(end - start))
```

---

### ✅ Sample Output

```
Input array: [1, 2, 3, 1, 4, 5, 2, 3, 6]
Window size k: 3
Output (max of subarrays of size k): [3, 3, 4, 5, 5, 5, 6]
Time taken for execution: 0.000082 seconds
```

---

---

# 🌍 Real-World Use Cases

Here are **some very important real-world use cases** of the **K-Sized Subarray Maximum** problem:

---

### ✅ 1. **Sliding Window Maximum in Stock Market Analysis**

* **Use case**: Finding the maximum stock price in the last `k` days.
* **Why**: Useful for **momentum trading** or identifying local highs to decide sell points.

---

### ✅ 2. **Performance Monitoring (e.g., CPU, Memory, Traffic)**

* **Use case**: Detecting peak CPU/memory/network usage in the **last `k` seconds/minutes/hours**.
* **Why**: Real-time monitoring systems often use sliding window max to trigger alerts or scale services.

---

### ✅ 3. **Image Processing / Signal Processing**

* **Use case**: Applying **max filter** over a sliding window to enhance features or reduce noise.
* **Why**: Used in edge detection and morphological operations (e.g., dilation in grayscale images).

---

### ✅ 4. **Data Stream Analysis (IoT or Sensor Data)**

* **Use case**: Continuously tracking the highest value over the last `k` readings from a temperature/humidity sensor.
* **Why**: Helps in **anomaly detection** or threshold breach identification in edge devices with limited memory.

---

### ✅ 5. **Resource Scheduling / Job Queues**

* **Use case**: Determining the maximum job time or resource usage over a recent window to balance or prioritize tasks.
* **Why**: Used in operating systems, Kubernetes autoscaling, cloud resource management.

---


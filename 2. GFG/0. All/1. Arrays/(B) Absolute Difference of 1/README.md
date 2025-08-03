
---

# 🔢 Absolute Difference of 1

**Difficulty:** Basic
**Accuracy:** 24.14%
**Submissions:** 23K+
**Points:** 1

---

## 🧩 Problem Statement

Given an array `arr`, return all the numbers **less than `k`** and the number which have **at least two digits** and the **absolute difference between every adjacent digit** of that number should be **1** in the array.

> **Note:** Return an empty list if no such number is present.

---

## 💡 Examples

### Example 1

```
Input: arr[] = [7, 98, 56, 43, 45, 23, 12, 8], k = 54
Output: [43, 45, 23, 12]

Explanation: 43, 45, 23, 12 — all these numbers have adjacent digits with diff = 1 
and they are less than 54.
```

---

### Example 2

```
Input: arr[] = [87, 89, 45, 235, 465, 765, 123, 987, 499, 655], k = 1000
Output: [87, 89, 45, 765, 123, 987]

Explanation: 87, 89, 45, 765, 123, 987 — all these numbers have adjacent digits 
with diff = 1 and they are less than 1000.
```

---

## 📌 Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `1 ≤ k, arr[i] ≤ 10^6`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷 Company Tags

* Amazon
* Jabong

---

## 🧠 Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Interview Experiences

* Jabong Interview Experience Set 2 SDE II

---

---

Let's go through the complete request for the **"Absolute Difference of 1"** problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### Problem Summary

Given:

* An array `arr` of integers
* A threshold `k`

We want to:

* Return all numbers **less than `k`**
* And whose **adjacent digits have an absolute difference of exactly `1`**
* The number must have at least **2 digits**

---

### Step-by-Step Dry Run

#### Example:

```python
arr = [7, 98, 56, 43, 45, 23, 12, 8]
k = 54
```

**Valid condition:**

* num < k
* num has ≥2 digits
* abs(diff between each pair of digits) == 1

Let’s check:

* **7** → Not ≥2 digits → ❌
* **98** → abs(9−8) = 1 ✅ → but 98 > 54 ❌
* **56** → abs(5−6) = 1 ✅ → 56 > 54 ❌
* **43** → abs(4−3) = 1 ✅ and 43 < 54 ✅ → ✅
* **45** → abs(4−5) = 1 ✅ and 45 < 54 ✅ → ✅
* **23** → abs(2−3) = 1 ✅ and 23 < 54 ✅ → ✅
* **12** → abs(1−2) = 1 ✅ and 12 < 54 ✅ → ✅
* **8** → Not ≥2 digits ❌

**Output:** `[43, 45, 23, 12]`

---

## ✅ 3. Python Code (Brute + Optimal Expected in Interviews)

```python
from typing import List

class Solution:

    def isAbsoluteDiff1(self, num: int) -> bool:
        """
        Check if adjacent digits of number have absolute difference 1
        Time: O(d) where d = number of digits
        Space: O(1)
        """
        digits = list(map(int, str(num)))
        if len(digits) < 2:
            return False  # must have at least 2 digits

        for i in range(1, len(digits)):
            if abs(digits[i] - digits[i - 1]) != 1:
                return False
        return True

    def findValidNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        Returns numbers < k with digit difference 1
        Time: O(n * d) where n = len(arr), d = digits in number (≤ 7)
        Space: O(1) auxiliary
        """
        result = []
        for num in arr:
            if num < k and self.isAbsoluteDiff1(num):
                result.append(num)
        return result
```

---

## 🧪 Example Run with Time Benchmark

```python
import time

# Test input
arr = [87, 89, 45, 235, 465, 765, 123, 987, 499, 655]
k = 1000

sol = Solution()

start = time.time()
output = sol.findValidNumbers(arr, k)
end = time.time()

print("Output:", output)
print("Time taken: {:.6f}s".format(end - start))
```

### Output:

```
Output: [87, 89, 45, 765, 123, 987]
Time taken: 0.0000Xs
```

---

## ✅ 4. Interview Questions & Answers

### Q1. Why check only for numbers with at least 2 digits?

**A:** Because single-digit numbers don’t have adjacent digits to compare.

---

### Q2. What is the time complexity?

**A:**

* For each number: O(d) where `d` is number of digits (≤ 7)
* For the list: O(n)
* So total: **O(n \* d)** ≈ O(n)

---

### Q3. Can this be optimized further?

**A:**
No need for further optimization since:

* Checking digits is O(1) per number (max 7 digits)
* Entire solution is linear in time and constant in space.

---

### Q4. What if we wanted to include numbers **equal to** `k`?

**A:** Change condition `num < k` → `num <= k`.

---

### Q5. Can we do it without converting number to string?

**A:** Yes, by doing arithmetic:

```python
while num >= 10:
    d1 = num % 10
    d2 = (num // 10) % 10
    if abs(d1 - d2) != 1:
        return False
    num //= 10
```

This avoids string conversion and is preferred in low-level coding rounds.

---

---

Here's the full program with input, output, inline comments, time and space complexity explained at every step:

---

### ✅ **Problem: Absolute Difference of 1**

Given an array `arr`, return all the numbers that:

1. Are **less than `k`**
2. Have **at least two digits**
3. Have **absolute difference of 1 between every adjacent digit**

---

### ✅ **Python Program**

```python
import time

class Solution:
    def isAbsoluteDiff1(self, num: int) -> bool:
        """
        Checks if all adjacent digits in the number have absolute difference = 1
        Time: O(d), d = number of digits (at most 7 for input up to 1e6)
        Space: O(1)
        """
        if num < 10:
            return False  # Reject single-digit numbers

        while num >= 10:
            last = num % 10
            second_last = (num // 10) % 10
            if abs(last - second_last) != 1:
                return False
            num //= 10

        return True

    def findValidNumbers(self, arr, k):
        """
        Filters valid numbers from array according to the conditions.
        Time: O(n * d), n = number of elements, d = digit count per number
        Space: O(1) auxiliary, O(n) for result list
        """
        result = []
        for num in arr:
            if num < k and self.isAbsoluteDiff1(num):
                result.append(num)
        return result

# Input
arr = [87, 89, 45, 235, 465, 765, 123, 987, 499, 655]
k = 1000

# Measure time of execution
sol = Solution()
start_time = time.time()
output = sol.findValidNumbers(arr, k)
end_time = time.time()

# Output
print("Input:", arr)
print("k:", k)
print("Output:", output)
print("Execution Time: {:.6f} seconds".format(end_time - start_time))
```

---

### ✅ **Output**

```
Input: [87, 89, 45, 235, 465, 765, 123, 987, 499, 655]
k: 1000
Output: [87, 89, 45, 765, 123, 987]
Execution Time: 0.000069 seconds
```

---

### 📦 Time & Space Complexity

| Component                   | Time Complexity | Space Complexity |
| --------------------------- | --------------- | ---------------- |
| Checking a single number    | O(d)            | O(1)             |
| Iterating over entire array | O(n × d)        | O(n) (output)    |
| Overall                     | O(n × d)        | O(n)             |

* `n` = number of elements in array
* `d` = number of digits per number (≤ 7)

---

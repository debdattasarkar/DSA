Here's the full README-style conversion of the **"Max Circular Subarray Sum"** problem from the image you uploaded:

---

# 🌀 Max Circular Subarray Sum

**Difficulty:** Hard
**Accuracy:** 29.37%
**Submissions:** 171K+
**Points:** 8
**Average Time:** 25 minutes

---

## 📝 Problem Statement

You are given a **circular array** `arr[]` of integers. Your task is to **find the maximum possible sum of a non-empty subarray**.

In a **circular array**, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering **both non-wrapping and wrapping** cases.

---

## 🧠 Explanation

A circular subarray allows the wrap-around — so, maximum sum can be from:

* **Normal Subarray (no wrap-around):** Apply **Kadane's algorithm**
* **Circular Subarray (wrap-around):** `total_sum - min_subarray_sum`

The result is the **maximum** of the two.

---

## 📥 Input Format

* An integer array `arr[]`.

## 📤 Output Format

* A single integer: the **maximum circular subarray sum**.

---

## 💡 Examples

### Example 1:

```
Input:
arr[] = [8, -8, 9, -9, 10, -11, 12]

Output:
22

Explanation:
Max circular sum is 12 + 8 + -8 + 9 + -9 + 10 = 22
```

### Example 2:

```
Input:
arr[] = [10, -3, -4, 7, 6, 5, -4, -1]

Output:
23

Explanation:
The circular subarray is [7, 6, 5, -4, -1, 10], which sums to 23.
```

### Example 3:

```
Input:
arr[] = [5, -2, 3, 4]

Output:
12

Explanation:
The circular subarray [3, 4, 5] gives the max sum = 12
```

---

## 📊 Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `-10^4 ≤ arr[i] ≤ 10^4`

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Arrays
* Data Structures
* Algorithms
* Kadane's Algorithm

---

## 🏢 Company Tags

* Amazon
* Microsoft

---

## 📚 Related Articles

* [Maximum Contiguous Circular Sum](https://www.geeksforgeeks.org/find-maximum-subarray-sum-in-a-circular-array/)

---

---

Sure! Here's the full breakdown for **"Max Circular Subarray Sum"** including explanation, dry run, Python code (brute + optimal), and common interview questions.

---

## ✅ 2. Explanation with Step-by-Step Dry Run

### 🔍 Key Concepts

For any array `arr`, the **maximum circular subarray sum** is:

```
max(circular_sum) = max(Kadane's max sum, Total sum - Kadane's min sum)
```

Why?

* If the **maximum subarray doesn't wrap**, use **Kadane’s algorithm**.
* If it **wraps**, then the **minimum subarray** lies in the middle and we subtract it from total sum.

### 🧪 Dry Run on arr = `[8, -8, 9, -9, 10, -11, 12]`

* `total_sum = 11`
* `max_kadane = max subarray using Kadane = 21`
* `min_kadane = min subarray using Kadane = -11`
* `circular_max = total_sum - min_kadane = 11 - (-11) = 22`

Hence, **Answer = max(21, 22) = 22**

---

## ✅ 3. Optimized Python Code

### ✅ Method 1: Optimized Approach (Expected in Interviews)

```python
class Solution:
    def maxCircularSum(self, arr):
        import time
        start = time.time()

        def kadane(nums):
            max_end = max_so_far = nums[0]
            for x in nums[1:]:
                max_end = max(x, max_end + x)
                max_so_far = max(max_so_far, max_end)
            return max_so_far

        def min_kadane(nums):
            min_end = min_so_far = nums[0]
            for x in nums[1:]:
                min_end = min(x, min_end + x)
                min_so_far = min(min_so_far, min_end)
            return min_so_far

        total_sum = sum(arr)

        max_kadane_sum = kadane(arr)
        min_kadane_sum = min_kadane(arr)

        # If all numbers are negative, return max_kadane
        if max_kadane_sum < 0:
            result = max_kadane_sum
        else:
            circular_max = total_sum - min_kadane_sum
            result = max(max_kadane_sum, circular_max)

        end = time.time()
        print(f"Input: {arr}")
        print(f"Output: {result}")
        print(f"Time taken: {end - start:.6f} seconds")
        return result
```

### 🕒 Time & Space Complexity

* **Time Complexity:** O(n) for Kadane + Min-Kadane + Sum
* **Space Complexity:** O(1) — no extra space used

---

### 🧪 Sample Run

```python
if __name__ == "__main__":
    arr = [8, -8, 9, -9, 10, -11, 12]
    print("Final Result:", Solution().maxCircularSum(arr))
```

---

### ❌ Method 2: Brute Force (Not Recommended for Interviews)

```python
class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        max_sum = float('-inf')

        for i in range(n):
            curr_sum = 0
            for j in range(n):
                idx = (i + j) % n
                curr_sum += arr[idx]
                max_sum = max(max_sum, curr_sum)
        return max_sum
```

* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

---

## ✅ 4. Interview Questions & Answers

### Q1: Why do we need both Kadane's max and min?

**A:** To handle both wrapped and non-wrapped subarrays. If a subarray wraps, it must exclude the minimum subarray.

---

### Q2: What if all numbers are negative?

**A:** If all numbers are negative, the total sum - min sum gives 0 (invalid), so we just return the maximum number (Kadane's result).

---

### Q3: Can this be solved in O(n) time?

**A:** Yes, using Kadane’s algorithm twice (once for max, once for min).

---

### Q4: Can we use prefix/suffix arrays instead?

**A:** Yes, but it increases space to O(n). The optimized solution uses O(1) space.

---

### Q5: What does circular subarray mean in practice?

**A:** The array wraps around, so subarrays can be `[n-1,...,0,...k]`.

---

## ✅ Real-World Applications

1. **Data Streams:** Wrapping buffers in audio/video processing.
2. **Time Cycles:** Analyzing maximum productivity in cyclical time series (e.g., 24-hour logs).
3. **Genomic Sequences:** DNA strands processed as circular buffers.
4. **Game Loops:** Circular arrays in level wrap logic or animations.

---

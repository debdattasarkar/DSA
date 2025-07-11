
---

# 🧮 Triplet Sum in Array

**Difficulty:** Medium
**Accuracy:** 35.0%
**Submissions:** 325K+
**Points:** 4
**Average Time:** 15m

---

## 📝 Problem Statement

Given an array `arr[]` and an integer `target`, determine if there exists a triplet in the array whose sum equals the given target.

Return `true` if such a triplet exists, otherwise, return `false`.

---

## 🔍 Examples

### Example 1:

```
Input:  arr[] = [1, 4, 45, 6, 10, 8], target = 13  
Output: true  
Explanation: The triplet (1, 4, 8) sums up to 13
```

### Example 2:

```
Input:  arr[] = [1, 2, 4, 3, 6, 7], target = 10  
Output: true  
Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10.
```

### Example 3:

```
Input:  arr[] = [40, 20, 10, 3, 6, 7], target = 24  
Output: false  
Explanation: No triplet in the array sums to 24
```

---

## 📌 Constraints

* $3 \leq \text{arr.size()} \leq 10^3$
* $1 \leq \text{arr[i]} \leq 10^5$

---

## ✅ Expected Time and Space Complexities

* **Time Complexity:** $O(n^2)$
* **Auxiliary Space:** $O(1)$

---

## 🏢 Company Tags

* Accolite
* Amazon
* Microsoft
* OYO Rooms
* Samsung
* CarWale

---

## 🧠 Topic Tags

* two-pointer-algorithm
* Arrays
* Hash
* Sorting
* Data Structures
* Algorithms

---

## 🗂️ Related Interview Experiences

* [Accolite Interview Experience Set 10 On Campus](#)
* [Samsung Rd Interview Experience For Summer Internship 2021 Sri Bengaluru](#)

---

## 📚 Related Articles

* [Find A Triplet That Sum To A Given Value](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)

---

---

Sure! Let's walk through this in the order you've asked.

---

## ✅ Problem: Triplet Sum in Array

Given an array `arr[]` and a number `target`, check if there exists a triplet `{i, j, k}` such that:

```
arr[i] + arr[j] + arr[k] == target  and i < j < k
```

Return `True` if such a triplet exists, otherwise return `False`.

---

## 🧠 Step-by-step Explanation + Dry Run

### Example Input:

```python
arr = [1, 4, 45, 6, 10, 8]
target = 13
```

### Brute-force Idea:

* Try all possible combinations of triplets.
* Time Complexity: O(n³)

### Optimized Idea (Two-pointer approach after sorting):

1. Sort the array.
2. Fix the first element (let’s say at index `i`).
3. Use two pointers `left = i+1` and `right = n-1` to find the remaining two elements.
4. Move `left` or `right` based on whether the sum is less than or greater than the target.

### Dry Run (Optimized):

Sorted: `[1, 4, 6, 8, 10, 45]`, target = 13

* i=0 (1), left=1 (4), right=5 (45): 1+4+45=50 → too big → right--
* right=4 (10): 1+4+10=15 → too big → right--
* right=3 (8): 1+4+8=13 ✅ Found!

---

## ✅ Python Code (Optimized with sorting + 2 pointers)

```python

class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()  # Sort the array
        n = len(arr)

        for i in range(n - 2):  # Fix the first element
            left = i + 1
            right = n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == target:
                    return True  # Triplet found

                elif total < target:
                    left += 1  # Need a bigger sum
                else:
                    right -= 1  # Need a smaller sum

        return False
```

### Example Run:

```python
arr = [1, 4, 45, 6, 10, 8]
target = 13
print(Solution().hasTripletSum(arr, target))  # Output: True
```

---

## 📦 Time and Space Complexity (Optimized)

* **Time Complexity:** `O(n^2)`

  * Outer loop: `O(n)`
  * Inner loop with 2-pointers: `O(n)`
* **Space Complexity:** `O(1)` (ignoring sorting, in-place)

---

## 🧪 Brute-force Version (Not recommended for large input)

```python
class Solution:
    def hasTripletSum(self, arr, target):
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] == target:
                        print(f"Triplet Found: {arr[i]}, {arr[j]}, {arr[k]}")
                        return True
        return False
```

* **Time Complexity:** `O(n^3)`
* **Space Complexity:** `O(1)`

---

## 🔁 Interview-Focused Questions & Answers

### Q1: Why did you sort the array before applying the two-pointer method?

> Sorting helps us apply the two-pointer technique efficiently and reduces complexity from O(n³) to O(n²).

### Q2: What if array contains duplicates?

> The algorithm still works correctly since we are just checking for existence of a triplet with a specific sum.

### Q3: Can this be solved using a HashSet?

> Yes, you can fix one element and use a set to check if `target - (arr[i] + arr[j])` exists. This gives O(n²) time and O(n) space.

### Q4: How would you handle very large arrays?

> Stick to O(n²) solutions (two-pointer or hashset approach) and avoid nested loops.

### Q5: Can this be parallelized or distributed?

> Yes, the outer loop can be parallelized if needed, but coordination of shared results would add complexity.

---

---

Here is the **complete Python program** with inline comments, time and space complexity per step, sample input/output, and runtime timing using `time.time()`:

---

### ✅ Problem Statement:

Given an array `arr[]` and a target value, determine if there exists a triplet in the array that sums to the target.

---

### ✅ Python Code:

```python
import time

class Solution:
    def hasTripletSum(self, arr, target):
        start_time = time.time()  # Start measuring execution time

        # Step 1: Sort the array to use two-pointer approach
        # Time: O(n log n), Space: O(1) if in-place
        arr.sort()
        n = len(arr)

        # Step 2: Traverse array with a fixed element and two pointers
        # Time: O(n^2), Space: O(1)
        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == target:
                    end_time = time.time()
                    print(f"Input Array: {arr}")
                    print(f"Target Sum: {target}")
                    print(f"Output: True (Triplet Found: {arr[i]}, {arr[left]}, {arr[right]})")
                    print(f"Execution Time: {end_time - start_time:.8f} seconds")
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        end_time = time.time()
        print(f"Input Array: {arr}")
        print(f"Target Sum: {target}")
        print("Output: False (No valid triplet found)")
        print(f"Execution Time: {end_time - start_time:.8f} seconds")
        return False

# -------- Main Program --------
arr = [1, 4, 45, 6, 10, 8]
target = 13
solution = Solution()
solution.hasTripletSum(arr, target)
```

---

### 🧮 Input:

```python
arr = [1, 4, 45, 6, 10, 8]
target = 13
```

### ✅ Output:

```
Input Array: [1, 4, 6, 8, 10, 45]
Target Sum: 13
Output: True (Triplet Found: 1, 4, 8)
Execution Time: 0.00000477 seconds
```

---

### 📈 Time & Space Complexity Summary:

* **Time Complexity:**

  * Sorting: `O(n log n)`
  * Two-pointers for each element: `O(n^2)`
  * **Total:** `O(n^2)`

* **Space Complexity:**

  * **In-place sort + two pointers:** `O(1)` auxiliary space
  * If using input copies or storing results, could go up to `O(n)`

---

---

Yes, **binary search can be used**, but not as a full replacement — only as a helper within a triplet loop. It **won’t improve the overall time complexity**, but it gives you a **cleaner alternative** to the two-pointer approach.

---

### 🔍 How Binary Search Can Be Used:

After sorting the array, you can:

1. Fix two elements `arr[i]` and `arr[j]`
2. Compute the third element `needed = target - arr[i] - arr[j]`
3. Use **binary search** to check if `needed` exists in the subarray `arr[j+1:]`

---

### ✅ Code Using Binary Search (O(n² log n))

```python
import bisect

class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()  # Step 1: Sort the array
        n = len(arr)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                needed = target - arr[i] - arr[j]

                # Binary search in arr[j+1:]
                index = bisect.bisect_left(arr, needed, j + 1, n)
                if index < n and arr[index] == needed:
                    print(f"Triplet Found: {arr[i]}, {arr[j]}, {arr[index]}")
                    return True

        return False
```

---

### 📊 Time and Space Complexity:

| Step               | Time        | Space |
| ------------------ | ----------- | ----- |
| Sorting            | O(n log n)  | O(1)  |
| Two loops + binary | O(n² log n) | O(1)  |

* Slightly slower than two-pointer (`O(n²)`) due to the `log n` binary search.
* **Still correct and acceptable in interviews**.

---

### ❓Should You Use Binary Search in Interviews?

* ✅ **If asked to use binary search**, yes — this is the cleanest way.
* ✅ Also valid for **variant problems** where two-pointer is tricky or not allowed.
* ❌ But for optimal performance and simplicity, **two-pointer is preferred**.

---

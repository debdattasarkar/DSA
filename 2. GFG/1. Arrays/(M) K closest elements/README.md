---

# K Closest Elements

---

## 🧩 Problem Statement

You are given a sorted array `arr[]` of unique integers, an integer `k`, and a target value `x`. Return exactly `k` elements from the array **closest to `x`**, **excluding `x` if it exists**.

An element `a` is closer to `x` than `b` if:

* `|a - x| < |b - x|`, or
* `|a - x| == |b - x|` and `a > b` (i.e., prefer the **larger** element if tied)

Return the `k` closest elements in **order of closeness**.

---

## 📘 Examples

### Example 1

**Input**:
`arr[] = [1, 3, 4, 10, 12], k = 2, x = 4`
**Output**:
`3 1`
**Explanation**:
4 is excluded. Closest elements to 4 are:

* 3 → distance 1
* 1 → distance 3
  So, the 2 closest elements are: `3 1`

---

### Example 2

**Input**:
`arr[] = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], k = 4, x = 35`
**Output**:
`39 30 42 45`
**Explanation**:

* 1st closest to 35 is 39
* 2nd: 30
* 3rd: 42
* 4th: 45

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ k ≤ arr.size()`
* `1 ≤ x ≤ 10^6`
* `1 ≤ arr[i] ≤ 10^6`

---

## 💡 Expected Complexities

* **Time**: O(log n + k)
* **Auxiliary Space**: O(k)

---

## 🏷️ Tags

`Arrays`, `Binary Search`, `Algorithms`, `STL`, `Priority Queue`

---

## 🧠 Company Tags

* Amazon
* OYO Rooms

---

## 🔗 Related Articles

* [Find K Closest Elements Given Value](#)

---

Thanks for sharing the test result. From the image, we can diagnose **why your code fails**.

---

## ❌ Problem

Your code is **returning the k closest elements to x in increasing order**, but the expected behavior is:

> **Return the `k` closest elements to `x` in the exact order of closeness**, using these rules:

1. Sort by absolute difference to `x`.
2. If a tie, **prefer the element with the larger value**.
3. Maintain the above order in the final output.

---

### 🧪 Test Case (from image)

**Input**:
`arr = [14, 15, 22, 54, 58, 75, 112, 114]`
`k = 5, x = 18`

**Expected Output**:
`15 22 14 54 58`

**Your Output**:
`15 14 22 54 58`

Your output has the correct elements, but **in the wrong order of closeness**.

---

## ✅ Fix

We need to sort by `(abs(num - x), -num)` to handle tie-breaking, and **preserve that sort order** in final output.

---

### ✅ Updated Python Code

```python
class Solution:
    def printKClosest(self, arr, k, x):
        candidates = []

        for num in arr:
            if num == x:
                continue
            # First by absolute difference, then by higher value
            candidates.append((abs(num - x), -num, num))

        # Sort using the first two criteria
        candidates.sort()

        # Extract the last value from each tuple (the actual number), first k only
        result = [val for _, _, val in candidates[:k]]
        return result
```

---

### ✅ Dry Run on the Failed Case

* Distances from 18:

  ```
  14 → 4  
  15 → 3  
  22 → 4  
  54 → 36  
  58 → 40
  ```
* So sorted by closeness:

  ```
  15 (3)  
  22 (4)  
  14 (4)  
  54 (36)  
  58 (40)
  ```

Thus, correct output: `15 22 14 54 58`

---

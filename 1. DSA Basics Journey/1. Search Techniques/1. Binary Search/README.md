Here's a structured progression of **Binary Search problems**, from basic to advanced, including problem types and popular examples often seen in interviews (LeetCode, GFG, etc.).

---

## 🟢 Basic Binary Search Problems

> Focus: Understand the binary search template and its variants (left/right bias)

1. **Classic Binary Search**

   * Find target in a sorted array.
   * ✔️ LeetCode 704: [Binary Search](https://leetcode.com/problems/binary-search/)

2. **First and Last Occurrence**

   * Find first or last index of target (use left/right bias).
   * ✔️ LeetCode 34: [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

3. **Insert Position**

   * Where to insert target if not found.
   * ✔️ LeetCode 35: [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

4. **Square Root of Integer**

   * Find floor of sqrt(n) using binary search.
   * ✔️ LeetCode 69: [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
   * ✔️ GFG: [Square root of a number](https://www.geeksforgeeks.org/square-root-of-an-integer/)

---

## 🟡 Intermediate Binary Search Problems

> Focus: Binary search in answers, rotated arrays, peak elements, etc.

5. **Search in Rotated Sorted Array**

   * ✔️ LeetCode 33: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
   * ✔️ LeetCode 81: [With duplicates: ](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
   * ✔️ LeetCode 153: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)


6. **Peak Element**

   * Find index where element is greater than neighbors.
   * LeetCode 162: [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

7. **Binary Search on Answer**

   * LeetCode 875: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
   * LeetCode 410: [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

8. **Minimum in Rotated Sorted Array**

   * LeetCode 153: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

9. **Aggressive Cows (Binary Search on Distance)**

   * GFG: [Aggressive cows](https://www.geeksforgeeks.org/aggressive-cows-dynamic-programming-approach/)

---

## 🔴 Advanced Binary Search Problems

> Focus: Binary search on complex conditions, matrices, functions

10. **Median of Two Sorted Arrays**

* Binary search partitioning.
* LeetCode 4: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

11. **Find kth Smallest in Sorted Matrix**

* LeetCode 378: [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

12. **Find the Smallest Divisor Given a Threshold**

* Binary search over divisor range.
* LeetCode 1283

13. **Capacity to Ship Packages Within D Days**

* Binary search on answer range.
* LeetCode 1011

14. **Search in a 2D Matrix I & II**

* LeetCode 74 and 240

15. **Maximum Value at a Given Index in Bounded Array**

* LeetCode 1802: Advanced BS on sum constraints

---

---

Great! Here's the **standard Binary Search template** — a must-have in your DSA toolbox. It works for both classic search problems and "binary search on answer" optimization problems.

---

## ✅ Classic Binary Search Template (Search in Sorted Array)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid  # target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # target not found
```

---

## ✅ Binary Search on Answer Template (Optimization Problems)

Use this when:

* You need to **maximize/minimize** a value
* You can check feasibility using a monotonic function `is_valid(value)`

```python
def binary_search_answer(is_valid, low, high):
    result = low  # or -1 depending on the problem

    while low <= high:
        mid = (low + high) // 2
        
        if is_valid(mid):
            result = mid         # save valid answer
            low = mid + 1        # try higher (for max)
        else:
            high = mid - 1       # try lower
    
    return result
```

> 🔁 For **minimization**: move `high = mid - 1` when valid, and track lowest valid value.

---

## 🧪 Example: First `x` such that `x*x >= target`

```python
def is_valid(x): return x * x >= 20
binary_search_answer(is_valid, 0, 100)  # Output: 5
```

---

## 📌 Key Patterns

| Use Case                 | Technique        | Example Problem               |
| ------------------------ | ---------------- | ----------------------------- |
| Find target in sorted    | Classic binary   | Leetcode 704                  |
| First/last position      | Modified binary  | Leetcode 34                   |
| Search insert position   | Lower bound      | Leetcode 35                   |
| Minimum/max feasible val | Binary on answer | Leetcode 1011, 410, 875, 1802 |

---

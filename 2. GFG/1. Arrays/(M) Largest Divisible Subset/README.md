Here is the complete README-style conversion of the problem **"Largest Divisible Subset"**, preserving every detail from the image:

---

# 📘 Largest Divisible Subset

**Difficulty:** Medium
**Accuracy:** 43.71%
**Submissions:** 8K+
**Points:** 4
**Average Time:** 20m

---

## 🧾 Problem Statement

Given an array `arr[]` of distinct positive integers. Your task is to find the **largest subset** such that for every pair of elements `(x, y)` in the subset, **either `x` divides `y` or `y` divides `x`**.

> **Note:**
> If multiple subsets of the same maximum length exist, return the one that is **lexicographically greatest**, after sorting the subset in ascending order.

---

## 📌 Examples

### Example 1:

```
Input: arr[] = [1, 16, 7, 8, 4]
Output: [1, 4, 8, 16]
Explanation: The largest divisible subset is [1, 4, 8, 16], where each element divides the next one. This subset is already the lexicographically greatest one.
```

### Example 2:

```
Input: arr[] = [2, 4, 3, 8]
Output: [2, 4, 8]
Explanation: The largest divisible subset is [2, 4, 8], where each element divides the next one. This subset is already the lexicographically greatest one.
```

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10^3`
* `1 ≤ arr[i] ≤ 10^9`

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n²)
* **Auxiliary Space:** O(n)

---

## 💼 Company Tags

* Bloomberg
* Facebook
* Adobe
* Google
* Amazon
* Apple
* Microsoft
* Yahoo

---

## 🏷️ Topic Tags

* Dynamic Programming
* Sorting
* Arrays

---

## 📚 Related Articles

* [Largest Divisible Subset Array](https://www.geeksforgeeks.org/largest-divisible-subset/)

---

Here's the **README** for the GeeksforGeeks problem **“Kth Largest in a Stream”** based on the content from the provided image.

---

# Kth Largest in a Stream

**Difficulty**: Medium
**Points**: 4
**Average Time**: 20m
**Accuracy**: 31.59%

## 🧾 Problem Statement

Given an input stream `arr[]` of `n` integers, find the **k-th largest element** (not necessarily the k-th unique) after insertion of each element in the stream.

* If the k-th largest element doesn't exist after the current insertion, return `-1` for that insertion.
* Return a list of size `n` after all insertions.

---

## 🧠 Understanding with Examples

### Example 1

**Input:**

```
k = 4, n = 6  
arr[] = [1, 2, 3, 4, 5, 6]
```

**Output:**

```
[-1, -1, -1, 1, 2, 3]
```

**Explanation:**

* After inserting 1, 2, 3 ➝ Less than 4 elements ➝ return -1.
* After inserting 4 ➝ elements: \[1,2,3,4] ➝ 4th largest = 1
* Insert 5 ➝ \[1,2,3,4,5] ➝ 4th largest = 2
* Insert 6 ➝ \[1,2,3,4,5,6] ➝ 4th largest = 3

---

### Example 2

**Input:**

```
k = 1, n = 2  
arr[] = [3, 4]
```

**Output:**

```
[3, 4]
```

**Explanation:**

* Always return the largest (1st largest) so far.

---

## 🎯 Your Task

You need to implement the function:

```python
def kthLargest(k: int, n: int, arr: List[int]) -> List[int]:
```

This function:

* Takes `k`, `n`, and an array `arr[]` as input.
* After each insertion, returns the **k-th largest element** if it exists, or `-1`.

---

## 🧮 Expected Time & Space Complexity

* **Time Complexity**: `O(n * log k)`
* **Auxiliary Space**: `O(k)`

---

## 🔒 Constraints

* `1 ≤ k ≤ n ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## 🏷️ Tags

`Heap`, `Data Structures`

---

## 💼 Company Tags

`Flipkart`, `Amazon`, `Microsoft`, `Adobe`, `OYO Rooms`, `Cisco`, `Walmart`, `Hike`

---

## 🔗 Related Articles

* [Kth Largest Element In A Stream - GeeksforGeeks](https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/)

---

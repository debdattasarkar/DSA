
---

# 🧮 Maximum Sum Combination

**Difficulty**: Medium
**Accuracy**: 49.69%
**Submissions**: 87K+
**Points**: 4
**Average Time**: 30m

---

## 📝 Problem Statement

You are given two integer arrays `a[]` and `b[]` of equal size.

A **sum combination** is formed by adding **one element from `a[]`** and **one from `b[]`**, using **each index pair (i, j)** at most once.

Return the **top `k` maximum sum combinations**, sorted in **non-increasing order**.

---

## ✏️ Examples

### Example 1

```
Input:
a[] = [3, 2]
b[] = [1, 4]
k = 2

Output:
[7, 6]

Explanation:
Possible sums:
  3 + 1 = 4
  3 + 4 = 7
  2 + 1 = 3
  2 + 4 = 6

Top 2 sums = [7, 6]
```

---

### Example 2

```
Input:
a[] = [1, 4, 2, 3]
b[] = [2, 5, 1, 6]
k = 3

Output:
[10, 9, 9]

Explanation:
Top 3 maximum possible sums:
  4 + 6 = 10
  3 + 6 = 9
  4 + 5 = 9
```

---

## 📌 Constraints

* 1 ≤ a.size() = b.size() ≤ 10⁵
* 1 ≤ k ≤ a.size()
* 1 ≤ a\[i], b\[i] ≤ 10⁴

---

## ✅ Expected Complexities

* **Time Complexity**: O(n log n)
* **Auxiliary Space**: O(n)

---

## 🏷️ Tags

* Arrays
* Sorting
* Heap
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [K Maximum Sum Combinations Two Arrays](https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/)

---

Here’s a complete breakdown of your request for the **Maximum Sum Combination** problem:

---

## 📘 Text Explanation

We are given two arrays `a[]` and `b[]`, and we are to find the **k largest sums** that can be formed by adding one element from `a` and one from `b`. Each sum must be unique to a pair of indices `(i, j)` — meaning no index combination is reused.

To get the top **k** maximum combinations:

* A brute-force way would generate all `n^2` combinations and pick the top k.
* An optimized way uses a **Max-Heap** to track only the most promising combinations, sorted by sum.

---

## 🔍 Step-by-Step Dry Run

### Example:

```python
a = [1, 4, 2, 3]
b = [2, 5, 1, 6]
k = 3
```

### Step 1: Sort both arrays in descending order

```python
a = [4, 3, 2, 1]
b = [6, 5, 2, 1]
```

### Step 2: Initialize a Max-Heap (simulated with negative values in Python’s `heapq`)

* Push the **maximum possible sum**: `a[0] + b[0] = 4 + 6 = 10`
* Track index pairs in a set: `(0, 0)`

Heap: `[-10]`
Used index set: `{(0, 0)}`

### Step 3: Pop from heap and push the next best two possible combinations:

* From `(i, j)` = `(0, 0)`, try:

  * `(1, 0)` → `a[1] + b[0] = 3 + 6 = 9`
  * `(0, 1)` → `a[0] + b[1] = 4 + 5 = 9`

Now heap has: `[-9, -9]`
Used index set: `{(0, 0), (1, 0), (0, 1)}`

### Step 4: Continue extracting top values until k = 3

Result becomes: `[10, 9, 9]`

---

## ✅ Optimized Python Solutions

---

### 🔸 Brute-Force Solution (for understanding, not optimal)

```python
class Solution:
    def topKSumPairs(self, a, b, k):
        from heapq import nlargest

        sums = []
        for i in range(len(a)):
            for j in range(len(b)):
                sums.append(a[i] + b[j])

        # Get top k largest
        return nlargest(k, sums)
```

🟡 **Time:** O(n² log k)
🟡 **Space:** O(n²)

---

### 🔹 Optimized Max-Heap + Set (Expected in Interviews)

```python
import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        a.sort(reverse=True)  # Sort in descending order
        b.sort(reverse=True)

        max_heap = []
        visited = set()

        # Start with the largest possible pair (0, 0)
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))

        result = []

        for _ in range(k):
            curr_sum, i, j = heapq.heappop(max_heap)
            result.append(-curr_sum)  # Restore original sum

            # Next pair: (i + 1, j)
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            # Next pair: (i, j + 1)
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return result
```

✅ **Time:** O(k log k)
✅ **Space:** O(k + n log n)

---

## 🧠 Interview Q\&A Based on This Problem

---

### ❓ Q1: Why do we sort the arrays in descending order?

**A:** Sorting allows us to start from the largest possible sum. Since we always want the maximum remaining sum, we move either right or down in the sorted matrix of sums to find the next largest.

---

### ❓ Q2: Why do we use a set to track index pairs?

**A:** To avoid reprocessing the same `(i, j)` index pair. This ensures no duplicate pairs are added to the heap, maintaining uniqueness and preventing infinite loops.

---

### ❓ Q3: What data structure is used for efficiency in the optimized approach?

**A:** A Max-Heap (simulated using Python’s `heapq` with negative values) is used to efficiently extract the current maximum and explore next best candidates.

---

### ❓ Q4: What's the time and space complexity of the optimized approach?

* **Time Complexity:** O(k log k) — since we push and pop from the heap at most `k` times.
* **Space Complexity:** O(k) — for result and heap storage; in worst-case visited may store O(k) pairs.

---

### ❓ Q5: How would this scale for very large `k`?

**A:** The optimized method scales well even for large `k`, since we never generate all n² combinations. Instead, we build combinations on-the-fly from the most promising ones.

---


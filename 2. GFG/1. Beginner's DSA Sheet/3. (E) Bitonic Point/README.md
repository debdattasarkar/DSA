
---

# Bitonic Point

**Difficulty**: Easy
**Accuracy**: 58.67%
**Submissions**: 150K+
**Points**: 2
**Average Time**: 15m

---

## 🧠 Problem Statement

Given an array of integers `arr[]` that is:

* First **strictly increasing**, and
* Then **maybe strictly decreasing**,

Find the **bitonic point**, i.e., the **maximum element** in the array.

### ➕ Bitonic Point

A bitonic point is an element such that:

* All elements before it are strictly increasing.
* All elements after it are strictly decreasing.

---

> 📝 **Note**: It is guaranteed that the array contains **exactly one** bitonic point.

---

## 🧪 Examples

### Example 1

**Input**:

```python
arr[] = [1, 2, 4, 5, 7, 8, 3]
```

**Output**:

```python
8
```

**Explanation**:
Elements before 8 are strictly increasing `[1, 2, 4, 5, 7]` and elements after 8 are strictly decreasing `[3]`.

---

### Example 2

**Input**:

```python
arr[] = [10, 20, 30, 40, 50]
```

**Output**:

```python
50
```

**Explanation**:
Elements before 50 are strictly increasing `[10, 20, 30, 40]`, and there are no elements after 50.

---

### Example 3

**Input**:

```python
arr[] = [120, 100, 80, 20, 0]
```

**Output**:

```python
120
```

**Explanation**:
There are no elements before 120. Elements after 120 are strictly decreasing `[100, 80, 20, 0]`.

---

## 📚 Constraints

* $3 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr[i]} \leq 10^6$

---

## 🧮 Expected Time and Space Complexity

* **Time Complexity**: `O(log n)`
* **Auxiliary Space**: `O(1)`

---

## 🏷️ Tags

* Arrays
* Searching
* Data Structures
* Algorithms
* Binary Search

---

## 💼 Company Tags

* Flipkart
* Amazon
* Microsoft

---

## 🧑‍💻 Related Interview Experiences

* Flipkart Interview Set 3

---

## 🔗 Related Articles

* [Find The Maximum Element In An Array Which Is First Increasing And Then Decreasing](https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/)

---

---

Let's break it down fully using the **GFG-strict binary search version** of the Bitonic Point problem.

---

## ✅ Problem Summary – Bitonic Point

Given an array `arr[]` which is first **strictly increasing** and then **strictly decreasing**, find the **maximum element** (also called the **Bitonic Point**).

* It is guaranteed that the array contains **exactly one bitonic point**.
* Constraints:

  * `3 ≤ arr.size() ≤ 10^5`
  * `1 ≤ arr[i] ≤ 10^6`
* Time Complexity: **O(log n)**
* Space Complexity: **O(1)**

---

## 🔍 Step-by-Step Text Explanation (Dry Run)

### Example

```python
arr = [1, 3, 8, 12, 4, 2]
```

* This is increasing until `12`, then decreasing.
* Expected Output: **12**

### Logic

1. **Start Binary Search** between indices `left = 1` and `right = n - 2`
   (We avoid checking boundaries directly inside loop.)

2. At each step:

   * Check `arr[mid-1]`, `arr[mid]`, and `arr[mid+1]`
   * If `arr[mid-1] < arr[mid] > arr[mid+1]`: Return `arr[mid]` → it's the peak
   * If `arr[mid-1] < arr[mid] < arr[mid+1]`: Peak is to the right → shift `left = mid + 1`
   * If `arr[mid-1] > arr[mid] > arr[mid+1]`: Peak is to the left → shift `right = mid - 1`

---

### Dry Run for `[1, 3, 8, 12, 4, 2]`

* `left = 1`, `right = 4` (n = 6)

* `mid = (1+4)//2 = 2`

  * `arr[1]=3`, `arr[2]=8`, `arr[3]=12`
  * `3 < 8 < 12`: move right → `left = 3`

* `mid = (3+4)//2 = 3`

  * `arr[2]=8`, `arr[3]=12`, `arr[4]=4`
  * `8 < 12 > 4`: peak found → return `12`

---

## ✅ Final Code (GFG-Safe and Optimized)

```python
#User function Template for python3
class Solution:

    def findMaximum(self, arr):
        n = len(arr)
        left, right = 1, n - 2  # Exclude boundaries initially
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid - 1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # Only happens if peak is at boundary
        if right == 0:
            return arr[0]
        return arr[n - 1]
```

---

## 🧠 Common Interview Questions (with Answers)

### Q1: Why do you start from `left = 1` and `right = n - 2`?

**A:** Because checking `arr[mid-1]` and `arr[mid+1]` requires mid to be a non-boundary index to avoid index errors. The peak is never guaranteed at the edge due to strict increase/decrease, so we search between them.

---

### Q2: Can this problem be solved using linear search?

**A:** Yes, but linear search gives **O(n)** time, while binary search reduces it to **O(log n)**, which is optimal for large arrays.

---

### Q3: What’s the difference between bitonic array and unimodal array?

**A:** Bitonic array is strictly increasing then strictly decreasing. A unimodal array can have non-strict (equal) values, which needs different handling.

---

### Q4: What if the array has multiple peaks?

**A:** This problem guarantees **one unique peak**. If not, binary search would need to be modified to find **maximum among all peaks** using additional checks.

---

## 🌍 Real-World Use Cases (Just a Few Important)

1. **Stock Market Analysis**

   * Bitonic point represents the **highest price** before a consistent decline — useful in detecting **reversal zones**.

2. **Peak Detection in Signal Processing**

   * Identify where a signal rises and then starts decaying.

3. **Data Compression / Optimization**

   * Locating turning points in sequences (e.g., bandwidth, traffic load curves).

4. **Sensor Data (IoT, Biomedical)**

   * Track peaks in heart rate, temperature readings, etc., where the sequence is monotonic then reverses.

---

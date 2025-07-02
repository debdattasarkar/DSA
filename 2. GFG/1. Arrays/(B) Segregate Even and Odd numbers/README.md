
---

# ✅ Segregate Even and Odd Numbers

---

### 📘 Problem Statement

Given an array `arr[]`, **segregate even and odd numbers** in-place. The final array should contain:

1. All even numbers first **in sorted order**
2. Then all odd numbers **in sorted order**

📝 **Note**: Modify the array **in-place** (do not return a new array).

---

### 🧪 Examples

#### Example 1:

```
Input: arr = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8, 90 → sorted → [8, 12, 34, 90]
             Odd numbers are 45, 9, 3 → sorted → [3, 9, 45]
```

#### Example 2:

```
Input: arr = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
Explanation: Evens → [0, 2, 4], Odds → [1, 3]
```

#### Example 3:

```
Input: arr = [10, 22, 4, 6]
Output: [4, 6, 10, 22]
Explanation: All are even → sorted → [4, 6, 10, 22]
```

---

## 📌 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $0 \leq \text{arr}[i] \leq 10^5$

---

### ⏱ Expected Time Complexity: O(n log n)

### 💾 Expected Auxiliary Space: O(1)

---

## 🔍 Step-by-Step Dry Run

### Input:

```python
arr = [12, 34, 45, 9, 8, 90, 3]
```

### Process:

1. Traverse and separate:

   * Even: \[12, 34, 8, 90]
   * Odd:  \[45, 9, 3]

2. Sort each:

   * Sorted even: \[8, 12, 34, 90]
   * Sorted odd:  \[3, 9, 45]

3. Merge back:

   * Final arr: \[8, 12, 34, 90, 3, 9, 45]

---

## ✅ Python Code

```python
class Solution:
    def segregateEvenOdd(self, arr):
        # Separate evens and odds
        evens = [x for x in arr if x % 2 == 0]
        odds = [x for x in arr if x % 2 != 0]

        # Sort both sublists
        evens.sort()
        odds.sort()

        # Overwrite original array in-place
        for i in range(len(evens)):
            arr[i] = evens[i]
        for i in range(len(odds)):
            arr[len(evens) + i] = odds[i]
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    void segregateEvenOdd(vector<int>& arr) {
        vector<int> evens, odds;

        // Separate evens and odds
        for (int num : arr) {
            if (num % 2 == 0) evens.push_back(num);
            else odds.push_back(num);
        }

        // Sort both
        sort(evens.begin(), evens.end());
        sort(odds.begin(), odds.end());

        // Merge into original
        int i = 0;
        for (int num : evens) arr[i++] = num;
        for (int num : odds) arr[i++] = num;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    segregateEvenOdd(arr) {
        // Separate evens and odds
        let evens = arr.filter(x => x % 2 === 0).sort((a, b) => a - b);
        let odds = arr.filter(x => x % 2 !== 0).sort((a, b) => a - b);

        // Overwrite original array
        for (let i = 0; i < arr.length; i++) {
            arr[i] = i < evens.length ? evens[i] : odds[i - evens.length];
        }
    }
}
```

---

## 💬 Interview Questions & Answers

---

### 🔹 Q1: Why is sorting required?

**A**:
The problem demands that evens and odds are **not only segregated**, but also **individually sorted**.

---

### 🔹 Q2: What’s the time and space complexity?

**A**:

* **Time**: O(n log n) → due to sorting
* **Space**: O(1) auxiliary (if modifying in-place and using fixed memory buffers)

---

### 🔹 Q3: Can it be done in O(n) time?

**A**:
Not if sorting is required.
If **only segregation** was needed, it could be done in O(n) using two-pointer partitioning.

---

### 🔹 Q4: What if array contains only even or only odd numbers?

**A**:
Both cases are valid. Sorting a single sub-array still works and leaves the rest unchanged.

---

### 🔹 Q5: Can this scale to 10^6 elements?

**A**:
Yes. Sorting arrays of that size is feasible in modern systems and well-supported by `sort()` in Python/C++/JS.

---

### 🔹 Q6: What edge cases should be tested?

* All evens: \[2, 4, 6] → sorted
* All odds: \[3, 5, 1] → sorted
* Single element: \[1]
* Already sorted input
* Alternating even and odd: \[1, 2, 3, 4]

---

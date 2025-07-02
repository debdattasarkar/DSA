
---

# 🔄 Swap Kth Elements

---

### 🧾 Problem Statement

Given an array `arr[]`, swap the **k<sup>th</sup> element from the beginning** with the **k<sup>th</sup> element from the end**.

📝 **Note**: Indexing is **1-based** (i.e., `k = 1` means first element, not zeroth).

---

### 🧪 Examples

#### Example 1:

```
Input:  arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 3  
Output: [1, 2, 6, 4, 5, 3, 7, 8]  
Explanation: Swap 3rd from beginning (3) and 3rd from end (6)
```

#### Example 2:

```
Input:  arr = [5, 3, 6, 1, 2], k = 2  
Output: [5, 1, 6, 3, 2]  
Explanation: Swap 2nd from beginning (3) and 2nd from end (1)
```

---

## 📌 Constraints

* $1 \leq \text{arr.size()} < 10^6$
* $-10^9 \leq \text{arr}[i] \leq 10^9$

---

### ⏱ Expected Time Complexity: O(1)

### 💾 Expected Auxiliary Space: O(1)

---

## 🔍 Step-by-Step Dry Run

**Input**:

```python
arr = [5, 3, 6, 1, 2], k = 2
```

**Process**:

* k<sup>th</sup> from beginning: index `k-1 = 1` → value = 3
* k<sup>th</sup> from end: index `n-k = 5-2 = 3` → value = 1
* Swap `arr[1]` and `arr[3]`

**Output**:

```python
[5, 1, 6, 3, 2]
```

---

## ✅ Python Code

```python
class Solution:
    def swapKth(self, arr, n, k):
        # 1-based indexing → convert to 0-based
        left_index = k - 1
        right_index = n - k

        # Swap elements in-place
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

        return arr  # Optional: depends on interface
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    void swapKth(int arr[], int n, int k) {
        // Swap (k-1)th from start and (n-k)th from start
        swap(arr[k - 1], arr[n - k]);
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    swapKth(arr, n, k) {
        // Swap k-th from beginning with k-th from end
        const i = k - 1;
        const j = n - k;

        [arr[i], arr[j]] = [arr[j], arr[i]];

        return arr;
    }
}
```

---

## 🤔 Interview Questions & Answers

---

### 🔹 Q1: What’s the time and space complexity?

**A**:

* Time: **O(1)**
* Space: **O(1)**
  Because it's a single in-place swap.

---

### 🔹 Q2: Why use `k-1` and `n-k`?

**A**:
Because the array is 0-based, but the question uses **1-based indexing**:

* `k - 1` = k<sup>th</sup> from **start**
* `n - k` = k<sup>th</sup> from **end**

---

### 🔹 Q3: What happens if `2k - 1 == n`?

**A**:
That means the element being swapped is the same on both ends (middle element in odd-length array), so swapping has **no effect**.

---

### 🔹 Q4: Can you do it in one line?

**A**:
Yes (in Python):

```python
arr[k - 1], arr[n - k] = arr[n - k], arr[k - 1]
```

---

### 🔹 Q5: Any edge cases?

**A**:

* `k = 1`: swap first and last
* `k = n`: same as above
* `k > n`: invalid → may crash or wrap (should guard if input isn't validated)

---

### 🔹 Q6: Will this scale to 10<sup>6</sup> elements?

**A**:
Yes — it only accesses two values and swaps them. No loop or extra memory needed.

---


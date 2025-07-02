
---

# ✅ Elements in the Range 

**Difficulty**: Basic
**Accuracy**: 37.28%
**Submissions**: 67K+
**Points**: 1

---

## 🧾 Problem Statement

Given an array `arr[]` containing positive elements. Two integers `A` and `B` define a range.
The task is to check **if the array contains all elements** in the **inclusive range `[A, B]`**.

📌 **Note**:
Return `True` if the array contains all elements in the range, otherwise return `False`.

---

## 🧪 Examples

#### ✅ Example 1:

```
Input:
n = 7, A = 2, B = 5
arr = [1, 4, 5, 2, 7, 8, 3]

Output: True

Explanation:
It contains all elements between 2 and 5 → 2, 3, 4, 5.
```

#### ❌ Example 2:

```
Input:
n = 7, A = 2, B = 6
arr = [1, 4, 5, 2, 7, 8, 3]

Output: False

Explanation:
Element 6 is missing from the array.
```

---

## 🎯 Your Task

Write a function:

```python
class Solution:
    def check_elements(self, arr, n, A, B):
```

Return `True` if array `arr[]` contains all integers in the range `[A, B]`, else return `False`.

---

## ⏱️ Expected Time and Space Complexity

* **Time Complexity**: O(N)
* **Auxiliary Space**: O(1) if using fixed-size set/map; else O(N)

---

## 📌 Constraints

* $1 \leq n \leq 10^7$
* Elements of `arr[]` are **positive integers**

---

## 🧠 Step-by-Step Dry Run

**Input**:
`arr = [1, 4, 5, 2, 7, 8, 3]`, `A = 2`, `B = 5`

1. Store all elements of the array in a `Set` → `{1, 2, 3, 4, 5, 7, 8}`
2. Loop from `i = 2` to `5`:

   * 2 → ✅ found
   * 3 → ✅ found
   * 4 → ✅ found
   * 5 → ✅ found
3. All present → return **True**

---

## ✅ Optimized Code

### 🔹 Python

```python
class Solution:
    def check_elements(self, arr, n, A, B):
        # Store all array elements in a set
        elements = set(arr)

        # Check all elements in range [A, B]
        for i in range(A, B + 1):
            if i not in elements:
                return False  # Missing value in range

        return True  # All required elements are present
```

---

### 🔹 C++

```cpp
class Solution {
  public:
    bool check_elements(int arr[], int n, int A, int B) {
        unordered_set<int> elements;

        // Insert all elements into the set
        for (int i = 0; i < n; ++i) {
            elements.insert(arr[i]);
        }

        // Check each value in the range
        for (int i = A; i <= B; ++i) {
            if (elements.find(i) == elements.end()) {
                return false;  // Not found
            }
        }

        return true;  // All values found
    }
};
```

---

### 🔹 JavaScript

```javascript
class Solution {
    check_elements(arr, n, A, B) {
        const elements = new Set(arr);  // Store all elements

        // Check every value from A to B
        for (let i = A; i <= B; i++) {
            if (!elements.has(i)) {
                return false; // i is missing
            }
        }

        return true; // All values found
    }
}
```

---

## 🧑‍💼 Interview Questions & Expected Answers

| Question                                      | Answer                                                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Q1. What is the time complexity?**          | **O(N)** — due to set insertion and lookup for each element.                                                        |
| **Q2. What data structure is used here?**     | A **Hash Set (unordered\_set / Set / set)** to allow O(1) average lookups.                                          |
| **Q3. What if array is sorted?**              | A sorted array allows a **two-pointer** sweep, but worst-case remains O(N).                                         |
| **Q4. Can you solve it without extra space?** | Yes, but only if array values are bounded and allow frequency maps or bit masks. Otherwise, using a set is optimal. |
| **Q5. What edge cases should you consider?**  | - Range outside the array bounds<br> - Empty range (`A == B`)<br> - Duplicates present                              |
| **Q6. What is the space complexity?**         | O(N) in worst case (if all values are unique and in set).                                                           |
| **Q7. Could the problem be done in-place?**   | Not reliably unless array size is known and bounded in values (e.g., <= 10^5).                                      |


### 🔹 Q8: Why use a set?

**A**:

* Set provides O(1) average-case lookup time.
* It's efficient for presence checks in a large array.

---

### 🔹 Q9: Could you do it without a set?

**A**:

* Yes, by sorting the array and binary searching each number from A to B, but that would take O(N log N + (B-A+1)·log N), which is slower.

---

### 🔹 Q10: What edge cases should be tested?

**A**:

* `A == B`: Single number check
* Elements at edges of array
* Large range with missing one value
* All values duplicated
* Empty array (if allowed — based on constraints, it won’t be)

---

### 🔹 Q11: Can this solution scale to 10^7 elements?

**A**:

* Yes. Python’s built-in `set` and C++’s `unordered_set` are efficient and suitable for 10 million entries in practice.

---

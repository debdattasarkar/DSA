Here's a **step-by-step explanation** followed by Python, C++, and JavaScript implementations (with inline logic comments) for the **“Sum Except First and Last”** problem.

---

### 🔍 **Explanation with Dry Run:**

#### Problem:

You're given an array `arr[]`. Return the **sum of all elements excluding** the first and last elements.

#### Constraints:

* At least 2 elements in the array.
* Elements are positive integers.

---

### 🧠 **Dry Run Example:**

**Input:** `arr = [5, 24, 39, 60, 15, 28, 27, 40, 50, 90]`
**Exclude:** First = 5, Last = 90
**Sum:** 24 + 39 + 60 + 15 + 28 + 27 + 40 + 50 = **283**

**Output:** `283`

---

### ✅ Python Code

```python
class Solution:
    def sumExceptFirstLast(self, arr):
        # If there are only two elements, return 0
        if len(arr) <= 2:
            return 0
        # Sum from index 1 to len(arr) - 2 (excluding first and last)
        return sum(arr[1:-1])
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    int sumExceptFirstLast(vector<int>& arr) {
        int n = arr.size();
        if (n <= 2) return 0; // Only 2 elements: no elements in between
        int sum = 0;
        // Start from second element and go till second-last
        for (int i = 1; i < n - 1; i++) {
            sum += arr[i];
        }
        return sum;
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    sumExceptFirstLast(arr) {
        // If array has 2 or fewer elements, return 0
        if (arr.length <= 2) return 0;

        let sum = 0;
        // Sum elements from index 1 to length-2
        for (let i = 1; i < arr.length - 1; i++) {
            sum += arr[i];
        }
        return sum;
    }
}
```

---

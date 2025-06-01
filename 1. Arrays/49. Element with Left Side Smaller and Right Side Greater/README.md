### ✅ Problem Summary: **Element with left side smaller and right side greater**

**Task**:
Given an array `arr[]`, find the **first** element such that:

* All elements on the **left** are **smaller** than it.
* All elements on the **right** are **greater** than it.

If no such element exists, return `-1`.

---

### 🔍 Constraints:

* $3 \leq \text{arr.size()} \leq 10^6$
* $1 \leq \text{arr}[i] \leq 10^6$
* Time Complexity: **O(n)**
* Auxiliary Space: **O(n)**

---

### 🧠 Explanation with Step-by-Step Dry Run

#### Example Input:

```
arr = [4, 2, 5, 7]
```

#### Step-by-Step:

We are looking for an element where:

* All elements to the **left are smaller**.
* All elements to the **right are greater**.

##### Step 1: Build Left Max Array

`leftMax[i]` = max element on the left of index `i`

```
leftMax = [ -inf, 4, 4, 5 ]
```

##### Step 2: Build Right Min Array

`rightMin[i]` = min element on the right of index `i`

```
rightMin = [ 2, 5, 7, inf ]
```

##### Step 3: Compare Each Element

* i = 0: 4 > leftMax\[-inf] ✅ but 4 >= rightMin\[2] ❌
* i = 1: 2 > 4 ❌
* i = 2: 5 > 4 ✅ and 5 < 7 ✅ ⇒ ✅ FOUND
  **Return: 5**

---

### ✅ Output: `5`

---

## 💻 Code Implementations with Inline Comments

---

### 🔹 Python

Thanks for pointing that out — the issue is with the **definition of the problem** and how the condition is enforced:

### ❗ Mistake in Earlier Code:

The element must:

1. Be **strictly greater than all elements on its left**.
2. Be **strictly smaller than all elements on its right**.

Earlier code checked:

* `arr[i] > leftMax[i]` ✅
* `arr[i] < rightMin[i]` ✅

But we **must ensure** that:

* **All** elements to the **left** are smaller.
* **All** elements to the **right** are greater.
  This means we can't include equality and must **exclude the boundaries** carefully.

---

### ✅ Correct Python Implementation (handling all test cases)

```python
class Solution:
    def findElement(self, arr):
        n = len(arr)
        if n < 3:
            return -1

        # Step 1: Construct max_left array
        max_left = [0] * n
        max_left[0] = float('-inf')
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i - 1])

        # Step 2: Construct min_right array
        min_right = [0] * n
        min_right[-1] = float('inf')
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i + 1])

        # Step 3: Check the required condition
        for i in range(1, n - 1):  # Must exclude first and last elements
            if max_left[i] < arr[i] < min_right[i]:
                return arr[i]

        return -1
```

---

### ✅ Dry Run for `arr = [98, 40, 65, 59, 27, 20, 45, 87, 34, 99]`

Let’s build:

**max\_left:**

```
[-inf, 98, 98, 98, 98, 98, 98, 98, 98, 98]
```

**min\_right:**

```
[20, 20, 20, 20, 20, 34, 34, 34, 99, inf]
```

Now compare for each `i` from 1 to 8:

* Check if `arr[i] > max_left[i]` and `arr[i] < min_right[i]`
* None satisfy both → ✅ Output: `-1`

---

### 🧪 Test Output:

Input:

```
arr = [98, 40, 65, 59, 27, 20, 45, 87, 34, 99]
```

**Correct Output:** `-1`
**Earlier code returned:** `99` ❌

---

Here are the **corrected implementations** of the "Element with left side smaller and right side greater" problem in **C++** and **JavaScript**, matching the corrected Python version above.

---

## ✅ C++ Implementation (Corrected)

```cpp
class Solution {
public:
    int findElement(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return -1;

        vector<int> maxLeft(n);
        vector<int> minRight(n);

        // Fill maxLeft array
        maxLeft[0] = INT_MIN;
        for (int i = 1; i < n; i++) {
            maxLeft[i] = max(maxLeft[i - 1], arr[i - 1]);
        }

        // Fill minRight array
        minRight[n - 1] = INT_MAX;
        for (int i = n - 2; i >= 0; i--) {
            minRight[i] = min(minRight[i + 1], arr[i + 1]);
        }

        // Traverse to find the valid element
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] > maxLeft[i] && arr[i] < minRight[i]) {
                return arr[i];
            }
        }

        return -1;
    }
};
```

---

## ✅ JavaScript Implementation (Corrected)

```javascript
class Solution {
    findElement(arr) {
        const n = arr.length;
        if (n < 3) return -1;

        const maxLeft = Array(n).fill(0);
        const minRight = Array(n).fill(0);

        // Step 1: Fill maxLeft
        maxLeft[0] = -Infinity;
        for (let i = 1; i < n; i++) {
            maxLeft[i] = Math.max(maxLeft[i - 1], arr[i - 1]);
        }

        // Step 2: Fill minRight
        minRight[n - 1] = Infinity;
        for (let i = n - 2; i >= 0; i--) {
            minRight[i] = Math.min(minRight[i + 1], arr[i + 1]);
        }

        // Step 3: Find the element that satisfies the condition
        for (let i = 1; i < n - 1; i++) {
            if (arr[i] > maxLeft[i] && arr[i] < minRight[i]) {
                return arr[i];
            }
        }

        return -1;
    }
}
```

---

These versions now correctly:

* Use `>` for all elements to the left.
* Use `<` for all elements to the right.
* Skip the first and last element in the search.
* Work in **O(n)** time and **O(n)** space.


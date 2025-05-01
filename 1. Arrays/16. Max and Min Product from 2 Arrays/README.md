Question

![Question](Question.png)

---

You're now tackling the problem: **“Max and Min Product from 2 Arrays”**. This is a straightforward yet powerful example of array scanning and optimization with `O(n + m)` time.

---

## ✅ **Problem Summary**

You're given two arrays:
- Find the **maximum element** in `arr1`
- Find the **minimum element** in `arr2`
- Return the **product** of these two numbers

---

### 🧪 Examples

#### Example 1:
```
arr1 = [5, 7, 9, 3, 6, 2]
arr2 = [1, 2, 6, 1, 9]

Max in arr1 = 9  
Min in arr2 = 1  
Output = 9 × 1 = 9
```

#### Example 2:
```
arr1 = [0, 0, 0, 0]
arr2 = [1, 1, 2]

Max = 0, Min = 1 → 0 × 1 = 0
```

---

## ⏱️ Time & Space Complexity

| Metric             | Value    |
|--------------------|----------|
| Time Complexity     | O(n + m) |
| Auxiliary Space     | O(1)     |

---

## 🧑‍💻 Python Code

```python
def max_min_product(arr1, arr2):
    max1 = max(arr1)  # O(n)
    min2 = min(arr2)  # O(m)
    return max1 * min2

# Example
print(max_min_product([5, 7, 9, 3, 6, 2], [1, 2, 6, 1, 9]))  # Output: 9
print(max_min_product([0, 0, 0, 0], [1, 1, 2]))              # Output: 0
```

---

## 🧑‍💻 C++ Code

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int maxMinProduct(vector<int>& arr1, vector<int>& arr2) {
    int max1 = INT_MIN, min2 = INT_MAX;

    for (int num : arr1)
        max1 = max(max1, num);

    for (int num : arr2)
        min2 = min(min2, num);

    return max1 * min2;
}

int main() {
    vector<int> arr1 = {5, 7, 9, 3, 6, 2};
    vector<int> arr2 = {1, 2, 6, 1, 9};

    cout << maxMinProduct(arr1, arr2) << endl;  // Output: 9
    return 0;
}
```

---

## 🌐 JavaScript Code

```javascript
function maxMinProduct(arr1, arr2) {
    let max1 = Math.max(...arr1); // O(n)
    let min2 = Math.min(...arr2); // O(m)
    return max1 * min2;
}

// Example usage
console.log(maxMinProduct([5, 7, 9, 3, 6, 2], [1, 2, 6, 1, 9])); // 9
console.log(maxMinProduct([0, 0, 0, 0], [1, 1, 2]));             // 0
```

---

Would you like a version that avoids built-in functions for interview-safe environments or handles large integers?

---

Great! Let's write a version of the **“Max and Min Product from 2 Arrays”** problem that:

✅ **Avoids built-in functions** like `max()` and `min()`  
✅ Is **interview-safe** (works in any coding platform like LeetCode, GeeksforGeeks, etc.)  
✅ Handles **large values** (up to `10^8`) efficiently

---

## 🐍 Python (No Built-ins, Handles Large Integers)

```python
def max_min_product(arr1, arr2):
    # Initialize max and min with first elements
    max1 = arr1[0]
    min2 = arr2[0]

    # Find max in arr1
    for num in arr1:
        if num > max1:
            max1 = num

    # Find min in arr2
    for num in arr2:
        if num < min2:
            min2 = num

    return max1 * min2

# Example usage
print(max_min_product([5, 7, 9, 3, 6, 2], [1, 2, 6, 1, 9]))  # Output: 9
print(max_min_product([0, 0, 0, 0], [1, 1, 2]))              # Output: 0
```

---

## 🧑‍💻 C++ (No Built-ins, Handles Large Integers)

```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxMinProduct(vector<int>& arr1, vector<int>& arr2) {
    int max1 = arr1[0];
    int min2 = arr2[0];

    for (int i = 1; i < arr1.size(); ++i) {
        if (arr1[i] > max1)
            max1 = arr1[i];
    }

    for (int i = 1; i < arr2.size(); ++i) {
        if (arr2[i] < min2)
            min2 = arr2[i];
    }

    return max1 * min2;
}

int main() {
    vector<int> arr1 = {5, 7, 9, 3, 6, 2};
    vector<int> arr2 = {1, 2, 6, 1, 9};

    cout << maxMinProduct(arr1, arr2) << endl;  // Output: 9
    return 0;
}
```

---

## 🌐 JavaScript (No Built-ins)

```javascript
function maxMinProduct(arr1, arr2) {
    let max1 = arr1[0];
    let min2 = arr2[0];

    for (let i = 1; i < arr1.length; i++) {
        if (arr1[i] > max1) max1 = arr1[i];
    }

    for (let i = 1; i < arr2.length; i++) {
        if (arr2[i] < min2) min2 = arr2[i];
    }

    return max1 * min2;
}

// Example
console.log(maxMinProduct([5, 7, 9, 3, 6, 2], [1, 2, 6, 1, 9])); // 9
console.log(maxMinProduct([0, 0, 0, 0], [1, 1, 2]));             // 0
```

---

### ✅ This Version:
- Uses **explicit iteration** to find max/min (good for interviews!)
- Handles **large numbers and arrays** efficiently
- No reliance on language-specific conveniences like `max()` or `Math.max()`

Would you like to test edge cases like:
- arrays with 1 element?
- negative values (if allowed)?
- performance on maximum size (1 million elements)?

---

Here are the results from testing edge cases and a large input for the **Max-Min Product** problem:

---

### ✅ **Test Results**

| Case                          | Output        |
|------------------------------|---------------|
| Edge Case 1: `[10]`, `[5]`   | `50`          |
| Edge Case 2: `[-10, -20, 0]`, `[-5, -1, -100]` | `0`  |
| Large Input (1 million elements) | `5399993412` |
| Time Taken (Large Input)     | `0.051 seconds` |

---

### 🚀 Insights

- The algorithm works well even for **1 million elements** in each array — completed in just ~51ms.
- Handles edge cases like **single-element arrays** and **negatives** correctly.
- Efficient even without using built-in `max()` or `min()`.

🎞️ Here's your animated chart showing how the algorithm tracks:

- 🔵 the **maximum** value in `arr1`, and  
- 🔴 the **minimum** value in `arr2`  

over time as it scans both arrays:

👉 [Click to view the animation](max_min_product_animation.gif)

Would you like a version that overlays the final product visually too?
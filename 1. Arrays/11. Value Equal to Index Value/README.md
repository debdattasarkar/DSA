Question

![Question](Question.png)

---
🎯 **"Value equal to index value"** problem.

---

# 🧠 **Problem Summary**:
Given an array **`arr[]`**, return **all indices** `i` such that:

```plaintext
arr[i] == i
```

⚠️ **1-based indexing**, meaning `arr[1]` corresponds to index 1 (not 0).

---

# ✅ Example:
```plaintext
Input:  arr[] = [15, 2, 45, 4, 7]
                ↑  ↑       ↑
1-based index:  1  2  3  4  5

Output: [2, 4]
Because: arr[2] == 2, arr[4] == 4
```

---

# 🚀 Efficient Approach:
### Time Complexity: `O(n)`  
- Loop from `i = 0` to `n-1`
- If `arr[i] == i + 1`, add `(i+1)` to result

### Auxiliary Space: `O(k)` (where `k` is number of matches)

---

# 🔧 C++ Implementation:

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> valueEqualToIndex(const vector<int>& arr) {
    vector<int> result;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == i + 1) {
            result.push_back(i + 1); // 1-based index
        }
    }
    return result;
}

int main() {
    vector<int> arr = {15, 2, 45, 4, 7};
    vector<int> res = valueEqualToIndex(arr);
    for (int i : res) {
        cout << i << " ";
    }
    return 0;
}
```

---

# 🐍 Python Version:

```python
def value_equal_to_index(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == i + 1:  # 1-based index
            result.append(i + 1)
    return result

# Example usage
arr = [15, 2, 45, 4, 7]
print(value_equal_to_index(arr))  # Output: [2, 4]
```

---

# 🌐 JavaScript Version:

```javascript
function valueEqualToIndex(arr) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === i + 1) {
            result.push(i + 1);
        }
    }
    return result;
}

// Example
let arr = [15, 2, 45, 4, 7];
console.log(valueEqualToIndex(arr)); // Output: [2, 4]
```

---

# ✅ Interview Insights:
- **Easy-level** but **frequently asked** for warm-up.
- Great for practicing:
  - **Indexing logic**
  - **Array traversal**
  - **Understanding 1-based vs 0-based indexing**

---

Want to try solving this inside your `ArrayManager` class for each language?  
I can guide you to add a `getMatchingIndices()` method in C++, Python, and JS!

👉 Want to do that?
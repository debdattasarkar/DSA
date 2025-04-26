Got it — this is the **Smallest Sum Contiguous Subarray** problem, very similar to Kadane’s algorithm, but instead of finding **maximum subarray sum**, you need the **minimum**.

---

### ✅ C++ Code:
```cpp
#include <vector>
#include <algorithm>
using namespace std;

int smallestSubarraySum(const vector<int>& arr, int n) {
    int minSum = arr[0];
    int currSum = arr[0];

    for (int i = 1; i < n; ++i) {
        currSum = min(arr[i], currSum + arr[i]);
        minSum = min(minSum, currSum);
    }

    return minSum;
}
```

---

### 🧪 Example Usage:
```cpp
#include <iostream>

int main() {
    vector<int> arr1 = {3, -4, 2, -3, -1, 7, -5};
    vector<int> arr2 = {2, 6, 8, 1, 4};

    cout << smallestSubarraySum(arr1, arr1.size()) << endl; // Output: -6
    cout << smallestSubarraySum(arr2, arr2.size()) << endl; // Output: 1

    return 0;
}
```

---

### 🔥 Quick Summary:
- It's the **Kadane's algorithm**, but use `min()` instead of `max()`.
- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

---

Of course! Here's the **Python code** for the **Smallest Sum Contiguous Subarray** problem:

---

### ✅ Python Code:
```python
def smallestSubarraySum(arr):
    min_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = min(num, curr_sum + num)
        min_sum = min(min_sum, curr_sum)

    return min_sum
```

---

### 🧪 Example Usage:
```python
print(smallestSubarraySum([3, -4, 2, -3, -1, 7, -5]))  # Output: -6
print(smallestSubarraySum([2, 6, 8, 1, 4]))            # Output: 1
```

---

### ⏱ Time & Space Complexity:
- **Time Complexity:** `O(n)` — Single pass through the array.
- **Space Complexity:** `O(1)` — Constant extra space.

---

Sure! Here's the **JavaScript version** for the **Smallest Sum Contiguous Subarray** problem:

---

### ✅ JavaScript Code:
```javascript
function smallestSubarraySum(arr) {
    let minSum = arr[0];
    let currSum = arr[0];

    for (let i = 1; i < arr.length; i++) {
        currSum = Math.min(arr[i], currSum + arr[i]);
        minSum = Math.min(minSum, currSum);
    }

    return minSum;
}
```

---

### 🧪 Example Usage:
```javascript
console.log(smallestSubarraySum([3, -4, 2, -3, -1, 7, -5])); // Output: -6
console.log(smallestSubarraySum([2, 6, 8, 1, 4]));           // Output: 1
```

---

### ⏱ Time & Space Complexity:
- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — constant space used.


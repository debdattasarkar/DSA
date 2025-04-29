Question

![Question](Question.png)

---
Alright! Let's **visually understand** the **XOR trick** 🔥:

---

### ⚡ XOR properties:
- `a ^ a = 0` → A number XOR itself cancels out.
- `a ^ 0 = a` → A number XOR 0 remains the same.
- XOR is **commutative and associative** (order doesn't matter).

---

### 🎯 Example:

Suppose we have the array:
```
arr = [1, 2, 3, 2, 3, 1, 3]
```

#### Step-by-step XOR:

| Step | Operation           | Result |
|-----|----------------------|--------|
| 1   | 0 ^ 1                | 1      |
| 2   | 1 ^ 2                | 3      |
| 3   | 3 ^ 3                | 0      |
| 4   | 0 ^ 2                | 2      |
| 5   | 2 ^ 3                | 1      |
| 6   | 1 ^ 1                | 0      |
| 7   | 0 ^ 3                | 3      |

✅ Final result = **3**

---

### 📈 Visual Flow:

```
Start: 0

0 ^ 1 = 1
1 ^ 2 = 3
3 ^ 3 = 0 (pair 3 cancels)
0 ^ 2 = 2
2 ^ 3 = 1
1 ^ 1 = 0 (pair 1 cancels)
0 ^ 3 = 3 (leftover 3)

Result: 3
```

✅ 3 appears **odd** number of times → Correct!

---

### 🔥 Why XOR works perfectly here?
Because:
- **Even number of same elements cancel** each other (`num ^ num = 0`).
- Only the **odd frequency number remains**!

---

Got it!  
This is the **Exceptionally Odd** problem.

---

### 🧠 Problem Understanding:

Given an array where:
- Every number appears **even** number of times,
- Except **one number** that appears **odd** number of times.

You must **find that exceptional number**.

---

### 🔥 Key Insight (Optimal Trick):
- If you XOR all elements together, **pairs cancel out** because:
  ```
  a ^ a = 0
  0 ^ b = b
  ```
- So at the end, **the leftover** will be the number that appeared odd times!

---

### ✅ Python Code:
```python
def getOddOccurrence(arr, n):
    result = 0
    for num in arr:
        result ^= num
    return result
```

---

### 🧪 Example Usage:
```python
print(getOddOccurrence([1, 2, 3, 2, 3, 1, 3], 7))  # Output: 3
print(getOddOccurrence([5, 7, 2, 7, 5, 2, 5], 7))  # Output: 5
```

---

### ⏱ Time & Space Complexity:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---
Of course! Here’s the **C++** and **JavaScript** versions of your provided **Python code**:

---

### ✅ C++ Code:
```cpp
#include <vector>
using namespace std;

int getOddOccurrence(const vector<int>& arr, int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        result ^= arr[i];
    }
    return result;
}
```

### 🧪 Example Usage in C++:
```cpp
#include <iostream>

int main() {
    vector<int> arr = {1, 2, 3, 2, 3, 1, 3};
    cout << getOddOccurrence(arr, arr.size()) << endl;  // Output: 3
}
```

---

### ✅ JavaScript Code:
```javascript
function getOddOccurrence(arr, n) {
    let result = 0;
    for (let num of arr) {
        result ^= num;
    }
    return result;
}
```

### 🧪 Example Usage in JavaScript:
```javascript
console.log(getOddOccurrence([1, 2, 3, 2, 3, 1, 3], 7));  // Output: 3
```

---

✅ All three versions (Python, C++, JavaScript) now match exactly and work perfectly for finding the **single odd-occurring number**!

Let me know if you want a **small practice problem** based on this XOR trick next! 🚀
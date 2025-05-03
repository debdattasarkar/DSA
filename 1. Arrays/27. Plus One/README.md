Thanks for sharing the problem about incrementing a number represented as an array of digits (i.e., **"Plus One"**).

Here’s a complete and clean solution in **Python**, **C++**, and **JavaScript**, including **inline comments** to help understand each step.

---

## ✅ Python Solution

```python
def increment(arr, N):
    # Traverse from the end to the start of the array
    for i in reversed(range(N)):
        if arr[i] < 9:
            arr[i] += 1  # Add 1 and stop if no carry needed
            return arr
        arr[i] = 0  # Set to 0 and continue to propagate the carry

    # If we exited the loop, all digits were 9 (e.g. 999 -> 1000)
    return [1] + [0] * N  # Add leading 1 and N zeroes

# Example usage
arr = [9, 9, 9]
print(increment(arr, len(arr)))  # Output: [1, 0, 0, 0]
```

---

## ✅ C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> increment(vector<int>& arr, int N) {
    // Traverse from last digit backwards
    for (int i = N - 1; i >= 0; --i) {
        if (arr[i] < 9) {
            arr[i]++;  // Simple increment
            return arr;
        }
        arr[i] = 0;  // Reset and carry continues
    }

    // All were 9s, need extra digit at front
    arr.insert(arr.begin(), 1);
    return arr;
}

int main() {
    vector<int> arr = {9, 9, 9};
    vector<int> res = increment(arr, arr.size());

    for (int x : res) cout << x << " ";
    return 0;
}
```

---

## ✅ JavaScript Solution

```javascript
function increment(arr, N) {
    // Loop from last digit to the start
    for (let i = N - 1; i >= 0; i--) {
        if (arr[i] < 9) {
            arr[i]++;
            return arr;
        }
        arr[i] = 0;  // Reset current digit and continue
    }

    // If all digits were 9, prepend 1
    return [1, ...Array(N).fill(0)];
}

// Example usage
let arr = [9, 9, 9];
console.log(increment(arr, arr.length));  // Output: [1, 0, 0, 0]
```

---

### ✅ Time and Space Complexity

* **Time**: O(N)
* **Space**: O(1) for in-place (excluding result in case of full carry)


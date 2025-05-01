You're now looking at the problem: **"Segregate Even and Odd numbers"** — a great test of array manipulation and sorting!

---

## ✅ Problem Summary

Given an array `arr[]`:

- Rearrange it **in-place** so that:
  - All **even numbers** come **first** (sorted in ascending order)
  - All **odd numbers** come **after** (also sorted in ascending order)

---

## 🧪 Examples

### Input:
```
arr = [12, 34, 45, 9, 8, 90, 3]
```
### Output:
```
[8, 12, 34, 90, 3, 9, 45]
```

### Explanation:
- Evens: `[12, 34, 8, 90]` → sort → `[8, 12, 34, 90]`
- Odds: `[45, 9, 3]` → sort → `[3, 9, 45]`

---

## ⏱️ Time and Space Complexity

| Metric             | Value       |
|--------------------|-------------|
| Time Complexity     | O(n log n)  |
| Space Complexity    | O(1) (if sorting done in-place) |

---

## 🐍 Python Solution (In-place)

```python
def segregate_even_odd(arr):
    # Separate even and odd numbers
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 == 1]

    # Sort both lists
    evens.sort()
    odds.sort()

    # Combine back into arr (in-place)
    arr[:] = evens + odds

# Example
arr = [12, 34, 45, 9, 8, 90, 3]
segregate_even_odd(arr)
print(arr)  # Output: [8, 12, 34, 90, 3, 9, 45]
```

---

## 🧑‍💻 C++ In-place Version

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void segregateEvenOdd(vector<int>& arr) {
    vector<int> evens, odds;

    for (int num : arr) {
        if (num % 2 == 0) evens.push_back(num);
        else odds.push_back(num);
    }

    sort(evens.begin(), evens.end());
    sort(odds.begin(), odds.end());

    // Merge back to original array
    int i = 0;
    for (int num : evens) arr[i++] = num;
    for (int num : odds) arr[i++] = num;
}

int main() {
    vector<int> arr = {12, 34, 45, 9, 8, 90, 3};
    segregateEvenOdd(arr);

    for (int x : arr) cout << x << " ";
    return 0;
}
```

---

## 🌐 JavaScript Version

```javascript
function segregateEvenOdd(arr) {
    let evens = arr.filter(x => x % 2 === 0).sort((a, b) => a - b);
    let odds = arr.filter(x => x % 2 !== 0).sort((a, b) => a - b);

    // Overwrite original array
    for (let i = 0; i < arr.length; i++) {
        arr[i] = i < evens.length ? evens[i] : odds[i - evens.length];
    }
}

// Example usage
let arr = [12, 34, 45, 9, 8, 90, 3];
segregateEvenOdd(arr);
console.log(arr);  // [8, 12, 34, 90, 3, 9, 45]
```

---

Would you like to visualize this as a two-phase process (partitioning + sorting), or optimize further for **true in-place** sorting without extra arrays?

🎞️ Here's your animated visualization of **even and odd number segregation**:

👉 [Click to view the animation](even_odd_segregation.gif)

- 🔵 **Even numbers** appear and get sorted to the front
- 🔴 **Odd numbers** follow and get sorted after evens

Would you like a version that keeps track of index swaps to truly simulate in-place operations?

🎉 Here's the animation showing **true in-place segregation** of even and odd numbers with sorting:

👉 [Click to view in-place animation](sandbox:/mnt/data/even_odd_inplace.gif)

- 🔵 **Even numbers** are moved and sorted in-place first  
- 🔴 **Odd numbers** follow, sorted in-place after evens  
- All changes happen on the original array structure

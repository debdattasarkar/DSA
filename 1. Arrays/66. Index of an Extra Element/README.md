Here's a **text explanation** with a **step-by-step dry run**, followed by working code in **Python**, **C++**, and **JavaScript** with inline comments.

---

## ✅ Problem Summary

You're given two **sorted** arrays:

* `arr1[]` of size `n`
* `arr2[]` of size `n - 1` (same as `arr1` but with **one element removed**)

### Task:

Find the **index** of the extra element in `arr1[]`.

---

## ✅ Dry Run Example

### Input:

```
arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8,    10, 12]
```

### Step-by-step:

* Compare both arrays element by element using binary search.
* At index `0`, `2 == 2`
* At index `1`, `4 == 4`
* At index `2`, `6 == 6`
* At index `3`, `8 == 8`
* At index `4`, `9 != 10` → ❗ Found mismatch

### Output:

```
4
```

---

## ✅ Python Code (With Comments)

```python
class Solution:
    def findExtra(self, a, b):
        low, high = 0, len(b)  # b is shorter by 1

        while low <= high:
            mid = (low + high) // 2
            # Check if elements differ or we've gone past b
            if mid >= len(b) or a[mid] != b[mid]:
                high = mid - 1  # mismatch is before or at mid
            else:
                low = mid + 1  # matched so far, search right

        return low  # 'low' ends at index of extra element
```

---

## ✅ C++ Code (With Inline Comments)

```cpp
class Solution {
  public:
    int findExtra(vector<int>& a, vector<int>& b) {
        int low = 0, high = b.size();  // b is one element shorter

        while (low <= high) {
            int mid = (low + high) / 2;

            // Either out of bounds or mismatch
            if (mid >= b.size() || a[mid] != b[mid]) {
                high = mid - 1;  // mismatch might be earlier
            } else {
                low = mid + 1;  // match, so go right
            }
        }
        return low;  // This is the index of extra element
    }
};
```

---

## ✅ JavaScript Code (With Inline Comments)

```javascript
class Solution {
    findExtra(a, b) {
        let low = 0, high = b.length; // b is shorter by 1

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            // Check if elements differ or we're past b
            if (mid >= b.length || a[mid] !== b[mid]) {
                high = mid - 1;  // mismatch could be earlier
            } else {
                low = mid + 1;  // match, move right
            }
        }

        return low;  // index of the extra element
    }
}
```

---

### ✅ Time & Space Complexity

* **Time Complexity:** `O(log n)` – due to binary search.
* **Space Complexity:** `O(1)` – constant extra space.

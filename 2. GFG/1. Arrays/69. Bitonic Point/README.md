To solve the **Bitonic Point** problem efficiently in `O(log n)` time, we can use a **modified binary search**. The idea is to find the maximum element in the array which is increasing and then decreasing (bitonic).

---

## 🔍 Step-by-Step Explanation

### Problem:

Find the **maximum element** in a **bitonic array** — one that increases and then decreases.

### Key Insight:

If `arr[mid] > arr[mid + 1] && arr[mid] > arr[mid - 1]`, then `arr[mid]` is the **bitonic point**.

Otherwise:

* If `arr[mid] > arr[mid + 1]`, we are in the **decreasing part**, so move `high = mid - 1`.
* If `arr[mid] < arr[mid + 1]`, we are in the **increasing part**, so move `low = mid + 1`.

---

## ✅ Python Code with Comments

```python
class Solution:

    def findMaximum(self, arr):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Handle boundary safely
            if mid > 0 and mid < len(arr) - 1:
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return arr[mid]
                elif arr[mid] > arr[mid - 1]:
                    # still increasing
                    low = mid + 1
                else:
                    # decreasing
                    high = mid - 1
            elif mid == 0:
                return max(arr[0], arr[1])
            elif mid == len(arr) - 1:
                return max(arr[-1], arr[-2])

        return -1  # unreachable if input is valid
```

---

## ✅ C++ Code with Comments

```cpp
class Solution {
  public:
    int findMaximum(vector<int> &arr) {
        int low = 0, high = arr.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (mid > 0 && mid < arr.size() - 1) {
                if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
                    return arr[mid];
                else if (arr[mid] > arr[mid - 1])
                    low = mid + 1;
                else
                    high = mid - 1;
            }
            else if (mid == 0) {
                return max(arr[0], arr[1]);
            }
            else if (mid == arr.size() - 1) {
                return max(arr[arr.size() - 1], arr[arr.size() - 2]);
            }
        }

        return -1; // fallback, though shouldn't happen per problem statement
    }
};
```

---

## ✅ JavaScript Code with Comments

```javascript
class Solution {
    findMaximum(arr) {
        let low = 0, high = arr.length - 1;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            if (mid > 0 && mid < arr.length - 1) {
                if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
                    return arr[mid];
                else if (arr[mid] > arr[mid - 1])
                    low = mid + 1;
                else
                    high = mid - 1;
            } else if (mid === 0) {
                return Math.max(arr[0], arr[1]);
            } else if (mid === arr.length - 1) {
                return Math.max(arr[arr.length - 1], arr[arr.length - 2]);
            }
        }

        return -1;
    }
}
```

---


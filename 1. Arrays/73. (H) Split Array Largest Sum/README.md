To solve the **Split Array Largest Sum** problem, we use **Binary Search** on the answer space combined with a **greedy validation** function.

---

### ✅ Problem Overview

**Goal:**
Split an array into `K` non-empty **contiguous** subarrays such that the **maximum subarray sum** among the `K` parts is **minimized**.

---

### 🔍 Dry Run (Example 1)

**Input:**
`arr = [1, 2, 3, 4]`, `K = 3`

**Optimal Split:**

* Split as `[1, 2]`, `[3]`, `[4]`
* Subarray sums = 3, 3, 4 → max = 4 ✅

---

### 💡 Key Idea: Binary Search + Greedy

**Why binary search?**
The answer lies between:

* **low = max(arr)** → can't have a split smaller than largest number
* **high = sum(arr)** → max possible when 1 subarray

We do binary search on this range and check feasibility.

#### 🧪 Feasibility Check:

* Try splitting array with current `mid` as max sum per part.
* If you need more than `K` parts → too small → search higher.
* Else → try lower.

---

### ✅ Python Implementation

```python
class Solution:
    def splitArray(self, arr, N, K):
        def isValid(mid):
            subarrays = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > mid:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return subarrays <= K

        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
```

---

### ✅ C++ Implementation

```cpp
class Solution {
  public:
    bool isValid(int arr[], int n, int k, int mid) {
        int subarrays = 1, curr_sum = 0;
        for (int i = 0; i < n; ++i) {
            if (curr_sum + arr[i] > mid) {
                subarrays++;
                curr_sum = arr[i];
            } else {
                curr_sum += arr[i];
            }
        }
        return subarrays <= k;
    }

    int splitArray(int arr[], int N, int K) {
        int low = *max_element(arr, arr + N);
        int high = accumulate(arr, arr + N, 0);
        int result = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isValid(arr, N, K, mid)) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return result;
    }
};
```

---

### ✅ JavaScript Implementation

```javascript
class Solution {
    splitArray(arr, N, K) {
        const isValid = (mid) => {
            let count = 1, curr_sum = 0;
            for (let num of arr) {
                if (curr_sum + num > mid) {
                    count++;
                    curr_sum = num;
                } else {
                    curr_sum += num;
                }
            }
            return count <= K;
        };

        let low = Math.max(...arr), high = arr.reduce((a, b) => a + b), result = high;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (isValid(mid)) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return result;
    }
}
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(N \* log(sum))
* **Space:** O(1)

Let me know if you'd like a diagram or interactive visualization of how binary search works in this case.

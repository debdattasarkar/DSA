### 🧠 Problem Summary: Painter’s Partition Problem - II

Given an array `arr[]` where `arr[i]` is the length of the `i-th` board and `k` painters, each taking 1 unit time per unit board length, find the **minimum time** to paint all boards **if each painter can only paint contiguous sections**.

---

### ✅ Key Insight:

We want to **minimize the maximum work assigned** to a painter under the constraint of **contiguous allocation**.

Use **binary search on the answer space** (between max(arr) and sum(arr)) and **greedily check** if `k` painters can paint within the guessed max time.

---

### 🧮 Dry Run Example:

```plaintext
arr = [5, 10, 30, 20, 15], k = 3

Search space: [30, 80]
Try mid = 55:
- Painter 1 -> 5+10+30 = 45 (ok)
- Painter 2 -> 20 (ok)
- Painter 3 -> 15 (ok) ✅ Works with 3 painters

Try lower: mid = 35:
- Painter 1 -> 5+10 = 15
- Painter 2 -> 30 (ok)
- Painter 3 -> 20+15 = 35 ✅ Just works

Try lower: mid = 34:
- Needs 4 painters ❌

Final answer = 35
```

---

### ✅ Python Code with Inline Comments

```python
class Solution:
    def minTime(self, arr, k):
        # Helper function to check if we can allocate boards to <= k painters
        def is_feasible(max_time):
            total, painters = 0, 1
            for length in arr:
                if total + length <= max_time:
                    total += length
                else:
                    painters += 1
                    total = length
            return painters <= k
        
        low = max(arr)           # A painter must at least paint the largest board
        high = sum(arr)         # One painter paints all
        result = high

        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                result = mid
                high = mid - 1  # Try to minimize further
            else:
                low = mid + 1   # Increase limit
        
        return result
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    bool isFeasible(vector<int>& arr, int k, int max_time) {
        int total = 0, painters = 1;
        for (int len : arr) {
            if (total + len <= max_time) {
                total += len;
            } else {
                painters++;
                total = len;
            }
        }
        return painters <= k;
    }

    int minTime(vector<int>& arr, int k) {
        int low = *max_element(arr.begin(), arr.end());
        int high = accumulate(arr.begin(), arr.end(), 0), result = high;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (isFeasible(arr, k, mid)) {
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

### ✅ JavaScript Code

```javascript
class Solution {
    isFeasible(arr, k, maxTime) {
        let total = 0, painters = 1;
        for (let len of arr) {
            if (total + len <= maxTime) {
                total += len;
            } else {
                painters++;
                total = len;
            }
        }
        return painters <= k;
    }

    minTime(arr, k) {
        let low = Math.max(...arr);
        let high = arr.reduce((a, b) => a + b, 0), result = high;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (this.isFeasible(arr, k, mid)) {
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

### 🕒 Time Complexity:

* Binary search range = `O(log(sum - max))`
* Feasibility check = `O(N)`
* **Overall = O(N \* log(sum))**

---

Let me know if you'd like the dry run or explanation visualized.

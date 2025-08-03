Here's a **text explanation**, **step-by-step dry run**, and full **Python, C++, and JavaScript implementations with inline comments** for the **Equilibrium Point** question:

---

### ✅ Problem Summary:

You are given an array of integers. Find an index (0-based) such that the sum of elements on the **left** is equal to the sum of elements on the **right**. If no such index exists, return `-1`.

---

### 🧠 Approach:

1. Compute the total sum of the array.
2. Iterate from left to right while maintaining the left sum.
3. At each index `i`, check:

   ```
   left_sum == total_sum - left_sum - arr[i]
   ```

   (i.e., sum of left == sum of right)
4. If so, return index `i`.
5. If no such index, return `-1`.

---

### 🪜 Dry Run:

Input: `arr = [-7, 1, 5, 2, -4, 3, 0]`
Total sum = `0`
Now, iterate:

* i = 0: left\_sum = 0 → 0 == 0 - (-7) → ❌
* i = 1: left\_sum = -7 → -7 == 0 - (-6) → ❌
* i = 2: left\_sum = -6 → -6 == -6 → ✅ return 2

---

### ✅ Python Implementation:

```python
class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i, val in enumerate(arr):
            # Check if left and right sums are equal
            if left_sum == total_sum - left_sum - val:
                return i
            left_sum += val

        return -1
```

---

### ✅ C++ Implementation:

```cpp
class Solution {
  public:
    int findEquilibrium(vector<int> &arr) {
        long long total_sum = accumulate(arr.begin(), arr.end(), 0LL);
        long long left_sum = 0;

        for (int i = 0; i < arr.size(); ++i) {
            // If left sum equals right sum, return index
            if (left_sum == total_sum - left_sum - arr[i]) {
                return i;
            }
            left_sum += arr[i];
        }
        return -1;
    }
};
```

---

### ✅ JavaScript Implementation:

```javascript
class Solution {
    findEquilibrium(arr) {
        let totalSum = arr.reduce((acc, val) => acc + val, 0);
        let leftSum = 0;

        for (let i = 0; i < arr.length; i++) {
            // Compare left and right sums
            if (leftSum === totalSum - leftSum - arr[i]) {
                return i;
            }
            leftSum += arr[i];
        }

        return -1;
    }
}
```

---
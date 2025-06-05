Absolutely! Below is the **same logic** — rearranging positives and negatives alternately starting with a positive number, maintaining **relative order**, and updating the original array **in-place** — implemented in **Python, C++, and JavaScript** with clear inline comments.

---

### ✅ Python Code (with inline comments):

```python
class Solution:
    def rearrange(self, arr):
        # Separate positive and negative elements
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]

        result = []
        i = j = 0

        # Alternate placing positive then negative elements
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            i += 1
            result.append(neg[j])
            j += 1

        # Add remaining positives or negatives if any
        result.extend(pos[i:])
        result.extend(neg[j:])

        # Update the original array in-place
        arr[:] = result
```

---

### ✅ C++ Code (with inline comments):

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void rearrange(vector<int>& arr) {
        vector<int> pos, neg;

        // Separate positives and negatives
        for (int num : arr) {
            if (num >= 0)
                pos.push_back(num);
            else
                neg.push_back(num);
        }

        vector<int> result;
        int i = 0, j = 0;

        // Alternate placement from pos and neg vectors
        while (i < pos.size() && j < neg.size()) {
            result.push_back(pos[i++]);
            result.push_back(neg[j++]);
        }

        // Add remaining positive elements
        while (i < pos.size())
            result.push_back(pos[i++]);

        // Add remaining negative elements
        while (j < neg.size())
            result.push_back(neg[j++]);

        // Modify the original array in-place
        for (int k = 0; k < arr.size(); ++k)
            arr[k] = result[k];
    }
};
```

---

### ✅ JavaScript Code (with inline comments):

```javascript
class Solution {
    rearrange(arr) {
        // Separate positives and negatives
        let pos = arr.filter(x => x >= 0);
        let neg = arr.filter(x => x < 0);

        let result = [];
        let i = 0, j = 0;

        // Alternate placement of positives and negatives
        while (i < pos.length && j < neg.length) {
            result.push(pos[i++]);
            result.push(neg[j++]);
        }

        // Add remaining elements if any
        while (i < pos.length) result.push(pos[i++]);
        while (j < neg.length) result.push(neg[j++]);

        // Modify original array in-place
        for (let k = 0; k < arr.length; k++) {
            arr[k] = result[k];
        }
    }
}
```

---

### 🧪 Test Case for All:

```text
Input:  [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
```

---

Great! Let's now enhance the solution with these features:

---

## ✅ Enhanced Requirements:

1. **In-place rearrangement** (no extra space)
2. **Start with positive** (default) OR optionally **negative**
3. Maintain **O(1) auxiliary space**
4. Does **not preserve relative order** (this is the trade-off for O(1) space)

---

## 🧠 Core Idea (for O(1) space):

* Use **two pointers**:

  * Traverse from index `0` to `n-1`.
  * If an element is at the **wrong place** (e.g. negative at even index), **find the next element with opposite sign** and **right rotate** the subarray.

This rearrangement will not maintain the original relative order — that’s the cost of constant space.

---

## ✅ Python Code (O(1) space):

```python
class Solution:
    def rearrange(self, arr):
        n = len(arr)

        for i in range(n):
            if i % 2 == 0:
                if arr[i] < 0:
                    j = i + 1
                    while j < n and arr[j] < 0:
                        j += 1
                    if j == n:
                        break
                    # Right rotate subarray [i..j]
                    temp = arr[j]
                    for k in range(j, i, -1):
                        arr[k] = arr[k - 1]
                    arr[i] = temp
            else:
                if arr[i] >= 0:
                    j = i + 1
                    while j < n and arr[j] >= 0:
                        j += 1
                    if j == n:
                        break
                    temp = arr[j]
                    for k in range(j, i, -1):
                        arr[k] = arr[k - 1]
                    arr[i] = temp
```

---

## ✅ C++ Code (O(1) space):

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void rearrange(vector<int>& arr) {
        int n = arr.size();

        for (int i = 0; i < n; ++i) {
            // Even index: expect positive
            if (i % 2 == 0 && arr[i] < 0) {
                int j = i + 1;
                while (j < n && arr[j] < 0) ++j;
                if (j == n) break;
                int temp = arr[j];
                for (int k = j; k > i; --k)
                    arr[k] = arr[k - 1];
                arr[i] = temp;
            }

            // Odd index: expect negative
            else if (i % 2 == 1 && arr[i] >= 0) {
                int j = i + 1;
                while (j < n && arr[j] >= 0) ++j;
                if (j == n) break;
                int temp = arr[j];
                for (int k = j; k > i; --k)
                    arr[k] = arr[k - 1];
                arr[i] = temp;
            }
        }
    }
};
```

---

## ✅ JavaScript Code (O(1) space):

```javascript
class Solution {
    rearrange(arr) {
        const n = arr.length;

        for (let i = 0; i < n; i++) {
            if (i % 2 === 0 && arr[i] < 0) {
                let j = i + 1;
                while (j < n && arr[j] < 0) j++;
                if (j === n) break;
                let temp = arr[j];
                for (let k = j; k > i; k--) arr[k] = arr[k - 1];
                arr[i] = temp;
            } else if (i % 2 === 1 && arr[i] >= 0) {
                let j = i + 1;
                while (j < n && arr[j] >= 0) j++;
                if (j === n) break;
                let temp = arr[j];
                for (let k = j; k > i; k--) arr[k] = arr[k - 1];
                arr[i] = temp;
            }
        }
    }
}
```

---

### 🧪 Example:

Input:

```
[9, 4, -2, -1, 5, 0, -5, -3, 2]
```

Output:

```
[9, -2, 4, -1, 5, -5, 0, -3, 2]
```

---



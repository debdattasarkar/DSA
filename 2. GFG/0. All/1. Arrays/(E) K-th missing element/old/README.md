Question

![Question](Question.png)

---

Sure! Here's a **text explanation** with a **step-by-step dry run** of the **“K-th missing element”** problem.

---

### 🔍 **Problem Summary**

Given a **strictly increasing array** `arr[]`, and an integer `k`, find the **k-th smallest missing number** starting from the **first element** of the array.

* If **no k-th missing element** exists, return **-1**.

---

### 🧠 **Concept**

In a perfect sequence starting at `arr[0]`, each element should be `arr[0] + i`.

So the number of **missing elements before `arr[i]`** is:

```python
missing_count = arr[i] - arr[0] - i
```

We iterate through the array to count how many values are missing. When the missing count becomes **≥ k**, the answer lies **before or at** index `i`.

---

### ✅ **Step-by-Step Dry Run**

#### Example:

```python
arr = [1, 3, 4, 5, 7], k = 2
```

#### Step 1: Initialize

* Start at index 1
* `missing_count = arr[i] - arr[0] - i`

---

#### Step 2: Compute missing at each step

| i | arr\[i] | arr\[0] + i | missing = arr\[i] - arr\[0] - i | total missing so far |
| - | ------- | ----------- | ------------------------------- | -------------------- |
| 1 | 3       | 2           | 3 - 1 - 1 = **1**               | 1                    |
| 2 | 4       | 3           | 4 - 1 - 2 = **1**               | 1                    |
| 3 | 5       | 4           | 5 - 1 - 3 = **1**               | 1                    |
| 4 | 7       | 5           | 7 - 1 - 4 = **2**               | ✅ Found at i = 4     |

---

#### Step 3: Find result in the gap

At index 4, we know the 2nd missing element lies between index 3 and 4:

* `arr[3] = 5`
* Missing numbers between 5 and 7: `[6]`

So, total missing up to 7 is 2, we want the **2nd** ⇒ `6`

---

### ✅ **Final Answer: `6`**

---

### 🧾 Formula for Final Answer

Once you find the index `i` such that:

```python
missing = arr[i] - arr[0] - i ≥ k
```

Then the answer is:

```python
result = arr[0] + k + i - 1
```

Or use:

```python
return arr[i - 1] + (k - missing_count_so_far)
```

---

Code implementation in Python, C++, or JavaScript:


Here are the **full implementations** of the **K-th missing element** problem in **Python, C++, and JavaScript**, with **inline comments** to explain the logic.

---

### ✅ Python Implementation

```python
class Solution:
    def KthMissingElement(self, arr, k):
        n = len(arr)

        for i in range(1, n):
            # Calculate how many numbers are missing between arr[i-1] and arr[i]
            missing = arr[i] - arr[i - 1] - 1

            if k <= missing:
                # If k is within the missing range, return the result
                return arr[i - 1] + k

            # Otherwise, skip these missing numbers
            k -= missing

        # If k-th missing is beyond the last element
        return -1

# Example usage
arr = [1, 3, 4, 5, 7]
k = 2
print(Solution().KthMissingElement(arr, k))  # Output: 6
```

---

### ✅ C++ Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int KthMissingElement(vector<int>& arr, int k) {
        int n = arr.size();

        for (int i = 1; i < n; ++i) {
            // Count how many numbers are missing between arr[i-1] and arr[i]
            int missing = arr[i] - arr[i - 1] - 1;

            if (k <= missing) {
                // The answer lies in this gap
                return arr[i - 1] + k;
            }

            // Skip over these missing numbers
            k -= missing;
        }

        // If not found within the array range
        return -1;
    }
};

// Example usage
int main() {
    Solution sol;
    vector<int> arr = {1, 3, 4, 5, 7};
    int k = 2;
    cout << sol.KthMissingElement(arr, k) << endl;  // Output: 6
    return 0;
}
```

---

### ✅ JavaScript Implementation

```javascript
class Solution {
    KthMissingElement(arr, k) {
        const n = arr.length;

        for (let i = 1; i < n; i++) {
            // Calculate missing numbers between arr[i-1] and arr[i]
            let missing = arr[i] - arr[i - 1] - 1;

            if (k <= missing) {
                // Found within this gap
                return arr[i - 1] + k;
            }

            // Move to next gap
            k -= missing;
        }

        // k-th missing doesn't exist within the array
        return -1;
    }
}

// Example usage
const arr = [1, 3, 4, 5, 7];
const k = 2;
const solution = new Solution();
console.log(solution.KthMissingElement(arr, k));  // Output: 6
```

---

Dry run on another example for this logic.

Here's a **step-by-step dry run** of the **K-th missing element** algorithm using the following example:

---

### 🔹 Input:

```plaintext
arr = [1, 3, 4, 5, 7]
k = 2
```

---

### 🔹 Goal:

Find the 2nd smallest number that is **missing** in the sequence starting from `arr[0]` and going forward.

---

### 🔹 Step-by-Step Flow:

#### Step 0: Initialize

* Start from the first index (`i = 1`)
* Initial `k = 2` (we need to find the 2nd missing number)

---

#### Step 1: Check between `arr[0]=1` and `arr[1]=3`

* Numbers between: `2`
* Missing count = `3 - 1 - 1 = 1`
* Since `k > 1`, skip this gap → `k = k - 1 = 1`

---

#### Step 2: Check between `arr[1]=3` and `arr[2]=4`

* No missing numbers
* Missing count = `4 - 3 - 1 = 0`
* `k = 1`, but no progress here → move to next

---

#### Step 3: Check between `arr[2]=4` and `arr[3]=5`

* No missing numbers
* Missing count = `5 - 4 - 1 = 0`
* `k = 1`, unchanged → move on

---

#### Step 4: Check between `arr[3]=5` and `arr[4]=7`

* Numbers between: `6`
* Missing count = `7 - 5 - 1 = 1`
* Now, `k = 1 <= 1`, so we found our missing number:

👉 **Result = 5 + 1 = 6**

---

### ✅ Final Output:

```plaintext
6
```

---
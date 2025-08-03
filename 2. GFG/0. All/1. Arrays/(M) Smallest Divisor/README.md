---

# 📘 Smallest Divisor

**Difficulty:** Medium

---

## 🧩 Problem Statement

You are given an integer array `arr[]` and an integer `k` (where `k ≥ arr.length`). Find the **smallest positive integer divisor** such that the **sum of the ceiling values** of each element in `arr[]` divided by this divisor is less than or equal to `k`.

---

## 🧪 Examples

### Example 1:

```
Input: 
arr[] = [1, 2, 5, 9], k = 6

Output:
5

Explanation:
ceil(1/5) + ceil(2/5) + ceil(5/5) + ceil(9/5)
= 1 + 1 + 1 + 2 = 5, which is ≤ 6
```

---

### Example 2:

```
Input:
arr[] = [1, 1, 1, 1], k = 4

Output:
1

Explanation:
ceil(1/1) + ceil(1/1) + ceil(1/1) + ceil(1/1)
= 1 + 1 + 1 + 1 = 4, which is ≤ 4
```

---

## ✅ Constraints

* `1 ≤ arr.length ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^6`
* `arr.length ≤ k ≤ 10^6`

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n \* log(max(arr\[i])))
* **Auxiliary Space:** O(1)

---

## 💡 Key Observations

* The higher the divisor, the smaller the sum of ceilings.
* Use **binary search** between `1` and `max(arr)` to find the smallest divisor that satisfies the condition.
* For each mid divisor, check if `sum(ceil(arr[i]/mid)) ≤ k`.

---

## 🔍 Tags

* Binary Search
* Arrays
* Algorithms

---

## 🔗 Related Articles

* [Smallest Divisor for Sum Constraint in Array Division](https://www.geeksforgeeks.org/smallest-divisor-for-sum-constraint-in-array-division/)

---
Sure! Here's the full explanation with a **step-by-step dry run** and the **code** in Python, C++, and JavaScript for the **"Smallest Divisor"** problem from GeeksforGeeks.

---

## 🧠 Problem Understanding

You are given an array `arr[]` and an integer `k`. You need to find the **smallest integer divisor** such that the **sum of all ceil(arr\[i] / divisor)** ≤ `k`.

---

## 🧩 Approach

We can use **binary search** to solve this problem efficiently.

### ✅ Key Observations:

* If we increase the divisor, the result of `ceil(arr[i] / divisor)` decreases.
* So, the **sum of all ceilings is a decreasing function** with respect to the divisor.
* We can apply **binary search** on the divisor in the range \[1, max(arr)].

---

## 🔍 Step-by-Step Dry Run

### Example:

```
arr = [1, 2, 5, 9]
k = 6
```

**Initial search space**: `left = 1`, `right = 9` (max(arr))

### Try mid = 5

* ceil(1/5) = 1
* ceil(2/5) = 1
* ceil(5/5) = 1
* ceil(9/5) = 2
* sum = 1+1+1+2 = 5 ≤ 6 → valid
* shrink right → right = 5

### Try mid = 3

* ceil(1/3) = 1
* ceil(2/3) = 1
* ceil(5/3) = 2
* ceil(9/3) = 3
* sum = 7 > 6 → invalid
* move left → left = 4

### Try mid = 4

* ceil(1/4) = 1
* ceil(2/4) = 1
* ceil(5/4) = 2
* ceil(9/4) = 3
* sum = 7 > 6 → invalid
* move left → left = 5

Now `left == right == 5` → smallest valid divisor = **5**

---

## ✅ Python Code

```python
import math

class Solution:
    def smallestDivisor(self, arr, k):
        def is_valid(divisor):
            return sum(math.ceil(x / divisor) for x in arr) <= k

        left, right = 1, max(arr)
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid  # try smaller divisor
            else:
                left = mid + 1  # increase divisor

        return left
```

---

## ✅ C++ Code

```cpp
#include <vector>
#include <cmath>
using namespace std;

class Solution {
  public:
    int smallestDivisor(vector<int>& arr, int k) {
        auto is_valid = [&](int divisor) {
            int total = 0;
            for (int num : arr)
                total += (num + divisor - 1) / divisor; // ceil division
            return total <= k;
        };

        int left = 1, right = *max_element(arr.begin(), arr.end());
        while (left < right) {
            int mid = (left + right) / 2;
            if (is_valid(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    smallestDivisor(arr, k) {
        const isValid = (divisor) => {
            let total = 0;
            for (let num of arr) {
                total += Math.ceil(num / divisor);
            }
            return total <= k;
        };

        let left = 1, right = Math.max(...arr);
        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (isValid(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

---

Sure! Let's do a **visual dry run in grid format** (table-style) for the **"Smallest Divisor"** problem using this input:

---

### **🧪 Example Input**

```
arr = [1, 2, 5, 9]
k = 6
```

We want to find the **smallest divisor** such that:

```
ceil(1/div) + ceil(2/div) + ceil(5/div) + ceil(9/div) ≤ 6
```

---

### 🔎 **Binary Search Table Dry Run**

| Step | left | right | mid | Ceil Sums with mid | Valid (≤ k)? | Action       |
| ---- | ---- | ----- | --- | ------------------ | ------------ | ------------ |
| 1    | 1    | 9     | 5   | 1+1+1+2 = 5        | ✅ Yes        | right = 5    |
| 2    | 1    | 5     | 3   | 1+1+2+3 = 7        | ❌ No         | left = 4     |
| 3    | 4    | 5     | 4   | 1+1+2+3 = 7        | ❌ No         | left = 5     |
| 4    | 5    | 5     | -   | -                  | ✅ Stop       | Found answer |

---

### ✅ **Answer: `5`**

That’s the **smallest divisor** where the sum of ceilings is ≤ `k`.

---

### ⏱ Time Complexity

* **Binary Search** over `divisor` from `1` to `max(arr)` → `log(max)`
* For each guess, we do a linear pass to compute ceil sum → `O(n)`
* So total: **O(n \* log(max(arr)))**

---

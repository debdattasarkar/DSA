
---

# Minimize the Heights I

**Difficulty**: Medium
**Accuracy**: 26.16%
**Submissions**: 120K+
**Points**: 4
**Average Time**: 25m

---

## Problem Statement

Given an array `arr[]` and a positive integer `k` denoting heights of towers, you have to modify the height of each tower either by increasing or decreasing them by `k` **only once**.

Find out what could be the possible **minimum difference** of the height of **shortest** and **longest** towers after you have modified each tower. The modified height of the tower can be negative.

> **Note**: A slight modification of the problem can be found [here](https://practice.geeksforgeeks.org/problems/minimize-the-heights-ii/1).

---

## Examples

### Example 1:

```
Input: arr[] = [1, 5, 8, 10], k = 2  
Output: 5  
Explanation: The array can be modified as [3, 3, 6, 8].  
The difference between the largest and the smallest is 8 - 3 = 5.
```

### Example 2:

```
Input: arr[] = [3, 9, 12, 16, 20], k = 3  
Output: 11  
Explanation: The array can be modified as [6, 12, 9, 13, 17].  
The difference between the largest and the smallest is 17 - 6 = 11.
```

---

## Constraints

* $1 \leq k \leq 10^4$
* $1 \leq \text{number of towers} \leq 10^5$
* $0 \leq \text{arr}[i] \leq 10^5$

---

## Expected Complexities

* **Time Complexity**: $O(n \log n)$
* **Auxiliary Space**: $O(1)$

---

## Company Tags

`Adobe`

---

## Topic Tags

* `two-pointer-algorithm`
* `Arrays`
* `Greedy`
* `Data Structures`
* `Algorithms`

---
You're absolutely right — and thank you for sharing the correct and clean implementation. ✅
You're using the **most optimal and interviewer-expected version** of the solution. Let's break this down and document it thoroughly so it can serve as a solid reference.

---

## ✅ Minimize the Heights I — README Style

### Problem Statement

You are given an array `arr[]` and a positive integer `k`.
Your task is to **modify each element only once**, by either increasing or decreasing it by `k`, and then **minimize the difference** between the maximum and minimum elements in the modified array.

---

### Constraints

* `1 ≤ k ≤ 10⁴`
* `1 ≤ number of towers ≤ 10⁵`
* `0 ≤ arr[i] ≤ 10⁵`
* Time: `O(n log n)`
* Space: `O(1)`

---

### Examples

#### Input:

```
arr = [1, 5, 8, 10]
k = 2
```

#### Output:

```
5
```

#### Explanation:

* Modify the array as `[3, 3, 6, 8]`
* Max = 8, Min = 3 → Diff = 5

---

### ✅ Optimal Code (Python)

```python
#User function Template for python3

class Solution:
    def getMinDiff(self,arr,k):
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()
        diff = arr[-1] - arr[0]  # Initial difference

        for i in range(n - 1):
            # min and max values after modifying elements
            low = min(arr[0] + k, arr[i + 1] - k)
            high = max(arr[-1] - k, arr[i] + k)
            diff = min(diff, high - low)

        return diff
```

---

### 📊 Dry Run (with example: arr = \[1, 5, 8, 10], k = 2)

| i | arr\[i] | arr\[i+1] | low = min(arr\[0]+k, arr\[i+1]-k) | high = max(arr\[-1]-k, arr\[i]+k) | high - low |
| - | ------- | --------- | --------------------------------- | --------------------------------- | ---------- |
| 0 | 1       | 5         | min(3, 3) = 3                     | max(8, 3) = 8                     | 5          |
| 1 | 5       | 8         | min(3, 6) = 3                     | max(8, 7) = 8                     | 5          |
| 2 | 8       | 10        | min(3, 8) = 3                     | max(8, 10) = 10                   | 7          |

* ✅ Final Answer: `min(5, 5, 7) = 5`

---

### ✅ C++ Version

```cpp
class Solution {
  public:
    int getMinDiff(vector<int> &arr, int k) {
        int n = arr.size();
        if (n == 1) return 0;
        sort(arr.begin(), arr.end());
        int diff = arr[n-1] - arr[0];

        for (int i = 0; i < n - 1; i++) {
            int low = min(arr[0] + k, arr[i + 1] - k);
            int high = max(arr[n - 1] - k, arr[i] + k);
            diff = min(diff, high - low);
        }
        return diff;
    }
};
```

---

### ✅ JavaScript Version

```javascript
class Solution {
    getMinDiff(arr, k) {
        arr.sort((a, b) => a - b);
        let n = arr.length;
        if (n === 1) return 0;

        let diff = arr[n - 1] - arr[0];

        for (let i = 0; i < n - 1; i++) {
            let low = Math.min(arr[0] + k, arr[i + 1] - k);
            let high = Math.max(arr[n - 1] - k, arr[i] + k);
            diff = Math.min(diff, high - low);
        }

        return diff;
    }
}
```

---

If you'd like, I can also generate a **flowchart** for this logic or explain potential follow-up questions for interviews.

Thanks again for holding the bar high — it's how these answers get better.

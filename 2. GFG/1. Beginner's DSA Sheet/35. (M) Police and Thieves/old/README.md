
---

# Police and Thieves 🕵️‍♂️🦹‍♀️

**Difficulty:** Medium
**Accuracy:** 34.03%
**Submissions:** 32K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given an array `arr[]`, where each element contains either a **'P'** for policeman or a **'T'** for thief, find the **maximum number of thieves** that can be caught by the police.

**Rules:**

1. Each policeman can catch **only one** thief.
2. A policeman **cannot catch a thief** who is more than **k units** away from him.

---

## Examples

### Example 1:

```
Input:
arr[] = ['P', 'T', 'T', 'P', 'T'], k = 1

Output:
2

Explanation:
- First policeman catches first thief
- Second policeman can catch either second or third thief
```

---

### Example 2:

```
Input:
arr[] = ['T', 'T', 'P', 'P', 'T', 'P'], k = 2

Output:
3

Explanation:
- Maximum 3 thieves can be caught.
```

---

## Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $1 \leq k \leq 1000$
* arr\[i] = 'P' or 'T'

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## Company Tags

* Microsoft

---

## Topic Tags

* Greedy
* Algorithms

---

## Related Articles

* [Policemen Catch Thieves](https://www.geeksforgeeks.org/policemen-catch-thieves/)

---

Here's a complete README-style breakdown with **step-by-step explanation**, **optimized code**, and **expected interview questions with answers** for the problem **"Police and Thieves"**:

---

## 🕵️‍♂️ Police and Thieves – Detailed Explanation

### ❓ Problem Summary

Given an array of `'P'` and `'T'`, and an integer `k`, each policeman `'P'` can catch at most one thief `'T'` within distance `k` to the left or right. Find the **maximum number of thieves** that can be caught.

### ✅ Rules:

* One police can catch only one thief.
* A thief can be caught **only if** within distance ≤ `k`.

---

### 🔍 Step-by-Step Dry Run

#### Input:

```
arr = ['T', 'T', 'P', 'P', 'T', 'P'], k = 2
```

#### Process:

1. Maintain two lists:

   * `police_positions = []`
   * `thief_positions = []`

2. Traverse the array and store indexes of `'P'` and `'T'`.

   ```
   thief_positions = [0, 1, 4]
   police_positions = [2, 3, 5]
   ```

3. Use two pointers `i`, `j` to iterate over `thief_positions` and `police_positions`.

   ```
   i = 0, j = 0
   |2 - 0| = 2 <= k => count = 1, i++, j++
   |3 - 1| = 2 <= k => count = 2, i++, j++
   |5 - 4| = 1 <= k => count = 3, i++, j++
   ```

✔ Final Count: `3`

---

## ✅ Optimized Code

### Python 🐍

```python
class Solution:
    def catchThieves(self, arr, k):
        n = len(arr)
        thieves = []
        police = []
        count = 0

        for i in range(n):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thieves.append(i)

        i = j = 0
        while i < len(thieves) and j < len(police):
            if abs(thieves[i] - police[j]) <= k:
                count += 1
                i += 1
                j += 1
            elif thieves[i] < police[j]:
                i += 1
            else:
                j += 1

        return count
```

---

### C++ 🇨++

```cpp
class Solution {
  public:
    int catchThieves(vector<char> &arr, int k) {
        int n = arr.size(), count = 0;
        vector<int> police, thieves;

        for (int i = 0; i < n; ++i) {
            if (arr[i] == 'P') police.push_back(i);
            else if (arr[i] == 'T') thieves.push_back(i);
        }

        int i = 0, j = 0;
        while (i < thieves.size() && j < police.size()) {
            if (abs(thieves[i] - police[j]) <= k) {
                count++;
                i++; j++;
            } else if (thieves[i] < police[j]) {
                i++;
            } else {
                j++;
            }
        }

        return count;
    }
};
```

---

### JavaScript 🟨

```javascript
class Solution {
    catchThieves(arr, k) {
        let police = [], thieves = [], count = 0;

        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === 'P') police.push(i);
            else if (arr[i] === 'T') thieves.push(i);
        }

        let i = 0, j = 0;
        while (i < thieves.length && j < police.length) {
            if (Math.abs(thieves[i] - police[j]) <= k) {
                count++;
                i++; j++;
            } else if (thieves[i] < police[j]) {
                i++;
            } else {
                j++;
            }
        }

        return count;
    }
}
```

---

## 💡 Interview Follow-up Questions (with Answers)

### Q1. What’s the time and space complexity?

**A:**

* Time: O(n)
* Space: O(n) for storing positions of police and thieves.

---

### Q2. What would be a brute-force solution?

**A:**
Try every combination of police and thieves with nested loops and distance check → O(n²) time.

---

### Q3. What if all elements were `'T'` or all `'P'`?

**A:**
Edge case → return `0`, since no pairs possible.

---

### Q4. How would you test this function in production?

**A:**

* Use randomized tests of varying sizes.
* Edge tests like no thieves, no police, `k=0`, or `k >= len(arr)`.

---

### Q5. Can this be done in-place?

**A:**
Yes, we can avoid extra lists and use queues or two-pointer walk during traversal.

---


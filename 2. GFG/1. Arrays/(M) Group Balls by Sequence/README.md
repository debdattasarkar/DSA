Here's the complete README-style conversion for the problem **"Group Balls by Sequence"** based on the image:

---

# Group Balls by Sequence

**Difficulty:** Medium
**Accuracy:** 48.46%
**Submissions:** 14K+
**Points:** 4

---

## Problem Statement

You are given an array `arr[]` of positive integers, where each element `arr[i]` represents the number written on the *i-th ball*, and a positive integer `k`.

Your task is to determine whether it is possible to rearrange all the balls into groups such that:

* Each group contains exactly `k` balls.
* The numbers in each group are **consecutive integers**.

---

## Examples

### Example 1:

**Input:**
`arr[] = [10, 1, 2, 11]`, `k = 2`
**Output:**
`true`
**Explanation:**
The hand can be rearranged as `[1, 2]`, `[10, 11]`.
There are two groups of size 2. Each group has 2 consecutive cards.

---

### Example 2:

**Input:**
`arr[] = [7, 8, 9, 10, 11]`, `k = 2`
**Output:**
`false`
**Explanation:**
The hand cannot be rearranged into groups of 2, since there are 5 cards, and 5 cards cannot be divided into groups of 2.

---

## Constraints

* `1 ≤ arr.size() ≤ 10⁶`
* `0 ≤ arr[i] ≤ 10⁵`
* `1 ≤ k ≤ 10³`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Related Articles

* [Group Balls by Sequence](https://www.geeksforgeeks.org/problems/group-balls-by-sequence/)

---

Here's the complete explanation, dry run, optimized implementations, and expected interview Q\&A for the **"Group Balls by Sequence"** problem.

---

## 🧠 Problem Summary

Given an array `arr[]` of positive integers and an integer `k`, determine if it's possible to group all elements such that:

* Each group has exactly `k` elements.
* The elements in each group are **consecutive integers**.

---

## 🔍 Step-by-Step Explanation

1. **Sort the array** – because to form consecutive groups, sorted order helps in easy access.
2. **Use a frequency map** (or Counter) to keep track of how many of each number exist.
3. **For each number `num` in the sorted array**:

   * If its count is zero, skip it (already used in a group).
   * Otherwise, try to form a group starting at `num` of length `k`:

     * For each `num + i` where `i` in `[0, k-1]`, check if it exists in the map with sufficient count.
     * If not, return `False`.
     * Otherwise, decrement the count for those numbers.

---

## 🔢 Dry Run Example

**Input:** `arr = [1, 2, 3, 6, 2, 3, 4, 7, 8]`, `k = 3`
**Sorted:** `[1, 2, 2, 3, 3, 4, 6, 7, 8]`

### Pass 1: Start with 1

→ Form group `[1,2,3]`
→ Frequencies of 1,2,3 reduce.

### Pass 2: Next smallest = 2

→ Form `[2,3,4]`
→ Frequencies reduce.

### Pass 3: Next = 6

→ Form `[6,7,8]`
→ All frequencies used.

✅ Return `True`

---

## ✅ Python Implementation

```python
from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False

        arr.sort()
        freq = Counter(arr)

        for num in arr:
            if freq[num] == 0:
                continue

            # Try to form a group starting at num
            for i in range(k):
                if freq[num + i] == 0:
                    return False
                freq[num + i] -= 1

        return True
```

---

## ✅ C++ Implementation

```cpp
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
  public:
    bool validgroup(vector<int>& arr, int k) {
        if (arr.size() % k != 0) return false;

        map<int, int> freq;
        for (int num : arr) freq[num]++;

        for (auto [num, count] : freq) {
            if (count == 0) continue;
            for (int i = 0; i < k; ++i) {
                if (freq[num + i] < count) return false;
                freq[num + i] -= count;
            }
        }

        return true;
    }
};
```

---

## ✅ JavaScript Implementation

```javascript
class Solution {
    validgroup(arr, k) {
        if (arr.length % k !== 0) return false;

        arr.sort((a, b) => a - b);
        const freq = new Map();

        for (let num of arr) {
            freq.set(num, (freq.get(num) || 0) + 1);
        }

        for (let num of arr) {
            if (freq.get(num) === 0) continue;

            for (let i = 0; i < k; i++) {
                let curr = num + i;
                if (!freq.has(curr) || freq.get(curr) === 0) return false;
                freq.set(curr, freq.get(curr) - 1);
            }
        }

        return true;
    }
}
```

---

## 📘 Expected Interview Questions

### Q1: Why do we need to sort the array?

**A:** Sorting allows us to check for consecutive group formations easily and maintain group order starting from the smallest unused element.

---

### Q2: What is the time complexity?

**A:**

* Sorting: O(n log n)
* Group formation: O(n)
  → **Total:** `O(n log n)`

---

### Q3: Can this solution handle large arrays efficiently?

**A:** Yes. The use of a hash map (`Counter` / `Map`) for frequency ensures constant-time access, making it scalable to large input sizes.

---

### Q4: What edge cases should you test for?

* `arr = []` and `k = 1` → invalid
* Array with all same numbers → valid if divisible by `k`
* Arrays with random gaps → invalid
* `k = 1` → each element forms its own group

---

### Q5: What if duplicates exist?

**A:** Handled using frequency counts. Each group formation checks and decrements frequency, supporting duplicates properly.

---


---

# 📘 Array Subset

### Difficulty: Basic

**Accuracy:** 44.05%
**Submissions:** 446K+
**Points:** 1
**Average Time:** 20m

---

## 📝 Problem Statement

Given two arrays **a\[]** and **b\[]**, your task is to determine whether **b\[] is a subset of a\[]**.

---

## 🔍 Examples

### Example 1:

```
Input:
a[] = [11, 7, 1, 13, 21, 3, 7, 3]
b[] = [11, 3, 7, 1, 7]

Output: true

Explanation: b[] is a subset of a[]
```

### Example 2:

```
Input:
a[] = [1, 2, 3, 4, 4, 5, 6]
b[] = [1, 2, 4]

Output: true

Explanation: b[] is a subset of a[]
```

### Example 3:

```
Input:
a[] = [10, 5, 2, 23, 19]
b[] = [19, 5, 3]

Output: false

Explanation: b[] is not a subset of a[]
```

---

## ✅ Constraints

* 1 ≤ a.size(), b.size() ≤ 10⁵
* 1 ≤ a\[i], b\[j] ≤ 10⁶

---

## 🧠 Expected Complexities

* **Time Complexity:** O(n + m)
* **Auxiliary Space:** O(n)

---

## 💡 Explanation + Step-by-Step Dry Run

### Approach: Frequency Hash Map

Use a frequency map to count elements in `a[]`, then check if all elements in `b[]` exist with enough frequency.

### Dry Run Example:

Let:

```
a = [1, 2, 3, 4, 4, 5, 6]  
b = [1, 2, 4]
```

#### Step 1: Build frequency map from `a`

```
freq = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 1,
    6: 1
}
```

#### Step 2: Check each element in `b` against the map

* b\[0] = 1 → exists → decrement count
* b\[1] = 2 → exists → decrement count
* b\[2] = 4 → exists → decrement count

All elements found, so **b is a subset of a**.

---

## 🐍 Python Implementation

```python
# User function Template for python3

class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):
        from collections import Counter

        freq = Counter(a)  # Count frequencies of a[]

        for num in b:
            if freq[num] == 0:
                return False  # Not found or exhausted
            freq[num] -= 1  # Use one occurrence
        
        return True
```

---

## 💠 C++ Implementation

```cpp
#include <unordered_map>
using namespace std;

class Solution {
  public:
    // Function to check if b is a subset of a
    bool isSubset(vector<int> &a, vector<int> &b) {
        unordered_map<int, int> freq;

        for (int num : a)
            freq[num]++;

        for (int num : b) {
            if (freq[num] == 0)
                return false;
            freq[num]--;
        }

        return true;
    }
};
```

---

## 🌐 JavaScript Implementation

```javascript
class Solution {
    // Function to check if b is a subset of a
    isSubset(a, b) {
        let freq = {};

        // Count frequencies of a[]
        for (let num of a) {
            freq[num] = (freq[num] || 0) + 1;
        }

        // Check if b[] is a subset
        for (let num of b) {
            if (!freq[num]) return false;
            freq[num]--;
        }

        return true;
    }
}
```

---

## 💬 Expected Interview Questions & Answers

---

### ❓ Q1: Can we solve this without extra space?

**A:** Yes, by sorting both arrays and using two-pointer technique, but that would cost O(n log n) time instead of O(n) with hashmap.

---

### ❓ Q2: What if duplicates are present in `b[]` but not enough in `a[]`?

**A:** Our hash-based solution accounts for frequency, so duplicates are properly handled.

---

### ❓ Q3: Can we solve this in O(1) space?

**A:** Only if elements fall in a small fixed range (e.g., 0 to 100), then a fixed-size frequency array can be used instead of a hash map.

---

### ❓ Q4: What if arrays are huge but sorted?

**A:** Then a two-pointer approach on sorted arrays works in O(n + m) time and O(1) space.

---

### ❓ Q5: What's the real-world use of subset checking?

**A:** It’s useful in permission systems, inventory validation, and search filtering (e.g., verifying if all requested items exist in stock).

---

## 🏢 Company Tags

* `Accolite`, `Qualcomm`, `GE`

## 🏷 Topic Tags

* `Arrays`, `Searching`, `Hash`, `Binary Search`, `Data Structures`, `Algorithms`

## 📚 Related Articles

* [Find Whether An Array Is Subset Of Another Array Set 1](https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/)

---

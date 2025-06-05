# 📊 Count Smaller Elements
---

## 🧾 Problem Statement

Given an array `arr` containing non-negative integers, return an array `res` such that:

* `res[i]` = Number of elements **smaller than `arr[i]`** present **to the right** of index `i`.

---

## 🧪 Examples

### Example 1:

```text
Input: arr[] = [12, 1, 2, 3, 0, 11, 4]  
Output: [6, 1, 1, 1, 0, 1, 0]  

Explanation:  
- There are 6 smaller elements after 12.  
- 1 smaller after 1 → [0]  
- 1 smaller after 2 → [0]  
- And so on.
```

### Example 2:

```text
Input: arr[] = [1, 2, 3, 4, 5]  
Output: [0, 0, 0, 0, 0]  

Explanation:  
- All elements are in ascending order, so no element has smaller elements to its right.
```

---

## 📌 Constraints

* 1 ≤ `arr.length` ≤ 10⁶
* 0 ≤ `arr[i]` ≤ 10⁸

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

* Google
* Codentation

---

## 🏷️ Tags

`Arrays` `Sorting` `Binary Search` `Data Structures` `Algorithms`

---

## 📚 Related Articles

* [Count Smaller Elements on Right Side - GeeksforGeeks](#)

---

Here’s a full explanation with **step-by-step dry run** and implementations for **Count Smaller Elements on Right Side** using **Binary Indexed Tree (Fenwick Tree)** approach, which meets the required `O(n log n)` time complexity.

---

## 🧠 Problem Understanding

We are given an array `arr`. For each index `i`, we want to count how many elements to the **right** of `i` are **less than `arr[i]`**.

---

## 🪜 Step-by-Step Dry Run

### Input:

```text
arr = [12, 1, 2, 3, 0, 11, 4]
```

### Output:

```text
[6, 1, 1, 1, 0, 1, 0]
```

### Explanation:

* For 12 → \[1, 2, 3, 0, 11, 4] → 6 smaller
* For 1 → \[2, 3, 0, 11, 4] → 1 smaller
* For 2 → \[3, 0, 11, 4] → 1 smaller
* ...

---

## 🧩 Approach: Binary Indexed Tree (Fenwick Tree)

### Key Steps:

1. **Coordinate compression**
   Because `arr[i]` can go up to 10⁸, we need to **compress values to a smaller index range** for BIT usage.

2. **Traverse array from right to left**
   At each step, query the BIT to find count of smaller elements seen so far.

3. **Use BIT to track frequency of elements** as you go.

---

## ✅ Python Code

```python
# User function Template for python3
class Solution:

    def constructLowerArray(self, arr):
        def update(index, bit):
            while index < len(bit):
                bit[index] += 1
                index += index & -index

        def query(index, bit):
            result = 0
            while index > 0:
                result += bit[index]
                index -= index & -index
            return result

        # Coordinate compression
        sorted_unique = sorted(set(arr))
        index_map = {val: i+1 for i, val in enumerate(sorted_unique)}  # 1-based indexing for BIT

        bit = [0] * (len(sorted_unique) + 2)
        res = []

        # Traverse from right to left
        for num in reversed(arr):
            idx = index_map[num]
            res.append(query(idx - 1, bit))  # count of smaller elements
            update(idx, bit)

        return res[::-1]  # reverse to restore original order
```

---

## 💠 C++ Code

```cpp
// User function Template for C++

class Solution {
  public:
    vector<int> constructLowerArray(vector<int> &arr) {
        int n = arr.size();
        vector<int> temp = arr;
        sort(temp.begin(), temp.end());
        unordered_map<int, int> index_map;

        int idx = 1;
        for (int val : temp) {
            if (index_map.count(val) == 0)
                index_map[val] = idx++;
        }

        vector<int> BIT(idx + 1, 0);
        vector<int> res(n);

        auto update = [&](int i) {
            while (i < BIT.size()) {
                BIT[i]++;
                i += (i & -i);
            }
        };

        auto query = [&](int i) {
            int ans = 0;
            while (i > 0) {
                ans += BIT[i];
                i -= (i & -i);
            }
            return ans;
        };

        for (int i = n - 1; i >= 0; i--) {
            int compressed = index_map[arr[i]];
            res[i] = query(compressed - 1);
            update(compressed);
        }

        return res;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
// User function Template for javascript

class Solution {
    constructLowerArray(arr) {
        const n = arr.length;

        // Coordinate compression
        const sorted = Array.from(new Set(arr)).sort((a, b) => a - b);
        const indexMap = new Map();
        for (let i = 0; i < sorted.length; i++) {
            indexMap.set(sorted[i], i + 1); // 1-based index
        }

        const BIT = Array(sorted.length + 2).fill(0);
        const res = [];

        const update = (i) => {
            while (i < BIT.length) {
                BIT[i]++;
                i += i & -i;
            }
        };

        const query = (i) => {
            let sum = 0;
            while (i > 0) {
                sum += BIT[i];
                i -= i & -i;
            }
            return sum;
        };

        // Traverse right to left
        for (let i = n - 1; i >= 0; i--) {
            const idx = indexMap.get(arr[i]);
            res.push(query(idx - 1));
            update(idx);
        }

        return res.reverse();
    }
}
```

---

## 🚀 Time and Space Complexity

| Type  | Complexity |
| ----- | ---------- |
| Time  | O(n log n) |
| Space | O(n)       |

---

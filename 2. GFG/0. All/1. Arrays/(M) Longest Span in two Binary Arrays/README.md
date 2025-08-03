
# 📏 Longest Span in Two Binary Arrays

---

## 🧾 Problem Statement

Given two binary arrays, `a1[]` and `a2[]`, find the **length of the longest common span (i, j)** where `j ≥ i` such that:

```
a1[i] + a1[i+1] + ... + a1[j] == a2[i] + a2[i+1] + ... + a2[j]
```

---

## 🧪 Examples

### Example 1:

```text
Input:
a1 = [0, 1, 0, 0, 0], a2 = [1, 0, 1, 0, 0]

Output:
4

Explanation:
The longest span with same sum is from index 1 to 4 (0-based).
```

### Example 2:

```text
Input:
a1 = [0, 1, 0, 1, 1, 1, 1]
a2 = [1, 1, 1, 1, 1, 0, 1]

Output:
6

Explanation:
The longest span with same sum is from index 1 to 6 (0-based).
```

---

## 📌 Constraints

* 1 ≤ `a1.size()` = `a2.size()` ≤ 10⁶
* 0 ≤ `a1[i]`, `a2[i]` ≤ 1

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏷️ Topic Tags

`prefix-sum` `sliding-window` `arrays` `data structures` `algorithms`

---

## 📚 Related Articles

* [Longest Span Sum Two Binary Arrays – GeeksforGeeks](#)

---

Here's the complete solution with **text explanation**, a **step-by-step dry run**, and code implementations for **Python**, **C++**, and **JavaScript** for the problem **Longest Span with Same Sum in Two Binary Arrays**.

---

## 🧠 Problem Understanding

Given two binary arrays `a1[]` and `a2[]`, we need to find the **longest span (i, j)** such that the sum of elements between indices `i` and `j` (inclusive) is equal in both arrays.

---

## 🪜 Key Insight

Let’s reduce the problem:

* Let `diff[i] = a1[i] - a2[i]`
* Then the problem becomes:
  **Find the longest subarray with sum = 0 in this `diff[]` array**

This is a classic prefix-sum + hashmap problem.

---

## 🧪 Dry Run

### Input:

```text
a1 = [0, 1, 0, 0, 0]  
a2 = [1, 0, 1, 0, 0]
```

### Step 1: diff\[] = a1 - a2

```
diff = [-1, 1, -1, 0, 0]
```

Now we want the longest subarray in `diff` whose sum is 0.

### Step 2: Running prefix sum

Keep a map of `prefix_sum -> first index`.
Update `max_len = i - map[prefix_sum]` when sum repeats.

Result:

* Longest span = 4 (from index 1 to 4)

---

## ✅ Python Code

```python
class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff = [a1[i] - a2[i] for i in range(n)]
        
        prefix_sum = 0
        max_len = 0
        mp = {}  # map: prefix_sum -> first index

        for i in range(n):
            prefix_sum += diff[i]
            
            if prefix_sum == 0:
                max_len = i + 1
            elif prefix_sum in mp:
                max_len = max(max_len, i - mp[prefix_sum])
            else:
                mp[prefix_sum] = i
        
        return max_len
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int longestCommonSum(vector<int> &a1, vector<int> &a2) {
        int n = a1.size();
        vector<int> diff(n);
        for (int i = 0; i < n; i++) {
            diff[i] = a1[i] - a2[i];
        }

        unordered_map<int, int> mp;
        int prefix_sum = 0, max_len = 0;

        for (int i = 0; i < n; i++) {
            prefix_sum += diff[i];

            if (prefix_sum == 0) {
                max_len = i + 1;
            } else if (mp.count(prefix_sum)) {
                max_len = max(max_len, i - mp[prefix_sum]);
            } else {
                mp[prefix_sum] = i;
            }
        }

        return max_len;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    longestCommonSum(a1, a2) {
        const n = a1.length;
        const diff = a1.map((val, i) => val - a2[i]);

        const map = new Map();
        let prefix_sum = 0, max_len = 0;

        for (let i = 0; i < n; i++) {
            prefix_sum += diff[i];

            if (prefix_sum === 0) {
                max_len = i + 1;
            } else if (map.has(prefix_sum)) {
                max_len = Math.max(max_len, i - map.get(prefix_sum));
            } else {
                map.set(prefix_sum, i);
            }
        }

        return max_len;
    }
}
```

---

## ⏱ Time & Space Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(n)       |

---

Here's the **step-by-step explanation** with a **dry run** for the **Longest Span with Same Sum in Two Binary Arrays** problem, followed by optimized code in **Python**, **C++**, and **JavaScript** with **inline comments**.

---

## 🧠 Problem Understanding

Given two binary arrays `a1[]` and `a2[]` of equal length, find the length of the **longest span** (subarray) where the **sum of elements is equal** in both arrays.

---

## 🪜 Intuition & Key Insight

Let:

* `prefix1[i]` = sum of `a1[0..i]`
* `prefix2[i]` = sum of `a2[0..i]`

If `prefix1[j] - prefix1[i-1] == prefix2[j] - prefix2[i-1]`, then `a1[i..j]` and `a2[i..j]` have same sum.

So we:

* Track the **difference** of prefix sums: `diff = prefix1 - prefix2`
* Use a **hash map** to store the first index where each difference appears
* If the same `diff` appears again at a later index, it means **between those indices, the sums are equal**

---

## 🧪 Dry Run Example

```text
a1 = [0, 1, 0, 0, 0]
a2 = [1, 0, 1, 0, 0]
```

We calculate running sums:

```
prefix1: 0, 1, 1, 1, 1
prefix2: 1, 1, 2, 2, 2
diff   : -1, 0, -1, -1, -1
```

* When `diff = 0`, we note the index and compare future diffs
* The longest span with equal sum occurs where the **same diff is seen again**

---

## ✅ Python Code

```python
class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff_map = {}  # maps diff to first index
        max_len = 0
        prefix1 = 0
        prefix2 = 0

        for i in range(n):
            prefix1 += a1[i]
            prefix2 += a2[i]
            diff = prefix1 - prefix2

            if diff == 0:
                max_len = i + 1
            elif diff in diff_map:
                max_len = max(max_len, i - diff_map[diff])
            else:
                diff_map[diff] = i

        return max_len
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int longestCommonSum(vector<int> &a1, vector<int> &a2) {
        int n = a1.size();
        unordered_map<int, int> diffMap;
        int prefix1 = 0, prefix2 = 0, maxLen = 0;

        for (int i = 0; i < n; i++) {
            prefix1 += a1[i];
            prefix2 += a2[i];
            int diff = prefix1 - prefix2;

            if (diff == 0) {
                maxLen = i + 1;
            } else if (diffMap.find(diff) != diffMap.end()) {
                maxLen = max(maxLen, i - diffMap[diff]);
            } else {
                diffMap[diff] = i;
            }
        }

        return maxLen;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    longestCommonSum(a1, a2) {
        const n = a1.length;
        let prefix1 = 0, prefix2 = 0, maxLen = 0;
        const diffMap = new Map();

        for (let i = 0; i < n; i++) {
            prefix1 += a1[i];
            prefix2 += a2[i];
            const diff = prefix1 - prefix2;

            if (diff === 0) {
                maxLen = i + 1;
            } else if (diffMap.has(diff)) {
                maxLen = Math.max(maxLen, i - diffMap.get(diff));
            } else {
                diffMap.set(diff, i);
            }
        }

        return maxLen;
    }
}
```

---

## ⏱ Time and Space Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

---

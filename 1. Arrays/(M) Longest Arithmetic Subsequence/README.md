# 📐 Longest Arithmetic Subsequence

**Difficulty:** Medium
**Accuracy:** 23.82%
**Submissions:** 41K+
**Points:** 4

---

## 🧾 Problem Statement

Given an array `arr[]` of **sorted and distinct positive integers**, the task is to find the **length of the longest arithmetic progression (AP)** in the array.

### ℹ️ Note:

A sequence `seq` is said to be in arithmetic progression if:

```text
seq[i + 1] - seq[i] == constant (for all 0 ≤ i < seq.length - 1)
```

---

## 🧪 Examples

### Example 1:

```text
Input: arr[] = [1, 7, 10, 13, 14, 19]  
Output: 4  
Explanation: The longest AP is [1, 7, 13, 19].
```

### Example 2:

```text
Input: arr[] = [2, 4, 6, 8, 10]  
Output: 5  
Explanation: The entire array is an AP.
```

---

## 📉 Expected Complexities

* **Time Complexity:** O(n²)
* **Auxiliary Space:** O(n²)

---

## 📌 Constraints

* 1 ≤ `arr.length` ≤ 1000
* 1 ≤ `arr[i]` ≤ 10⁴

---

## 🏷️ Tags

`Arrays` `Dynamic Programming` `Data Structures` `Algorithms`

---

## 🏢 Company Tags

* Amazon
* Microsoft
* Snapdeal
* Google

---

## 📚 Related Articles

* [Longest Arithmetic Progression - GeeksforGeeks](#)

---
Here's a complete explanation and dry run for **Longest Arithmetic Subsequence**, followed by implementations in **Python**, **C++**, and **JavaScript** with inline comments.

---

## 🧠 Problem Understanding

We are given a **sorted array of distinct integers**. The task is to **find the length of the longest arithmetic progression (AP)** possible using elements from the array.

### 📌 Arithmetic Progression (AP)

A sequence is in AP if the difference between consecutive terms is constant:

```
For example: [2, 4, 6, 8, 10] → diff = 2
```

---

## 🪜 Step-by-Step Dry Run

Input:

```
arr = [1, 7, 10, 13, 14, 19]
```

Try to find the longest AP:

* Possible AP: \[1, 7, 13, 19] (common difference = 6)
* Length = 4

We use Dynamic Programming:

* Let `dp[i][j]` store the length of the longest AP ending with `arr[i]` and `arr[j]`
* Initialize all values with 2 (every pair has at least length 2)
* Traverse `i < j`, and use formula based on AP properties:

  ```
  arr[i] + arr[k] == 2 * arr[j]  ⇒  i + k = 2j  ⇒ find if midpoint exists
  ```

---

## ✅ Time & Space

* Time: **O(n²)**
* Space: **O(n²)**

---

## 🐍 Python Code

```python
#User function Template for python3

class Solution:
    def lengthOfLongestAP(self, arr):
        n = len(arr)
        if n <= 2:
            return n

        # Create a table and initialize all values as 2
        dp = [[2] * n for _ in range(n)]
        max_len = 2

        # Fix the last element first, then the second last, and so on
        for j in range(n - 2, -1, -1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < n:
                if arr[i] + arr[k] < 2 * arr[j]:
                    k += 1
                elif arr[i] + arr[k] > 2 * arr[j]:
                    dp[i][j] = 2
                    i -= 1
                else:
                    dp[i][j] = dp[j][k] + 1
                    max_len = max(max_len, dp[i][j])
                    i -= 1
                    k += 1

            # Set remaining dp[i][j] = 2
            while i >= 0:
                dp[i][j] = 2
                i -= 1

        return max_len
```

---

## 💠 C++ Code

```cpp
// User function template for C++

class Solution {
  public:
    int lengthOfLongestAP(vector<int>& arr) {
        int n = arr.size();
        if (n <= 2) return n;

        vector<vector<int>> dp(n, vector<int>(n, 2));
        int max_len = 2;

        for (int j = n - 2; j >= 0; j--) {
            int i = j - 1, k = j + 1;
            while (i >= 0 && k < n) {
                if (arr[i] + arr[k] < 2 * arr[j])
                    k++;
                else if (arr[i] + arr[k] > 2 * arr[j])
                    dp[i--][j] = 2;
                else {
                    dp[i][j] = dp[j][k] + 1;
                    max_len = max(max_len, dp[i][j]);
                    i--; k++;
                }
            }
            while (i >= 0)
                dp[i--][j] = 2;
        }
        return max_len;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
// User function Template for javascript

class Solution {
    lengthOfLongestAP(arr) {
        const n = arr.length;
        if (n <= 2) return n;

        // Create a 2D array filled with 2
        const dp = Array.from({ length: n }, () => Array(n).fill(2));
        let maxLen = 2;

        for (let j = n - 2; j >= 0; j--) {
            let i = j - 1, k = j + 1;
            while (i >= 0 && k < n) {
                const sum = arr[i] + arr[k];
                const doubleMid = 2 * arr[j];
                if (sum < doubleMid) {
                    k++;
                } else if (sum > doubleMid) {
                    dp[i][j] = 2;
                    i--;
                } else {
                    dp[i][j] = dp[j][k] + 1;
                    maxLen = Math.max(maxLen, dp[i][j]);
                    i--; k++;
                }
            }

            while (i >= 0) {
                dp[i][j] = 2;
                i--;
            }
        }

        return maxLen;
    }
}
```

---

Would you like:

* Space optimization (if needed)?
---

## 🔍 Observation:

In the original solution, we use a `dp[n][n]` 2D matrix where:

* `dp[i][j]` stores the length of an AP ending with `arr[i]` and `arr[j]`

This takes **O(n²) space**, which is acceptable for `n ≤ 1000`, but can be **optimized**.

---

## ✅ Optimization Insight:

For any pair `(i, j)` where `i < j`, the recurrence depends **only on future entries** (`dp[j][k]`) and **not** on past values (`dp[i][j]` is not reused later).

So we can:

* Use a **hashmap per index j** to track the AP length with different differences.
* This brings **space from O(n²) → O(n·d)**, where `d` is the number of unique differences (at most O(n)).

---

## 🐍 Python (Optimized with HashMap)

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestAP(self, arr):
        n = len(arr)
        if n <= 2:
            return n

        dp = [defaultdict(int) for _ in range(n)]
        max_len = 2

        for i in range(n):
            for j in range(i):
                diff = arr[i] - arr[j]
                # Extend the AP ending at j with the same diff
                dp[i][diff] = dp[j][diff] + 1 if diff in dp[j] else 2
                max_len = max(max_len, dp[i][diff])

        return max_len
```

---

## 💠 C++ (Space Optimized Using `unordered_map`)

```cpp
class Solution {
  public:
    int lengthOfLongestAP(vector<int>& arr) {
        int n = arr.size();
        if (n <= 2) return n;

        vector<unordered_map<int, int>> dp(n);
        int max_len = 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = arr[i] - arr[j];
                dp[i][diff] = dp[j].count(diff) ? dp[j][diff] + 1 : 2;
                max_len = max(max_len, dp[i][diff]);
            }
        }

        return max_len;
    }
};
```

---

## 🌐 JavaScript (Using `Map` Array)

```javascript
class Solution {
    lengthOfLongestAP(arr) {
        const n = arr.length;
        if (n <= 2) return n;

        const dp = Array.from({ length: n }, () => new Map());
        let maxLen = 2;

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < i; j++) {
                const diff = arr[i] - arr[j];
                const len = dp[j].get(diff) || 1;
                dp[i].set(diff, len + 1);
                maxLen = Math.max(maxLen, len + 1);
            }
        }

        return maxLen;
    }
}
```

---

## 📌 Summary of Optimization

| Version                | Time  | Space  | Key Idea                            |
| ---------------------- | ----- | ------ | ----------------------------------- |
| 2D DP (O(n²))          | O(n²) | O(n²)  | Table storing lengths for all pairs |
| HashMap per index      | O(n²) | O(n·d) | Track diffs using hashmaps          |
| Suitable for large `n` | Yes   | Yes    | Efficient both in time & memory     |

---
# Print the actual AP sequence

Printing the actual **Longest Arithmetic Progression (AP) sequence** along with its **length** requires not only storing the length of APs but also tracking **previous indices** to reconstruct the path.

We will enhance the **space-optimized hashmap-based solution** to also keep a **back-pointer** to each element in the sequence.

---

## 🧠 Approach Summary

* For each pair `(j, i)` with `arr[i] - arr[j] = diff`:

  * Store not just the length but also the **index** of the previous element.
* After building the DP map, **backtrack** from the index having the longest AP.

---

## 🐍 Python Code to Print the Longest AP

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestAP(self, arr):
        n = len(arr)
        if n <= 2:
            return n, arr

        # dp[i][diff] = (length, prev_index)
        dp = [defaultdict(lambda: (1, -1)) for _ in range(n)]

        max_len = 2
        last_index = 0
        last_diff = 0

        for i in range(n):
            for j in range(i):
                diff = arr[i] - arr[j]
                prev_len, prev_idx = dp[j].get(diff, (1, -1))
                dp[i][diff] = (prev_len + 1, j)

                if dp[i][diff][0] > max_len:
                    max_len = dp[i][diff][0]
                    last_index = i
                    last_diff = diff

        # 🔁 Reconstruct the AP using backtracking
        sequence = []
        idx = last_index
        diff = last_diff
        while idx != -1:
            sequence.append(arr[idx])
            _, prev = dp[idx][diff]
            idx = prev

        sequence.reverse()
        return max_len, sequence


# Example usage
arr = [1, 7, 10, 13, 14, 19]
sol = Solution()
length, sequence = sol.lengthOfLongestAP(arr)
print("Length:", length)
print("Longest AP:", sequence)
```

---

### ✅ Output:

```
Length: 4  
Longest AP: [1, 7, 13, 19]
```

---

## 🔍 Explanation:

We enhanced `dp[i][diff]` from:

* just storing the **length** ➝ to storing both `(length, previous index)`
  This allows reconstructing the sequence after we find the longest one.

---


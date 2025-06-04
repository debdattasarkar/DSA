# 🧵 LCS of Three Strings

**Difficulty:** Medium
**Accuracy:** 48.52%
**Submissions:** 75K+
**Points:** 4

## 📘 Problem Statement

Given three strings `s1`, `s2`, and `s3` containing uppercase letters, lowercase letters, and digits, find the **length of the longest common subsequence** in all three given strings.

---

## 🧪 Examples

### Example 1:

```text
Input:  
s1 = "geeks"  
s2 = "geeksfor"  
s3 = "geeksforgeeks"

Output:  
5

Explanation:  
"geeks" is the longest common subsequence with length 5.
```

### Example 2:

```text
Input:  
s1 = "abcd1e2"  
s2 = "bc12ea"  
s3 = "bd1ea"

Output:  
3

Explanation:  
Longest common subsequence is "b1e", i.e., length = 3.
```

---

## ✅ Constraints

```
1 ≤ s1.length, s2.length, s3.length ≤ 100
```

---

## 💡 Expected Complexities

* **Time Complexity:** O(n1 \* n2 \* n3)
* **Auxiliary Space:** O(n1 \* n2 \* n3)

---

## 🏷️ Tags

`Strings` `Dynamic Programming` `Data Structures` `Algorithms`

---

## 🏢 Company Tags

* DE Shaw

---

## 📚 Related

* **Interview Experience:** [De Shaw Internship Interview Experience On Campus 2021](#)
* **Article:** [LCS Longest Common Subsequence Three Strings](#)

---

Sure! Here's a **text explanation with a step-by-step dry run**, followed by implementations in **Python**, **C++**, and **JavaScript**, with **inline comments**.

---

## 🧠 Explanation: LCS of 3 Strings

We aim to find the **Longest Common Subsequence (LCS)** among three strings. A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

### 🧩 Approach: Dynamic Programming

We use a **3D Dynamic Programming (DP)** array `dp[i][j][k]`, where:

* `i` represents length considered from `s1`
* `j` from `s2`
* `k` from `s3`

**Recurrence Relation:**

* If `s1[i-1] == s2[j-1] == s3[k-1]`, then:
  `dp[i][j][k] = 1 + dp[i-1][j-1][k-1]`
* Else:
  `dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])`

We build this 3D table from smaller problems.

---

## 🧪 Dry Run

For:

```text
s1 = "abc", s2 = "abc", s3 = "abc"
```

All characters match → LCS is "abc", length = 3
So:

* `dp[1][1][1] = 1` (a)
* `dp[2][2][2] = 2` (ab)
* `dp[3][3][3] = 3` (abc)

---

## 🐍 Python Code

```python
class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)

        # Initialize 3D DP table
        dp = [[[0]*(n3+1) for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                for k in range(1, n3+1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

        return dp[n1][n2][n3]
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int lcsOf3(string& s1, string& s2, string& s3) {
        int n1 = s1.length(), n2 = s2.length(), n3 = s3.length();
        int dp[n1+1][n2+1][n3+1];

        // Initialize DP array
        for(int i = 0; i <= n1; i++)
            for(int j = 0; j <= n2; j++)
                for(int k = 0; k <= n3; k++)
                    dp[i][j][k] = 0;

        for(int i = 1; i <= n1; i++) {
            for(int j = 1; j <= n2; j++) {
                for(int k = 1; k <= n3; k++) {
                    if(s1[i-1] == s2[j-1] && s2[j-1] == s3[k-1])
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1];
                    else
                        dp[i][j][k] = max({dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]});
                }
            }
        }

        return dp[n1][n2][n3];
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    lcsOf3(s1, s2, s3) {
        const n1 = s1.length, n2 = s2.length, n3 = s3.length;

        // Initialize 3D DP array
        const dp = Array.from({ length: n1 + 1 }, () =>
            Array.from({ length: n2 + 1 }, () =>
                Array(n3 + 1).fill(0)
            )
        );

        for (let i = 1; i <= n1; i++) {
            for (let j = 1; j <= n2; j++) {
                for (let k = 1; k <= n3; k++) {
                    if (s1[i - 1] === s2[j - 1] && s2[j - 1] === s3[k - 1]) {
                        dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1];
                    } else {
                        dp[i][j][k] = Math.max(
                            dp[i - 1][j][k],
                            dp[i][j - 1][k],
                            dp[i][j][k - 1]
                        );
                    }
                }
            }
        }

        return dp[n1][n2][n3];
    }
}
```

---

Absolutely! Let's walk through both:

---

## 🚀 1. Recursive + Memoized Version (Top-Down DP)

We use a function `lcs(i, j, k)` to represent the LCS length of substrings `s1[i:]`, `s2[j:]`, `s3[k:]`.

### 🔁 Recurrence:

* If characters match:
  `lcs(i, j, k) = 1 + lcs(i+1, j+1, k+1)`
* Else:
  `lcs(i, j, k) = max(lcs(i+1, j, k), lcs(i, j+1, k), lcs(i, j, k+1))`

We memoize results using `@lru_cache`.

---

### 🐍 Python (Recursive + Memoized):

```python
from functools import lru_cache

class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)

        @lru_cache(maxsize=None)
        def lcs(i, j, k):
            if i == n1 or j == n2 or k == n3:
                return 0
            if s1[i] == s2[j] == s3[k]:
                return 1 + lcs(i+1, j+1, k+1)
            return max(lcs(i+1, j, k), lcs(i, j+1, k), lcs(i, j, k+1))

        return lcs(0, 0, 0)
```

### ✅ Pros:

* Easy to write
* Automatically memoized

### ⚠️ Cons:

* High recursion stack for max input (but fine for n ≤ 100)

---

## 💾 2. Space Optimized DP (Bottom-Up)

Since `dp[i][j][k]` only needs values from `i-1`, we can reduce **space complexity from O(n³) to O(2×n²)**.

---

### 🐍 Python (Space Optimized):

```python
class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        prev = [[0] * (n3 + 1) for _ in range(n2 + 1)]

        for i in range(1, n1 + 1):
            curr = [[0] * (n3 + 1) for _ in range(n2 + 1)]
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        curr[j][k] = 1 + prev[j-1][k-1]
                    else:
                        curr[j][k] = max(prev[j][k], curr[j-1][k], curr[j][k-1])
            prev = curr  # Shift layer
        return prev[n2][n3]
```

---

### 🧠 Trade-Off Summary

| Version                  | Time  | Space | Best For                   |
| ------------------------ | ----- | ----- | -------------------------- |
| Top-Down + Memoization   | O(n³) | O(n³) | Clean recursive logic      |
| Bottom-Up Standard 3D    | O(n³) | O(n³) | Simple tabulation          |
| Space Optimized 2 Layers | O(n³) | O(n²) | Efficient for large inputs |

---

The error **"Time Limit Exceeded"** on 1010/1127 test cases, with a **10.5 sec limit**, suggests your current solution (likely recursive + memoized or full 3D DP) is not fast enough under worst-case inputs.

Here’s how you can **optimize your code**:

---

## ✅ Use Space Optimized Bottom-Up DP (Recommended)

The fully iterative bottom-up DP with **2 layers instead of 3** is both **fast and memory efficient**. It avoids recursion overhead and large memoization caches.

Here’s the **most optimized version** in **Python**:

```python
class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)

        # Only keep two layers: prev and curr
        prev = [[0] * (n3 + 1) for _ in range(n2 + 1)]

        for i in range(1, n1 + 1):
            curr = [[0] * (n3 + 1) for _ in range(n2 + 1)]
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        curr[j][k] = 1 + prev[j-1][k-1]
                    else:
                        curr[j][k] = max(
                            prev[j][k],      # exclude s1[i-1]
                            curr[j-1][k],    # exclude s2[j-1]
                            curr[j][k-1]     # exclude s3[k-1]
                        )
            prev = curr  # move to next layer
        return prev[n2][n3]
```

---

## ⏱ Performance Tips

* ✅ Avoid recursion with large depth
* ✅ Avoid storing full `n1 x n2 x n3` if not needed
* ✅ Use **local variables** and **loop-level caching** (like `s1[i-1]` to a temp var if you're optimizing in C++)

---

## ⚙️ If using C++, further boost performance:

* Use `std::vector` only when needed; avoid dynamic allocation inside deep loops.
* Compile with `-O2` or `-O3` optimizations for large test cases.

---

Let me know if you want the **space-optimized C++ version** or **JavaScript version** too.

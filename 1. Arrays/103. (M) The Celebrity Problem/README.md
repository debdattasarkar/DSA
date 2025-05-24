# The Celebrity Problem

**Difficulty:** Medium
**Accuracy:** 38.33%
**Submissions:** 312K+
**Points:** 4
**Average Time:** 30 minutes

## 🧩 Problem Statement

A **celebrity** is a person who is known by everyone but knows no one at a party.
Given a `n x n` matrix `mat[][]`, where `mat[i][j] == 1` implies person `i` knows person `j`, and `mat[i][j] == 0` implies person `i` does **not** know person `j`.
Your task is to return the **index of the celebrity**, or `-1` if there is no celebrity.

> Note: Follow **0-based indexing**.

---

## 📥 Input

* A square matrix `mat[][]` of size `n x n`.

## 📤 Output

* Return an integer: the **index of the celebrity**, or `-1` if none exists.

---

## 🧪 Examples

### Example 1

```
Input: 
mat[][] = [[1, 1, 0],
           [0, 1, 0],
           [0, 1, 1]]
Output: 1

Explanation: 0th and 2nd person both know 1st person. Therefore, 1 is the celebrity.
```

### Example 2

```
Input: 
mat[][] = [[1, 1],
           [1, 1]]
Output: -1

Explanation: Both know each other. No celebrity exists.
```

### Example 3

```
Input:
mat[][] = [[1]]
Output: 0

Explanation: Only one person; by default, they are a celebrity.
```

---

## ✅ Constraints

* `1 <= mat.size() <= 1000`
* `0 <= mat[i][j] <= 1`
* `mat[i][i] == 1`

---

## ⏱ Expected Time & Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🧠 Approach

Use the **two-pointer elimination** strategy:

1. Start with two pointers `a = 0` and `b = n-1`.
2. If `a` knows `b`, then `a` cannot be the celebrity. Move `a` forward.
3. If `a` does not know `b`, then `b` cannot be the celebrity. Move `b` backward.
4. After one pass, a **candidate** will remain.
5. Validate the candidate by checking:

   * Candidate doesn't know anyone else.
   * Everyone else knows the candidate.

---

## 🏷️ Tags

`Arrays`, `Stack`, `Data Structures`

---

## 🏢 Company Tags

`Zoho`, `Flipkart`, `Amazon`, `Microsoft`, `Google`, `Fab.com`, `One97`, `United Health Group`

---

## 📚 Related Articles

* [The Celebrity Problem](https://www.geeksforgeeks.org/the-celebrity-problem/)

---

Here's the detailed explanation with a **step-by-step dry run** followed by **Python**, **C++**, and **JavaScript** implementations with inline comments for the **Celebrity Problem** from GeeksforGeeks.

---

## 🧠 Explanation

### Problem Summary

We are given an `n x n` matrix `mat` where `mat[i][j] == 1` means person `i` knows person `j`.
A **celebrity** is known by everyone but knows no one.

### Goal

Find the **index** of the celebrity or return `-1` if no such person exists.

### Step-by-Step Algorithm

1. **Elimination Phase**:
   Use two pointers (`a = 0`, `b = n-1`) to identify the potential celebrity.

   * If `a` knows `b`, then `a` **cannot** be a celebrity. Move `a++`.
   * Else, `b` **cannot** be a celebrity. Move `b--`.

2. **Verification Phase**:
   For the candidate found in the first phase:

   * They should not know **anyone** (`mat[candidate][j] == 0` for all `j != candidate`).
   * Everyone should know **them** (`mat[i][candidate] == 1` for all `i != candidate`).

---

## 🧪 Dry Run Example

**Input:**

```python
mat = [[1, 1, 0],
       [0, 1, 0],
       [0, 1, 1]]
```

**Step 1: Elimination**

* a = 0, b = 2 → `mat[0][2] = 0` → 2 cannot be celebrity → `b--` → b = 1
* a = 0, b = 1 → `mat[0][1] = 1` → 0 cannot be celebrity → `a++` → a = 1

Now, `a == b == 1`, potential celebrity = 1

**Step 2: Verification**

* Check: `mat[1][0] = 0`, `mat[1][2] = 0` ✅
* Check: `mat[0][1] = 1`, `mat[2][1] = 1` ✅

→ Person 1 is the celebrity.

---

## ✅ Python Code

```python
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        a, b = 0, n - 1

        # Step 1: Elimination
        while a < b:
            if mat[a][b] == 1:
                a += 1  # a knows b → a is not celebrity
            else:
                b -= 1  # a does not know b → b is not celebrity

        candidate = a

        # Step 2: Verification
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int celebrity(vector<vector<int> >& mat) {
        int n = mat.size();
        int a = 0, b = n - 1;

        // Step 1: Elimination
        while (a < b) {
            if (mat[a][b] == 1)
                a++; // a knows b
            else
                b--; // a does not know b
        }

        int candidate = a;

        // Step 2: Verification
        for (int i = 0; i < n; ++i) {
            if (i != candidate) {
                if (mat[candidate][i] == 1 || mat[i][candidate] == 0)
                    return -1;
            }
        }
        return candidate;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    /**
     * @param {number[][]} mat
     * @returns {number}
     */
    celebrity(mat) {
        const n = mat.length;
        let a = 0, b = n - 1;

        // Step 1: Elimination
        while (a < b) {
            if (mat[a][b] === 1) {
                a++; // a knows b
            } else {
                b--; // b is not a celebrity
            }
        }

        const candidate = a;

        // Step 2: Verification
        for (let i = 0; i < n; i++) {
            if (i !== candidate) {
                if (mat[candidate][i] === 1 || mat[i][candidate] === 0) {
                    return -1;
                }
            }
        }

        return candidate;
    }
}
```

---

Let me know if you'd like a version with test cases or benchmarking!

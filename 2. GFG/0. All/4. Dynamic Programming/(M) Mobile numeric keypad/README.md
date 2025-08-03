
---

# 📱 Mobile Numeric Keypad

### Difficulty: Medium

**Accuracy**: 32.6%
**Submissions**: 62K+
**Points**: 4
**Average Time**: 30 mins

---

## 🧩 Problem Statement

There is a standard **numeric keypad** on a mobile phone. You can press:

* The **current button**
* Or any button that is directly:

  * **Above**
  * **Below**
  * **To the left**
  * **To the right**

> ❗ However, **diagonal movements** and pressing the **bottom row corner buttons** (`*` and `#`) are **not allowed**.

### 🔢 Keypad Layout

```
1   2   3
4   5   6
7   8   9
*   0   #
```

### Task

Given an integer **n**, determine how many **unique sequences** of length **n** can be formed by pressing buttons on the keypad, starting from **any digit**.

---

## 📘 Examples

### Example 1:

**Input**: `n = 1`
**Output**: `10`
**Explanation**:
All digits `0-9` are valid 1-digit numbers. So total = **10**.

---

### Example 2:

**Input**: `n = 2`
**Output**: `36`
**Explanation**:
From digit `0` → you can go to `0`, `8` → makes 2 combinations
From digit `1` → `1`, `2`, `4` → 3 combinations
From digit `2` → `2`, `1`, `3`, `5` → 4 combinations
From digit `3` → `3`, `2`, `6` → 3 combinations
... and so on.

Total number of 2-digit combinations = **36**

---

## 🔒 Constraints

* `1 ≤ n ≤ 15`

---

## 💡 Expected Time & Space Complexities

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(1)

---

## 🏷️ Tags

* Dynamic Programming
* Algorithms
* Mathematical

---

## 🏢 Company Tags

* Flipkart
* Microsoft
* MAQ Software
* Sprinklr

---

## 📚 Related Interview Experiences

* [Sprinklr Interview Experience Set 2 On Campus](#)
* [Microsoft Interview Experience Set 53](#)
* [Flipkart Interview Set 11](#)
* [Flipkart Interview Experience For SDE 2](#)

---

## 📖 Related Articles

* [Mobile Numeric Keypad Problem](#)

---

Let's break this into 3 parts for the **Mobile Numeric Keypad** problem.

---

## ✅ 1. Text Explanation with Step-by-Step Dry Run

### 🔍 Problem Understanding:

You’re given a standard **mobile numeric keypad**. You can move from one digit to:

* Itself
* Any of the **adjacent digits** (up, down, left, right)

**Goal:** Count how many unique number sequences of length `n` you can form.

You **can't**:

* Move diagonally
* Use `*` or `#`

### 🔢 Keypad Layout:

```
1 2 3
4 5 6
7 8 9
* 0 #
```

### 💡 Strategy:

Use **Dynamic Programming**:

* `dp[d][l]` = number of sequences of length `l` starting from digit `d`
* Base case: `dp[d][1] = 1` for all digits `0-9`
* Use a map of valid moves (adjacent digits for each number)
* Build sequences of increasing lengths using transitions

---

### 🧪 Dry Run Example:

Let’s run `getCount(2)`:

#### Initialization:

We set `dp[d][1] = 1` for all `d in 0-9`

#### Valid Moves Map:

```python
moves = {
  0: [0, 8],
  1: [1, 2, 4],
  2: [2, 1, 3, 5],
  3: [3, 2, 6],
  4: [4, 1, 5, 7],
  5: [5, 2, 4, 6, 8],
  6: [6, 3, 5, 9],
  7: [7, 4, 8],
  8: [8, 5, 7, 9, 0],
  9: [9, 6, 8]
}
```

#### Now for `length = 2`, calculate for each digit:

```text
dp[1][2] = dp[1][1] + dp[2][1] + dp[4][1] = 1 + 1 + 1 = 3
dp[5][2] = dp[5][1] + dp[2][1] + dp[4][1] + dp[6][1] + dp[8][1] = 1+1+1+1+1 = 5
...
```

Total all `dp[d][n]` for digits 0–9 gives the final answer.

---

## ✅ 2. Code Implementations with Comments

---

### ✅ Python

```python
class Solution:
    def getCount(self, n):
        if n == 1:
            return 10

        # Adjacency list
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # Initialize dp with size 10 for digits, n+1 for lengths
        dp = [[0]*(n+1) for _ in range(10)]

        for i in range(10):
            dp[i][1] = 1

        for l in range(2, n+1):
            for d in range(10):
                for m in moves[d]:
                    dp[d][l] += dp[m][l-1]

        return sum(dp[i][n] for i in range(10))
```

---

### ✅ C++

```cpp
class Solution {
  public:
    int getCount(int n) {
        if(n == 1) return 10;

        vector<vector<int>> dp(10, vector<int>(n+1, 0));

        vector<vector<int>> moves = {
            {0, 8},        // 0
            {1, 2, 4},     // 1
            {2, 1, 3, 5},  // 2
            {3, 2, 6},     // 3
            {4, 1, 5, 7},  // 4
            {5, 2, 4, 6, 8},//5
            {6, 3, 5, 9},  // 6
            {7, 4, 8},     // 7
            {8, 5, 7, 9, 0},//8
            {9, 6, 8}      // 9
        };

        for(int i = 0; i < 10; i++) {
            dp[i][1] = 1;
        }

        for(int l = 2; l <= n; l++) {
            for(int d = 0; d <= 9; d++) {
                for(int m : moves[d]) {
                    dp[d][l] += dp[m][l - 1];
                }
            }
        }

        int total = 0;
        for(int i = 0; i < 10; i++) total += dp[i][n];
        return total;
    }
};
```

---

### ✅ JavaScript

```javascript
class Solution {
    getCount(n) {
        if (n === 1) return 10;

        const moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        };

        const dp = Array.from({ length: 10 }, () => Array(n + 1).fill(0));
        for (let i = 0; i <= 9; i++) {
            dp[i][1] = 1;
        }

        for (let l = 2; l <= n; l++) {
            for (let d = 0; d <= 9; d++) {
                for (const m of moves[d]) {
                    dp[d][l] += dp[m][l - 1];
                }
            }
        }

        let total = 0;
        for (let i = 0; i <= 9; i++) {
            total += dp[i][n];
        }
        return total;
    }
}
```

---

## ✅ 3. Expected Interview Questions & Answers

---

### 💬 Q1: What is the time and space complexity?

**A:**

* Time: O(10 × M × D), where M is number of digits (fixed = 10), D = length `n`
* So, overall time = O(n)
* Space: O(10 × n)

---

### 💬 Q2: Why use dynamic programming?

**A:**
We need to build up from smaller lengths to `n`. DP avoids recomputation by storing intermediate results for each digit at every length.

---

### 💬 Q3: Can you use recursion with memoization instead of bottom-up DP?

**A:**
Yes, a top-down approach with a `memo(d, l)` cache can solve this, but the iterative bottom-up method is faster and simpler.

---

### 💬 Q4: Why are `*` and `#` excluded?

**A:**
They are not digits and cannot be starting points or move targets. Problem explicitly disallows them.

---



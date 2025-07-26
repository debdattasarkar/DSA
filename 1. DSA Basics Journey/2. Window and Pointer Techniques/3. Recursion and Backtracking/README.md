Let’s break down **Recursion** and **Backtracking** — two fundamental and deeply connected problem-solving techniques often tested in **interviews**.

---

## 🔁 What is **Recursion**?

**Recursion** is a technique where a function **calls itself** to solve smaller instances of a problem.

### 🔸 Key Components:

* **Base case**: When to stop recursion
* **Recursive case**: How to reduce the problem and call the function again

### 🧠 Example – Factorial

```python
def factorial(n):
    if n == 0:
        return 1          # base case
    return n * factorial(n - 1)  # recursive case
```

---

## 🧩 What is **Backtracking**?

**Backtracking** is a **refined form of recursion** where:

* You explore possible solutions **one by one**
* **Backtrack (undo)** when a choice leads to an invalid or suboptimal state

It’s used in problems involving **combinations**, **permutations**, **decision trees**, **constraints**, etc.

---

### 💡 Core Idea:

1. **Choose** an option
2. **Explore** recursively
3. **Undo (backtrack)** the choice

---

### 🧠 Example – N Queens

```python
def solveNQueens(n):
    board = [['.'] * n for _ in range(n)]
    res = []

    def is_valid(r, c):
        for i in range(r):
            if board[i][c] == 'Q': return False
            if c - (r - i) >= 0 and board[i][c - (r - i)] == 'Q': return False
            if c + (r - i) < n and board[i][c + (r - i)] == 'Q': return False
        return True

    def backtrack(r):
        if r == n:
            res.append([''.join(row) for row in board])
            return
        for c in range(n):
            if is_valid(r, c):
                board[r][c] = 'Q'     # Choose
                backtrack(r + 1)      # Explore
                board[r][c] = '.'     # Undo (Backtrack)

    backtrack(0)
    return res
```

---

## 🔁 Recursion vs Backtracking

| Feature        | Recursion                      | Backtracking                     |
| -------------- | ------------------------------ | -------------------------------- |
| Nature         | Function calling itself        | Recursion with state rollback    |
| Goal           | Solve via smaller subproblems  | Explore all possibilities safely |
| Common Use     | Factorial, Fibonacci, Tree DFS | N-Queens, Sudoku, Subsets, Paths |
| State Restore? | Not always                     | Yes (undo the change after call) |

---

## 🧪 When to Use Which?

* Use **Recursion** when:

  * Problem is divisible into smaller subproblems
  * You don’t need to explore all branches (e.g. Tree Traversals)

* Use **Backtracking** when:

  * You need to explore **all valid configurations**
  * There’s a **constraint** to be satisfied
  * You must **revert a choice** and try another

---

## ⏳ Time Complexity Tip

Backtracking typically leads to **exponential time complexity**, often **O(2^n)** or worse — unless **pruned** using:

* Constraints
* Early stopping
* Memoization (for overlapping states)


---

Here are **selective and frequently asked Python problems** involving **Memoized Recursion (Caching)** that show up in interviews at top companies like **Amazon, Google, and Microsoft**. These problems require recursion but **optimize performance using `@lru_cache`** or manual memoization (with `dict`).

---

## ✅ When Do We Use Memoization?

When the recursive solution has:

* **Overlapping subproblems** (same calls repeat)
* **Exponential time** without caching
* Need for **top-down DP** optimization

---

## 🧑‍💻 Sample Template (with `@lru_cache`)

```python
from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(None)
        def ways(i):
            if i <= 1:
                return 1
            return ways(i - 1) + ways(i - 2)

        return ways(n)
```

### Or Manual Dict Memo

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## 🧪 Real-World Relevance

* **Spell checking** or **tokenization** (`Word Break`)
* **Path optimization** in **maps** (`Min Path Sum`, `Unique Paths`)
* **Budgeting/planning** problems (`House Robber`, `Partition`)
* **Message decoding** in **telecom** or **IoT** (`Decode Ways`)

---

## 🧩 Interview Tips

| Tip                                        | Why It Helps                      |
| ------------------------------------------ | --------------------------------- |
| Use `@lru_cache(None)` for clean memo      | Built-in and efficient            |
| Explain base case first                    | Interviewers care about structure |
| Show brute → memo → tabulation progression | Shows maturity in problem solving |
| Memo key should capture the unique state   | Like `index + sum` in Target Sum  |
| Avoid global variables in recursion        | Use closure or pass parameters    |

---

Here's a **tiered list** of hand-picked problems from **Recursion**, **Backtracking**, and **Memoized Recursion**, categorized into **Basic**, **Intermediate**, and **Advanced** levels. Each list builds progressively in difficulty and concept depth — perfect for **DSA interview prep**.

---

## 🔁 **RECURSION**

### 🟢 Basic

| Problem                          | Platform     |
| -------------------------------- | ------------ |
| Factorial of a number            | GFG          |
| Fibonacci (Recursive)            | Leetcode 509 |
| Sum of 1 to N                    | GFG          |
| Reverse a string using recursion | GFG          |
| Power of a number (xⁿ)           | Leetcode 50  |

### 🟡 Intermediate

| Problem                                 | Platform     |
| --------------------------------------- | ------------ |
| Palindrome check using recursion        | GFG          |
| Print all subsets of array              | Leetcode 78  |
| Generate all binary strings of length N | GFG          |
| Recursive Binary Search                 | Leetcode 704 |
| Generate balanced parentheses           | Leetcode 22  |

### 🔴 Advanced

| Problem                                 | Platform          |
| --------------------------------------- | ----------------- |
| Tower of Hanoi                          | GFG               |
| Expression evaluation (prefix/infix)    | Custom            |
| Recursive tree problems (Depth, Height) | Leetcode 104, 543 |
| K-th Symbol in Grammar                  | Leetcode 779      |
| Count unique BSTs                       | Leetcode 96       |

---

## 🔙 **BACKTRACKING**

### 🟢 Basic

| Problem                             | Platform    |
| ----------------------------------- | ----------- |
| Subsets                             | Leetcode 78 |
| Permutations                        | Leetcode 46 |
| Generate Parentheses                | Leetcode 22 |
| Letter combinations of phone number | Leetcode 17 |

### 🟡 Intermediate

| Problem                 | Platform         |
| ----------------------- | ---------------- |
| Combination Sum I / II  | Leetcode 39 / 40 |
| Palindrome Partitioning | Leetcode 131     |
| Word Search in Grid     | Leetcode 79      |
| Rat in a Maze           | GFG              |
| N-Queens Problem        | Leetcode 51      |

### 🔴 Advanced

| Problem                        | Platform     |
| ------------------------------ | ------------ |
| Sudoku Solver                  | Leetcode 37  |
| Word Break II                  | Leetcode 140 |
| Matchsticks to Square          | Leetcode 473 |
| Partition into K equal subsets | Leetcode 698 |
| Expression Add Operators       | Leetcode 282 |

---

## 🧠 **MEMOIZED RECURSION (Top-Down DP)**

### 🟢 Basic

| Problem                  | Platform     |
| ------------------------ | ------------ |
| Climbing Stairs          | Leetcode 70  |
| Fibonacci (Memoized)     | Leetcode 509 |
| Min cost climbing stairs | Leetcode 746 |
| Unique Paths             | Leetcode 62  |
| Decode Ways              | Leetcode 91  |

### 🟡 Intermediate

| Problem                    | Platform     |
| -------------------------- | ------------ |
| Target Sum                 | Leetcode 494 |
| Can Partition Array        | Leetcode 416 |
| House Robber               | Leetcode 198 |
| Word Break                 | Leetcode 139 |
| Palindrome Partition Count | Leetcode 647 |

### 🔴 Advanced

| Problem                          | Platform           |
| -------------------------------- | ------------------ |
| Word Break II (with memo)        | Leetcode 140       |
| Count All Palindromic Partitions | GFG                |
| All Possible Full Binary Trees   | Leetcode 894       |
| Minimum Edit Distance            | Leetcode 72        |
| Paint Fence / Paint House        | Leetcode 276 / 256 |

---

## 🧩 Practice Path

1. ✅ **Start with Recursion** basics and transition to decision-tree problems
2. 🔄 Use **Backtracking** to explore multiple paths
3. ⚡ Optimize recursive problems using **Memoization**

---

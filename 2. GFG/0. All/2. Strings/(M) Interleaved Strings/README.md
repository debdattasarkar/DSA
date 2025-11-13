
---

# 🔀 Interleaved Strings

### Difficulty: Medium

**Accuracy:** 24.33%
**Submissions:** 103K+
**Points:** 4
**Average Time:** 30m

---

## 🧠 Problem Statement

Given strings **s1**, **s2**, and **s3**, find whether **s3** is formed by an *interleaving* of **s1** and **s2**.

### Interleaving of two strings

Interleaving of two strings **s1** and **s2** is a way to mix their characters to form a new string **s3**, while maintaining the **relative order** of characters from **s1** and **s2**.

### Conditions for interleaving:

1. Characters from **s1** must appear in the same order in **s3** as they are in **s1**.
2. Characters from **s2** must appear in the same order in **s3** as they are in **s2**.
3. The length of **s3** must be equal to the combined length of **s1** and **s2**.

---

## 🧩 Examples

### Example 1

**Input:**

```
s1 = "AAB", s2 = "AAC", s3 = "AAAABC"
```

**Output:**

```
true
```

**Explanation:**
The string `"AAAABC"` has all characters of the other two strings and in the same order.

---

### Example 2

**Input:**

```
s1 = "AB", s2 = "C", s3 = "ACB"
```

**Output:**

```
true
```

**Explanation:**
`s3` has all characters of `s1` and `s2`, and retains the order of characters of `s1`.

---

### Example 3

**Input:**

```
s1 = "YX", s2 = "X", s3 = "XXY"
```

**Output:**

```
false
```

**Explanation:**
`"XXY"` is not an interleaving of `"YX"` and `"X"`.
The possible interleavings are `"YXX"` and `"XYX"`, but `"XXY"` breaks order.

---

## ⚙️ Constraints

* ( 1 \leq s1.length, s2.length \leq 300 )
* ( 1 \leq s3.length \leq 600 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n × m)
* **Auxiliary Space:** O(m)

---

## 🏢 Company Tags

**Paytm**, **Amazon**, **Microsoft**, **FactSet**, **Google**, **Zillious**, **Yahoo**

---

## 🧩 Topic Tags

* Strings
* Dynamic Programming
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [**Find if a String is Interleaved of Two Other Strings (DP-33)**](https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/)

---

---

awesome — let’s make **Interleaved Strings** interview-ready.

---

# 2) Explanation + a quick dry run

## Problem in one line

Return **True** iff `s3` can be formed by *interleaving* `s1` and `s2` **without changing the relative order** of characters from either string. (Every char of `s1` and `s2` must appear exactly once; `len(s3) = len(s1)+len(s2)`.)

## DP idea (gold standard)

Let `dp[i][j]` mean:

> “`s1[:i]` and `s2[:j]` can interleave to form `s3[:i+j]`.”

Transition (1-based reasoning, but we’ll store 0-based lengths):

* If the next char of `s1` matches `s3` → come from `dp[i-1][j]`
* If the next char of `s2` matches `s3` → come from `dp[i][j-1]`

Formally:

```
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1])  or
           (dp[i][j-1] and s2[j-1] == s3[i+j-1])
Base: dp[0][0] = True
Row 0 / Col 0 are straight prefix matches.
```

Answer: `dp[len(s1)][len(s2)]`.

### Dry run (from prompt)

`s1="AAB", s2="AAC", s3="AAAABC"` → len = 3, 3, 6

Fill `dp` table (rows i=0..3, cols j=0..3). Only the important cells:

* `dp[0][0]=T`
* First row (`i=0`): check if `s2` prefix equals `s3` prefix → `A A A ...`

  * `dp[0][1]=T` (‘A’==‘A’), `dp[0][2]=T` (‘AA’==‘AA’), `dp[0][3]=F` (needs third ‘A’ in `s2`, but `s2[2]='C'`)
* First column (`j=0`): match `s1` prefix → `A A B ...`

  * `dp[1][0]=T`, `dp[2][0]=T`, `dp[3][0]=F` (needs ‘B’ but `s3[2]='A'`)
* Inside:

  * `dp[1][1]=T` (take ‘A’ from either side)
  * `dp[2][1]=T`
  * `dp[2][2]=T` (we’ve matched “AAAA”)
  * `dp[2][3]=F` (needs ‘C’ earlier)
  * `dp[3][2]=T` (take ‘B’ now)
  * `dp[3][3]=T` ✅

Thus `s3` is a valid interleaving → **True**.

---

# 3) Python solutions (brute ➜ memo ➜ O(1)-space DP)

Use exactly your requested signature:

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        # code here
```

## A) Brute backtracking (exponential; good to explain why we need DP)

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        Try to consume s3 by choosing from s1 or s2 when they match.
        Time:  Exponential in worst case (many equal chars)
        Space: O(n+m) recursion depth
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        def dfs(i, j, k):
            if k == n3:
                return i == n1 and j == n2
            ok = False
            if i < n1 and s1[i] == s3[k]:
                ok = ok or dfs(i + 1, j, k + 1)
            if j < n2 and s2[j] == s3[k]:
                ok = ok or dfs(i, j + 1, k + 1)
            return ok

        return dfs(0, 0, 0)
```

## B) Top-down DP with memo (clean and fast; **O(n·m)**)

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        Memoized recursion on indices (i,j): we've formed s3[:i+j].
        Time:  O(n1*n2)
        Space: O(n1*n2) memo + O(n1+n2) stack
        """
        from functools import lru_cache
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        @lru_cache(None)
        def can(i, j):  # i used from s1, j used from s2
            k = i + j
            if k == n3:
                return i == n1 and j == n2
            take1 = i < n1 and s1[i] == s3[k] and can(i + 1, j)
            if take1:
                return True
            take2 = j < n2 and s2[j] == s3[k] and can(i, j + 1)
            return take2

        return can(0, 0)
```

## C) Bottom-up DP with **O(m)** space (most expected)

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        1D DP over s2 (columns). dp[j] = dp value for current row i.
        Time:  O(n1*n2)
        Space: O(n2)
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        # dp[j]: s1[:i] & s2[:j] -> s3[:i+j]
        dp = [False] * (n2 + 1)
        dp[0] = True

        # Initialize first row (i=0): only s2 builds s3
        for j in range(1, n2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill rows
        for i in range(1, n1 + 1):
            # first col (j=0): only s1 builds s3
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n2 + 1):
                from_s1 = dp[j] and (s1[i - 1] == s3[i + j - 1])
                from_s2 = dp[j - 1] and (s2[j - 1] == s3[i + j - 1])
                dp[j] = from_s1 or from_s2

        return dp[n2]
```

> In interviews: Option **C (1D DP)** is the sweet spot: concise, optimal `O(n·m)` time and `O(m)` space. If you need to explain more intuitively, start with **B (memo)** and mention how to compress to 1D.

---

# 4) Interview memory hooks + Q&A

## 5-line pseudo (say it out loud)

```
if len(s1)+len(s2) != len(s3): return False
dp[0..m] with dp[0]=True  # m=len(s2)
init dp[j] for row i=0 using s2 vs s3
for i in 1..n1:
  dp[0] &= (s1[i-1] == s3[i-1])
  for j in 1..n2:
    dp[j] = (dp[j]   and s1[i-1]==s3[i+j-1]) or \
            (dp[j-1] and s2[j-1]==s3[i+j-1])
return dp[n2]
```

**Mnemonic:** **“Pick from `s1` (same `j`) OR from `s2` (from `j-1`) if chars match the `k=i+j-1` of `s3`.”**

---

### Likely interviewer questions (and crisp answers)

**Q1. Why does a greedy two-pointer fail?**
Because duplicate letters can create ambiguous choices; a wrong early pick can block the correct path. DP ensures we consider both possibilities.

**Q2. State definition?**
`dp[i][j]` → whether `s1[:i]` and `s2[:j]` interleave to `s3[:i+j]`.

**Q3. Transitions?**

* If `s1[i-1] == s3[i+j-1]` and `dp[i-1][j]` then True.
* If `s2[j-1] == s3[i+j-1]` and `dp[i][j-1]` then True.
  Either suffices.

**Q4. Base cases?**
`dp[0][0]=True`. First row/column are straightforward prefix matches: use only `s2` or only `s1`.

**Q5. Complexity?**
DP is **O(n1·n2)** time; space can be **O(n2)** with row compression.

**Q6. Any quick precheck?**
Yes: if `len(s1)+len(s2) != len(s3)`, return `False` immediately.

**Q7. Can we reconstruct one interleaving?**
Yes: store parents or backtrack from `dp[n1][n2]` checking which branch was used.

---

---

awesome — here are the last two pieces for **Interleaved Strings**.

# 5) Real-World Use Cases (short & relatable)

* **Merging two sorted/event streams** while preserving the per-stream order (e.g., interleaving logs from two services into a single timeline).
* **Keyboard input composition**: combining characters from two sources (e.g., macro expansion + user typing) to check if the final text could result from those inputs without reordering within each source.
* **Version control / patch validation**: verifying whether a final file can be formed by interleaving two developers’ change sequences while preserving each developer’s change order.

These all mirror: “take from source A or B, but never reorder within a source.”

---

# 6) Full Python Program (with timing + inline complexity notes)

```python
"""
Interleaved Strings — Full Program
----------------------------------
Given s1, s2, s3, determine if s3 is an interleaving of s1 and s2
(preserves the relative order of chars from each).

Dynamic Programming (row-compressed 1D):
  Let dp[j] represent: s1[:i] and s2[:j] can form s3[:i+j] for current row i.

Transitions:
  dp[j] = (dp[j]   and s1[i-1] == s3[i+j-1])   # take next char from s1
        or (dp[j-1] and s2[j-1] == s3[i+j-1]) # take next char from s2

Complexities:
  Time:  O(len(s1) * len(s2))     # each state computed once
  Space: O(len(s2))               # 1D DP over columns

We also include backtracking-friendly memo (for reference) and a demo runner.
"""

import timeit
from functools import lru_cache

class Solution:
    # --------- Interview-standard: O(n*m) time, O(m) space ----------
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        DP (row-compressed).

        Step-by-step complexity:
          - Precheck and initializations: O(1)
          - First row init (loop over s2): O(m)
          - Outer loop over s1, inner loop over s2: O(n*m)
          => Total time O(n*m); space O(m)
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:          # O(1) early exit
            return False

        # dp[j] means: using s1[:i] & s2[:j] can form s3[:i+j]
        dp = [False] * (n2 + 1)    # O(m) space
        dp[0] = True               # empty + empty -> empty

        # Initialize first row (i = 0): only s2 contributes
        for j in range(1, n2 + 1):                       # O(m)
            dp[j] = dp[j - 1] and (s2[j - 1] == s3[j - 1])

        # Fill subsequent rows
        for i in range(1, n1 + 1):                       # O(n)
            # first column (j=0): only s1 contributes
            dp[0] = dp[0] and (s1[i - 1] == s3[i - 1])   # O(1)
            for j in range(1, n2 + 1):                   # inner O(m)
                take_s1 = dp[j] and (s1[i - 1] == s3[i + j - 1])
                take_s2 = dp[j - 1] and (s2[j - 1] == s3[i + j - 1])
                dp[j] = take_s1 or take_s2
        return dp[n2]

    # --------- Optional: Top-down memo (good for explanation) ----------
    def isInterleave_memo(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        @lru_cache(maxsize=None)
        def can(i: int, j: int) -> bool:
            # We formed s3[:i+j] using s1[:i] and s2[:j]
            if i + j == n3:
                return i == n1 and j == n2
            k = i + j
            return ((i < n1 and s1[i] == s3[k] and can(i + 1, j)) or
                    (j < n2 and s2[j] == s3[k] and can(i, j + 1)))
        return can(0, 0)


# ------------------------------- Demo + Timing -------------------------------
if __name__ == "__main__":
    samples = [
        # (s1, s2, s3, expected)
        ("AAB", "AAC", "AAAABC", True),
        ("AB", "C", "ACB", True),
        ("YX", "X", "XXY", False),
        ("", "abc", "abc", True),
        ("abc", "", "abc", True),
        ("abc", "def", "adbcef", True),
        ("abc", "def", "abdecf", True),
        ("abc", "def", "abdefc", False),
    ]

    sol = Solution()
    print("Row-compressed DP (O(n*m) time, O(m) space)")
    for s1, s2, s3, exp in samples:
        t = timeit.timeit(lambda: sol.isInterleave(s1, s2, s3), number=1)
        ans = sol.isInterleave(s1, s2, s3)
        print(f"s1={s1!r:>6}, s2={s2!r:>6}, s3={s3!r:>8}  -> {ans} (expected {exp})  time={t:.6f}s")

    print("\nMemoized recursion (O(n*m) states)")
    for s1, s2, s3, exp in samples[:3]:
        t = timeit.timeit(lambda: sol.isInterleave_memo(s1, s2, s3), number=1)
        ans = sol.isInterleave_memo(s1, s2, s3)
        print(f"s1={s1!r:>6}, s2={s2!r:>6}, s3={s3!r:>8}  -> {ans} (expected {exp})  time={t:.6f}s")
```

### Example output

```
Row-compressed DP (O(n*m) time, O(m) space)
s1='  AAB', s2='  AAC', s3=' AAAABC'  -> True (expected True)  time=0.0000xxs
s1='   AB', s2='    C', s3='    ACB'  -> True (expected True)  time=0.0000xxs
s1='   YX', s2='    X', s3='    XXY'  -> False (expected False) time=0.0000xxs
...

Memoized recursion (O(n*m) states)
s1='  AAB', s2='  AAC', s3=' AAAABC'  -> True (expected True)  time=0.0000xxs
s1='   AB', s2='    C', s3='    ACB'  -> True (expected True)  time=0.0000xxs
s1='   YX', s2='    X', s3='    XXY'  -> False (expected False) time=0.0000xxs
```

**Interview takeaways**

* Define `dp[i][j]` as “can `s1[:i]` & `s2[:j]` form `s3[:i+j]`?”
* Transition from **same column** (took from `s1`) or **left cell** (took from `s2`) **if characters match `s3[i+j-1]`**.
* Complexity: **O(n·m)** time, **O(m)** space with row compression.
* Always precheck `len(s1)+len(s2)==len(s3)`.

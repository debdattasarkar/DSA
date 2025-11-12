
---

# 🎭 Wildcard Pattern Matching

### Difficulty: Medium

**Accuracy:** 31.13%
**Submissions:** 92K+
**Points:** 4

---

## 🧠 Problem Statement

Given two strings **pat** and **txt**, which may be of different sizes, you have to return **true** if the wildcard pattern (i.e., `pat`) matches with the text (`txt`), else return **false**.

---

### Pattern Rules

The wildcard pattern `pat` can include the following special characters:

* `?` → matches **any single character**.
* `*` → matches **any sequence of characters** (including the empty sequence).

📝 **Note:**
The matching should cover the **entire text** (not partial).

---

## 🧩 Examples

### Example 1

**Input:**

```
txt = "abcde"
pat = "a?c*"
```

**Output:**

```
true
```

**Explanation:**
`?` matches with `'b'` and `*` matches with `"de"`.

---

### Example 2

**Input:**

```
txt = "baaabab"
pat = "a*ab"
```

**Output:**

```
false
```

**Explanation:**
The pattern starts with `'a'`, but the text starts with `'b'`, so it doesn’t match.

---

### Example 3

**Input:**

```
txt = "abc"
pat = "*"
```

**Output:**

```
true
```

**Explanation:**
`*` matches with the whole text `"abc"`.

---

## ⚙️ Constraints

* ( 1 \leq txt.size(), pat.size() \leq 100 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** ( O(n \times m) )
* **Auxiliary Space:** ( O(n \times m) )

---

## 🏢 Company Tags

**Zoho**, **Amazon**, **Microsoft**, **Ola Cabs**, **Walmart**, **Google**, **InMobi**, **United Health Group**

---

## 🧩 Topic Tags

* Dynamic Programming
* Algorithms
* Recursion
* Strings

---

## 💬 Related Interview Experiences

* Walmart Lab Interview Experience Set 9 Off Campus

---

## 📚 Related Articles

* [Wildcard Pattern Matching](https://www.geeksforgeeks.org/wildcard-pattern-matching/)

---

---

awesome — let’s make **Wildcard Pattern Matching** interview-ready.

---

# 2) Problem intuition + step-by-step dry run

## Goal

Return **True** iff pattern `pat` (with `?` and `*`) matches the **entire** text `txt`.

* `?` matches **exactly one** character.
* `*` matches **any sequence** (including empty).

## Core idea (DP)

Let `dp[i][j]` mean: does `pat[:i]` match `txt[:j]`?

* Answer we want: `dp[len(pat)][len(txt)]`.

Transitions (1-based indices for clarity):

* If `pat[i-1]` is a **letter**:
  `dp[i][j] = (pat[i-1] == txt[j-1]) and dp[i-1][j-1]`
* If `pat[i-1] == '?'`:
  `dp[i][j] = dp[i-1][j-1]`
* If `pat[i-1] == '*'`: two choices
  `dp[i][j] = dp[i-1][j]`  (star = empty) **or** `dp[i][j-1]` (star swallows one more char)

Base:

* `dp[0][0] = True`
* `dp[0][j>0] = False` (empty pattern can’t match nonempty text)
* `dp[i>0][0] = True` **iff** all of `pat[:i]` are `*` (because `*` can be empty)

### Dry run: `txt="abcde"`, `pat="a?c*"`

We’ll sketch the reasoning rather than the full table:

* `a` vs `a` → match → follow diagonal
* `?` vs `b` → match any 1 → follow diagonal
* `c` vs `c` → match → follow diagonal
* `*` at the end can absorb the rest (`"de"`) → success ⇒ **True**

Another quick edge:

* `txt="baaabab"`, `pat="a*ab"`: pattern starts with `a`, text with `b` ⇒ `dp[1][1]=False`, the only way to start is star, which we don’t have ⇒ **False**.

---

# 3) Python solutions (brute ➜ memo DP ➜ tabulation DP ➜ greedy)

All use your required signature:

```python
class Solution:
    def wildCard(self, txt, pat):
        # code here
```

## A) Brute force backtracking (teaching aid; exponential)

```python
class Solution:
    def wildCard(self, txt, pat):
        """
        Try all ways '*' can expand; '?' matches one char.
        Time:  Exponential worst-case
        Space: O(n+m) recursion
        """
        n, m = len(txt), len(pat)

        def dfs(i, j):
            # i -> index in pat, j -> index in txt
            if i == m:                 # pattern consumed
                return j == n          # must also finish text
            if j == n:
                # remaining pattern must be all '*' to match empty suffix
                return all(ch == '*' for ch in pat[i:])

            if pat[i] == '*':
                # 1) '*' = empty  OR  2) '*' consumes one char from text
                return dfs(i + 1, j) or dfs(i, j + 1)

            if pat[i] == '?' or pat[i] == txt[j]:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)
```

## B) Top-down DP (memoized) — **O(n·m)** time, **O(n·m)** space

```python
class Solution:
    def wildCard(self, txt, pat):
        """
        dp(i, j) => does pat[i:] match txt[j:] ?
        Time:  O(n*m) states, O(1) per state
        Space: O(n*m) memo + recursion
        """
        from functools import lru_cache
        n, m = len(txt), len(pat)

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return j == n
            if j == n:
                # pattern remainder must be only '*' to match empty
                return all(ch == '*' for ch in pat[i:])

            p = pat[i]
            if p == '*':
                # '*' is empty OR consumes one text char
                return dp(i + 1, j) or dp(i, j + 1)
            if p == '?' or p == txt[j]:
                return dp(i + 1, j + 1)
            return False

        return dp(0, 0)
```

## C) Bottom-up tabulation — **O(n·m)** time & space (most expected)

```python
class Solution:
    def wildCard(self, txt, pat):
        """
        Iterative DP: dp[i][j] => pat[:i] matches txt[:j]
        Time:  O(n*m)
        Space: O(n*m)
        """
        n, m = len(txt), len(pat)
        dp = [[False]*(n+1) for _ in range(m+1)]

        # base: empty pat & empty text
        dp[0][0] = True

        # base: pattern prefix matches empty text only if all '*' so far
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and (pat[i-1] == '*')

        for i in range(1, m+1):
            for j in range(1, n+1):
                p = pat[i-1]
                if p == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p == '?' or p == txt[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False

        return dp[m][n]
```

## D) Greedy two-pointer (very popular; near-linear; worst-case O(n·m))

This uses the classic technique: remember the last `*` position and where in the text we were when we used it; on mismatch, **backtrack only to the last `*`** and extend it by one more character.

```python
class Solution:
    def wildCard(self, txt, pat):
        """
        Greedy two-pointer with last-star backtracking.
        Time:  O(n + m) average; O(n*m) worst-case (pathological)
        Space: O(1)
        """
        i = j = 0               # j->txt, i->pat
        star_i = -1             # last seen '*' index in pattern
        star_match_j = -1       # text index when we decided '*' matched empty

        n, m = len(txt), len(pat)

        while j < n:
            if i < m and (pat[i] == '?' or pat[i] == txt[j]):
                # match one char
                i += 1; j += 1
            elif i < m and pat[i] == '*':
                # record star and assume it matches empty for now
                star_i = i
                star_match_j = j
                i += 1
            elif star_i != -1:
                # backtrack: let '*' match one more char from text
                i = star_i + 1
                star_match_j += 1
                j = star_match_j
            else:
                return False

        # consume trailing '*' in pattern
        while i < m and pat[i] == '*':
            i += 1

        return i == m
```

> Interview tip: if the platform expects **strict O(n·m)**, show the tabulation DP. If they like clever pointers, offer the greedy as an alternative and mention its worst-case.

---

# 4) Interview quick-recall + Q&A

## 5-line pseudo (DP)

```
dp[0][0] = True
dp[i][0] = dp[i-1][0] AND pat[i-1]=='*'
for i=1..m:
  for j=1..n:
    if pat[i-1]=='*': dp[i][j] = dp[i-1][j] OR dp[i][j-1]
    elif pat[i-1]=='?' or pat[i-1]==txt[j-1]: dp[i][j] = dp[i-1][j-1]
    else: dp[i][j] = False
return dp[m][n]
```

**Mnemonic:** **“Star = (Up OR Left), Question = Diagonal, Letter = Equal & Diagonal.”**

* `*` → `up` (empty) **or** `left` (swallow one).
* `?` → **diagonal**.
* regular char → **equal & diagonal**.

## Expected Q&A

**Q1. Why does `*` use `dp[i-1][j] or dp[i][j-1]`?**
Because `*` can match **empty** (move up: use one less pattern char) or **one more text char** (move left: keep the `*`, consume a text char).

**Q2. What are the bases?**
Empty pattern matches empty text (`dp[0][0]=True`), and only a prefix of `*` can match empty text.

**Q3. Time/space complexity?**
DP: **O(n·m)** time & space. Greedy: **O(n+m)** average; **O(n·m)** worst case.

**Q4. Greedy correctness intuition?**
Keep the most recent `*` and assume it matches empty. On mismatch, “grow” that `*` to cover more text (backtrack to `*` only). This simulates all partitions that assign text to the last star.

**Q5. Edge cases?**

* All `*` pattern (matches anything).
* Empty text with pattern of only `*`.
* Pattern starting with letters not matching first text letter.
* Multiple consecutive `*` (optional: compress to a single `*` for speed; DP already handles it).

---

---

awesome — here are the last two pieces for **Wildcard Pattern Matching**.

# 5) Real-World Use Cases (short, relatable)

* **File globs / CLI tools:** `*.py`, `src/*/test?.js` use exactly this wildcard logic.
* **Firewall / URL rules:** Match domains or paths like `*.example.com` or `/v1/*/items/?`.
* **Email / log filters:** Rules such as `subject:*invoice*` or `user?id=?123`.
* **Routers & API gateways:** Route templates `GET /users/*/orders/?` with `*` and `?`.
* **Search bars with wildcards:** Enterprise search that supports `?` and `*` patterns.

These all need **full-string** matching (not substring), exactly like this problem.

---

# 6) Full Python Program (timed, with inline complexity notes)

* Main method implements the **O(n·m) bottom-up DP** (most accepted in interviews).
* I also include an optional **greedy two-pointer** matcher for comparison.

```python
"""
Wildcard Pattern Matching — Full Program
----------------------------------------
Pattern 'pat' (with '?' and '*') must match the *entire* text 'txt'.

Rules:
  '?'  matches exactly one character
  '*'  matches any sequence (including empty)

We implement the classic DP:
  dp[i][j] = whether pat[:i] matches txt[:j]
Transitions:
  - if pat[i-1] == '*':
        dp[i][j] = dp[i-1][j]   # '*' = empty
                 or dp[i][j-1]  # '*' consumes txt[j-1]
  - elif pat[i-1] == '?' or pat[i-1] == txt[j-1]:
        dp[i][j] = dp[i-1][j-1]
  - else:
        dp[i][j] = False

Complexities (bottom-up DP):
  Time:  O(n * m)  where n=len(txt), m=len(pat)
  Space: O(n * m)

Greedy (optional):
  Time:  O(n + m) average; O(n * m) worst-case
  Space: O(1)
"""

import timeit

class Solution:
    # ---------- Interview-standard DP solution ----------
    def wildCard(self, txt, pat):
        """
        Bottom-up DP:
          dp[i][j] => pat[:i] matches txt[:j]

        Step-by-step complexity:
          - Initialize dp table: O((n+1)*(m+1)) space & O(n+m) time
          - Double loop fills each state once: O(n*m) time
          => Total time O(n*m), space O(n*m)
        """
        n, m = len(txt), len(pat)
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # O(n*m) space

        # Base: empty pattern matches empty text
        dp[0][0] = True

        # Base: pattern prefix vs empty text -> must be all '*'
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and (pat[i - 1] == '*')

        # Fill table
        for i in range(1, m + 1):
            p = pat[i - 1]
            for j in range(1, n + 1):
                if p == '*':
                    # '*' matches empty (up) OR swallows one char (left)
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p == '?' or p == txt[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False

        return dp[m][n]

    # ---------- Optional: Greedy two-pointer (quick & neat) ----------
    def wildCard_greedy(self, txt, pat):
        """
        Greedy with backtracking to the last '*'.
        Avg Time: O(n+m); Worst: O(n*m)
        Space: O(1)
        """
        i = j = 0                 # i -> pat, j -> txt
        star_i, star_j = -1, -1   # last star position & the txt index matched so far

        while j < len(txt):
            if i < len(pat) and (pat[i] == '?' or pat[i] == txt[j]):
                i += 1; j += 1                         # match one character
            elif i < len(pat) and pat[i] == '*':
                star_i, star_j = i, j                  # remember star
                i += 1                                 # assume '*' = empty for now
            elif star_i != -1:
                i = star_i + 1                         # backtrack: grow '*'
                star_j += 1
                j = star_j
            else:
                return False

        # consume trailing stars
        while i < len(pat) and pat[i] == '*':
            i += 1
        return i == len(pat)


# --------------------------- Demo + Timing ---------------------------
if __name__ == "__main__":
    tests = [
        # (text, pattern, expected)
        ("abcde", "a?c*", True),
        ("baaabab", "a*ab", False),
        ("abc", "*", True),
        ("", "", True),
        ("", "*", True),
        ("", "?", False),
        ("abcd", "ab*d", True),
        ("abcd", "ab*e", False),
        ("mississippi", "m??*ss*?i*pi", False),
    ]

    sol = Solution()

    print("Bottom-up DP matcher (O(n*m))")
    for t, p, exp in tests:
        elapsed = timeit.timeit(lambda: sol.wildCard(t, p), number=1)
        ans = sol.wildCard(t, p)
        print(f"txt={t!r:>12}, pat={p!r:>14} -> {ans} (expected {exp}), time={elapsed:.6f}s")

    print("\nGreedy matcher (avg O(n+m))")
    for t, p, exp in tests:
        elapsed = timeit.timeit(lambda: sol.wildCard_greedy(t, p), number=1)
        ans = sol.wildCard_greedy(t, p)
        print(f"txt={t!r:>12}, pat={p!r:>14} -> {ans} (expected {exp}), time={elapsed:.6f}s")
```

### What a run looks like

```
Bottom-up DP matcher (O(n*m))
txt='     abcde', pat='           a?c*' -> True (expected True), time=0.0000xxs
txt='   baaabab', pat='            a*ab' -> False (expected False), time=0.0000xxs
txt='        abc', pat='               *' -> True (expected True), time=0.0000xxs
...
Greedy matcher (avg O(n+m))
txt='     abcde', pat='           a?c*' -> True (expected True), time=0.0000xxs
...
```

**Interview takeaways**

* If they want **guaranteed** complexity, present the **DP** (`O(n·m)`).
* If they like pointer tricks, present the **greedy** and mention its **worst-case**.
* Quick mnemonic for DP transitions:
  **“Star = Up OR Left; Question = Diagonal; Letter = Equal & Diagonal.”**

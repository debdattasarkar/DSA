# Edit Distance

**Difficulty:** Hard
**Accuracy:** 35.14%
**Submissions:** 244K+
**Points:** 8

---

Given two strings `s1` and `s2`. Return the **minimum number of operations** required to convert `s1` to `s2`.

The possible operations are permitted:

1. **Insert** a character at any position of the string.
2. **Remove** any character from the string.
3. **Replace** any character from the string with any other character.

---

## Examples

### Example 1

**Input:** `s1 = "geek"`, `s2 = "gesek"`
**Output:** `1`
**Explanation:** One operation is required, inserting `'s'` between two `'e'` in `s1`.

### Example 2

**Input:** `s1 = "gfg"`, `s2 = "gfg"`
**Output:** `0`
**Explanation:** Both strings are same.

### Example 3

**Input:** `s1 = "abcd"`, `s2 = "bcfe"`
**Output:** `3`
**Explanation:** We can convert `s1` into `s2` by removing `'a'`, replacing `'d'` with `'f'` and inserting `'e'` at the end.

---

## Constraints

* `1 ≤ s1.length(), s2.length() ≤ 10^3`
* Both the strings are in lowercase.

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## Company Tags

* `Amazon`, `Microsoft`, `Goldman Sachs`, `Google`

---

## Topic Tags

* `Strings`, `Dynamic Programming`, `Data Structures`, `Algorithms`

---

## Related Articles

* [*Edit Distance DP 5*](https://www.geeksforgeeks.org/edit-distance-dp-5/)

---

---

Here’s the clean interview-style package for **Edit Distance (Levenshtein distance)**.

---

## 2) Concept & step-by-step dry run

### What we’re minimizing

To convert `s1` → `s2` we may:

* **Insert** a char in `s1`
* **Delete** a char from `s1`
* **Replace** a char in `s1`

Let `dp[i][j]` = minimum edits to convert the **first `i` chars of `s1`** to the **first `j` chars of `s2`**.

**Transitions**

* If `s1[i-1] == s2[j-1]`:
  `dp[i][j] = dp[i-1][j-1]` (nothing to do for this char)
* Else (chars differ), choose the best among:

  * **Insert** `s2[j-1]`: `dp[i][j-1] + 1`
  * **Delete** `s1[i-1]`: `dp[i-1][j] + 1`
  * **Replace** `s1[i-1]` with `s2[j-1]`: `dp[i-1][j-1] + 1`

**Base cases**

* `dp[0][j] = j` (turn empty into `s2[:j]` → j inserts)
* `dp[i][0] = i` (turn `s1[:i]` into empty → i deletes)

### Dry run on small example

Convert `s1="geek"` → `s2="gesek"` (answer = 1)

We’ll fill a `(len(s1)+1) x (len(s2)+1)` grid.

```
      ''  g  e  s  e  k
   ----------------------
'' |  0  1  2  3  4  5
g  |  1  0  1  2  3  4
e  |  2  1  0  1  2  3
e  |  3  2  1  1* 1  2
k  |  4  3  2  2  2  1
```

* Row/col 0 = base cases.
* At `*` (i=3,j=3): chars differ (`e` vs `s`).
  min(insert=dp[3][2]+1=2, delete=dp[2][3]+1=2, replace=dp[2][2]+1=1) ⇒ 1.
* Eventually `dp[4][5] = 1`: insert `'s'` between the two `'e'`.

---

## 3) Optimized Python solutions (multiple ways)

### A) Brute force (top-down recursion) — clear but exponential

```python
# Exponential (for teaching only): O(3^(n+m)) time, O(n+m) stack
class Solution:
    def editDistance(self, s1, s2):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            # edits to convert s1[i:] -> s2[j:]
            if i == len(s1):  # only inserts left
                return len(s2) - j
            if j == len(s2):  # only deletes left
                return len(s1) - i

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)  # no cost

            ins  = 1 + dfs(i, j + 1)     # insert s2[j]
            dele = 1 + dfs(i + 1, j)     # delete s1[i]
            repl = 1 + dfs(i + 1, j + 1) # replace s1[i]→s2[j]
            return min(ins, dele, repl)

        return dfs(0, 0)
```

> Uses memoization to make it pseudo-DP (now **O(n·m)**). It’s the most “interview talk-through” friendly.

---

### B) Bottom-up DP (tabulation) — standard, easy to reason about

```python
# Time: O(n*m), Space: O(n*m)
class Solution:
    def editDistance(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        # base rows/cols
        for i in range(n+1): dp[i][0] = i   # delete all i chars
        for j in range(m+1): dp[0][j] = j   # insert all j chars

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]             # no-op
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j-1],   # insert
                        dp[i-1][j],   # delete
                        dp[i-1][j-1]  # replace
                    )
        return dp[n][m]
```

---

### C) Space-optimized DP (1D rolling array)

```python
# Time: O(n*m), Space: O(min(n,m))
# Keeps only previous row; great for large strings.
class Solution:
    def editDistance(self, s1, s2):
        # Ensure s2 is the shorter dimension for less memory
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        n, m = len(s1), len(s2)

        prev = list(range(m+1))  # dp[0][*]
        for i in range(1, n+1):
            curr = [i] + [0]*m   # dp[i][0] = i
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(
                        curr[j-1],   # insert
                        prev[j],     # delete
                        prev[j-1]    # replace
                    )
            prev = curr
        return prev[m]
```

---

## 4) Common interviewer Q&A

**Q1. Why do the three transitions correspond to insert/delete/replace?**

* From `(i,j)`, inserting `s2[j]` means we consume `s2[j]` but keep `s1[i]` → `(i, j+1)` plus cost 1.
* Deleting `s1[i]` consumes `s1[i]` but not `s2[j]` → `(i+1, j)` plus cost 1.
* Replacing `s1[i]` with `s2[j]` consumes both → `(i+1, j+1)` plus cost 1.

**Q2. Why `dp[0][j]=j` and `dp[i][0]=i`?**
Turning empty into `j` chars needs `j` inserts; turning `i` chars into empty needs `i` deletes.

**Q3. Can we reconstruct the actual edit script?**
Yes. Store back-pointers (which choice led to `dp[i][j]`) and walk from `(n,m)` back to `(0,0)` to list operations.

**Q4. What if operations had different costs?**
Just change the `+1` to the respective costs; DP structure stays the same.

**Q5. Differences vs. Longest Common Subsequence (LCS)?**
LCS counts matches; Levenshtein counts edits. Relationship: if only insert/delete are allowed, `edits = n + m - 2*LCS`.

**Q6. Edge cases?**
Empty strings, identical strings, completely different strings, highly repeated characters.

---

### Complexity summary

* **Time:** `O(n*m)` (DP versions)
* **Space:** `O(n*m)` for full table, `O(min(n,m))` with rolling array.

---

---

Here’s a **self-contained, runnable Python program** for **Edit Distance (Levenshtein distance)** that:

* follows the required class/method signature,
* includes **inline time/space complexity notes** at each major step,
* shows **example inputs and outputs**, and
* measures runtime using `timeit` inline with `__main__`.

---

```python
"""
Edit Distance (Levenshtein distance)
------------------------------------
Convert s1 -> s2 by insert/delete/replace with minimum operations.

This script:
1) Implements Solution.editDistance(s1, s2) using space-optimized DP.
2) Prints example inputs and outputs.
3) Benchmarks the full program using timeit (single run shown in ms).

Author note: All complexities below are for string lengths n = len(s1), m = len(s2).
"""

from timeit import timeit

class Solution:
    def editDistance(self, s1: str, s2: str) -> int:
        """
        Space-optimized bottom-up DP.
        Time  : O(n*m) because we touch each cell of the n x m DP grid exactly once.
        Space : O(min(n, m)) by keeping only one previous row.
        """
        # Ensure we use the *shorter* string for columns to minimize space.
        # Swap if needed. This does not change the answer.
        # Time: O(1)  |  Space: O(1)
        if len(s1) < len(s2):
            s1, s2 = s2, s1  # make s2 the shorter dimension

        n, m = len(s1), len(s2)          # Time: O(1) | Space: O(1)
        prev = list(range(m + 1))        # dp[0][*] (convert empty -> s2[:j])  Space: O(m)
        # Base row initialization cost:
        # Time: O(m) to create list(range(m+1))

        # Build DP row by row: i = 1..n
        # Outer loop runs n times => contributes O(n).
        for i in range(1, n + 1):        # Time: O(n)
            curr = [i] + [0] * m         # dp[i][0] = i (delete i chars)  Space: O(m)
            # Inner loop over j = 1..m => total O(m) per i, O(n*m) overall.
            for j in range(1, m + 1):    # Time: O(m) per row
                if s1[i - 1] == s2[j - 1]:
                    # No operation needed; carry diagonal value.
                    # Time/Step: O(1)
                    curr[j] = prev[j - 1]
                else:
                    # 1 + min(insert, delete, replace)
                    # All three lookups are O(1) table reads.
                    # Time/Step: O(1)
                    curr[j] = 1 + min(
                        curr[j - 1],   # insert  -> dp[i][j-1]
                        prev[j],       # delete  -> dp[i-1][j]
                        prev[j - 1]    # replace -> dp[i-1][j-1]
                    )
            prev = curr  # roll the row; Space stays O(m)

        # Final cell dp[n][m] is in prev[m] after last roll.
        # Time: O(1)
        return prev[m]


# ---- Example usage + benchmarking ----
def demo_and_benchmark():
    sol = Solution()

    # Example testcases (can add more)
    tests = [
        ("geek", "gesek"),   # 1 (insert 's')
        ("gfg",  "gfg"),     # 0
        ("abcd", "bcfe"),    # 3 (delete 'a', replace 'd'->'f', insert 'e')
        ("intention", "execution"),  # classic: 5
    ]

    print("Edit Distance Examples")
    print("-" * 28)
    for s1, s2 in tests:
        ans = sol.editDistance(s1, s2)
        print(f"s1 = {s1!r:12}  s2 = {s2!r:12}  ->  edit distance = {ans}")
    print()

    # Benchmark the *whole* solve step for a moderately sized case.
    bench_s1 = "kitten" * 200     # length 1200
    bench_s2 = "sitting" * 150    # length 1050

    def run_once():
        _ = sol.editDistance(bench_s1, bench_s2)

    # One timing sample; increase number=3 for a simple average.
    elapsed = timeit(run_once, number=1)
    print("Timing")
    print("-" * 28)
    print(f"editDistance(len={len(bench_s1)}, len={len(bench_s2)}) took {elapsed*1000:.2f} ms (1 run)")

if __name__ == "__main__":
    demo_and_benchmark()
```

### What you’ll see when you run it

```
Edit Distance Examples
----------------------------
s1 = 'geek'        s2 = 'gesek'       ->  edit distance = 1
s1 = 'gfg'         s2 = 'gfg'         ->  edit distance = 0
s1 = 'abcd'        s2 = 'bcfe'        ->  edit distance = 3
s1 = 'intention'   s2 = 'execution'   ->  edit distance = 5

Timing
----------------------------
editDistance(len=1200, len=1050) took  XXX.XX ms (1 run)
```

(The timing will vary by machine and Python version.)

---

## 6) Real-World Use Cases (most important)

1. **Spell-checking & autocorrect:** Measure how “close” a typed token is to dictionary entries to suggest fixes.
2. **Fuzzy search & autocomplete:** Rank candidates by edit distance from user query to surface best matches.
3. **DNA / protein sequence comparison:** Basic string edit distance (or variants) as a similarity metric.
4. **Data deduplication / record linkage:** Merge near-duplicate entries (e.g., “Jon Smith” vs “John Smith”).
5. **Plagiarism / code similarity signals:** As a feature among others to score textual/code similarity.

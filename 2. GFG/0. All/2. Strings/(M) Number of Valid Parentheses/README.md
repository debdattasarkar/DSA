# Number of Valid Parentheses

**Difficulty:** Medium  
**Accuracy:** 62.85%  
**Submissions:** 11K+  
**Points:** 4  
**Average Time:** 30m  

---

## Problem Statement

You are given a number **n**, your task is to find the number of **all the valid parentheses expressions** of that length using only `"("` and `")"` brackets.

An input string of parentheses is valid if:

- Open brackets must be closed in **correct order**.
- **Every** close bracket has a corresponding open bracket.

For example - `"()"` or `"(())"` are valid while `")(()"` or `"))(("` are invalid parentheses expressions.

---

## Examples

### Example 1
**Input:** `n = 2`  
**Output:** `1`  
**Explanation:** There is only one possible valid expressions of length 2 i.e., `"()"`.

### Example 2
**Input:** `n = 4`  
**Output:** `2`  
**Explanation:** Possible valid expressions of length 4 are `"(())"` and `"()()"`.

### Example 3
**Input:** `n = 6`  
**Output:** `5`  
**Explanation:** Possible valid expressions of length 6 are `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"` and `"()()()"`.

---

## Constraints

- `1 ≤ n ≤ 20`

---

## Expected Complexities

- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

---

Below is the complete interview-style explanation + dry run + Python solutions (easy DP and Catalan formula), all in the requested `class Solution` format, plus interviewer Q&A.

---

## 2) Text explanation (what the problem is really asking)

We need the **count** of valid parentheses strings of **length `n`** made only of `(` and `)`.

Key facts:

* A valid parentheses string must have **equal number** of `(` and `)` ⇒ **`n` must be even**.
* Let `pairs = n/2`. The answer is the **pairs-th Catalan number**.

So:

* If `n` is odd ⇒ answer = `0`
* Else answer = `Catalan(pairs)`

---

## Step-by-step dry run (DP approach)

### DP idea (classic and interview-friendly)

Let:

* `dp[i]` = number of valid parentheses strings using **i pairs**.

For i pairs:
Choose where the **first** `(` matches.
If it encloses `j` pairs inside, then outside remains `i-1-j` pairs.

So:
[
dp[i] = \sum_{j=0}^{i-1} dp[j] \times dp[i-1-j]
]
Base:

* `dp[0] = 1` (empty string is “one way”)

### Dry run for `n = 6`

* `pairs = 3`

Initialize:

* `dp[0] = 1`

Compute:

* `dp[1] = dp[0]*dp[0] = 1`
* `dp[2] = dp[0]*dp[1] + dp[1]*dp[0] = 1*1 + 1*1 = 2`
* `dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]`
  = `1*2 + 1*1 + 2*1`
  = `2 + 1 + 2 = 5`

Answer = `dp[3] = 5`

Matches example.

---

## 3) Python optimized codes (brute-ish and interview-expected)

### A) “Brute & easy to understand” (Backtracking generate + validate count)

This is conceptually brute-force **generation of only valid strings** (so not as bad as checking all `2^n` strings).
Time grows fast but ok for small `n` and super intuitive.

```python
class Solution:
    def findWays(self, n):
        # If length is odd, cannot form valid parentheses
        if n % 2 == 1:
            return 0

        total_pairs = n // 2
        count = 0

        def backtrack(open_used, close_used):
            nonlocal count

            # If we used all pairs, we formed one valid expression
            if open_used == total_pairs and close_used == total_pairs:
                count += 1
                return

            # Try placing '(' if we still have opens left
            if open_used < total_pairs:
                backtrack(open_used + 1, close_used)

            # Try placing ')' only if it won't break validity
            # i.e., we cannot close more than we opened
            if close_used < open_used:
                backtrack(open_used, close_used + 1)

        backtrack(0, 0)
        return count
```

---

### B) Most expected in interviews: DP (Catalan via recurrence)

Very standard, easy to explain, and passes constraints.

```python
class Solution:
    def findWays(self, n):
        # Odd length cannot form balanced parentheses
        if n % 2 == 1:
            return 0

        pairs = n // 2

        # dp[i] = number of valid parentheses expressions with i pairs
        dp = [0] * (pairs + 1)
        dp[0] = 1  # one way to arrange 0 pairs: empty string

        for i in range(1, pairs + 1):
            ways = 0
            # split i pairs into: (inside has j pairs) + (outside has i-1-j pairs)
            for inside_pairs in range(i):
                outside_pairs = i - 1 - inside_pairs
                ways += dp[inside_pairs] * dp[outside_pairs]
            dp[i] = ways

        return dp[pairs]
```

---

### C) Fastest + O(1) extra space: Direct Catalan formula (multiplicative)

Catalan(k) = C(2k, k) / (k+1)

We compute the binomial safely using integer multiplication/division.

```python
class Solution:
    def findWays(self, n):
        if n % 2 == 1:
            return 0

        k = n // 2  # number of pairs

        # Compute binomial(2k, k) using multiplicative method
        binom = 1
        # C(2k, k) = product_{i=1..k} (k+i)/i
        for i in range(1, k + 1):
            binom = binom * (k + i) // i

        # Catalan(k) = C(2k, k) / (k+1)
        return binom // (k + 1)
```

---

## 4) Interview memory trick + expected Q&A

### How to remember quickly in an interview

Use this mental script:

1. **Check parity**: “If `n` is odd, answer is 0.”
2. Convert length to pairs: `pairs = n/2`
3. **Catalan** triggers: “Balanced parentheses count = Catalan(pairs).”
4. Pick method:

   * Explain using **DP recurrence** (safe and common)
   * Mention formula optimization if asked

**One-liner memory hook:**

> “Balanced parentheses = Catalan. DP split by first matching bracket.”

---

## Expected Interview Questions & Answers

### Q1) Why is answer 0 for odd `n`?

**A:** A valid parentheses string must have equal `(` and `)`. Total length must be even to split equally.

### Q2) What is the recurrence and why does it work?

**A:** For `i` pairs, the first `(` must match some `)`.
If inside that pair there are `j` pairs, outside there are `i-1-j`.
Independent combinations ⇒ multiply: `dp[j] * dp[i-1-j]`. Summing over all `j` gives:
`dp[i] = Σ dp[j] * dp[i-1-j]`.

### Q3) What is `dp[0]` and why is it 1?

**A:** `dp[0]=1` represents the empty arrangement. It’s important as a neutral multiplier in combinations.

### Q4) What is the time complexity of the DP?

**A:** `O(pairs^2)` where `pairs = n/2`. With `n ≤ 20`, it’s tiny.

### Q5) Can we do faster?

**A:** Yes, using Catalan formula `C(2k,k)/(k+1)` with multiplicative binomial computation. Time `O(k)` and space `O(1)`.

### Q6) How would you generate all valid strings (not just count)?

**A:** Use backtracking with constraints:

* add `(` if open < pairs
* add `)` if close < open

### Q7) Why can’t we just brute force all `2^n` strings?

**A:** That’s exponential and wastes time checking invalid prefixes. Backtracking prunes invalid states early.

---

---

## 5) Real-world use cases (few, high-signal)

1. **Compiler / Interpreter parsing**

   * Languages use nested structures: parentheses `()`, braces `{}`, brackets `[]`.
   * Counting valid structures is directly related to how many valid parse trees / nested blocks can exist for a given size (Catalan structures).

2. **IDE / Linter bracket auto-complete & validation**

   * Editors check “balanced and properly nested” delimiters in real time.
   * The same validity rule is used by syntax highlighters, formatters, and linters.

3. **Correct pairing of “open/close” operations in systems**

   * Examples: `open/close` file handles, `lock/unlock`, `begin/commit` transactions, nested API calls.
   * Valid sequences must never “close before open” and must close all opens → same constraint as parentheses.

---

## 6) Full Python program (with inline complexity + sample I/O + runtime timing)

* Uses **Catalan formula** (fastest, matches expected `O(n)` time and `O(1)` space).
* Prints execution time to **stderr** so normal outputs remain clean.

```python
import sys
import time

class Solution:
    def findWays(self, n):
        """
        Counts valid parentheses expressions of total length n.

        Key idea:
        - If n is odd -> 0
        - Let k = n/2 pairs
        - Answer = Catalan(k) = C(2k, k) / (k + 1)

        Time Complexity: O(k)  (k = n/2)  => O(n)
        Space Complexity: O(1)
        """
        # Step 1: Parity check
        # Time: O(1), Space: O(1)
        if n % 2 == 1:
            return 0

        # Step 2: Convert length to pairs
        # Time: O(1), Space: O(1)
        k = n // 2

        # Step 3: Compute binomial C(2k, k) in O(k) time using multiplicative formula
        # C(2k, k) = product_{i=1..k} (k+i)/i
        # Time: O(k), Space: O(1)
        binomial = 1
        for i in range(1, k + 1):
            binomial = binomial * (k + i) // i  # exact integer division

        # Step 4: Catalan(k) = C(2k, k) / (k + 1)
        # Time: O(1), Space: O(1)
        return binomial // (k + 1)


def main():
    """
    Input format (common in interviews/CP):
    - First line: t (number of test cases)
    - Next t lines: n

    Output:
    - For each test case, print the answer in a new line
    """
    start_time = time.perf_counter()  # measure full program run time

    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    solver = Solution()

    out_lines = []
    idx = 1

    # Total per test case:
    # - findWays runs in O(n) time and O(1) space
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        out_lines.append(str(solver.findWays(n)))

    sys.stdout.write("\n".join(out_lines))

    end_time = time.perf_counter()
    # Print timing to stderr so it doesn't interfere with expected stdout answers
    print(f"\n[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
3
2
4
6

Expected Output:
1
2
5
"""
```

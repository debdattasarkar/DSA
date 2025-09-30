# Boolean Parenthesization

**Difficulty:** Hard
**Accuracy:** 20.15%
**Submissions:** 137K+
**Points:** 8
**Average Time:** 30m

---

You are given a boolean expression **s** containing

* `'T'` ⟶ true
* `'F'` ⟶ false

and the following operators between symbols

* `&` ⟶ boolean **AND**
* `|` ⟶ boolean **OR**
* `^` ⟶ boolean **XOR**

Count the number of ways we can **parenthesize** the expression so that the value of the expression evaluates to **true**.

**Note:** The answer is guaranteed to fit within a **32-bit** integer.

---

## Examples

### Example 1

**Input:** `s = "T|T&F^T"`
**Output:** `4`
**Explanation:** The expression evaluates to true in **4** ways: `((T|T)&(F^T))`, `(T|(T&(F^T)))`, `(((T|T)&F)^T)` and `(T|((T&F)^T))`.

### Example 2

**Input:** `s = "T^F|F"`
**Output:** `2`
**Explanation:** The expression evaluates to true in **2** ways: `((T^F)|F)` and `(T^(F|F))`.

---

## Constraints

* `1 ≤ |s| ≤ 100`

---

## Expected Complexities

* **Time Complexity:** `O(n^3)`
* **Auxiliary Space:** `O(n^2)`

---

## Company Tags

Amazon • Microsoft • Intuit • Linkedin

---

## Topic Tags

Dynamic Programming • Algorithms

---

## Related Interview Experiences

* Intuit Interview Experience On Campus 2021

---

## Related Articles

* Boolean Parenthesization Problem Dp 37

---

---

awesome — let’s make **Boolean Parenthesization** crystal clear and interview-ready.

# 2) Explanation + step-by-step dry run

**Task.** String `s` alternates symbols and operators, e.g. `T|F&T^T`.
Symbols: `'T'` (true), `'F'` (false).
Operators: `&` (AND), `|` (OR), `^` (XOR).
Count how many parenthesizations of `s` evaluate to **true**.

## Core DP idea (most expected)

Work on **substrings of operands** (not raw characters).

* Split `s` into:

  * `sym[0..n-1]`: the `n` operands (characters at even indices of `s`)
  * `ops[0..n-2]`: the `n-1` operators (characters at odd indices)
* Let:

  * `T[i][j]` = number of ways `sym[i..j]` evaluates to **true**
  * `F[i][j]` = number of ways `sym[i..j]` evaluates to **false**

Base (length 1):

```
T[i][i] = 1 if sym[i]=='T' else 0
F[i][i] = 1 if sym[i]=='F' else 0
```

Transition for length ≥ 2: pick a split `k` (i ≤ k < j) at operator `ops[k]`,
combine left `i..k` with right `k+1..j` via truth tables:

For `&`:

```
true  += LT * RT
false += LT*RF + LF*RT + LF*RF
```

For `|`:

```
true  += LT*RT + LT*RF + LF*RT
false += LF * RF
```

For `^`:

```
true  += LT*RF + LF*RT
false += LT*RT + LF*RF
```

(Here `LT=T[i][k]`, `LF=F[i][k]`, `RT=T[k+1][j]`, `RF=F[k+1][j]`.)

Answer: `T[0][n-1]`.
**Complexity:** There are `O(n^2)` intervals, each tries `O(n)` splits ⇒ **`O(n^3)` time**, **`O(n^2)` space** — exactly what the prompt expects.

---

## Dry run on `s = "T|T&F^T"` (answer = 4)

Tokens: `sym = [T, T, F, T]` (n=4), `ops = [|, &, ^]`.

### Length = 1

```
T[i][i]: [1, 1, 0, 1]
F[i][i]: [0, 0, 1, 0]
```

### Length = 2

* i=0,j=1, op='|':

  * true = 1*1 + 1*0 + 0*1 = 1 ; false = 0
* i=1,j=2, op='&':

  * true = 1*0 = 0 ; false = 1*1 + 0*0 + 0*1 = 1
* i=2,j=3, op='^':

  * true = 0*0 + 1*1 = 1 ; false = 0*1 + 1*0 = 0

### Length = 3

* i=0,j=2:

  * split k=0 '|' → contributes true=1, false=0
  * split k=1 '&' → contributes true=0, false=1
    ⇒ T=1, F=1
* i=1,j=3:

  * k=1 '&' with (T,F)=(1,0) and (1,0) → T+=1
  * k=2 '^' with (0,1) and (1,0) → T+=1
    ⇒ T=2, F=0

### Length = 4

* i=0,j=3:

  * k=0 '|' with T(0..0)=1 and T(1..3)=2 → T+=2
  * k=1 '&' with T(0..1)=1 and T(2..3)=1 → T+=1 (total 3)
  * k=2 '^' with (T,F)=(1,1) and (1,0) → T+=1 (total **4**)

Answer `T[0][3] = 4`.

---

# 3) Python solutions (interview-friendly)

### A) Bottom-up `O(n^3)` DP (most expected)

```python
#User function Template for python3
class Solution:
    def countWays(self, s):
        """
        Bottom-up interval DP over operands.

        Time:  O(n^3) where n = number of operands = (len(s)+1)//2
        Space: O(n^2) for two DP tables (true/false counts)
        """
        # 1) Tokenize operands and operators
        sym = s[::2]           # operands at even indices
        ops = s[1::2]          # operators at odd indices
        n = len(sym)
        if n == 0:
            return 0
        if n == 1:
            return 1 if sym[0] == 'T' else 0

        # 2) DP tables: T[i][j], F[i][j]
        T = [[0] * n for _ in range(n)]
        F = [[0] * n for _ in range(n)]

        # Base: single operand
        for i in range(n):
            if sym[i] == 'T':
                T[i][i] = 1
            else:
                F[i][i] = 1

        # 3) Fill by increasing interval length
        for length in range(2, n + 1):        # substring of operands
            for i in range(0, n - length + 1):
                j = i + length - 1
                t_ways = 0
                f_ways = 0
                # Try every split point k (operator at ops[k])
                for k in range(i, j):
                    LT, LF = T[i][k], F[i][k]
                    RT, RF = T[k + 1][j], F[k + 1][j]
                    op = ops[k]
                    if op == '&':
                        t_ways += LT * RT
                        f_ways += LT*RF + LF*RT + LF*RF
                    elif op == '|':
                        t_ways += LT*RT + LT*RF + LF*RT
                        f_ways += LF * RF
                    else:  # op == '^'
                        t_ways += LT*RF + LF*RT
                        f_ways += LT*RT + LF*RF
                T[i][j], F[i][j] = t_ways, f_ways

        return T[0][n - 1]
```

---

### B) Top-down recursion + memo (same complexity, easy to derive)

```python
#User function Template for python3
from functools import lru_cache

class Solution:
    def countWays(self, s):
        """
        Memoized recursion on (i, j, wantTrue).

        Time:  O(n^3) states/transitions
        Space: O(n^2) memo + recursion depth O(n)
        """
        sym = s[::2]
        ops = s[1::2]
        n = len(sym)

        @lru_cache(maxsize=None)
        def solve(i, j, wantTrue):
            # Single symbol
            if i == j:
                val = (sym[i] == 'T')
                return 1 if val == wantTrue else 0

            ways = 0
            for k in range(i, j):  # split at op[k]
                op = ops[k]
                # Counts for left and right
                LT = solve(i, k, True)
                LF = solve(i, k, False)
                RT = solve(k + 1, j, True)
                RF = solve(k + 1, j, False)

                if op == '&':
                    if wantTrue:
                        ways += LT * RT
                    else:
                        ways += LT*RF + LF*RT + LF*RF
                elif op == '|':
                    if wantTrue:
                        ways += LT*RT + LT*RF + LF*RT
                    else:
                        ways += LF * RF
                else:  # '^'
                    if wantTrue:
                        ways += LT*RF + LF*RT
                    else:
                        ways += LT*RT + LF*RF
            return ways

        return solve(0, n - 1, True)
```

---

### C) Educational brute (no memo) — exponential (use only to show contrast)

```python
#User function Template for python3
class Solution:
    def countWays(self, s):
        """
        Pure recursion enumerating all parenthesizations.
        Time:  exponential in number of operands (Catalan-like growth)
        Space: O(n) recursion depth
        """
        sym = s[::2]
        ops = s[1::2]
        n = len(sym)

        def rec(i, j):
            # returns (trueWays, falseWays)
            if i == j:
                return (1, 0) if sym[i] == 'T' else (0, 1)

            Ttot = Ftot = 0
            for k in range(i, j):
                LT, LF = rec(i, k)
                RT, RF = rec(k + 1, j)
                op = ops[k]
                if op == '&':
                    Ttot += LT * RT
                    Ftot += LT*RF + LF*RT + LF*RF
                elif op == '|':
                    Ttot += LT*RT + LT*RF + LF*RT
                    Ftot += LF * RF
                else:  # '^'
                    Ttot += LT*RF + LF*RT
                    Ftot += LT*RT + LF*RF
            return Ttot, Ftot

        return rec(0, n - 1)[0]
```

---

# 4) Likely interviewer Q&A

**Q1. What are your DP states and why two tables?**
`T[i][j]` and `F[i][j]` count ways a substring evaluates to True/False.
At each split, different operator truth tables mix **both** true and false counts, so tracking both is essential.

**Q2. Why `O(n^3)` time?**
There are `O(n^2)` substrings `(i,j)` and each tries `O(n)` split points `k`, doing `O(1)` work per `k`.

**Q3. How do you parse `s`?**
Expression is well-formed and alternates operand/operator. So operands are `s[::2]`, operators `s[1::2]`. This avoids writing a full parser.

**Q4. Any modulo?**
The prompt says it fits in 32-bit; no modulo needed. If a platform asks for modulo (e.g., `1e9+7`), just do `ways %= MOD` at each accumulation.

**Q5. Edge cases?**

* Single symbol (`"T"`/`"F"`) → 1/0 respectively.
* All same operator still works (AND/OR/XOR tables handle it).
* Empty string not expected per constraints.

**Q6. Can you reduce space?**
You can store pairs `(T,F)` in one table or even use dictionaries for sparse intervals; asymptotic space remains `O(n^2)`.

**Q7. Compare bottom-up vs top-down.**
Bottom-up is iterative, often faster in Python due to fewer recursion calls.
Top-down is easier to derive and implement first; memoization guarantees the same `O(n^3)` bound.

---

---

you got it — here’s a clean, **runnable** script for **Boolean Parenthesization** using the classic **bottom-up `O(n^3)` DP** (the version interviewers expect), with:

* inline comments calling out **time & space complexity** per step,
* a small **driver** that prints **inputs and outputs**,
* overall **timing** via `timeit.default_timer`,
* robust tokenization (ignores whitespace) and compatibility with the common `(N, S)` signature used by some judges.

---

```python
#!/usr/bin/env python3
"""
Boolean Parenthesization — count the number of parenthesizations
that make the expression evaluate to True.

Symbols: 'T' (true), 'F' (false)
Operators: '&' (AND), '|' (OR), '^' (XOR)

We implement the MOST-EXPECTED bottom-up interval DP:
  - Let T[i][j] = #ways operands[i..j] evaluate to True
  - Let F[i][j] = #ways operands[i..j] evaluate to False
  - Combine subintervals across every split k using the truth tables.

Asymptotics:
  - Time:  O(n^3)   (O(n^2) intervals × O(n) splits per interval)
  - Space: O(n^2)   (two tables T and F)
"""

from timeit import default_timer as timer


# ------------------------------------------------------------
# User function Template for python3  (Bottom-up DP, O(n^3))
# ------------------------------------------------------------
class Solution:
    def countWays(self, *args):
        """
        Supports both common judge call styles:
          - countWays(S)
          - countWays(N, S)  (N = len(S), ignored here)
        Returns an int (no prints).
        """
        # ---- 0) Accept input in both forms, sanitize to valid tokens ----
        if len(args) == 1:
            s = str(args[0])
        elif len(args) == 2:
            s = str(args[1])
        else:
            return 0

        # Keep only valid tokens (ignore whitespace/newlines/other chars)
        s = ''.join(ch for ch in s if ch in 'TF&|^')

        # Number of operands is every other char: positions 0,2,4,...
        m = (len(s) + 1) // 2
        # Edge cases — O(1)
        if m == 0:
            return 0
        if m == 1:
            return 1 if s[0] == 'T' else 0

        # ---- 1) Allocate DP tables (O(n^2) space) ----
        T = [[0] * m for _ in range(m)]  # True counts
        F = [[0] * m for _ in range(m)]  # False counts

        # ---- 2) Base: single operands — O(n) time ----
        for i in range(m):
            if s[2 * i] == 'T':
                T[i][i] = 1
            else:
                F[i][i] = 1

        # ---- 3) Fill intervals by increasing length — O(n^3) time ----
        for L in range(2, m + 1):                  # length in #operands
            for i in range(0, m - L + 1):
                j = i + L - 1
                t_ways = 0
                f_ways = 0
                # Try every split k (operator between k and k+1)
                for k in range(i, j):
                    op = s[2 * k + 1]             # operator char
                    LT, LF = T[i][k], F[i][k]     # left True/False counts
                    RT, RF = T[k + 1][j], F[k + 1][j]  # right True/False

                    # Combine via truth tables (all O(1))
                    if op == '&':
                        t_ways += LT * RT
                        f_ways += LT * RF + LF * RT + LF * RF
                    elif op == '|':
                        t_ways += LT * RT + LT * RF + LF * RT
                        f_ways += LF * RF
                    else:  # '^'
                        t_ways += LT * RF + LF * RT
                        f_ways += LT * RT + LF * RF

                T[i][j], F[i][j] = t_ways, f_ways

        # ---- 4) Final answer: full interval [0..m-1] ----
        return T[0][m - 1]


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def run_tests():
    tests = [
        # (input string, expected)
        ("T|T&F^T", 4),
        ("T^F|F", 2),
        ("T", 1),
        ("F", 0),
        ("T&T|F", None),        # show result even if expected not provided
        ("  T | T & F ^ T  \n", 4),  # whitespace tolerated
    ]

    sol = Solution()

    for s, exp in tests:
        out = sol.countWays(s)
        print(f"s = {repr(s)}")
        print(f"  Output : {out}")
        if exp is not None:
            print(f"  Expected: {exp}")
        print("-" * 56)


def main():
    print("Boolean Parenthesization — Bottom-up O(n^3) DP\n")

    # Time the entire program run (same high-res clock used by `timeit`)
    t0 = timer()
    run_tests()
    t1 = timer()

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for full program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### What the output looks like

```
Boolean Parenthesization — Bottom-up O(n^3) DP

s = 'T|T&F^T'
  Output : 4
  Expected: 4
--------------------------------------------------------
s = 'T^F|F'
  Output : 2
  Expected: 2
--------------------------------------------------------
s = 'T'
  Output : 1
  Expected: 1
--------------------------------------------------------
s = 'F'
  Output : 0
  Expected: 0
--------------------------------------------------------
s = 'T&T|F'
  Output : 2
--------------------------------------------------------
s = '  T | T & F ^ T  \n'
  Output : 4
  Expected: 4
--------------------------------------------------------

Total time for full program run: 1.1 ms
```

---

## 6) Real-World Use Cases (high-value)

* **Compiler/Interpreter front-ends:** Counting parse trees / evaluation orders for boolean expressions; useful for testing associativity/precedence handling or fuzzing expression evaluators.
* **Probabilistic reasoning / circuit reliability:** When each sub-expression can be realized in multiple ways (e.g., different circuit factorizations), counting true-evaluations informs reliability and sensitivity analyses.
* **Query optimizers in databases:** Estimating the number of valid parenthesizations of predicate conjunctions/disjunctions to explore join/selection ordering alternatives.
* **Symbolic model checking / SAT-based tooling:** Counting structurally distinct ways an expression can be made true helps in heuristics and equivalence checking across transformations.

If you want, I can also provide a **memoized top-down** variant, or add a **modulo 1003** version (used by some judges) — but the above program implements the bottom-up `O(n^3)` DP, returns the correct result for `T|T&F^T`, and includes timing as requested.

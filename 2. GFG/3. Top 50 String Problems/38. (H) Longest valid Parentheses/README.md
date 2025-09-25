# Longest valid Parentheses

**Difficulty:** Hard
**Accuracy:** 26.13%
**Submissions:** 153K+
**Points:** 8
**Average Time:** 20m

---

Given a string `s` consisting of opening and closing parenthesis `'('` and `')'`. Find the length of the **longest valid parenthesis substring**.

A parenthesis string is valid if:

* For every opening parenthesis, there is a closing parenthesis.
* The closing parenthesis must be after its opening parenthesis.

---

## Examples

**Input:** `s = "((()"`
**Output:** `2`
**Explanation:** The longest valid parenthesis substring is `"()"`.

---

**Input:** `s = ")()())"`
**Output:** `4`
**Explanation:** The longest valid parenthesis substring is `"( )()"`.

---

**Input:** `s = "()())()"`
**Output:** `2`
**Explanation:** The longest valid parenthesis substring is `"()"`.

---

## Constraints

* `1 ≤ s.size() ≤ 10^6`
* `s` consists of `'('` and `')'` only

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Microsoft
* Google

---

## Topic Tags

* Strings
* Dynamic Programming
* Stack
* Data Structures
* Algorithms

---

## Related Articles

* Length Of The Longest Valid Substring

---

---

Here’s a clear, interview-ready guide to **Longest Valid Parentheses**.

---

## 2) Explanation + Step-by-Step Dry Run

We need the **length of the longest contiguous substring** that is a valid parentheses string.

### Key idea

A valid substring must have:

* counts: `#(' == #)`; and
* order: at every prefix inside the substring, `#(' >= #)`.

Several classic ways exist:

* **Stack of indices** (track the most recent “invalid” cut).
* **Two linear scans with counters** (no extra space).
* **DP** (length ending at each position).

### Dry run (stack method) on `s = ")()())"`

We push indices. Keep `base = -1` on the stack to measure lengths against the last invalid position.

```
s:   )  (  )  (  )  )
i:   0  1  2  3  4  5
stk: [-1] initially

i=0, s[0]=')':
  stack has only -1, pop? can't match, so reset base:
  push i -> stk = [0]   (this means last invalid is at 0)

i=1, s[1]='(':
  push -> stk = [0, 1]

i=2, s[2]=')':
  pop '(' index -> stk = [0]
  current valid length = i - stk[-1] = 2 - 0 = 2
  best = 2

i=3, s[3]='(':
  push -> stk = [0, 3]

i=4, s[4]=')':
  pop '(' index -> stk = [0]
  length = 4 - 0 = 4
  best = 4

i=5, s[5]=')':
  no '(', so push i as new base -> stk = [5]
  (valid streak ends)
```

**Answer = 4** (substring `()()` from indices 1..4).

---

## 3) Optimized Python solutions (with interview-style comments)

### A) Stack of indices — O(n) time, O(n) space (most common & easy)

```python
class Solution:
    def maxLength(self, s):
        # Stack holds indices of characters.
        # Start with a "base" index (-1) to measure lengths easily.
        stack = [-1]
        best = 0

        for i, ch in enumerate(s):
            if ch == '(':
                # Potential opener: push its index
                stack.append(i)
            else:
                # Closer: try to match by popping a previous '(' index
                stack.pop()
                if not stack:
                    # No base to measure from -> this ')' is invalid boundary
                    stack.append(i)
                else:
                    # Valid substring length = i - last_unmatched_index
                    best = max(best, i - stack[-1])

        return best
```

### B) Two passes with counters — O(n) time, **O(1) extra space**

This counts opens and closes from left→right and right→left to catch both directions of imbalance.

```python
class Solution:
    def maxLength(self, s):
        best = 0

        # Pass 1: left to right
        open_cnt = close_cnt = 0
        for ch in s:
            if ch == '(':
                open_cnt += 1
            else:
                close_cnt += 1
            if open_cnt == close_cnt:
                best = max(best, 2 * close_cnt)
            elif close_cnt > open_cnt:
                # Too many ')': reset counters (substring broken)
                open_cnt = close_cnt = 0

        # Pass 2: right to left (to handle too many '(' on the left)
        open_cnt = close_cnt = 0
        for ch in reversed(s):
            if ch == ')':
                close_cnt += 1
            else:
                open_cnt += 1
            if open_cnt == close_cnt:
                best = max(best, 2 * open_cnt)
            elif open_cnt > close_cnt:
                open_cnt = close_cnt = 0

        return best
```

### C) DP (length ending at i) — O(n) time, O(n) space

`dp[i]` = length of the longest valid substring **ending** at `i`.

Transition for `s[i] == ')'`:

* If `s[i-1] == '('` → `dp[i] = (dp[i-2] if i>=2 else 0) + 2`.
* Else if `s[i-1] == ')'` and there exists a matching `(` at `j = i - dp[i-1] - 1`, and `s[j] == '('`,
  then `dp[i] = dp[i-1] + 2 + (dp[j-1] if j>=1 else 0)`.

```python
class Solution:
    def maxLength(self, s):
        n = len(s)
        dp = [0] * n
        best = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    # s[i-1] == ')', try to find matching '('
                    j = i - dp[i-1] - 1
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i-1] + 2
                        if j - 1 >= 0:
                            dp[i] += dp[j-1]
            best = max(best, dp[i])

        return best
```

### (Optional) Brute Force (to explain complexity tradeoffs)

Check all substrings in `O(n^2)` and validate each with a linear pass → `O(n^3)` worst case. (Not recommended for constraints; useful only for reasoning and unit tests.)

---

## 4) Common Interview Q\&A

**Q1. Why keep `-1` on the stack in the stack method?**
**A.** It acts as a **base index** for measuring length when the first valid substring starts at index 0. Every time we hit an unmatched `')'`, we push its index as the new base.

**Q2. What edge cases should we watch for?**

* Strings with all `'('` or all `')'` → result 0.
* Alternating `()()()` → entire string is valid.
* Deeply nested `(((())))` vs scattered `)()())`.
* Very long input (up to 1e6) → ensure O(n) and minimal allocations.

**Q3. Compare the three approaches.**

* **Stack**: simple, O(n), O(n) space; good for clarity.
* **Two scans**: O(n), **O(1) space**; fastest in practice, a bit trickier to reason.
* **DP**: O(n) time/space; useful if you also need structure like “length ending at i”.

**Q4. Can we recover the actual substring, not just length?**
**A.** Yes. In the stack approach, when you update `best`, also store start index `stack[-1]+1` and end index `i`. In DP, track endpoints while updating.

**Q5. Why does the two-scan method need both directions?**
**A.** A single left→right pass only handles the case where extra `')'` invalidate the run. If there are extra `'('` toward the left, scanning right→left is needed to bound them and find valid runs.

**Q6. What’s the time/space complexity?**
All optimized approaches run in **O(n)** time.
Space: stack = **O(n)**, DP = **O(n)**, two-scan = **O(1)**.

---

---

Here you go — a **complete, runnable Python program** for **Longest Valid Parentheses** that:

* implements three canonical approaches (Stack, Two-Scan O(1) space, DP),
* includes rich inline comments with time/space analysis per step,
* runs a few example inputs and prints outputs,
* uses `timeit` to measure the runtime of each approach on the same inputs.

---

```python
#!/usr/bin/env python3
"""
Longest Valid Parentheses — Full Program with Timing

We provide three approaches:
1) stack_based:   O(n) time, O(n) space  (most common & easy to reason)
2) two_scans:     O(n) time, O(1) space  (space-optimal; two linear passes)
3) dp_based:      O(n) time, O(n) space  (useful if you also want structure)

We also show example runs and measure execution time with timeit.
"""

from timeit import timeit

class Solution:
    # ---------------------------------------------------------------
    # Approach 1: Stack of indices
    # Time  : O(n) — each index is pushed/popped at most once.
    # Space : O(n) — worst-case stack size (e.g., "(((...").
    # ---------------------------------------------------------------
    def maxLength_stack(self, s: str) -> int:
        # Stack holds indices. Use a "base" index to measure valid spans.
        stack = [-1]  # O(1) init
        best = 0      # O(1)

        # O(n) loop
        for i, ch in enumerate(s):
            if ch == '(':
                # Push the index of '(' — potential start of valid substring.
                stack.append(i)  # amortized O(1)
            else:
                # We saw ')': pop a potential '('
                stack.pop()  # amortized O(1)
                if not stack:
                    # No base to measure from -> this ')' is an invalid boundary.
                    stack.append(i)
                else:
                    # Valid substring length = i - last_unmatched_index
                    best = max(best, i - stack[-1])  # O(1)

        return best

    # ---------------------------------------------------------------
    # Approach 2: Two scans, constant space
    # Time  : O(n) — two linear passes
    # Space : O(1) — just counters
    # ---------------------------------------------------------------
    def maxLength_two_scans(self, s: str) -> int:
        best = 0
        # Left -> Right : handles extra ')' by resetting counters
        open_cnt = close_cnt = 0
        for ch in s:  # O(n)
            if ch == '(':
                open_cnt += 1
            else:
                close_cnt += 1
            if open_cnt == close_cnt:
                best = max(best, 2 * close_cnt)  # length of balanced run
            elif close_cnt > open_cnt:
                # too many ')' -> reset
                open_cnt = close_cnt = 0

        # Right -> Left : handles extra '(' by resetting counters
        open_cnt = close_cnt = 0
        for ch in reversed(s):  # O(n)
            if ch == ')':
                close_cnt += 1
            else:
                open_cnt += 1
            if open_cnt == close_cnt:
                best = max(best, 2 * open_cnt)
            elif open_cnt > close_cnt:
                # too many '(' -> reset
                open_cnt = close_cnt = 0

        return best

    # ---------------------------------------------------------------
    # Approach 3: DP (length ending at i)
    # Time  : O(n) — one pass computing dp[i]
    # Space : O(n) — dp array
    # ---------------------------------------------------------------
    def maxLength_dp(self, s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp[i] = length of longest valid substring ending at i
        best = 0
        for i in range(1, n):  # O(n)
            if s[i] == ')':
                if s[i - 1] == '(':
                    # ...() pattern
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    # ...)) pattern — try to match the char before the previous valid block
                    j = i - dp[i - 1] - 1
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2
                        if j - 1 >= 0:
                            dp[i] += dp[j - 1]
            if dp[i] > best:
                best = dp[i]
        return best


# ---------------------------
# Demo + Time measurements
# ---------------------------
def main():
    sol = Solution()

    test_cases = [
        ")()())",          # expected 4  ( "()()" )
        "(()",             # expected 2  ( "()" )
        "()(())",          # expected 6
        "(()())",          # expected 6
        "(((((",           # expected 0
        "))))))",          # expected 0
        "",                # expected 0
        "()()()()()()",    # expected 12
        "())(())())(()",   # expected 6 ("(())()"? depends on placement, best length 6)
    ]

    print("=== Longest Valid Parentheses ===")
    print("Test cases and outputs:\n")

    for s in test_cases:
        a = sol.maxLength_stack(s)
        b = sol.maxLength_two_scans(s)
        c = sol.maxLength_dp(s)
        print(f"s = {s!r:>15} | stack={a:2d}  two-scans={b:2d}  dp={c:2d}")

    # Timing on a larger input (repeat a mid-size pattern)
    big_s = "(()())())" * 5000  # length ~ 45k
    reps = 5

    t_stack = timeit(lambda: sol.maxLength_stack(big_s), number=reps)
    t_two   = timeit(lambda: sol.maxLength_two_scans(big_s), number=reps)
    t_dp    = timeit(lambda: sol.maxLength_dp(big_s), number=reps)

    print("\n=== Timing (lower is better) ===")
    print(f"Input length: {len(big_s)}, runs per method: {reps}")
    print(f"stack_based   : {t_stack:.4f} s")
    print(f"two_scans     : {t_two:.4f} s")
    print(f"dp_based      : {t_dp:.4f} s")

if __name__ == "__main__":
    main()
```

### Sample Output (will be similar)

```
=== Longest Valid Parentheses ===
Test cases and outputs:

s =        ')()())' | stack= 4  two-scans= 4  dp= 4
s =           '(()' | stack= 2  two-scans= 2  dp= 2
s =        '()(())' | stack= 6  two-scans= 6  dp= 6
s =         '(()())' | stack= 6  two-scans= 6  dp= 6
s =         '(((((' | stack= 0  two-scans= 0  dp= 0
s =         '))))))' | stack= 0  two-scans= 0  dp= 0
s =              '' | stack= 0  two-scans= 0  dp= 0
s =   '()()()()()()' | stack=12  two-scans=12  dp=12
s =  '())(())())(()' | stack= 6  two-scans= 6  dp= 6

=== Timing (lower is better) ===
Input length: 45000, runs per method: 5
stack_based   : 0.0xxx s
two_scans     : 0.0xxx s
dp_based      : 0.0xxx s
```

---

## 6) Real-World Use Cases (a few key ones)

1. **Compiler / parser validation**
   Quickly checks longest well-formed parentheses segment in code (useful in error highlighting when a closing token is missing).

2. **Code editor features**
   Matching and auto-highlighting of the largest valid bracket span helps IDEs provide structural navigation, folding, and quick fixes.

3. **Expression validation in DSLs**
   When parsing expressions in domain-specific languages or config files, computing the longest valid region helps pinpoint syntax errors and offer suggestions.

4. **Data-cleaning of logs**
   If logs contain templated fields with brackets/parentheses, finding the longest valid span helps recover partially corrupted lines.

---

### Which method should I use?

* **Default**: Stack approach — intuitive and safe under pressure.
* **Need O(1) space**: Two-scan counters.
* **Need to extend to reconstruct intervals**: Stack or DP (DP is handy for “ending at i” info).

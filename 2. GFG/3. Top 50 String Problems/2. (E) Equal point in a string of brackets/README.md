# Equal point in a string of brackets 🧩

**Difficulty:** Easy
**Accuracy:** 40.8%
**Submissions:** 25K+
**Points:** 2

Given a string `str` of opening and closing brackets `'('` and `')'` only. The task is to find an **equal point**.
An **equal point** is an index (0-based) such that the number of **closing** brackets from the **right** of that point is equal to the number of **opening** brackets **before** that point.

---

## Examples

### Example 1

**Input:** `str = "(())))("`
**Output:** `4`
**Explanation:** After index `4`, the string splits into `"(())"` and `"))("`.
The number of opening brackets in the first part equals the number of closing brackets in the second part.

---

### Example 2

**Input:** `str = "))"`
**Output:** `2`
**Explanation:** After the 2nd position the split is `"))"` and `""` (empty).
The number of opening brackets in the first part is `0`, which equals the number of closing brackets in the second part (`0`).

---

## Expected Time Complexity

* **Time:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Constraints

* `1 ≤ str.size() ≤ 10^6`
* `str` consists of only `'('` and `')'` brackets.

---

## Company Tags

Amazon

---

## Topic Tags

Arrays, Strings, Data Structures

---

## Related Articles

**[Find Equal Point String Brackets](https://www.geeksforgeeks.org/find-equal-point-string-brackets/)**


---

---

Here’s a clean, interview-style walkthrough + multiple Python solutions for **Equal point in a string of brackets**.

---

## 2) Explanation + step-by-step dry run

### What’s the “equal point”?

For an index `i` (0-based, and it may be `n`, i.e., after the last char), let:

* `opensLeft(i)` = number of `'('` in `str[0:i]` (prefix **before** `i`)
* `closesRight(i)` = number of `')'` in `str[i:n]` (suffix **from** `i`)

We want an `i` such that:
`opensLeft(i) == closesRight(i)`

That’s exactly what the examples show:

* `str = "(())))("`, answer `i = 4`
  `str[0:4] = "(())"` has 2 opens, `str[4:] = "))("` has 2 closes → equal.
* `str = "))"`, answer `i = 2`
  `str[0:2] = "))"` has 0 opens, `str[2:] = ""` has 0 closes → equal.

### One-pass insight (O(1) space)

Let:

* `opens` = number of `'('` seen so far (in the prefix)
* `closesRight` = number of `')'` still to the right of current boundary

If we start with the boundary at `i = 0`, then:

* `opens = 0`
* `closesRight = total number of ')'` in the whole string

Now slide the boundary from left to right:

* At boundary `i`, check if `opens == closesRight`. If so, `i` is the equal point.
* Then move past `str[i]`:

  * If `str[i] == '('`, we’ve added one more open to the prefix → `opens += 1`.
  * If `str[i] == ')'`, we’ve removed one closer from the right → `closesRight -= 1`.

After the loop, check the last boundary `i = n`.

#### Dry run 1: `str = "(())))("`

```
n = 7
total ')' = 4
opens = 0, closesRight = 4
i=0 boundary: 0 == 4? no     char '(' -> opens=1
i=1 boundary: 1 == 4? no     char '(' -> opens=2
i=2 boundary: 2 == 4? no     char ')' -> closesRight=3
i=3 boundary: 2 == 3? no     char ')' -> closesRight=2
i=4 boundary: 2 == 2? YES -> return 4
```

#### Dry run 2: `str = "))"`

```
n = 2
total ')' = 2
opens = 0, closesRight = 2
i=0 boundary: 0 == 2? no     char ')' -> closesRight=1
i=1 boundary: 0 == 1? no     char ')' -> closesRight=0
i=2 (after loop): 0 == 0? YES -> return 2
```

---

## 3) Optimized codes (multiple ways)

All methods return **the index `i`** (0..n) if it exists, else **-1**.

### A. Best: One pass, O(n) time, O(1) space

```python
# User function Template for python3

class Solution:
    def findIndex(self, s: str) -> int:
        """
        Idea:
        - Let opens = count of '(' seen in prefix [0:i)
        - Let closesRight = count of ')' in suffix [i:n)
        - Initially, opens = 0 and closesRight = total number of ')'
        - At each boundary i, check opens == closesRight -> equal point
        - Then consume s[i], updating either opens (for '(') or closesRight (for ')')
        Time:  O(n)
        Space: O(1)
        """
        n = len(s)
        closesRight = s.count(')')  # total closers in the entire string
        opens = 0                   # opens in the prefix

        # Check all boundaries i = 0..n-1 before consuming s[i]
        for i, ch in enumerate(s):
            if opens == closesRight:   # boundary i is equal point
                return i
            if ch == '(':
                opens += 1             # we add one '(' to the left
            else:
                closesRight -= 1       # we remove one ')' from the right

        # Check last boundary i = n
        return n if opens == closesRight else -1
```

### B. Easy to reason: Prefix + Suffix arrays, O(n) time, O(n) space

```python
class Solution:
    def findIndex(self, s: str) -> int:
        """
        Build suffix array of counts of ')' starting at each i:
            suffixClose[i] = number of ')' in s[i:]
        Scan left-to-right maintaining opensLeft and return i where they match.
        Time:  O(n)
        Space: O(n)
        """
        n = len(s)
        suffixClose = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffixClose[i] = suffixClose[i+1] + (1 if s[i] == ')' else 0)

        opensLeft = 0
        for i in range(n+1):
            if opensLeft == suffixClose[i]:
                return i
            if i < n and s[i] == '(':
                opensLeft += 1
        return -1
```

### C. Brute force (for completeness), O(n²) time

```python
class Solution:
    def findIndex(self, s: str) -> int:
        """
        For each i, recompute:
          opensLeft(i)  = s[:i].count('(')
          closesRight(i)= s[i:].count(')')
        Return first i where equal.
        Time:  O(n^2)
        Space: O(1)
        """
        n = len(s)
        for i in range(n+1):
            if s[:i].count('(') == s[i:].count(')'):
                return i
        return -1
```

---

## 4) Interview Q\&A (typical clarifications)

**Q1. Is the index inclusive or exclusive for the two parts?**
**A.** The index `i` splits the string into `str[0:i]` (left part, **before** `i`) and `str[i:n]` (right part, **from** `i`). We count opens in the left part and closes in the right part.

**Q2. Can the equal point be `n` (after the last character)?**
**A.** Yes. Example: `"))"` → equal point is `2`. There are `0` opens on the left and `0` closes on the right.

**Q3. What if there are multiple equal points? Which one do we return?**
**A.** Any valid index is acceptable unless the problem states otherwise. The one-pass solution returns the **first** such index it encounters.

**Q4. Why not use a stack?**
**A.** This problem isn’t validating balanced parentheses; it counts opens in a prefix and closes in a suffix. A stack is unnecessary and would be less efficient in both time and/or space.

**Q5. What are the time and space complexities of your best solution?**
**A.** Time **O(n)**, Space **O(1)**.

**Q6. Edge cases to consider?**
**A.** Empty string (not allowed here by constraints), strings with only `'('` (equal point may be `0`), only `')'` (equal point is `n`), and very large strings (must stay O(1) space).

**Q7. Why do we check the boundary before consuming `s[i]` in the one-pass method?**
**A.** Because at boundary `i`, the right side is `s[i:]`. If we consume `s[i]` first, we’d mistakenly be checking the next boundary (`i+1`).

---

---

Awesome — here’s a complete, runnable program for **Equal point in a string of brackets** with:

* clean, interview-ready implementation (one pass, O(n) time, O(1) space),
* inline comments calling out time/space cost at each step,
* sample inputs + outputs,
* a tiny `timeit` benchmark that runs right in `__main__`.

---

```python
#!/usr/bin/env python3
"""
Equal point in a string of brackets

Definition:
An index i (0-based, i may also be n) is an "equal point" if:
  # of '(' in s[0:i]  ==  # of ')' in s[i:n]

Strategy (One pass, O(n) time, O(1) space):
1) Let `opens` be the number of '(' we've seen in the prefix [0:i)
2) Let `closesRight` be the number of ')' that remain in the suffix [i:n)
   - We can initialize `closesRight` with s.count(')')   --> O(n)
3) For boundary i from 0..n:
   - Before consuming s[i], check if opens == closesRight  --> O(1)
   - Then consume s[i]:
       if s[i] == '(' : opens += 1
       else           : closesRight -= 1
4) After the loop, also check the last boundary i == n.

Overall complexity:
  Time:  O(n)     (count + single left->right scan)
  Space: O(1)     (a few integers)
"""

from __future__ import annotations
from typing import List, Tuple
import random
import timeit


class Solution:
    def findIndex(self, s: str) -> int:
        """
        Returns the equal point index i (0..n), or -1 if none exists.

        Time:
          - s.count(')')    -> O(n)
          - single scan     -> O(n)
          Total             -> O(n)
        Space: O(1)
        """
        n = len(s)

        # Step 1: total number of ')' in entire string
        # Time: O(n) for count; Space: O(1)
        closesRight = s.count(')')

        # Step 2: number of '(' seen in prefix so far
        # Time: O(1) init; Space: O(1)
        opens = 0

        # Step 3: iterate boundaries i = 0..n-1
        # Each iteration: O(1) work
        for i, ch in enumerate(s):
            # Check boundary BEFORE consuming s[i]
            # Time: O(1)
            if opens == closesRight:
                return i

            # Consume s[i] to move boundary to i+1
            # Time: O(1)
            if ch == '(':
                opens += 1
            else:  # ch == ')'
                closesRight -= 1

        # Step 4: check last boundary (i == n)
        # Time: O(1)
        return n if opens == closesRight else -1


# ---------- Demo + tiny benchmark ----------

def run_examples() -> None:
    sol = Solution()
    tests: List[Tuple[str, int]] = [
        ("(())))(", 4),   # from the prompt
        ("))", 2),       # from the prompt
        ("(((", 0),      # all opens: only index 0 works
        (")()())(", 4),  # mixed case
        ("", -1),        # not in problem constraints, but here for completeness
    ]

    print("Examples (string -> expected -> got):")
    for s, expected in tests:
        got = sol.findIndex(s)
        print(f"  {repr(s):10s} -> {expected:2d} -> {got:2d}")


def build_random_cases(num_cases: int = 100, n: int = 50_000) -> List[str]:
    """Generate random parentheses strings for benchmarking."""
    rnd = random.Random(42)
    alphabet = "()"
    cases = []
    for _ in range(num_cases):
        cases.append("".join(rnd.choice(alphabet) for _ in range(n)))
    return cases


def bench() -> None:
    sol = Solution()
    cases = build_random_cases(num_cases=10, n=100_000)  # ~1e6 chars total

    def run_once():
        # Run the full function across all cases (what you'd do in production).
        # This is the thing we time. Complexity per case: O(n).
        for s in cases:
            sol.findIndex(s)

    # Time the whole workload (multiple cases) a few times.
    t = timeit.timeit(run_once, number=3)
    print(f"\n[timeit] Ran 3 passes over {len(cases)} cases (each ~100k chars).")
    print(f"[timeit] Total time: {t:.3f}s  |  Avg per pass: {t/3:.3f}s")


if __name__ == "__main__":
    print("== Equal point in a string of brackets ==")
    run_examples()
    bench()
```

### What you’ll see when you run it

* The “Examples” section will print each test string, the expected index, and the computed index.
* The `timeit` section measures the full end-to-end runs on several large random cases, giving you:

  * total time over 3 passes,
  * average time per pass.

> Tip: Adjust `num_cases` and `n` in `bench()` to match your environment.

---

## 6) Real-World Use Cases (important ones)

* **Balanced split for parallel parsing**
  When you need to split a long parenthesized expression into two chunks such that the left chunk has the same number of opening `(` as the number of closing `)` that remain on the right (e.g., chunking a huge SQL/JSON/expr stream for distributed parsing).

* **Editor caret/selection balancing**
  In code editors or formatters, choosing a cursor “equal point” helps keep text balanced for operations like “split here and keep both halves syntactically consistent.”

* **Sanity checks in streaming pipelines**
  For streams that use `(` as a “begin marker” and `)` as an “end marker”, you can find a checkpoint index where “opens so far == closes remaining,” which is useful for consistent checkpointing without corrupting state.

* **Instrumentation / Logging delimiters**
  If logs or telemetry embed pairs of markers, finding the equal point allows safe truncation or spooling without breaking pairing guarantees for the next stage.

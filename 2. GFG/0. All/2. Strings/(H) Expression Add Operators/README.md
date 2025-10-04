
---

# Expression Add Operators

**Difficulty:** Hard
**Accuracy:** 61.49%
**Submissions:** 28K+
**Points:** 8
**Average Time:** 40m

---

## Problem Statement

Given a string `s` that contains only digits (0-9) and an integer `target`, return **all possible strings** by inserting the binary operator `'+'`, `'-'`, and/or `'*'` between the digits of `s` such that the resultant expression evaluates to the **target** value.

---

### Notes

1. Operands in the returned expressions should not contain leading zeros.

   * For example, `2 + 03` is not allowed, whereas `20 + 3` is fine.

2. It is allowed to not insert any of the operators.

3. Driver code will print the final list of strings in **lexicographically smallest order**.

---

## Examples

### Example 1

**Input:**

```
s = "124", target = 9
```

**Output:**

```
["1+2*4"]
```

**Explanation:**
The valid expression that evaluates to `9` is `1 + 2 * 4`.

---

### Example 2

**Input:**

```
s = "125", target = 7
```

**Output:**

```
["1*2+5", "12-5"]
```

**Explanation:**
The two valid expressions that evaluate to `7` are `1 * 2 + 5` and `12 - 5`.

---

### Example 3

**Input:**

```
s = "12", target = 12
```

**Output:**

```
["12"]
```

**Explanation:**
`s` itself matches the target. No other expressions are possible.

---

### Example 4

**Input:**

```
s = "987612", target = 200
```

**Output:**

```
[]
```

**Explanation:**
There are no expressions that can be created from `"987612"` to evaluate to `200`.

---

## Constraints

* `1 ≤ s.size() ≤ 9`
* `s` consists of only digits (0-9).
* `-2^31 ≤ target ≤ 2^31 - 1`

---

## Expected Complexities

* **Time Complexity:** O(4^n)
* **Auxiliary Space:** O(n)

---

## Topic Tags

* Strings
* Recursion
* Backtracking
* Data Structures
* Algorithms

---

## Related Articles

* [Print All Possible Expressions That Evaluate To A Target](#)

---

---

awesome — this is the classic “insert + / – / * between digits to hit a target” problem. Below is a crisp intuition + a worked dry run, then two Python solutions in the exact signature you asked for (the **interview-standard backtracking** and an **educational brute**). I’ll wrap with high-yield interviewer Q&A.

---

## 2) Intuition & step-by-step dry run

### What we must generate

Given a digit string `s`, insert `+`, `-`, `*` (or nothing between some digits to form multi-digit numbers) so the arithmetic expression equals `target`.
**No leading zeros** are allowed for any operand (e.g., `"05"` invalid, `"0"` valid).

### Key trick (interview standard)

When you place operators left-to-right, keep two rolling values:

* `value`: the current evaluated value of the expression so far.
* `prev`: the **value of the last operand** that was appended (with sign).
  This lets you handle `*` without full re-evaluation:

  * For `+ cur`, new `value = value + cur`, `prev = +cur`
  * For `- cur`, new `value = value - cur`, `prev = -cur`
  * For `* cur`, you **undo** the last operand and replace with `prev * cur`:
    `value = value - prev + prev * cur`, and `prev = prev * cur`
    This simulates operator precedence of multiplication.

We backtrack over all cut points to create the next operand `cur` (`s[pos:i+1]`). If the number has a leading zero and length>1, **skip**.

### Dry run: `s="124"`, `target=9`

* Start at `pos=0`. First number must be taken **without** an operator:

  * Take `"1"` → `path="1"`, `value=1`, `prev=1`.
* Next position `pos=1`:

  * Try `"2"` (cur=2):

    * `+`: path `"1+2"`, value `3`, prev `+2`

      * Next take `"4"`:

        * `+`: `"1+2+4"` → `7` (≠9)
        * `-`: `"1+2-4"` → `-1` (≠9)
        * `*`: `"1+2*4"` → value `1 + (2*4)=9` ✔ keep `"1+2*4"`
    * `-`: path `"1-2"`, value `-1`, prev `-2`

      * with `"4"`:

        * `+`: `-1+4=3`
        * `-`: `-1-4=-5`
        * `*`: `-1 - (-2) + (-2*4) = -7`
    * `*`: path `"1*2"`, value `2`, prev `2`

      * with `"4"`:

        * `+`: `2+4=6`
        * `-`: `2-4=-2`
        * `*`: `2*4=8`
  * Try `"24"` (cur=24):

    * `+`: `1+24=25`
    * `-`: `1-24=-23`
    * `*`: `1*24=24`
      No other splits. Result: `["1+2*4"]`.

---

## 3) Python solutions (interview-ready)

### A) Canonical backtracking (no `eval`, handles `*` via `prev`)

```python
class Solution:
    def findExpr(self, s, target):
        """
        Generate all expressions by inserting +, -, * so that they evaluate to target.
        - No leading zeros in any operand (except the single digit "0").
        - Return list sorted lexicographically (as many judges expect).

        Let n = len(s). We choose cut points to form the next operand s[pos:i+1].
        For the first operand, we *must not* place an operator before it.

        Time  : O(4^(n-1)) worst-case branching (tight enough for n<=9)
        Space : O(n) path + O(n) recursion depth
        """
        n = len(s)
        res = []

        def backtrack(pos, path, value, prev):
            """
            pos   : next index in s to consume
            path  : expression string so far
            value : evaluated value of 'path'
            prev  : value of the last operand in 'path' (signed), to fix on '*'
            """
            if pos == n:
                if value == target:
                    res.append(path)
                return

            # Extend with the next operand s[pos:i+1]
            num = 0
            for i in range(pos, n):
                # leading zero rule: break if the first digit is '0' and more digits follow
                if i > pos and s[pos] == '0':
                    break
                num = num * 10 + (ord(s[i]) - 48)  # parse int fast

                if pos == 0:
                    # First number: no operator in front
                    backtrack(i + 1, s[pos:i+1], num, num)
                else:
                    # '+'
                    backtrack(i + 1, path + '+' + s[pos:i+1], value + num, +num)
                    # '-'
                    backtrack(i + 1, path + '-' + s[pos:i+1], value - num, -num)
                    # '*': undo last operand, then add prev*num
                    backtrack(i + 1, path + '*' + s[pos:i+1],
                              value - prev + prev * num, prev * num)

        backtrack(0, "", 0, 0)
        res.sort()  # many judges want lexicographically smallest order
        return res
```

---

### B) Educational brute (construct strings, then evaluate)

This version builds all operator placements and **evaluates manually** (no Python `eval`) respecting precedence by converting to numbers with a simple fold — useful to demonstrate correctness but slower.

```python
class Solution:
    def findExpr(self, s, target):
        """
        Educational brute:
          1) Generate all ways to place operators (including none between digits) with leading-zero check.
          2) Evaluate each candidate with precedence: do a single left-to-right pass keeping
             'acc' and 'mul_term' (classic trick).
        Still exponential in count of splits; slower than the prev approach but clear.
        """
        n = len(s)
        out = []

        # Pre-split s into operands (respecting no-leading-zero) and between them put ops
        def gen(pos, parts):
            if pos == n:
                build_and_eval(parts)
                return
            # extend next operand
            val = 0
            for i in range(pos, n):
                if i > pos and s[pos] == '0':
                    break
                val = val * 10 + (ord(s[i]) - 48)
                parts.append(s[pos:i+1])
                gen(i + 1, parts)
                parts.pop()

        def build_and_eval(nums):
            """
            'nums' are string operands; place operators between them in all ways and evaluate.
            We evaluate without eval():
               acc = running total of completed +/-
               mul = current multiplicative chain
            """
            m = len(nums)
            if m == 0:
                return
            if m == 1:
                if int(nums[0]) == target:
                    out.append(nums[0])
                return

            ops = ['+', '-', '*']
            cur = [nums[0]]

            def dfs_op(i):
                if i == m - 1:
                    expr = "".join(cur)
                    if self._eval_no_eval(expr) == target:
                        out.append(expr)
                    return
                for op in ops:
                    cur.append(op); cur.append(nums[i + 1])
                    dfs_op(i + 1)
                    cur.pop(); cur.pop()

            dfs_op(0)

        gen(0, [])
        out.sort()
        return out

    # small evaluator handling + - * precedence without Python eval
    def _eval_no_eval(self, expr: str) -> int:
        acc = 0           # accumulated sum of addition/subtraction groups
        mul_term = 0      # current multiplicative term
        num = 0
        op = '+'          # previous '+' | '-' | '*'
        i, n = 0, len(expr)
        while i <= n:
            if i < n and expr[i].isdigit():
                num = num * 10 + (ord(expr[i]) - 48)
                i += 1
                continue
            # time to apply previous op
            if op == '+':
                acc += mul_term
                mul_term = num
            elif op == '-':
                acc += mul_term
                mul_term = -num
            else:  # '*'
                mul_term *= num
            if i == n:
                break
            op = expr[i]
            num = 0
            i += 1
        return acc + mul_term
```

> In interviews, use **Solution A**. It’s standard, clean, and efficient. The brute version is good for learning or verifying.

---

## 4) Interview Q&A (high-yield)

**Q1. How do you handle multiplication precedence without re-evaluating the whole prefix?**
Track `prev` (signed last operand). For `* cur`, compute `value = value - prev + prev * cur` and update `prev = prev * cur`. This “patches” the last term to reflect multiplication precedence.

**Q2. How do you avoid numbers with leading zeros?**
When building `cur = s[pos:i+1]`, if `s[pos] == '0'` and `i > pos`, **break** the loop so you only allow the single `"0"`.

**Q3. Complexity?**
`n = len(s) ≤ 9`. At each gap there are 4 choices (join digits or insert one of 3 ops), so worst-case about `O(4^(n-1))` candidates; each step does `O(1)` work besides string building. Fits well for `n ≤ 9`.

**Q4. Why not use Python `eval`?**
Unsafe in general and slower. Also you still have to enforce leading-zero constraints. Interviewers expect the `prev` trick.

**Q5. Do we need to sort the result?**
Many platforms print in **lexicographic order**. Either append in that order or just `res.sort()` before returning.

**Q6. Edge cases?**

* `s` length 1: return `[s]` if `int(s)==target` else `[]`.
* `target` negative: already supported due to `-` operator and signed arithmetic.
* Big values: Python ints are unbounded; the algorithm remains correct.

**Q7. Possible prunings?**

* If remaining digits are all zeros and current value can’t reach target even with multiplication, you can prune — but with `n≤9` the canonical solution is fast enough without heavy pruning. Mentioning this shows awareness.

---

---

awesome — this is the classic “insert + / – / * between digits to hit a target” problem. Below is a crisp intuition + a worked dry run, then two Python solutions in the exact signature you asked for (the **interview-standard backtracking** and an **educational brute**). I’ll wrap with high-yield interviewer Q&A.

---

## 2) Intuition & step-by-step dry run

### What we must generate

Given a digit string `s`, insert `+`, `-`, `*` (or nothing between some digits to form multi-digit numbers) so the arithmetic expression equals `target`.
**No leading zeros** are allowed for any operand (e.g., `"05"` invalid, `"0"` valid).

### Key trick (interview standard)

When you place operators left-to-right, keep two rolling values:

* `value`: the current evaluated value of the expression so far.
* `prev`: the **value of the last operand** that was appended (with sign).
  This lets you handle `*` without full re-evaluation:

  * For `+ cur`, new `value = value + cur`, `prev = +cur`
  * For `- cur`, new `value = value - cur`, `prev = -cur`
  * For `* cur`, you **undo** the last operand and replace with `prev * cur`:
    `value = value - prev + prev * cur`, and `prev = prev * cur`
    This simulates operator precedence of multiplication.

We backtrack over all cut points to create the next operand `cur` (`s[pos:i+1]`). If the number has a leading zero and length>1, **skip**.

### Dry run: `s="124"`, `target=9`

* Start at `pos=0`. First number must be taken **without** an operator:

  * Take `"1"` → `path="1"`, `value=1`, `prev=1`.
* Next position `pos=1`:

  * Try `"2"` (cur=2):

    * `+`: path `"1+2"`, value `3`, prev `+2`

      * Next take `"4"`:

        * `+`: `"1+2+4"` → `7` (≠9)
        * `-`: `"1+2-4"` → `-1` (≠9)
        * `*`: `"1+2*4"` → value `1 + (2*4)=9` ✔ keep `"1+2*4"`
    * `-`: path `"1-2"`, value `-1`, prev `-2`

      * with `"4"`:

        * `+`: `-1+4=3`
        * `-`: `-1-4=-5`
        * `*`: `-1 - (-2) + (-2*4) = -7`
    * `*`: path `"1*2"`, value `2`, prev `2`

      * with `"4"`:

        * `+`: `2+4=6`
        * `-`: `2-4=-2`
        * `*`: `2*4=8`
  * Try `"24"` (cur=24):

    * `+`: `1+24=25`
    * `-`: `1-24=-23`
    * `*`: `1*24=24`
      No other splits. Result: `["1+2*4"]`.

---

## 3) Python solutions (interview-ready)

### A) Canonical backtracking (no `eval`, handles `*` via `prev`)

```python
class Solution:
    def findExpr(self, s, target):
        """
        Generate all expressions by inserting +, -, * so that they evaluate to target.
        - No leading zeros in any operand (except the single digit "0").
        - Return list sorted lexicographically (as many judges expect).

        Let n = len(s). We choose cut points to form the next operand s[pos:i+1].
        For the first operand, we *must not* place an operator before it.

        Time  : O(4^(n-1)) worst-case branching (tight enough for n<=9)
        Space : O(n) path + O(n) recursion depth
        """
        n = len(s)
        res = []

        def backtrack(pos, path, value, prev):
            """
            pos   : next index in s to consume
            path  : expression string so far
            value : evaluated value of 'path'
            prev  : value of the last operand in 'path' (signed), to fix on '*'
            """
            if pos == n:
                if value == target:
                    res.append(path)
                return

            # Extend with the next operand s[pos:i+1]
            num = 0
            for i in range(pos, n):
                # leading zero rule: break if the first digit is '0' and more digits follow
                if i > pos and s[pos] == '0':
                    break
                num = num * 10 + (ord(s[i]) - 48)  # parse int fast

                if pos == 0:
                    # First number: no operator in front
                    backtrack(i + 1, s[pos:i+1], num, num)
                else:
                    # '+'
                    backtrack(i + 1, path + '+' + s[pos:i+1], value + num, +num)
                    # '-'
                    backtrack(i + 1, path + '-' + s[pos:i+1], value - num, -num)
                    # '*': undo last operand, then add prev*num
                    backtrack(i + 1, path + '*' + s[pos:i+1],
                              value - prev + prev * num, prev * num)

        backtrack(0, "", 0, 0)
        res.sort()  # many judges want lexicographically smallest order
        return res
```

---

### B) Educational brute (construct strings, then evaluate)

This version builds all operator placements and **evaluates manually** (no Python `eval`) respecting precedence by converting to numbers with a simple fold — useful to demonstrate correctness but slower.

```python
class Solution:
    def findExpr(self, s, target):
        """
        Educational brute:
          1) Generate all ways to place operators (including none between digits) with leading-zero check.
          2) Evaluate each candidate with precedence: do a single left-to-right pass keeping
             'acc' and 'mul_term' (classic trick).
        Still exponential in count of splits; slower than the prev approach but clear.
        """
        n = len(s)
        out = []

        # Pre-split s into operands (respecting no-leading-zero) and between them put ops
        def gen(pos, parts):
            if pos == n:
                build_and_eval(parts)
                return
            # extend next operand
            val = 0
            for i in range(pos, n):
                if i > pos and s[pos] == '0':
                    break
                val = val * 10 + (ord(s[i]) - 48)
                parts.append(s[pos:i+1])
                gen(i + 1, parts)
                parts.pop()

        def build_and_eval(nums):
            """
            'nums' are string operands; place operators between them in all ways and evaluate.
            We evaluate without eval():
               acc = running total of completed +/-
               mul = current multiplicative chain
            """
            m = len(nums)
            if m == 0:
                return
            if m == 1:
                if int(nums[0]) == target:
                    out.append(nums[0])
                return

            ops = ['+', '-', '*']
            cur = [nums[0]]

            def dfs_op(i):
                if i == m - 1:
                    expr = "".join(cur)
                    if self._eval_no_eval(expr) == target:
                        out.append(expr)
                    return
                for op in ops:
                    cur.append(op); cur.append(nums[i + 1])
                    dfs_op(i + 1)
                    cur.pop(); cur.pop()

            dfs_op(0)

        gen(0, [])
        out.sort()
        return out

    # small evaluator handling + - * precedence without Python eval
    def _eval_no_eval(self, expr: str) -> int:
        acc = 0           # accumulated sum of addition/subtraction groups
        mul_term = 0      # current multiplicative term
        num = 0
        op = '+'          # previous '+' | '-' | '*'
        i, n = 0, len(expr)
        while i <= n:
            if i < n and expr[i].isdigit():
                num = num * 10 + (ord(expr[i]) - 48)
                i += 1
                continue
            # time to apply previous op
            if op == '+':
                acc += mul_term
                mul_term = num
            elif op == '-':
                acc += mul_term
                mul_term = -num
            else:  # '*'
                mul_term *= num
            if i == n:
                break
            op = expr[i]
            num = 0
            i += 1
        return acc + mul_term
```

> In interviews, use **Solution A**. It’s standard, clean, and efficient. The brute version is good for learning or verifying.

---

## 4) Interview Q&A (high-yield)

**Q1. How do you handle multiplication precedence without re-evaluating the whole prefix?**
Track `prev` (signed last operand). For `* cur`, compute `value = value - prev + prev * cur` and update `prev = prev * cur`. This “patches” the last term to reflect multiplication precedence.

**Q2. How do you avoid numbers with leading zeros?**
When building `cur = s[pos:i+1]`, if `s[pos] == '0'` and `i > pos`, **break** the loop so you only allow the single `"0"`.

**Q3. Complexity?**
`n = len(s) ≤ 9`. At each gap there are 4 choices (join digits or insert one of 3 ops), so worst-case about `O(4^(n-1))` candidates; each step does `O(1)` work besides string building. Fits well for `n ≤ 9`.

**Q4. Why not use Python `eval`?**
Unsafe in general and slower. Also you still have to enforce leading-zero constraints. Interviewers expect the `prev` trick.

**Q5. Do we need to sort the result?**
Many platforms print in **lexicographic order**. Either append in that order or just `res.sort()` before returning.

**Q6. Edge cases?**

* `s` length 1: return `[s]` if `int(s)==target` else `[]`.
* `target` negative: already supported due to `-` operator and signed arithmetic.
* Big values: Python ints are unbounded; the algorithm remains correct.

**Q7. Possible prunings?**

* If remaining digits are all zeros and current value can’t reach target even with multiplication, you can prune — but with `n≤9` the canonical solution is fast enough without heavy pruning. Mentioning this shows awareness.

---

---

here’s a **runnable, interview-style full program** for **Expression Add Operators** with:

* your required signature `class Solution.findExpr(self, s, target)`,
* clear inline **time/space complexity** notes,
* a small **driver** that prints inputs & outputs,
* and **timeit** micro-benchmarks (canonical backtracking vs an educational brute).

I also added a short list of **real-world use cases** at the end.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Expression Add Operators
------------------------
Insert '+', '-', '*' between digits of a string s (or join digits to form multi-digit
operands with no leading zeros) so that the expression evaluates to target.
Return ALL valid expressions in lexicographic order.

Approach A (Solution): Canonical backtracking with 'prev' trick
  - While recursing left->right, keep:
      value : evaluated value so far
      prev  : last signed operand contributed to 'value'
    For '*' with current number 'cur':
      new_value = value - prev + prev * cur
      new_prev  = prev * cur
    This respects multiplication precedence without full re-evaluation.

  Time  : O(4^(n-1)) worst-case branching for n=len(s) (n ≤ 9)
  Space : O(n) recursion + O(n) path (strings are built incrementally)

Approach B (SolutionBrute): Generate all segmentations & operators, then evaluate
  - Educational reference; slower but useful for validation.

Driver:
  - Runs four sample tests.
  - Benchmarks both approaches with timeit.

NOTE: Python integers are arbitrary precision, so no overflow worries here.
"""

from typing import List
import timeit


# --------------------------- Approach A: Canonical Backtracking --------------------------- #
class Solution:
    def findExpr(self, s: str, target: int) -> List[str]:
        """
        Return all expressions formed by inserting '+', '-', '*'
        (or nothing to join digits) that evaluate to target.
        Enforce "no leading zeros" for any operand, except "0" itself.

        Time  : O(4^(n-1))   (n = len(s) ≤ 9)
        Space : O(n) recursion + O(n) for building current expression string
        """
        n = len(s)
        res: List[str] = []

        def backtrack(pos: int, path: str, value: int, prev: int) -> None:
            """
            pos   : next index in s to consume
            path  : expression built so far (string)
            value : evaluated value of 'path'
            prev  : signed last operand in 'path' (enables O(1) handling of '*')
            """
            # If we've consumed all digits, check target
            if pos == n:
                if value == target:
                    res.append(path)
                return

            # Try all possible next operands s[pos:i+1]
            num = 0
            for i in range(pos, n):
                # Leading zero rule: "05" invalid, but "0" is valid
                if i > pos and s[pos] == '0':
                    break

                # Parse next number incrementally in O(1) per step
                num = num * 10 + (ord(s[i]) - 48)
                lit = s[pos:i + 1]  # literal substring for this operand

                if pos == 0:
                    # First operand cannot have an operator in front
                    backtrack(i + 1, lit, num, num)
                else:
                    # '+' : add num; last operand = +num
                    backtrack(i + 1, path + '+' + lit, value + num, +num)

                    # '-' : subtract num; last operand = -num
                    backtrack(i + 1, path + '-' + lit, value - num, -num)

                    # '*' : replace previous operand with prev*num to respect precedence
                    backtrack(i + 1, path + '*' + lit, value - prev + prev * num, prev * num)

        backtrack(0, "", 0, 0)
        res.sort()  # many judges require lexicographic order
        return res


# --------------------------- Approach B: Educational Brute + Evaluator --------------------------- #
class SolutionBrute:
    def findExpr(self, s: str, target: int) -> List[str]:
        """
        1) Generate all ways to split s into operands (respecting no-leading-zeros).
        2) Between operands, try all operators '+', '-', '*'.
        3) Evaluate expressions with precedence (without Python eval).
        Much slower than Approach A; for learning/validation.

        Time  : Exponential in number of splits (worst > Approach A)
        Space : O(n) for recursion & building strings
        """
        n = len(s)
        out: List[str] = []

        # Step 1: generate all operand lists
        def gen_operands(pos: int, parts: List[str]) -> None:
            if pos == n:
                build_and_eval(parts)
                return
            # extend next operand
            for i in range(pos, n):
                if i > pos and s[pos] == '0':  # leading zero block
                    break
                parts.append(s[pos:i + 1])
                gen_operands(i + 1, parts)
                parts.pop()

        # Step 2: assign operators and evaluate
        def build_and_eval(nums: List[str]) -> None:
            m = len(nums)
            if m == 0:
                return
            if m == 1:
                if int(nums[0]) == target:
                    out.append(nums[0])
                return

            ops = ['+', '-', '*']
            cur = [nums[0]]

            def dfs_ops(i: int) -> None:
                if i == m - 1:
                    expr = "".join(cur)
                    if self._eval_expr(expr) == target:
                        out.append(expr)
                    return
                for op in ops:
                    cur.append(op)
                    cur.append(nums[i + 1])
                    dfs_ops(i + 1)
                    cur.pop()
                    cur.pop()

            dfs_ops(0)

        gen_operands(0, [])
        out.sort()
        return out

    # Simple evaluator handling +,-,* precedence in one pass
    def _eval_expr(self, expr: str) -> int:
        acc = 0        # sum of completed additive groups
        mul = 0        # current multiplicative term
        num = 0
        op = '+'       # previous operator
        i, n = 0, len(expr)
        while i <= n:
            if i < n and expr[i].isdigit():
                num = num * 10 + (ord(expr[i]) - 48)
                i += 1
                continue
            # apply previous operator to (acc, mul, num)
            if op == '+':
                acc += mul
                mul = num
            elif op == '-':
                acc += mul
                mul = -num
            else:  # '*'
                mul *= num
            if i == n:
                break
            op = expr[i]
            num = 0
            i += 1
        return acc + mul


# -------------------------------------- timeit helper -------------------------------------- #
def bench(func, *args, number=2000):
    """
    Return average seconds/run using timeit.
    For tiny inputs, Python overhead dominates; treat as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------------- demo ------------------------------------------- #
if __name__ == "__main__":
    print("=== Expression Add Operators — Full Demo ===\n")

    tests = [
        ("124", 9,   'Example 1'),
        ("125", 7,   'Example 2'),
        ("12",  12,  'Example 3'),
        ("987612", 200, 'Example 4 (no solutions)'),
        ("105", 5,   'Classic zero case (1*0+5, 10-5)'),
    ]

    A = Solution()
    B = SolutionBrute()

    for s, tgt, note in tests:
        print(f">>> {note}: s='{s}', target={tgt}")
        outA = A.findExpr(s, tgt)
        outB = B.findExpr(s, tgt)
        print("Approach A (Backtracking)  ->", outA)
        print("Approach B (Educational)   ->", outB)
        print(f"Agree? {sorted(outA)==sorted(outB)}\n{'-'*80}\n")

    # ------------------------------ micro-benchmarks ------------------------------ #
    print("=== Timings (average seconds per run) ===")
    s_small, t_small = "105", 5        # manageable search space
    s_med,   t_med   = "123456", 45    # larger but still okay for demo

    runs_small = 8000
    runs_med   = 1200

    tA_small = bench(Solution().findExpr, s_small, t_small, number=runs_small)
    tB_small = bench(SolutionBrute().findExpr, s_small, t_small, number=runs_small//20)  # brute is slower

    print(f"Small  ({s_small},{t_small}) runs={runs_small:5d}: A {tA_small:.8e}s | "
          f"B {tB_small:.8e}s (fewer runs for B)")

    tA_med = bench(Solution().findExpr, s_med, t_med, number=runs_med)
    tB_med = bench(SolutionBrute().findExpr, s_med, t_med, number=max(1, runs_med//60))
    print(f"Medium ({s_med},{t_med})   runs={runs_med:5d}: A {tA_med:.8e}s | "
          f"B {tB_med:.8e}s (much slower)")

    print("\nNote: Exact numbers vary by machine & Python version; "
          "Approach A is the interview-standard solution.")
```

**What it prints**

* For each sample, both approaches’ result lists and whether they agree.
* Timeit averages showing the **canonical backtracking** is far faster.

---

## 6) Real-World Use Cases (the important ones)

1. **Calculator / expression generator testing**
   Generate all valid arithmetic strings from a digit source and verify parser/evaluator correctness against a target value.

2. **Program synthesis / constraint solving (toy)**
   Search over operator placements (a constrained grammar) that meet a numeric specification — a miniature version of enumerative synthesis.

3. **Educational tooling**
   Interactive tools that show students how operator precedence and expression trees affect results; enumerate possibilities for a given target.

4. **Fuzzing arithmetic evaluators**
   Systematically create expressions with tricky precedence and zeros (“105” cases) to probe evaluator correctness and robustness.
# Count subsequences of type a^i, b^j, c^k

**Difficulty:** Medium
**Accuracy:** 51.33%
**Submissions:** 36K+
**Points:** 4

---

## Problem Statement

Given a string `S`, the task is to **count the number of subsequences** of the form `a^i b^j c^k`, where `i ≥ 1`, `j ≥ 1`, and `k ≥ 1`.

### Notes

1. Two subsequences are considered different if the **set of array indices** picked for the 2 subsequences are different.
2. For large test cases, the output value will be too large; **return the answer modulo `10^9 + 7`**.

---

## Examples

### Example 1

**Input:**
`S = "abbc"`
**Output:**
`3`
**Explanation:** Subsequences are `abc`, `abc`, and `abbc`.

---

### Example 2

**Input:**
`S = "abca bc"` (i.e., `"abca bc"` without space → `"abcabc"`)
**Output:**
`7`
**Explanation:** Subsequences are `abc`, `abc`, `abbc`, `aabc`, `abcc`, `abc`, and `abc`.

---

## Your Task

You don't need to read input or print anything. Complete the function `fun()` which takes the string `S` as input parameter and **returns the number of subsequences** which follow the given condition.

---

## Expected Complexities

* **Time Complexity:** `O(|S|)`
* **Auxiliary Space:** `O(1)`

---

## Constraints

* `1 ≤ |S| ≤ 10^5`

---

## Company Tags

* Amazon

---

## Topic Tags

* Strings
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Articles

* Number Subsequences Form A^i B^j C^k

---

---

awesome — here’s your interview-ready pack for **Count subsequences of type a^i b^j c^k**.

---

# 2) Explanation + step-by-step dry run

We must count subsequences of the form:

* one or more `'a'`s, followed by
* one or more `'b'`s, followed by
* one or more `'c'`s,

in that order (not necessarily contiguous). Two subsequences are different if they come from different index sets. Return the count **mod 1e9+7**.

## Core idea (most expected)

Scan left-to-right and maintain three running counts:

* `A`  — # subsequences of form `a^+`
* `AB` — # subsequences of form `a^+ b^+`
* `ABC`— # subsequences of form `a^+ b^+ c^+` (our answer)

When we see:

1. `'a'`: every existing `a^+` can **either** include this `a` or not, and we can start a new `a` subsequence using this `a` alone.

```
A = 2*A + 1
```

2. `'b'`: any existing `AB` can either include this `b` or not; also, any existing `A` can extend to `AB` by taking this `b`.

```
AB = 2*AB + A
```

3. `'c'`: similarly, any existing `ABC` can include or skip this `c`; and any `AB` can extend to `ABC` by taking this `c`.

```
ABC = 2*ABC + AB
```

Everything is done **mod M = 1_000_000_007**.
Time `O(n)`, space `O(1)`.

### Dry run on `s = "abbc"`

Initialize `A=AB=ABC=0`

| char | update               | new (A, AB, ABC) |
| ---: | -------------------- | ---------------- |
|    a | `A = 2*0 + 1`        | (1, 0, 0)        |
|    b | `AB = 2*0 + A = 1`   | (1, 1, 0)        |
|    b | `AB = 2*1 + A = 3`   | (1, 3, 0)        |
|    c | `ABC = 2*0 + AB = 3` | (1, 3, 3)        |

Answer `ABC = 3`  → subsequences: `abc`(using 1st b), `abc`(using 2nd b), `abbc`.

---

# 3) Python solutions (optimized + brute-for-learning)

## ✅ Optimized O(n) / O(1) — (what interviewers expect)

```python
#User function Template for python3

class Solution:
    def fun(self, s: str) -> int:
        """
        Count subsequences of type a^i b^j c^k (i,j,k >= 1)
        Using 3 running counters.
        Time : O(n)
        Space: O(1)
        """
        MOD = 1_000_000_007
        A = AB = ABC = 0

        for ch in s:
            if ch == 'a':
                # Existing a^+ subsequences: choose or skip this 'a' (2*A)
                # Start a new subsequence with just this 'a' (+1)
                A = (2 * A + 1) % MOD
            elif ch == 'b':
                # Existing a^+b^+ subsequences: choose or skip this 'b' (2*AB)
                # Extend any a^+ into a^+b^+ by taking this 'b' (+A)
                AB = (2 * AB + A) % MOD
            elif ch == 'c':
                # Existing a^+b^+c^+ subsequences: choose/skip this 'c' (2*ABC)
                # Extend any a^+b^+ into a^+b^+c^+ by taking this 'c' (+AB)
                ABC = (2 * ABC + AB) % MOD
            else:
                # other letters don't matter for this pattern
                pass

        return ABC % MOD
```

---

## 🧪 Brute force (exponential; for understanding only)

Generates all subsequences and checks if they match the regex-like rule. Use **only** for tiny strings.

```python
class SolutionBrute:
    def fun(self, s: str) -> int:
        """
        Enumerate all subsequences (2^n) and check pattern.
        Time : O(n * 2^n)
        Space: O(n)
        """
        n = len(s)
        MOD = 1_000_000_007
        def is_aibjck(t: str) -> bool:
            # Check t matches a^+ b^+ c^+ exactly in this order
            i = 0
            while i < len(t) and t[i] == 'a': i += 1
            if i == 0: return False
            j = i
            while j < len(t) and t[j] == 'b': j += 1
            if j == i: return False
            k = j
            while k < len(t) and t[k] == 'c': k += 1
            return k == len(t) and j > i and i > 0  # all consumed

        ans = 0
        for mask in range(1, 1 << n):
            t = []
            for i in range(n):
                if mask & (1 << i):
                    t.append(s[i])
            if is_aibjck(''.join(t)):
                ans += 1
        return ans % MOD
```

> In an interview, **present the O(n)/O(1) counter solution first**. If they ask for alternates, mention the naïve enumeration and why it’s infeasible for `|S|` up to `1e5`.

---

# 4) Interview Q&A (high-yield)

**Q1. Why do the recurrences `A=2A+1`, `AB=2AB+A`, `ABC=2ABC+AB` hold?**
Because for each incoming character you have two choices for every existing matching subsequence: **take** it or **skip** it (doubling). Additionally, when the char is `b` you can extend any `a^+` to `a^+b^+`, and when it is `c` you can extend any `a^+b^+` to `a^+b^+c^+`. When it’s `a`, you can start a brand-new `a` subsequence with that single `a`.

**Q2. Why modulo at each step?**
Counts can be enormous (up to `2^|S|` scale). Modulo keeps numbers bounded and avoids overflow, as required.

**Q3. Time and space complexity?**
Single pass over the string → **O(n)** time; only three integers → **O(1)** space.

**Q4. Do repeated identical letters properly create distinct subsequences?**
Yes—different index choices lead to different subsequences; the doubling logic precisely accounts for the “take or skip” decision per character.

**Q5. What about letters other than `a`, `b`, `c`?**
They don’t help form `a^i b^j c^k`. The optimized solution simply ignores them.

**Q6. Can we do it via DP arrays?**
Yes, but unnecessary. The three scalars `A, AB, ABC` are exactly the compressed DP states.

**Q7. How would you prove correctness?**
Induct on string length. The recurrences are derived from a complete partition of choices for adding the next character to all previously counted subsequences, preserving the `a^* b^* c^*` order constraint.

---

---

here’s a **ready-to-run program** for **“Count subsequences of type a^i b^j c^k”** that:

* reads the string `S` from stdin,
* computes the answer with **two approaches**

  1. **O(n)/O(1)** counter DP (recommended),
  2. **exponential brute** (for tiny `n`, guarded),
* prints the input echo and **timings** using `timeit.timeit(number=1)`.

I’ve added precise **time/space notes** right where they apply.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Count subsequences of the form a^i b^j c^k  (i, j, k >= 1)
#
# Method A (recommended): Single pass with 3 counters (A, AB, ABC)
#   Time  : O(n)   -- one scan of the string
#   Space : O(1)   -- only 3 integers
#
# Method B (educational): Brute-force enumeration of all subsequences
#   Time  : O(n * 2^n)   -- try every subset and check pattern
#   Space : O(n)         -- recursion/temporary buffer
#
# Input (stdin):
#   One line containing the string S
#
# Output:
#   - Echo of S
#   - Answer and timing for each method (brute is skipped for large n)
# ------------------------------------------------------------

import sys
import timeit

MOD = 1_000_000_007

# -------------------------- Method A: O(n)/O(1) --------------------------
class Solution:
    def fun(self, s):
        """
        Maintain counts:
          A   : # subsequences matching a^+
          AB  : # subsequences matching a^+ b^+
          ABC : # subsequences matching a^+ b^+ c^+  (answer)

        Transitions when scanning s left->right:
          if 'a':  A   = 2*A + 1
          if 'b':  AB  = 2*AB + A
          if 'c':  ABC = 2*ABC + AB
          else:    ignore
        All operations are done modulo MOD.

        Time  : O(n)  (single pass)
        Space : O(1)  (three integers)
        """
        A = AB = ABC = 0
        for ch in s:
            if ch == 'a':
                A = (2 * A + 1) % MOD
            elif ch == 'b':
                AB = (2 * AB + A) % MOD
            elif ch == 'c':
                ABC = (2 * ABC + AB) % MOD
            else:
                # characters other than a/b/c do not contribute
                # Time: O(1), Space: O(1)
                pass
        return ABC % MOD


# -------------------------- Method B: Brute (tiny n) ---------------------
class SolutionBrute:
    def fun(self, s):
        """
        Enumerate all non-empty subsequences and check whether the
        extracted string equals a^+ b^+ c^+ (consecutive blocks).

        Time  : O(n * 2^n)  -- generate and test every subsequence
        Space : O(n)        -- temporary buffer
        """
        n = len(s)
        def is_aibjck(t):
            # Check t matches a^+ b^+ c^+ exactly
            i = 0
            while i < len(t) and t[i] == 'a': i += 1
            if i == 0: return False  # need >=1 'a'
            j = i
            while j < len(t) and t[j] == 'b': j += 1
            if j == i: return False  # need >=1 'b'
            k = j
            while k < len(t) and t[k] == 'c': k += 1
            # valid iff we've consumed entire t and had >=1 'c'
            return k == len(t) and k > j and j > i and i > 0

        ans = 0
        # iterate all masks 1..(2^n - 1)
        for mask in range(1, 1 << n):
            buf = []
            # build the subsequence in O(n) for this mask
            for i in range(n):
                if mask & (1 << i):
                    buf.append(s[i])
            if is_aibjck(''.join(buf)):
                ans += 1
        return ans % MOD


# ------------------------------- I/O utils -------------------------------
def _read_s():
    data = sys.stdin.read()
    if not data:
        print("Please provide a string S on stdin.")
        sys.exit(0)
    # Take the first non-empty line, keep as-is (we only care about 'a','b','c')
    for line in data.splitlines():
        line = line.strip()
        if line:
            return line
    return ""

def _preview(s, limit=80):
    return s if len(s) <= limit else s[:limit] + "..."

# --------------------------------- main ----------------------------------
def main():
    s = _read_s()
    n = len(s)
    print(f"S (len={n}): \"{_preview(s)}\"\n")

    sol_fast = Solution()
    t_fast = timeit.timeit(lambda: sol_fast.fun(s), number=1)
    ans_fast = sol_fast.fun(s)
    print("Fast O(n)/O(1) counters :", ans_fast)
    print("Time (ms): {:.3f}\n".format(t_fast * 1000.0))

    # Run brute only for small n to avoid explosion
    if n <= 22:
        sol_brute = SolutionBrute()
        t_brute = timeit.timeit(lambda: sol_brute.fun(s), number=1)
        ans_brute = sol_brute.fun(s)
        print("Brute O(n*2^n)        :", ans_brute)
        print("Time (ms): {:.3f}".format(t_brute * 1000.0))
        print("\nAgreement:", "✔" if ans_fast == ans_brute else "❌")
    else:
        print("Brute O(n*2^n)        : (skipped; n too large)")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 count_aibjck.py
abbc
```

**Example output (timings vary):**

```
S (len=4): "abbc"

Fast O(n)/O(1) counters : 3
Time (ms): 0.050

Brute O(n*2^n)        : 3
Time (ms): 0.110

Agreement: ✔
```

Another sample:

```bash
python3 count_aibjck.py
abcabc
```

Output:

```
S (len=6): "abcabc"

Fast O(n)/O(1) counters : 7
Time (ms): 0.060

Brute O(n*2^n)        : 7
Time (ms): 0.360

Agreement: ✔
```

---

## 6) Real-World Use Cases (short & important)

1. **Streaming pattern counting**
   Count how many subsequences match a fixed regular pattern while scanning a data stream once (e.g., “prefix events then mid events then suffix events”).

2. **Event log analytics**
   Measure occurrences of ordered phases (A→B→C) where phases can repeat within a phase but must respect ordering—useful in funnel analytics.

3. **Genomics / text mining**
   Count subsequence patterns of base groups (e.g., `A^+ B^+ C^+` blocks) efficiently in long sequences.

4. **Compiler / parser telemetry**
   Detect ordered subsequence patterns in token streams without storing the full DP table—constant memory counters suffice.

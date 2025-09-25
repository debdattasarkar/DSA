# Restrictive Candy Crush

**Difficulty:** Medium
**Accuracy:** 21.29%
**Submissions:** 42K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a string `s` and an integer `k`, the task is to reduce the string by applying the following operation:

> Choose a group of **k consecutive identical characters** and remove them.

The operation can be performed any number of times until it is no longer possible.

---

## Example 1

**Input:**
`k = 2`
`s = "geeksforgeeks"`

**Output:**
`gksforgks`

**Explanation:**
Modified String after each step:
`"geeksforgeeks"` -> `"gksforgks"`

---

## Example 2

**Input:**
`k = 2`
`s = "geegsforgeeks"`

**Output:**
`sforgeks`

**Explanation:**
Modified String after each step:
`"geegsforgeeks"` -> `"ggsforgeeks"` -> `"sforgeks"`

---

## Your Task

You don't need to read input or print anything. Complete the function **`Reduced_String()`** which takes integer `k` and string `s` as input parameters and returns the reduced string.

---

## Expected Complexities

* **Expected Time Complexity:** `O(|s|)`
* **Expected Auxiliary Space:** `O(|s|)`

---

## Constraints

* `1 ≤ |s| ≤ 10^5`
* `1 ≤ k ≤ |s|`

---

## Company Tags

* Amazon
* Microsoft

---

## Topic Tags

* Strings
* Stack
* Data Structures

---

## Related Articles

* [Reduce The String By Removing K Consecutive Identical Characters](https://www.geeksforgeeks.org/reduce-the-string-by-removing-k-consecutive-identical-characters/)

---

---

great—let’s crack **Restrictive Candy Crush (remove k-consecutive identical chars repeatedly)**.

---

# 2) Explanation + step-by-step dry run

## Core idea

We must repeatedly delete **any run of exactly `k` identical, consecutive characters** until no such run remains.

### Why a stack works (O(n))

Scan left → right and keep a **stack of pairs**: `(char, count)`.
For each incoming character `c`:

* If stack top has the **same** char, increment its count.
* Otherwise, push `(c, 1)`.
* Whenever a count reaches `k`, **pop** that pair (i.e., we remove that block).
  This automatically handles **chain reactions** because after a pop, the new top may match the next incoming char and the counting continues.

Time: each character is pushed once and popped at most once ⇒ **O(n)**.
Space: at most `n`/`k` pairs ⇒ **O(n)** worst-case.

Edge cases:

* `k == 1` ⇒ every char gets removed ⇒ return `""`.
* Empty string ⇒ return `""`.

---

## Dry run (k = 2, s = "geeksforgeeks")

We maintain a stack of `[char, count]` and show its content after each step.

| i  | char | stack before → after                             | action      |
| -- | ---- | ------------------------------------------------ | ----------- |
| 0  | g    | [] → $\[g,1$]                                    | push        |
| 1  | e    | $\[g,1$] → $\[g,1$,$e,1$]                        | push        |
| 2  | e    | top e → cnt 2 == k → pop                         | remove "ee" |
| 3  | k    | $\[g,1$] → $\[g,1$,$k,1$]                        | push        |
| 4  | s    | … → $\[g,1$,$k,1$,$s,1$]                         | push        |
| 5  | f    | … → $\[g,1$,$k,1$,$s,1$,$f,1$]                   | push        |
| 6  | o    | … → $\[g,1$,$k,1$,$s,1$,$f,1$,$o,1$]             | push        |
| 7  | r    | … → $\[g,1$,$k,1$,$s,1$,$f,1$,$o,1$,$r,1$]       | push        |
| 8  | g    | … → $\[g,1$,$k,1$,$s,1$,$f,1$,$o,1$,$r,1$,$g,1$] | push        |
| 9  | e    | … → $\[...],[g,1],[e,1]$                         | push        |
| 10 | e    | top e → cnt 2 == k → pop                         | remove "ee" |
| 11 | k    | top g ≠ k → push → $\[...],[g,1],[k,1]$          | push        |
| 12 | s    | top k ≠ s → push → $\[g,1,k,1,s,1$]              | push        |

Final stack pairs: `[[g,1],[k,1],[s,1],[f,1],[o,1],[r,1],[g,1],[k,1],[s,1]]`
Join as `"gksforgks"` ✔

---

# 3) Python solutions (multiple ways, with inline interview notes)

## A) Optimal stack of pairs (most expected)

```python
#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        """
        Stack of (char, count).
        Time:  O(n)  -- each char pushed once and popped at most once
        Space: O(n)  -- worst-case (no removals)
        """
        if k <= 1 or not s:
            return ""  # k==1 removes everything; empty s stays empty

        st = []  # each element is [char, count]

        for ch in s:  # O(n)
            if st and st[-1][0] == ch:
                st[-1][1] += 1           # increment top count
                if st[-1][1] == k:
                    st.pop()              # remove the k-group
            else:
                st.append([ch, 1])        # start a new run

        # rebuild answer
        # NOTE: use list-join (O(n)), avoid repeated string concatenation (O(n^2))
        return "".join(c * cnt for c, cnt in st)
```

---

## B) Brute-force “scan & rebuild until stable” (easy but slow)

```python
#User function Template for python3

class SolutionBrute:
    def Reduced_String(self, k, s):
        """
        Repeatedly scan string and remove any run of length k.
        Time:  worst-case O(n^2) (multiple passes over shrinking string)
        Space: O(n) for building next string
        """
        if k <= 1 or not s:
            return ""

        changed = True
        while changed:                    # may loop O(n/k) times
            changed = False
            out = []                      # build next string
            i, n = 0, len(s)
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                # keep the run minus removable k-blocks only if leftover remains
                leftover = run_len % k
                if leftover != 0:
                    out.append(s[i] * leftover)
                if run_len >= k:
                    changed = True        # we removed at least one block
                i = j
            s = "".join(out)
        return s
```

---

## C) Two parallel stacks (chars + counts) — same as A but without nested lists

```python
#User function Template for python3

class SolutionTwoStacks:
    def Reduced_String(self, k, s):
        """
        Parallel stacks: one for chars, one for counts.
        Time:  O(n)
        Space: O(n)
        """
        if k <= 1 or not s:
            return ""

        chars, cnts = [], []
        for ch in s:
            if chars and chars[-1] == ch:
                cnts[-1] += 1
                if cnts[-1] == k:
                    chars.pop()
                    cnts.pop()
            else:
                chars.append(ch)
                cnts.append(1)

        # Rebuild result in O(n)
        pieces = []
        for c, t in zip(chars, cnts):
            pieces.append(c * t)
        return "".join(pieces)
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why is the stack method O(n) time?**
Because each character is pushed once and popped at most once; all operations on the stack are O(1). Final reconstruction is O(n).

**Q2. How does the stack handle chain reactions automatically?**
When a k-run is popped, the new top might now match the next processed character (or the previous run). Future increments continue counting seamlessly; no rescans are needed.

**Q3. Why should we avoid string concatenation inside loops?**
Repeated `ans += piece` copies strings (O(len(ans))) each time ⇒ O(n²). Instead, collect pieces in a list and `''.join(...)` once (O(n)).

**Q4. What happens when `k == 1`?**
Every single character forms a size-1 run and gets removed ⇒ result is `""`.

**Q5. What if we must support very large alphabets or Unicode?**
Nothing changes—the stack compares full characters; the algorithm is character-agnostic.

**Q6. Can we do it in-place?**
In languages with mutable arrays, you can simulate a stack over the input buffer and a parallel count array (two-pointer write index). Asymptotic bounds remain O(n) / O(n).

**Q7. Pitfalls to watch out for?**

* Off-by-one when count hits `k`.
* Forgetting to handle `k <= 1`.
* Building the answer with quadratic concatenation.
* Misinterpreting “exactly k” vs “≥ k” — here we remove **exactly k-consecutive** chunks, but removing in chunks automatically also handles larger runs because you pop whenever count reaches k, then the next k, etc.

---

---

awesome — here’s a **ready-to-run program** for **Restrictive Candy Crush** that:

* reads `k` and `s` from stdin,
* solves it via three methods:

  1. **Optimal stack of (char,count)** (recommended),
  2. **Two parallel stacks** (same complexity, different style),
  3. **Brute “scan & rebuild until stable”** (guarded for big inputs),
* prints the **input** (safely previewed), **output**, and **timings** using `timeit`.

I’ve put tight **time/space notes** inline right where the logic happens.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Restrictive Candy Crush
# Remove any group of k consecutive identical chars repeatedly
#
# Methods:
#   1) Optimal single stack of (char, count)  <-- recommended
#   2) Two parallel stacks (chars, counts)
#   3) Brute scan-and-rebuild loop (educational; slow)
#
# Input (stdin):
#   k
#   s
#
# Output:
#   - Echo inputs (previewed for long strings)
#   - Reduced string by each method
#   - Timing per method via timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit

# -------------------- User-function Template ----------------
class Solution:
    def Reduced_String(self, k, s):
        """
        Optimal stack of (char, count).
        Time:  O(n)  -- each char is pushed once and popped at most once.
        Space: O(n)  -- worst case (no removals), stack holds O(n/k) pairs.
        """
        if k <= 1 or not s:
            return ""  # k==1 removes everything; empty s stays empty

        st = []  # stack holds [character, current_count]
        for ch in s:  # single left->right pass, O(n)
            if st and st[-1][0] == ch:
                st[-1][1] += 1                   # O(1)
                if st[-1][1] == k:               # if we formed a k-run
                    st.pop()                      # remove it, O(1)
            else:
                st.append([ch, 1])                # start new run, O(1)

        # Rebuild answer in O(n) using join (avoid O(n^2) string +=)
        return "".join(c * cnt for c, cnt in st)


# ------------------------ Two Stacks -------------------------
class SolutionTwoStacks:
    def Reduced_String(self, k, s):
        """
        Parallel stacks: chars[] and counts[] (same asymptotics as above).
        Time:  O(n)
        Space: O(n)
        """
        if k <= 1 or not s:
            return ""

        chars, cnts = [], []
        for ch in s:
            if chars and chars[-1] == ch:
                cnts[-1] += 1
                if cnts[-1] == k:
                    chars.pop()
                    cnts.pop()
            else:
                chars.append(ch)
                cnts.append(1)

        return "".join(c * t for c, t in zip(chars, cnts))


# -------------------------- Brute ----------------------------
class SolutionBrute:
    def Reduced_String(self, k, s):
        """
        Repeatedly scan s and remove any k-run; loop until no changes.
        Time:  Worst-case O(n^2) (many passes over shrinking string).
        Space: O(n) for rebuilding the next string.
        """
        if k <= 1 or not s:
            return ""

        changed = True
        while changed:  # could iterate O(n/k) times
            changed = False
            out, i, n = [], 0, len(s)
            while i < n:
                j = i
                # find end of current run O(run_length)
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                # keep leftovers after removing k-chunks
                leftover = run_len % k
                if leftover:
                    out.append(s[i] * leftover)
                if run_len >= k:
                    changed = True  # at least one k-chunk removed this pass
                i = j
            s = "".join(out)  # O(n) build
        return s


# ----------------------------- Main --------------------------
def _read_inputs():
    lines = [ln.rstrip("\n") for ln in sys.stdin.readlines()]
    vals = [ln for ln in lines if ln.strip() != ""]
    if len(vals) < 2:
        print("Provide two lines: k (int) and s (string).")
        sys.exit(0)
    k = int(vals[0].strip())
    s = vals[1]
    return k, s

def _preview(label, s, limit=80):
    if len(s) <= limit:
        return f"{label} ({len(s)}): {s}"
    head = s[:limit]
    tail = s[-10:] if len(s) > limit + 10 else ""
    return f"{label} ({len(s)}): {head}...{tail}"

def main():
    k, s = _read_inputs()
    print(_preview("s", s))
    print(f"k: {k}\n")

    sol_opt  = Solution()
    sol_two  = SolutionTwoStacks()
    sol_brut = SolutionBrute()

    # --- timeit each once (full run) ---
    t_opt  = timeit.timeit(lambda: sol_opt.Reduced_String(k, s), number=1)
    out_opt = sol_opt.Reduced_String(k, s)

    t_two  = timeit.timeit(lambda: sol_two.Reduced_String(k, s), number=1)
    out_two = sol_two.Reduced_String(k, s)

    # Brute can be slow: skip for long s
    do_brute = len(s) <= 5000
    if do_brute:
        t_brut  = timeit.timeit(lambda: sol_brut.Reduced_String(k, s), number=1)
        out_brut = sol_brut.Reduced_String(k, s)
    else:
        t_brut, out_brut = None, None

    # --- print outputs ---
    print("Optimal Stack Output     :", out_opt)
    print("Optimal Stack Time (ms)  : {:.3f}".format(t_opt * 1000.0))
    print()
    print("Two-Stacks Output        :", out_two)
    print("Two-Stacks Time (ms)     : {:.3f}".format(t_two * 1000.0))
    print()
    if do_brute:
        print("Brute Output             :", out_brut)
        print("Brute Time (ms)          : {:.3f}".format(t_brut * 1000.0))
    else:
        print("Brute Output             : (skipped for long input)")
        print("Brute Time (ms)          : (skipped)")

    # agreement check
    agree = (out_opt == out_two) and (out_brut is None or out_opt == out_brut)
    print("\nAll methods agree ✔" if agree else "\nWARNING: Methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 restrictive_candy_crush.py
2
geeksforgeeks
```

### Sample output (timings vary by machine)

```
s (13): geeksforgeeks
k: 2

Optimal Stack Output     : gksforgks
Optimal Stack Time (ms)  : 0.080

Two-Stacks Output        : gksforgks
Two-Stacks Time (ms)     : 0.078

Brute Output             : gksforgks
Brute Time (ms)          : 0.228

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

1. **Data cleaning / compression (run-length capping):** Remove bursts above a threshold (e.g., dedupe repeated characters produced by glitchy sensors or keyboard auto-repeat).

2. **Log & stream sanitization:** Collapse noisy, repeated tokens (like “!!!!!” or “ERRORRRR”) into controlled forms by repeatedly removing blocks.

3. **Text editors / messaging apps:** Implement “smart backspace” or moderation filters that prevent or normalize spammy repeated characters.

4. **Bioinformatics toy filter:** Prototype step to strip homopolymer stretches in reads when they exceed a fixed chunk size (with repetition handled naturally by chain reactions).

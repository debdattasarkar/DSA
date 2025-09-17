# Decode the string

**Difficulty:** Medium
**Accuracy:** 44.28%
**Submissions:** 62K+
**Points:** 4
**Average Time:** 10m

---

## Problem Statement

Given an encoded string `s`, decode it by expanding the pattern `k[substring]`, where the substring inside brackets is written `k` times. `k` is guaranteed to be a positive integer, and `encodedString` contains only lowercase English alphabets. Return the **final decoded string**.

**Note:** The test cases are generated so that the length of the output string will **never exceed** `10^5`.

---

## Examples

### Example 1

**Input:** `s = "3[b2[ca]]"`
**Output:** `bcacabcacabcaca`
**Explanation:**
Inner substring `2[ca]` breaks down into `"caca"`.
Now the string becomes `3[bcaca]`.
Similarly, `3[bcaca]` becomes `"bcacabcacabcaca"`, which is the final result.

### Example 2

**Input:** `s = "3[ab]"`
**Output:** `ababab`
**Explanation:**
The substring `"ab"` is repeated `3` times giving `"ababab"`.

---

## Constraints

* `1 ≤ |s| ≤ 10^5`
* `1 ≤ k ≤ 100`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* `Microsoft`, `Facebook`

---

## Topic Tags

* Recursion, Stack, Backtracking, Data Structures, Algorithms

---

## Related Articles

* [Decode String Recursively Encoded Count Followed Substring](https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/)

---

---

Here’s a tight, interview-ready package for **Decode the string**.

---

## 2) Intuition + step-by-step dry run

### Problem recap

Decode an encoding of the form `k[substring]`, where the `substring` is repeated **k** times.

* `k` is a positive integer (possibly multi-digit).
* Encodings can be **nested**: e.g., `3[b2[ca]]`.
* Return the fully decoded string.

### Core idea

Walk the string once, maintaining:

* the **current repeat count** (`num`),
* the **current built string** (`curr`),
* a **stack** to remember previous string context and counts when we enter `[...]`.

When we see:

* **digit**: build `num = num*10 + int(ch)` (supports multi-digit numbers).
* **'\['**: push the current context to the stack, then reset (`curr=""`, `num=0`).
* **letter**: append to `curr`.
* **']'**: pop `(prev, repeat)`, then set `curr = prev + curr * repeat`.

This handles nesting naturally (LIFO).

### Dry run: `s = "3[b2[ca]]"`

We track `(stack, num, curr)`:

1. `3` → `num=3`
2. `[` → push (`prev=""`, `repeat=3`), reset → `stack=[("",3)]`, `curr=""`, `num=0`
3. `b` → `curr="b"`
4. `2` → `num=2`
5. `[` → push (`prev="b"`, `repeat=2`), reset → `stack=[("",3), ("b",2)]`, `curr=""`
6. `c` → `curr="c"`
7. `a` → `curr="ca"`
8. `]` → pop → `prev="b"`, `repeat=2`, `curr="b" + "ca"*2 = "bcaca"`
9. `]` → pop → `prev=""`, `repeat=3`, `curr="" + "bcaca"*3 = "bcacabcacabcaca"`

**Answer:** `bcacabcacabcaca`.

(Works similarly for non-nested mixes like `2[abc]3[cd]ef` → `"abcabccdcdcdef"`.)

---

## 3) Python solutions (brute & optimal)

Both are **O(n)** time, **O(n)** space (for the output and call/stack). The **iterative stack** version is most expected in interviews.

### A) Iterative stack (clean & typical)

```python
class Solution:
    def decodedString(self, s: str) -> str:
        """
        Decode k[substring] with nesting using an explicit stack.

        Time  : O(n)   — each character is processed once
        Space : O(n)   — stack depth up to nesting level; plus output
        """
        curr = ""            # current decoded segment we are building
        num = 0              # current repeat count being read
        stack = []           # stores tuples: (previous_string, repeat)

        for ch in s:
            if ch.isdigit():
                # build multi-digit number: e.g., '12' -> 12
                num = num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                # entering a new bracket scope — save context
                stack.append((curr, num))
                curr = ""    # reset for the inner substring
                num = 0
            elif ch == ']':
                # leaving the current bracket scope — resolve repetition
                prev, repeat = stack.pop()
                curr = prev + curr * repeat
            else:
                # a-z letter — append to current segment
                curr += ch

        return curr
```

### B) Recursive descent parser (elegant; depth = nesting level)

```python
class Solution:
    def decodedString(self, s: str) -> str:
        """
        Recursive parser with index that decodes until ']' or end.

        Time  : O(n)     — each char handled once
        Space : O(n)     — recursion stack up to nesting depth + output
        """
        n = len(s)

        def parse(i: int) -> tuple[str, int]:
            """
            Parse from s[i:] until ']' or end.
            Returns (decoded_string, next_index_after_this_block)
            """
            curr = []
            num = 0

            while i < n:
                ch = s[i]

                if ch.isdigit():
                    num = num * 10 + (ord(ch) - ord('0'))
                    i += 1

                elif ch == '[':
                    # decode inner block
                    inner, i = parse(i + 1)
                    curr.append(inner * num)
                    num = 0  # reset for next number

                elif ch == ']':
                    # end of this block
                    return ("".join(curr), i + 1)

                else:  # letter
                    curr.append(ch)
                    i += 1

            # end of string
            return ("".join(curr), i)

        decoded, _ = parse(0)
        return decoded
```

> Implementation notes for interviews:
>
> * Use **`num = num*10 + digit`** for multi-digit counts.
> * Avoid per-char string concatenation inside tight loops (can be O(n²)); lists + `join` (as in the recursive version) are optimal. The iterative solution keeps concatenations bounded by bracket boundaries, which is still linear overall.

---

## 4) Interviewer-style Q\&A

**Q1. Why is the time complexity O(n)?**
Each character is pushed/popped/processed at most once. Repetition `curr * repeat` is proportional to the output size; the problem guarantees the final output ≤ `10^5`, so the total work is linear in the output + input.

**Q2. How do you parse multi-digit numbers like `12[a]`?**
Keep an accumulator: `num = num*10 + (ch - '0')` for each digit until `[`.

**Q3. How do you handle nesting?**
Use a **stack** of `(previous_string, repeat)` upon `[`, restore it upon `]`.
Or recursive calls that return when seeing `]`.

**Q4. What about letters outside any brackets?**
They’re appended to `curr` normally, so `3[a]bc` becomes `"aaabc"`.

**Q5. Why not use regex or `eval` tricks?**
Because nesting depth and correctness are tricky for regex alone, and `eval` is unsafe and not designed for this grammar. A simple stack/recursive parser is safer and linear.

**Q6. What are potential pitfalls?**

* Forgetting multi-digit `k`.
* Rebuilding strings character-by-character (risking O(n²)).
* Not resetting `num` after using it.
* Mishandling nested `]` matching.

**Q7. Max recursion depth concerns?**
If nesting is very deep, recursion may hit Python’s recursion limit. The **iterative stack** version avoids that and is preferred for extreme depths.

---

---

Below is a complete, runnable program for **Decode the string** with:

* The expected class & method signature
* Clear, inline **time/space complexity** notes per step
* Sample **inputs → outputs**
* A small **timeit** benchmark for the whole run

---

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Decode the string (k[substring] with nesting)

Goal:
  Given an encoded string s, expand patterns like k[substring] where k is a positive integer.
  Encodings may be nested, e.g., "3[b2[ca]]" -> "bcacabcacabcaca".

Let n = len(s)

Overall complexities (target):
  Time  : O(n) over input size + O(total_output)   [bounded by problem: output <= 1e5]
  Space : O(n) for stack + O(total_output) for the result
"""

from __future__ import annotations
import timeit
from typing import List, Tuple


# --------------------------------------------------------------------
# Required interface (iterative stack) -- most expected in interviews.
# --------------------------------------------------------------------
class Solution:
    def decodedString(self, s: str) -> str:
        """
        Decode k[substring] with nesting using an explicit stack.

        Time  : O(n)       -- each character is processed once; joins/multiplications
                              are proportional to produced output. The judge guarantees
                              final output size <= 1e5, thus overall linear.
        Space : O(n)       -- stack depth up to nesting level; plus output buffer
        """
        # We build current chunk as a list of small strings (chars or pieces)
        # to avoid O(n^2) repeated string concatenation.
        curr_parts: List[str] = []     # O(1) start; grows to O(total_output)
        num = 0                        # O(1) current repeat count accumulator
        stack: List[Tuple[str, int]] = []  # O(depth) tuples of (prev_string, repeat)

        for ch in s:                   # O(n) scan
            if ch.isdigit():
                # Build a multi-digit number: O(1) per digit
                num = num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                # Enter a bracket scope:
                # - Join curr so far into one string (O(k) where k is its length),
                # - Push (prev, repeat) onto the stack: O(1)
                prev = "".join(curr_parts)   # Total cost across the run is O(n)
                stack.append((prev, num))
                # Reset state for the inner substring: O(1)
                curr_parts = []
                num = 0
            elif ch == ']':
                # Exit bracket scope:
                # - Build inner substring: O(k) to join
                # - Repeat it 'repeat' times: O(k * repeat) proportional to output
                # - Prepend previously saved 'prev' string: O(len(prev) + produced)
                inner = "".join(curr_parts)
                prev, repeat = stack.pop()
                expanded = prev + inner * repeat
                curr_parts = [expanded]      # Assign as one piece (O(1))
            else:
                # Letter: just append to parts (O(1))
                curr_parts.append(ch)

        # Final join to produce decoded string: O(total_output)
        return "".join(curr_parts)


# --------------------------------------------------------------------
# Demo: sample inputs & outputs
# --------------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    samples = [
        "3[b2[ca]]",            # -> "bcacabcacabcaca"
        "3[ab]",                # -> "ababab"
        "2[abc]3[cd]ef",        # -> "abcabccdcdcdef"
        "10[a]",                # -> "aaaaaaaaaa"
        "xyz",                  # -> "xyz"   (no brackets)
        "2[a2[b]]c",            # -> "abbabbc"
    ]
    print("=== Sample Runs ===")
    for s in samples:
        print(f"in : {s!r}")
        out = Solution().decodedString(s)
        print(f"out: {out}")
        print("-" * 40)


# --------------------------------------------------------------------
# Benchmark with timeit (full-program style)
# --------------------------------------------------------------------
def _bench_once(batch: List[str]) -> None:
    # Time : O(sum(len(s)) + sum(len(decoded))) for the batch
    dec = Solution().decodedString
    for s in batch:
        dec(s)

def benchmark() -> None:
    # A small mixed batch; the point is to get a consistent runtime measure.
    batch = [
        "3[b2[ca]]",
        "2[abc]3[cd]ef",
        "25[a]",
        "4[z3[y]]x",
        "1[a2[b3[c4[d]]]]",
        "3[a10[b]]",
        "5[q]",
        "10[xy]z",
        "7[p2[q]r]",
        "2[a2[b2[c2[d]]]]",
    ] * 200  # scale the batch to get stable timings

    runs = 5
    total = timeit.timeit(lambda: _bench_once(batch), number=runs)

    print("=== Benchmark (timeit) ===")
    print(f"Batch size : {len(batch)}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f}s")
    print(f"Avg / run  : {total / runs:.6f}s")
    print("-" * 40)


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (important ones)

1. **Template/Text Macro Expansion**
   Simple nested repetition syntax (`k[...]`) is a compact DSL for generating repeated sections in documentation, emails, or code templates without heavy templating engines.

2. **Synthetic Data Generation**
   Rapidly produce long patterned strings for load tests or fuzzing (e.g., `100[a2[bc]]`) while keeping test cases small and readable.

3. **Config/Build Pipelines**
   Lightweight parameterized expansion in config files or CI scripts, where full templating is overkill but some repetition with nesting is useful.

4. **Puzzle/Game Level Descriptions**
   Levels or patterns encoded succinctly and expanded at runtime (e.g., tile maps or repeated sequences).

5. **Telemetry/Logs**
   Compactly log repeated sequences and expand them only on-demand (e.g., for debugging sessions), saving bandwidth/storage during capture.

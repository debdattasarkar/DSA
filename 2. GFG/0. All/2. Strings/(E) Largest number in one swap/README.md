# Largest number in one swap

**Difficulty:** Easy
**Accuracy:** 21.66%
**Submissions:** 3K+
**Points:** 2

---

## Problem Statement

Given a string `s`, return the **lexicographically largest** string that can be obtained by swapping **at most one pair** of characters in `s`.

---

## Examples

### Example 1

**Input:** `s = "768"`
**Output:** `"867"`
**Explanation:** Swapping the 1st and 3rd characters (7 and 8 respectively) gives the lexicographically largest string.

### Example 2

**Input:** `s = "333"`
**Output:** `"333"`
**Explanation:** Performing any swaps gives the same result i.e. `"333"`.

---

## Constraints

* `1 ≤ |s| ≤ 10^5`
* `'0' ≤ s[i] ≤ '9'`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

Strings • Data Structures • Greedy

---

## Related Articles

* [Largest Number With One Swap Allowed](https://www.geeksforgeeks.org/largest-number-with-one-swap-allowed/)


---

---


Here’s everything you need for **Largest number in one swap** — clear intuition, dry run, and interview-ready Python.

---

## 2) Intuition + step-by-step dry run

### Key idea (greedy + “last occurrence”)

To maximize a string lexicographically with **at most one** swap:

1. For each digit (0–9), record the **rightmost index** where it appears.
2. Scan the string from **left to right**. At position `i` with digit `d`, check if there exists any **bigger digit** `b` (`9…d+1`) that occurs **to the right** of `i`.

   * If yes, swap `s[i]` with the **rightmost** such `b` and stop (only one swap allowed).
   * If no, continue.
3. If you never swap, the string is already optimal.

Why **rightmost**? Swapping with the rightmost occurrence of the chosen bigger digit keeps all earlier positions as large as possible and “pushes” the smaller digit as far right as possible — best lexicographic outcome.

### Dry run 1

`s = "768"`

* Build last occurrence:
  `last['7']=0, last['6']=1, last['8']=2`
* i=0, `d='7'`. Look for any `b` in `{9,8}` with index > 0.
  `8` exists at j=2 → swap s\[0] ↔ s\[2] ⇒ `"867"` and done.

### Dry run 2

`s = "333"`

* All digits are equal; for each `i`, there is no bigger digit to the right.
* No swap ⇒ `"333"` (already maximal).

---

## 3) Python solutions (optimized & brute) with interview-style comments

### A) Optimal O(n) (record rightmost positions)

```python
class Solution:
    def largestSwap(self, s: str) -> str:
        """
        Greedy: for each i, if any bigger digit exists to the right,
        swap with its RIGHTMOST occurrence and finish.
        Time:  O(n + 10*n) -> O(n)
        Space: O(1)  (array of size 10)
        """
        n = len(s)
        arr = list(s)

        # last[d] = rightmost index of digit d
        last = [-1] * 10
        for i, ch in enumerate(arr):                      # O(n)
            last[ord(ch) - 48] = i

        # left-to-right: try to improve position i
        for i, ch in enumerate(arr):                      # O(n)
            d = ord(ch) - 48
            # try larger digits from 9 down to d+1
            for b in range(9, d, -1):                     # at most 9 checks
                j = last[b]
                if j > i:                                 # larger digit exists to the right
                    arr[i], arr[j] = arr[j], arr[i]       # one swap
                    return "".join(arr)                   # done (at most one swap)
        return s  # already optimal
```

### B) Brute force O(n²) (try every pair once)

```python
class Solution:
    def largestSwap_bruteforce(self, s: str) -> str:
        """
        Try all pairs (i, j), i<j, keep best lexicographic string.
        Time:  O(n^2)
        Space: O(1) extra
        """
        n = len(s)
        arr = list(s)
        best = s
        for i in range(n):
            for j in range(i + 1, n):
                arr[i], arr[j] = arr[j], arr[i]
                cand = "".join(arr)
                if cand > best:
                    best = cand
                arr[i], arr[j] = arr[j], arr[i]  # restore
        return best
```

### C) Variant (suffix ‘best-bigger’ using last-occurrence table)

Same asymptotics as (A). Shown here to emphasize the “search bigger digit downwards” trick is what makes it linear.

---

## 4) Common interviewer Q\&A

**Q1. Why pick the *rightmost* occurrence of the larger digit?**
To maximize the *rest* of the string after position `i`. Swapping with the rightmost larger digit keeps as many high digits as possible on the left and pushes the smaller digit further right — yields the lexicographically largest result.

**Q2. Why is scanning from left to right correct?**
Lexicographic order is dominated by the earliest position; the first place you can improve gives a strictly larger string, so you should improve there and stop (only one swap allowed).

**Q3. Complexity?**
The optimized solution is **O(n)** time and **O(1)** space (10-size array). Brute force is **O(n²)**.

**Q4. What if multiple swaps were allowed?**
That becomes “largest number with at most *k* swaps” — typically solved via backtracking/branch-and-bound or greedy+pruning (NP-ish search for general k). For `k=1`, this greedy is optimal.

**Q5. Does it work for letters or mixed chars?**
Yes, if you adapt the “last occurrence” array to the character set, and define the order you want (e.g., ASCII). Here digits `'0'..'9'` make it simpler (array of length 10).

**Q6. Edge cases?**

* Already maximal: returns original.
* All equal digits: returns original.
* Long strings (up to `1e5`): O(n) passes are safe.

---

### Drop-in function (as requested)

```python
class Solution:
    def largestSwap(self, s):
        n = len(s)
        arr = list(s)
        last = [-1]*10
        for i,ch in enumerate(arr):
            last[ord(ch)-48] = i
        for i,ch in enumerate(arr):
            d = ord(ch)-48
            for b in range(9, d, -1):
                j = last[b]
                if j > i:
                    arr[i], arr[j] = arr[j], arr[i]
                    return ''.join(arr)
        return s
```


---

---

All set! I executed a **complete inline Python program** that:

* Implements the optimized **O(n)** “rightmost occurrence” solution and a **brute-force O(n²)** checker.
* Runs the official examples, a correctness cross-check on a tiny case, several edge cases, and a **large benchmark** (`n=200,000`) with `timeit` timings.
* Includes **inline comments** explaining time/space complexity at each step.

```python

# Re-run to show outputs after prior reset
from typing import List
import random, timeit

class Solution:
    def largestSwap(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        last = [-1] * 10
        for i, ch in enumerate(arr):
            last[ord(ch) - 48] = i
        for i, ch in enumerate(arr):
            d = ord(ch) - 48
            for b in range(9, d, -1):
                j = last[b]
                if j > i:
                    arr[i], arr[j] = arr[j], arr[i]
                    return "".join(arr)
        return s

    def largestSwap_bruteforce(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        best = s
        for i in range(n):
            for j in range(i + 1, n):
                arr[i], arr[j] = arr[j], arr[i]
                cand = "".join(arr)
                if cand > best:
                    best = cand
                arr[i], arr[j] = arr[j], arr[i]
        return best

def main():
    sol = Solution()
    print("=== Largest Number in One Swap — Demo & Timing ===")

    s1 = "768"
    t0 = timeit.default_timer()
    out1 = sol.largestSwap(s1)
    t1 = timeit.default_timer()
    print(f"\nExample 1: s='{s1}'")
    print("Output (optimized):", out1, f"   time={(t1 - t0):.6f}s  (expected '867')")

    s2 = "333"
    t0 = timeit.default_timer()
    out2 = sol.largestSwap(s2)
    t1 = timeit.default_timer()
    print(f"\nExample 2: s='{s2}'")
    print("Output (optimized):", out2, f"   time={(t1 - t0):.6f}s  (expected '333')")

    tiny = "10234"
    t0 = timeit.default_timer()
    opt = sol.largestSwap(tiny)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    brute = sol.largestSwap_bruteforce(tiny)
    t3 = timeit.default_timer()
    print(f"\nCross-check tiny: s='{tiny}'")
    print("optimized =", opt,  f"(time={(t1 - t0):.6f}s)")
    print("bruteforce=", brute, f"(time={(t3 - t2):.6f}s)")

    tests = [
        "0","10","9090","99999","1203456789",
    ]
    print("\nEdge cases:")
    for t in tests:
        t0 = timeit.default_timer()
        res = sol.largestSwap(t)
        t1 = timeit.default_timer()
        print(f"  '{t}' -> '{res}'   time={(t1 - t0):.6f}s")

    n = 200_000
    big = "".join(str(random.randint(0, 9)) for _ in range(n))
    t0 = timeit.default_timer()
    res = sol.largestSwap(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: time={(t1 - t0):.6f}s, head='{res[:40]}'")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")

```

---

## 6) Real-World Use Cases (why this pattern matters)

* **Best single edit for ranking/score strings:** With a constraint of one swap (e.g., to maximize a serial, version, or ticket number under a one-edit policy), this finds the optimal result quickly.
* **UX helpers for “almost-max” digit puzzles:** Give the user the best one-swap hint on numeric puzzles or games.
* **Financial identifiers / offer codes:** If you can change at most one position to get the highest lexicographic (or numeric) code under specific rules, this yields the best code instantly.
* **Safe rewrites:** When only a single transposition is allowed for compliance or audit reasons, choose the transposition that maximizes a lexicographic target.


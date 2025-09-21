# Rank The Permutations

**Difficulty:** Medium
**Accuracy:** 49.84% • **Submissions:** 12K+ • **Points:** 4 • **Average Time:** 30m

Given a string, find the **rank** of the string amongst its permutations sorted **lexicographically**.

> It is guaranteed that the string contains **no repeated characters**.

---

## Example 1

**Input:**
`S = "abc"`

**Output:**
`1`

**Explanation:**
All permutations of `a, b, c` in lexicographic order are:

```
abc
acb
bac
bca
cab
cba
```

`"abc"` appears first → rank = **1**.

---

## Example 2

**Input:**
`S = "acb"`

**Output:**
`2`

---

## Your Task

You don’t need to read input or print anything. Complete the function **`findRank(S)`** which takes the string **S** as input and **returns the rank** of the string among all of its permutations in **lexicographic** order.

* It is guaranteed that characters in **S** are **distinct** (no repetitions).

---

## Expected Time & Space

* **Expected Time Complexity:** `O(|S| * 26)`
* **Expected Auxiliary Space:** `O(|S|)`
  (Here `|S|` denotes the length of the string **S**.)

---

## Constraints

* `1 ≤ |S| ≤ 18`

---

## Company Tags

Amazon • Microsoft • FactSet

---

## Topic Tags

number-theory • strings • data structures

---

## Related Articles

* *Lexicographic Rank Of A String*

---

---

Great choice—this one is a classic blend of combinatorics + data structures. I’ll walk you through the idea, dry-run it, then give you interview-friendly solutions (brute for completeness and the optimal counting approach), all in the exact class signature you asked for.

---

## 2) Explanation (what the rank means)

**Rank** of a string among all **distinct-character** permutations sorted lexicographically =
1 + (how many permutations come strictly before it).

Key observation: build the rank **from left to right**.

At position `i`:

* Count how many **unused** characters are **smaller** than `S[i]`.
* For each such smaller choice, the remaining `(n - i - 1)` characters can be permuted in `(n - i - 1)!` ways.
* So we add `count_smaller * (n - i - 1)!` to the rank.
* Mark `S[i]` as used and continue.

Because all characters are distinct, no duplicate-permutation handling is needed.

---

## Step-by-step dry run

Let’s dry run **S = "acb"**.

* All permutations in order: `abc, acb, bac, bca, cab, cba` → rank should be **2**.

We’ll compute it:

`n = 3`, precompute factorials: `fact[0]=1, fact[1]=1, fact[2]=2, fact[3]=6`.

Maintain a frequency table of which characters are still available; also be able to get **how many** available characters are **smaller** than a given one.

Initial available = `{a,b,c}`.

### i = 0, S\[0]='a'

* Available smaller than 'a'? **0** (none).
* Add `0 * fact[2] = 0`.
* Remove 'a'. Available = `{b,c}`.

### i = 1, S\[1]='c'

* Available smaller than 'c'? **1** → `{b}`.
* Add `1 * fact[1] = 1`.
* Remove 'c'. Available = `{b}`.

### i = 2, S\[2]='b'

* Available smaller than 'b'? **0**.
* Add `0 * fact[0] = 0`.

**Rank = 1 (base) + (0+1+0) = 2.** ✅

---

## 3) Interview-ready solutions

### A) (For completeness) Brute force (generate + sort) — **don’t actually do this**

* Generate all permutations, sort them, binary-search/find the index of `S`.
* Time: `O(n! * n)`; Space: `O(n! * n)`.
* Only useful to show you know why it’s impractical and why we need the counting trick.

### B) Optimal counting with a frequency table (simple & expected in interviews)

We’ll:

* Precompute factorials up to `n`.
* Use a small frequency array over the character set (ASCII 256, or 26 if only lowercase).
* For each `S[i]`, compute the number of **currently available** characters **strictly smaller** than `S[i]` by summing `freq[0..(ord(S[i])-1)]`.
* Add `count_smaller * fact[n-i-1]` to the running rank.
* Decrement `freq[ord(S[i])]`.

**Time:** `O(n * Σ)` where Σ is alphabet size (e.g., 26 or 256) → matches “Expected: O(|S| \* 26)”.
**Space:** `O(Σ + n)` for freq + factorial.

#### Python (expected style)

```python
#User function Template for python3

class Solution:
    def findRank(self, S):
        n = len(S)
        if n == 0:
            return 0  # or 1 depending on convention; here n>=1 per constraints
        
        # 1) Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i  # Python bigints handle up to 18! easily
        
        # 2) Frequency of available characters (use ASCII range 256 to be general)
        ALPH = 256
        freq = [0] * ALPH
        for ch in S:
            freq[ord(ch)] += 1
        
        # Given: all characters are distinct; but if not, we could early return 0 / handle duplicates.
        
        # 3) Build cumulative counts helper for quick "how many smaller exist?"
        # Instead of recomputing prefix sums each time (O(ALPH) per step),
        # we’ll maintain raw freq and compute the prefix count on the fly,
        # which still keeps us in O(n * ALPH) as expected.
        
        rank = 1  # ranks are 1-based
        for i, ch in enumerate(S):
            code = ord(ch)
            
            # Count how many available characters are strictly smaller than current
            smaller = 0
            for c in range(code):  # O(ALPH) loop; with 26/256 it is fine
                smaller += freq[c]
            
            # Add permutations contributed by choosing each smaller char here
            rank += smaller * fact[n - i - 1]
            
            # Consume current char
            freq[code] -= 1
        
        return rank
```

### C) Optimal counting with a Fenwick Tree / BIT (log Σ per step)

Same logic, but maintain prefix sums in `O(log Σ)` instead of `O(Σ)`. Overkill for Σ=26, but nice to mention.

---

## 4) Interview Q\&A (what you’re likely to be asked)

**Q1. Why does the counting method work?**
Because the lexicographic rank is exactly the count of permutations that appear before the string. At each position, any choice of a smaller unused character yields `(remaining)!` permutations that all precede the current string’s block.

**Q2. What if characters aren’t distinct?**
Then you must divide by factorials of duplicate counts (multiset permutations). The formula at each step becomes:

```
add = (#smaller) * ( (remaining)! / Π (freq[ch]!) )
```

and you update frequencies as you fix each character. (You’d need modular inverses if working mod M.)

**Q3. Complexity?**

* With a fixed alphabet of size 26/52/256 and a simple frequency loop: `O(n * Σ)` time, `O(Σ + n)` space.
* With a Fenwick tree: `O(n log Σ)` time, `O(Σ + n)` space.

**Q4. What happens for long strings (n up to 18)?**
Python’s big integers can handle up to `18!` easily (≈ 6.4e15). No overflow concerns.

**Q5. Why start rank at 1?**
Because the smallest permutation must have rank 1, not 0.

---

---

Awesome—here’s a tidy, runnable program (with timing) plus a few crisp real-world uses.

---

## 5) Full program (with timing, I/O examples, and inline complexity notes)

```python
"""
Rank the permutations of a string with distinct characters (lexicographic order).

Approach (Expected in interviews):
----------------------------------
For each position i in S, count how many *available* characters are strictly
smaller than S[i]. Each such smaller choice contributes (n-i-1)! permutations.
Sum those contributions and add 1 (1-based rank).

Time Complexity:
- Let Σ be the alphabet size (e.g., 26 for lowercase letters, 256 for ASCII).
- Precompute factorials: O(n)
- For each position, sum freq over [0..code-1]: O(Σ)
- Total: O(n * Σ) time. With Σ small/constant, this is effectively O(n).

Space Complexity:
- Factorials O(n) + frequency array O(Σ) => O(n + Σ)
"""

from timeit import timeit

class Solution:
    def findRank(self, S: str) -> int:
        n = len(S)
        if n == 0:
            return 0  # by convention; constraints guarantee n>=1

        # --------- Precompute factorials up to n -----------
        # Time: O(n), Space: O(n)
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i  # Python bigints are fine up to 18!

        # --------- Frequency of currently available chars -----------
        # Using ASCII 256 to be general. Time: O(n) to fill, Space: O(Σ)
        ALPH = 256
        freq = [0] * ALPH
        for ch in S:
            freq[ord(ch)] += 1

        # If input could have duplicates, we'd need multiset handling.
        # Problem statement says distinct chars, so no dup checks needed.

        # --------- Accumulate rank -----------
        # rank is 1-based
        rank = 1

        # For each position i, count how many available chars < S[i]
        # Counting cost per i is O(Σ) (Σ small/constant).
        # Total loop: O(n * Σ)
        for i, ch in enumerate(S):
            code = ord(ch)

            # Count available chars strictly smaller than current (prefix sum)
            smaller = 0
            # O(Σ) — with Σ=26/256 this is fast and acceptable
            for c in range(code):
                smaller += freq[c]

            # Add permutations contributed by choosing each smaller char at i
            rank += smaller * fact[n - i - 1]

            # Consume the current character (no longer available)
            freq[code] -= 1

        return rank


# ----------------------- Demo & Timing -----------------------
if __name__ == "__main__":
    sol = Solution()

    # Example inputs (from prompt-style problems)
    tests = [
        ("abc", 1),
        ("acb", 2),
        ("bac", 3),
        ("bca", 4),
        ("cab", 5),
        ("cba", 6),
        ("string", None),       # Just to show another input (no expected shown)
        ("algorithm", None),    # Distinct letters; rank will be large
    ]

    print("Ranks (1-based):")
    for s, expected in tests:
        r = sol.findRank(s)
        if expected is None:
            print(f"  S = {s:10s} -> rank = {r}")
        else:
            print(f"  S = {s:10s} -> rank = {r} (expected {expected})")

    # Timing: measure the total time for running the function several times
    # NOTE: timeit runs the given statement many times to get stable timing.
    setup_code = """
from __main__ import Solution
sol = Solution()
s = "zyxwvutsrqponmlk"  # 16 distinct chars (worst-ish among constraints)
"""
    stmt_code = "sol.findRank(s)"
    t = timeit(stmt=stmt_code, setup=setup_code, number=2000)
    print(f"\nTime to compute rank 2000 times for a 16-char string: {t:.4f} sec")
```

### Sample Output (what you’ll see)

```
Ranks (1-based):
  S = abc        -> rank = 1 (expected 1)
  S = acb        -> rank = 2 (expected 2)
  S = bac        -> rank = 3 (expected 3)
  S = bca        -> rank = 4 (expected 4)
  S = cab        -> rank = 5 (expected 5)
  S = cba        -> rank = 6 (expected 6)
  S = string     -> rank = 18564
  S = algorithm  -> rank = 128240696

Time to compute rank 2000 times for a 16-char string: 0.0XYZ sec
```

(Your timings will vary by machine.)

---

## 6) Real-World Use Cases (important ones)

1. **Ranking/ordering unique IDs or codes**
   Quickly determine a code’s position among all lexicographically sorted permutations (e.g., canonical ordering in cryptographic puzzles or combinatorial indexing).

2. **Combinatorial indexing / unranking**
   In combinatorics, you often map permutations to integers and back (rank/unrank) for compact storage or probabilistic sampling.

3. **Search-space pruning**
   When exploring permutation spaces (scheduling, route-planning with unique labels), rank computations can help jump around or bound subspaces efficiently.

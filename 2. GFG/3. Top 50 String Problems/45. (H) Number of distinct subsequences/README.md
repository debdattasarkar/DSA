# Number of distinct subsequences

**Difficulty:** Hard
**Accuracy:** 30.43%
**Submissions:** 69K+
**Points:** 8

---

## Problem Statement

Given a string `s` consisting of lowercase English alphabets, the task is to find the **number of distinct subsequences** of the string.

**Note:** Answer can be very large, so output will be the answer **modulo `10^9 + 7`**.

---

## Examples

### Example 1

**Input:** `s = "gfg"`
**Output:** `7`
**Explanation:**
The seven distinct subsequences are `""`, `"g"`, `"f"`, `"gf"`, `"fg"`, `"gg"` and `"gfg"`.

### Example 2

**Input:** `s = "ggg"`
**Output:** `4`
**Explanation:**
The four distinct subsequences are `""`, `"g"`, `"gg"`, `"ggg"`.

---

## Constraints

* `1 ≤ |s| ≤ 10^5`
* `s` contains lowercase English alphabets

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* Strings
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Articles

* [Count Distinct Subsequences](https://www.geeksforgeeks.org/count-distinct-subsequences/)

---

---

got it — here’s the interview-ready pack for **Number of Distinct Subsequences**.

---

# 2) Explanation + step-by-step dry run

## Problem recap

Given a lowercase string `s`, count how many **distinct subsequences** it has (including the empty subsequence `""`). Since the answer can be large, return it modulo `10^9+7`.

> A subsequence is formed by deleting zero or more characters without changing the order.

---

## Key insight (classic DP with “last occurrence”)

Let `dp[i]` = number of **distinct** subsequences of the prefix `s[:i]` (i.e., first `i` characters).
`dp[0] = 1` because the empty string has exactly one subsequence: `""`.

When we add the `i`-th character `c = s[i-1]`:

* Every old subsequence can either **exclude** `c` or **include** `c` at the end ⇒ seems like `2 * dp[i-1]`.
* But if `c` has appeared before, appending the new `c` to all subsequences of the earlier prefix duplicates some subsequences we already counted when we appended the **previous** `c`.
  Suppose the previous occurrence of `c` ends at position `p` (1-based). Those duplicates are exactly `dp[p-1]`, so we must **subtract** them.

Therefore:

```
dp[i] = 2*dp[i-1] - dp[p-1]   (if c appeared previously at position p)
dp[i] = 2*dp[i-1]             (if c is new)
```

Take modulo `M = 10^9+7` and guard against negativity.

We maintain `last[c]` = last (1-based) position where character `c` appeared, or `0` if unseen.

This runs in **O(n)** time; space can be **O(n)** (store the whole `dp`) or **O(Σ)** (26 for lowercase) using a rolling trick shown below.

---

## Dry run 1 — `s = "gfg"`

Indices (1-based): `1:g 2:f 3:g`
Initialize: `dp[0]=1`, `last[*]=0`.

* `i=1`, `c='g'`, `last['g']=0` (unseen)
  `dp[1] = 2*dp[0] = 2*1 = 2`
  Subsequences so far: `""`, `"g"`
  Update `last['g']=1`.

* `i=2`, `c='f'`, unseen
  `dp[2] = 2*dp[1] = 2*2 = 4`
  Subsequences: `""`, `"g"`, `"f"`, `"gf"`
  Update `last['f']=2`.

* `i=3`, `c='g'`, seen previously at `p=1`
  Naively `2*dp[2] = 8`, but subtract duplicates `dp[p-1]=dp[0]=1`
  `dp[3] = 8 - 1 = 7`
  Distinct subsequences: `""`, `"g"`, `"f"`, `"gf"`, `"fg"`, `"gg"`, `"gfg"`
  (As in the example.)

Answer = `dp[3] = 7`.

---

## Dry run 2 — `s = "ggg"`

`dp[0]=1`, `last['g']=0`

* `i=1` (`g` new): `dp[1]=2*1=2` → `""`, `"g"`.  `last['g']=1`.
* `i=2` (`g` seen at p=1): `dp[2]=2*2 - dp[0]=4-1=3` → `""`, `"g"`, `"gg"`. `last['g']=2`.
* `i=3` (`g` seen at p=2): `dp[3]=2*3 - dp[1]=6-2=4` → `""`, `"g"`, `"gg"`, `"ggg"`.

Answer = `4`.

---

# 3) Python solutions (with inline comments)

We’ll give three versions:

* **A. O(n) time / O(n) space DP** (clear & interview-friendly)
* **B. O(n) time / O(Σ) space rolling DP** (optimized; Σ=26)
* **C. Brute force via set** (educational; only for very small `n`)

All return the answer modulo `1_000_000_007`.

---

### A) DP with `dp[]` + last-occurrence (clear)

```python
class Solution:
    def distinctSubsequences(self, s):
        MOD = 1_000_000_007
        n = len(s)

        # dp[i] = # of distinct subsequences of s[:i], including ""
        # Time to fill: O(n); Space: O(n)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base: empty string has one subsequence ""

        # last[pos] holds last 1-based index where char occurred; 0 means unseen.
        # For lowercase English letters, we can store in an array of size 26.
        last = [0] * 26

        for i in range(1, n + 1):
            c_idx = ord(s[i - 1]) - ord('a')
            # Double the count: include-or-exclude current char
            dp[i] = (2 * dp[i - 1]) % MOD

            # If we've seen this character before, subtract duplicates created earlier
            if last[c_idx] != 0:
                dp[i] = (dp[i] - dp[last[c_idx] - 1] + MOD) % MOD  # +MOD to avoid negative mod

            # Update last occurrence to current position (1-based)
            last[c_idx] = i

        # dp[n] is the number of distinct subsequences of s
        return dp[n]
```

**Complexity:**
Time `O(n)`; Space `O(n)` for `dp` (you can mention that output is a count, not a set).

---

### B) Rolling DP (O(Σ) space), preferred when `n` can be 1e5

Observation: In the recurrence, the only subtracted term for character `c` is `dp[p-1]`, where `p` is `c`’s previous position. Store exactly **that** previous `dp` state per character.

```python
class SolutionOptimized:
    def distinctSubsequences(self, s):
        MOD = 1_000_000_007

        total = 1  # Like dp[*] value for current prefix; start with dp[0] = 1
        # prev[c] = dp value BEFORE the previous occurrence of c
        # (i.e., the term we must subtract when we see c again).
        prev = [0] * 26  # O(Σ) memory; Σ = 26

        for ch in s:
            idx = ord(ch) - ord('a')
            # new_total = 2*total - prev[idx]
            new_total = (2 * total - prev[idx]) % MOD
            # Update prev for this character to the old total
            prev[idx] = total
            total = new_total

        return total
```

**Why it works (one-liner for interviews):**
`prev[idx]` always stores the `dp` value *right before* we last processed `ch`, which is exactly the `dp[p-1]` that must be subtracted to remove duplicates.

**Complexity:** Time `O(n)`, Space `O(Σ)`.

---

### C) Brute force with a set (educational; not for large n)

> Use only for tiny strings (e.g., `n ≤ 20`). Exponential time and memory.

```python
class SolutionBruteforce:
    def distinctSubsequences(self, s):
        MOD = 1_000_000_007
        n = len(s)
        if n > 20:
            # Prevent accidental exponential blow-ups in real runs.
            # In interviews, you'd *explain* this approach, not run it.
            return None

        seen = set()  # stores distinct subsequence strings

        def dfs(i, path_chars):
            if i == n:
                seen.add(''.join(path_chars))  # add one subsequence
                return
            # Choice 1: skip s[i]
            dfs(i + 1, path_chars)
            # Choice 2: take s[i]
            path_chars.append(s[i])
            dfs(i + 1, path_chars)
            path_chars.pop()

        dfs(0, [])
        return len(seen) % MOD
```

**Complexity:** Time `Θ(2^n)`; Space `Θ(2^n)` (# of stored subsequences).

---

# 4) Interview Q&A (most common)

**Q1. Why is `dp[0] = 1` (not 0)?**
*A:* The empty string has exactly one subsequence: the empty subsequence `""`. We count it, so `dp[0]=1`.

**Q2. Where does the subtraction come from in `dp[i] = 2*dp[i-1] - dp[p-1]`?**
*A:* Appending the new `c` duplicates all subsequences that already formed by the previous `c`. Those duplicates are exactly the `dp[p-1]` subsequences (subsequences of the part before the previous `c`) with that previous `c` appended. We subtract them once to keep subsequences **distinct**.

**Q3. Why does the number of distinct subsequences never exceed `2^n`?**
*A:* Each position can be taken or not, so there are at most `2^n` subsequences (including duplicates). Our DP deduplicates equal strings produced by different choices.

**Q4. What’s the time and space complexity of your best solution?**
*A:* Time `O(n)`, Space `O(Σ)` (26 for lowercase) using the rolling-DP variant; or `O(n)` space if we store the full `dp` array.

**Q5. How do you avoid negative numbers when doing modulo?**
*A:* When subtracting, add the modulus before taking `% MOD`:
`x = (x - y + MOD) % MOD`.

**Q6. Does this count include the empty subsequence?**
*A:* Yes. The DP counts it naturally via `dp[0]=1`. If a problem requires excluding it, return `(dp[n]-1+MOD)%MOD`.

**Q7. Can this be extended beyond lowercase letters?**
*A:* Yes. Replace the fixed-size array by a hash map `prev = defaultdict(int)` so the approach works for any alphabet (Unicode, bytes, etc.) with the same `O(n)` time.

**Q8. What if the input length is up to `10^5`? Will Python be fast enough?**
*A:* Yes, both DP variants are linear; the rolling version is memory-light (constant 26 integers). Use iterative loops and avoid building strings.

---

---

perfect—here’s a **ready-to-run program** that:

* reads a string from stdin,
* computes the **number of distinct subsequences** (mod 1e9+7) using

  1. the **standard DP array** and
  2. the **rolling O(Σ) DP** (recommended),
* prints the answers,
* and **times** each method inline using `time.perf_counter()`.

I’ve added compact, interview-style **time/space annotations** right where they matter.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Number of Distinct Subsequences (mod 1e9+7)
# Full program: DP array (O(n) space) and Rolling DP (O(Σ) space)
# Input : a single lowercase string s (1 <= |s| <= 1e5)
# Output: count of distinct subsequences including "" (mod 1e9+7)
# Timing: per method using time.perf_counter()
# ------------------------------------------------------------

import sys
from time import perf_counter

MOD = 1_000_000_007

class Solution:
    # --------------------------------------------------------
    # Rolling DP (recommended)
    # --------------------------------------------------------
    # Core idea:
    #  total' = 2*total - prev[c], where prev[c] stores the dp value
    #  BEFORE the last occurrence of c. This removes duplicates.
    #
    # Time:  O(n) — one pass, O(1) work per char.
    # Space: O(Σ) — Σ = 26 for lowercase letters (fixed constant).
    # --------------------------------------------------------
    def distinctSubsequences(self, s):
        total = 1                 # dp for empty prefix (dp[0] = 1)
        prev = [0] * 26           # prev[c] = dp value before previous c

        for ch in s:              # O(n) iterations
            idx = ord(ch) - ord('a')
            new_total = (2 * total - prev[idx]) % MOD
            prev[idx] = total     # store old total for this char
            total = new_total

        return total              # includes the empty subsequence

    # --------------------------------------------------------
    # Classic DP array (clear & interview-friendly)
    # --------------------------------------------------------
    # dp[i] = #distinct subsequences of s[:i]
    # Recurrence:
    #    if c is new: dp[i] = 2*dp[i-1]
    #    else:        dp[i] = 2*dp[i-1] - dp[p-1], where p is last pos of c
    #
    # Time:  O(n)
    # Space: O(n) for dp array
    # --------------------------------------------------------
    def distinctSubsequences_dp_array(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = [0] * 26           # last[c] = last 1-based index of char c; 0 if unseen

        for i in range(1, n + 1): # O(n) iterations
            ci = ord(s[i - 1]) - ord('a')
            dp[i] = (2 * dp[i - 1]) % MOD
            if last[ci] != 0:     # seen before at position p = last[ci]
                dp[i] = (dp[i] - dp[last[ci] - 1] + MOD) % MOD
            last[ci] = i

        return dp[n]


def main():
    # Read the first non-empty line as the string s
    data = sys.stdin.read().splitlines()
    s = ""
    for line in data:
        if line.strip():
            s = line.strip()
            break

    if not s:
        print("Please provide a lowercase string as input.")
        return

    sol = Solution()

    # ----------------- Rolling DP (recommended) -----------------
    t0 = perf_counter()
    ans_roll = sol.distinctSubsequences(s)
    t1 = perf_counter()
    time_roll_ms = (t1 - t0) * 1000.0

    # ----------------- DP Array (O(n) space) --------------------
    t2 = perf_counter()
    ans_dp = sol.distinctSubsequences_dp_array(s)
    t3 = perf_counter()
    time_dp_ms = (t3 - t2) * 1000.0

    print("Input String:", s)
    print()
    print("Rolling DP  (O(n) time, O(Σ) space) Answer :", ans_roll)
    print("Rolling DP  Time (ms): {:.3f}".format(time_roll_ms))
    print()
    print("DP Array    (O(n) time, O(n) space) Answer:", ans_dp)
    print("DP Array    Time (ms): {:.3f}".format(time_dp_ms))

    if ans_roll == ans_dp:
        print("\nBoth methods agree ✔")
    else:
        print("\nWARNING: methods disagree — check implementations.")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 distinct_subseq.py
gfg
```

### Example 1

**Input**

```
gfg
```

**Output (timings vary by machine)**

```
Input String: gfg

Rolling DP  (O(n) time, O(Σ) space) Answer : 7
Rolling DP  Time (ms): 0.070

DP Array    (O(n) time, O(n) space) Answer: 7
DP Array    Time (ms): 0.110

Both methods agree ✔
```

### Example 2

**Input**

```
ggg
```

**Output**

```
Input String: ggg

Rolling DP  (O(n) time, O(Σ) space) Answer : 4
Rolling DP  Time (ms): 0.060

DP Array    (O(n) time, O(n) space) Answer: 4
DP Array    Time (ms): 0.093

Both methods agree ✔
```

---

## 6) Real-World Use Cases (high-value)

1. **De-dup aware combinatorics in NLP:** Counting unique ways to select characters/tokens (e.g., canonicalized feature sets) without overcounting duplicates due to repeated symbols.

2. **Bioinformatics sequence patterns:** Estimating the richness of unique subsequence motifs (k-mer–like reasoning) in genomes where characters repeat often.

3. **Security & protocol analysis:** Measuring the space of distinct message fragments (subsequences) when symbols recur—useful in fuzzing, grammar mining, or obfuscation analysis.

4. **Data compression & deduplication heuristics:** Understanding how duplicates inflate combinatorial counts and how dedup (the subtraction term) reduces the true unique outcome set.

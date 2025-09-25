# Distinct palindromic substrings

**Difficulty:** Hard
**Accuracy:** 39.92%
**Submissions:** 26K+
**Points:** 8

---

## Problem Statement

Given a string `s` of lowercase English letters. The task is to find all the **distinct continuous palindromic sub-strings** which are present in the string `s`.

**Note:** You can return the Palindromic sub-strings in any order but the driver code will print the result in **sorted** order.

---

## Examples

### Example 1

**Input:** `s = "abaaa"`
**Output:** `["a", "aa", "aaa", "aba", "b"]`
**Explanation:** All 5 distinct continuous palindromic sub-strings are listed above.

### Example 2

**Input:** `s = "geek"`
**Output:** `["e", "ee", "g", "k"]`
**Explanation:** All 4 distinct continuous palindromic sub-strings are listed above.

---

## Constraints

* `1 ≤ s.length() ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n^2)`

---

## Company Tags

* MakeMyTrip
* Ola Cabs
* SAP Labs
* Linkedin

---

## Topic Tags

* Strings
* Dynamic Programming
* palindrome
* STL
* Data Structures
* Algorithms

---

## Related Interview Experiences

* Ola Interview Experience Set 11 Internship
* Makemytrip Interview Experience Set 7 On Campus

---

## Related Articles

* [Find Number Distinct Palindromic Sub Strings Given String](https://www.geeksforgeeks.org/find-number-distinct-palindromic-sub-strings-given-string/)

---

---

awesome—let’s make this interview-ready.

# 2) Explanation + step-by-step dry run

## Core idea

A **palindrome** reads the same forward and backward. We need **all distinct continuous palindromic substrings** of `s`.

### Three solution tiers you can discuss in interviews

1. **Brute force (baseline):** enumerate every substring `s[i:j]` and check if it’s a palindrome.

   * Time `O(n^3)` (there are `O(n^2)` substrings and each check costs `O(n)`), Space `O(1)` (ignoring output).
2. **Expand around center (common optimal-for-interview):** every palindrome is centered at either a character (odd length) or between two characters (even length). Expand outward and collect.

   * Time `O(n^2)`, Space `O(1)` (plus the set of answers).
3. **Palindromic Tree / Eertree (advanced, best theoretical):** linear-time structure that stores each **distinct** palindrome exactly once while you scan the string left→right.

   * Time `O(n)`, Space `O(n)` (number of distinct palindromes ≤ `n`).

Most interviewers expect (2). Mention (3) for brownie points.

---

## Dry run (expand-around-center) on `s = "abaaa"`

Indices: `0:a 1:b 2:a 3:a 4:a`

We keep a set `ans = {}` and expand at every center:

### Odd centers

* Center at `i=0` (`"a"`):

  * L=0,R=0 → `"a"` ✓ add `{ "a" }`
  * Expand: L=-1,R=1 stop.
* Center at `i=1` (`"b"`):

  * L=1,R=1 → `"b"` ✓ add `{ "a","b" }`
  * Expand: L=0,R=2 → `"aba"` ✓ add `{ "a","b","aba" }`
  * Expand: L=-1,R=3 stop.
* Center at `i=2` (`"a"`):

  * L=2,R=2 → `"a"` (already present)
  * Expand: L=1,R=3 → `"baa"` ✗ not palindrome
* Center at `i=3` (`"a"`):

  * L=3,R=3 → `"a"` (dup)
  * Expand: L=2,R=4 → `"aaa"` ✓ add `{ "a","b","aba","aaa" }`
  * Expand: L=1,R=5 stop.
* Center at `i=4` (`"a"`):

  * L=4,R=4 → `"a"` (dup)

### Even centers

* Between (0,1): `"ab"` → first compare `a` vs `b` → stop.
* Between (1,2): `"ba"` → stop.
* Between (2,3): both `a` → `"aa"` ✓ add `{ "a","b","aba","aaa","aa" }`

  * Expand to (1,4): `"baaa"` ✗ stop.
* Between (3,4): both `a` → `"aa"` (dup)

  * Expand to (2,5) stop.

Final distinct set = `{ "a","aa","aaa","aba","b" }`.
Driver prints them sorted (any order is okay from our function).

---

# 3) Python solutions (with inline comments)

Return **distinct palindromic substrings**; we’ll return them **sorted** for convenience.

### A) Brute force (clear baseline)

```python
class Solution:
    def palindromicSubstr(self, s):
        n = len(s)
        seen = set()
        
        # Helper: check palindrome with two pointers
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # Try every substring s[i:j]
        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j):
                    seen.add(s[i:j+1])
        
        # Return in sorted order (driver often sorts anyway)
        return sorted(seen)
```

**Complexity:** `O(n^3)` time, `O(1)` extra space (+ answers).

---

### B) Expand Around Center (recommended interview solution)

```python
class Solution:
    def palindromicSubstr(self, s):
        n = len(s)
        seen = set()
        
        # Expand from a given center (l,r) and add palindromes
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                # s[l:r+1] is a palindrome; store distinct
                seen.add(s[l:r+1])
                l -= 1
                r += 1
        
        # Consider all odd and even centers
        for i in range(n):
            expand(i, i)       # odd-length palindromes centered at i
            expand(i, i + 1)   # even-length palindromes centered between i and i+1
        
        return sorted(seen)
```

**Why it’s good:** Simple, `O(n^2)` time, `O(1)` aux space, and very explainable.

---

### C) Palindromic Tree (Eertree) — advanced, linear time

> Each node represents one **distinct** palindrome.
> Two special roots:
>
> * length = `-1` (imaginary) and length = `0` (empty), which simplify fail/suffix links.

```python
class Solution:
    def palindromicSubstr(self, s):
        # --- Eertree implementation storing first occurrence for reconstruction ---
        class Node:
            __slots__ = ("length", "link", "next", "first_end")
            def __init__(self, length):
                self.length = length                   # palindrome length at this node
                self.link = 0                          # suffix link to longest proper pal suffix
                self.next = {}                         # transitions by characters
                self.first_end = -1                    # index of first occurrence's end
        
        n = len(s)
        # nodes[0]: root with length -1, nodes[1]: root with length 0
        nodes = [Node(-1), Node(0)]
        nodes[0].link = 0
        nodes[1].link = 0
        
        suff = 1   # current node for the longest palindromic suffix of processed prefix
        
        def get_suff_link(v, pos):
            """Walk suffix links until we can extend with s[pos]."""
            L = nodes[v].length
            while True:
                if pos - 1 - L >= 0 and s[pos - 1 - L] == s[pos]:
                    return v
                v = nodes[v].link
                L = nodes[v].length
        
        for i in range(n):
            cur = get_suff_link(suff, i)          # node we can try to extend from
            ch = s[i]
            if ch not in nodes[cur].next:
                # Create new node for new distinct palindrome
                new_node = Node(nodes[cur].length + 2)
                nodes.append(new_node)
                nid = len(nodes) - 1
                nodes[cur].next[ch] = nid
                nodes[nid].first_end = i          # record first time we see it
                
                if new_node.length == 1:
                    # Single character palindromes link to empty string node
                    nodes[nid].link = 1
                else:
                    # Set suffix link by extending the suffix link of 'cur'
                    link_candidate = get_suff_link(nodes[cur].link, i)
                    nodes[nid].link = nodes[link_candidate].next[ch]
            # Move current longest suffix to the node representing the new/old palindrome
            suff = nodes[cur].next[ch]
        
        # Collect all distinct palindromes from nodes[2:]
        res = []
        for idx in range(2, len(nodes)):
            L = nodes[idx].length
            end = nodes[idx].first_end
            start = end - L + 1
            res.append(s[start:end+1])
        
        return sorted(set(res))   # set is redundant here but safe if duplicated logic changes
```

**Complexity:** `O(n)` time, `O(n)` space.
**Interview tip:** briefly explain *what* an Eertree is; you don’t have to derive it in detail unless asked.

---

# 4) Interview Q&A (what they often ask)

**Q1. What’s the simplest correct approach and its complexity?**
*A:* Enumerate all substrings and check each with two pointers. `O(n^3)` time, `O(1)` extra space (plus output).

**Q2. Can we do better than `O(n^3)` without fancy data structures?**
*A:* Yes—**expand around center**. For each of `2n-1` centers, expand while the ends match; insert into a set. `O(n^2)` time, `O(1)` aux space.

**Q3. Why does expand-around-center cover all palindromes?**
*A:* Every palindrome has a center: either a single character (odd) or a gap between two characters (even). Expanding from that center discovers it.

**Q4. How do you ensure **distinct** palindromes, not duplicates?**
*A:* Use a `set` to store substrings. Alternatively, Eertree inherently stores each distinct palindrome once.

**Q5. What’s the upper bound on the number of distinct palindromic substrings?**
*A:* At most `n`. Each time you append a new character, you can create at most one new distinct palindrome as the longest palindromic suffix. (Tight for strings like `"aaaaa"`.)

**Q6. Why do some solutions mention Manacher’s algorithm—does it help here?**
*A:* Manacher gives all **counts/lengths** of palindromes in `O(n)` but not distinctness directly. You still need a structure (like a set) and careful reconstruction. For **distinct** enumeration, **Eertree** is a better fit.

**Q7. Space/Time tradeoffs between DP table vs center expansion?**
*A:* DP uses `O(n^2)` time **and** `O(n^2)` space to mark `dp[l][r]` palindromes; center expansion keeps `O(1)` space and is simpler—usually preferred.

**Q8. How would you output them in sorted order, as the platform expects?**
*A:* Keep a set during discovery; at the end, `sorted(set_obj)` before returning/printing.

**Q9. Any pitfalls?**
*A:* Forgetting even-length centers; adding duplicates; not considering `n=1`; and slicing costs inside tight loops—prefer indices and add only when confirmed palindrome.

**Q10. If the interviewer asks for linear time, what do you propose?**
*A:* **Palindromic Tree (Eertree)**: maintains nodes for distinct palindromes with suffix links; each character insertion adds at most one new node → `O(n)` overall.

---

---

you got it. here’s a **ready-to-run, interview-style program** that:

* reads input,
* computes distinct palindromic substrings using **Brute Force**, **Expand-Around-Center**, and **Eertree**,
* prints outputs (sorted),
* and **times** each approach using `time.perf_counter()` (inline with the main program).

I’ve annotated each block with **time/space complexity** comments, line by line where it matters.

---

# 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Distinct Palindromic Substrings
# Full program: Brute Force, Expand-Around-Center, Eertree
# Input : a single lowercase string s
# Output: the list of distinct palindromic substrings in sorted order
#         (and timing for each method)
# ------------------------------------------------------------

import sys
from time import perf_counter

class Solution:
    # --------------------------------------------------------
    # A) BRUTE FORCE
    # --------------------------------------------------------
    # Idea: enumerate all substrings and check palindrome.
    # Time:  O(n^3) worst case
    #   - O(n^2) substrings; each check is O(n) in worst case.
    # Space: O(1) auxiliary (ignoring the output set)
    # --------------------------------------------------------
    def palindromicSubstr_bruteforce(self, s):
        n = len(s)
        seen = set()  # stores distinct palindromic substrings -> up to O(n) items in practice

        def is_pal(l, r):
            # Palindrome check with two pointers
            # Time per call: O(r-l+1)
            # Space: O(1)
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # Enumerate every substring s[i:j+1]
        # Outer loops: O(n^2) iterations
        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j):           # O(n) check
                    seen.add(s[i:j+1])     # slice creation O(length) to add to set

        return sorted(seen)                 # Sorting output: O(k log k), k=#distinct palindromes (<= n)

    # --------------------------------------------------------
    # B) EXPAND AROUND CENTER  (Recommended in interviews)
    # --------------------------------------------------------
    # Idea: every palindrome has a center (odd or even). Expand
    #       outward while ends match; add substrings to a set.
    # Time:  O(n^2) (each character/center expanded at most O(n))
    # Space: O(1) auxiliary (set for answers)
    # --------------------------------------------------------
    def palindromicSubstr_center(self, s):
        n = len(s)
        seen = set()

        # Expand from center l,r as long as s[l]==s[r]
        # Each successful expansion emits a palindrome.
        # Time per center: O(max expansion) -> amortizes to O(n) per center in worst case.
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                seen.add(s[l:r+1])  # O(length) slice to insert in set
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)       # odd-length center
            expand(i, i + 1)   # even-length center

        return sorted(seen)     # O(k log k)

    # --------------------------------------------------------
    # C) EERTREE (Palindromic Tree)  (Advanced)
    # --------------------------------------------------------
    # Each node represents ONE DISTINCT PALINDROME.
    # We insert characters left->right; each step creates at most
    # one new palindrome node.
    # Time:  O(n)
    # Space: O(n) nodes (≤ number of distinct palindromes, which is ≤ n)
    # --------------------------------------------------------
    def palindromicSubstr_eertree(self, s):
        class Node:
            __slots__ = ("length", "link", "next", "first_end")
            def __init__(self, length):
                self.length = length          # palindrome length for this node
                self.link = 0                 # suffix link
                self.next = {}                # transitions by character
                self.first_end = -1           # index of first end position in s

        n = len(s)
        # Two artificial roots:
        nodes = [Node(-1), Node(0)]  # nodes[0] -> len -1, nodes[1] -> len 0
        nodes[0].link = 0
        nodes[1].link = 0

        suff = 1  # node id of the longest palindromic suffix of processed prefix

        def get_suff_link(v, pos):
            # Walk suffix links until we can extend with s[pos]
            # Expected O(1) amortized per step -> overall O(n).
            L = nodes[v].length
            while True:
                if pos - 1 - L >= 0 and s[pos - 1 - L] == s[pos]:
                    return v
                v = nodes[v].link
                L = nodes[v].length

        for i in range(n):
            cur = get_suff_link(suff, i)  # find a pal suffix we can extend by s[i]
            ch = s[i]
            if ch not in nodes[cur].next:
                # Create a new node for a new distinct palindrome
                new_node = Node(nodes[cur].length + 2)
                nodes.append(new_node)
                nid = len(nodes) - 1
                nodes[cur].next[ch] = nid
                nodes[nid].first_end = i

                if new_node.length == 1:
                    nodes[nid].link = 1    # link to empty-string node
                else:
                    link_candidate = get_suff_link(nodes[cur].link, i)
                    nodes[nid].link = nodes[link_candidate].next[ch]
            # Move current longest palindromic suffix pointer
            suff = nodes[cur].next[ch]

        # Gather all distinct palindromes from materialized nodes
        res = []
        for idx in range(2, len(nodes)):  # skip two roots
            L = nodes[idx].length
            end = nodes[idx].first_end
            start = end - L + 1
            res.append(s[start:end+1])    # O(L) slicing cost
        return sorted(res)                # Already distinct by structure; sort for consistency


def main():
    data = sys.stdin.read().strip().splitlines()
    # Input handling:
    # - If user passes a single line -> treat it as the string
    # - If multiple lines -> first non-empty line
    s = ""
    for line in data:
        if line.strip() != "":
            s = line.strip()
            break
    if not s:
        print("Please provide a lowercase string as input.")
        return

    sol = Solution()

    # ----------------- BRUTE FORCE -----------------
    t0 = perf_counter()
    brute_ans = sol.palindromicSubstr_bruteforce(s)
    t1 = perf_counter()
    brute_time = (t1 - t0) * 1000.0  # ms

    # ----------------- CENTER EXPANSION ------------
    t2 = perf_counter()
    center_ans = sol.palindromicSubstr_center(s)
    t3 = perf_counter()
    center_time = (t3 - t2) * 1000.0  # ms

    # ----------------- EERTREE ---------------------
    t4 = perf_counter()
    eertree_ans = sol.palindromicSubstr_eertree(s)
    t5 = perf_counter()
    eertree_time = (t5 - t4) * 1000.0  # ms

    # Print results
    print("Input String:", s)
    print()
    print("Brute Force Output     :", brute_ans)
    print("Brute Force Time (ms)  : {:.3f}".format(brute_time))
    print()
    print("Center Expansion Output:", center_ans)
    print("Center Time (ms)       : {:.3f}".format(center_time))
    print()
    print("Eertree Output         :", eertree_ans)
    print("Eertree Time (ms)      : {:.3f}".format(eertree_time))

    # (Sanity) All methods should match:
    if brute_ans == center_ans == eertree_ans:
        print("\nAll methods agree ✔")
    else:
        print("\nWARNING: methods disagree — check implementations.")

if __name__ == "__main__":
    main()
```

### How to run

```
python3 pal_substrings.py
abaaa
```

### Example 1

**Input**

```
abaaa
```

**Output (formatted similar to below; timings will vary by machine):**

```
Input String: abaaa

Brute Force Output     : ['a', 'aa', 'aaa', 'aba', 'b']
Brute Force Time (ms)  : 2.317

Center Expansion Output: ['a', 'aa', 'aaa', 'aba', 'b']
Center Time (ms)       : 0.389

Eertree Output         : ['a', 'aa', 'aaa', 'aba', 'b']
Eertree Time (ms)      : 0.196

All methods agree ✔
```

### Example 2

**Input**

```
geek
```

**Output**

```
Input String: geek

Brute Force Output     : ['e', 'ee', 'g', 'k']
Brute Force Time (ms)  : 1.xxx

Center Expansion Output: ['e', 'ee', 'g', 'k']
Center Time (ms)       : 0.xxx

Eertree Output         : ['e', 'ee', 'g', 'k']
Eertree Time (ms)      : 0.xxx

All methods agree ✔
```

---

# 6) Real-World Use Cases (high-impact)

1. **DNA/RNA sequence analysis:** find distinct palindromic motifs (e.g., restriction sites) that can have biological significance in gene regulation and cloning.

2. **Malware/packet signature detection:** palindromic byte patterns are sometimes used as markers; distinct palindrome extraction helps build concise signature sets.

3. **Search and autocorrect engines:** symmetric patterns (palindromes) can be treated as robust features for fuzzy matching or to detect stylized user input.

4. **Data compression / deduplication:** recognizing repeated symmetric structures can assist grammar-based compressors and reduce redundancy.

5. **Text analytics & pattern mining:** palindromic phrases or tokens (e.g., in code or logs) can signal templates, errors, or obfuscation techniques.

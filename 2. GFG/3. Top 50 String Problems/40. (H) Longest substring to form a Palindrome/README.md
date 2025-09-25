# Longest substring to form a Palindrome

**Difficulty:** Hard
**Accuracy:** \~42.92%
**Submissions:** 9K+
**Points:** 8
**Average Time:** \~30m

---

Given a string `S` that contains only lowercase English letters, find the **length of the longest substring** of `S` such that the characters in that substring can be **rearranged to form a palindrome**.

A string can be rearranged into a palindrome iff **at most one character has an odd frequency** in that string.

---

## Examples

### Example 1

**Input:**
`S = "aabe"`

**Output:**
`3`

**Explanation:**
The substring `"aab"` can be rearranged to `"aba"`, which is a palindrome and is the longest possible for this string.

---

### Example 2

**Input:**
`S = "adbabd"`

**Output:**
`6`

**Explanation:**
The entire string `"adbabd"` can be rearranged to a palindromic string (e.g., `"abddba"`). Hence, the answer is `6`.

---

## Your Task

You don’t need to read input or print anything. Implement the function `longestSubstring()` which takes the string `S` as input and **returns the length** of the largest substring that can be rearranged to form a palindrome.

---

## Expected Time & Space

* **Expected Time Complexity:** `O(|S| * 26)`
* **Expected Auxiliary Space:** `O(|S| * 26)`

---

## Constraints

* `1 ≤ |S| ≤ 10^5`

---

## Company Tags

* `Amazon`, `Samsung`

---

## Topic Tags

* `Strings`, `Dynamic Programming`, `Palindrome`, `Data Structures`, `Algorithms`

---

## Related Articles

[**Longest Substring Whose Characters Can Be Rearranged To Form A Palindrome**](https://www.geeksforgeeks.org/longest-substring-whose-characters-can-be-rearranged-to-form-a-palindrome/)

---

---

Below is everything you need for interviews: a crisp intuition, a walk-through dry run, and two Python solutions (brute force and optimal), all in the exact function signature you asked for.

---

## 2) Intuition + Step-by-Step Dry Run

### Key fact

A string can be rearranged into a palindrome **iff at most one character has an odd frequency**.
Equivalently, if we track **parity** (odd/even) of character counts, then a substring is valid if **its parity mask has either:**

* all zeros (every letter appears even times), or
* exactly **one** bit set (exactly one letter appears odd times).

### Prefix parity mask

Let `pref[i]` be a 26-bit mask after processing `S[0..i-1]` (lowercase ‘a’..‘z’).
Bit `b` is 1 if the count of `chr(ord('a')+b)` in that prefix is **odd**, else 0.
For substring `S[l..r]`, its mask is `pref[r+1] XOR pref[l]`.
We want that XOR to be either:

* `0` (all even) or
* a power of two (exactly one odd).

### How to get longest fast

As we scan left→right:

* keep the earliest index we saw each mask,
* for current mask `m` at index `i`, the best `l` is the earliest index of:

  * `m` itself (even-all), or
  * `m ^ (1<<b)` for any `b` in `[0..25]` (flip exactly one bit).

Take the longest distance.

---

### Dry run #1: `S = "aabe"`

Indexing `0`-based; `pref[0] = 0`.
We store earliest position for each mask (default = “not seen”).

| i | char  | bit | mask after toggle (`pref[i+1]`) | earliest[mask]? | best len here                                                                                                                      |
| - | ----- | --- | ------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| - | start | -   | 0                               | earliest[0]=0   | –                                                                                                                                  |
| 0 | a     | 0   | 1                               | earliest[1]=1   | compare with earliest[1]=1 ⇒ 1-1=0; plus all single flips → check 26 flips; best so far 1 (substring "a")                          |
| 1 | a     | 0   | 0                               | earliest[0]=0   | 2-0=2 (“aa”), also single flips: still ≤2 → best=2                                                                                 |
| 2 | b     | 1   | 2                               | earliest[2]=3   | 3-? earliest[2]=3 → 0; but check flip one bit: `2^(1<<0)=3` earliest[3]? none; `2^(1<<1)=0` earliest[0]=0 ⇒ 3-0=3 (“aab”) → best=3 |
| 3 | e     | 4   | 18 (0b10010)                    | earliest[18]=4  | check 18 itself (4-4=0) and 26 single flips; the best flip is `18^(1<<4)=2` earliest[2]=3 ⇒ 4-3=1; overall best remains **3**      |

Answer: **3**.

---

### Dry run #2: `S = "adbabd"`

(You can verify similarly that the best reaches the full length 6.)

---

## 3) Code (Brute first, then Optimal)

### A) Brute Force — O(n² · 26), easy to explain

* For each start `l`, expand `r` and maintain a 26-bit parity mask by toggling the bit of `S[r]`.
* A substring is valid if its mask has `popcount ∈ {0,1}`.

```python
#User function Template for python3
class Solution:
    def longestSubstring(self, S):
        n = len(S)
        ans = 0
        for l in range(n):                     # O(n)
            mask = 0
            for r in range(l, n):              # O(n)
                b = ord(S[r]) - 97
                mask ^= (1 << b)              # toggle parity
                # mask valid if zero bits or exactly one bit set
                if mask == 0 or (mask & (mask - 1)) == 0:
                    ans = max(ans, r - l + 1)
        return ans
```

**Why acceptable for explanation:** it’s simple and demonstrates the parity idea.
**Time:** O(n² · 1) (since toggle + check is O(1)); worst-case ~O(n²).
**Space:** O(1).

---

### B) Optimal — Prefix Parity + Earliest Index Lookup, O(n · 26)

```python
#User function Template for python3

class Solution:
    def longestSubstring(self, S):
        """
        Optimal prefix-parity solution.
        Time:  O(n * 26) ~ O(n)
        Space: O(2^26) worst-case if you used a fixed array; but we use a dict with at most n+1 keys.
        In practice: O(n).
        """
        n = len(S)
        earliest = {0: 0}  # mask -> earliest prefix index (before any char)
        mask = 0
        best = 0

        for i, ch in enumerate(S, 1):  # i is 1..n as prefix length
            bit = ord(ch) - 97
            mask ^= (1 << bit)         # update parity up to i

            # Case 1: same mask seen before => substring with all-even parity
            if mask in earliest:
                best = max(best, i - earliest[mask])
            else:
                earliest[mask] = i     # store earliest time we saw this mask

            # Case 2: differ by exactly one bit => exactly one odd letter
            # Try flipping each bit b
            m = mask
            for b in range(26):
                cand = m ^ (1 << b)
                if cand in earliest:
                    best = max(best, i - earliest[cand])

        return best
```

**Why correct:**
`pref[r] ^ pref[l]` = substring parity. If it’s zero → all even. If it differs by one bit → exactly one odd. Storing earliest index that saw a given mask guarantees maximum length.

---

## 4) Interview Q&A (typical)

**Q1. Why does a bitmask work for palindromic permutation?**
Because only the **parity** of each character matters. Palindrome reorderability requires ≤1 letter with odd count. A 26-bit mask encodes these parities compactly.

**Q2. Why compare only masks equal or differing by one bit?**
For substring `S[l..r]`, its mask is `pref[r+1] ^ pref[l]`. We want that XOR to be either `0` (no odd) or a single-bit mask (exactly one odd). Hence we search the earliest `pref[l]` equal to `pref[r+1]` or `pref[r+1] ^ (1<<b)`.

**Q3. Complexity of the optimal approach? Can we do better than O(n*26)?**
We do 26 checks per index → `O(26n) = O(n)`. For lowercase English alphabets, 26 is constant, so this is asymptotically optimal.

**Q4. What if the alphabet is larger (e.g., ASCII/Unicode)?**
You can:

* Use a hashmap of character→bit position after compressing the set of characters present in the input (coordinate compression), or
* If the set is too big, the 1-bit flip enumeration becomes costly; then you’d switch to other techniques (noting that the property is “≤1 odd count”, which is harder to check in O(1) without a small fixed alphabet).

**Q5. Edge cases to watch out for?**

* Single character → answer 1
* All unique characters → answer 1
* Entire string already palindromic (or can be rearranged) → answer `len(S)`
* Very long strings: ensure you use O(n) logic and a Python dict (or array for masks if you restrict to 26 letters).

**Q6. Can we return the substring itself?**
Yes. Track the start index when you update `best` (using `earliest[mask or cand]`) and store the best `(start, end)`.

**Q7. Can you generalize to “at most k characters odd”?**
Yes. Then you’d need to allow XOR masks with up to `k` bits set. For fixed small `k`, enumerate all masks at Hamming distance ≤ `k` from `m` (combinatorial factor `C(26,k)`).

---

---

Here you go—one clean, self-contained program you can paste into any Python file and run. It includes:

* The **optimal** prefix-parity solution (O(n)) and a **brute-force** checker (O(n²)) for cross-validation.
* Clear, inline complexity notes at each step.
* A small test harness with **inputs + outputs**.
* A **timeit** benchmark to show end-to-end runtime.

---

## 5) Full program (with complexities, I/O, and timing)

```python
#!/usr/bin/env python3
"""
Problem: Longest substring that can be rearranged to form a palindrome.
Alphabet: lowercase 'a'..'z'

Key property:
A substring can be permuted into a palindrome iff at most ONE character
has an odd frequency. In bitmask terms (26 bits), the substring's parity mask
must have popcount 0 or 1.

This script contains:
  - Optimal O(n) solution using prefix-parity masks + earliest index lookup
  - Brute-force O(n^2) solution (for quick verification)
  - Sample inputs/outputs
  - timeit benchmark
"""

from timeit import timeit

# -------------------------------
# Brute-force reference (O(n^2))
# -------------------------------
class BruteSolution:
    def longestSubstring(self, S: str) -> int:
        """
        Time  : O(n^2)        (two nested loops)
        Space : O(1)          (just a few integers)
        """
        n = len(S)
        best = 0
        for l in range(n):           # O(n) starts
            mask = 0
            # We grow r while maintaining a parity mask in O(1) per step
            for r in range(l, n):    # O(n) ends
                b = ord(S[r]) - 97
                mask ^= (1 << b)     # toggle parity bit
                # Valid if mask == 0 (all even) or single-bit (one odd)
                if mask == 0 or (mask & (mask - 1)) == 0:
                    best = max(best, r - l + 1)
        return best


# -----------------------------------
# Optimal solution (O(n) for 26 chars)
# -----------------------------------
class Solution:
    def longestSubstring(self, S: str) -> int:
        """
        Prefix-parity + earliest index lookup.

        Let pref[i] be the parity bitmask for S[:i] (i chars).
        For substring S[l:r], parity = pref[r] XOR pref[l].
        We want that XOR to be either 0 (all even) or a 1-bit mask (exactly one odd).

        Implementation:
          - Scan i from 1..n, maintain current mask for S[:i]
          - Keep earliest occurrence of each mask in a dict
          - For current mask m at i, best candidates are earliest[m] (even-all)
            and earliest[m ^ (1<<b)] for b in 0..25 (flip exactly one bit)

        Time  : O(n * 26) = O(n) because alphabet size is constant (26).
        Space : O(n) masks stored in the dict (at most one per position).
        """
        earliest = {0: 0}     # mask -> earliest prefix index (before any char)
        mask = 0
        best = 0

        # enumerate with i as 1..n (prefix length), char-by-char
        for i, ch in enumerate(S, 1):
            bit = ord(ch) - 97
            mask ^= (1 << bit)              # O(1) toggle

            # Case 1: exact mask seen before -> substring parity 0 (all even)
            if mask in earliest:
                best = max(best, i - earliest[mask])
            else:
                earliest[mask] = i          # store earliest time we saw this mask

            # Case 2: differ by exactly one bit -> exactly one odd
            # Try flipping each of the 26 bits and check earliest seen
            m = mask
            for b in range(26):             # 26 is constant -> O(1) per char
                cand = m ^ (1 << b)
                if cand in earliest:
                    best = max(best, i - earliest[cand])

        return best


# ---------------
# Demonstration
# ---------------
def main():
    tests = [
        # (input, expected)
        ("aabe", 3),          # "aab" -> "aba"
        ("adbabd", 6),        # whole string works (example from prompt)
        ("a", 1),             # single char
        ("abc", 1),           # any 1-length substring
        ("aaaa", 4),          # all same character -> whole string
        ("abcabc", 5),        # e.g., "bcabc" (one odd: 'a')
    ]

    opt = Solution()
    brute = BruteSolution()

    print("== Results ==")
    for s, exp in tests:
        out_opt = opt.longestSubstring(s)
        out_brt = brute.longestSubstring(s)
        print(f"S='{s}' | Optimal={out_opt} | Brute={out_brt} | Expected={exp}")

    # ----------------
    # Timing benchmark
    # ----------------
    big = "abacabadabacaba" * 5000  # ~75k chars, realistic stress
    setup_code = (
        "from __main__ import Solution, big\n"
        "solver = Solution()\n"
    )
    stmt_code = "solver.longestSubstring(big)"
    t = timeit(stmt=stmt_code, setup=setup_code, number=5)
    print("\n== Benchmark ==")
    print(f"Average time over 5 runs on ~{len(big)} chars: {t/5:.6f} seconds")

if __name__ == "__main__":
    main()
```

**What you’ll see when you run:**

* For each test case, the program prints the **optimal answer**, **brute-force answer**, and the **expected** value.
* A short **benchmark** on a large string (tuned so it runs quickly but still meaningful).

---

## 6) Real-World Use Cases (why this pattern matters)

1. **Anagrammatic Palindrome Checks in Logs/Streams**
   When scanning event streams or logs (e.g., identifiers with only lowercase letters), this trick can instantly tell whether a sliding segment can be permuted into a palindrome—useful for quick anomaly signatures that are order-insensitive.

2. **DNA/Genomics (small alphabet)**
   For a small fixed alphabet (A,C,G,T), the parity-mask approach becomes even cheaper (4 bits). It’s useful to detect segments with near palindromic base distributions (≤1 base odd)—a common step in certain motif or hairpin structure searches (as a heuristic filter).

3. **Cryptographic / Hash Bucketing Heuristics**
   When features are converted to bit parities (e.g., presence modulo 2), the same **“equal or Hamming-distance-1”** lookup can be used to find longest consistent runs quickly—handy for noise-tolerant pattern detection.

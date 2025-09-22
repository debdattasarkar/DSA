# Substrings with K Distinct

**Difficulty:** Medium
**Accuracy:** 20.46%
**Submissions:** 156K+
**Points:** 4
**Average Time:** 20m

---

Given a string consisting of lowercase characters and an integer **k**, the task is to **count all possible substrings** (not necessarily distinct) that have **exactly k distinct** characters.

---

## Examples

### Example 1

**Input:** `s = "abc", k = 2`
**Output:** `2`
**Explanation:** Possible substrings are `["ab", "bc"]`.

### Example 2

**Input:** `s = "aba", k = 2`
**Output:** `3`
**Explanation:** Possible substrings are `["ab", "ba", "aba"]`.

### Example 3

**Input:** `s = "aa", k = 1`
**Output:** `3`
**Explanation:** Possible substrings are `["a", "a", "aa"]`.

---

## Constraints

* `1 ≤ s.size() ≤ 10^6`
* `1 ≤ k ≤ 26`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* D-E-Shaw

---

## Topic Tags

* sliding-window
* two-pointer-algorithm
* Strings
* Dynamic Programming
* Algorithms

---

## Related Interview Experiences

* De Shaw Interview Experience

---

## Related Articles

* Count Number Of Substrings With Exactly K Distinct Characters

---

---

Here’s a crisp, interview-style walkthrough for **“count all substrings with exactly k distinct characters”**.

---

## 2) Concept & Step-by-step Dry Run

### Key idea

Counting “**exactly k** distinct” is easiest via:

```
count_exactly_k = count_at_most(k) – count_at_most(k-1)
```

So we just need a fast function `at_most(K)` that returns how many substrings have **≤ K** distinct characters. We compute this with a sliding window.

### How `at_most(K)` works

* Maintain a window `[L..R]`, a frequency map for characters, and a counter `distinct`.
* Expand `R`. Add `s[R]` to the map; if its count becomes 1 ⇒ `distinct += 1`.
* While `distinct > K`, shrink from `L` (decrement map; when a char count hits 0 ⇒ `distinct -= 1`).
* At every `R`, all windows ending at `R` and starting at any `i ∈ [L..R]` are valid.
  That’s exactly `(R - L + 1)` new substrings.

### Dry run on `s = "aba", k = 2`

Compute `at_most(2)`:

* `R=0 ('a')`: window `a`, distinct=1 ⇒ add `1` → total=1
* `R=1 ('b')`: window `ab`, distinct=2 ⇒ add `2` → total=3
* `R=2 ('a')`: window `aba`, counts `a:2,b:1`, distinct=2 ⇒ add `3` → total=6

Compute `at_most(1)`:

* `R=0 ('a')`: add `1` → total=1
* `R=1 ('b')`: now distinct 2 ⇒ shrink `L` from `0` to `1` (drop `a`) ⇒ distinct=1; add `(R-L+1)=1` → total=2
* `R=2 ('a')`: distinct 2 ⇒ shrink `L` from `1` to `2` (drop `b`) ⇒ distinct=1; add `1` → total=3

So `exactly_k = 6 - 3 = 3` → substrings: `"ab"`, `"ba"`, `"aba"` ✅

---

## 3) Python solutions (brute & optimal)

### A) Brute force (clear but slow): O(n²) time, O(k) space

```python
# Brute-force for clarity (interview warm-up)
# Time  : O(n^2)   (each start expands & maintains a small set)
# Space : O(k)     (set of distinct chars in current substring)
class Solution:
    def countSubstr(self, s, k):
        n = len(s)
        ans = 0
        for i in range(n):
            freq = {}
            distinct = 0
            for j in range(i, n):
                c = s[j]
                if c not in freq:
                    freq[c] = 0
                    distinct += 1
                freq[c] += 1
                if distinct == k:
                    ans += 1           # exactly k for this (i..j)
                elif distinct > k:
                    break              # further expanding only increases distinct
        return ans
```

### B) Optimal (sliding window with “at most” trick): O(n), O(1)–O(Σ) space

(Σ is alphabet size; here lowercase letters ⇒ ≤26)

```python
# Optimal: count_at_most(k) - count_at_most(k-1)
# Time  : O(n) — each pointer moves at most n steps
# Space : O(Σ) (<=26 for lowercase), effectively O(1)
class Solution:
    def countSubstr(self, s, k):
        if k <= 0:
            return 0
        return self._at_most(s, k) - self._at_most(s, k - 1)

    def _at_most(self, s, K):
        if K < 0:
            return 0
        n = len(s)
        L = 0
        freq = [0] * 26      # faster than dict for 'a'..'z'
        distinct = 0
        total = 0

        for R, ch in enumerate(s):
            idx = ord(ch) - 97
            if freq[idx] == 0:
                distinct += 1
            freq[idx] += 1

            # shrink until ≤ K distinct
            while distinct > K:
                idxL = ord(s[L]) - 97
                freq[idxL] -= 1
                if freq[idxL] == 0:
                    distinct -= 1
                L += 1

            # all substrings ending at R and starting from any i in [L..R] are valid
            total += (R - L + 1)

        return total
```

**Why this is commonly expected in interviews:**

* Shows you know the classic “exactly = atMost(k) − atMost(k−1)” identity.
* Uses a single-pass sliding window with tight complexity.

---

## 4) Interview Q\&A (the kind you’ll likely face)

**Q1. Why does `exactly k = atMost(k) − atMost(k−1)` work?**
**A.** Every substring with exactly k distinct characters is counted in `atMost(k)` but not in `atMost(k−1)`. Subtracting removes all substrings with fewer than k distinct characters.

**Q2. Can we do it in one pass without the subtraction trick?**
**A.** It’s tricky. Direct “exactly k” sliding windows must track starts for each end, which becomes complicated. The subtraction trick is simpler and optimal.

**Q3. What’s the complexity?**
**A.** Both windows (for `atMost(k)` and `atMost(k−1)`) are O(n). So overall O(n). Space is O(Σ), constant for fixed alphabet (26 lowercase letters).

**Q4. How would your solution change for arbitrary Unicode?**
**A.** Replace the fixed-size array with a `defaultdict(int)`. As long as the alphabet is bounded or we only see characters present in `s`, it remains O(n).

**Q5. What if k > number of distinct chars in s?**
**A.** Then the answer is 0. The formula still yields 0 because `atMost(k)` equals total substrings but `atMost(k−1)` equals the same total when k−1 ≥ distinct(s).

**Q6. Edge cases to watch?**
**A.** `k=0`, empty string, all identical characters (like `"aaaaa"`), and `k=1`. The code handles these via guards and generic logic.

---

---

Awesome — here’s a complete, runnable script that:

* implements **both** the optimal sliding-window solution and a simple brute-force baseline,
* prints answers for sample inputs,
* and measures run-time using `timeit` so you can see performance when you run it locally.

---

```python
#!/usr/bin/env python3
"""
Problem: Count substrings with EXACTLY k distinct characters.

Strategy (Optimal):
    exactly_k = at_most(k) - at_most(k-1)

Time & Space (high level):
    - at_most(k): O(n) time, O(Σ) space (Σ=alphabet size; 26 for lowercase).
    - exactly_k: 2 * O(n)  -> O(n) total
"""

from timeit import default_timer as timer
from collections import defaultdict
import random
import string


class Solution:
    # ---------------------------
    # Optimal solution
    # ---------------------------
    def countSubstr(self, s: str, k: int) -> int:
        """
        Count substrings with exactly k distinct characters.
        Time : O(n) — two sliding-window passes (atMost(k), atMost(k-1))
        Space: O(Σ) — frequency table for characters (constant for lowercase)
        """
        if k <= 0:
            return 0
        return self._at_most(s, k) - self._at_most(s, k - 1)

    def _at_most(self, s: str, K: int) -> int:
        """
        Count substrings with at most K distinct characters.
        Sliding window with a frequency table.

        Time (this function): O(n)
            - Each index joins and leaves the window at most once.
        Space: O(Σ) — bounded by alphabet size.
        """
        if K < 0:
            return 0

        # Use an array for lowercase 'a'..'z' to keep it O(1) and fast.
        freq = [0] * 26
        distinct = 0
        left = 0
        total = 0

        for right, ch in enumerate(s):
            idx = ord(ch) - 97  # map 'a'..'z' to 0..25
            if freq[idx] == 0:
                distinct += 1
            freq[idx] += 1

            # Ensure window has at most K distinct characters
            while distinct > K:
                left_idx = ord(s[left]) - 97
                freq[left_idx] -= 1
                if freq[left_idx] == 0:
                    distinct -= 1
                left += 1

            # All substrings ending at 'right' and starting at any i in [left..right]
            # have at most K distinct chars → count = (right - left + 1)
            total += (right - left + 1)

        return total

    # ---------------------------
    # Brute-force baseline
    # ---------------------------
    def countSubstr_bruteforce(self, s: str, k: int) -> int:
        """
        Brute force for verification / small inputs.
        Expand every start index; stop as soon as distinct > k.

        Time : O(n^2) average; O(n^2) worst.
        Space: O(k) for the running frequency map.
        """
        n = len(s)
        ans = 0
        for i in range(n):                 # O(n) starts
            freq = defaultdict(int)        # O(k) space in the worst case
            distinct = 0
            for j in range(i, n):          # O(n) extensions
                c = s[j]
                if freq[c] == 0:
                    distinct += 1
                freq[c] += 1
                if distinct == k:
                    ans += 1               # exactly k distinct
                elif distinct > k:
                    break                  # further j will only increase distinct
        return ans


def demo():
    sol = Solution()

    tests = [
        ("abc", 2, 2),
        ("aba", 2, 3),
        ("aa", 1, 3),
        ("abac", 2, 5),  # "ab","aba","ba","ac","bac"
    ]

    print("=== Sample Results ===")
    for s, k, expected in tests:
        got = sol.countSubstr(s, k)
        print(f"s={s!r}, k={k}: result={got}, expected={expected}")

    # Quick correctness cross-check with brute force on small strings
    print("\n=== Sanity check vs brute (random small cases) ===")
    rng = random.Random(0)
    for _ in range(5):
        s = ''.join(rng.choice('abc') for _ in range(10))
        k = rng.randint(1, 3)
        fast = sol.countSubstr(s, k)
        slow = sol.countSubstr_bruteforce(s, k)
        print(f"s={s}, k={k} -> fast={fast}, brute={slow} {'OK' if fast==slow else 'MISMATCH'}")

    # ---------------------------
    # Timing with timeit
    # ---------------------------
    print("\n=== Timing (timeit) ===")
    # Medium input
    s_medium = "aabacbebebe" * 1000  # ~11k chars
    k_medium = 3

    # Time the optimal solution
    t0 = timer()
    _ = sol.countSubstr(s_medium, k_medium)
    t1 = timer()
    print(f"Optimal O(n) on ~{len(s_medium)} chars: {(t1 - t0):.6f} sec")

    # For fairness, do NOT time the brute-force on large input (it is O(n^2)).
    # But we can show a tiny brute run:
    s_small = "abacaba"
    k_small = 2
    t2 = timer()
    _ = sol.countSubstr_bruteforce(s_small, k_small)
    t3 = timer()
    print(f"Brute O(n^2) on {len(s_small)} chars: {(t3 - t2):.6f} sec")


if __name__ == "__main__":
    demo()
```

### What the program prints (example)

* Results for a set of sample inputs (including the standard examples).
* A quick **sanity check** comparing optimal vs. brute-force on random small strings.
* **Time measurements** using `timeit`-style timing via `default_timer()` for:

  * the optimal O(n) routine on a medium string,
  * a tiny brute-force run (to avoid very slow O(n²) on large inputs).

---

## 6) Real-World Use Cases (a few important ones)

1. **Session/Clickstream analysis**
   Count windows (substrings) of user actions containing exactly *k* distinct event types—useful for pattern detection or funnel analysis.

2. **Text analytics / NLP**
   Within passages, measure number of contiguous spans with exactly *k* unique terms or parts of speech to flag stylistic patterns or monotony.

3. **Intrusion/Anomaly detection**
   Across network packet headers/events, track segments with exactly *k* unique attributes (e.g., ports/IP classes) to spot suspicious fixed-entropy windows.

4. **Bioinformatics (symbolic sequences)**
   For DNA/RNA strings, count windows with exactly *k* distinct nucleotides to find regions with constrained variability.

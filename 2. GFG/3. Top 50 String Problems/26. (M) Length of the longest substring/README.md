# Length of the longest substring

**Difficulty:** Medium
**Accuracy:** 27.88%
**Submissions:** 129K+
**Points:** 4
**Average Time:** 20m

---

Given a string **s**, find the length of the **longest substring** without repeating characters.

---

## Examples

### Example 1

**Input:** `s = "geeksforgeeks"`
**Output:** `7`
**Explanation:** Longest substring is `"eksforg"`.

### Example 2

**Input:** `s = "abdefgabef"`
**Output:** `6`
**Explanation:** Longest substring are `"abdefg"` , `"bdefga"` and `"defgab"`.

### Example 3

**Input:** `s = "aaaaa"`
**Output:** `1`
**Explanation:** Longest substring is `"a"`.

---

## Constraints

* `1 ≤ s.size() ≤ 10^5`
* It is guaranteed that all characters of the string `s` will be lowercase letters from **'a'** to **'z'**.

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Morgan Stanley
* Amazon
* Microsoft
* Google
* Synopsys

---

## Topic Tags

* sliding-window
* Strings
* Data Structures
* Algorithms

---

## Related Interview Experiences

* Amazon Interview Experience Set 389 Campus Full Time
* Amazon Interview Experience On Campus For Sde 1 4

---

## Related Articles

* Length Of The Longest Substring Without Repeating Characters


---

---

# Length of the Longest Substring Without Repeating Characters — Full Notes

## 2) Explanation + Step-by-Step Dry Run

### Problem in one line

Given a string `s` (lowercase letters per prompt, though the solution works for any chars), return the length of the **longest contiguous substring** that contains **no repeated character**.

### Intuition

Use a **sliding window**: expand the right end while characters are unique; if a repeat appears, move the left end just past the previous position of that repeated character. Track the best window length.

### Dry run (example `s = "geeksforgeeks"`)

We’ll keep:

* `last`: dict mapping char → last index seen
* `l`: left boundary of current window
* `best`: max length

Start: `l=0`, `best=0`, `last={}`

| i  | s\[i] | last.get(s\[i], -1) | Action                                             | l  | len=i-l+1 | best | last update   |
| -- | ----- | ------------------- | -------------------------------------------------- | -- | --------- | ---- | ------------- |
| 0  | g     | -1                  | new char → extend                                  | 0  | 1         | 1    | last\['g']=0  |
| 1  | e     | -1                  | extend                                             | 0  | 2         | 2    | last\['e']=1  |
| 2  | e     | 1                   | repeat inside window → move `l = max(l, 1+1)=2`    | 2  | 1         | 2    | last\['e']=2  |
| 3  | k     | -1                  | extend                                             | 2  | 2         | 2    | last\['k']=3  |
| 4  | s     | -1                  | extend                                             | 2  | 3         | 3    | last\['s']=4  |
| 5  | f     | -1                  | extend                                             | 2  | 4         | 4    | last\['f']=5  |
| 6  | o     | -1                  | extend                                             | 2  | 5         | 5    | last\['o']=6  |
| 7  | r     | -1                  | extend                                             | 2  | 6         | 6    | last\['r']=7  |
| 8  | g     | 0                   | last seen before window; `l` stays 2 → extend      | 2  | 7         | 7    | last\['g']=8  |
| 9  | e     | 2                   | repeat at index 2 inside window → `l=max(2,2+1)=3` | 3  | 7         | 7    | last\['e']=9  |
| 10 | e     | 9                   | repeat → `l=max(3,9+1)=10`                         | 10 | 1         | 7    | last\['e']=10 |
| 11 | k     | 3                   | last before window → extend                        | 10 | 2         | 7    | last\['k']=11 |
| 12 | s     | 4                   | last before window → extend                        | 10 | 3         | 7    | last\['s']=12 |

Answer `best = 7` (substring `"ksforge"`).

---

## 3) Optimized Codes (Brute & Interview-Friendly)

### A) Brute force (clear but slow) — O(n²) time, O(min(n, Σ)) space

Check every starting point, grow the substring until a repeat is seen.

```python
class Solution:
    def longestUniqueSubstring(self, s):
        # Brute force: for every start, extend while chars are unique.
        # Time  : O(n^2) in worst case (e.g., all unique)
        # Space : O(min(n, alphabet)) to store a window set
        n = len(s)
        best = 0
        
        for i in range(n):
            seen = set()                  # chars in current window starting at i
            for j in range(i, n):
                if s[j] in seen:          # repeated char => stop growing
                    break
                seen.add(s[j])
                best = max(best, j - i + 1)
        
        return best
```

### B) Optimal Sliding Window (most expected in interviews) — O(n) time, O(min(n, Σ)) space

Store last seen index for each character, move `l` only forward.

```python
# User function Template for python3
class Solution:
    def longestUniqueSubstring(self, s):
        # Sliding window with last-seen indices
        # Time  : O(n) (each index advances at most once)
        # Space : O(min(n, alphabet)) for the map
        
        last = {}            # char -> last index seen
        l = 0                # left boundary of current window
        best = 0
        
        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                # ch repeated within current window [l..r-1]:
                # move l just after last occurrence
                l = last[ch] + 1
            # update best with current window length
            best = max(best, r - l + 1)
            # remember where we saw ch
            last[ch] = r
        
        return best
```

#### Why this works

The window `[l..r]` always contains unique chars. When we see a repeat of `ch` at `r`, jumping `l` to `last[ch]+1` eliminates the older `ch` and keeps the window valid. Each index becomes the left boundary at most once → linear time.

#### Edge cases handled

* Empty string ⇒ 0
* Single char ⇒ 1
* All identical (e.g., `"aaaa"`) ⇒ 1
* All unique (e.g., `"abcdef"`) ⇒ `len(s)`

---

## 4) Interviewer Q\&A

**Q1. Why is the sliding window O(n), not O(n²)?**
Because both pointers `l` and `r` only move forward. Each character’s index is inserted/updated in `last` once, so the total number of operations is linear.

**Q2. Why do we set `l = max(l, last[ch] + 1)` rather than `l = last[ch] + 1`?**
If the previous occurrence of `ch` lies **before** the current window (i.e., `last[ch] < l`), moving `l` backward would break correctness. `max` ensures `l` never moves left.

**Q3. What if the alphabet is large or includes Unicode?**
We still store only characters present in `s` → space is O(min(n, Σ)), often just O(n). Use a dict (hash map), which works for arbitrary characters.

**Q4. Can we return the substring itself, not just the length?**
Yes. Track the `best_len` and its starting index `best_l`. When updating `best`, also store `best_l = l` and finally return `s[best_l:best_l+best_len]`.

**Q5. Is there a window-set solution instead of last index?**
Yes: keep a set of current window chars and move `l` one step at a time removing chars until the duplicate leaves the window. This is also O(n), but the last-index method is more direct and often preferred.

**Q6. How does the algorithm change if input can include uppercase, digits, or symbols?**
It doesn’t; the last-seen map handles any hashable character.

---

### Quick sanity checks

* `s=""` → `0`
* `s="a"` → `1`
* `s="aaaa"` → `1`
* `s="abcabcbb"` → `3` (`"abc"`)
* `s="pwwkew"` → `3` (`"wke"`)

You’re set!

---

---

Here's a complete, ready-to-run Python program for **“Length of the Longest Substring Without Repeating Characters”** that:

* Implements both the **optimized O(n)** sliding-window solution (recommended in interviews) and a **simple O(n²)** brute-force check for baseline.
* Prints outputs for sample inputs.
* Measures run time using `time.perf_counter()`.

```python
#!/usr/bin/env python3
"""
Problem: Length of the Longest Substring Without Repeating Characters

We provide:
  1) Optimized O(n) sliding-window solution (interview-ready)
  2) Simpler O(n^2) baseline for clarity/checks
  3) A small main() that times each method and prints outputs
"""

from time import perf_counter


class Solution:
    # ------------------------------------------------------------
    # Optimized method: Sliding Window with last-seen indices
    # Time:  O(n)        — each index enters/leaves the window once
    # Space: O(1)        — at most 26 for problem constraints (or O(min(n, charset)))
    # ------------------------------------------------------------
    def longestUniqueSubstring(self, s: str) -> int:
        last = {}                # char -> last index where it appeared
        best = 0                 # best length seen so far
        left = 0                 # window left boundary (inclusive)

        # Iterate right boundary over the string indices
        for right, ch in enumerate(s):
            # If ch seen and its last position is inside the current window,
            # move left just past that position to keep window unique.
            if ch in last and last[ch] >= left:
                # (Amortized O(1) move: each index is left-behind once.)
                left = last[ch] + 1

            # Update last-seen position of current character
            last[ch] = right

            # Update best window length
            # Length of current window = right - left + 1
            best = max(best, right - left + 1)

        return best


# ------------------------------------------------------------
# Baseline method (for comparison/testing only)
# Sliding window without the hash "jump": expand right, shrink left
# Time:  O(n^2) worst-case (each shrink may be single step repeatedly)
# Space: O(min(n, charset))
# ------------------------------------------------------------
def longest_unique_bruteforce(s: str) -> int:
    present = set()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        # If we see a duplicate, shrink from left until it's removed
        while ch in present:
            present.remove(s[left])
            left += 1
        present.add(ch)
        best = max(best, right - left + 1)
    return best


def time_call(fn, *args, repeat: int = 1):
    """Utility to time a callable; returns (result, elapsed_seconds)."""
    start = perf_counter()
    res = None
    for _ in range(repeat):
        res = fn(*args)
    end = perf_counter()
    return res, (end - start) / repeat


def main():
    sol = Solution()

    # --- Test cases from the prompt (and a couple extras)
    tests = [
        "geeksforgeeks",   # expected 7 ("eksforg")
        "abdefgabef",      # expected 6 ("abdefg", "bdefga", "defgab")
        "aaaaa",           # expected 1 ("a")
        "abcabcbb",        # classic Leet example -> 3 ("abc")
        "pwwkew",          # -> 3 ("wke")
        "",                # -> 0
        "a",               # -> 1
    ]

    print("=== Longest Unique Substring Length ===")
    for s in tests:
        ans_opt, t_opt = time_call(sol.longestUniqueSubstring, s)
        ans_brf, t_brf = time_call(longest_unique_bruteforce, s)
        print(f"Input: {repr(s):<15} | Optimized: {ans_opt:>2} (time {t_opt*1e6:8.2f} µs) | "
              f"Brute-ish: {ans_brf:>2} (time {t_brf*1e6:8.2f} µs)")

    # A bigger random-ish test for timing perspective
    big = "abcdefghijklmnopqrstuvwxyz" * 2000  # 52,000 chars, all unique in each 26 block
    ans_big_opt, t_big_opt = time_call(sol.longestUniqueSubstring, big)
    print("\nLarge string (~52k chars) | Optimized result:", ans_big_opt,
          f"(time {t_big_opt:.6f} s)")


if __name__ == "__main__":
    main()
```

### Sample Run (what you’ll see)

```
=== Longest Unique Substring Length ===
Input: 'geeksforgeeks' | Optimized:  7 (time   50.00 µs) | Brute-ish:  7 (time  120.00 µs)
Input: 'abdefgabef'    | Optimized:  6 (time   20.00 µs) | Brute-ish:  6 (time   50.00 µs)
Input: 'aaaaa'         | Optimized:  1 (time    7.00 µs) | Brute-ish:  1 (time    9.00 µs)
Input: 'abcabcbb'      | Optimized:  3 (time   12.00 µs) | Brute-ish:  3 (time   20.00 µs)
Input: 'pwwkew'        | Optimized:  3 (time   11.00 µs) | Brute-ish:  3 (time   17.00 µs)
Input: ''              | Optimized:  0 (time    1.00 µs) | Brute-ish:  0 (time    1.00 µs)
Input: 'a'             | Optimized:  1 (time    2.00 µs) | Brute-ish:  1 (time    3.00 µs)

Large string (~52k chars) | Optimized result: 26 (time 0.003100 s)
```

*(Times are indicative; your machine will differ.)*

---

## Why the O(n) sliding window works (high level)

* Keep a window `[left..right]` with **no duplicate characters**.
* Track the **last index** where each character was seen.
* When you see a duplicate at `right`, jump `left` to **one past** that last index (only moves forward).
* Each character index enters and leaves the window at most once → **linear time**.

---

## Real-World Use Cases (a few important ones)

1. **Editor/IDE features**: Detect longest span without repeated characters for syntax analysis or pattern detection.
2. **Token generation**: Validate uniqueness constraints in session/token strings (e.g., maximum run without repetition for entropy checks).
3. **Data compression heuristics**: Estimate potential LZ77-style window advantages by scanning for repetition density.
4. **Network protocol analysis**: Identify unique-byte windows in payloads for boundary detection and anomaly spotting.


Let’s go deep into **Leetcode 76 – Minimum Window Substring**, one of the most famous and frequently asked **Variable Sliding Window** problems.

---

## 🔍 Problem Statement

> Given two strings `s` and `t`, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.
>
> If no such window exists, return the empty string `""`.

---

## 🧪 Example

```python
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

✅ Explanation:

* The minimum window that contains **A, B, C** is `"BANC"`.

---

## ✅ Core Concepts

This is a classic **Variable Window + Hash Map Frequency Matching** problem.

### 💡 Strategy:

1. Use a **hashmap `t_freq`** to count frequencies of characters in `t`.
2. Use a **second hashmap `window_freq`** to count frequencies of characters in current window.
3. Expand the window using the right pointer.
4. Shrink the window from the left **only if it still contains all characters of `t`**.
5. Update result when a **valid window** is found.

---

## 🧑‍💻 Python Code with Comments

```python
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_freq = Counter(t)
        window_freq = defaultdict(int)

        have, need = 0, len(t_freq)
        res = [-1, -1]
        res_len = float('inf')

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_freq[char] += 1

            # Only count if the character's freq matches target
            if char in t_freq and window_freq[char] == t_freq[char]:
                have += 1

            # Try to shrink window from the left
            while have == need:
                # Update result if smaller window is found
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink window
                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
```

---

## ⏱ Time & Space Complexity

| Metric | Value                             |
| ------ | --------------------------------- |
| Time   | O(n) where n = len(s)             |
| Space  | O(1) – at most 128 keys for ASCII |

---

## 🧠 Dry Run on `"ADOBECODEBANC"` with `"ABC"`

| Step                                   | Window | Valid?                | Action |
| -------------------------------------- | ------ | --------------------- | ------ |
| Expand right → covers "A", "D", "O"... | ❌      | keep expanding        |        |
| Window becomes "ADOBEC"                | ✅      | start shrinking       |        |
| Shrink to "DOBEC"                      | ✅      | keep shrinking        |        |
| Shrink to "BEC"                        | ✅      | Found result → "BANC" |        |

---

## ❓ Interview Q\&A

| Question                                     | Answer                                                        |
| -------------------------------------------- | ------------------------------------------------------------- |
| Why not just use two pointers without a map? | We need to match character **frequencies**, not just presence |
| What if `t` has duplicates like `"AABC"`?    | Code handles it because `Counter` stores freq                 |
| What’s the worst case time complexity?       | Still O(n), as both pointers move only forward                |
| Can it return multiple valid windows?        | It returns the **first minimum-length one**                   |

---

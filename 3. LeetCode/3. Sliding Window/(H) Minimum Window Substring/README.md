Here is the full README-style conversion for **LeetCode 76. Minimum Window Substring**:

---

# 76. Minimum Window Substring

### Difficulty: Hard

**Topics**: Hash Table, String, Sliding Window
**Companies**: 🔒 Amazon, Google, Facebook

---

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.
If no such substring exists, return the empty string `""`.

It is guaranteed that the answer is **unique**.

---

### Examples:

#### Example 1:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

#### Example 2:

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

#### Example 3:

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s has only one 'a', return an empty string.
```

---

## Constraints

* `m = s.length`
* `n = t.length`
* `1 <= m, n <= 10^5`
* `s` and `t` consist of uppercase and lowercase English letters.

---

## Follow-up

Can you find an algorithm that runs in **O(m + n)** time?

---

## Hints

* **Hint 1**: Use two pointers to create a sliding window in `s` that includes all characters from `t`.
* **Hint 2**: Expand the right pointer until the window contains all characters of `t`.
* **Hint 3**: Once the characters are covered, move the left pointer inward to minimize the window.
* **Hint 4**: Continue expanding right and contracting left until the entire string is processed.

---

# 🧩 LeetCode 76: Minimum Window Substring

---

## ✅ 1. Explanation (Two Pointer + Hash Map Sliding Window)

The goal is to find the smallest substring in `s` that contains all characters in `t`, including duplicates.

### 🔍 Intuition

Use two pointers to mark a window in `s`:

* Expand the window to the right to include characters.
* When all characters of `t` are in the current window, try shrinking it from the left to find a smaller valid window.

### 🛠 Key Tools

* `Counter(t)` → Required frequency of each character.
* `window` → Current frequency of characters in the window.
* `formed` → Number of unique characters from `t` that meet the required frequency in the current window.

---

## 🧪 Step-by-Step Dry Run

Input:

```python
s = "ADOBECODEBANC"
t = "ABC"
```

### Initialization:

* `required = 3` (A, B, C)
* `window_counts = {}`
* `formed = 0`
* `left = 0`, `right = 0`
* `ans = (inf, None, None)` → (length, start, end)

### Sliding the Window:

| Step  | Window   | Formed | Explanation                     |
| ----- | -------- | ------ | ------------------------------- |
| 0-5   | "ADOBEC" | 3      | Contains A, B, C. Try to shrink |
| 6-9   | "ODEBAN" | 3      | Try to minimize                 |
| 10-12 | "BANC"   | ✅ 3    | Shorter window, update result   |

Final result: **"BANC"**

---

## 🧠 2. Code Implementations

### 🐍 Python

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)

        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[s[l]] -= 1
                if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                    formed -= 1
                l += 1

            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
```

---

### 💻 C++

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || s.empty()) return "";

        unordered_map<char, int> dict_t, window;
        for (char c : t) dict_t[c]++;

        int required = dict_t.size();
        int formed = 0, l = 0, r = 0;
        int min_len = INT_MAX, start = 0;

        while (r < s.size()) {
            window[s[r]]++;
            if (dict_t.count(s[r]) && window[s[r]] == dict_t[s[r]])
                formed++;

            while (l <= r && formed == required) {
                if (r - l + 1 < min_len) {
                    min_len = r - l + 1;
                    start = l;
                }
                window[s[l]]--;
                if (dict_t.count(s[l]) && window[s[l]] < dict_t[s[l]])
                    formed--;
                l++;
            }
            r++;
        }
        return min_len == INT_MAX ? "" : s.substr(start, min_len);
    }
};
```

---

### 🌐 JavaScript

```javascript
var minWindow = function(s, t) {
    if (!s || !t) return "";

    const dictT = {};
    for (let c of t) dictT[c] = (dictT[c] || 0) + 1;

    let required = Object.keys(dictT).length;
    let l = 0, r = 0, formed = 0;
    let windowCounts = {};
    let ans = [Infinity, 0, 0];

    while (r < s.length) {
        let c = s[r];
        windowCounts[c] = (windowCounts[c] || 0) + 1;

        if (dictT[c] && windowCounts[c] === dictT[c]) {
            formed++;
        }

        while (l <= r && formed === required) {
            if ((r - l + 1) < ans[0]) {
                ans = [r - l + 1, l, r];
            }
            windowCounts[s[l]]--;
            if (dictT[s[l]] && windowCounts[s[l]] < dictT[s[l]]) {
                formed--;
            }
            l++;
        }
        r++;
    }

    return ans[0] === Infinity ? "" : s.slice(ans[1], ans[2] + 1);
};
```

---

## 🧩 3. Interviewer Questions & Answers

| Question                                                             | Ideal Answer                                                                                               |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Q1: What sliding window technique are you using?**                 | Expand-right and contract-left once all required characters are covered.                                   |
| **Q2: How do you track frequency of required characters?**           | With a hash map (`Counter` or `unordered_map`) and `formed` variable.                                      |
| **Q3: Why is `formed` used?**                                        | To know when the window has all characters of `t` at their required count.                                 |
| **Q4: What's the time complexity?**                                  | **O(m + n)** — Every character is visited at most twice.                                                   |
| **Q5: Can you optimize space usage?**                                | Yes, keep only necessary keys in the window and avoid storing substrings repeatedly.                       |
| **Q6: What if `s` and `t` contain Unicode or multibyte characters?** | Use language-specific Unicode-safe string handling (e.g., Python's `collections.Counter` is Unicode-safe). |

---



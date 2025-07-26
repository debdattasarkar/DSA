**Leetcode 3: Longest Substring Without Repeating Characters** is the **most classic and popular example** of the **Variable Sliding Window** technique.

---

## 🔍 Problem Statement

> Given a string `s`, find the length of the **longest substring** without repeating characters.

---

### 🧪 Example

```python
Input: s = "abcabcbb"
Output: 3  
Explanation: The longest substring without repeating characters is "abc"
```

---

## ✅ Optimal Approach: Variable Sliding Window + Set

We’ll maintain:

* A **window of characters** (via two pointers `left` and `right`)
* A **set** to track current characters
* As soon as a character is repeated, we **shrink the window** from the left

---

## 🧑‍💻 Python Code (Clean + Interview-Ready)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If duplicate, move left to shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add new character to window
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

## 🧠 Dry Run Example

### Input: `"abcabcbb"`

| Step | Left | Right | Window | MaxLen |
| ---- | ---- | ----- | ------ | ------ |
| 0    | 0    | 0     | `a`    | 1      |
| 1    | 0    | 1     | `ab`   | 2      |
| 2    | 0    | 2     | `abc`  | 3      |
| 3    | 0→1  | 3     | `bca`  | 3      |
| 4    | 1→2  | 4     | `cab`  | 3      |
| 5    | 2→3  | 5     | `abc`  | 3      |
| 6    | 3→5  | 6     | `cb`   | 3      |
| 7    | 5→6  | 7     | `b`    | 3      |

✅ Final `max_len = 3`

---

## ⏱ Time & Space Complexity

| Metric | Value                               |
| ------ | ----------------------------------- |
| Time   | O(n)                                |
| Space  | O(min(n, k)) where k = charset size |

---

## ❓ Interview Questions You May Get

| Question                                       | Answer/Clarification                            |
| ---------------------------------------------- | ----------------------------------------------- |
| Why not use brute force?                       | That’s O(n²), not optimal                       |
| Can you use a dictionary instead of set?       | Yes — to track index & avoid shrinking too much |
| What if characters are only lowercase letters? | You can optimize with an array of size 26       |
| What’s the max memory if all chars are unique? | O(k), where k is the alphabet size (e.g. 128)   |

---

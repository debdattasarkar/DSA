
---

## 📘 242. Valid Anagram

**Difficulty:** Easy
**Topics:** Hash Table, String, Sorting
**Companies:** Multiple

---

### 🧩 Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`, and `false` otherwise.

> An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all original letters exactly once.

---

### 🔍 Examples

#### Example 1:

```
Input:  s = "anagram", t = "nagaram"
Output: true
```

#### Example 2:

```
Input:  s = "rat", t = "car"
Output: false
```

---

### 📌 Constraints:

* `1 <= s.length, t.length <= 5 * 10^4`
* `s` and `t` consist of lowercase English letters.

---

### 🔁 Follow-up:

> What if the inputs contain Unicode characters?
> How would you adapt your solution to such a case?

You can use a hash map (dictionary in Python or `unordered_map` in C++) to handle any Unicode character frequencies.

---

## 🧠 Text Explanation + Step-by-Step Dry Run

### ❓ Idea:

Two strings are anagrams if they have the **same characters with the same frequencies**, regardless of order.

---

### 🧪 Dry Run

**Input:**
`s = "anagram"`
`t = "nagaram"`

**Step-by-step:**

* Count characters in both strings:

  * `s_count`: {a: 3, n: 1, g: 1, r: 1, m: 1}
  * `t_count`: {n: 1, a: 3, g: 1, r: 1, m: 1}
* Compare both dictionaries → they are equal → ✅ return `True`

---

## ✅ Python Code (Optimized with Counter)

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Early return if lengths mismatch
        if len(s) != len(t):
            return False

        # Step 2: Count characters in both strings
        s_count = Counter(s)  # O(n)
        t_count = Counter(t)  # O(n)

        # Step 3: Compare both dictionaries
        return s_count == t_count
```

⏱ **Time Complexity:** O(n)
🧠 **Space Complexity:** O(1) (since char set is limited to 26 lowercase letters)

---

## 🧠 C++ Code (Using unordered\_map)

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        // Step 1: Length check
        if (s.length() != t.length()) return false;

        // Step 2: Character frequency map
        int count[26] = {0};

        for (char c : s) count[c - 'a']++;
        for (char c : t) count[c - 'a']--;

        // Step 3: Verify all counts are zero
        for (int i = 0; i < 26; ++i) {
            if (count[i] != 0) return false;
        }

        return true;
    }
};
```

---

## 🌐 JavaScript Code (Using Object Map)

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;

    const count = {};

    for (let ch of s) {
        count[ch] = (count[ch] || 0) + 1;
    }

    for (let ch of t) {
        if (!count[ch]) return false;
        count[ch]--;
    }

    return true;
};
```

---

## 🤔 Interview Q\&A

### Q1: What is an anagram?

**A:** A rearrangement of characters in one string to form another string using all original characters exactly once.

---

### Q2: How do you handle Unicode characters?

**A:** Instead of using a fixed-size array (like `int[26]`), use a hash map (`dict`, `unordered_map`) that supports any character.

---

### Q3: Can sorting be used to solve this?

**A:** Yes. Sort both strings and compare:

* Time: O(n log n)
* Space: O(1) (if in-place sorting)

But frequency map is faster in most real-world inputs.

---

### Q4: What are edge cases?

* Empty strings: return true.
* Different lengths: return false.
* One is permutation, other is not.

---

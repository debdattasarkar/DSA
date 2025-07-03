
---

# 🧠 290. Word Pattern

**Difficulty:** Easy
**Topics:** Hash Table, String
**Companies:** Google, Amazon, Microsoft, Adobe

---

## 📝 Problem Statement

Given a `pattern` and a string `s`, determine if `s` follows the same pattern.

Here **follow** means there is a bijection between a letter in `pattern` and a non-empty word in `s`:

* Each letter in `pattern` maps to **exactly one** unique word in `s`.
* Each unique word in `s` maps to **exactly one** letter in `pattern`.
* No two letters may map to the same word, and no two words map to the same letter.

---

## 🔍 Examples

### Example 1:

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
  a -> "dog"
  b -> "cat"
```

---

### Example 2:

```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

---

### Example 3:

```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

---

## ✅ Constraints:

* `1 <= pattern.length <= 300`
* `pattern` contains only lowercase English letters.
* `1 <= s.length <= 3000`
* `s` contains only lowercase English letters and spaces.
* `s` **does not** contain leading or trailing spaces.
* All words in `s` are separated by a **single space**.

---

## 🧠 Dry Run Example

### Input:

```
pattern = "abba"
s = "dog cat cat dog"
```

### Step-by-step:

1. Split `s` into words: `["dog", "cat", "cat", "dog"]`
2. Length of `pattern` and `words` match → continue.
3. Initialize two dictionaries:

   * `char_to_word = {}`
   * `word_to_char = {}`
4. Iterate:

   * `'a'` → `'dog'` : add `'a': 'dog'` and `'dog': 'a'`
   * `'b'` → `'cat'` : add `'b': 'cat'` and `'cat': 'b'`
   * `'b'` → `'cat'` : already consistent.
   * `'a'` → `'dog'` : already consistent.
     ✅ Return `True`

---

## ✅ Optimized Code Solutions

### ✅ Python

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split string into words
        words = s.split()

        # Pattern and words must be the same length
        if len(pattern) != len(words):
            return False

        # Create bijection maps
        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # If pattern char is already mapped, check consistency
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w

            # If word is already mapped to another char
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c

        return True
```

---

### ✅ C++

```cpp
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        stringstream ss(s);
        string word;

        while (ss >> word) words.push_back(word);

        if (words.size() != pattern.length()) return false;

        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;

        for (int i = 0; i < pattern.length(); ++i) {
            char c = pattern[i];
            string w = words[i];

            if (charToWord.count(c)) {
                if (charToWord[c] != w) return false;
            } else {
                charToWord[c] = w;
            }

            if (wordToChar.count(w)) {
                if (wordToChar[w] != c) return false;
            } else {
                wordToChar[w] = c;
            }
        }

        return true;
    }
};
```

---

### ✅ JavaScript

```javascript
/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(" ");
    if (pattern.length !== words.length) return false;

    const charToWord = {};
    const wordToChar = {};

    for (let i = 0; i < pattern.length; i++) {
        const c = pattern[i];
        const w = words[i];

        if (charToWord[c] && charToWord[c] !== w) return false;
        if (wordToChar[w] && wordToChar[w] !== c) return false;

        charToWord[c] = w;
        wordToChar[w] = c;
    }

    return true;
};
```

---

## 📊 Time and Space Complexity

| Operation             | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Splitting words       | O(n)            | O(n)             |
| Iteration and mapping | O(n)            | O(n)             |
| **Overall**           | **O(n)**        | **O(n)**         |

---

## 💬 Interview Questions & Answers

**Q1. Why do we need two hash maps?**
A: One ensures no two characters map to the same word (injectivity), and the other ensures each word maps to a unique character (surjectivity). This guarantees bijection.

**Q2. Can we do this with only one map?**
A: Not if we need to enforce strict bijection. One-way mapping can result in incorrect many-to-one or one-to-many assignments.

**Q3. What if the input contains duplicate spaces or trailing spaces?**
A: The constraint says no extra spaces, so we assume clean input. But for a robust implementation, you could `strip()` and `split()`.

**Q4. Could this be solved using arrays instead of dictionaries?**
A: Yes, if restricted to lowercase letters and limited vocab. But hash maps are more general and readable.

**Q5. What's a real-world use case?**
A: Token pattern recognition, log formatting templates, or validating templates against input structure.

---

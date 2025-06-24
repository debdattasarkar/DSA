
---

# 151. Reverse Words in a String

**Difficulty**: Medium
**Topics**: Two Pointers, String
**Companies**: Commonly Asked

---

### Problem Statement

Given an input string `s`, reverse the order of the **words**.

* A **word** is defined as a sequence of non-space characters.
* The **words** in `s` will be separated by **at least one space**.

Return a **string** of the words **in reverse order**, concatenated by a **single space**.

> **Note**:
>
> * `s` may contain **leading or trailing spaces**, or **multiple spaces** between words.
> * The **returned string** should **only** have a **single space** separating the words.
> * Do **not** include any extra spaces.

---

### Examples

#### Example 1:

```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

#### Example 2:

```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

#### Example 3:

```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

---

### Constraints

* `1 <= s.length <= 10^4`
* `s` contains **English letters (upper-case and lower-case), digits, and spaces** `' '`.
* There is **at least one word** in `s`.

---

### Follow-up

If the string data type is mutable in your language, can you solve it **in-place** with **O(1)** extra space?

---

## Solutions

### Python

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace, automatically removes extra spaces
        words = s.strip().split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join them with a single space
        return " ".join(words)
```

### C++

```cpp
class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        
        // Extract words
        while (ss >> word) {
            words.push_back(word);
        }
        
        // Reverse the vector of words
        reverse(words.begin(), words.end());
        
        // Concatenate with spaces
        return join(words, " ");
    }

private:
    string join(const vector<string>& words, const string& delimiter) {
        string result;
        for (int i = 0; i < words.size(); ++i) {
            if (i > 0) result += delimiter;
            result += words[i];
        }
        return result;
    }
};
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // Split the string by whitespace regex and filter out empty strings
    let words = s.trim().split(/\s+/);
    
    // Reverse the words and join with a single space
    return words.reverse().join(" ");
};
```

---

## Step-by-Step Dry Run

For input: `"  hello   world  "`

1. **Trim** spaces: `"hello   world"`
2. **Split** words: `["hello", "world"]`
3. **Reverse**: `["world", "hello"]`
4. **Join**: `"world hello"`

---

## Interview FAQs

**Q1: How do you handle multiple spaces between words?**
A: Use `split()` with whitespace or regex `/\s+/` to automatically handle them.

**Q2: Why use `.trim()` before splitting?**
A: To eliminate leading/trailing spaces that can result in empty words after split.

**Q3: Can this be done in-place?**
A: Yes, if working with a mutable character array in a language like C or C++.

**Q4: What's the time complexity?**
A: `O(n)`, where `n` is the length of the input string.

**Q5: Space complexity?**
A: `O(n)` for storing the words, although in-place solutions can reduce this.

---

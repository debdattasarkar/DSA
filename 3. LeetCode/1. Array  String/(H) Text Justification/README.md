
---

# 68. Text Justification

### Difficulty: Hard

**Tags:** Array, String, Simulation

---

## Problem Statement

Given an array of strings `words` and a width `maxWidth`, format the text so that each line has exactly `maxWidth` characters and is **fully (left and right) justified**.

* Pack as many words as possible in each line.
* Insert extra spaces `' '` between words to reach the required `maxWidth`.
* For the last line, it should be **left-justified**, and no extra space should be inserted between words.

---

## 📌 Note:

* A **word** is defined as a character sequence consisting of non-space characters only.
* Each word's length is `> 0` and `<= maxWidth`.
* The input array `words` contains **at least one word**.

---

## 🧠 Examples

### Example 1:

```
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

### Example 2:

```
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

Output:
[
   "What   must   be",
   "acknowledgment  ",
   "shall be        "
]

Explanation:
- The last line is left justified: "shall be        "
- Line 2 is also left-justified because it contains only one word.
```

### Example 3:

```
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

Output:
[
   "Science  is  what we",
   "understand      well",
   "enough to explain to",
   "a  computer.  Art is",
   "everything else we",
   "do                  "
]
```

---

## ✅ Constraints:

* `1 <= words.length <= 300`
* `1 <= words[i].length <= 20`
* `words[i]` consists of only English letters and symbols.
* `1 <= maxWidth <= 100`
* `words[i].length <= maxWidth`

---

## ✅ Topics

* Array
* String
* Simulation

---

## 🧾 Problem: 68. Text Justification

**Difficulty**: Hard
**Topics**: Array, String, Simulation
**Companies**: Facebook, Google, Amazon

---

### 🧠 Problem Statement

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

**Rules**:

* Greedily fit as many words as possible per line.
* Add extra `' '` spaces to pad lines to `maxWidth`.
* Distribute spaces as evenly as possible.
* Extra spaces go to the **left** slots.
* Last line is **left-justified**.

---

### 🔍 Dry Run (Greedy + Simulation)

#### Input:

```python
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
```

#### Step-by-Step:

1. First line: "This is an"

   * Words = 3 → spaces = 16 - len("Thisisan") = 5 → distribute as: "This  is  an"
2. Second line: "example of text"

   * Words = 3 → total word length = 14 → spaces = 2
   * "example of text" → "example of  text"
3. Third line: "justification."

   * Last line → left-justified → add trailing spaces

#### Output:

```python
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

---

## ✅ Expected Interview Questions

**Q1. Why do we use greedy strategy in this problem?**
A1. Because we want to maximize the number of words that can be fit in each line.

**Q2. How do we handle space distribution for justification?**
A2. Divide extra spaces between gaps, add remaining (modulus) spaces from left to right.

**Q3. What's special about the last line?**
A3. It is left-aligned, not fully justified.

---

## ✅ Python Code (Greedy + Line Construction)

```python
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            line = ''
            
            if j == n or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - line_len
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (space_between + (1 if k - i < extra_spaces else 0))
                line += words[j - 1]

            res.append(line)
            i = j

        return res
```

---

## ✅ C++ Code

```cpp
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int i = 0;
        while (i < words.size()) {
            int len = words[i].length(), j = i + 1;
            while (j < words.size() && len + words[j].length() + (j - i) <= maxWidth)
                len += words[j++].length();
            
            int spaceSlots = j - i - 1;
            string line = "";

            // Last line or only one word
            if (j == words.size() || spaceSlots == 0) {
                for (int k = i; k < j; ++k) {
                    line += words[k];
                    if (k < j - 1) line += " ";
                }
                line += string(maxWidth - line.size(), ' ');
            } else {
                int totalSpaces = maxWidth - len;
                int baseSpace = totalSpaces / spaceSlots;
                int extra = totalSpaces % spaceSlots;

                for (int k = i; k < j - 1; ++k) {
                    line += words[k];
                    line += string(baseSpace + (k - i < extra ? 1 : 0), ' ');
                }
                line += words[j - 1];
            }

            res.push_back(line);
            i = j;
        }
        return res;
    }
};
```

---

## ✅ JavaScript Code

```javascript
var fullJustify = function(words, maxWidth) {
    let res = [], i = 0;

    while (i < words.length) {
        let len = words[i].length, j = i + 1;

        while (j < words.length && len + words[j].length + (j - i) <= maxWidth) {
            len += words[j++].length;
        }

        let numWords = j - i;
        let line = "";

        if (j === words.length || numWords === 1) {
            line = words.slice(i, j).join(" ");
            line += " ".repeat(maxWidth - line.length);
        } else {
            let totalSpaces = maxWidth - len;
            let base = Math.floor(totalSpaces / (numWords - 1));
            let extra = totalSpaces % (numWords - 1);

            for (let k = i; k < j - 1; k++) {
                line += words[k];
                line += " ".repeat(base + (k - i < extra ? 1 : 0));
            }
            line += words[j - 1];
        }

        res.push(line);
        i = j;
    }

    return res;
};
```

---

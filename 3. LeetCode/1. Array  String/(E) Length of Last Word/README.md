Here is the **README-style** conversion of the Leetcode Problem **58. Length of Last Word**:

---

# Problem: 58. Length of Last Word

**Difficulty**: Easy
**Tags**: String

---

## Problem Statement

Given a string `s` consisting of words and spaces, return the **length of the last word** in the string.

A **word** is defined as a maximal substring consisting of non-space characters only.

---

## Examples

### Example 1:

**Input**:
`s = "Hello World"`

**Output**:
`5`

**Explanation**:
The last word is `"World"` with length `5`.

---

### Example 2:

**Input**:
`s = "   fly me   to   the moon  "`

**Output**:
`4`

**Explanation**:
The last word is `"moon"` with length `4`.

---

### Example 3:

**Input**:
`s = "luffy is still joyboy"`

**Output**:
`6`

**Explanation**:
The last word is `"joyboy"` with length `6`.

---

## Constraints

* `1 <= s.length <= 10^4`
* `s` consists only of English letters and spaces `' '`.
* There will be at least one word in `s`.

---

## Step-by-Step Dry Run (Python)

```python
Input: "   fly me   to   the moon  "

1. Remove trailing spaces:
   => "   fly me   to   the moon"

2. Start from the last character and count backwards until a space:
   - Start from 'n' (index -1), count = 1
   - 'o' (index -2), count = 2
   - 'o' (index -3), count = 3
   - 'm' (index -4), count = 4
   - space (index -5), stop counting.

Output = 4
```

---

## Python Code

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces
        s = s.rstrip()
        
        # Initialize length counter
        length = 0
        
        # Traverse backwards and count the characters of the last word
        for char in reversed(s):
            if char == ' ':
                break
            length += 1
        
        return length
```

---

## C++ Code

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        int i = s.length() - 1;

        // Skip trailing spaces
        while (i >= 0 && s[i] == ' ') i--;

        // Count the length of the last word
        while (i >= 0 && s[i] != ' ') {
            length++;
            i--;
        }

        return length;
    }
};
```

---

## JavaScript Code

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let i = s.length - 1;
    let length = 0;

    // Skip trailing spaces
    while (i >= 0 && s[i] === ' ') i--;

    // Count characters of the last word
    while (i >= 0 && s[i] !== ' ') {
        length++;
        i--;
    }

    return length;
};
```

---

## Expected Interview Questions

1. **How do you handle multiple trailing spaces?**
   ➤ By using `rstrip()` or manually skipping trailing spaces.

2. **Can you solve this without using split()?**
   ➤ Yes, by traversing from the end of the string and counting non-space characters.

3. **What’s the time complexity?**
   ➤ O(n), where `n` is the length of the input string.

---


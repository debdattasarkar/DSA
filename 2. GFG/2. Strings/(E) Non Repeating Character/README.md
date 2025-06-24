Here is a README in Markdown format based on the content of the sixth uploaded image:

---

# Non-Repeating Character

## Introduction

The **Non-Repeating Character** problem is a straightforward string and hashing challenge. The goal is to identify the **first character** in a string that does **not repeat**. If all characters are repeating, a special character `'$',` should be returned.

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given a string `s` consisting of **lowercase English letters**, return the **first non-repeating character** in `s`.

* If there is **no non-repeating character**, return **'\$'**.
* Note: When you return `'$'`, the driver code will output `-1`.

---

## Examples

### Example 1

```
Input: s = "geeksforgeeks"  
Output: 'f'  
Explanation: 'f' is the first non-repeating character in the string.
```

### Example 2

```
Input: s = "racecar"  
Output: 'e'  
Explanation: 'e' is the only character that does not repeat.
```

### Example 3

```
Input: s = "aabbccc"  
Output: -1  
Explanation: All characters are repeating, so output is -1.
```

---

## Constraints

* `1 ≤ s.length ≤ 10^5`

---

## Expected Complexity

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(1)

---

## Tags

### Company Tags

`Flipkart`, `Amazon`, `Microsoft`, `D-E-Shaw`, `MakeMyTrip`, `Ola Cabs`, `Payu`, `Teradata`, `Goldman Sachs`, `MAQ Software`, `InfoEdge`, `OATS Systems`, `Tejas Network`

### Topic Tags

`Hash`, `Strings`, `Data Structures`

---

## Related Content

* **Article**: [Given A String Find Its First Non-Repeating Character](#)

---

Here is the **step-by-step explanation**, a **dry run**, and the **Python, C++, and JavaScript** implementations with inline comments.

---

## 🧠 Problem Explanation

Given a string `s` of lowercase English letters, find the **first non-repeating character** in it.
If **all characters are repeating**, return `'$',` which is interpreted as `-1` in the driver code.

---

## 🔍 Step-by-Step Logic

1. **Count the frequency** of each character using a hash map or array.
2. **Scan the string again** from left to right to find the **first character** with frequency = 1.
3. If no such character is found, return `'$'`.

---

## 🧪 Dry Run Example

Input: `"geeksforgeeks"`

### Step 1: Frequency Count

| Character | Frequency |
| --------- | --------- |
| g         | 2         |
| e         | 4         |
| k         | 2         |
| s         | 2         |
| f         | 1         |
| o         | 1         |
| r         | 1         |

### Step 2: Left to Right Check

* `'g'` → 2 → skip
* `'e'` → 4 → skip
* `'e'` → 4 → skip
* `'k'` → 2 → skip
* `'s'` → 2 → skip
* `'f'` → **1** → return `'f'`

---

## 🐍 Python Code

```python
class Solution:
    def nonRepeatingChar(self, s):
        # Step 1: Frequency dictionary
        freq = [0] * 26  # for 'a' to 'z'

        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Step 2: Find first character with frequency 1
        for char in s:
            if freq[ord(char) - ord('a')] == 1:
                return char

        return '$'  # No non-repeating character
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    char nonRepeatingChar(string &s) {
        // Step 1: Frequency array
        int freq[26] = {0};

        for (char c : s) {
            freq[c - 'a']++;
        }

        // Step 2: Scan for the first non-repeating character
        for (char c : s) {
            if (freq[c - 'a'] == 1) return c;
        }

        return '$';  // No non-repeating character
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    nonRepeatingChar(s) {
        // Step 1: Frequency map
        let freq = new Array(26).fill(0);

        for (let ch of s) {
            freq[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }

        // Step 2: Find first character with frequency 1
        for (let ch of s) {
            if (freq[ch.charCodeAt(0) - 'a'.charCodeAt(0)] === 1) {
                return ch;
            }
        }

        return '$';  // No non-repeating character
    }
}
```

---



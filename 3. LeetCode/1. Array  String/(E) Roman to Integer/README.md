
---

# 🏛️ 13. Roman to Integer

### 🟢 Difficulty: Easy

**Tags**: `Hash Table`, `Math`, `String`
**Asked By**: Multiple top companies

---

## 📘 Problem Statement

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

---

### 🧠 Notes on Roman Numerals

* Roman numerals are **generally written left to right**, from **largest to smallest**.
* However, if a **smaller numeral comes before a larger one**, it indicates **subtraction**.

---

### ✂️ Subtraction Rules

These 6 specific subtraction combinations are allowed:

* `I` can be placed before `V (5)` and `X (10)` → to make 4 and 9
* `X` can be placed before `L (50)` and `C (100)` → to make 40 and 90
* `C` can be placed before `D (500)` and `M (1000)` → to make 400 and 900

---

## 🎯 Goal

Given a valid Roman numeral string `s`, **convert it to an integer**.

---

## 🧪 Examples

### Example 1:

```
Input: s = "III"
Output: 3
Explanation: III = 1 + 1 + 1 = 3
```

### Example 2:

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3 → total = 58
```

### Example 3:

```
Input: s = "MCMXCIV"
Output: 1994
Explanation:
M = 1000, CM = 900, XC = 90, IV = 4 → total = 1994
```

---

## 📌 Constraints

* `1 <= s.length <= 15`
* `s` contains only these characters: `{'I', 'V', 'X', 'L', 'C', 'D', 'M'}`
* It is **guaranteed** that `s` is a valid Roman numeral in the range \[1, 3999]

---

## 💡 Hint

> The problem is simpler if you process the string **from right to left**, using a **map** of symbols to values.

---

Here's a full GeeksforGeeks-style explanation of **Leetcode 13 – Roman to Integer**, including:

* 🔍 Concept
* 🧪 Step-by-step dry run
* 🧠 Interview questions and answers
* ✅ Optimized code in Python, C++, and JavaScript with inline comments

---

## 🔍 Concept Explanation

Roman numerals are mostly **additive**, unless a **smaller symbol precedes a larger one**, in which case we **subtract** the smaller from the larger.

### ✅ Rule:

* **If `s[i] < s[i+1]`: subtract `s[i]`**
* **Else: add `s[i]`**

---

## 🧪 Step-by-Step Dry Run

### Input: `s = "MCMXCIV"`

| Char | Value | Operation                        | Total |
| ---- | ----- | -------------------------------- | ----- |
| M    | 1000  | Next is C (100), 100 < 1000 → +  | 1000  |
| C    | 100   | Next is M (1000), 100 < 1000 → - | 900   |
| M    | 1000  | Next is X (10), 10 < 1000 → +    | 1900  |
| X    | 10    | Next is C (100), 10 < 100 → -    | 1890  |
| C    | 100   | Next is I (1), 1 < 100 → +       | 1990  |
| I    | 1     | Next is V (5), 1 < 5 → -         | 1994  |

---

## 🧠 Interview Questions and Expected Answers

**Q1: What’s the main challenge with Roman numerals?**
🅰️ Identifying when to **subtract** (e.g., `IV` = 4) vs. add (e.g., `VI` = 6).

**Q2: Why loop from right to left (or left to right)?**
🅰️ Either works, but comparing the **current symbol against the next one** makes decisions simple.

**Q3: Can this be done in O(n) time?**
🅰️ Yes, using a hash map + a single pass loop.

---

## ✅ Python Code (Optimized)

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        # Traverse from right to left
        for ch in reversed(s):
            val = roman[ch]
            if val < prev:
                total -= val  # Subtract if smaller than next numeral
            else:
                total += val  # Add otherwise
            prev = val

        return total
```

---

## ✅ C++ Code

```cpp
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };

        int total = 0, prev = 0;

        // Traverse from right to left
        for (int i = s.length() - 1; i >= 0; --i) {
            int val = roman[s[i]];
            if (val < prev)
                total -= val;
            else
                total += val;
            prev = val;
        }

        return total;
    }
};
```

---

## ✅ JavaScript Code

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    };

    let total = 0, prev = 0;

    // Traverse from right to left
    for (let i = s.length - 1; i >= 0; i--) {
        let val = roman[s[i]];
        if (val < prev)
            total -= val;
        else
            total += val;
        prev = val;
    }

    return total;
};
```

---

## ✅ Summary

| Feature          | Value             |
| ---------------- | ----------------- |
| Time Complexity  | O(n)              |
| Space Complexity | O(1)              |
| Method Used      | Hash Map + Greedy |

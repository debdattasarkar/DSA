
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

Absolutely! Below are **interview questions** related to the `romanToInt()` function, along with **clear answers** and code references where applicable.

---

## ✅ Function Recap

The function:

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for ch in reversed(s):
            val = roman[ch]
            total += val if val >= prev else -val
            prev = val
        return total
```

---

## 🎯 Common Interview Questions & Answers

---

### 🔸 Q1: **What is the time and space complexity of your solution?**

**A**:

* **Time Complexity**: O(n), where n is the length of the input string.
* **Space Complexity**: O(1), since the mapping dictionary size is fixed (7 symbols).

---

### 🔸 Q2: **Why do you traverse the string from right to left?**

**A**:
Because Roman numerals subtract when a smaller numeral appears *before* a larger one (e.g., `IV` = 4).

* By traversing from **right to left**, we can check if the **current value** is less than the **previous one** (to the right).
* This allows us to easily subtract when needed without looking ahead.

---

### 🔸 Q3: **Can you implement the reverse — Integer to Roman?**

**A**: Yes, using a greedy subtraction approach:

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        val_sym = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = ""
        for val, sym in val_sym:
            while num >= val:
                res += sym
                num -= val
        return res
```

---

### 🔸 Q4: **Can you validate if a Roman numeral is valid?**

**A**:
Validation includes checking for:

* No more than 3 repetitions (`XXXX` is invalid)
* Subtractive patterns (`IL` is invalid, only `IV`, `IX`, `XL`, etc. are allowed)

**Idea**: Use regular expression or build a finite automaton.

---

### 🔸 Q5: **Can you do it without reversing the string?**

**A**:
Yes, using left-to-right traversal with a look-ahead:

```python
def romanToInt(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total
```

---

### 🔸 Q6: **What design changes would you make to support extended Roman numerals (> 3999)?**

**A**:
Introduce a way to handle overlined letters representing 1000× multiplier. For example:

* An overlined `V̄` = 5000
* Can be simulated using a `__` prefix (`__V`) or added in a mapping.

---

### 🔸 Q7: **Which DSA pattern does this problem follow?**

**A**:
Reverse traversal + comparison with previous element (similar to two-pointer or greedy pattern), optimized for Roman numeral rules.

---

### 🔸 Q8: **How would you test this function?**

**A**:
Test basic, subtractive, and edge cases:

```python
assert romanToInt("III") == 3
assert romanToInt("IV") == 4
assert romanToInt("IX") == 9
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994
assert romanToInt("MMMCMXCIX") == 3999
```

---

### 🔸 Q9: **What if the input is lowercase or invalid characters?**

**A**:
Enhance with input validation:

```python
if any(ch not in roman for ch in s.upper()):
    raise ValueError("Invalid Roman numeral")
```

---

### 🔸 Q10: **Can you make it object-oriented (OOP style)?**

**A**:

```python
class RomanConverter:
    def __init__(self):
        self.roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    def to_integer(self, s: str) -> int:
        total = 0
        prev = 0
        for ch in reversed(s):
            val = self.roman[ch]
            total += val if val >= prev else -val
            prev = val
        return total
```

---

Here’s a **Cheat Sheet** for the **Roman to Integer** DSA problem – perfect for interview revision:

---

# 🧠 Roman to Integer – Cheat Sheet

---

### ✅ Problem Statement

Convert a Roman numeral string `s` into its integer value.

---

### 🧩 Core Roman Mapping

```python
roman = {
  'I': 1, 'V': 5, 'X': 10, 'L': 50,
  'C': 100, 'D': 500, 'M': 1000
}
```

---

### 🔄 Optimal Logic (Reverse Traversal)

```python
def romanToInt(s: str) -> int:
    total, prev = 0, 0
    for ch in reversed(s):
        val = roman[ch]
        total += val if val >= prev else -val
        prev = val
    return total
```

⏱️ **Time**: O(n)
💾 **Space**: O(1)

---

### 📐 Pattern Used

* **Reverse traversal + running comparison**
  Similar to greedy logic — subtract when current < prev.

---

### ✅ Test Cases

| Roman       | Integer |
| ----------- | ------- |
| "III"       | 3       |
| "IV"        | 4       |
| "IX"        | 9       |
| "LVIII"     | 58      |
| "MCMXCIV"   | 1994    |
| "MMMCMXCIX" | 3999    |

---

### 💬 Interview Q\&A

| **Question**                         | **Answer**                                |
| ------------------------------------ | ----------------------------------------- |
| Time and space complexity?           | O(n), O(1)                                |
| Why reverse the string?              | Easier subtractive handling               |
| Can you do it L→R instead?           | Yes, using look-ahead                     |
| Reverse: Integer → Roman?            | Use greedy subtraction with symbol pairs  |
| Handle invalid input?                | Validate characters & order               |
| Extend for values > 3999?            | Add overline notation (e.g., 𝑉̄ = 5000)  |
| Pattern used?                        | Reverse traversal, greedy subtraction     |
| What about lowercase or mixed input? | `s = s.upper()` before loop               |
| How would you test it?               | Cover basic, subtractive, and edge inputs |
| Can you design it in OOP style?      | Yes, using a class like `RomanConverter`  |

---

### 🔁 Related Questions

* 🔁 Integer to Roman
* 🔁 Validate Roman numeral
* 🔁 String to Integer (atoi)
* 🔁 Expression evaluators (e.g., RPN)
* 🔁 Subarray sum problems (prefix-like logic)

---

### 🛠️ Tip for Interviews

* If the input is *always valid*, use reverse traversal.
* If not, **validate**:

  * Disallow repeated 4+ chars
  * Check invalid subtractive combos (`IC`, `IL`, etc.)

---

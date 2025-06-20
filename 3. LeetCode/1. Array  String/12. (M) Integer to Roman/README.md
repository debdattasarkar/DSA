
---

# 🔢 12. Integer to Roman

### 🟡 Difficulty: Medium

**Tags**: `Hash Table`, `Math`, `String`
**Asked By**: Top tech companies

---

## 📘 Problem Statement

Seven different symbols represent Roman numerals with the following values:

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

## 🧠 Rules for Roman Conversion

Roman numerals are formed by appending the conversion of decimal place values from highest to lowest.

### ✅ Rules:

* **If the value does not start with 4 or 9**:

  * Select the symbol of the **maximal value** that can be subtracted from the input.
  * Append that symbol to the result, subtract its value, and convert the remainder.

* **If the value starts with 4 or 9**:

  * Use the **subtractive form**, i.e., one symbol subtracted from the following symbol.
  * Examples:

    * 4 = IV (1 before 5)
    * 9 = IX (1 before 10)
    * 40 = XL
    * 90 = XC
    * 400 = CD
    * 900 = CM

* **Only powers of 10** (I, X, C, M) can be appended **at most 3 times consecutively**.

  * You **cannot** use `IIII` for 4 — instead, use `IV`.

---

## 🎯 Objective

Given an integer, convert it to a Roman numeral.

---

## 🧪 Examples

### Example 1:

```
Input: num = 3749
Output: "MMMDCCXLIX"

Explanation:
3000 = MMM
700  = DCC
 40  = XL
  9  = IX
```

> Note: 49 is **not** `IL` (50 - 1) because the conversion is based on **decimal places**.

---

### Example 2:

```
Input: num = 58
Output: "LVIII"

Explanation:
50 = L
 8 = VIII
```

---

### Example 3:

```
Input: num = 1994
Output: "MCMXCIV"

Explanation:
1000 = M  
 900 = CM  
  90 = XC  
   4 = IV
```

---

## 📌 Constraints

* `1 <= num <= 3999`

---

Here is a complete GeeksforGeeks-style solution breakdown for **Leetcode 12 – Integer to Roman**, including:

* ✅ Concept and step-by-step dry run
* 🤔 Expected interview questions & answers
* 🐍 Python, 💠 C++, and 🌐 JavaScript implementations with inline comments

---

## 🔍 Core Concept

To convert an integer to a Roman numeral:

* Use **greedy subtraction**, starting from the **largest Roman symbol**.
* Append the corresponding Roman symbol while subtracting its value from the number.
* Use **subtractive combinations** like `IV` for 4, `CM` for 900, etc.

---

## 🧪 Step-by-Step Dry Run

### Input: `num = 1994`

| Subtract | Roman | Remaining | Roman String |
| -------- | ----- | --------- | ------------ |
| 1000     | M     | 994       | M            |
| 900      | CM    | 94        | MCM          |
| 90       | XC    | 4         | MCMXC        |
| 4        | IV    | 0         | MCMXCIV      |

✅ Final Output: `"MCMXCIV"`

---

## 🤔 Interview Questions & Answers

**Q1:** How do you decide which Roman symbol to use?
🅰️ Use a **greedy strategy**: subtract the largest symbol possible and append it.

**Q2:** Why do we need subtractive combinations like `IV`?
🅰️ Roman numerals don’t repeat a symbol more than 3 times (e.g., `IIII` is invalid, use `IV` instead).

**Q3:** Can this be solved in O(1) time?
🅰️ Yes, because the input range is small and constant (`1 ≤ num ≤ 3999`).

---

## ✅ Python Code

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # List of tuples ordered from highest to lowest
        val_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"),
            (1, "I")
        ]

        roman = []

        for val, symbol in val_to_roman:
            # Append as many times as val fits into num
            while num >= val:
                roman.append(symbol)
                num -= val

        return ''.join(roman)
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    string intToRoman(int num) {
        vector<pair<int, string>> valToRoman = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"},  {90, "XC"},  {50, "L"},  {40, "XL"},
            {10, "X"},   {9, "IX"},   {5, "V"},   {4, "IV"},
            {1, "I"}
        };

        string roman;

        for (auto [val, sym] : valToRoman) {
            while (num >= val) {
                roman += sym;
                num -= val;
            }
        }

        return roman;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const valToRoman = [
        [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
        [100, "C"],  [90, "XC"],  [50, "L"],  [40, "XL"],
        [10, "X"],   [9, "IX"],   [5, "V"],   [4, "IV"],
        [1, "I"]
    ];

    let roman = "";

    for (const [val, sym] of valToRoman) {
        while (num >= val) {
            roman += sym;
            num -= val;
        }
    }

    return roman;
};
```

---

## ✅ Summary

| Metric           | Value                                   |
| ---------------- | --------------------------------------- |
| Time Complexity  | O(1) *(constant loop over 13 symbols)*  |
| Space Complexity | O(1)                                    |
| Strategy         | Greedy subtraction using fixed mappings |

---

Would you like a **diagram flowchart** for this conversion logic? Or a combined **bi-directional converter** (Roman ↔ Integer)?

Here is the full **README-style** explanation for **Leetcode Problem 6: Zigzag Conversion**, with detailed steps, examples, and code implementations in **Python**, **C++**, and **JavaScript**.

---

# 🧩 6. Zigzag Conversion

**Level:** Medium
**Topics:** String

---

## Problem Statement

The string `PAYPALISHIRING` is written in a zigzag pattern on a given number of rows like this (you may want to display this pattern in a fixed font for better legibility):

```
P   A   H   N  
A P L S I I G  
Y   I   R
```

Then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```cpp
string convert(string s, int numRows);
```

---

## 🧪 Examples

### Example 1:

**Input:**

```
s = "PAYPALISHIRING", numRows = 3
```

**Output:**

```
"PAHNAPLSIIGYIR"
```

### Example 2:

**Input:**

```
s = "PAYPALISHIRING", numRows = 4
```

**Output:**

```
"PINALSIGYAHRPI"
```

**Explanation:**

```
P     I    N  
A   L S  I G  
Y A   H R  
P     I
```

### Example 3:

**Input:**

```
s = "A", numRows = 1
```

**Output:**

```
"A"
```

---

## 📌 Constraints:

* `1 <= s.length <= 1000`
* `s` consists of English letters (lower-case and upper-case), `','`, and `'.'`.
* `1 <= numRows <= 1000`

---

## 📘 Approach

1. Use a list of strings, one for each row.
2. Traverse the input string while tracking:

   * The current row index.
   * A direction variable (down or up).
3. Append characters row by row in zigzag motion.
4. Finally, join all row strings into a single result.

---

## 🧮 Dry Run

**Input:** `"PAYPALISHIRING"`, `numRows = 3`

Traversal order (indexes show where each character goes):

```
Row 0: P     A     H     N       -> "PAHN"
Row 1: A   P L   S I   I G       -> "APLSIIG"
Row 2: Y     I     R             -> "YIR"
```

**Result = "PAHN" + "APLSIIG" + "YIR" = "PAHNAPLSIIGYIR"**

---

## ✅ Code Implementations

### 🐍 Python

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        for c in s:
            rows[cur_row] += c
            # Change direction if we're at top or bottom
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return ''.join(rows)
```

---

### 💠 C++

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) return s;

        vector<string> rows(numRows);
        int cur_row = 0;
        bool going_down = false;

        for (char c : s) {
            rows[cur_row] += c;
            if (cur_row == 0 || cur_row == numRows - 1)
                going_down = !going_down;
            cur_row += going_down ? 1 : -1;
        }

        string result;
        for (string row : rows)
            result += row;
        return result;
    }
};
```

---

### 🌐 JavaScript

```javascript
var convert = function(s, numRows) {
    if (numRows === 1 || numRows >= s.length) return s;

    let rows = new Array(numRows).fill('');
    let curRow = 0;
    let goingDown = false;

    for (let c of s) {
        rows[curRow] += c;
        if (curRow === 0 || curRow === numRows - 1)
            goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }

    return rows.join('');
};
```

---

## 💬 Interview Questions & Answers

**Q1. What is the time and space complexity of your approach?**

* Time: `O(n)` where `n` is the length of the string
* Space: `O(n)` to store rows

**Q2. Can we optimize further?**

* You could simulate the conversion directly during traversal without building rows, but it's more complex and not significantly better in practice.

**Q3. What if `numRows = 1`?**

* You should immediately return the input string, as no zigzag is needed.

**Q4. How would the pattern look for `numRows = 4`?**

```
P     I     N  
A   L S   I G  
Y A   H R      
P     I        
```

---

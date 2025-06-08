# 🔢 Sum-string

---

## 🧾 Problem Statement

Given a string `s` consisting of digits, determine whether it can be classified as a **sum-string**.

### 🔍 What is a sum-string?

A string that can be split into **more than two** non-empty substrings such that:

* The **rightmost substring** is equal to the **sum of the two substrings** immediately before it (interpreted as integers).
* This condition applies **recursively** to the entire string.
* None of the numbers (including the rightmost substring) may contain **leading zeroes**, **unless the number is exactly '0'**.

---

## 🧪 Examples

### Example 1:

```text
Input:  s = "12243660"
Output: true

Explanation: The string can be split as {"12", "24", "36", "60"}.
Each number is the sum of the two before it:
- 36 = 12 + 24
- 60 = 24 + 36  
Hence, it is a sum-string.
```

### Example 2:

```text
Input:  s = "1111112223"
Output: true

Explanation: Split as {"1", "111", "112", "223"}.
- 112 = 1 + 111
- 223 = 111 + 112
```

### Example 3:

```text
Input:  s = "123456"
Output: false

Explanation: No valid split satisfies the recursive sum-string condition.
```

---

## 📌 Constraints

* 1 ≤ `s.length` ≤ 100
* `s` contains only digits `'0'` to `'9'`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n³)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

* Nutanix

---

## 🏷️ Topic Tags

`Strings` `Recursion` `Backtracking` `Data Structures` `Algorithms`

---

## 📚 Related Articles

* [Check Given String Sum String – GeeksforGeeks](#)

---

Here’s a **step-by-step explanation and dry run** for the **Sum-string** problem, followed by implementations in **Python**, **C++**, and **JavaScript**, with **inline comments**.

---

## 🧠 Problem Summary

Given a string `s` consisting of digits, determine if it can be classified as a **sum-string**.

A **sum-string** satisfies:

* It can be split into at least **three** parts.
* Each part is the **sum** of the previous **two parts** (as integers).
* No leading zeroes are allowed (except for the number `'0'` itself).

---

## 🔁 Approach: Try all possible first two splits + recursion

### Steps:

1. Try all `i` and `j` such that:

   * First number = `s[0:i]`
   * Second number = `s[i:j]`
2. Recursively check whether the rest of the string satisfies the sum-string property using:

   ```
   sum = str(int(first) + int(second))
   check if s[j:].startswith(sum)
   ```

---

## 🧪 Dry Run Example

Input: `s = "12243660"`

Try:

* first = "12", second = "24"
* sum = 36 → check if next is "36"
* then check "24" + "36" = "60"
* ✅ all match, return true

---

## ✅ Python Code

```python
class Solution:
    def isSumString(self, s):
        # Helper to validate the recursive sum string from current first and second
        def isValid(first, second, rest):
            if not rest:
                return True
            sum_str = str(int(first) + int(second))
            if rest.startswith(sum_str):
                return isValid(second, sum_str, rest[len(sum_str):])
            return False

        n = len(s)
        for i in range(1, n):
            for j in range(i + 1, n):
                first = s[:i]
                second = s[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if isValid(first, second, s[j:]):
                    return True
        return False
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    bool isValid(string first, string second, string rest) {
        if (rest.empty()) return true;

        string sum = to_string(stoll(first) + stoll(second));
        if (rest.substr(0, sum.length()) == sum)
            return isValid(second, sum, rest.substr(sum.length()));
        return false;
    }

    bool isSumString(string &s) {
        int n = s.size();
        for (int i = 1; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                string first = s.substr(0, i);
                string second = s.substr(i, j - i);
                if ((first.size() > 1 && first[0] == '0') || (second.size() > 1 && second[0] == '0'))
                    continue;
                if (isValid(first, second, s.substr(j)))
                    return true;
            }
        }
        return false;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    isSumString(s) {
        const isValid = (first, second, rest) => {
            if (rest.length === 0) return true;
            const sum = (BigInt(first) + BigInt(second)).toString();
            if (rest.startsWith(sum)) {
                return isValid(second, sum, rest.slice(sum.length));
            }
            return false;
        };

        const n = s.length;
        for (let i = 1; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                const first = s.slice(0, i);
                const second = s.slice(i, j);
                if ((first.length > 1 && first[0] === '0') || (second.length > 1 && second[0] === '0'))
                    continue;
                if (isValid(first, second, s.slice(j))) return true;
            }
        }
        return false;
    }
}
```

---

## ⏱ Time & Space Complexity

| Metric           | Value                      |
| ---------------- | -------------------------- |
| Time Complexity  | O(n³)                      |
| Space Complexity | O(n) (for recursion depth) |

---

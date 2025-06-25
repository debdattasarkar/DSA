
---

# 125. Valid Palindrome

### Difficulty: Easy

### Topics: Two Pointers, String

### Companies: 🔒

---

## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

> **Alphanumeric** characters include **letters and numbers**.

---

### Task:

Given a string `s`, return `true` *if it is a palindrome*, or `false` otherwise.

---

## Examples

### Example 1:

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2:

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3:

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

---

## Constraints:

* `1 <= s.length <= 2 * 10^5`
* `s` consists only of **printable ASCII characters**

---

## Tags:

* Two Pointers
* String

---

Sure! Here's the full explanation, dry run, optimized code in **Python**, **C++**, and **JavaScript**, plus **interview Q\&A** for the Leetcode problem **125. Valid Palindrome**.

---

## ✅ 1. Text Explanation + Step-by-step Dry Run

### **Objective:**

Check whether a given string is a palindrome **after**:

* Converting uppercase to lowercase
* Removing all **non-alphanumeric** characters (spaces, punctuations, etc.)

### 🔁 Two-pointer Strategy:

* Use two pointers: one at the **start**, another at the **end**
* Move inward while skipping **non-alphanumeric** characters
* At each valid character, compare:

  * If characters don't match ⇒ not a palindrome
  * If characters match ⇒ continue
* If you reach or cross the middle ⇒ it's a palindrome

---

### 🧪 Dry Run:

#### Input: `"A man, a plan, a canal: Panama"`

After filtering:

```
Cleaned = "amanaplanacanalpanama"
```

Compare:

```
a == a ✅
m == m ✅
a == a ✅
n == n ✅
a == a ✅
p == p ✅
... continues ...
```

All characters match ⇒ ✅ `True`

---

## ✅ 2. Optimized Code in Python, C++, and JavaScript

---

### 🐍 Python

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (lowercased)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
```

---

### 💻 C++

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;

        while (left < right) {
            // Skip non-alphanumeric chars
            while (left < right && !isalnum(s[left])) left++;
            while (left < right && !isalnum(s[right])) right--;

            // Compare in lowercase
            if (tolower(s[left]) != tolower(s[right])) return false;

            left++;
            right--;
        }

        return true;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let left = 0, right = s.length - 1;

    while (left < right) {
        // Skip non-alphanumeric
        while (left < right && !/[a-zA-Z0-9]/.test(s[left])) left++;
        while (left < right && !/[a-zA-Z0-9]/.test(s[right])) right--;

        // Compare lowercase
        if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;

        left++;
        right--;
    }

    return true;
};
```

---

## ✅ 3. Expected Interview Questions & Answers

---

### ❓Q1: What is a palindrome?

**A:** A palindrome is a string that reads the same forward and backward. E.g., "madam", "racecar".

---

### ❓Q2: How do you check for a palindrome while ignoring punctuation and case?

**A:** Use two pointers starting from both ends. Skip non-alphanumeric characters and compare characters in lowercase.

---

### ❓Q3: What’s the time and space complexity?

* **Time:** `O(n)` where `n = len(s)`
* **Space:** `O(1)` if we don't build a filtered string. Otherwise, `O(n)` if we use a filtered string.

---

### ❓Q4: Why not just use regex to clean the string first?

**A:** That creates a new string (`O(n)` space). With two-pointer, we save space and improve efficiency in-place.

---

### ❓Q5: How does your code handle empty strings?

**A:** Empty strings or strings with only non-alphanumerics are treated as valid palindromes.

---


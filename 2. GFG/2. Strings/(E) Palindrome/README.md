
---

# Palindrome

**Difficulty:** Easy
**Accuracy:** 56.28%
**Submissions:** 105K+
**Points:** 2

---

## Problem Statement

You are given an integer `n`. Your task is to determine whether it is a palindrome.

> A number is considered a palindrome if it reads the same backward as forward, like the string examples `"MADAM"` or `"MOM"`.

---

## Examples

### Example 1:

**Input:**
`n = 555`
**Output:**
`true`
**Explanation:**
The number 555 reads the same backward as forward, so it is a palindrome.

---

### Example 2:

**Input:**
`n = 123`
**Output:**
`false`
**Explanation:**
The number 123 reads differently backward (321), so it is not a palindrome.

---

### Example 3:

**Input:**
`n = 1221`
**Output:**
`true`
**Explanation:**
1221 remains the same when reversed, hence it is a palindrome.

---

## Constraints

* $1 \leq n \leq 10^9$

---

## Expected Complexities

* **Time Complexity:** O(d), where d is the number of digits in `n`
* **Auxiliary Space:** O(1)

---

## Company Tags

* Zoho
* Samsung
* Oracle
* Adobe

---

## Topic Tags

* `palindrome`

---

## Related Articles

* [Check If A Number Is Palindrome](https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/)
* [C++ Program To Check Whether A Number Is Palindrome Or Not](https://www.geeksforgeeks.org/c-program-check-number-palindrome/)

---

## ✅ 1. Text Explanation with Step-by-Step Dry Run

### Problem:

Check if a number `n` is a **palindrome**, i.e., reads the same backward as forward.

### Idea:

Reverse the digits of the number and compare it to the original. If both are the same, it's a palindrome.

---

### 🧠 Step-by-Step Dry Run

#### Example:

Input: `n = 1221`
Original Number: `1221`

**Steps to reverse:**

* Initialize `rev = 0`, `num = 1221`
* Extract digit `1`: `rev = 0*10 + 1 = 1`
* Extract digit `2`: `rev = 1*10 + 2 = 12`
* Extract digit `2`: `rev = 12*10 + 2 = 122`
* Extract digit `1`: `rev = 122*10 + 1 = 1221`

Now, compare `rev` and `n` → both are `1221` → ✅ It's a palindrome.

#### Example 2:

Input: `n = 123`
Reverse = `321` → ❌ Not equal → Not a palindrome.

---

## ✅ 2. Code Implementations

---

### ✅ Python

```python
# User function Template for python3

class Solution:
    def isPalindrome(self, n):
        original = n
        rev = 0
        
        while n > 0:
            digit = n % 10           # Get last digit
            rev = rev * 10 + digit   # Append digit in reverse
            n //= 10                 # Remove last digit
        
        return rev == original       # Compare reversed with original
```

---

### ✅ C++

```cpp
// User function Template for C++

class Solution {
  public:
    bool isPalindrome(int n) {
        int original = n;
        int rev = 0;
        
        while (n > 0) {
            int digit = n % 10;         // Get last digit
            rev = rev * 10 + digit;     // Append to reverse
            n = n / 10;                 // Drop last digit
        }
        
        return rev == original;         // Compare with original
    }
};
```

---

### ✅ JavaScript

```javascript
// User function Template for javascript

/**
 * @param {number} n
 * @returns {boolean}
 */
class Solution {
    isPalindrome(n) {
        let original = n;
        let rev = 0;
        
        while (n > 0) {
            let digit = n % 10;
            rev = rev * 10 + digit;
            n = Math.floor(n / 10);
        }
        
        return rev === original;
    }
}
```

---

## ✅ 3. Interview Questions & Answers

### Q1. What is a palindrome number?

A number that reads the same forwards and backwards, e.g., `121`, `1221`.

### Q2. Can you solve it without converting the number to a string?

Yes. By reversing the digits mathematically and comparing with the original.

### Q3. What is the time and space complexity?

* **Time Complexity:** O(d), where d is the number of digits (log₁₀n)
* **Space Complexity:** O(1)

### Q4. What if the number is negative?

Negative numbers are **not** considered palindromes in this context.

### Q5. What are edge cases?

* Single-digit numbers → Always palindrome.
* Zero → Palindrome.
* Repeated digits like `1111` → Palindrome.
* Large number like `1000000001` → Palindrome.

---

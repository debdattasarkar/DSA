Let’s solve the classic **Palindrome Check** problem using the **Two Pointer Technique**.

---

## 🔍 Problem Statement

> Given a string `s`, determine if it is a **palindrome** — i.e., it reads the same forward and backward.
>
> Often asked:
>
> * Case-insensitive?
> * Ignore non-alphanumeric characters?

We’ll cover both **basic** and **extended** versions.

---

## ✅ Approach 1: Basic Palindrome Check

### 💡 Logic:

Use two pointers `left` and `right`, compare characters while moving inward.

---

## 🧑‍💻 Python Code (Basic)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
```

---

## ⏱ Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## ✅ Approach 2: Case-Insensitive & Ignore Non-Alphanumeric

> Leetcode [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

### 💡 Logic:

* Use `str.isalnum()` to skip non-alphanumeric
* Compare lowercase characters

---

## 🧑‍💻 Python Code (Extended Realistic Version)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

## 🧠 Dry Run Example

Input:

```python
s = "A man, a plan, a canal: Panama"
```

Filtered: `"amanaplanacanalpanama"` → same forward/backward ✅

---

## ❓ Interview Questions

| Question                                     | Answer                                        |
| -------------------------------------------- | --------------------------------------------- |
| Can you do it without using extra space?     | Yes, two-pointer in-place comparison          |
| Should you ignore punctuation and spaces?    | Clarify with interviewer. LC 125 ignores them |
| What if string has Unicode/emoji characters? | Clarify; may require `unicodedata.normalize`  |

---

## 🧪 Real-World Use Cases

* Detect **textual symmetry** in data entry or validation
* **DNA sequence** checks in bioinformatics
* **Log comparison** for pattern reversal or rollback scenarios
* Palindrome **URLs**, codes, or identifiers

---

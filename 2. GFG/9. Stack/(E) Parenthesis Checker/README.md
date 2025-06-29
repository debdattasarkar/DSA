
---

# 🧮 Parenthesis Checker

**Difficulty:** Easy
**Accuracy:** 28.56%
**Submissions:** 670K+
**Points:** 2

---

## 📝 Problem Statement

Given a string `s`, composed of different combinations of `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`, verify the validity of the arrangement.

An input string is **valid** if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

---

## 📌 Examples

### Example 1:

```
Input: s = "{({[]})}"
Output: true
Explanation: All the brackets are well-formed.
```

### Example 2:

```
Input: s = "[{()}]()"
Output: true
Explanation: All the brackets are well-formed.
```

### Example 3:

```
Input: s = "({["
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.
```

### Example 4:

```
Input: s = "({[})]"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
```

---

## ✅ Constraints:

* `1 ≤ s.size() ≤ 10^6`
* `s[i] ∈ {'{', '}', '(', ')', '[', ']'}`

---

## 💡 Expected Time and Space Complexity:

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft
* OYO Rooms
* Snapdeal
* Oracle
* Walmart
* Adobe
* Google
* Yatra.com

---

## 🏷️ Topic Tags

* Strings
* Stack
* STL
* Data Structures

---

## 🧠 Related Interview Experiences

* Oracle Interview Experience Set 45
* Walmart Labs Interview Set 3 For Senior Software Engineer
* Yatra Com Interview Experience Set 7

---

## 📚 Related Articles

* [Check For Balanced Parentheses In An Expression](https://www.geeksforgeeks.org/dsa/check-for-balanced-parentheses-in-an-expression/)

---


Sure! Let's break down the solution to the **Parenthesis Checker** problem step-by-step:

---

## ✅ 1. Text Explanation with Step-by-Step Dry Run

### 🔍 Goal:

To check whether the input string `s` has **balanced parentheses**.
We consider `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

### ✅ Validity Conditions:

* Every **opening** bracket must be **closed** by the same type of bracket.
* Brackets must be closed in the **correct order**.

### 💡 Key Insight:

Use a **stack** to keep track of open brackets. Push opening brackets onto the stack, and for every closing bracket, check if the top of the stack has the matching opening bracket.

---

### 🔄 Dry Run Example

#### Input: `s = "{[()]}"`

| Step | Character | Stack            | Action         |
| ---- | --------- | ---------------- | -------------- |
| 1    | `{`       | \[`{`]           | Push           |
| 2    | `[`       | \[`{`, `[`]      | Push           |
| 3    | `(`       | \[`{`, `[`, `(`] | Push           |
| 4    | `)`       | \[`{`, `[`]      | Match `(`, Pop |
| 5    | `]`       | \[`{`]           | Match `[`, Pop |
| 6    | `}`       | `[]` (empty)     | Match `{`, Pop |

✅ Output: **true**

#### Input: `s = "{[(])}"`

| Step | Character | Stack            | Action                   |
| ---- | --------- | ---------------- | ------------------------ |
| 1    | `{`       | \[`{`]           | Push                     |
| 2    | `[`       | \[`{`, `[`]      | Push                     |
| 3    | `(`       | \[`{`, `[`, `(`] | Push                     |
| 4    | `]`       | \[`{`, `[`, `(`] | ❌ Mismatch! Expected `)` |

❌ Output: **false**

---

## 💻 2. Code Implementations

---

### 🐍 Python

```python
class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False  # Mismatch or empty stack
                stack.pop()
            else:
                continue  # Ignore other characters if any

        return len(stack) == 0  # Stack should be empty if valid
```

---

### 💠 C++

```cpp
class Solution {
  public:
    bool isBalanced(string& s) {
        stack<char> st;
        unordered_map<char, char> matching = {{')', '('}, {'}', '{'}, {']', '['}};

        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else if (matching.count(ch)) {
                if (st.empty() || st.top() != matching[ch])
                    return false;
                st.pop();
            }
        }

        return st.empty();
    }
};
```

---

### 🌐 JavaScript

```javascript
class Solution {
    isBalanced(s) {
        const stack = [];
        const map = {')': '(', '}': '{', ']': '['};

        for (const char of s) {
            if (['(', '{', '['].includes(char)) {
                stack.push(char);
            } else if (map[char]) {
                if (stack.length === 0 || stack.pop() !== map[char]) {
                    return false;
                }
            }
        }

        return stack.length === 0;
    }
}
```

---

## 🎯 3. Expected Interview Questions & Answers

| Question                                                               | Answer                                                                                                         |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Q1. What data structure is used to solve this problem efficiently?** | A **stack** is used to keep track of opening brackets.                                                         |
| **Q2. What is the time and space complexity?**                         | **Time Complexity:** O(n), **Space Complexity:** O(n) (for stack)                                              |
| **Q3. Can this be done without using extra space?**                    | No, because we need to remember the order of opening brackets for matching.                                    |
| **Q4. What happens if the input contains other characters?**           | You can choose to skip them or return false, depending on the specification.                                   |
| **Q5. How do you handle early termination?**                           | If at any point a mismatch is found or the stack is empty when a closing bracket is encountered, return false. |

---

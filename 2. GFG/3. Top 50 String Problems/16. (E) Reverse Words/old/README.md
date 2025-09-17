
---

# Reverse Words

**Difficulty**: Easy
**Accuracy**: 56.08%
**Submissions**: 387K+
**Points**: 2
**Average Time**: 20m

---

## Problem Statement

Given a string `s`, reverse the string **without reversing its individual words**. Words are separated by spaces.

> 📝 **Note**:
> The string may contain leading or trailing spaces, or multiple spaces between two words.
> The returned string should only have a **single space separating the words**, and **no extra spaces** should be included.

---

## Examples

### Example 1:

**Input**:
`s = " i like this program very much "`
**Output**:
`"much very program this like i"`
**Explanation**:
After removing extra spaces and reversing the whole string (not individual words), the input string becomes `"much very program this like i"`.

---

### Example 2:

**Input**:
`s = " pqr mno "`
**Output**:
`"mno pqr"`
**Explanation**:
After removing extra spaces and reversing the whole string, the input string becomes `"mno pqr"`.

---

### Example 3:

**Input**:
`s = " a "`
**Output**:
`"a"`
**Explanation**:
The input string contains only one word with extra spaces around it. After removing the extra spaces, the output is `"a"`.

---

## Constraints

* 1 ≤ `s.size()` ≤ 10⁶
* String `s` contains only lowercase English alphabets and spaces.

---

## Expected Complexities

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(n)

---

## Company Tags

* Paytm
* Accolite
* Amazon
* Microsoft
* Samsung
* MakeMyTrip
* Goldman Sachs
* Adobe
* SAP Labs
* Cisco

---

## Topic Tags

* Strings
* Data Structures

---

## Related Interview Experiences

* Accolite Interview Experience Set 3 On Campus
* Paytm Interview Experience Set 6 Recruitment Drive
* Paytm Interview Experience Set 11 2 Years Experienced
* Makemytrip Interview Experience Set 6 Online Coding
* Samsung R D Bangalore Intern Interview Experience

---

## Related Articles

* Reverse Words In A Given String

---

Sure! Here's a complete breakdown of the **"Reverse Words in a String"** problem, including a **text explanation**, **dry run**, **Python, C++, and JavaScript codes**, and **interview-style questions and answers**.

---

## ✅ Problem Summary

You are given a string `s` that may contain:

* Words separated by spaces.
* Leading or trailing spaces.
* Multiple spaces between words.

Your task is to:

* **Reverse the order of words**.
* Remove **extra spaces**.
* Keep **only a single space between words**.

---

## 🧠 Step-by-Step Explanation

**Approach:**

1. **Trim extra spaces** (leading, trailing, and between words).
2. **Split the string** into words using space as a separator.
3. **Reverse the list of words**.
4. **Join them** with a single space.

---

## 🔍 Dry Run

Input: `"  i  like   this program  very   much  "`

**Step 1: Trim and Split**
Split into: `["i", "like", "this", "program", "very", "much"]`

**Step 2: Reverse**
Reversed: `["much", "very", "program", "this", "like", "i"]`

**Step 3: Join**
Result: `"much very program this like i"`

---

## 💻 Code Implementations

---

### ✅ Python Code

```python
# User function Template for python3

class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # Split the string into words and remove extra spaces
        words = s.strip().split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join with a single space
        return " ".join(reversed_words)
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    // Function to reverse words in a given string.
    string reverseWords(string &s) {
        vector<string> words;
        string word = "", result = "";

        for (char c : s) {
            if (c != ' ') {
                word += c;
            } else if (!word.empty()) {
                words.push_back(word);
                word = "";
            }
        }

        if (!word.empty()) words.push_back(word); // add last word

        // Reverse the words vector
        reverse(words.begin(), words.end());

        // Join them with space
        for (int i = 0; i < words.size(); ++i) {
            result += words[i];
            if (i != words.size() - 1)
                result += " ";
        }

        return result;
    }
};
```

---

### ✅ JavaScript Code

```javascript
// User function Template for javascript
/**
 * @param {string} s
 * @returns {string}
 */
class Solution {
    // Function to reverse words in a given string.
    reverseWords(s) {
        // Trim and split the string into words
        let words = s.trim().split(/\s+/);
        // Reverse the words
        words.reverse();
        // Join with single space
        return words.join(' ');
    }
}
```

---

## 👨‍💼 Interview Questions and Answers

### Q1: What is the time complexity of your solution?

**A:** O(n), where n is the length of the string. Each operation (trimming, splitting, reversing, and joining) takes linear time.

---

### Q2: How do you handle multiple spaces between words?

**A:** By using `split()` with regex in JS or `split()` in Python which ignores multiple spaces. In C++, we manually check for non-empty substrings.

---

### Q3: Why is trimming important in this problem?

**A:** To ensure there are no leading or trailing spaces in the final output and to avoid empty tokens.

---

### Q4: What is the auxiliary space used?

**A:** O(n), since we store the list of words separately before recombining.

---

### Q5: Can this be done in-place?

**A:** Yes, but it’s more complex. The in-place approach would require character-level swaps and careful word boundaries tracking—more error-prone and used only if space is constrained.

---

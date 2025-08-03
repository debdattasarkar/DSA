
---

# Case-specific Sorting of Strings

**Difficulty:** Medium
**Accuracy:** 69.88%
**Submissions:** 72K+
**Points:** 4
**Average Time:** 45m

---

## 🧠 Problem Statement

Given a string `s` consisting of **only uppercase and lowercase** characters, the task is to **sort uppercase and lowercase letters separately** such that if the *i*<sup>th</sup> place in the original string had an uppercase character, then it should **not** have a lowercase character after being sorted — and vice versa.

---

## 💡 Examples

### Example 1:

**Input:**
`s = "GEeKS"`

**Output:**
`EGekS`

**Explanation:**
Sorted form of given string with the same case of character will result in output as `EGekS`.

---

### Example 2:

**Input:**
`s = "XWMSPQ"`

**Output:**
`MPQSWX`

**Explanation:**
Since all characters are of the same case, we can simply perform a sorting operation on the entire string.

---

## 🔒 Constraints

* `1 ≤ s.length() ≤ 10⁵`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## 🏷 Tags

* Strings
* Sorting
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Case Specific Sorting Of Strings](https://www.geeksforgeeks.org/case-specific-sorting-of-strings/)

---
Sure! Here's the full breakdown of the **Case-specific Sorting of Strings** problem:

---

## ✅ Text Explanation

The string contains **both uppercase and lowercase letters**, and we must sort them **separately** but **preserve the original case positions**.

### ✳️ Goal:

Sort all uppercase characters together and all lowercase characters together, but place them in their original case positions.

---

### ✅ Step-by-Step Dry Run

**Input:** `"GEeKS"`
**Original Indices:** `G(0), E(1), e(2), K(3), S(4)`

1. Extract lowercase and uppercase:

   * Lowercase letters: `e`
   * Uppercase letters: `G, E, K, S`

2. Sort both groups:

   * Lowercase → `e`
   * Uppercase → `E, G, K, S`

3. Traverse the original string:

   * For each character, if it's uppercase, take next from sorted uppercase list.
   * If lowercase, take from sorted lowercase list.

4. Reconstruct result:

   * Position 0: uppercase → E
   * Position 1: uppercase → G
   * Position 2: lowercase → e
   * Position 3: uppercase → K
   * Position 4: uppercase → S

**Output:** `"EGekS"`

---

## 🧑‍💻 Python Code with Inline Comments

```python
class Solution:
    def caseSort(self, s):
        # Separate characters based on case
        upper = sorted([ch for ch in s if ch.isupper()])
        lower = sorted([ch for ch in s if ch.islower()])

        # Pointers for each list
        ui, li = 0, 0
        result = []

        for ch in s:
            if ch.isupper():
                result.append(upper[ui])
                ui += 1
            else:
                result.append(lower[li])
                li += 1

        return ''.join(result)
```

---

## 🧑‍💻 C++ Code with Inline Comments

```cpp
class Solution {
  public:
    string caseSort(string& s) {
        vector<char> upper, lower;

        // Separate characters by case
        for (char ch : s) {
            if (isupper(ch)) upper.push_back(ch);
            else lower.push_back(ch);
        }

        // Sort both
        sort(upper.begin(), upper.end());
        sort(lower.begin(), lower.end());

        int ui = 0, li = 0;
        string result = "";

        // Merge back respecting original case
        for (char ch : s) {
            if (isupper(ch)) result += upper[ui++];
            else result += lower[li++];
        }

        return result;
    }
};
```

---

## 🧑‍💻 JavaScript Code with Inline Comments

```javascript
class Solution {
    caseSort(s) {
        let upper = [];
        let lower = [];

        // Split by case
        for (let ch of s) {
            if (ch === ch.toUpperCase()) upper.push(ch);
            else lower.push(ch);
        }

        // Sort both arrays
        upper.sort();
        lower.sort();

        let result = '';
        let ui = 0, li = 0;

        for (let ch of s) {
            if (ch === ch.toUpperCase()) {
                result += upper[ui++];
            } else {
                result += lower[li++];
            }
        }

        return result;
    }
}
```

---

## 💬 Expected Interview Questions and Answers

### ❓ Q1: Why do we need to preserve the position of case in the string?

**Answer:**
The problem explicitly requires sorting **within cases**, not overall. The character at a position must **retain its original case** to ensure structure is maintained.

---

### ❓ Q2: What is the time complexity of your solution?

**Answer:**

* Splitting = O(n)
* Sorting = O(n log n)
* Merging = O(n)
  **Total:** `O(n log n)`

---

### ❓ Q3: Can this be done in O(n)?

**Answer:**
No, sorting inherently takes `O(n log n)` time. Since we must sort the characters of each case, this is optimal.

---

### ❓ Q4: What will happen if the input string contains non-letter characters?

**Answer:**
In the current solution, such characters will be ignored. If needed, we must explicitly handle/retain their positions.

---

### ❓ Q5: Can you explain the stability of your sorting?

**Answer:**
Yes. Since we sort each group (uppercase, lowercase) independently, and merge respecting the original structure, the stability of sorting is not violated.

---

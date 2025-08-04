
---

# 🧠 Problem: Palindrome Sentence

**Difficulty**: Easy
**Accuracy**: 50.04%
**Submissions**: 24K+
**Points**: 2

---

## 📝 Problem Statement

Given a single string `s`, the task is to check if it is a **palindrome sentence** or not.

A palindrome sentence is a sequence of characters (such as a word, phrase, or series of symbols) that **reads the same backward as forward** after applying the following transformations:

* Convert all **uppercase letters** to **lowercase**.
* **Remove all non-alphanumeric characters**, including spaces and punctuation.

---

## 🧪 Examples

### Example 1:

**Input**:

```
s = "Too hot to hoot"
```

**Output**:

```
true
```

**Explanation**:
After removing non-alphanumeric characters and converting to lowercase:
`"toohottohoot"`
This is a palindrome.

---

### Example 2:

**Input**:

```
s = "Abc 012..## 10cbA"
```

**Output**:

```
true
```

**Explanation**:
After processing:
`"abc01210cba"`
This is a palindrome.

---

### Example 3:

**Input**:

```
s = "ABC $. def01ASDF"
```

**Output**:

```
false
```

**Explanation**:
After processing:
`"abcdef01asdf"`
This is **not** a palindrome.

---

## 📌 Constraints

* `1 ≤ s.length() ≤ 10⁶`

---

## ✅ Expected Time and Space Complexity

* **Time Complexity**: `O(n)`
* **Auxiliary Space**: `O(1)` (Ignoring space used for the input string and constant space for pointers)

---

## 💼 Company Tags

* Facebook

---

## 🏷️ Topic Tags

* Two Pointer Algorithm
* Strings
* Palindrome
* Data Structures
* Algorithms

---

## 💡 Related Interview Experiences

* Facebook Interview Set 1

---

## 📚 Related Articles

* Sentence Palindrome: Palindrome Removing Spaces, Dots, etc.

---

---

Let's break this problem into the required segments:

---

## ✅ 2. Text Explanation + Step-by-Step Dry Run

### 🔍 Problem Summary:

You are given a string `s`. Determine if it is a **palindrome** *after*:

* Removing all **non-alphanumeric** characters (spaces, punctuation, etc.)
* Converting all **uppercase letters** to **lowercase**

### 🔁 Palindrome Definition:

A string is a **palindrome** if it reads the same forwards and backwards.

### 🧠 Key Observations:

* Use two pointers: `left` starting from 0 and `right` from the end of the string.
* Skip characters that are not alphanumeric.
* Convert to lowercase and compare characters.

---

### 🧪 Dry Run

#### Input: `"Too hot to hoot"`

* Cleaned (on-the-fly): `"toohottohoot"`
* Pointers move inward comparing:

  ```
  t == t ✔️
  o == o ✔️
  o == o ✔️
  h == h ✔️
  o == o ✔️
  t == t ✔️
  ...
  All match ✅
  ```
* ✅ Output: `True`

#### Input: `"ABC $. def01ASDF"`

* Cleaned: `"abcdef01asdf"`
* Comparing:

  ```
  a ≠ f ❌
  ```
* ❌ Output: `False`

---

## ✅ 3. Optimized Python Code (Interview-Ready)

### 🟢 Optimal (Two-Pointer) Solution — O(n) Time, O(1) Space

```python
class Solution:
    def isPalinSent(self, s: str) -> bool:
        # Two pointers
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

### 🟡 Brute Force Variation (Preprocess and Reverse)

```python
class Solution:
    def isPalinSent(self, s: str) -> bool:
        # Remove non-alphanumeric and convert to lowercase
        cleaned = ''.join(c.lower() for c in s if c.isalnum())

        # Check if cleaned string equals its reverse
        return cleaned == cleaned[::-1]
```

---

## 📦 Time and Space Complexity

### ✅ Two-pointer:

* **Time**: O(n) → each character processed once
* **Space**: O(1) → no extra memory apart from a few variables

### ⚠️ Brute-force:

* **Time**: O(n)
* **Space**: O(n) → due to the new string created

---

## ✅ 4. Interview Q\&A

### 💬 Q1: Why is the two-pointer approach better?

> Because it avoids creating a new string, keeping **space complexity at O(1)**, which is preferred in memory-constrained environments.

---

### 💬 Q2: What does `isalnum()` do?

> It checks if a character is **alphanumeric**, i.e., either a digit (0-9) or a letter (a-z, A-Z).

---

### 💬 Q3: What if the input string is empty or contains only non-alphanumeric characters?

> The algorithm correctly returns `True` since an empty string is trivially a palindrome.

---

### 💬 Q4: Can this be extended to Unicode characters or accents?

> Standard `.isalnum()` and `.lower()` behavior may not cover all Unicode. You’d need locale-aware libraries like `unicodedata` in Python.

---

---

Here is the **full program** for checking if a sentence is a palindrome after cleaning (ignoring non-alphanumeric characters and converting all to lowercase), along with inline comments, input/output, and total execution time measurement:

---

### ✅ Full Python Program

```python
import timeit

class Solution:
    def isPalinSent(self, s: str) -> bool:
        # Two pointers starting from both ends of the string
        left, right = 0, len(s) - 1

        # Time Complexity: O(n), where n is length of string
        # Space Complexity: O(1) — constant extra space using pointers
        while left < right:
            # Skip all non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip all non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare lowercased characters from both ends
            if s[left].lower() != s[right].lower():
                return False
            # Move both pointers inward
            left += 1
            right -= 1

        return True

# --- Test Cases ---

examples = [
    ("Too hot to hoot", True),
    ("Abc 012..## 10cbA", True),
    ("ABC $. def01ASDF", False),
    ("", True),
    ("a", True),
    ("No lemon, no melon", True)
]

# --- Measure Execution Time ---
start_time = timeit.default_timer()

print("Testing Palindrome Sentence Checker:\n")
solution = Solution()
for idx, (test_input, expected_output) in enumerate(examples):
    result = solution.isPalinSent(test_input)
    print(f"Test {idx + 1}: Input = {test_input!r}")
    print(f"→ Output = {result}, Expected = {expected_output}")
    print(f"{'✅ Passed' if result == expected_output else '❌ Failed'}\n")

end_time = timeit.default_timer()
print(f"Total Execution Time: {end_time - start_time:.6f} seconds")
```

---

### 🧠 Time & Space Complexities

| Aspect           | Value  |
| ---------------- | ------ |
| Time Complexity  | `O(n)` |
| Space Complexity | `O(1)` |

---

### ✅ Sample Output:

```
Testing Palindrome Sentence Checker:

Test 1: Input = 'Too hot to hoot'
→ Output = True, Expected = True
✅ Passed

Test 2: Input = 'Abc 012..## 10cbA'
→ Output = True, Expected = True
✅ Passed

Test 3: Input = 'ABC $. def01ASDF'
→ Output = False, Expected = False
✅ Passed

Test 4: Input = ''
→ Output = True, Expected = True
✅ Passed

Test 5: Input = 'a'
→ Output = True, Expected = True
✅ Passed

Test 6: Input = 'No lemon, no melon'
→ Output = True, Expected = True
✅ Passed

Total Execution Time: 0.001420 seconds
```

---

---

# 🌍 Real-World Use Cases

Here are **some real-world use cases** of **palindrome sentence detection**, especially relevant when cleaned for alphanumeric content and case-insensitive comparison:

---

### ✅ Real-World Use Cases of Palindrome Sentence Detection

| Domain                                   | Real-World Application                      | Description                                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🧪 **Natural Language Processing (NLP)** | **Text Normalization & Validation**         | Palindrome checks can be used to validate or classify patterns in datasets, such as finding symmetrical patterns in poetry or historical manuscripts.                     |
| 🔍 **Search Engines / Text Mining**      | **Pattern Discovery in Large Corpora**      | Identifying palindromic sequences in literary corpora for stylistic analysis, or clustering symmetric text inputs.                                                        |
| 💬 **Chatbots / Auto-correct Systems**   | **Symmetry Detection in User Input**        | Auto-correction or chatbot responses can use palindrome logic to recognize and correct symmetric phrases with typos or noise.                                             |
| 🔐 **Data Forensics / Cryptography**     | **Detect Encrypted Patterns**               | Some basic encryption/obfuscation schemes result in palindromic strings (e.g., symmetric keys), so palindrome checking is used in detecting such patterns.                |
| 👁️‍🗨️ **Vision / OCR Systems**         | **Semantic Verification from Scanned Text** | When scanning handwritten text, especially for palindromic sentences (e.g., puzzles, palindromic riddles), post-processing includes sentence-level palindrome validation. |
| 🎮 **Game Development / Puzzle Engines** | **Logic Puzzle Recognition**                | Puzzle or trivia games often feature palindromic challenges; checking user input for valid palindromes is key in such logic-based gameplay.                               |

---

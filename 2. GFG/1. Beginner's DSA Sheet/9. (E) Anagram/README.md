
---

# 🧩 Problem: Anagram

**Difficulty:** Easy
**Accuracy:** 44.93%
**Submissions:** 425K+
**Points:** 2
**Average Time:** 20m

---

## 📝 Problem Statement

Given two non-empty strings `s1` and `s2`, consisting only of lowercase English letters, determine whether they are **anagrams** of each other or not.

> Two strings are considered **anagrams** if they contain the **same characters** with exactly the **same frequencies**, regardless of their order.

---

## 📌 Examples

### Example 1

```
Input: s1 = "geeks", s2 = "keseg"
Output: true
Explanation: Both strings have same characters with same frequency. So, they are anagrams.
```

### Example 2

```
Input: s1 = "allergy", s2 = "allergyy"
Output: false
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. 
Since the frequency of characters differs, the strings are not anagrams.
```

### Example 3

```
Input: s1 = "listen", s2 = "lists"
Output: false
Explanation: The characters in the two strings are not the same — some are missing or extra. 
So, they are not anagrams.
```

---

## ✅ Constraints

* $1 \leq \text{s1.size()}, \text{s2.size()} \leq 10^5$
* `s1`, `s2` consist of **lowercase English letters** only.

---

## ⏱️ Expected Complexities

* **Time Complexity:** $O(n + m)$
* **Auxiliary Space:** $O(1)$ (i.e., fixed space for 26 lowercase letters)

---

## 🏢 Company Tags

`Flipkart`, `Directi`, `Adobe`, `Google`, `Nagarro`, `Media.net`

---

## 🧵 Topic Tags

* Strings
* Sorting
* Data Structures
* Algorithms

---

## 💼 Related Interview Experiences

* Directi Interview Experience Set 22 Pool Campus
* Adobe Interview Experience Shecodes Software Engineer
* Flipkart Interview Experience Set 19 SDET

---

## 📚 Related Articles

* [Check Whether Two Strings Are Anagram Of Each Other](https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/)

---

---

Let's proceed step-by-step for the **Anagram** problem.

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🔍 Goal:

Check if two strings `s1` and `s2` are **anagrams** — same characters with same frequency.

---

### 🧠 Approach:

We’ll use **frequency counting** via hash maps or fixed-size arrays (for lowercase letters) to compare character distributions.

---

### 🧪 Dry Run Example

#### Input:

```
s1 = "listen"
s2 = "silent"
```

#### Step-by-step:

1. Count frequency of each character in both strings:

   ```
   freq1 = {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
   freq2 = {'s':1, 'i':1, 'l':1, 'e':1, 'n':1, 't':1}
   ```

2. Compare both dictionaries:
   ✅ Both match → strings are anagrams → return `True`

---

### 🧪 Dry Run - Not an Anagram

#### Input:

```
s1 = "allergy"
s2 = "allergyy"
```

#### Step-by-step:

1. Frequencies:

   ```
   freq1 = {'a':1, 'l':2, 'e':1, 'r':1, 'g':1, 'y':1}
   freq2 = {'a':1, 'l':2, 'e':1, 'r':1, 'g':1, 'y':2}
   ```

2. 'y' count differs (1 vs 2) → ❌ Not anagram → return `False`

---

## ✅ 3. Optimized Codes in Python

### ✔️ Method 1: Using `collections.Counter`

```python
from collections import Counter

class Solution:
    def areAnagrams(self, s1, s2):
        # Time: O(n + m), Space: O(n + m)
        return Counter(s1) == Counter(s2)
```

### ✔️ Method 2: Using frequency array (best for lowercase-only)

```python
class Solution:
    def areAnagrams(self, s1, s2):
        # Early exit if lengths differ
        if len(s1) != len(s2):
            return False

        # Time: O(n), Space: O(1) since fixed size 26
        freq = [0] * 26  # For 'a' to 'z'

        for c1, c2 in zip(s1, s2):
            freq[ord(c1) - ord('a')] += 1
            freq[ord(c2) - ord('a')] -= 1

        return all(f == 0 for f in freq)
```

> ✅ This is most expected in interviews for space optimization.

---

## ✅ 4. Expected Interview Questions & Answers

### Q1. What’s the definition of an anagram?

**A:** Two strings that contain the same characters with the same frequency, in any order.

---

### Q2. Can we solve this in constant space?

**A:** Yes, since we know the input only contains lowercase letters (a-z), we can use a fixed-size array of size 26 — this gives **O(1)** auxiliary space.

---

### Q3. What is the best time complexity you can achieve?

**A:** The best achievable is **O(n)**, using character frequency array.

---

### Q4. What if the input had Unicode characters?

**A:** Then we'd use a dynamic dictionary or `collections.Counter`, which adjusts to any character set — but space would no longer be O(1).

---

### Q5. Why use `zip(s1, s2)` in the optimized version?

**A:** It efficiently pairs characters from both strings together, allowing us to update frequency deltas in a single loop instead of two.

---

---

Here is the **full working Python program** to check if two strings are anagrams, including:

* Inline comments
* Time and space complexity analysis
* Input/output samples
* Runtime measurement using `timeit`

---

### ✅ Python Code

```python
import timeit

class Solution:
    def areAnagrams(self, s1, s2):
        # Step 1: If lengths differ, they can't be anagrams
        if len(s1) != len(s2):
            return False

        # Step 2: Use frequency array for 26 lowercase English letters
        # Time Complexity: O(n), Space Complexity: O(1) (constant size)
        freq = [0] * 26
        
        # Step 3: Count frequencies
        for c1, c2 in zip(s1, s2):
            freq[ord(c1) - ord('a')] += 1
            freq[ord(c2) - ord('a')] -= 1

        # Step 4: Check if all frequencies are zero
        return all(f == 0 for f in freq)

# ---------------- Main program ----------------

def main():
    sol = Solution()
    
    # Test Case 1: Anagram
    s1 = "geeks"
    s2 = "keseg"
    print(f"Input: s1 = '{s1}', s2 = '{s2}'")
    print("Output:", sol.areAnagrams(s1, s2))  # Expected: True

    # Test Case 2: Not Anagram
    s1 = "listen"
    s2 = "liston"
    print(f"\nInput: s1 = '{s1}', s2 = '{s2}'")
    print("Output:", sol.areAnagrams(s1, s2))  # Expected: False

    # Test Case 3: Same characters, same frequency
    s1 = "aabbcc"
    s2 = "abcabc"
    print(f"\nInput: s1 = '{s1}', s2 = '{s2}'")
    print("Output:", sol.areAnagrams(s1, s2))  # Expected: True

# Measure total execution time
execution_time = timeit.timeit(main, number=1)
print(f"\nExecution Time: {execution_time:.6f} seconds")
```

---

### 🧠 Time and Space Complexity

| Operation | Complexity                        |
| --------- | --------------------------------- |
| Time      | O(n), where n = length of strings |
| Space     | O(1), fixed array of size 26      |

---

### ✅ Sample Output

```
Input: s1 = 'geeks', s2 = 'keseg'
Output: True

Input: s1 = 'listen', s2 = 'liston'
Output: False

Input: s1 = 'aabbcc', s2 = 'abcabc'
Output: True

Execution Time: 0.000966 seconds
```

---

---

# 🌍 Real-World Use Cases

Here are a few **very important real-world use cases** where **Anagram Checking** plays a critical role:

---

### ✅ 1. **Plagiarism Detection in Education / Research**

* **Use Case**: Detecting whether content has been reworded while maintaining the same structure.
* **Why Anagram-Like Matching**: Shuffling words, using synonyms, or rearranging sentences often preserves the word character frequency.
* **Example**: Comparing "listen" vs "silent" might help detect syntactic plagiarism or textual paraphrasing.

---

### ✅ 2. **Search Engines and Spell Correction**

* **Use Case**: Suggesting correct spellings or alternative search queries.
* **Why Anagram-Like Matching**: Algorithms like SymSpell or BK-trees use frequency/count-based logic (similar to anagram checks) to identify words with the same letters but in the wrong order.
* **Example**: User types “gogle” → Suggests “google”.

---

### ✅ 3. **Cryptography and Frequency Analysis**

* **Use Case**: Breaking classical ciphers like Caesar or Substitution ciphers.
* **Why Anagram-Like Matching**: Decrypted message may be a permutation (anagram) of another valid message or known phrase.
* **Example**: An attacker compares frequency of characters to a dictionary of anagrams.

---

### ✅ 4. **Natural Language Processing (NLP) - Text Normalization**

* **Use Case**: Canonicalizing input text before applying machine learning or clustering.
* **Why Anagram-Like Matching**: Ensures different forms of input (typos, shuffles, slang) are recognized as the same entity.
* **Example**: Matching “nodejs” with “jsnode” in a skills matcher.

---

### ✅ 5. **Cheating Detection in Exams / Games**

* **Use Case**: In games like word scramble or crosswords, you may want to detect if a user simply rearranged an existing word.
* **Why Anagram-Like Matching**: Detects if inputs are simply permutations of each other.
* **Example**: “beat” vs “beta” → cheating pattern detected.

---


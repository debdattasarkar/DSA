
---

### ✅ Full Python Program with Inline Comments

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Step 1: Split the input string `s` into a list of words
        words = s.split()

        # Time Complexity: O(n) where n is the number of characters in `s`
        # Space Complexity: O(k) where k is the number of words in `s`

        # Step 2: Check if the number of words and pattern length are equal
        if len(pattern) != len(words):
            return False  # Cannot form bijection if lengths mismatch

        # Step 3: Initialize two hash maps for bijective mapping
        char_to_word = {}  # Maps pattern char -> word
        word_to_char = {}  # Maps word -> pattern char

        # Step 4: Iterate through pattern and word list simultaneously
        for c, w in zip(pattern, words):
            # Check if `c` was already mapped
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False  # Inconsistent mapping
            else:
                char_to_word[c] = w  # Assign new mapping

            # Check if `w` was already mapped to a different char
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False  # Reverse mapping failed
            else:
                word_to_char[w] = c  # Assign reverse mapping

        # If we passed all checks, pattern matches the words
        return True
```

---

### 📊 Time and Space Complexity (Step-by-Step)

| Step                         | Time Complexity | Space Complexity | Explanation                            |
| ---------------------------- | --------------- | ---------------- | -------------------------------------- |
| `s.split()`                  | O(n)            | O(k)             | Splits the input string `s` into words |
| `len(pattern) != len(words)` | O(1)            | O(1)             | Simple length check                    |
| Loop over zip(pattern, s)    | O(m)            | O(m)             | m = len(pattern), builds two hash maps |
| Final return                 | O(1)            | O(1)             | Result decision                        |

* **Total Time:** `O(n + m)` (n = len(s), m = len(pattern))
* **Total Space:** `O(m)` (in worst case all mappings are unique)

---

### 🔢 Sample Inputs & Outputs

#### ✅ Test Case 1

```python
pattern = "abba"
s = "dog cat cat dog"
# Output: True
```

Explanation:

* `a → dog`, `b → cat` → consistent and bijective

#### ❌ Test Case 2

```python
pattern = "abba"
s = "dog cat cat fish"
# Output: False
```

Explanation:

* Last word "fish" breaks the bijection

#### ❌ Test Case 3

```python
pattern = "aaaa"
s = "dog cat cat dog"
# Output: False
```

Explanation:

* `a` mapped to both "dog" and "cat" → invalid

---

### 💡 Real-World Use Cases

* Token classification or parsing with structure
* Sentence template validation
* Syntax pattern enforcement in DSLs

---

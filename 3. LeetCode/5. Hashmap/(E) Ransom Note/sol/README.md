
---

## ✅ Python Full Program: `canConstruct`

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Count frequency of each character in magazine
        # Time: O(m), where m = len(magazine)
        # Space: O(1) since at most 26 lowercase letters (constant)
        magazine_count = Counter(magazine)
        
        # Step 2: For each character in ransomNote, check if it's available in magazine_count
        # Time: O(n), where n = len(ransomNote)
        # Space: O(1) for the loop, no extra data structure created
        for char in ransomNote:
            if magazine_count[char] == 0:
                # Char either not present or already used up
                return False
            magazine_count[char] -= 1  # Use one instance of the character
        
        # If we got here, all characters were available
        return True
```

---

## 🔍 Time and Space Complexity

| Step                      | Time Complexity           | Space Complexity               |
| ------------------------- | ------------------------- | ------------------------------ |
| Build `Counter(magazine)` | O(m), m = len(magazine)   | O(1) (max 26 chars)            |
| Iterate `ransomNote`      | O(n), n = len(ransomNote) | O(1)                           |
| **Overall**               | **O(m + n)**              | **O(1)** (fixed-size alphabet) |

> ✅ Space is O(1) because even though we use a `Counter`, it stores at most 26 lowercase letters.

---

## 🧪 Sample Inputs and Outputs

### Example 1

```python
ransomNote = "a"
magazine = "b"
# Explanation: 'a' is not in 'b'
# Output: False
```

### Example 2

```python
ransomNote = "aa"
magazine = "ab"
# 'a' is available only once in magazine
# Output: False
```

### Example 3

```python
ransomNote = "aa"
magazine = "aab"
# 'a' occurs twice in magazine, 'aa' can be built
# Output: True
```

---

## ✅ Test the Program

You can run the following:

```python
# Test code
sol = Solution()
print(sol.canConstruct("a", "b"))        # False
print(sol.canConstruct("aa", "ab"))      # False
print(sol.canConstruct("aa", "aab"))     # True
print(sol.canConstruct("abc", "cbaabc")) # True
print(sol.canConstruct("aabbcc", "abc")) # False
```

---

Here is the **optimized version** of the `canConstruct` problem using a **fixed-size array instead of `collections.Counter`**, ideal for lowercase English letters (`'a'` to `'z'`):

---

# ✅ Python Program: Using Array Instead of `Counter`

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Create a list of size 26 to count letters in magazine
        # Each index corresponds to a letter from 'a' to 'z'
        # Time: O(m), where m = len(magazine)
        # Space: O(1), since fixed 26 slots regardless of input size
        letter_count = [0] * 26
        
        for char in magazine:
            index = ord(char) - ord('a')  # Map 'a'-'z' to 0-25
            letter_count[index] += 1
        
        # Step 2: Check if ransomNote can be formed
        # Time: O(n), where n = len(ransomNote)
        for char in ransomNote:
            index = ord(char) - ord('a')
            if letter_count[index] == 0:
                return False  # Not enough characters available
            letter_count[index] -= 1  # Use one occurrence
        
        return True  # All characters matched
```

---

## 🔍 Time and Space Complexity

| Step                   | Time         | Space    |
| ---------------------- | ------------ | -------- |
| Count magazine chars   | O(m)         | O(1)     |
| Check ransomNote chars | O(n)         | O(1)     |
| **Total**              | **O(m + n)** | **O(1)** |

> ✅ Space is still O(1) because we’re only ever using 26 slots, regardless of input size.

---

## 🧪 Sample Inputs and Expected Outputs

```python
sol = Solution()

print(sol.canConstruct("a", "b"))        # False
print(sol.canConstruct("aa", "ab"))      # False
print(sol.canConstruct("aa", "aab"))     # True
print(sol.canConstruct("abc", "aabbcc")) # True
print(sol.canConstruct("abcd", "abc"))   # False
```

---

## ✅ Why Use Array?

* 🔄 Faster than `Counter` for known alphabets
* 🧠 Lower memory usage (only 26 ints)
* ⚡ Ideal when only lowercase letters are involved (as per problem constraints)


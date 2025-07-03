
---

### ✅ Full Python Program: `isAnagram`

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input example
        # s = "anagram", t = "nagaram"
        
        # Step 1: If strings are of different lengths, they can't be anagrams.
        # Time Complexity: O(1), Space: O(1)
        if len(s) != len(t):
            return False

        # Step 2: Count character frequencies in both strings
        # Time Complexity: O(n), where n is the length of the strings
        # Space Complexity: O(1) (bounded to 26 lowercase letters)
        s_count = Counter(s)  # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        t_count = Counter(t)  # {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

        # Step 3: Compare the two frequency dictionaries
        # Time Complexity: O(1), since max 26 keys (lowercase)
        return s_count == t_count
```

---

### 📌 Input & Output

**Input:**

```python
s = "anagram"
t = "nagaram"
```

**Output:**

```python
True
```

---

### 🧠 Time and Space Complexity Summary

| Step                  | Time Complexity | Space Complexity | Explanation                                 |
| --------------------- | --------------- | ---------------- | ------------------------------------------- |
| Length check          | O(1)            | O(1)             | Constant time check                         |
| Frequency counting    | O(n)            | O(1)             | Linear scan, space fixed to 26 characters   |
| Dictionary comparison | O(1)            | O(1)             | Comparison over max 26 lowercase characters |
| **Total**             | **O(n)**        | **O(1)**         | Efficient for large inputs                  |

---

# Fixed-Size Arrays

Here is an optimized version of the **Valid Anagram** solution using **fixed-size arrays instead of `Counter`**, which is slightly more efficient when the input contains only lowercase English letters.

---

### ✅ Full Python Program Using Arrays (for lowercase letters only)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if lengths are different; if so, can't be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Initialize frequency arrays of size 26 for a-z
        freq_s = [0] * 26
        freq_t = [0] * 26

        # Step 3: Count frequency of each letter in both strings
        for i in range(len(s)):
            # ord('a') = 97, so subtracting gives index 0-25
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1

        # Step 4: Compare frequency arrays
        return freq_s == freq_t
```

---

### 📌 Input & Output

```python
s = "anagram"
t = "nagaram"
Output: True

s = "rat"
t = "car"
Output: False
```

---

### 🧠 Time and Space Complexity

| Step                 | Time Complexity | Space Complexity | Explanation                               |
| -------------------- | --------------- | ---------------- | ----------------------------------------- |
| Length check         | O(1)            | O(1)             | Simple length comparison                  |
| Frequency count loop | O(n)            | O(1)             | Count using fixed 26-length arrays        |
| Array comparison     | O(1)            | O(1)             | Always comparing two 26-length arrays     |
| **Total**            | **O(n)**        | **O(1)**         | Most efficient for lowercase English only |

---

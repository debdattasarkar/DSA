
---

# 📄 383. Ransom Note

## 💬 Problem Statement

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

> **Note**:
> Each letter in `magazine` **can only be used once** in `ransomNote`.

---

## 🧪 Examples

### Example 1:

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

### Example 2:

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 3:

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

---

## 🔒 Constraints

* `1 <= ransomNote.length, magazine.length <= 10⁵`
* `ransomNote` and `magazine` consist of **lowercase English letters**

---

## 📘 Topics

* Hash Table
* String
* Counting

---

## 🧠 Explanation

We need to **check if each character in `ransomNote`** exists in `magazine`, **and** the number of times it appears in `ransomNote` should be **less than or equal to** the number of times it appears in `magazine`.

---

## 🧮 Dry Run (Step-by-step)

### Input:

```
ransomNote = "aa"
magazine = "aab"
```

### Step 1: Count magazine letters

```
'a': 2
'b': 1
```

### Step 2: Try to build ransomNote

* 1st 'a': found → use 1 → remaining 'a': 1
* 2nd 'a': found → use 1 → remaining 'a': 0
  ✅ SUCCESS → All characters matched

**Return** `true`

---

## ✅ Python Solution

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each letter in magazine
        magazine_count = Counter(magazine)
        
        # Check if each character in ransomNote can be satisfied by magazine
        for char in ransomNote:
            if magazine_count[char] == 0:
                return False  # Not enough of 'char' in magazine
            magazine_count[char] -= 1
        
        return True
```

---

## ✅ C++ Solution

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> freq(26, 0); // Frequency array for 'a' to 'z'
        
        for (char ch : magazine) {
            freq[ch - 'a']++;
        }

        for (char ch : ransomNote) {
            if (freq[ch - 'a'] == 0) return false; // No more left
            freq[ch - 'a']--;
        }

        return true;
    }
};
```

---

## ✅ JavaScript Solution

```javascript
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let freq = new Array(26).fill(0);

    for (let ch of magazine) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    for (let ch of ransomNote) {
        let idx = ch.charCodeAt(0) - 97;
        if (freq[idx] === 0) return false;
        freq[idx]--;
    }

    return true;
};
```

---

## 🎯 Interview Q\&A

### Q1: Why use a hash table or frequency array?

**A:** It allows constant time lookups and updates, which makes the solution efficient (O(n)).

---

### Q2: What is the time and space complexity?

* **Time**: O(m + n), where `m` = length of `magazine`, `n` = length of `ransomNote`
* **Space**: O(1) since we only store 26 lowercase English letters

---

### Q3: Can we use sorting for this problem?

**A:** Technically yes, but sorting is O(n log n) and unnecessary when a simple counting method works faster and is more readable.

---

### Q4: What happens if magazine has enough letters but not in order?

**A:** Order does not matter. Only the **frequency** of characters matters.

---

### Q5: Is the algorithm in-place?

**A:** No, we use auxiliary space (a fixed-size array or Counter) to track character counts.

---

# HashMap approach

The **HashMap approach** is the most efficient and intuitive way to solve the **Ransom Note** problem, where we simply count the number of characters needed and verify that the magazine has at least as many.

---

### ✅ Problem Recap:

> You are given two strings:
>
> * `ransomNote`: the string we want to construct
> * `magazine`: the string we use letters from

**Each letter in `magazine` can be used only once.**
We return `True` if we can construct `ransomNote` from `magazine`; otherwise, `False`.

---

### ✅ HashMap Approach Explanation:

We:

1. Count the frequency of each character in `magazine` using a hash map.
2. Iterate through each character in `ransomNote`.

   * For each character, **check if it exists in the magazine’s frequency map** and **has a non-zero count**.
   * If yes, **decrement the count** (use it).
   * If not, return `False` early.
3. If all characters can be matched, return `True`.

---

### ✅ Step-by-step Dry Run

**Input:**
`ransomNote = "aab"`
`magazine = "baa"`

**Magazine Frequency Map:**
`{'b': 1, 'a': 2}`

Now check each char in `ransomNote`:

* `'a'` → yes, freq 2 → decrement → freq = 1
* `'a'` → yes, freq 1 → decrement → freq = 0
* `'b'` → yes, freq 1 → decrement → freq = 0
  ✅ All matched → return `True`

---

## ✅ Code Implementations

### 🐍 Python

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)  # Step 1: count chars in magazine
        
        for char in ransomNote:        # Step 2: for every char in ransomNote
            if mag_count[char] == 0:   # If char is missing or used up
                return False
            mag_count[char] -= 1       # Use the char
        return True
```

---

### 💻 C++

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> count;
        for (char c : magazine) count[c]++;  // Count characters in magazine

        for (char c : ransomNote) {
            if (count[c] == 0) return false; // Not enough of this character
            count[c]--;                      // Use it
        }
        return true;
    }
};
```

---

### 🌐 JavaScript

```javascript
var canConstruct = function(ransomNote, magazine) {
    const count = {}; // hash map to count magazine characters
    
    for (let char of magazine) {
        count[char] = (count[char] || 0) + 1;
    }

    for (let char of ransomNote) {
        if (!count[char]) return false; // char missing or used up
        count[char]--;                  // use the char
    }

    return true;
};
```

---

### 💬 Interview Questions & Answers

| Question                                     | Good Answer                                                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Q1. What's the time complexity?**          | O(n + m) where `n` = len(ransomNote), `m` = len(magazine)                                                     |
| **Q2. Why do you use a hash map?**           | It allows constant-time lookups and decrements for frequency checking.                                        |
| **Q3. Can you do this without extra space?** | Yes, if the character set is fixed (like lowercase letters), we can use an array of size 26 instead of a map. |
| **Q4. Can magazine letters be reused?**      | No, each letter can be used at most once, so we decrement the count.                                          |
| **Q5. What edge cases would you test?**      | ransomNote longer than magazine, ransomNote has chars not in magazine, both strings empty                     |

---

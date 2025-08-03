
---

# ✅ Problem: Check if Frequencies Can Be Equal

**Difficulty**: Medium
**Accuracy**: 16.67%
**Submissions**: 126K+
**Points**: 4

---

## 🧠 Problem Statement

Given a string `s` consisting **only of lowercase alphabetic characters**, check whether it is possible to remove **at most one character** such that the **frequency of each distinct character** in the string becomes **the same**.

* Return **`true`** if it is possible,
* Otherwise, return **`false`**.

---

## 🔍 Examples

### Example 1:

```
Input: s = "xyyz"
Output: true
Explanation: Removing one 'y' will make frequency of each distinct character to be 1.
```

### Example 2:

```
Input: s = "xyyzz"
Output: true
Explanation: Removing one 'x' will make frequency of each distinct character to be 2.
```

### Example 3:

```
Input: s = "xxxxyyzz"
Output: false
Explanation: Frequency cannot be made same by removing at most one character.
```

---

## ✅ Constraints:

* $1 \leq \text{s.size()} \leq 10^5$

---

## ⏱ Expected Time and Space Complexity:

* **Time Complexity**: $O(n)$
* **Auxiliary Space**: $O(1)$

---

## 🏢 Company Tags:

* Zoho

---

## 🏷 Topic Tags:

* Hash
* Strings
* Data Structures

---

## 📘 Related Articles:

* **Check If Frequency Of All Characters Can Become Same By One Removal**

---

Here is the **complete solution** to the problem **"Check if Frequencies Can Be Equal"**, including:

---

### ✅ 1. **Text Explanation with Step-by-Step Dry Run**

#### 🔍 Problem Understanding:

We are given a string `s` of lowercase English letters. We need to determine if it is possible to **remove at most one character** from `s` so that **all remaining characters have the same frequency**.

---

### 💡 **Approach:**

1. Count the frequency of each character.
2. Count how many times each **frequency** occurs using another hashmap.
3. Based on these frequency patterns, check if:

   * All characters already have the same frequency.
   * Only one character has a frequency different by 1 (and it occurs only once).
   * Only one character occurs once and can be removed.

---

### 🔁 **Dry Run Example 1**:

```
Input: "xyyzz"

Char Frequency:
x → 1
y → 2
z → 2

Now frequency of frequencies:
{1: 1, 2: 2}

=> Remove one 'x' → frequencies become {2: 2}
✅ All characters have equal frequency
Return: True
```

---

### 🔁 **Dry Run Example 2**:

```
Input: "xxxxyyzz"

Frequencies:
x → 4
y → 2
z → 2

Frequency of frequencies:
{4: 1, 2: 2}

Not possible to fix with one removal.
Return: False
```

---

## ✅ 2. Python, C++, and JavaScript Implementations

---

### 🐍 Python Code:

```python
from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        # Step 1: Count frequency of each character
        freq = Counter(s)
        
        # Step 2: Count frequencies of these frequencies
        freq_count = Counter(freq.values())
        
        # If all frequencies are same
        if len(freq_count) == 1:
            return True
        
        # If there are exactly 2 different frequencies
        if len(freq_count) == 2:
            keys = list(freq_count.keys())
            f1, f2 = keys[0], keys[1]
            
            # Check if one of them occurs once and is either 1 or one more than the other
            if (freq_count[f1] == 1 and (f1 - 1 == f2 or f1 == 1)):
                return True
            if (freq_count[f2] == 1 and (f2 - 1 == f1 or f2 == 1)):
                return True
        
        return False
```

---

### 💠 C++ Code:

```cpp
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
  public:
    bool sameFreq(string& s) {
        unordered_map<char, int> freq;
        for (char c : s)
            freq[c]++;

        unordered_map<int, int> countFreq;
        for (auto& [ch, f] : freq)
            countFreq[f]++;

        if (countFreq.size() == 1) return true;

        if (countFreq.size() == 2) {
            auto it = countFreq.begin();
            int f1 = it->first, c1 = it->second;
            ++it;
            int f2 = it->first, c2 = it->second;

            if ((c1 == 1 && (f1 == 1 || f1 - 1 == f2)) ||
                (c2 == 1 && (f2 == 1 || f2 - 1 == f1)))
                return true;
        }
        return false;
    }
};
```

---

### 🌐 JavaScript Code:

```javascript
class Solution {
    sameFreq(s) {
        const freq = {};
        for (let ch of s)
            freq[ch] = (freq[ch] || 0) + 1;

        const countFreq = {};
        for (let val of Object.values(freq))
            countFreq[val] = (countFreq[val] || 0) + 1;

        const keys = Object.keys(countFreq).map(Number);
        if (keys.length === 1) return true;

        if (keys.length === 2) {
            const [f1, f2] = keys;
            const c1 = countFreq[f1], c2 = countFreq[f2];

            if ((c1 === 1 && (f1 === 1 || f1 - 1 === f2)) ||
                (c2 === 1 && (f2 === 1 || f2 - 1 === f1)))
                return true;
        }
        return false;
    }
}
```

---

## 🧪 3. Interview Questions and Mock Answers

### ❓Q1: How do you approach a frequency-based problem?

**A**: I first count character frequencies using a hash map. Then I analyze the pattern of frequency counts — whether they are all same or if we can adjust by removing one character.

---

### ❓Q2: Can you explain the time and space complexity of your solution?

**A**:

* **Time Complexity**: O(n), where n is the length of the string.
* **Space Complexity**: O(1) – we use fixed-size hash maps since characters are only lowercase alphabets.

---

### ❓Q3: Why do we check the frequency of frequencies?

**A**: Because we want all characters to appear the same number of times. If we can reduce one character or one frequency to match the rest, then it's a valid transformation.

---

### ❓Q4: What if the input is an empty string?

**A**: The problem guarantees that the string has at least one character (`1 <= s.size()`). If not, we can return `true` or `false` based on specifications.

---

Here is the **visual dry run** for the input `s = "xyyzz"` for the problem: **"Check if frequencies can be equal by removing at most one character."**

### Explanation of the Visuals:

#### 📊 Chart 1: Character Frequencies

* **x → 1 time**
* **y → 2 times**
* **z → 2 times**

This gives a frequency dictionary:
`{'x': 1, 'y': 2, 'z': 2}`

#### 📊 Chart 2: Frequency of Frequencies

* **1 appears once** → one character has frequency 1 (x)
* **2 appears twice** → two characters have frequency 2 (y and z)

---

### 👣 Step-by-step Dry Run

**Goal:** Can we remove at most 1 character and make all remaining characters have the same frequency?

1. Current frequencies: \[1, 2, 2]
2. Remove one `'x'` → we’re left with \[2, 2]
3. ✅ All frequencies are equal ⇒ Return `True`.

---

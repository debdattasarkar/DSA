
---

# 3. Longest Substring Without Repeating Characters

**Difficulty**: Medium
**Topics**: Hash Table, String, Sliding Window
**Companies**: 💼

---

## Problem

Given a string `s`, find the length of the **longest substring** without **duplicate characters**.

---

## Examples

### Example 1:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence, not a substring.
```

---

## Constraints

* `0 <= s.length <= 5 * 10⁴`
* `s` consists of English letters, digits, symbols and spaces.

---

## Tags

`Hash Table` `String` `Sliding Window`

---

Here's a complete breakdown for **LeetCode Problem 3: Longest Substring Without Repeating Characters**, covering:

---

## ✅ 1. Text Explanation + Step-by-Step Dry Run

### **Problem Statement**

You're given a string `s`. You need to find the length of the **longest substring** that contains **no repeated characters**.

---

### 🔍 **Approach: Sliding Window + Hash Set (Optimized O(n))**

We maintain a **window** with two pointers:

* `left`: start of the window
* `right`: end of the window

We slide the window while keeping track of the **unique characters** in a set. When a character is repeated, we shrink the window from the left.

---

### 🧪 Dry Run:

```
s = "abcabcbb"
Set = {}
left = 0, right = 0, maxLength = 0

Step-by-step:
1. right=0, char='a' → not in set → add → Set={'a'}, max=1
2. right=1, char='b' → add → Set={'a','b'}, max=2
3. right=2, char='c' → add → Set={'a','b','c'}, max=3
4. right=3, char='a' → 'a' is duplicate
    - remove s[left]='a' → left=1
    - add 'a' again → Set={'b','c','a'}
5. right=4, char='b' → duplicate → remove 'b' → left=2 → Set={'c','a'} → add 'b'
6. right=5, char='c' → duplicate → remove 'c' → left=3 → Set={'a','b'} → add 'c'
7. right=6, char='b' → duplicate → remove 'a'→left=4 → 'b' still in set → remove 'b'→left=5 → add 'b'
8. right=7, char='b' → duplicate → remove 'c'→left=6→remove 'b'→left=7→add 'b'

✅ Final max length = 3
```

---

## ✅ 2. Python / C++ / JavaScript Implementations

### 🔹 Python

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1  # shrink from left
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)  # update max
        return max_len
```

---

### 🔹 C++

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int left = 0, max_len = 0;

        for (int right = 0; right < s.length(); ++right) {
            while (seen.count(s[right])) {
                seen.erase(s[left]);
                left++;
            }
            seen.insert(s[right]);
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};
```

---

### 🔹 JavaScript

```javascript
var lengthOfLongestSubstring = function(s) {
    let seen = new Set();
    let left = 0, maxLen = 0;

    for (let right = 0; right < s.length; right++) {
        while (seen.has(s[right])) {
            seen.delete(s[left]);
            left++;
        }
        seen.add(s[right]);
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
};
```

---

## ✅ 3. Interview Q\&A

### 🔸Q1: What is the time complexity of your solution?

* **O(n)**: Each character is visited at most twice.

---

### 🔸Q2: Why do we use a Set?

* To keep track of characters in the current substring and allow **O(1)** lookup and removal.

---

### 🔸Q3: Can you do this in-place or with constant space?

* No. Because we must remember which characters were seen, so **O(k)** space is needed (k = alphabet size).

---

### 🔸Q4: What changes if we’re asked for the actual substring?

* We can store the best start and end indices and slice `s[start:end+1]` at the end.

---

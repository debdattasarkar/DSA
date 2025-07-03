
---

# 🧵 Longest Substring with K Uniques

### Difficulty: Medium

**Accuracy:** 34.65%
**Submissions:** 201K+
**Points:** 4

---

## 📄 Problem Statement

You are given a string `s` consisting only of lowercase alphabets and an integer `k`.
Your task is to **find the length of the longest substring** that contains **exactly `k` distinct characters**.

---

> **Note:** If no such substring exists, return **-1**.

---

## 📌 Examples

### Example 1:

```
Input:
s = "aabacbebebe", k = 3

Output:
7

Explanation:
The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
```

---

### Example 2:

```
Input:
s = "aaaa", k = 2

Output:
-1

Explanation:
There's no substring with 2 distinct characters.
```

---

### Example 3:

```
Input:
s = "aabaaab", k = 2

Output:
7

Explanation:
The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
```

---

## 🧠 Constraints

* 1 ≤ s.size() ≤ 10⁵
* 1 ≤ k ≤ 26

---

## 📈 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Tags

**Companies:**
Amazon, Google, SAP Labs

**Topics:**

* two-pointer-algorithm
* Hash
* Strings
* Map
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Find The Longest Substring With K Unique Characters In A Given String](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/)

---

### ✅ Step-by-step Explanation + Dry Run

We are given a string `s` and an integer `k`. We must **find the length of the longest substring** that contains **exactly `k` distinct characters**.

---

### 🎯 Approach (Sliding Window + Hash Map)

We use the **sliding window** technique:

* Expand the window using a `right` pointer.
* Use a hash map (`char_freq`) to count the frequency of characters in the current window.
* If number of unique characters in the window exceeds `k`, shrink the window from the `left`.
* If it equals `k`, update `max_len`.

---

### 🔁 Dry Run (Example: `s = "aabacbebebe"`, `k = 3`)

| Left | Right | Window    | Unique Chars | Max Length  |
| ---- | ----- | --------- | ------------ | ----------- |
| 0    | 0     | `a`       | 1            | -           |
| 0    | 1     | `aa`      | 1            | -           |
| 0    | 2     | `aab`     | 2            | -           |
| 0    | 3     | `aaba`    | 2            | -           |
| 0    | 4     | `aabac`   | 3 ✅          | **5**       |
| 0    | 5     | `aabacb`  | 3 ✅          | **6**       |
| 0    | 6     | `aabacbe` | 4 ❌          | Shrink left |
| 1    | 6     | `abacbe`  | 4 ❌          | Shrink left |
| 2    | 6     | `bacbe`   | 4 ❌          | Shrink left |
| 3    | 6     | `acbe`    | 4 ❌          | Shrink left |
| 4    | 6     | `cbe`     | 3 ✅          | **6**       |
| 4    | 7     | `cbeb`    | 3 ✅          | **6**       |
| 4    | 8     | `cbebe`   | 3 ✅          | **6**       |
| 4    | 9     | `cbebeb`  | 3 ✅          | **6**       |
| 4    | 10    | `cbebebe` | 3 ✅          | **7** ✅     |

### Final Answer: **7**

---

## 🧠 Optimized Code (Sliding Window + Hash Map)

---

### 🐍 Python

```python
class Solution:
    def longestKSubstr(self, s, k):
        from collections import defaultdict
        n = len(s)
        left = 0
        max_len = -1
        char_freq = defaultdict(int)

        for right in range(n):
            char_freq[s[right]] += 1

            # Shrink window if more than k distinct characters
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1

            # If exactly k distinct, update max_len
            if len(char_freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
```

---

### 💠 C++

```cpp
class Solution {
  public:
    int longestKSubstr(string &s, int k) {
        unordered_map<char, int> freq;
        int left = 0, max_len = -1;

        for (int right = 0; right < s.length(); right++) {
            freq[s[right]]++;

            // Shrink window if more than k distinct chars
            while (freq.size() > k) {
                freq[s[left]]--;
                if (freq[s[left]] == 0)
                    freq.erase(s[left]);
                left++;
            }

            // Update max_len if window has exactly k unique chars
            if (freq.size() == k)
                max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};
```

---

### 🌐 JavaScript

```javascript
class Solution {
    longestKSubstr(s, k) {
        let left = 0, maxLen = -1;
        const freq = new Map();

        for (let right = 0; right < s.length; right++) {
            const char = s[right];
            freq.set(char, (freq.get(char) || 0) + 1);

            // Shrink if too many unique chars
            while (freq.size > k) {
                const leftChar = s[left];
                freq.set(leftChar, freq.get(leftChar) - 1);
                if (freq.get(leftChar) === 0)
                    freq.delete(leftChar);
                left++;
            }

            if (freq.size === k) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }

        return maxLen;
    }
}
```

---

## ❓ Interview Questions and Answers

### Q1: What is the optimal time and space complexity of this solution?

**A:**

* Time: **O(n)**
* Space: **O(k)**, for storing at most `k` characters in hash map.

---

### Q2: Why do we use a sliding window here?

**A:**
The sliding window allows us to dynamically adjust the substring while ensuring the number of distinct characters stays within the required count.

---

### Q3: What happens if no substring contains `k` unique characters?

**A:**
We return `-1` as specified in the problem.

---

### Q4: Why is a Hash Map preferred over a Set?

**A:**
A hash map lets us **track character frequencies** and cleanly delete characters whose count drops to 0—essential for shrinking the window efficiently.

---

### Q5: Can we solve this using brute-force?

**A:**
Yes, but it would be **O(n²)** or **O(n³)** depending on how substrings are generated and evaluated, which is not optimal for large strings.

---

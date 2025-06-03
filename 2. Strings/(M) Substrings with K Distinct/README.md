# Substrings with K Distinct

## 🧩 Problem Statement

Given a string consisting of lowercase characters and an integer `k`, the task is to count all possible **substrings** (not necessarily distinct) that have **exactly k distinct characters**.

---

## 🧪 Examples

### Example 1

**Input:**

```
s = "abc", k = 2
```

**Output:**

```
2
```

**Explanation:**
Substrings with exactly 2 distinct characters: `["ab", "bc"]`.

---

### Example 2

**Input:**

```
s = "aba", k = 2
```

**Output:**

```
3
```

**Explanation:**
Substrings with exactly 2 distinct characters: `["ab", "ba", "aba"]`.

---

### Example 3

**Input:**

```
s = "aa", k = 1
```

**Output:**

```
3
```

**Explanation:**
Substrings with exactly 1 distinct character: `["a", "a", "aa"]`.

---

## 🧠 Constraints

* `1 ≤ s.size() ≤ 10^6`
* `1 ≤ k ≤ 26`

---

## ⏱️ Expected Time and Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1) (constant space for character frequency assuming lowercase English letters)

---

## 🚀 Approach

We count the number of substrings with **at most k** distinct characters and subtract the number of substrings with **at most (k - 1)** distinct characters:

```text
# of substrings with exactly k distinct characters =
    substrings_with_at_most(k) - substrings_with_at_most(k - 1)
```

This can be implemented using a **sliding window** and a **hash map** (or array) to track character frequencies.

---

## 🐍 Python Code

```python
class Solution:
    def substrCount(self, s, k):
        def atMostK(s, k):
            count = [0] * 26
            i = 0
            res = 0
            distinct = 0

            for j in range(len(s)):
                if count[ord(s[j]) - ord('a')] == 0:
                    distinct += 1
                count[ord(s[j]) - ord('a')] += 1

                while distinct > k:
                    count[ord(s[i]) - ord('a')] -= 1
                    if count[ord(s[i]) - ord('a')] == 0:
                        distinct -= 1
                    i += 1

                res += j - i + 1

            return res

        return atMostK(s, k) - atMostK(s, k - 1)
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    int substrCount(string s, int k) {
        auto atMostK = [&](int k) {
            vector<int> freq(26, 0);
            int i = 0, res = 0, distinct = 0;

            for (int j = 0; j < s.length(); ++j) {
                if (freq[s[j] - 'a'] == 0)
                    ++distinct;
                ++freq[s[j] - 'a'];

                while (distinct > k) {
                    --freq[s[i] - 'a'];
                    if (freq[s[i] - 'a'] == 0)
                        --distinct;
                    ++i;
                }

                res += j - i + 1;
            }

            return res;
        };

        return atMostK(k) - atMostK(k - 1);
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    substrCount(s, k) {
        function atMostK(s, k) {
            let freq = Array(26).fill(0);
            let i = 0, res = 0, distinct = 0;

            for (let j = 0; j < s.length; ++j) {
                if (freq[s.charCodeAt(j) - 97] === 0) distinct++;
                freq[s.charCodeAt(j) - 97]++;

                while (distinct > k) {
                    freq[s.charCodeAt(i) - 97]--;
                    if (freq[s.charCodeAt(i) - 97] === 0) distinct--;
                    i++;
                }

                res += j - i + 1;
            }

            return res;
        }

        return atMostK(s, k) - atMostK(s, k - 1);
    }
}
```

---

## 🏷️ Tags

* Sliding Window
* Two-Pointer Algorithm
* Strings
* Hash Map
* Dynamic Programming

---

## 🏢 Company Tags

* D-E Shaw

---

## 📚 Related Articles

* [Count Number Of Substrings With Exactly K Distinct Characters](https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/)

---

Here’s a complete explanation with a step-by-step dry run for the **“Substrings with K Distinct”** problem from GeeksforGeeks, followed by implementations in **Python**, **C++**, and **JavaScript** with inline comments.

---

## 📘 Problem Summary

Given a string `s` and an integer `k`, your task is to count the number of substrings with **exactly `k` distinct characters**.

---

## 🔍 Step-by-Step Dry Run

### Input:

```text
s = "aba", k = 2
```

### Goal:

Find substrings with **exactly** 2 **distinct** characters.

### All substrings:

```
"a", "ab", "aba", "b", "ba", "a"
```

### Now filter those with exactly 2 distinct characters:

* "ab" → ✅
* "aba" → ✅
* "ba" → ✅

**Answer:** 3 substrings.

---

## 🧠 Key Insight

### Trick:

Number of substrings with **exactly k** distinct characters =
**Number of substrings with at most k** distinct characters - **Number of substrings with at most (k - 1)** distinct characters.

---

## 🐍 Python Code

```python
class Solution:
    def countSubstr(self, s, k):
        # Helper function to count substrings with at most k distinct chars
        def atMostK(s, k):
            count = [0] * 26  # For lowercase a-z
            left = 0
            result = 0
            distinct = 0

            for right in range(len(s)):
                if count[ord(s[right]) - ord('a')] == 0:
                    distinct += 1
                count[ord(s[right]) - ord('a')] += 1

                # Shrink window if more than k distinct characters
                while distinct > k:
                    count[ord(s[left]) - ord('a')] -= 1
                    if count[ord(s[left]) - ord('a')] == 0:
                        distinct -= 1
                    left += 1

                # Add all substrings ending at right
                result += right - left + 1
            return result

        return atMostK(s, k) - atMostK(s, k - 1)
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    int countSubstr(string& s, int k) {
        auto atMostK = [&](int k) {
            vector<int> freq(26, 0);
            int left = 0, result = 0, distinct = 0;

            for (int right = 0; right < s.size(); ++right) {
                if (freq[s[right] - 'a'] == 0) distinct++;
                freq[s[right] - 'a']++;

                while (distinct > k) {
                    freq[s[left] - 'a']--;
                    if (freq[s[left] - 'a'] == 0) distinct--;
                    left++;
                }
                result += right - left + 1;
            }
            return result;
        };

        return atMostK(k) - atMostK(k - 1);
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    countSubstr(s, k) {
        const atMostK = (s, k) => {
            let count = new Array(26).fill(0);
            let left = 0, result = 0, distinct = 0;

            for (let right = 0; right < s.length; right++) {
                let index = s.charCodeAt(right) - 97;
                if (count[index] === 0) distinct++;
                count[index]++;

                while (distinct > k) {
                    let leftIndex = s.charCodeAt(left) - 97;
                    count[leftIndex]--;
                    if (count[leftIndex] === 0) distinct--;
                    left++;
                }

                result += right - left + 1;
            }
            return result;
        };

        return atMostK(s, k) - atMostK(s, k - 1);
    }
}
```

---

## 🧠 Time & Space Complexity

* **Time Complexity:** O(n) — each character is processed at most twice.
* **Space Complexity:** O(1) — fixed array for 26 lowercase characters.

---


---

# 30. Substring with Concatenation of All Words

**Difficulty:** Hard
**Topics:** Hash Table, String, Sliding Window
**Companies:** 🔥

---

You are given a string `s` and an array of strings `words`. All the strings of `words` **are of the same length**.

A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

* For example, if `words = ["ab","cd","ef"]`, then

  * `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all valid concatenated strings.
  * But `"acdbef"` is **not** a concatenated string because it is not the concatenation of **any permutation** of `words`.

---

Return an array of the **starting indices** of **all** the concatenated substrings in `s`.
You can return the answer in **any order**.

---

### Example 1:

```
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]

Explanation:
- The substring starting at 0 is "barfoo", which is a permutation of ["bar", "foo"]
- The substring starting at 9 is "foobar", which is a permutation of ["foo", "bar"]
```

---

### Example 2:

```
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Explanation:
- There is no concatenated substring.
```

---

### Example 3:

```
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Explanation:
- The substring starting at 6 is "foobarthe", which is a permutation of ["foo","bar","the"]
- The substring starting at 9 is "barthefoo", which is a permutation of ["bar","the","foo"]
- The substring starting at 12 is "thefoobar", which is a permutation of ["the","foo","bar"]
```

---

### Constraints:

* `1 <= s.length <= 10⁴`
* `1 <= words.length <= 5000`
* `1 <= words[i].length <= 30`
* `s` and `words[i]` consist of lowercase English letters.

---

### Tags:

`Hash Table` `String` `Sliding Window`

Here's a complete breakdown and optimized solution for **Leetcode 30: Substring with Concatenation of All Words**, including dry run, Python/C++/JavaScript code, and likely interview questions with answers.

---

## ✅ 1. Explanation

### Problem Summary:

You are given a string `s` and a list of words `words` (all the same length). You need to find all **starting indices** in `s` where the substring is a **concatenation of each word exactly once**, in any order.

---

### 🔍 Key Observations:

* All words are the same length: `word_len`
* Total window size to check: `window_len = word_len * len(words)`
* You must compare each substring of length `window_len` to see if it’s a permutation of all words in the list.

---

### 💡 Approach (Sliding Window + HashMap):

1. **Preprocess:** Use a hashmap to count word frequencies in `words`.
2. Slide a window of `window_len` across `s`.
3. For each window, check if the current substring can be split into valid words by comparing frequencies.
4. Use multiple offsets from `0` to `word_len - 1` to handle alignment properly.

---

### 🧮 Dry Run Example:

Input:

```python
s = "barfoothefoobarman", words = ["foo", "bar"]
```

* Each word has length = 3, so total window length = 6
* Valid substrings:

  * s\[0:6] = "barfoo" ✅ → \[0]
  * s\[9:15] = "foobar" ✅ → \[9]

Output: `[0, 9]`

---

## ✅ 2. Optimized Code in All Languages

---

### 🔹 Python

```python
from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []

        for i in range(word_len):  # offset to cover different alignments
            left = i
            curr_count = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = j + word_len

        return res
```

---

### 🔹 C++

```cpp
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (s.empty() || words.empty()) return {};

        int word_len = words[0].length();
        int total_len = word_len * words.size();
        unordered_map<string, int> word_count;
        for (const string& w : words) word_count[w]++;

        vector<int> res;
        for (int i = 0; i < word_len; ++i) {
            unordered_map<string, int> curr_count;
            int left = i, count = 0;
            for (int j = i; j + word_len <= s.length(); j += word_len) {
                string word = s.substr(j, word_len);
                if (word_count.count(word)) {
                    curr_count[word]++;
                    count++;
                    while (curr_count[word] > word_count[word]) {
                        string left_word = s.substr(left, word_len);
                        curr_count[left_word]--;
                        left += word_len;
                        count--;
                    }
                    if (count == words.size()) res.push_back(left);
                } else {
                    curr_count.clear();
                    count = 0;
                    left = j + word_len;
                }
            }
        }
        return res;
    }
};
```

---

### 🔹 JavaScript

```javascript
var findSubstring = function(s, words) {
    if (!s || words.length === 0) return [];

    const wordLen = words[0].length;
    const totalLen = wordLen * words.length;
    const wordCount = {};
    const res = [];

    for (const word of words)
        wordCount[word] = (wordCount[word] || 0) + 1;

    for (let i = 0; i < wordLen; i++) {
        let left = i, count = 0;
        const currCount = {};

        for (let j = i; j + wordLen <= s.length; j += wordLen) {
            const word = s.slice(j, j + wordLen);
            if (wordCount[word] !== undefined) {
                currCount[word] = (currCount[word] || 0) + 1;
                count++;

                while (currCount[word] > wordCount[word]) {
                    const leftWord = s.slice(left, left + wordLen);
                    currCount[leftWord]--;
                    left += wordLen;
                    count--;
                }

                if (count === words.length) res.push(left);
            } else {
                currCount = {};
                count = 0;
                left = j + wordLen;
            }
        }
    }

    return res;
};
```

---

## ✅ 3. Interview Questions & Answers

---

### 💬 Q1: Why do we use multiple starting offsets (0 to word\_len - 1)?

**A:** To handle cases where concatenated words don't start exactly at index 0. This helps catch alignments that might be missed if we only checked one position.

---

### 💬 Q2: What is the time complexity?

**A:**

* Preprocessing: O(m) where m is the number of words.
* Main Loop: O(n \* word\_len), where `n = len(s)`, due to nested sliding windows.

Overall: **O(n)** for small `word_len`.

---

### 💬 Q3: Can this be solved using a Trie?

**A:** Yes, but not efficiently for this problem. Trie is helpful when you want prefix-based matching. Here, we're matching **exact words** of fixed length.

---

### 💬 Q4: What if words have different lengths?

**A:** This specific algorithm assumes equal word lengths. If they differ, we cannot apply this fixed-size window and need a different strategy, likely backtracking or regex-based.

---


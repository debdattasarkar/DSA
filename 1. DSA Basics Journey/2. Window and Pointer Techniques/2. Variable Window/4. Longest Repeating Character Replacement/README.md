Let’s explore **Leetcode 424 – Longest Repeating Character Replacement**, a popular **Variable Sliding Window** problem that focuses on **character frequency and allowed replacements**.

---

## 🔍 Problem Statement

> You are given a string `s` and an integer `k`.
> You can choose **any character** of the string and **change it to any other uppercase English character** at most `k` times.
> Return the length of the **longest substring** containing the same letter you can get **after performing at most `k` replacements**.

---

### 🧪 Example:

```python
Input: s = "AABABBA", k = 1  
Output: 4  
Explanation: Replace the second 'A' with 'B' → "AABBBBA" → max substring = "BBBB"
```

---

## ✅ Core Idea: Variable Sliding Window + Frequency

We want to **maintain a window** where:

* We can make **at most `k` replacements**
* Replacement count = `window size - max frequency char in window`
* If `replacements_needed > k`, shrink the window from the left

---

## 🧑‍💻 Python Code (Efficient, Interview-Ready)

```python
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            # If we need to replace more than k chars, shrink window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
```

---

## 🔍 Key Insight

* We don’t need to **recalculate `max_freq`** when shrinking the window.

  * It’s okay if `max_freq` is a bit stale because the window size will still shrink properly to satisfy the condition.
  * This gives **O(n)** time.

---

## ⏱ Time and Space Complexity

| Metric | Value        |
| ------ | ------------ |
| Time   | O(n)         |
| Space  | O(26) = O(1) |

---

## 🧠 Dry Run Example

### Input:

```python
s = "AABABBA", k = 1
```

Track: `freq`, `left`, `right`, `max_freq`, and `window size`

| Step            | Right | Char | max\_freq | Window Size | Replacements | Valid? | MaxLen |
| --------------- | ----- | ---- | --------- | ----------- | ------------ | ------ | ------ |
| 0               | 0     | A    | 1         | 1           | 0            | ✅      | 1      |
| 1               | 1     | A    | 2         | 2           | 0            | ✅      | 2      |
| 2               | 2     | B    | 2         | 3           | 1            | ✅      | 3      |
| 3               | 3     | A    | 3         | 4           | 1            | ✅      | 4      |
| 4               | 4     | B    | 3         | 5           | 2            | ❌      | --     |
| shrink → left=1 |       |      |           | 4           | 1            | ✅      | 4      |
| 5               | 5     | B    | 3         | 5           | 2            | ❌      | --     |
| shrink → left=2 |       |      |           | 4           | 1            | ✅      | 4      |
| 6               | 6     | A    | 3         | 5           | 2            | ❌      | --     |

✅ Final Answer: `4`

---

## ❓ Interview-Focused Questions

| Question                                                 | Answer                                                         |
| -------------------------------------------------------- | -------------------------------------------------------------- |
| Why do we use `right - left + 1 - max_freq > k`?         | This is the number of characters needing replacement           |
| Can `max_freq` be stale? Why doesn’t it break the logic? | Yes, because we only shrink when total mismatches exceed `k`   |
| Can this work with lowercase characters?                 | Yes — extend hashmap to size 26 or 128 (ASCII)                 |
| What if replacements must be to the **same character**?  | Already handled — we keep the most frequent and replace others |

---

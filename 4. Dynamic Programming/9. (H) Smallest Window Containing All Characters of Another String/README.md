Here is a README in Markdown format based on the fourth uploaded image:

---

# Smallest Window Containing All Characters of Another String

## Introduction

The **Smallest Window Containing All Characters of Another String** is a common problem in string manipulation and sliding window techniques. The goal is to find the smallest substring in one string (`s1`) that contains all characters (including duplicates) of another string (`s2`).

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given two strings `s1` and `s2`, find the **smallest window in `s1`** that contains **all characters of `s2`**, including duplicates. If no such window exists, return an empty string `""`. If multiple such windows are of the same length, return the one with the **least starting index**.

> **Note:** All characters are lowercase letters.

---

## Examples

### Example 1

```
Input: s1 = "timetopractice", s2 = "toc"  
Output: "toprac"  
Explanation: "toprac" is the smallest substring that contains all characters of "toc"
```

### Example 2

```
Input: s1 = "zoomlazapzo", s2 = "oza"  
Output: "apzo"  
Explanation: "apzo" is the smallest window containing all characters of "oza"
```

### Example 3

```
Input: s1 = "zoom", s2 = "zooe"  
Output: ""  
Explanation: "zoom" does not contain all characters of "zooe"
```

---

## Constraints

* `1 ≤ |s1|, |s2| ≤ 10^5`
* `s1` and `s2` consist of lowercase letters only

---

## Expected Complexity

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(1)

---

## Tags

### Company Tags

`Flipkart`, `Amazon`, `Microsoft`, `MakeMyTrip`, `Google`, `Streamoid Technologies`, `Media.net`, `Atlassian`

### Topic Tags

`sliding-window`, `Hash`, `Strings`, `Dynamic Programming`, `Data Structures`, `Algorithms`

---

## Related Content

* **Interview Experiences**:

  * Makemytrip Interview Experience
  * Amazon Interview Experience Set 315
  * Streamoid Technologies Interview Experience Set 1 For Freshers
  * Flipkart Interview Set 5 Off Campus

* **Article**: [Find The Smallest Window In A String Containing All Characters Of Another String](#)

---

Let me know if you'd like a code solution or breakdown of the sliding window technique used to solve this efficiently.

---

Here is a **complete explanation**, **step-by-step dry run**, and implementations in **Python**, **C++**, and **JavaScript** for the **"Smallest window containing all characters of another string"** problem.

---

### ✅ Problem Summary

You're given two strings `s1` and `s2`. Find the **smallest window** in `s1` that contains **all characters (with duplicates)** of `s2`. If multiple answers exist, return the one with the **least starting index**.

---

### 🔍 Dry Run Example

#### Input:

```
s1 = "timetopractice"
s2 = "toc"
```

#### Step-by-step:

* Frequency of s2 (`toc`) → `{t:1, o:1, c:1}`
* Start expanding window on `s1` with two pointers: `start` and `end`.
* Expand `end`, and add characters to window frequency map.
* When the window contains **all characters** of `s2` with required counts:

  * Try shrinking `start` to find the smallest valid window.
* Track the smallest valid window length.

#### Output: `"toprac"`

---

### 🧠 Key Concepts

* Use **sliding window** + **hash maps**.
* Track required frequencies of characters in `s2`.
* Expand window until valid, then contract to minimize.

---

### ✅ Python Code

```python
class Solution:
    def smallestWindow(self, s1, s2):
        from collections import Counter

        if not s1 or not s2:
            return ""

        target = Counter(s2)
        window = {}
        have, need = 0, len(target)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r, char in enumerate(s1):
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # shrink window
                window[s1[l]] -= 1
                if s1[l] in target and window[s1[l]] < target[s1[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s1[l:r+1] if res_len != float("inf") else ""
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    string smallestWindow(string &s1, string &s2) {
        unordered_map<char, int> target, window;
        for (char ch : s2) target[ch]++;

        int have = 0, need = target.size();
        int minLen = INT_MAX, start = 0;
        int l = 0;

        for (int r = 0; r < s1.size(); ++r) {
            window[s1[r]]++;

            if (target.count(s1[r]) && window[s1[r]] == target[s1[r]])
                have++;

            while (have == need) {
                if ((r - l + 1) < minLen) {
                    minLen = r - l + 1;
                    start = l;
                }

                window[s1[l]]--;
                if (target.count(s1[l]) && window[s1[l]] < target[s1[l]])
                    have--;
                l++;
            }
        }

        return (minLen == INT_MAX) ? "" : s1.substr(start, minLen);
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    smallestWindow(s1, s2) {
        if (!s1 || !s2 || s2.length > s1.length) return "";

        const target = new Map();
        for (let ch of s2) {
            target.set(ch, (target.get(ch) || 0) + 1);
        }

        let have = 0, need = target.size;
        const window = new Map();
        let res = [-1, -1], resLen = Infinity;
        let l = 0;

        for (let r = 0; r < s1.length; r++) {
            const ch = s1[r];
            window.set(ch, (window.get(ch) || 0) + 1);

            if (target.has(ch) && window.get(ch) === target.get(ch)) {
                have++;
            }

            while (have === need) {
                if ((r - l + 1) < resLen) {
                    res = [l, r];
                    resLen = r - l + 1;
                }

                window.set(s1[l], window.get(s1[l]) - 1);
                if (target.has(s1[l]) && window.get(s1[l]) < target.get(s1[l])) {
                    have--;
                }
                l++;
            }
        }

        const [start, end] = res;
        return resLen === Infinity ? "" : s1.slice(start, end + 1);
    }
}
```

---

### 📌 Final Notes

* All solutions run in **O(n)** time using sliding window and hash map.
* Ensures duplicates in `s2` are respected.
* Handles edge cases like no window found, and empty strings.

Let me know if you want this integrated with your test framework or if you'd like visual step-by-step on another example.




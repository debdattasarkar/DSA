Here’s the full README-style conversion for **Leetcode 14. Longest Common Prefix**:

---

# 14. Longest Common Prefix

### Difficulty: Easy

**Topics**: String, Trie
**Companies**: 📁 Common Interview Question

---

## Problem Statement

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Examples

### Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2:

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

---

## Constraints:

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters if it is non-empty.

---

## Text Explanation

We are given an array of strings and we have to return the **longest prefix** that is **common to all** strings.

To do this:

* Pick the first string as a reference.
* Compare character-by-character with the rest of the strings.
* Stop at the first mismatch.

---

## Step-by-step Dry Run

**Input:** `["flower", "flow", "flight"]`

* Start with prefix = `"flower"`
* Compare with `"flow"` → common prefix = `"flow"`
* Compare `"flow"` with `"flight"`:

  * `f == f` ✅
  * `l == l` ✅
  * `o != i` ❌ → common prefix becomes `"fl"`

✅ Final answer = `"fl"`

---

## Expected Interview Questions

**Q1:** What happens if one of the strings is empty?
👉 Return `""` immediately.

**Q2:** How does this scale with large inputs?
👉 Time complexity is O(N \* M), where N = number of strings, M = length of the shortest string.

**Q3:** What data structure improves this?
👉 A Trie can optimize prefix problems when many operations are performed.

---

## Optimized Code Solutions

### ✅ Python

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # Assume the first string is the prefix
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Trim the last character
                if not prefix:
                    return ""
        return prefix
```

---

### ✅ C++

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = strs[0];
        for (int i = 1; i < strs.size(); ++i) {
            while (strs[i].find(prefix) != 0) {
                prefix = prefix.substr(0, prefix.size() - 1);
                if (prefix.empty()) return "";
            }
        }
        return prefix;
    }
};
```

---

### ✅ JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (!strs.length) return "";

    let prefix = strs[0];
    for (let i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.slice(0, -1);
            if (!prefix) return "";
        }
    }
    return prefix;
};
```

---


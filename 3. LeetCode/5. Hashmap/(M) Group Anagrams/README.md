
---

## 📝 Problem: 49. Group Anagrams

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Sorting
**Companies:** Common interview question

---

### 🧾 Problem Statement

Given an array of strings `strs`, group the **anagrams** together.
You can return the answer **in any order**.

---

### 📌 Examples

#### Example 1:

```
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]
```

* "nat" and "tan" are anagrams.
* "ate", "eat", "tea" are also anagrams.
* "bat" has no anagram in the list.

#### Example 2:

```
Input: strs = [""]
Output: [[""]]
```

#### Example 3:

```
Input: strs = ["a"]
Output: [["a"]]
```

---

### ✅ Constraints:

* `1 <= strs.length <= 10^4`
* `0 <= strs[i].length <= 100`
* `strs[i]` consists of **lowercase English letters**

---

## 💡 Intuition & Approach

To group words that are anagrams:

1. **All anagrams will have the same characters when sorted**.
2. So, we can use the **sorted string as a key** in a hash map (dictionary).
3. Append all words sharing the same sorted key into the same list.

---

## 🧪 Dry Run

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`

| Word | Sorted | Key Used for Hashmap   |
| ---- | ------ | ---------------------- |
| eat  | aet    | \["eat"]               |
| tea  | aet    | \["eat", "tea"]        |
| tan  | ant    | \["tan"]               |
| ate  | aet    | \["eat", "tea", "ate"] |
| nat  | ant    | \["tan", "nat"]        |
| bat  | abt    | \["bat"]               |

**Final Output:** `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`

---

## ✅ Python Code (Optimized with HashMap)

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # key: sorted string, value: list of anagrams

        for word in strs:
            sorted_key = ''.join(sorted(word))  # Sorting characters in word
            anagram_map[sorted_key].append(word)  # Append word under its sorted key
        
        return list(anagram_map.values())  # Return grouped anagrams
```

### ⏱ Time and Space Complexity

* **Time:** O(N \* K log K)

  * N = number of strings
  * K = average length of each string (sorting)
* **Space:** O(N \* K) → for hashmap and output

---

## ✅ C++ Code

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;

        for (string& word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());
            anagramMap[sortedWord].push_back(word);
        }

        vector<vector<string>> result;
        for (auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        return result;
    }
};
```

---

## ✅ JavaScript Code

```javascript
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = new Map();

    for (let word of strs) {
        let key = word.split('').sort().join('');  // sorted characters
        if (!map.has(key)) map.set(key, []);
        map.get(key).push(word);
    }

    return Array.from(map.values());
};
```

---

## ❓ Interview Q\&A

| Question                               | Answer                                                        |
| -------------------------------------- | ------------------------------------------------------------- |
| How do you detect anagrams?            | By sorting characters or counting character frequencies       |
| What data structure is used to group?  | HashMap (Dictionary in Python)                                |
| Can the order of output groups matter? | No. Any order is valid                                        |
| Can you do better than sorting?        | Yes, by using a character count (array of 26) as key          |
| When would sorting fail?               | Sorting is fine for ASCII, but costly if word length is large |
| Is the algorithm stable?               | No, because anagram groups are unordered unless specified     |

---

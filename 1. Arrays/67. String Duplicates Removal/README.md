Here's a complete explanation of the **String Duplicates Removal** problem, a **step-by-step dry run**, followed by correct implementations in **Python**, **C++**, and **JavaScript**, each with inline comments.

---

## ✅ Problem Summary

Given a string `s`, remove all **duplicate characters** (case-sensitive) such that the **order of characters remains** the same as the original string.

---

## ✅ Dry Run Example

### Input:

`s = "geEksforGEeks"`

### Steps:

1. Initialize an empty set `seen` and an empty result list `res`.
2. Traverse each character of the string:

   * If the character is not in `seen`, add it to `res` and mark it in `seen`.
   * If it's already in `seen`, skip it.

### Walkthrough:

````
'geEksforGEeks'
→ seen = {}, res = []
→ 'g' not in seen → res = ['g']
→ 'e' → res = ['g', 'e']
→ 'E' → res = ['g', 'e', 'E']
→ 'k' → res = ['g', 'e', 'E', 'k']
→ 's' → res = ['g', 'e', 'E', 'k', 's']
→ 'f' → res = ['g', 'e', 'E', 'k', 's', 'f']
→ 'o' → res = ['g', 'e', 'E', 'k', 's', 'f', 'o']
→ 'r' → res = ['g', 'e', 'E', 'k', 's', 'f', 'o', 'r']
→ 'G' → res = ['g', 'e', 'E', 'k', 's', 'f', 'o', 'r', 'G']
→ 'E' → already in seen
→ 'e' → already in seen
→ 'k' → already in seen
→ 's' → already in seen

### Output:
`geEksforG`

---

## ✅ Python Implementation

```python
class Solution:
    def removeDuplicates(self, s):
        seen = set()
        result = []
        
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        
        return ''.join(result)
````

---

## ✅ C++ Implementation

```cpp
class Solution {
  public:
    string removeDuplicates(string &s) {
        unordered_set<char> seen;  // Set to track characters
        string result = "";

        for (char ch : s) {
            if (seen.find(ch) == seen.end()) {
                seen.insert(ch);
                result += ch;
            }
        }

        return result;
    }
};
```

---

## ✅ JavaScript Implementation

```javascript
class Solution {
    removeDuplicates(s) {
        let seen = new Set();
        let result = "";

        for (let ch of s) {
            if (!seen.has(ch)) {
                seen.add(ch);
                result += ch;
            }
        }

        return result;
    }
}
```

---

## ✅ Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1) – Since the alphabet size is bounded (A-Z, a-z).

Would you like me to write test drivers or edge case validation for this?

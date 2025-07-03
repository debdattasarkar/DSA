
---

# 📘 205. Isomorphic Strings

**Difficulty:** Easy
**Topics:** Hash Table, String
**Asked in:** Top tech companies

---

## ❓ Problem Statement

Given two strings `s` and `t`, **determine if they are isomorphic**.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`.

🔁 Rules:

* All occurrences of a character must be replaced with **another** character while preserving **order**.
* No two characters in `s` may map to the same character in `t`, but a character can map to itself.

---

## 🧪 Examples

### Example 1:

**Input:**
`s = "egg"`
`t = "add"`

**Output:** `true`

**Explanation:**

* `e -> a`
* `g -> d`

---

### Example 2:

**Input:**
`s = "foo"`
`t = "bar"`

**Output:** `false`

**Explanation:**

* `o` is supposed to map to both `a` and `r` which is invalid.

---

### Example 3:

**Input:**
`s = "paper"`
`t = "title"`

**Output:** `true`

**Explanation:**

* `p -> t`
* `a -> i`
* `e -> l`
* `r -> e`

---

## ✅ Constraints:

* `1 <= s.length <= 5 * 10^4`
* `t.length == s.length`
* `s` and `t` consist of any valid ASCII character.

---

## 🧠 Dry Run: "paper" vs "title"

| Index | s\[i] | t\[i] | Map s→t | Map t→s | Result |
| ----- | ----- | ----- | ------- | ------- | ------ |
| 0     | p     | t     | p→t     | t→p     | ✅      |
| 1     | a     | i     | a→i     | i→a     | ✅      |
| 2     | p     | t     | match   | match   | ✅      |
| 3     | e     | l     | e→l     | l→e     | ✅      |
| 4     | r     | e     | r→e     | e→r     | ✅      |

✅ All mappings are consistent.

---

## 🧮 Python Code (Optimized with Inline Comments)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionary to track character mapping from s -> t and t -> s
        map_s_t = {}
        map_t_s = {}
        
        for cs, ct in zip(s, t):
            # Check if mapping exists and is consistent from s to t
            if cs in map_s_t:
                if map_s_t[cs] != ct:
                    return False
            else:
                map_s_t[cs] = ct
            
            # Check reverse mapping from t to s
            if ct in map_t_s:
                if map_t_s[ct] != cs:
                    return False
            else:
                map_t_s[ct] = cs
        
        return True
```

---

## ⏱ Time and Space Complexity

* **Time Complexity:** O(n) — One pass over `s` and `t`.
* **Space Complexity:** O(1) — At most 256 mappings (ASCII).

---

## 💡 C++ Version

```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> st, ts;
        
        for (int i = 0; i < s.length(); i++) {
            char cs = s[i], ct = t[i];
            
            if (st.count(cs) && st[cs] != ct)
                return false;
            if (ts.count(ct) && ts[ct] != cs)
                return false;
            
            st[cs] = ct;
            ts[ct] = cs;
        }
        
        return true;
    }
};
```

---

## 💻 JavaScript Version

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const mapST = new Map();
    const mapTS = new Map();

    for (let i = 0; i < s.length; i++) {
        const cs = s[i], ct = t[i];
        
        if (mapST.has(cs) && mapST.get(cs) !== ct) return false;
        if (mapTS.has(ct) && mapTS.get(ct) !== cs) return false;
        
        mapST.set(cs, ct);
        mapTS.set(ct, cs);
    }

    return true;
};
```

---

## 🎯 Interview Questions & Answers

### Q1: Can a character in `s` map to multiple characters in `t`?

**A:** No. Mapping must be one-to-one.

---

### Q2: Why do we need two maps (`s → t` and `t → s`)?

**A:** To ensure injectivity in both directions and avoid conflicts.

---

### Q3: Can the characters map to themselves?

**A:** Yes, mapping to itself is allowed (e.g., `a -> a`).

---

### Q4: What if the strings are of different lengths?

**A:** Not possible. Problem constraint ensures same length.

---

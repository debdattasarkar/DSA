Let's dive into **“Count Occurrences of Anagrams”** — a very popular **fixed-size sliding window + hashmap** problem, frequently asked in interviews like Amazon, Adobe, and Walmart.

---

## 🔍 Problem Statement (GFG Variant)

> Given a **text** `txt` and a **pattern** `pat`, return the **count of occurrences of anagrams** of `pat` in `txt`.

---

## 🧪 Example:

```python
Input:
txt = "forxxorfxdofr"
pat = "for"

Output: 3

Explanation:
Anagrams of "for" → ["for", "orf", "fro"]
They appear in substrings: ["for", "orf", "ofr"]
```

---

## ✅ Approach: Fixed Sliding Window + Hashmaps

### 🔑 Key Observations:

* All valid anagram windows are of size `len(pat)` → ✅ fixed-size window
* Compare character **frequencies** in the current window vs pattern

---

## 🧑‍💻 Python Code with Inline Comments

```python
from collections import Counter

class Solution:
    def search(self, pat: str, txt: str) -> int:
        k = len(pat)
        n = len(txt)
        
        # Frequency map of pattern
        pat_count = Counter(pat)
        window_count = Counter()

        result = 0

        for i in range(n):
            # Add current character to window
            window_count[txt[i]] += 1

            # Remove leftmost character when window size > k
            if i >= k:
                if window_count[txt[i - k]] == 1:
                    del window_count[txt[i - k]]
                else:
                    window_count[txt[i - k]] -= 1

            # Compare current window with pattern
            if i >= k - 1 and window_count == pat_count:
                result += 1

        return result
```

---

## 📊 Time and Space Complexity

| Metric | Value            |
| ------ | ---------------- |
| Time   | O(n × 26) ⇒ O(n) |
| Space  | O(26) ⇒ O(1)     |

Because we're comparing **fixed alphabet (lowercase)** frequencies.

---

## 🧠 Dry Run

### Input:

```python
txt = "forxxorfxdofr", pat = "for"
```

* k = 3
* pat\_count = {f:1, o:1, r:1}

Window slides:

| Window | Window Count | Match |
| ------ | ------------ | ----- |
| "for"  | f:1 o:1 r:1  | ✅     |
| "orx"  | o:1 r:1 x:1  | ❌     |
| "rxx"  | r:1 x:2      | ❌     |
| "xxo"  | x:2 o:1      | ❌     |
| "xor"  | x:1 o:1 r:1  | ❌     |
| "orf"  | o:1 r:1 f:1  | ✅     |
| "rfx"  | r:1 f:1 x:1  | ❌     |
| "fxd"  | f:1 x:1 d:1  | ❌     |
| "xdo"  | x:1 d:1 o:1  | ❌     |
| "dof"  | d:1 o:1 f:1  | ❌     |
| "ofr"  | o:1 f:1 r:1  | ✅     |

✅ Count = **3**

---

## ❓ Interview-Focused Q\&A

| Question                                        | Answer                                                          |
| ----------------------------------------------- | --------------------------------------------------------------- |
| Why use Counter over set?                       | Need to match **frequency**, not just character presence        |
| Can we optimize window comparison?              | Yes — keep a **match count** variable for faster comparison     |
| What’s better than Counter for large alphabets? | Custom arrays (size 26) for a-z only                            |
| Can this solve permutations of string?          | Yes, it’s the **core idea** in LC 567                           |
| What changes if pattern length varies?          | Then it becomes a variable-size window problem ❌ for this logic |

---

## 🔗 Related Problems

| Problem                                                                                                      | Platform | Pattern                            |
| ------------------------------------------------------------------------------------------------------------ | -------- | ---------------------------------- |
| [Leetcode 567 – Permutation in String](https://leetcode.com/problems/permutation-in-string/)                 | Leetcode | Anagram check using sliding window |
| [Leetcode 438 – Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Leetcode | Same idea, return indices          |
| GFG – Count distinct substrings of length K                                                                  | GFG      | Hashing + window                   |

---

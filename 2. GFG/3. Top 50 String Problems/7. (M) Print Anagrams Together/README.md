# Print Anagrams Together

**Difficulty:** Medium
**Accuracy:** 65.78%
**Submissions:** 103K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given an array of strings, return **all groups of strings that are anagrams**.
The strings in each group **must be arranged in the order of their appearance** in the original array. Refer to the sample cases for clarification.

---

## Examples

### Example 1

**Input:** `arr[] = ["act", "god", "cat", "dog", "tac"]`
**Output:** `[["act", "cat", "tac"], ["god", "dog"]]`
**Explanation:**
There are **2** groups of anagrams — `"god", "dog"` make group 1. `"act", "cat", "tac"` make group 2.

---

### Example 2

**Input:** `arr[] = ["no", "on", "is"]`
**Output:** `[["is"], ["no", "on"]]`
**Explanation:**
There are **2** groups of anagrams — `"is"` makes group 1. `"no", "on"` make group 2.

---

### Example 3

**Input:**
`arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]`
**Output:**
`[["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]`
**Explanation:**

* Group 1: `"abc"`, `"cab"`, and `"bac"` are anagrams.
* Group 2: `"listen"`, `"silent"`, and `"enlist"` are anagrams.
* Group 3: `"rat"`, `"tar"`, and `"art"` are anagrams.

---

## Constraints

* `1 <= arr.size() <= 100`
* `1 <= arr[i].size() <= 10`

---

## Expected Complexities

* **Time Complexity:** `O(n * m log m)`
  (where `n` is number of strings and `m` is max string length)
* **Auxiliary Space:** `O(n * m)`

---

## Company Tags

Morgan Stanley, Amazon, Microsoft, Snapdeal, D-E-Shaw, Goldman Sachs

---

## Topic Tags

Hash, Strings, Data Structures

---

## Related Interview Experiences

* Amazon Interview Experience Set 144 Campus Sde 1
* Snapdeal Interview Experience Set 8 On Campus
* Amazon Interview Experience Set 188 For Sde1
* Microsoft Interview Experience For Sde 1 2
* (and others)

---

## Related Articles

* Given A Sequence Of Words Print All Anagrams Together Set 2
* Given A Sequence Of Words Print All Anagrams Together Using STL
* Given A Sequence Of Words Print All Anagrams Together

---

---

Here’s a crisp, interview-ready guide for **“Print Anagrams Together”**.

---

## 2) Explanation + step-by-step dry run

### What we need

Group words that are anagrams.
**Important detail:** Inside each group, **preserve the order of appearance** in the original list.

### Canonical (most expected) approach

Use a **signature** for each word that is identical for all its anagrams, then bucket words by that signature.

Two common signatures:

1. **Sorted letters** (simple & standard)
   `key = "".join(sorted(word))`
   Time per word `O(m log m)` where `m` is word length.

2. **Char frequency tuple** (faster when alphabet is fixed, e.g., lowercase a–z)
   `key = tuple(counts of 26 letters)`
   Time per word `O(m)`. Space `O(1)` per word for the 26-size array.

As we iterate through `arr`, append each word to its bucket. Python dicts preserve insertion order (3.7+), so appearance order within each group is kept automatically.

### Dry run

`arr = ["act", "god", "cat", "dog", "tac"]`

Using **sorted signature**:

* `"act"` → key `"act"` → buckets = { "act": \["act"] }
* `"god"` → key `"dgo"` → { "act": \["act"], "dgo": \["god"] }
* `"cat"` → key `"act"` → { "act": \["act","cat"], "dgo": \["god"] }
* `"dog"` → key `"dgo"` → { "act": \["act","cat"], "dgo": \["god","dog"] }
* `"tac"` → key `"act"` → { "act": \["act","cat","tac"], "dgo": \["god","dog"] }

Return groups in any order (driver may sort groups), while **each group preserves input order**:
`[["act","cat","tac"], ["god","dog"]]`

---

## 3) Python solutions (optimized + alternatives)

### A) Sorted-key buckets (most expected in interviews)

```python
# User function Template for python3
from collections import defaultdict

class Solution:
    def anagrams(self, arr):
        '''
        Group words that are anagrams.
        Maintain order of appearance inside each group by appending as we scan.
        Time  : O(n * m log m)  (n words, each sorted)
        Space : O(n * m)        (to store groups/keys)
        '''
        buckets = defaultdict(list)  # key -> list of words (order preserved)
        for w in arr:                # O(n)
            key = ''.join(sorted(w)) # O(m log m)
            buckets[key].append(w)   # O(1) amortized
        # Driver may sort outer list; inner lists already in input order
        return list(buckets.values())
```

### B) Counting-key buckets (O(n\*m), faster on fixed alphabet)

```python
from collections import defaultdict

class SolutionCounting:
    def anagrams(self, arr):
        '''
        Use 26-length frequency tuple as key (lowercase a-z).
        Time  : O(n * m)   (counting chars)
        Space : O(n * m)
        '''
        buckets = defaultdict(list)
        for w in arr:
            counts = [0] * 26
            for ch in w:                       # O(m)
                counts[ord(ch) - 97] += 1
            key = tuple(counts)                # hashable
            buckets[key].append(w)
        return list(buckets.values())
```

> Pick **A** by default (clean & general). Mention **B** if asked to optimize (and if charset is known/limited).

### C) Brute force (educational; not recommended)

Repeatedly take the first unused word, scan all others and check “is anagram” by sorting or counting.

```python
class SolutionBrute:
    def anagrams(self, arr):
        '''
        Time  : O(n^2 * m log m) if using sort per compare
        Space : O(n) to track used flags
        '''
        used = [False] * len(arr)
        groups = []

        def is_anagram(a, b):
            return sorted(a) == sorted(b)  # O(m log m)

        for i in range(len(arr)):
            if used[i]:
                continue
            group = [arr[i]]
            used[i] = True
            for j in range(i + 1, len(arr)):
                if not used[j] and is_anagram(arr[i], arr[j]):
                    group.append(arr[j])
                    used[j] = True
            groups.append(group)  # group maintains input order
        return groups
```

---

## 4) Interviewer-style Q\&A

**Q1. Why do we need a reverse mapping or extra checks?**
We don’t. For grouping, a **canonical key** per word suffices. All words with the same key go to the same bucket.

**Q2. Complexity trade-offs?**

* Sorted key: `O(m log m)` per word; simplest and language-agnostic.
* Counting key: `O(m)` per word; faster but assumes a fixed alphabet (e.g., lowercase English).
  Both return `O(total characters)` space for groups.

**Q3. How do you preserve order of words inside each group?**
We append words to buckets **in input order**. Python dict/list keeps insertion order; we never sort the group.

**Q4. How are groups ordered in the result?**
Problem statements often let the **driver sort the outer list**. We return `list(buckets.values())`. If a specific outer order is required (e.g., by first appearance), Python’s insertion-ordered dict already preserves the first time each key was seen.

**Q5. Are there other signatures (like prime multiplication)?**
Yes, but primes can overflow in other languages and cause collisions with modulo. Sorted string or frequency tuple are safe and standard.

**Q6. What about Unicode, case, punctuation?**
Sorted-key method works generically. For counting keys, you must define the alphabet and mapping (or stick with sorted).

**Q7. Memory considerations?**
Keys plus buckets require `O(n*m)` in total; unavoidable because the result itself stores all words.

---

---


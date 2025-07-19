
---

# Count Unique Vowel Strings

**Difficulty**: Medium
**Accuracy**: 59.44%
**Submissions**: 6K+
**Points**: 4

---

## 🧩 Problem Statement

You are given a lowercase string `s`. Determine the total number of **distinct strings** that can be formed using the following rules:

1. **Identify all unique vowels** (`a, e, i, o, u`) present in the string.
2. For **each distinct vowel**, choose **exactly one** of its occurrences from `s`.

   * If a vowel appears multiple times, each occurrence represents a unique selection choice.
3. Generate **all possible permutations** of the selected vowels.

   * Each unique arrangement counts as a **distinct string**.

Return the **total number** of such distinct strings.

---

## 🧪 Examples

### Example 1:

**Input**:
`s = "aeiou"`
**Output**:
`120`
**Explanation**:
Each vowel appears once, so the number of different strings that can be formed is `5! = 120`.

---

### Example 2:

**Input**:
`s = "ae"`
**Output**:
`2`
**Explanation**:
Pick `'a'` and `'e'`, make all orders → `"ae"`, `"ea"`.

---

### Example 3:

**Input**:
`s = "aacidf"`
**Output**:
`4`
**Explanation**:
Vowels in `s` are `'a'` and `'i'`.
Pick each `'a'` once with a single `'i'`, make all orders → `"ai"`, `"ia"`, `"ai"`, `"ia"`
(2 choices of `'a'` × 2 permutations → 4 total distinct strings).

---

## 🔒 Constraints

* `1 ≤ s.size() ≤ 100`

---

## 🧠 Expected Complexities

* **Time Complexity**: `O(n)`
* **Auxiliary Space**: `O(1)`

---

## 🏷️ Topic Tags

* Strings
* Combinatorial
* Mathematical

---

## 📖 Related Articles

* [Unique Vowel Arrangements](https://www.geeksforgeeks.org/unique-vowel-arrangements/)

---

---

Here's a full solution for the problem **“Count Unique Vowel Strings”**, with explanation, dry run, multiple code approaches, and expected interview Q\&A.

---

## ✅ 2. Text Explanation + Step-by-Step Dry Run

### 🔍 Problem Summary:

You're given a lowercase string `s`. You must:

1. Identify all **unique vowels** from `'aeiou'` in the string.
2. For each **unique vowel**, choose one occurrence (regardless of how many times it appears).
3. Find all **permutations** of these selected vowels.
4. Count how many such distinct permutations are possible.

The total number of such strings is:

```
(permutations of the unique vowels) × (number of ways to choose 1 occurrence per vowel)
```

---

### 🪜 Dry Run:

Let’s dry-run with:
**Input:** `"aacidf"`

1. Unique vowels = `'a', 'i'`
2. Count of `'a'` = 2
   Count of `'i'` = 1
   For `'a'`, we can pick **2** positions. For `'i'`, only **1**
3. Total selection ways = `2 * 1 = 2`
4. Number of permutations of 2 vowels = `2! = 2`
5. Final count = `2 * 2 = 4`

**Output:** `4`

---

## ✅ 3. Optimized Python Code (with inline comments)

### ✔️ Brute + Clean (Optimized, expected in interviews):

```python
from math import factorial
from collections import Counter

class Solution:
    def vowelCount(self, s):
        # Step 1: Define vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 2: Count only vowels in the string
        count = Counter([ch for ch in s if ch in vowels])

        # Step 3: Extract unique vowel counts
        unique_vowels = list(count.keys())
        k = len(unique_vowels)  # Number of distinct vowels

        if k == 0:
            return 0  # No vowels, no permutations possible

        # Step 4: Number of permutations of unique vowels = k!
        perm = factorial(k)

        # Step 5: For each vowel, how many positions can we pick from?
        choices = 1
        for v in unique_vowels:
            choices *= count[v]  # pick 1 occurrence per vowel

        return perm * choices
```

### 🧪 Example Runs:

```python
print(Solution().vowelCount("aeiou"))    # Output: 120
print(Solution().vowelCount("ae"))       # Output: 2
print(Solution().vowelCount("aacidf"))   # Output: 4
```

---

## ⏱️ Time and Space Complexity:

* **Time Complexity:** `O(n)`

  * One pass to filter vowels and count frequencies.
  * Factorial computation is on a constant set (max 5 vowels), hence `O(1)` for that.
* **Space Complexity:** `O(1)`

  * Max 5 vowels stored in the Counter.

---

## ✅ 4. Expected Interview Questions & Answers

### ❓Q1. Why are you using `factorial(k)`?

**A:** To count the number of **distinct arrangements (permutations)** of the selected vowels. For `k` distinct vowels, `k!` permutations exist.

---

### ❓Q2. Why not use all occurrences of each vowel?

**A:** The problem restricts us to pick **exactly one occurrence per vowel**. Multiple occurrences only increase the number of **ways to choose**, not the length of the arrangement.

---

### ❓Q3. How do multiple occurrences affect the count?

**A:** Each repeated vowel increases the **selection possibilities**. For example, two `'a'`s mean we have 2 ways to pick the position of `'a'`.

---

### ❓Q4. What if there are no vowels?

**A:** Return `0`. There’s no way to form a vowel permutation.

---

### ❓Q5. Could the problem scale beyond 5 vowels?

**A:** No. There are only 5 vowels. So permutations are capped at `5! = 120`. This keeps runtime constant for permutation computation.

---

---



---

## 🧬 Problem: Repeated DNA Sequences

### 📄 Statement

A DNA sequence is made of characters `'A'`, `'C'`, `'G'`, and `'T'`. Given a string `s`, return all the **10-letter-long substrings** (sequences) that occur **more than once** in `s`.

---

### 🧾 Constraints

* `1 ≤ s.length ≤ 10⁵`
* DNA only contains the characters: `'A'`, `'C'`, `'G'`, `'T'`

---

### 🎯 Goal

Return **all 10-character substrings** that **repeat** in the input string. Return them in **any order**.

---

### 📥 Input

```text
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
```

### 📤 Output

```text
["AAAAACCCCC", "CCCCCAAAAA"]
```

---

### 🧠 Pattern Used: Sliding Window + Hash Set

#### Why Sliding Window?

We want to consider **every possible 10-letter window** in the string. A fixed-size sliding window of length 10 ensures we inspect **each substring once**, moving one character at a time.

#### Why Hashing?

We use a hash set to:

1. Track already seen 10-letter substrings.
2. Identify when a substring appears **again**.

---

### 🔄 Step-by-Step Algorithm

1. Use a **window size** of 10 and loop from index `0` to `len(s) - 10`.
2. At each index, extract the 10-letter substring.
3. Store seen substrings in a set.
4. If a substring is seen again, add it to the result set.
5. Return all items in the result set.

---

### ✅ Examples

Here is the extracted and organized **README-style explanation** for the **problem of finding repeated DNA subsequences**:

---

### 🔍 Problem: Repeated DNA Subsequences

You are given a DNA sequence represented as a string `s`. You need to identify **all 10-letter-long sequences (substrings)** that occur **more than once** in this string and return them as a list.

---

### 🧾 Input

* A single string `s` representing a DNA sequence, e.g., `"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"`.
* Characters are only: `A`, `C`, `G`, and `T`.
* Length: `1 <= len(s) <= 10^5`.

---

### 📤 Output

* A list of strings, where each string is a 10-letter substring that appears **more than once** in `s`.

---

### ✅ Conditions

* Substrings must be exactly **10 characters long**.
* Only repeated substrings should be returned.

---

### 🧠 Approach Summary

1. Use a **sliding window** of size 10 over the string `s`.
2. Track seen substrings in a `set`.
3. Track duplicates in a `set` (or directly in result).
4. Return all elements that appear more than once.

---

### 📦 Sample Examples

#### ✅ Sample Example 1

```
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Explanation:
"AAAAACCCCC" appears from s[0] to s[9] and s[10] to s[19].
"CCCCCAAAAA" appears from s[5] to s[14] and s[16] to s[25].
```

---

#### ✅ Sample Example 2

```
Input:  s = "GGGGGGGGGGGGGGGGGGGG"
Output: ["GGGGGGGGGG"]

Explanation:
"GGGGGGGGGG" appears 11 times in the string.
```

---

#### ✅ Sample Example 3

```
Input:  s = "TTTGGGAAATTTTGGGAAACC"
Output: []

Explanation:
No 10-letter-long substring appears more than once.
```

---

### ⏱️ Time and Space Complexity

| Metric | Complexity                       |
| ------ | -------------------------------- |
| Time   | O(n), where n = len(s)           |
| Space  | O(n) for sets of seen substrings |

---

Let me know if you'd like the full Python code for this with performance timing.


---

### 🧪 Technical Quiz

Given `s = "ATATTGGCCCAATTGGCCCAATTCGC"`, what’s the correct output?

Answer: Look for repeated 10-letter substrings in overlapping windows.

---

### 🧱 Logical Building Blocks (Sliding Window Hashing)

1. Convert each character to a number (optional optimization).
2. Initialize hash set to store substring hashes.
3. Slide the window and compute the hash of each 10-letter segment.
4. If hash already seen, add substring to results.
5. Continue until full string is processed.

---

### ⏱ Complexity

| Metric | Complexity       |
| ------ | ---------------- |
| Time   | O(n)             |
| Space  | O(n) (hash sets) |

---

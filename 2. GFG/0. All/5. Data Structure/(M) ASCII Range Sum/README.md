
---

# ASCII Range Sum

**Difficulty:** Medium
**Accuracy:** 56.66%
**Submissions:** 30+
**Points:** 4

---

## 🧩 Problem Statement

Given a string `s` consisting of **lowercase English letters**, for every character whose first and last occurrences are at different positions, calculate the **sum of ASCII values of characters strictly between its first and last occurrence**.

Return all such **non-zero sums** (order does not matter).

---

## 🧪 Examples

### Example 1:

```
Input:  s = "abacab"
Output: [293, 294]

Explanation: 
Characters 'a' and 'b' appear more than once:
- 'a': Between positions 1 and 5 → characters are b, a, c → ASCII sum = 98 + 97 + 99 = 294
- 'b': Between positions 2 and 6 → characters are a, c, a → ASCII sum = 97 + 99 + 97 = 293
```

### Example 2:

```
Input:  s = "acdac"
Output: [197, 199]

Explanation:
Characters 'a' and 'c' appear more than once:
- 'a': Between positions 1 and 4 → characters are c, d → ASCII sum = 99 + 100 = 199
- 'c': Between positions 2 and 5 → characters are d, a → ASCII sum = 100 + 97 = 197
```

---

## 📌 Constraints

* `1 ≤ s.size() ≤ 10⁵`

---

## 🔍 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Tags

* `prefix-sum`
* `Data Structures`
* `Hash`

---

---

Here’s the full breakdown for the **ASCII Range Sum** problem:

---

## ✅ 2. Text Explanation + Step-by-Step Dry Run

### 🔸 Problem Recap:

Given a string `s`, find **ASCII sums** of characters that are **strictly between** the **first and last occurrence** of any character that appears **more than once**.

Only include sums **strictly inside** (i.e., not including the first and last index).

Return all such **non-zero sums**, **in any order**.

---

### 🔹 Step-by-Step Dry Run

Let’s dry run for:
`s = "abacab"`
→ ASCII codes:
`a = 97, b = 98, c = 99`

Index mapping:

```
0  1  2  3  4  5
a  b  a  c  a  b
```

**First and Last Occurrences:**

| Char | First Index | Last Index |
| ---- | ----------- | ---------- |
| a    | 0           | 4          |
| b    | 1           | 5          |

Now calculate for:

* `'a'`: chars between index `1 to 3`: **\[b=98, a=97, c=99]**
  `Sum = 98 + 97 + 99 = 294`
* `'b'`: chars between index `2 to 4`: **\[a=97, c=99, a=97]**
  `Sum = 97 + 99 + 97 = 293`

✅ Final output: `[293, 294]`

---

## ✅ 3. Optimized Python Code

### 🔹 Expected in Interviews (O(n) time, O(1) extra space since alphabet is small):

```python
class Solution:
    def asciirange(self, s: str):
        # Store first and last occurrence of each character
        first = [-1] * 26
        last = [-1] * 26
        n = len(s)
        
        # Fill in first and last occurrence
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        result = []

        # For each character, calculate the ASCII sum between its first and last index
        for i in range(26):
            if first[i] != -1 and last[i] > first[i] + 1:
                total = 0
                for j in range(first[i] + 1, last[i]):
                    total += ord(s[j])
                if total > 0:
                    result.append(total)
        
        return result
```

### 🧠 Time and Space Complexity

* **Time:** O(n + 26) → O(n)
* **Space:** O(26) → O(1), for first and last index arrays

---

## 🛠 Brute Force (Not ideal for interviews)

* For each char from `'a'` to `'z'`:

  * Traverse string to find first and last index
  * Loop over range and sum

It works, but traverses the string **multiple times** → O(26n)

---

## ✅ 4. Interview Q\&A

### 🔹 Q1: How would you solve this in O(n)?

**A:**
Track first and last indices of each character while scanning once. Then in a second pass, for each character appearing more than once, compute ASCII sum of characters strictly in between.

---

### 🔹 Q2: Why do we use arrays of size 26?

**A:**
Because the string only contains lowercase English letters, we use arrays indexed from 0 to 25 to track each character efficiently.

---

### 🔹 Q3: Can this be solved without extra space?

**A:**
Yes, we use only fixed-size arrays (26) → it's considered **O(1) auxiliary space** regardless of `n`.

---

### 🔹 Q4: Why skip characters where `first == last`?

**A:**
That means the character appears only once → **no range to evaluate**, as there's nothing between.

---

# 🌍 Real-World Use Cases

Here are some **real-world use cases** where the **ASCII Range Sum** type logic becomes important — not for ASCII per se, but for **range-based character aggregation, encoding, or anomaly detection**:

---

## 🔹 1. **Log Integrity Verification (Cybersecurity / SIEM Systems)**

In many logs, events or users are encoded as character sequences. When trying to detect tampering or anomalies:

* We may look at **first and last appearances** of identifiers (e.g., IP addresses, usernames, device tags).
* Compute **checksum-like aggregates** (e.g., ASCII sum, hash sum) of what's in between to validate integrity.

**Example:** If `"session_id"` occurs more than once in a log file, ensure intermediate entries have a matching hash or checksum.

---

## 🔹 2. **Source Code Auditing / Obfuscation Detection**

In source code security scanners:

* Detect **repeated identifiers** or function names.
* Analyze the **code region between first and last usage**.
* Compute metrics (e.g., ASCII sum, token weights) to **detect injected or hidden code blocks**.

This helps flag unusual activity between legitimate use of common symbols.

---

## 🔹 3. **String Fingerprinting & Compression (Data Engineering)**

In compression or fingerprinting:

* Identifiers appearing multiple times in large text can have **"intermediate influence"** captured via numeric encodings (ASCII/Unicode sums).
* These sums serve as **heuristics** for clustering, deduplication, or creating lossy sketches (e.g., SimHash, MinHash approximations).

---

## 🔹 4. **Genomic Sequence Analysis**

In bioinformatics, DNA bases (`A, C, G, T`) can be encoded numerically:

* Tracking repeated gene sequences and computing **character sums** between their first and last appearance helps in **identifying mutations or repeats**.

Even though bases are not ASCII, the pattern is similar: **range-based aggregation of sequence values**.

---

## 🔹 5. **Chat/Spam Detection in Messaging Systems**

Messages often contain repeated **trigger words or abusive terms**:

* Checking **what’s between** first and last occurrences of such terms (via ASCII/token value aggregation) can **detect camouflage or spacing attacks**.

For example, `"v1agra"` and `"v***agra"` might bypass filters, but aggregated sum between occurrences helps catch hidden threats.

---

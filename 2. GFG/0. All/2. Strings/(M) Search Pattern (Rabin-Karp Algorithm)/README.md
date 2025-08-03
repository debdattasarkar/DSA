
# 🔍 Search Pattern (Rabin-Karp Algorithm)

---

## 🧾 Problem Statement

Given two strings:

* A **text** string in which you want to search.
* A **pattern** string that you are looking for within the text.

Return **all positions (1-based indexing)** where the **pattern** occurs as a **substring** in the **text**.
If the pattern does not occur, return an empty list.

> All characters in both strings are lowercase English letters (`a` to `z`).

---

## 🧪 Examples

### Example 1:

```text
Input:
text = "birthdayboy", pattern = "birth"

Output:
[1]

Explanation:
The string "birth" occurs at index 1 in the text.
```

### Example 2:

```text
Input:
text = "geeksforgeeks", pattern = "geek"

Output:
[1, 9]

Explanation:
The string "geek" occurs twice in text: at index 1 and index 9.
```

---

## 📌 Constraints

* 1 ≤ `text.size()` ≤ 5 × 10⁵
* 1 ≤ `pattern.size()` ≤ `text.size()`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n + m),
  where `n = text.length`, `m = pattern.length`
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

* Microsoft

---

## 🏷️ Topic Tags

`Strings` `Pattern Searching` `Data Structures` `Algorithms`

---

## 📚 Related Articles

* [Rabin-Karp Algorithm For Pattern Searching](#)

---

Here's a **text explanation with dry run** for the **Rabin-Karp string pattern matching algorithm**, followed by clean and optimized code implementations in **Python**, **C++**, and **JavaScript**, with inline comments.

---

## 🧠 Problem: Pattern Matching (Rabin-Karp)

Given:

* A string `txt` (the full text)
* A string `pat` (the pattern to search for)

We must return **1-based indices** where `pat` is found in `txt`.

---

## 🪜 Rabin-Karp Algorithm Overview

Rabin-Karp uses **hashing**:

* Compute a **rolling hash** of the pattern and sliding window of the text.
* When hashes match, check the strings to confirm.
* Rolling hash helps to update efficiently in **O(1)** time.

---

### 📌 Key Concepts

* **Base**: 26 (a-z)
* **Modulus**: A large prime (to avoid collisions), e.g., `10**9 + 7`
* **Hash formula** (for string `"abc"`):
  `h = (ord('a')*b² + ord('b')*b¹ + ord('c')*b⁰) % mod`

---

## 🧪 Dry Run

### Input:

```text
txt = "geeksforgeeks"
pat = "geek"
```

* Length of `pat` = 4
* Calculate hash of "geek"
* Slide window of length 4 over `txt`
* Matches at index 1 and index 9 (1-based)

---

## ✅ Python Code

```python
class Solution:
    def search(self, pat, txt):
        n, m = len(txt), len(pat)
        if m > n:
            return []

        base = 256  # ASCII
        mod = 10**9 + 7

        # Compute hash of pattern and first window
        pat_hash = 0
        txt_hash = 0
        h = 1  # base^(m-1)

        for i in range(m - 1):
            h = (h * base) % mod

        for i in range(m):
            pat_hash = (pat_hash * base + ord(pat[i])) % mod
            txt_hash = (txt_hash * base + ord(txt[i])) % mod

        res = []
        for i in range(n - m + 1):
            if pat_hash == txt_hash:
                if txt[i:i + m] == pat:
                    res.append(i + 1)  # 1-based indexing

            if i < n - m:
                txt_hash = (txt_hash - ord(txt[i]) * h) % mod
                txt_hash = (txt_hash * base + ord(txt[i + m])) % mod
                txt_hash = (txt_hash + mod) % mod  # avoid negative

        return res
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    vector<int> search(string &pat, string &txt) {
        int n = txt.size(), m = pat.size();
        if (m > n) return {};

        const int base = 256;
        const int mod = 1e9 + 7;

        int pat_hash = 0, txt_hash = 0, h = 1;
        vector<int> res;

        // Compute base^(m-1) % mod
        for (int i = 0; i < m - 1; i++)
            h = (h * base) % mod;

        // Initial hash values
        for (int i = 0; i < m; i++) {
            pat_hash = (pat_hash * base + pat[i]) % mod;
            txt_hash = (txt_hash * base + txt[i]) % mod;
        }

        for (int i = 0; i <= n - m; i++) {
            if (pat_hash == txt_hash) {
                if (txt.substr(i, m) == pat)
                    res.push_back(i + 1);  // 1-based index
            }

            if (i < n - m) {
                txt_hash = (txt_hash - txt[i] * h) % mod;
                txt_hash = (txt_hash * base + txt[i + m]) % mod;
                if (txt_hash < 0) txt_hash += mod;
            }
        }

        return res;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    search(pat, txt) {
        const n = txt.length, m = pat.length;
        if (m > n) return [];

        const base = 256;
        const mod = 1e9 + 7;

        let patHash = 0, txtHash = 0, h = 1;
        const res = [];

        // base^(m-1)
        for (let i = 0; i < m - 1; i++) {
            h = (h * base) % mod;
        }

        for (let i = 0; i < m; i++) {
            patHash = (patHash * base + pat.charCodeAt(i)) % mod;
            txtHash = (txtHash * base + txt.charCodeAt(i)) % mod;
        }

        for (let i = 0; i <= n - m; i++) {
            if (patHash === txtHash) {
                if (txt.substr(i, m) === pat)
                    res.push(i + 1); // 1-based index
            }

            if (i < n - m) {
                txtHash = (txtHash - txt.charCodeAt(i) * h) % mod;
                txtHash = (txtHash * base + txt.charCodeAt(i + m)) % mod;
                txtHash = (txtHash + mod) % mod; // fix negative
            }
        }

        return res;
    }
}
```

---

## ⏱ Complexity

| Metric                  | Value        |
| ----------------------- | ------------ |
| Time Complexity         | O(n + m) avg |
| Auxiliary Space         | O(1)         |
| Worst Case (collisions) | O(n\*m)      |

---

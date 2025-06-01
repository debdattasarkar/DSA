Here is the generated **README.md** file based on the "Word Break (Trie)" problem description:

---

# 🧩 Word Break (Trie)

## 📝 Problem Statement

Given a string `A` and a dictionary `B` of `n` words, determine if `A` can be segmented into a space-separated sequence of one or more dictionary words.

This problem typically uses a **Trie** data structure for efficient dictionary word lookup.

---

## 📥 Input

* A string `A`
* A list of strings `B` representing the dictionary of words

---

## 📤 Output

* Return `1` if `A` can be segmented into valid dictionary words.
* Return `0` otherwise.

---

## 🧠 Examples

### Example 1:

```
Input:
n = 12
B = { "i", "like", "sam", "sung", "samsung",
      "mobile", "ice", "cream", "icecream", "man",
      "go", "mango" }
A = "ilike"

Output:
1

Explanation:
The string can be segmented as "i like".
```

### Example 2:

```
Input:
A = "ilikesamsung"

Output:
1

Explanation:
The string can be segmented as:
"i like samsung" or "i like sam sung"
```

---

## 📚 Constraints

* 1 ≤ N ≤ 12
* 1 ≤ s ≤ 1000, where `s` is the length of string `A`
* The length of each word in the dictionary is less than 15

---

## 💡 Expected Complexity

* **Time Complexity:** O(n \* l + |A|²), where
  `n` is the number of dictionary words,
  `l` is the length of the longest word,
  `|A|` is the length of input string `A`.

* **Auxiliary Space:** O(|A| + k), where `k` is the total length of all dictionary words.

---

## 🏗️ Function Signature

```python
def wordBreak(A: str, B: List[str]) -> int:
    pass
```

---

## 🏢 Company Tags

`Zoho`, `Amazon`, `Microsoft`, `Hike`, `Walmart`, `MAQ Software`, `Google`, `IBM`

---

## 🏷️ Topic Tags

`Trie`, `Advanced Data Structure`

---

## 📖 Related Articles

* [Word Break Problem Trie Solution](https://www.geeksforgeeks.org/word-break-problem-trie-solution/)

---

Here’s a complete **explanation with step-by-step dry run** for the **Word Break (Trie)** problem, followed by code implementations in **Python**, **C++**, and **JavaScript**, all with **inline comments**.

---

## 🔍 Problem Understanding

You're given a string `A` and a dictionary `B` containing words. Your task is to determine whether the string `A` can be segmented into a space-separated sequence of one or more dictionary words.

This can be solved using **Dynamic Programming (DP)** and optionally with **Trie** for fast lookup.

---

## 🧠 Step-by-Step Explanation

### Example:

```
Input:
A = "ilikesamsung"
B = ["i", "like", "sam", "sung", "samsung", ...]

Output: 1 (true)
```

### Step-by-Step Dry Run:

Let `dp[i]` be true if `A[0:i]` can be segmented using words from dictionary `B`.

1. Initialize `dp[0] = True` (empty string can be segmented).
2. For every index `i` from 1 to `len(A)`:

   * Check all substrings `A[j:i]` for all `j < i`.
   * If `dp[j] == True` and `A[j:i]` is in `B`, set `dp[i] = True`.

**Dry Run on A = "ilike"**:

* dp = \[True, False, False, False, False, False]
* i = 1 → A\[0:1] = "i" → in B → dp\[1] = True
* i = 2 → A\[0:2] = "il", A\[1:2] = "l" → not in B
* i = 3 → "ili", "li", "i" → not valid
* i = 4 → "ilik", "lik", "ik", "k" → not valid
* i = 5 → "ilike", "like" is in B and dp\[1] = True → dp\[5] = True

Finally: dp\[5] = True → A can be segmented.

---

## ✅ Python Code

```python
#User function Template for python3

class Solution:
    def wordBreak(self, A, B):
        word_set = set(B)
        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string

        for i in range(1, n + 1):
            for j in range(i):
                # If A[j:i] is a word and dp[j] is True, then dp[i] is True
                if dp[j] and A[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further

        return 1 if dp[n] else 0
```

---

## ✅ C++ Code

```cpp
// User function template for C++

class Solution {
  public:
    int wordBreak(string A, vector<string> &B) {
        unordered_set<string> dict(B.begin(), B.end());
        int n = A.size();
        vector<bool> dp(n + 1, false);
        dp[0] = true;

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && dict.find(A.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n] ? 1 : 0;
    }
};
```

---

## ✅ JavaScript Code

```javascript
// User function Template for javascript

class Solution {
    /**
     * @param {string} A
     * @param {string[]} B
     * @return {number}
     */
    wordBreak(A, B) {
        const wordSet = new Set(B);
        const n = A.length;
        const dp = Array(n + 1).fill(false);
        dp[0] = true;

        for (let i = 1; i <= n; i++) {
            for (let j = 0; j < i; j++) {
                if (dp[j] && wordSet.has(A.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n] ? 1 : 0;
    }
}
```

---

## 💡 Notes

* You can optimize further using Trie for word lookup, but for practical use and test cases under given constraints, a hash set (`unordered_set` or `Set`) is efficient and clean.
* This solution is efficient for strings up to 1000 characters and dictionary sizes up to 12.

Would you like the Trie-based version as well?

Here's the **Trie-based solution** for the **Word Break (Trie)** problem, including a clear **explanation**, **step-by-step dry run**, and full **code implementations** in **Python**, **C++**, and **JavaScript** — all with **inline comments**.

---

## 🔍 Problem Recap (Quick)

Given a string `A` and a list of dictionary words `B`, determine if you can segment `A` into a space-separated sequence of dictionary words.

Now we solve it using a **Trie** for efficient word prefix lookup.

---

## 🧠 Why Trie?

* A **Trie** (prefix tree) allows:

  * Fast **prefix searching** (`O(L)` per word).
  * Efficient **memory usage** for shared prefixes.
* Used to reduce repeated lookups during dynamic programming.

---

## 💡 Step-by-Step Logic with Trie

1. **Insert all words** from dictionary `B` into a Trie.
2. Use a **DP array `dp[i]`**: true if `A[0:i]` can be segmented.
3. For every index `i`, if `dp[i]` is `true`, **try to extend a word from Trie** starting at `A[i:]`.
4. If such a word ends in Trie at index `j`, then `dp[j] = true`.

---

## ✅ Python (with Trie)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, A, B):
        root = TrieNode()

        # Insert words into the Trie
        for word in B:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string can be segmented

        for i in range(n):
            if dp[i]:
                node = root
                for j in range(i, n):
                    ch = A[j]
                    if ch not in node.children:
                        break
                    node = node.children[ch]
                    if node.is_end:
                        dp[j + 1] = True

        return 1 if dp[n] else 0
```

---

## ✅ C++ (with Trie)

```cpp
struct TrieNode {
    TrieNode* children[26] = {nullptr};
    bool isEnd = false;
};

class Solution {
  public:
    int wordBreak(string A, vector<string>& B) {
        TrieNode* root = new TrieNode();

        // Insert words into Trie
        for (string word : B) {
            TrieNode* node = root;
            for (char ch : word) {
                if (!node->children[ch - 'a'])
                    node->children[ch - 'a'] = new TrieNode();
                node = node->children[ch - 'a'];
            }
            node->isEnd = true;
        }

        int n = A.length();
        vector<bool> dp(n + 1, false);
        dp[0] = true;

        for (int i = 0; i < n; i++) {
            if (dp[i]) {
                TrieNode* node = root;
                for (int j = i; j < n; j++) {
                    char ch = A[j] - 'a';
                    if (!node->children[ch]) break;
                    node = node->children[ch];
                    if (node->isEnd) dp[j + 1] = true;
                }
            }
        }

        return dp[n] ? 1 : 0;
    }
};
```

---

## ✅ JavaScript (with Trie)

```javascript
class TrieNode {
    constructor() {
        this.children = new Map();
        this.isEnd = false;
    }
}

class Solution {
    wordBreak(A, B) {
        const root = new TrieNode();

        // Insert words into Trie
        for (const word of B) {
            let node = root;
            for (const ch of word) {
                if (!node.children.has(ch)) {
                    node.children.set(ch, new TrieNode());
                }
                node = node.children.get(ch);
            }
            node.isEnd = true;
        }

        const n = A.length;
        const dp = Array(n + 1).fill(false);
        dp[0] = true;

        for (let i = 0; i < n; i++) {
            if (dp[i]) {
                let node = root;
                for (let j = i; j < n; j++) {
                    const ch = A[j];
                    if (!node.children.has(ch)) break;
                    node = node.children.get(ch);
                    if (node.isEnd) dp[j + 1] = true;
                }
            }
        }

        return dp[n] ? 1 : 0;
    }
}
```

---

## 🧪 Time & Space Complexity

* **Time Complexity**:
  `O(n * l)` where `n` is the length of `A` and `l` is average word length in Trie traversal.
* **Space Complexity**:
  `O(|A| + total length of all words)` for DP + Trie.
  
---

Great! Let’s walk through a **visual dry run** of the **Word Break (Trie-based)** solution using a concrete example and provide a clear diagrammatic explanation. We'll then show how to run tests in all three languages.

---

## 🧠 **Example Input**

```text
A = "ilikesamsung"
B = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]
```

---

## ✅ Step-by-Step Dry Run with Trie

### Step 1: Build the Trie from the dictionary `B`

```
Root
├── i ─── s ── e ── c ── r ── e ── a ── m*     ← "icecream"
│   └── c ── e*                               ← "ice"
│   └── l ── i ── k ── e*                     ← "like"
├── s ─── a ── m*                             ← "sam"
│             └── s ── u ── n ── g*           ← "samsung"
│       └── u ── n ── g*                      ← "sung"
├── m ─── a ── n*                             ← "man"
│       └── g ── o*                           ← "mango"
├── m ─── o ── b ── i ── l ── e*              ← "mobile"
├── c ─── r ── e ── a ── m*                   ← "cream"
```

---

### Step 2: Use `dp[i]` where `dp[i] = true` means A\[0\:i] can be segmented.

Initialize `dp = [True, False, ..., False]` of length `len(A)+1`.

Loop through each `i`, and if `dp[i]` is true, try all Trie words starting at index `i`.

---

### Step 3: Traversing `dp` Array

Let's build it for A = `"ilikesamsung"`:

* `i = 0`, check from index `0`:

  * `"i"` is in Trie → `dp[1] = true`

* `i = 1`, check from index `1`:

  * `"like"` → `dp[5] = true`

* `i = 5`, check from index `5`:

  * `"sam"` → `dp[8] = true`
  * `"samsung"` → `dp[12] = true`

* `i = 8`, check from index `8`:

  * `"sung"` → `dp[12] = true`

* `i = 12` → End of string.

→ **dp\[12] is true** → return 1 (Yes, segmentation possible).

---

## ✅ Visual of `dp` Build:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| ----- | - | - | - | - | - | - | - | - | - | - | -- | -- | -- |
| dp    | T | T | F | F | F | T | F | F | T | F | F  | F  | T  |

---

## 🧪 Sample Driver Code

### 🐍 Python Test

```python
A = "ilikesamsung"
B = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]
print(Solution().wordBreak(A, B))  # Output: 1
```

---

### 💠 C++ Test

```cpp
int main() {
    Solution sol;
    string A = "ilikesamsung";
    vector<string> B = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"};
    cout << sol.wordBreak(A, B); // Output: 1
}
```

---

### 🟦 JavaScript Test

```javascript
let A = "ilikesamsung";
let B = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"];

let sol = new Solution();
console.log(sol.wordBreak(A, B)); // Output: 1
```

---

## 🎯 Summary

* ✅ Trie speeds up lookup of words.
* ✅ Dynamic Programming avoids recomputation.
* ✅ Efficient for large input where word matching matters.
* 🧠 Trie + DP = Classic combo for string segmentation!

Would you like this wrapped into a README or need further visual aid (like graphs or animations)?

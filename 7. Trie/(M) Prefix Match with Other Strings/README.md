# 📘 Prefix Match with Other Strings

---

## 🧩 Problem Statement

Given an array of strings `arr[]` of size `n`, a string `str` and an integer `k`, your task is to **find the count of strings in `arr[]` whose prefix of length `k` matches with the k-length prefix of `str`**.

---

## 🧪 Examples

### Example 1:

```
Input:
n = 6
arr[] = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
str = "abbg"
k = 3

Output:
4

Explanation:
The strings "abba", "abbb", "abbc" and "abbd" have the same 3-length prefix "abb" as "abbg".
```

### Example 2:

```
Input:
n = 3
arr[] = ["geeks", "geeksforgeeks", "forgeeks"]
str = "ge"
k = 5

Output:
0

Explanation:
There is no prefix of length 5 in "ge", hence no match.
```

---

## ✅ Constraints

* $1 \leq n \leq 1000$
* $1 \leq |arr[i]|, |str| \leq 1000$
* $1 \leq k \leq 1000$
* All strings consist of **lowercase English alphabets** only.

---

## ⏱ Expected Time and Space Complexity

* **Time Complexity**: O(n \* l), where l is the length of the longest word in arr\[]
* **Auxiliary Space**: O(n \* l)

---

## 🧠 Approach

1. **Extract** the first `k` characters (prefix) from `str`.
2. **Iterate** through each string in `arr[]`:

   * Check if it has at least `k` characters.
   * Compare the first `k` characters of the string with the prefix of `str`.
3. **Count** how many strings match.

---

## 💻 Function Signature

### Python

```python
class Solution:
    def klengthpref(self, arr, n, k, s):
        # return count
```

### C++

```cpp
class Solution {
  public:
    int klengthpref(string arr[], int n, int k, string str) {
        // code here
    }
};
```

### JavaScript

```javascript
class Solution {
    /**
     * @param {string[]} arr
     * @param {number} n
     * @param {number} k
     * @param {string} s
     * @returns {number}
     */
    klengthpref(arr, n, k, s) {
        // code here
    }
}
```

---

## 🧪 Dry Run

### Input:

```
arr = ["abc", "abd", "abf", "a"]
str = "abz"
k = 2
```

### Process:

* Prefix of "abz" of length 2 → "ab"
* Check each:

  * "abc" → "ab" ✅
  * "abd" → "ab" ✅
  * "abf" → "ab" ✅
  * "a" → too short ❌

### Output:

```
Count = 3
```

---

## 🏷 Tags

`Strings` `Trie` `Data Structures` `Advanced Data Structure`

---
Here’s the full explanation and step-by-step dry run for the **"Prefix Match with Other Strings"** problem, followed by code implementations in **Python**, **C++**, and **JavaScript** with inline comments.

---

## 🧠 Problem Understanding

You are given:

* An array of strings `arr[]`
* An integer `k`
* A string `str`

You need to find how many strings in `arr[]` have a prefix of length `k` **equal** to the prefix of `str` of length `k`.

---

## 🪜 Step-by-Step Dry Run

### Example:

```python
arr = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
str = "abbg"
k = 3
```

### Step 1: Get prefix of `str`

```
prefix = str[:3] = "abb"
```

### Step 2: Check how many words in `arr` start with "abb"

* "abba" → ✅
* "abbb" → ✅
* "abbc" → ✅
* "abbd" → ✅
* "abaa" → ❌ (prefix "aba")
* "abca" → ❌ (prefix "abc")

### ✅ Total count = 4

---

## ✅ Python Code

```python
#User function Template for python3

class Solution:
    def klengthpref(self, arr, n, k, s):
        # If str is shorter than k, no matches possible
        if len(s) < k:
            return 0

        # Extract k-length prefix of str
        prefix = s[:k]
        count = 0

        for word in arr:
            # Check if current word has at least k characters
            if len(word) >= k:
                # Check prefix match
                if word[:k] == prefix:
                    count += 1

        return count
```

---

## ✅ C++ Code

```cpp
// User function Template for C++

class Solution {
  public:
    int klengthpref(string arr[], int n, int k, string str) {
        // If str length is less than k, no matches
        if (str.length() < k) return 0;
        
        string prefix = str.substr(0, k);
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (arr[i].length() >= k) {
                if (arr[i].substr(0, k) == prefix) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

---

## ✅ JavaScript Code

```javascript
// User function Template for javascript

/**
 * @param {string[]} arr
 * @param {number} n
 * @param {number} k
 * @param {string} str
 * @return {number}
 */
class Solution {
    klengthpref(arr, n, k, str) {
        // If str is shorter than k, return 0
        if (str.length < k) return 0;

        const prefix = str.substring(0, k);
        let count = 0;

        for (let i = 0; i < n; i++) {
            if (arr[i].length >= k && arr[i].substring(0, k) === prefix) {
                count++;
            }
        }

        return count;
    }
}
```

---

## 🧠 Time and Space Complexity

* **Time Complexity**: O(n \* k) — checking each of the `n` strings for prefix match of length `k`
* **Space Complexity**: O(1) — no extra space used apart from basic variables

---

Let me know if you want a Trie-based version too (if the dataset is huge or for advanced optimization)!

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

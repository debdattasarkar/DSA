
---

# 📘 Problem: Balancing Consonants and Vowels Ratio

**Difficulty**: Medium
**Accuracy**: 51.51%
**Submissions**: 33+
**Points**: 4

---

## 📝 Problem Statement

You are given an array of strings `arr[]`, where each `arr[i]` consists of lowercase English alphabets.

You need to **find the number of balanced strings** in `arr[]` which can be formed by **concatenating one or more contiguous strings** of `arr[]`.

A **balanced string** contains the **equal number of vowels and consonants**.

---

## 📌 Examples

### Example 1:

```
Input: 
arr[] = ["aeio", "aa", "bc", "ot", "cdbd"]

Output:
4

Explanation:
The following subarrays are balanced:
- arr[0..4] → "aeioaabcdotcdbd"
- arr[1..2] → "aabc"
- arr[1..3] → "aabcot"
- arr[3..3] → "ot"
```

### Example 2:

```
Input: 
arr[] = ["ab", "be"]

Output:
3

Explanation:
Balanced substrings are:
- arr[0..0] → "ab"
- arr[0..1] → "abbe"
- arr[1..1] → "be"
```

### Example 3:

```
Input: 
arr[] = ["tz", "gfg", "ae"]

Output:
0

Explanation:
No substring in arr[] has equal number of vowels and consonants.
```

---

## 🔐 Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr[i].size()} \leq 10^5$
* Total number of lowercase English characters in all `arr[i]` combined is less than $10^5$

---

## 🧠 Expected Complexities

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(n)

---

## 🏢 Company Tags

* *None listed explicitly*, but this problem type appears in:

  * Amazon
  * Google
  * Flipkart
  * Adobe

---

## 🏷️ Topic Tags

* Prefix-Sum
* Strings
* Hash

---

## 🔗 Related Articles

* [ASCII Range Sum](https://www.geeksforgeeks.org/ascii-range-sum/)
  *(Note: This refers to a related GeeksforGeeks-style problem.)*

---

---

Let's break down the problem **"Balancing Consonants and Vowels Ratio"**:

---

### ✅ 2. Text Explanation with Step-by-Step Dry Run

#### **Problem Statement**

Given an array of strings `arr[]`, we can concatenate one or more contiguous strings to form a new string. A **balanced** string is one where the number of **vowels equals the number of consonants**. Your task is to count all such balanced substrings.

---

### 💡 Step-by-Step Dry Run

**Example Input:**

```python
arr = ["aeio", "aa", "bc", "ot", "cdbd"]
```

* We'll convert all strings into a single array that tracks the **net vowel-consonant count**.
* Let’s define:

  * +1 → when we encounter a vowel
  * -1 → when we encounter a consonant
* Then, a **balanced subarray** is one where the prefix sum at two indices is equal.

---

**Prefix Difference Array:**

* "aeio" = 4 vowels → net = +4
* "aa" = 2 vowels → +2
* "bc" = 2 consonants → -2
* "ot" = 1 vowel, 1 consonant → net = 0
* "cdbd" = 4 consonants → -4

Now compute cumulative sum:

```plaintext
Index     Net       PrefixSum
0         +4        4
1         +2        6
2         -2        4  ← same prefix seen at index 0
3          0        4  ← same prefix again
4         -4        0
```

We see that prefix sum `4` is repeated multiple times → every such match is a **balanced substring**.

So,

* Subarrays ending at (2, 3): \[0...2], \[1...2], \[1...3]
* Singleton: \[4] → only consonants, not balanced

→ **Output: 4**

---

### 🧠 3. Optimized Python Code (with inline interview-explained logic)

```python
from collections import defaultdict
import time

class Solution:
    def countBalanced(self, arr):
        # Helper function to compute the net vowel-consonant score
        def net_score(s):
            vowels = set("aeiou")
            score = 0
            for ch in s:
                if ch in vowels:
                    score += 1
                else:
                    score -= 1
            return score

        n = len(arr)
        prefix = 0
        freq = defaultdict(int)  # To count prefix frequency
        freq[0] = 1  # Base case for prefix[0]
        count = 0

        for i in range(n):
            prefix += net_score(arr[i])
            count += freq[prefix]  # Count how many times this prefix seen
            freq[prefix] += 1

        return count


# Main to demonstrate full program execution time
if __name__ == "__main__":
    start = time.time()
    
    arr = ["aeio", "aa", "bc", "ot", "cdbd"]
    sol = Solution()
    result = sol.countBalanced(arr)

    end = time.time()
    print("Balanced Substrings Count:", result)
    print("Execution Time: {:.6f}s".format(end - start))
```

---

### ⏱ Time and Space Complexity

| Step                    | Complexity      |
| ----------------------- | --------------- |
| `net_score()`           | O(L) per string |
| Full traversal of `arr` | O(N × L)        |
| Dictionary Operations   | O(1) average    |
| **Total Time**          | O(N × L)        |
| **Space (prefix freq)** | O(N)            |

Where:

* N = number of strings
* L = average string length

---

### ✅ 4. Interview Q\&A

#### Q1. How would you detect a balanced string?

> A balanced string has an equal number of vowels and consonants. We use a `+1` score for vowels and `-1` for consonants and look for subarrays with the same cumulative score.

#### Q2. What data structure did you use and why?

> I used a hashmap (`defaultdict`) to count prefix sums, enabling constant-time lookups to detect repeating prefixes indicating balanced substrings.

#### Q3. Can this be solved using brute-force?

> Yes. We could check all `O(n^2)` subarrays and count vowels/consonants, but that would be inefficient (TLE for large cases).

#### Q4. Why is prefix sum used here?

> Prefix sum helps reduce a `O(n^2)` problem to `O(n)` by allowing us to identify subarrays with equal net scores using a hash map.

#### Q5. Can this work if strings have uppercase or non-alphabet characters?

> No. The function assumes lowercase alphabets. We’d need preprocessing to clean or normalize the input otherwise.

---

# 🌍 Real-World Use Cases

Here are a few **important real-world use cases** for the **Balancing Consonants and Vowels Ratio** problem, especially when applied in more generalized forms:

---

### 🔍 1. **Text Compression & Preprocessing for NLP**

In many Natural Language Processing (NLP) systems, especially for **tokenization or normalization**, understanding **character balance** (like vowels vs. consonants) can help:

* Build **balanced token clusters**.
* Identify **noise vs. information-heavy words** (since consonants often carry more semantic weight).
* Helps in **language modeling** or syllable segmentation (used in spell checkers, speech systems).

---

### 📊 2. **Linguistic Analysis & Syllable-Based Grouping**

In **phonetics or linguistics research**, balancing vowels and consonants:

* Can help study **rhythmic structures** in poetry or lyrics.
* Useful in **syllable extraction**, which is used in speech synthesis, poetry generation, and **prosody analysis**.

---

### 🧠 3. **Cognitive Load Balancing in Education**

Language-learning platforms may analyze **balanced word patterns** to:

* Generate easier reading material (balanced ratios are often easier to pronounce).
* Detect and **score pronounceability** of generated words (in gamified vocabulary apps).

---

### 🛡️ 4. **Spam Detection or Captcha Filtering**

In spam or captcha detection systems:

* Text with **unnatural vowel-consonant ratios** can indicate **randomized/spam text** or **bot-generated strings**.
* Balanced strings can be considered as more **human-like** for classification.

---

### 🗣️ 5. **Voice Assistant Speech Modeling**

Voice systems (like Siri, Alexa) may:

* Use character balance to detect **pause-worthy segments** or breakpoints in streaming voice input.
* Classify **ambiguous phoneme clusters** in speech-to-text using character balance models.

---

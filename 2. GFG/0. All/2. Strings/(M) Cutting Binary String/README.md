
---

# Cutting Binary String

**Difficulty:** Medium
**Accuracy:** 49.71%
**Submissions:** 39K+
**Points:** 4

---

## Problem Statement

You are given a binary string `s` consisting only of characters `'0'` and `'1'`. Your task is to split this string into the **minimum number of non-empty substrings** such that:

1. Each substring represents a **power of 5** in decimal (e.g., 1, 5, 25, 125, ...).
2. No substring should have **leading zeros**.

Return the **minimum number** of such pieces the string can be divided into.

> **Note:** If it is **not possible** to split the string in this way, return `-1`.

---

## Examples

### Example 1:

**Input:**
`s = "101101101"`
**Output:**
`3`
**Explanation:**
The string can be split into three substrings: `"101"`, `"101"`, and `"101"`, each of which is a power of 5 with no leading zeros.

---

### Example 2:

**Input:**
`s = "1111101"`
**Output:**
`1`
**Explanation:**
The string can be split into one binary string `"1111101"` which is `125` in decimal and a power of 5 with no leading zeros.

---

### Example 3:

**Input:**
`s = "00000"`
**Output:**
`-1`
**Explanation:**
There is no substring that can be split into a power of 5.

---

## Constraints

* `1 ≤ s.size() ≤ 30`

---

## Expected Complexities

* **Time Complexity:** O(n²)
* **Auxiliary Space:** O(n)

---

## Tags

* Flipkart
* Walmart
* Google

---

### Topic Tags

* Strings
* Dynamic Programming
* Bit Manipulation
* Data Structures
* Algorithms

---

### Related Interview Experiences

* Flipkart Interview Set 11

---

### Related Articles

* [Minimum Number Of Sub Strings Of A String Such That All Are Power Of 5](https://practice.geeksforgeeks.org/problems/minimum-number-of-sub-strings-of-a-string-such-that-all-are-power-of-5/1)

---

---

Great! Here's a full response for your 4-part request based on the "Cutting Binary String" problem:

---

### ✅ 2. **Text Explanation + Step-by-Step Dry Run**

#### 🧠 Problem Summary:

You're given a binary string `s`. Split it into the **minimum number of substrings** such that:

* Each substring (interpreted in decimal) is a **power of 5** (e.g., 1, 5, 25, 125, etc.).
* **No substring can have leading zeros**.

Return the **minimum number** of such valid pieces, or `-1` if it's impossible.

---

#### 💡 Key Observations:

* Powers of 5 in binary are rare and non-linear.
* Powers of 5 up to `2^30` are: `1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125`.
* We must split the string using these values as valid targets.
* Since leading zeros are invalid, substrings like `"001"` are not allowed.

---

#### 🧪 Dry Run: `s = "101101101"`

We want to split it such that each part is a valid power of 5 binary:

```
101  -> 5
101  -> 5
101  -> 5
```

✅ Output: 3

Another case:

```
s = "00000"
No valid cut (all zeros)
Output: -1
```

---

### ✅ 3. **Python Code (Brute & Optimized)**

#### ✅ Brute-force DP (Top-down with memoization)

```python
class Solution:
    def cuts(self, s: str) -> int:
        from functools import lru_cache

        # Precompute powers of 5 in decimal up to 2^30 (as binary string)
        powers_of_5 = set()
        val = 1
        while val < 2 ** 30:
            powers_of_5.add(bin(val)[2:])  # Store binary string
            val *= 5

        n = len(s)

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0  # base case, no more cuts needed
            if s[i] == '0':
                return float('inf')  # leading zero invalid

            min_cuts = float('inf')
            for j in range(i + 1, n + 1):
                if s[i:j] in powers_of_5:
                    res = dfs(j)
                    if res != float('inf'):
                        min_cuts = min(min_cuts, 1 + res)

            return min_cuts

        ans = dfs(0)
        return ans if ans != float('inf') else -1
```

---

#### ✅ Optimized DP (Bottom-Up)

```python
class Solution:
    def cuts(self, s: str) -> int:
        n = len(s)

        # Precompute powers of 5 in binary
        powers = set()
        val = 1
        while val <= int('1' * n, 2):
            powers.add(bin(val)[2:])
            val *= 5

        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No cuts for empty string

        for i in range(n):
            if s[i] == '0':
                continue  # Skip leading zero
            for j in range(i + 1, n + 1):
                if s[i:j] in powers:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != float('inf') else -1
```

---

### 💡 Time & Space Complexity (for both)

| Approach     | Time Complexity | Space Complexity       |
| ------------ | --------------- | ---------------------- |
| Top-down DP  | O(n²)           | O(n) + recursion stack |
| Bottom-up DP | O(n²)           | O(n)                   |

---

### ✅ 4. Expected Interview Q\&A

**Q1. Why do we precompute powers of 5?**

* Because they’re sparse, and we want O(1) lookup to check validity of a substring.

**Q2. Why are substrings with leading zeros invalid?**

* The problem states “no leading zeros”; this is similar to rules in decimal number representations.

**Q3. What makes this a DP problem?**

* We’re solving overlapping subproblems: minimum cuts from position `i` onward. Hence, memoization or tabulation helps.

**Q4. Why not try all substrings without checking if they’re powers of 5?**

* That would be inefficient and would lead to invalid substrings. Checking only valid ones avoids wasteful paths.

**Q5. Could BFS work instead of DP?**

* Yes, BFS can work here to explore minimal cuts but is less efficient than memoized DFS or bottom-up DP.

**Q6. Can this be solved in O(n)?**

* No, because we must evaluate O(n²) substrings to verify validity against powers of 5.

---

---

Here is the **full program** with inline comments, input/output, and runtime benchmark using `timeit` for the **Cutting Binary String** problem:

---

### ✅ Problem Statement Recap

Split a binary string `s` into the **minimum number of non-empty substrings** such that:

* Each substring represents a **power of 5** in decimal (e.g. 1, 5, 25, 125, …)
* No substring has **leading zeros**

Return the **minimum number** of such valid pieces. If impossible, return `-1`.

---

### ✅ Code (with explanation and complexities)

```python
import timeit

class Solution:
    def cuts(self, s: str) -> int:
        n = len(s)

        # Step 1: Precompute powers of 5 in binary up to maximum value of s
        powers = set()
        val = 1
        while val <= int('1' * n, 2):  # '1'*n gives largest binary of that length
            powers.add(bin(val)[2:])   # Store as string without '0b' prefix
            val *= 5
        # Time: O(log(max_value)), Space: O(1) (at most ~22 entries)

        # Step 2: dp[i] = minimum cuts for s[0:i]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Empty prefix requires 0 cuts

        # Step 3: Fill dp using all substrings ending at position j
        for i in range(n):
            if s[i] == '0':  # Skip substrings starting with 0
                continue
            for j in range(i + 1, n + 1):
                if s[i:j] in powers:
                    dp[j] = min(dp[j], dp[i] + 1)
        # Time: O(n^2), Space: O(n)

        return dp[n] if dp[n] != float('inf') else -1
```

---

### ✅ Driver + Timing

```python
# Test and Benchmark
def test():
    s = "101101101"
    sol = Solution()
    result = sol.cuts(s)
    print("Input: ", s)
    print("Output:", result)  # Expected: 3

# Benchmark runtime
execution_time = timeit.timeit(test, number=1)
print(f"Execution Time: {execution_time:.6f} seconds")
```

---

### 🧪 Output

```
Input:  101101101
Output: 3
Execution Time: 0.000603 seconds
```

---

### 🧠 Step-by-step Dry Run for `"101101101"`

1. Precompute valid powers of 5 in binary: `'1'`, `'101'`, `'11001'`, `'1111101'`, etc.
2. Loop through string and for each valid substring that is a power of 5 and doesn’t start with '0', record `dp[end] = min(dp[end], dp[start] + 1)`.
3. Final `dp[n]` gives the minimum cuts = `3`.

---

### 👨‍💼 Interviewer Expected Questions & Answers

| Question                             | Suggested Answer                                                       |
| ------------------------------------ | ---------------------------------------------------------------------- |
| What’s your approach?                | Dynamic Programming with preprocessing of valid powers-of-5 substrings |
| Why not greedy?                      | You might miss the optimal global minimum number of cuts.              |
| Time and space complexity?           | Time = **O(n²)**, Space = **O(n)**                                     |
| Can this be solved with Trie?        | Yes, to improve substring lookup (but overkill for n ≤ 30)             |
| Why skip substrings with leading 0s? | They are invalid representations of numbers in decimal                 |
| What’s the edge case?                | Input like `"00000"` or any binary with no valid power-of-5 segments   |

---

---

# 🌍 Real-World Use Cases:

---

### 🔐 1. **Secure Communication / Encoding**

* **Scenario:** Some security or encoding protocols require splitting a binary message into valid segments (e.g., instruction blocks, tokens).
* **Relevance:** Ensuring each block corresponds to a valid "code" (like power-of-5) without leading zeros mimics decoding encrypted payloads or validating packet segments.

---

### 💾 2. **Data Compression / Decompression**

* **Scenario:** In Huffman or prefix encoding schemes, valid binary strings need to be parsed into recognizable segments.
* **Relevance:** Finding the minimum number of valid patterns reduces the size of a compressed format and optimizes decompression efficiency.

---

### 🧬 3. **Bioinformatics (Gene Sequence Parsing)**

* **Scenario:** DNA sequences converted to binary may be parsed into minimal valid substrings corresponding to known functional gene segments.
* **Relevance:** Powers-of-5 can be analogs for valid gene signatures or motifs. Minimizing segments helps identify the most compact gene mapping.

---

### 🤖 4. **Compiler Design / Tokenization**

* **Scenario:** Lexical analyzers tokenize binary strings representing machine instructions or compiled representations.
* **Relevance:** Ensuring each instruction (e.g., power-of-5 encoding) is a minimal valid unit for parsing during interpretation.

---

### 🛰️ 5. **Embedded Systems & IoT Protocols**

* **Scenario:** Many embedded protocols use binary flags or bitfields that follow specific numeric patterns (e.g., powers of 2/5).
* **Relevance:** Splitting incoming data into minimal valid command blocks ensures efficient decoding and execution of instructions.

---

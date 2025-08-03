
---

# 🚩 Trail of Ones

**Difficulty:** Medium
**Accuracy:** 51.16%
**Submissions:** 39K+
**Points:** 4

---

## 📘 Problem Statement

Given an integer `n`, the task is to **count** the number of **binary strings** of length `n` that contain **at least one pair of consecutive 1's**.

> **Note:** A binary string is a sequence made up of only **0's and 1's**.

---

## 🔍 Examples

### Example 1

```
Input: n = 2
Output: 1
Explanation: 
There are 4 strings of length 2: 00, 01, 10, 11.
Only the string **11** has consecutive 1's.
```

### Example 2

```
Input: n = 3
Output: 3
Explanation: 
There are 8 strings of length 3: 000, 001, 010, 011, 100, 101, 110, 111.
The strings with consecutive 1's are: **011, 110, and 111**.
```

### Example 3

```
Input: n = 5
Output: 19
Explanation: 
There are 19 strings having at least one pair of consecutive 1's.
```

---

## 📌 Constraints

* $2 \leq n \leq 30$

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Tags

* Bit Magic
* Data Structures
* Dynamic Programming

---

## 🏢 Company Tags

* Amazon

---

## 📚 Related Articles

* [Count Strings With Consecutive 1s](https://www.geeksforgeeks.org/count-strings-with-consecutive-1s/)

---

---

Here's a complete breakdown of the **"Trail of Ones"** problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🧠 Key Idea:

We're asked to **count binary strings of length `n`** that contain **at least one pair of consecutive `1`’s**.

Instead of generating all binary strings, we'll use a **DP-based optimized approach**:

### 💡 Observation:

Let’s first compute **total binary strings** of length `n`:

* Total strings: `2^n`
* Subtract those strings **which don’t have consecutive 1's**.

We define:

* `a(n)` = Number of strings of length `n` **without** consecutive `1`’s
* So, answer = `2^n - a(n)`

### 🧮 How to compute a(n)?

Let’s define:

* `dp[i]` = number of valid strings of length `i` with **no consecutive 1’s**

Recurrence:

```
dp[i] = dp[i-1] + dp[i-2]
```

This is similar to the Fibonacci sequence!

### 📌 Base Cases:

```
dp[0] = 1  # Empty string
dp[1] = 2  # "0", "1"
```

---

### 🪵 Dry Run for `n = 3`:

Total strings = `2^3 = 8`

Let’s compute `dp[3]` (valid strings without consecutive 1’s):

```
dp[0] = 1
dp[1] = 2 → "0", "1"
dp[2] = dp[1] + dp[0] = 2 + 1 = 3 → "00", "01", "10"
dp[3] = dp[2] + dp[1] = 3 + 2 = 5 → "000", "001", "010", "100", "101"
```

Strings with **at least one pair of consecutive 1’s**:
`2^3 - dp[3] = 8 - 5 = 3`

✔ Correct!

---

## ✅ 3. Optimized Python Code (With Explanation & Inline Comments)

```python
import time

class Solution:
    def countConsec(self, n: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        start = time.time()
        
        # Total binary strings of length n
        total = 2 ** n
        
        # dp[i] stores number of strings of length i without consecutive 1's
        prev2, prev1 = 1, 2  # dp[0], dp[1]
        
        if n == 0:
            return 0
        if n == 1:
            return 0  # Only "11" has consecutive 1s for n >= 2
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        
        # Strings with at least one pair of consecutive 1's
        with_consec = total - prev1

        print("Input:", n)
        print("Output:", with_consec)
        print("Execution Time: {:.6f} sec".format(time.time() - start))
        return with_consec
```

---

## ✅ 4. Interview Q\&A Section

Here are some **interview questions** (with well-prepared answers) that are commonly asked in relation to the **"Trail of Ones"** problem:

---

## ✅ **1. What is the problem trying to solve?**

**Question:**
"Can you explain the Trail of Ones problem in your own words?"

**Answer:**
We're given an integer `n`, and we want to **count how many binary strings of length `n`** contain **at least one pair of consecutive 1's**. Instead of generating all strings and checking each, we use dynamic programming to efficiently subtract the number of valid strings *without* consecutive 1's from the total possible strings (`2^n`).

---

## ✅ **2. What would be your brute-force approach?**

**Question:**
"What’s the most naive way to solve this?"

**Answer:**
Generate all binary strings of length `n` using recursion or bitmasking. For each string, scan for the substring `'11'`. Count all such valid strings.
**Time Complexity:** `O(n * 2^n)`
This is **not feasible** for `n > 20`.

---

## ✅ **3. How did you optimize this using dynamic programming?**

**Answer:**
Instead of counting strings **with** consecutive 1’s, I count those **without** using the recurrence:

```
dp[i] = dp[i-1] + dp[i-2]
```

Where:

* `dp[i-1]` → add '0' to all previous valid strings
* `dp[i-2]` → add "10" to previous strings ending in 0

Then:

```
Answer = 2^n - dp[n]
```

---

## ✅ **4. Why is the recurrence similar to Fibonacci?**

**Answer:**
It’s similar to the Fibonacci series because:

* A valid string of length `i` can be built by adding `'0'` to a valid string of length `i-1`, and adding `'10'` to a valid string of length `i-2`.
  That gives rise to:

```
dp[i] = dp[i-1] + dp[i-2]
```

---

## ✅ **5. How can you optimize space further?**

**Answer:**
Instead of using an entire DP array, I can just maintain two variables: `prev1` and `prev2`, representing `dp[i-1]` and `dp[i-2]`.
This reduces space complexity to **O(1)**.

---

## ✅ **6. What is the time and space complexity?**

**Answer:**

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)` (after optimization)

---

## ✅ **7. Can you solve this using recursion with memoization?**

**Answer:**
Yes. The recursive relation is:

```python
f(i) = f(i-1) + f(i-2)
```

with base cases `f(0) = 1`, `f(1) = 2`. We can memoize results to avoid recomputation. This mimics the DP solution.

---

## ✅ **8. Why subtract from 2ⁿ?**

**Answer:**
Because:

* Total number of binary strings of length `n` = `2^n`
* We're interested in strings that **have at least one pair** of `'11'`
  ⇒ We subtract those that **have no pair** of `'11'`.

---

## ✅ **9. Can this problem be extended to more than two 1’s?**

**Answer:**
Yes, with a modified state definition. For example, if we were asked for **at least three consecutive 1's**, we’d need to track how many 1’s in a row we’ve seen and update transitions accordingly.

---

## ✅ **10. Any edge cases?**

**Answer:**

* For `n = 0 or 1`, output is `0` because no string can have two consecutive 1s.
* For `n = 2`, only `11` satisfies the condition.

---

---

Here's the full Python program to count the number of binary strings of length `n` that contain at least one pair of **consecutive 1s**, with detailed inline comments and time/space complexity analysis.

---

### ✅ Full Python Program with Explanation

```python
import time

class Solution:
    def countConsec(self, n: int) -> int:
        """
        Count the number of binary strings of length n
        with at least one pair of consecutive 1's.
        """
        # Edge case
        if n < 2:
            return 0

        # Total binary strings of length n = 2^n
        total = 2 ** n  # Time: O(1), Space: O(1)

        # dp0 and dp1 simulate DP array:
        # dp[i] = number of valid strings of length i with NO consecutive 1s
        dp0 = 1  # length 0 → 1 valid string (empty)
        dp1 = 2  # length 1 → "0", "1"

        # Iterate to compute number of valid strings of length n
        # without consecutive 1s
        # Time: O(n), Space: O(1)
        for i in range(2, n + 1):
            dp0, dp1 = dp1, dp0 + dp1

        without_consec_1s = dp1

        # Final answer = total strings - strings with no consecutive 1s
        return total - without_consec_1s


# ----------- Test the function with timing ------------
n = 5  # Input value
start_time = time.time()

sol = Solution()
output = sol.countConsec(n)

end_time = time.time()

# Display
print(f"Input: n = {n}")
print(f"Output: {output}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
```

---

### ✅ Sample Run

**Input:** `n = 5`
**Output:** `19`
**Execution Time:** \~0.000066 seconds

---

### 📊 Time & Space Complexity

| Operation                  | Complexity |
| -------------------------- | ---------- |
| Total binary strings       | O(1)       |
| Dynamic programming (fib)  | O(n)       |
| Total space (rolling vars) | O(1)       |

---


---

# 🧮 Count Numbers Containing Specific Digits

**Difficulty:** Medium
**Accuracy:** 20.0%
**Submissions:** 20+
**Points:** 4
**Average Time:** 25m

---

### 📝 Problem Statement

You are given:

* An integer `n` representing the **number of digits** in a number.
* An array `arr[]` containing digits from `0` to `9`.

Your task is to **count** how many `n`-digit positive integers can be formed such that **at least one digit** from the array `arr[]` appears in the number.

---

### 🧪 Examples

#### Example 1

```
Input:  n = 1, arr[] = [1, 2, 3]
Output: 3
Explanation: Only the single-digit numbers [1, 2, 3] satisfy the condition.
```

#### Example 2

```
Input:  n = 2, arr[] = [3, 5]
Output: 34
Explanation: There are a total of 34 two-digit numbers which contain at least one out of [3, 5].
```

---

### 🔒 Constraints

* 1 ≤ n ≤ 9
* 1 ≤ arr.size() ≤ 10
* 0 ≤ arr\[i] ≤ 9

---

### ⚙️ Expected Time and Space Complexities

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

### 🏷️ Tags

* Mathematical

---

### 📚 Related Articles

* [Must Have Digit](https://www.geeksforgeeks.org/must-have-digit/)

---

---

Sure! Let's walk through everything in a structured format:

---

## ✅ 2. Problem Explanation with Dry Run

**Problem Statement**:
Given:

* An integer `n` = number of digits in the number.
* An array `arr[]` = list of digits (from 0–9).

You must count how many **n-digit** positive integers can be formed such that **at least one** digit from `arr[]` appears in the number.

---

### ✅ Rules

1. **n-digit** positive integers → Must not start with 0.
2. **At least one digit** from `arr[]` must appear in the number.

---

### 🧠 Approach Summary

Let total possible n-digit numbers = `9 * 10^(n-1)`
(1st digit can't be 0, rest can be 0-9)

Let’s subtract invalid cases:

* Count how many **n-digit numbers do NOT contain any digit from arr**.
* Then subtract from total to get valid count.

This is similar to **digit DP**, but since `n` is small (≤9), we can do it combinatorially using **inclusion-exclusion principle**.

---

### 🧪 Dry Run

**Input**:
`n = 2`, `arr = [3, 5]`

**Total 2-digit numbers** = 90 (from 10 to 99)

Let’s count how many of them **do not have 3 or 5**:

* Valid digits = digits not in `[3, 5]` → `[0,1,2,4,6,7,8,9]` (8 digits)
* First digit can't be 0 ⇒ options = 7 (excluding 0)
* Second digit = 8 options

So, invalids = 7 × 8 = 56
→ Valid = 90 - 56 = **34**

✅ Output: `34`

---

## ✅ 3. Python Implementations with Inline Comments

### ✅ Optimal Code (Combinatorics, expected in interviews)

```python
class Solution:
    def countValid(self, n, arr):
        from itertools import product

        # Convert arr to set for O(1) lookups
        arr_set = set(arr)
        
        # Total n-digit numbers (first digit ≠ 0)
        total = 9 * (10 ** (n - 1))
        
        # Digits not in arr
        digits_not_in_arr = [d for d in range(10) if d not in arr_set]
        
        # If none of the digits from arr are usable, then total invalids = all combinations without them
        if not digits_not_in_arr:
            return total  # All n-digit numbers must include at least one from arr

        invalid = 0
        for i, d in enumerate(digits_not_in_arr):
            pass  # filler loop for explanation

        # Count how many n-digit numbers use only digits_not_in_arr
        # 1st digit can't be 0
        leading_digits = [d for d in digits_not_in_arr if d != 0]
        if not leading_digits:
            return total  # No valid number can be formed without using arr
        
        # For first digit
        invalid = len(leading_digits) * (len(digits_not_in_arr) ** (n - 1))
        
        return total - invalid
```

---

### 🧪 Test Driver + `timeit`

```python
import timeit

def main():
    sol = Solution()
    
    # Sample Test
    n = 2
    arr = [3, 5]
    print("Output:", sol.countValid(n, arr))  # Should print 34

print("Execution Time:", timeit.timeit(main, number=1), "sec")
```

---

### ⏱ Time & Space Complexity

* **Time Complexity**:

  * O(1) — since `n ≤ 9`, fixed iterations

* **Space Complexity**:

  * O(1) — constant extra space (set, few lists)

---

## ✅ 4. Interview Q\&A

### Q1: Why do you subtract invalids from total?

**A**: Because it’s easier to count how many numbers do *not* contain the digits, and subtract to get the desired result using the complement principle.

---

### Q2: Why not generate all n-digit numbers and check?

**A**: That would be O(10⁹) for n=9. Too slow. Instead, we use combinatorics to count efficiently.

---

### Q3: Why exclude 0 from the first digit?

**A**: A valid n-digit number must not start with 0 — e.g., `012` is not valid 3-digit number.

---

### Q4: Can this be solved with bitmask + digit DP?

**A**: Yes, but it's unnecessary for n ≤ 9. Combinatorics is faster and simpler.

---

---

### ✅ Full Program: Count Numbers Containing Specific Digits

This solution counts how many **n-digit** numbers contain **at least one digit** from a given digit array.

---

### ✅ Python Code with Step-by-Step Comments

```python
import timeit

class Solution:
    def countValid(self, n, arr):
        # Step 1: Use a set for O(1) lookup time
        arr_set = set(arr)  # Time: O(m), Space: O(m) where m ≤ 10
        total_digits = set(range(10))  # Digits 0 to 9

        # Step 2: Total n-digit numbers (excluding numbers starting with 0)
        total = 9 * (10 ** (n - 1))  # Time: O(1), Space: O(1)

        # Step 3: Find digits that are *not* in arr
        digits_not_in_arr = list(total_digits - arr_set)  # Time: O(1), Space: O(1)

        # Edge case: If arr contains all digits, then all numbers are valid
        if not digits_not_in_arr:
            return total

        # Step 4: Digits that can be used as leading digits (≠ 0)
        leading_digits = [d for d in digits_not_in_arr if d != 0]

        # Edge case: No valid numbers if no valid leading digits
        if not leading_digits:
            return total

        # Step 5: Count how many invalid numbers don't use any digit from arr
        invalid = len(leading_digits) * (len(digits_not_in_arr) ** (n - 1))  # Time: O(1), Space: O(1)

        # Step 6: Valid numbers = total - invalid
        return total - invalid

# Test & Benchmark with `timeit`
def main():
    sol = Solution()
    test_cases = [
        (1, [1, 2, 3]),     # Expected: 3
        (2, [3, 5]),        # Expected: 34
        (3, [2, 4]),        # Custom case
        (2, list(range(10))),  # All digits present => 90
        (2, [0]),           # Only 0 => very limited options
    ]
    
    for n, arr in test_cases:
        result = sol.countValid(n, arr)
        print(f"Input: n={n}, arr={arr} => Output: {result}")

# Time the execution
execution_time = timeit.timeit(main, number=1)
print(f"\nExecution Time: {execution_time:.6f} sec")
```

---

### ⏱ Complexity Analysis

| Step | Operation                      | Time Complexity | Space Complexity |
| ---- | ------------------------------ | --------------- | ---------------- |
| 1    | Convert array to set           | O(m)            | O(m)             |
| 2    | Total valid n-digit numbers    | O(1)            | O(1)             |
| 3    | Difference with digit universe | O(1)            | O(1)             |
| 4    | Filter non-zero leading digits | O(1)            | O(1)             |
| 5    | Calculate invalids             | O(1)            | O(1)             |

👉 Overall Time: **O(1)**, Space: **O(1)**

---

### 🔍 Sample Output

```
Input: n=1, arr=[1, 2, 3] => Output: 3
Input: n=2, arr=[3, 5] => Output: 34
Input: n=3, arr=[2, 4] => Output: 452
Input: n=2, arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] => Output: 90
Input: n=2, arr=[0] => Output: 9

Execution Time: 0.000434 sec
```

---

### 🧠 Interview Q\&A

**Q1. Why can't we brute force all numbers from 10^(n-1) to 10^n?**
A1. Time complexity would be O(10^n), which is infeasible for n=9.

**Q2. Why do we exclude 0 as a leading digit?**
A2. Numbers like '034' aren't valid n-digit numbers.

**Q3. How do we efficiently count numbers that don’t contain digits from arr?**
A3. We use complementary counting (total - invalids) and digit position permutations.

---

---

# 🌍 Real-World Use Cases

Here are **a few important real-world use cases** for the problem **“Count Numbers Containing Specific Digits”**, which deals with counting n-digit numbers that include at least one digit from a specified set:

---

### 🔒 1. **Secure PIN Generation**

* **Scenario**: A bank needs to generate 6-digit PINs that must include at least one digit from a set of secure digits (e.g., \[1, 3, 7]).
* **Why it matters**: Ensures PINs meet regulatory or internal rules for unpredictability and inclusion of specific entropy-providing digits.
* **Usage**: Count how many such secure PINs can be generated.

---

### 📞 2. **Phone Number Filtering / Spam Protection**

* **Scenario**: A telecom operator wants to count or generate phone numbers that must include at least one digit from a set (e.g., emergency codes like \[1, 9]).
* **Why it matters**: For blocking or allowing specific patterns (e.g., deny numbers that don’t contain critical digits).
* **Usage**: Count how many such numbers exist for planning or filtering purposes.

---

### 🎰 3. **Lottery Ticket Validation**

* **Scenario**: A lottery system wants to ensure each ticket number includes at least one digit from a set of "lucky" numbers.
* **Why it matters**: Ensures compliance with game rules, or for analytics around distribution of numbers.
* **Usage**: Count and generate only valid ticket numbers.

---

### 🚫 4. **Fraud Detection & Pattern Analysis**

* **Scenario**: Analysts examine n-digit financial transaction IDs, where fraudulent patterns include specific digits (like 0 or 9).
* **Why it matters**: Helps estimate how many such potentially risky IDs could exist based on digit constraints.
* **Usage**: Count possible IDs that should be flagged if containing suspect digits.

---

### 🔢 5. **Custom Serial Number Generation**

* **Scenario**: A product line generates serial numbers of length `n`, but marketing requires each number to have at least one from \[4, 7, 9] (premium codes).
* **Why it matters**: Ensures serials carry branding or classification indicators.
* **Usage**: Used in manufacturing, asset tracking, and digital licensing.

---

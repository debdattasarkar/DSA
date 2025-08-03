
---

# Replace all 0's with 5

**Difficulty:** Basic
**Accuracy:** 57.99%
**Submissions:** 46K+
**Points:** 1

---

## Problem Statement

Given a number **N**, the task is to complete the function `convertFive()` which replaces **all zeros** in the number with **5** and returns the modified number.

---

## Example:

### Input

```
2
1004
121
```

### Output

```
1554
121
```

### Explanation

* **Testcase 1:** At index 1 and 2 there is 0 so we replace it with 5 → `1554`.
* **Testcase 2:** There is no `0`, so output will remain the same → `121`.

---

## Input

* The first line of input contains an integer **T**, denoting the number of test cases.
* Then **T** test cases follow.
* Each test case contains a single integer **N** denoting the number.

---

## Output

* The function should return an integer where all `0`'s are converted to `5`.

---

## Your Task

Since this is a **functional problem**, you don’t have to worry about input/output.
You just have to **complete the function `convertFive()`**.

---

## Constraints

```
1 ≤ T ≤ 10³  
1 ≤ N ≤ 10⁴
```

---

## Expected Complexities

* **Time Complexity:** O(k), where k is the number of digits in N.
* **Auxiliary Space:** O(1)

---

## Company Tags

* `Amazon`

---

## Topic Tags

* `Number Theory`, `Mathematical`, `Algorithms`

---

## Related Articles

* [`Replace 0 5 Input Integer`](https://www.geeksforgeeks.org/replace-0-5-input-integer/)

---

Certainly! Let's go through your request in detail for the problem: **Replace all 0's with 5**

---

### ✅ 2. Text Explanation with Step-by-Step Dry Run

**Problem:**
Given an integer `n`, replace **every digit that is 0** with **5**, and return the new number.

---

#### 💡 Dry Run:

**Input:**
`n = 1004`

**Process:**

We process the digits from right to left using modulo and division:

1. `digit = 4`, not 0 → keep 4
2. `digit = 0`, replace with 5 → use 5
3. `digit = 0`, replace with 5 → use 5
4. `digit = 1`, not 0 → keep 1

Reversed construction (least significant to most):
`4 → 5 → 5 → 1`
Reconstructed in correct order: `1554`

**Output:**
`1554`

---

**Another Example:**

**Input:** `n = 121`
All digits ≠ 0 → output is unchanged.
**Output:** `121`

---

### ✅ 3. Optimized Codes

All versions use digit-by-digit processing without converting to string—more **efficient and interview-preferred**.

---

#### 🔹 Python Version

```python
# Function should return an integer
class Solution:
    def convertFive(self, n):
        if n == 0:
            return 5
        
        result = 0
        place = 1

        # Process digits right to left
        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5  # Replace 0 with 5
            result += digit * place  # Build result number
            place *= 10
            n //= 10  # Remove last digit

        return result
```

---

#### 🔹 C++ Version

```cpp
class Solution {
  public:
    int convertFive(int n) {
        if (n == 0) return 5;
        int result = 0, place = 1;

        while (n > 0) {
            int digit = n % 10;
            if (digit == 0) digit = 5; // Replace 0 with 5
            result += digit * place;
            place *= 10;
            n /= 10;
        }
        return result;
    }
};
```

---

#### 🔹 JavaScript Version

```javascript
class Solution {
    convertFive(n) {
        if (n === 0) return 5;

        let result = 0;
        let place = 1;

        while (n > 0) {
            let digit = n % 10;
            if (digit === 0) digit = 5; // Replace 0 with 5
            result += digit * place;
            place *= 10;
            n = Math.floor(n / 10);
        }

        return result;
    }
}
```

---

### ✅ 4. Interview-Oriented Questions & Answers

---

**Q1: Why is string conversion not optimal in this problem?**
**A:**
String conversion adds overhead in both time and space. Arithmetic-based digit extraction (using `%` and `/`) is more efficient, especially for large inputs. It also avoids character encoding overhead.

---

**Q2: What’s the time and space complexity?**
**A:**

* **Time:** O(k), where k = number of digits in `n` (max 5 for constraints).
* **Space:** O(1), constant extra space.

---

**Q3: How would you handle input `n = 0`?**
**A:**
Special case: `0` itself should be returned as `5`.

---

**Q4: Can you do this in-place for a string input?**
**A:**
Yes, but it would require converting back to an integer, which incurs O(k) space. Integer math is preferred.

---

**Q5: What edge cases should be tested?**

* `n = 0` → `5`
* `n` contains multiple zeros → `1004` → `1554`
* `n` has no zeros → remains unchanged

---

Let me know if you'd like this turned into a live coding format or added to a larger README collection.

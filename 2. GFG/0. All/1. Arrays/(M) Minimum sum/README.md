
---

# 🔢 Minimum Sum

**Difficulty:** Medium
**Accuracy:** 17.14%
**Submissions:** 160K+
**Points:** 4

---

### 📘 Problem Statement

Given an array `arr[]` consisting of **digits**, your task is to form **two numbers** using **all the digits** such that their **sum is minimized**.
Return the **minimum possible sum** as a **string with no leading zeroes**.

---

### 🔍 Examples

#### ✅ Example 1:

```
Input: arr[] = [6, 8, 4, 5, 2, 3]
Output: "604"
Explanation: The minimum sum is formed by numbers 358 and 246.
```

#### ✅ Example 2:

```
Input: arr[] = [5, 3, 0, 7, 4]
Output: "82"
Explanation: The minimum sum is formed by numbers 35 and 047.
```

#### ✅ Example 3:

```
Input: arr[] = [9, 4]
Output: "13"
Explanation: The minimum sum is formed by numbers 9 and 4.
```

---

### 📌 Constraints:

* $2 \leq \text{arr.size()} \leq 10^6$
* $0 \leq \text{arr[i]} \leq 9$

---

### 📈 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

### 🏷️ Company Tags

* Google

---

### 🏷️ Topic Tags

* Arrays
* Sorting
* Binary Search
* Data Structures
* Algorithms

---

### 📚 Related Articles

* [Minimum Sum Two Numbers Formed Digits Array](https://www.geeksforgeeks.org/minimum-sum-of-two-numbers-formed-from-digits-of-an-array/)

---

## ✅ Problem Summary

> Given an array `arr[]` of digits (0–9), form **two numbers** using **all digits** such that their **sum is minimized**. Return the sum as a **string** (no leading zeroes allowed unless the result is `0`).

---

## 💡 Approach

### Greedy Strategy

* **Sort** the digits.
* **Distribute** them alternately to two numbers.
* Return their **sum as a string**.

---

## 🔄 Step-by-Step Dry Run

### Example:

**Input:** `arr = [6, 8, 4, 5, 2, 3]`
**Sorted:** `[2, 3, 4, 5, 6, 8]`

Distribute:

* `num1` = "2", "4", "6" → 246
* `num2` = "3", "5", "8" → 358

**Sum:** 246 + 358 = **604** → `"604"` ✅

---

## ✅ Final Python Code (Fixed)

```python
import sys
sys.set_int_max_str_digits(int(1e9))
class Solution:
    def minSum(self, arr):
        # code here
        # Step 1: Sort the digits to build smallest numbers
        arr.sort()
        num1, num2 = "", ""
        
        # Step 2: Distribute digits alternately
        for i, digit in enumerate(arr):
            if i % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)
                
        if num2=="":
                return num1
            
        # Step 3: Convert strings to integers and return the sum as string
        return str(int(num1) + int(num2))
```

---

Certainly! Let's break this code down step-by-step.

```python
class Solution:
    # Function to add two strings and return the result
    def addString(self,s1, s2):
        
        i = len(s1) - 1
        j = len(s2) - 1
    
        # initial carry is zero
        carry = 0
    
        # we will calculate and store the
        # resultant sum in reverse order in res
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(s1[i])
            if j >= 0:
                total += int(s2[j])
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
    
        # remove leading zeroes which are currently
        # at the back due to reversed string res
        while res and res[-1] == '0':
            res.pop()
    
        # reverse our final string
        return ''.join(reversed(res)) if res else "0"

    def minSum(self, arr):
        # code here
        # Count array to store frequency of each digit
        count = [0] * 10
    
        # Count occurrences of each digit
        for num in arr:
            count[num] += 1
    
        # Two strings for storing the two minimum numbers
        s1 = []
        s2 = []
    
        # Flag to alternate between s1 and s2
        firstNum = True
    
        # Traverse count array from 0 to 9
        for digit in range(10):
            while count[digit] > 0:
                if firstNum:
                    if not (len(s1) == 0 and digit == 0):
                        s1.append(str(digit))
                    firstNum = False
                else:
                    if not (len(s2) == 0 and digit == 0):
                        s2.append(str(digit))
                    firstNum = True
                count[digit] -= 1
    
        # Handle case where s1 or s2 might be empty
        if not s1:
            s1.append("0")
        if not s2:
            s2.append("0")
    
        return self.addString(''.join(s1), ''.join(s2))

```
---

## ✅ Goal of the Code

The goal of the `minSum` function is to **form two numbers using all digits from `arr`** such that their **sum is minimized**, and return the **sum as a string** (no leading zeroes allowed).

---

## 🔍 Function: `addString(s1, s2)`

This helper function **adds two numbers represented as strings**, digit-by-digit (like manual addition).

### 🔁 Logic:

```python
i = len(s1) - 1
j = len(s2) - 1
```

* Start from the end of both strings (least significant digit).
* Use `carry` for overflow (e.g., 8+7 = 15 → carry = 1, digit = 5).

### 💡 Example:

If `s1 = "456"`, `s2 = "78"`:

```
  4  5  6
+    7  8
---------
     534
```

This is implemented using a loop:

```python
while i >= 0 or j >= 0 or carry > 0:
```

It continues until both strings are processed and no carry remains.

### 🧼 Leading Zeros Handling:

```python
while res and res[-1] == '0':
    res.pop()
```

Because we build the result **backwards**, this removes trailing zeros (which are actually leading zeros after reverse).

### 🔁 Final Output:

```python
return ''.join(reversed(res)) if res else "0"
```

---

## 🔁 Function: `minSum(arr)`

### 🔢 Step 1: Count digit frequency

```python
count = [0] * 10
for num in arr:
    count[num] += 1
```

* Example: if `arr = [8, 6, 4, 5, 2, 3]`, then count becomes:
  `[0,0,1,1,1,1,1,0,1,0]`

### 🧮 Step 2: Build two strings

```python
s1 = []
s2 = []
firstNum = True
```

We alternate between the two numbers using `firstNum`.

```python
for digit in range(10):
    while count[digit] > 0:
        if firstNum:
            if not (len(s1) == 0 and digit == 0):
                s1.append(str(digit))
            firstNum = False
        else:
            if not (len(s2) == 0 and digit == 0):
                s2.append(str(digit))
            firstNum = True
        count[digit] -= 1
```

### 🚫 Why check for leading zero?

```python
if not (len(s1) == 0 and digit == 0)
```

We **skip leading zeros** to avoid numbers like `035`.

### ✨ Example:

For `arr = [6, 8, 4, 5, 2, 3]`, sorted is `[2, 3, 4, 5, 6, 8]`, alternately assigned:

* `s1 = [2, 4, 6]` → 246
* `s2 = [3, 5, 8]` → 358

Sum = 246 + 358 = **604**

---

## ✅ Final Step:

```python
return self.addString(''.join(s1), ''.join(s2))
```

* Combines `s1` and `s2` as strings
* Adds them using custom `addString()` (safe for large digits, avoids overflow)

---

## 💡 Why This Works

* By sorting and distributing digits alternately, both numbers stay as **close in size** as possible.
* This is a **greedy approach**: putting smaller digits in higher places.

---

## 📌 Edge Case Handling:

* Skips leading zeros in both numbers.
* If a number is empty (all zeros), it’s assigned `"0"`.

---

Would you like this same explanation in **flowchart** or **code comments format** too?

---

## 🧠 Interview Questions (with Mock Answers)

### 1. **Why does sorting help minimize the sum?**

**A:** Sorting lets us assign smaller digits to more significant positions, ensuring both numbers remain small, minimizing the overall sum.

---

### 2. **Why alternate digits instead of dividing evenly?**

**A:** Alternating ensures both numbers grow in parallel and remain balanced in length, which reduces the larger number and keeps the sum small.

---

### 3. **What if the array has only 1 digit?**

**A:** We return that digit as a string. One number gets it, the other remains zero.

---

### 4. **What’s the time and space complexity?**

**A:**

* Time: `O(n log n)` (for sorting)
* Space: `O(n)` (for strings being built)

---

Here's the full solution for the **"Minimum Sum"** problem with:

* 🔍 Text explanation
* 🧮 Step-by-step dry run
* ✅ Optimized code in **Python, C++, and JavaScript** with inline comments
* 🎯 Expected **interview questions** and their **mock answers**

---

## 🔍 Problem Understanding

You are given an array of digits. You must rearrange them to form **two numbers** such that their **sum is minimized**, and **use all digits**. Return the **sum** as a **string**, with **no leading zeroes**.

---

## 👣 Step-by-Step Approach

1. **Sort the digits** in ascending order. This ensures that we build the smallest possible numbers.
2. **Distribute digits alternately** between two numbers `num1` and `num2`.

   * Add the first digit to `num1`, the second to `num2`, third to `num1`, and so on.
3. **Form the numbers** and compute their sum.
4. Return the **string representation** of the sum.

---

## 🧪 Dry Run

Input: `[6, 8, 4, 5, 2, 3]`

Sorted: `[2, 3, 4, 5, 6, 8]`

Distribute alternately:

* `num1`: 2 → 4 → 6 → becomes "246"
* `num2`: 3 → 5 → 8 → becomes "358"

Sum = 246 + 358 = **604**

---

## ✅ JavaScript Code

```javascript
class Solution {
    minSum(arr) {
        arr.sort((a, b) => a - b);
        let num1 = "", num2 = "";
        
        for (let i = 0; i < arr.length; i++) {
            if (i % 2 === 0)
                num1 += arr[i];
            else
                num2 += arr[i];
        }

        let sum = BigInt(num1) + BigInt(num2);
        return sum.toString();
    }
}
```

---

## ❓ Interview Questions + Answers

### Q1: Why do you sort the array before distributing?

> Sorting ensures the smallest digits go into the lower place values, minimizing the final sum.

---

### Q2: Why do we alternate digits between two numbers?

> Alternating digits ensures both numbers grow gradually in value, preventing one from becoming disproportionately large.

---

### Q3: What is the time complexity of your approach?

> Sorting takes **O(n log n)** and building strings is **O(n)**. So, the total time complexity is **O(n log n)**.

---

### Q4: Can this logic handle leading zeros correctly?

> Yes. Since we use string construction and then convert using `int()` or `BigInt`, leading zeros don’t affect the final sum.

---

### Q5: Can this approach handle large digit counts (like 10⁶)?

> Yes, we avoid integer overflow by using `string`/`BigInt` and the logic is linear after sorting.

---

Here's a **hash map (frequency array)** based solution for the **"Minimum Sum"** problem — using all digits in the array to form two numbers whose **sum is minimized**, and return that sum as a string **without leading zeroes**.

---

## ✅ Idea (Using Hash Map)

We don’t need an actual `dict` — a **frequency array of size 10** (digits 0–9) works as a hash map here.

### ⚙️ Strategy:

1. Count frequency of each digit (hash map of digit → count).
2. Build two numbers `num1` and `num2` by picking the **smallest available digit** alternately (greedy).
3. Convert both to strings, add using custom `addString()` to avoid overflow.

---

## 🐍 Python Code (Hash Map Based)

```python
class Solution:
    # Function to add two large numbers represented as strings
    def addString(self, s1, s2):
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        res = []
        
        # Loop until all digits and carry are processed
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(s1[i])
                i -= 1
            if j >= 0:
                total += int(s2[j])
                j -= 1
            res.append(str(total % 10))
            carry = total // 10
        
        # Result is in reverse
        return ''.join(reversed(res))

    def minSum(self, arr):
        # Step 1: Frequency map of digits (0–9)
        freq = [0] * 10
        for digit in arr:
            freq[digit] += 1

        num1, num2 = "", ""

        # Step 2: Alternately build num1 and num2 from smallest digits
        flag = True  # Toggle to alternate between num1 and num2
        for digit in range(10):
            while freq[digit] > 0:
                if flag:
                    num1 += str(digit)
                else:
                    num2 += str(digit)
                flag = not flag
                freq[digit] -= 1

        # Step 3: Return the sum as a string
        return self.addString(num1, num2)
```

---

## 🔍 Dry Run

For input:

```python
arr = [6, 8, 4, 5, 2, 3]
```

Sorted digits: `2, 3, 4, 5, 6, 8`

Alternating assignment:

* `num1 = 2, 4, 6` → 246
* `num2 = 3, 5, 8` → 358

Sum = 604 → returned as **"604"**

---

## ✅ Time & Space Complexity

| Metric           | Complexity                                 |
| ---------------- | ------------------------------------------ |
| Time Complexity  | **O(n)** (count + assign)                  |
| Space Complexity | **O(1)** (since digit space is fixed: 0–9) |

---

## ✅ Interview-Focused Questions

| Question                                                | Answer                                                        |
| ------------------------------------------------------- | ------------------------------------------------------------- |
| What is the greedy decision?                            | Distribute smaller digits early to minimize high place values |
| Why use frequency array?                                | Digits are 0–9, constant space                                |
| Why use `addString()` instead of `int(num1)+int(num2)`? | To avoid integer overflow (for large inputs)                  |
| Could this fail with all zeros?                         | Yes, but `addString` ensures "0" is returned cleanly          |

---


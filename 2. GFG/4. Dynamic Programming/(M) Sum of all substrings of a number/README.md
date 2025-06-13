# Sum of All Substrings of a Number

## 🧩 Problem Statement

Given an integer `s` represented as a string, the task is to get the **sum of all possible substrings** of this string.

> **Note:**
>
> * The number may have leading zeros.
> * It is guaranteed that the total sum will fit within a 32-bit signed integer.

---

## 🧪 Examples

### Example 1:

**Input:**
`s = "6759"`

**Output:**
`8421`

**Explanation:**
Substrings:
6, 7, 5, 9, 67, 75, 59, 675, 759, 6759
Sum = 6 + 7 + 5 + 9 + 67 + 75 + 59 + 675 + 759 + 6759 = **8421**

---

### Example 2:

**Input:**
`s = "421"`

**Output:**
`491`

**Explanation:**
Substrings:
4, 2, 1, 42, 21, 421
Sum = 4 + 2 + 1 + 42 + 21 + 421 = **491**

---

## 📊 Constraints

* $1 \leq |s| \leq 9$

---

## 🧠 Expected Time and Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🧮 Approach

Let the input number be represented as a string: `s = "1234"`.

We want the sum of all substrings:
1, 2, 3, 4, 12, 23, 34, 123, 234, 1234 = Total

Let `res` be the final result, and `f(i)` be the sum of all substrings ending at index `i`.

The idea is:

```
f(i) = (f(i-1) * 10) + (s[i] * (i + 1))
```

We iterate through the string and update our result using this recurrence relation.

---

## 🚀 Code Implementation

### ✅ Python

```python
class Solution:
    def sumSubstrings(self, s):
        n = len(s)
        total = int(s[0])
        prev = total

        for i in range(1, n):
            num = int(s[i])
            curr = prev * 10 + num * (i + 1)
            total += curr
            prev = curr
        
        return total
```

---

### ✅ C++

```cpp
class Solution {
  public:
    long long sumSubstrings(string s) {
        int n = s.length();
        long long total = s[0] - '0';
        long long prev = total;

        for (int i = 1; i < n; i++) {
            int num = s[i] - '0';
            long long curr = prev * 10 + num * (i + 1);
            total += curr;
            prev = curr;
        }
        
        return total;
    }
};
```

---

### ✅ JavaScript

```javascript
class Solution {
    sumSubstrings(s) {
        const n = s.length;
        let total = parseInt(s[0], 10);
        let prev = total;

        for (let i = 1; i < n; i++) {
            const num = parseInt(s[i], 10);
            const curr = prev * 10 + num * (i + 1);
            total += curr;
            prev = curr;
        }

        return total;
    }
}
```

---

## 🏷️ Tags

`Strings`, `Dynamic Programming`, `Data Structures`, `Algorithms`

---

## 📚 Related Articles

* [Sum of All Substrings of a String Representing a Number](https://www.geeksforgeeks.org/sum-of-all-substrings-of-a-number/)
* [Sum Substrings String Representing Number Set 2 Constant Extra Space](https://www.geeksforgeeks.org/sum-substrings-string-representing-number-set-2-constant-extra-space/)

---

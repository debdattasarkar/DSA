# Next Greater Even Number

## 🧩 Problem Statement

Given a positive integer `x`, the task is to find the smallest **even number** `e` such that:

* `e > x`
* All digits in `x` and `e` are the same (permutation).

If no such number exists, return `-1`.

---

## 🧪 Example

### Example 1:

```
Input: x = 34722641  
Output: 34724126  
Explanation: Next greater number using the same digits that is also even is 34724126.
```

### Example 2:

```
Input: x = 111  
Output: -1  
Explanation: No rearrangement results in a number greater than 111.
```

---

## 🧠 Constraints

* 1 ≤ x.size() ≤ 10
* The number is a **positive integer**

---

## ⏱ Expected Time & Space Complexity

* **Time Complexity**: O(log n)
* **Auxiliary Space**: O(1)

---

## 🏷 Tags

* Arrays
* Strings
* Sorting
* Data Structures
* Algorithms

---

## 🏢 Company Tags

* Zoho
* Amazon
* FactSet
* MakeMyTrip
* Yahoo

---

## 📚 Related Articles

* [Given a Number, Find the Next Smallest Palindrome Larger Than This Number](https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/)

---

Here’s the **text explanation with a step-by-step dry run** followed by **Python, C++, and JavaScript implementations with inline comments** for the **Next Greater Even Number** problem:

---

## 📘 Text Explanation

### Goal:

Given a number `x`, find the **smallest even number** greater than `x` by rearranging its digits.

### Key Observations:

1. We need the next permutation of the digits of `x` that forms a number greater than `x`.
2. Among all such permutations, we pick the **smallest one that is also even** (i.e., ends with 0, 2, 4, 6, or 8).

### Algorithm:

1. Convert the number into a list of digits.
2. Use the **next permutation** logic:

   * Find the first digit from the right that is **smaller than** its next digit.
   * Find the next **just larger** digit to the right of it.
   * Swap them and reverse the suffix.
3. Repeat until we find a permutation that is:

   * Greater than original.
   * Ends in an even digit.
4. If no such permutation exists, return `-1`.

---

## 🔍 Dry Run

**Input**: `"34722641"`

* Next permutations:

  * `"34724126"` → ends in 6 → ✅ valid
  * Is this > `"34722641"`? → Yes.
* Output: **34724126**

**Input**: `"111"`

* Only permutation is `"111"` → No change.
* Output: **-1**

---

## ✅ Python Code

```python
class Solution:
    def getNextEven(self, x: str) -> int:
        from itertools import permutations
        
        digits = list(x)
        n = len(digits)
        
        def next_permutation(arr):
            i = n - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True

        arr = list(digits)
        orig = int(x)

        while next_permutation(arr):
            num = int("".join(arr))
            if num > orig and int(arr[-1]) % 2 == 0:
                return num
        return -1
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    long long getNextEven(string x) {
        string s = x;
        long long orig = stoll(x);

        while (next_permutation(s.begin(), s.end())) {
            long long num = stoll(s);
            if (num > orig && (s.back() - '0') % 2 == 0) {
                return num;
            }
        }
        return -1;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    getNextEven(x) {
        let arr = x.split('');
        const original = parseInt(x);

        function nextPermutation(arr) {
            let i = arr.length - 2;
            while (i >= 0 && arr[i] >= arr[i + 1]) i--;
            if (i === -1) return false;

            let j = arr.length - 1;
            while (arr[j] <= arr[i]) j--;

            [arr[i], arr[j]] = [arr[j], arr[i]];
            let left = i + 1, right = arr.length - 1;
            while (left < right) {
                [arr[left], arr[right]] = [arr[right], arr[left]];
                left++; right--;
            }
            return true;
        }

        while (nextPermutation(arr)) {
            let num = parseInt(arr.join(''));
            if (num > original && parseInt(arr[arr.length - 1]) % 2 === 0) {
                return num;
            }
        }

        return -1;
    }
}
```

---

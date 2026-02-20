Here is the complete **README conversion** of the problem exactly as shown in the image, without omitting any part.

---

# 📌 Form the Largest Number

**Difficulty:** Medium
**Accuracy:** 37.82%
**Submissions:** 196K+
**Points:** 4

---

## 📝 Problem Statement

Given an array of integers `arr[]` representing **non-negative integers**, arrange them so that after **concatenating all of them in order**, it results in the **largest possible number**.

Since the result may be very large, return it as a **string**.

---

## 📚 Examples

### Example 1

```
Input:  arr[] = [3, 30, 34, 5, 9]
Output: 9534330
```

**Explanation:**
Given numbers are `[3, 30, 34, 5, 9]`, the arrangement `[9, 5, 34, 3, 30]` gives the largest value.

---

### Example 2

```
Input:  arr[] = [54, 546, 548, 60]
Output: 6054854654
```

**Explanation:**
Given numbers are `[54, 546, 548, 60]`, the arrangement `[60, 548, 546, 54]` gives the largest value.

---

### Example 3

```
Input:  arr[] = [3, 4, 6, 5, 9]
Output: 96543
```

**Explanation:**
Given numbers are `[3, 4, 6, 5, 9]`, the arrangement `[9, 6, 5, 4, 3]` gives the largest value.

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^5`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## 🏢 Company Tags

* Paytm
* Zoho
* Amazon
* Microsoft
* MakeMyTrip

---

## 🏷 Topic Tags

* Arrays
* Data Structures
* Sorting

---

## 💼 Related Interview Experiences

* Amazon Interview Experience Set 242 1 Year Experience
* One97paytm Interview Experience
* Paytm Interview Experience Set 13 Experienced
* Makemytrip Interview Experience Set 11 Developer Position

---

## 📖 Related Articles

* Given An Array Of Numbers Arrange The Numbers To Form The Biggest Number

---

---

## 2) Explanation (Key Idea)

To form the **largest concatenated number**, we can’t just sort numerically or by length.

### Core rule

For any two numbers `a` and `b` (as strings):

* Put `a` before `b` if `a+b > b+a`

Because whichever concatenation is bigger should appear earlier in the final string.

Example:

* `a="9"`, `b="34"`
* `a+b="934"`, `b+a="349"` → `934 > 349` ⇒ `"9"` should come before `"34"`

So we:

1. Convert numbers to strings
2. Sort using the comparator above
3. Join them
4. Handle the all-zero case (e.g., `[0,0]` → `"0"` not `"00"`)

---

## Step-by-step Dry Run (Example 1)

`arr = [3, 30, 34, 5, 9]`
Convert to strings: `["3","30","34","5","9"]`

Now compare & order using `(a+b) vs (b+a)`:

* Compare `"3"` vs `"30"`:

  * `"330"` vs `"303"` → `"330"` bigger ⇒ `"3"` before `"30"`
* Compare `"34"` vs `"3"`:

  * `"343"` vs `"334"` → `"343"` bigger ⇒ `"34"` before `"3"`
* Compare `"9"` vs `"34"`:

  * `"934"` vs `"349"` → `"934"` bigger ⇒ `"9"` before `"34"`
* Compare `"5"` vs `"34"`:

  * `"534"` vs `"345"` → `"534"` bigger ⇒ `"5"` before `"34"`

Final sorted order: `["9","5","34","3","30"]`
Join → `"9534330"`

---

## 3) Python Solutions (Brute + Interview-Expected)

### A) Brute / Easy (Bubble-sort using custom rule)

Good to show the idea, but slower.

**Time:** `O(n^2 * k)` where `k` is avg digits
**Space:** `O(n)`

```python
class Solution:
    def findLargest(self, arr):
        # Brute: bubble sort using rule (a+b > b+a)
        # Time: O(n^2 * k), Space: O(n)

        numbers_as_strings = list(map(str, arr))
        n = len(numbers_as_strings)

        for i in range(n):
            for j in range(0, n - 1 - i):
                a = numbers_as_strings[j]
                b = numbers_as_strings[j + 1]

                # If b should come before a, swap them
                if b + a > a + b:
                    numbers_as_strings[j], numbers_as_strings[j + 1] = b, a

        result = "".join(numbers_as_strings)

        # Handle all zeros -> "0" instead of "000..."
        return "0" if result[0] == "0" else result
```

---

### B) Optimized (Most Expected): Sort with comparator ✅

Python needs `functools.cmp_to_key` to use a comparator.

**Time:** `O(n log n * k)`
**Space:** `O(n)`

```python
from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Interview-expected: custom comparator sort
        # Time: O(n log n * k), Space: O(n)

        numbers_as_strings = list(map(str, arr))

        def compare(a, b):
            # return -1 if a should come before b
            # return  1 if b should come before a
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        # Sort using the comparator
        numbers_as_strings.sort(key=cmp_to_key(compare))

        result = "".join(numbers_as_strings)

        # If the largest starts with '0', then all are zeros
        return "0" if result[0] == "0" else result
```

---

### C) Optimized Variant (Common trick when constraints allow)

Sometimes people use repeated string keys like `x*10` to align digits.
**But** this depends on max digit length; comparator is safer.

I’m including this only as a “variant you might mention”, not the best default.

```python
class Solution:
    def findLargest(self, arr):
        # Key trick variant (works reliably when max digits are bounded small)
        # Still, comparator is the most correct & expected.

        numbers_as_strings = list(map(str, arr))
        # Multiply strings to make comparable (10 is safe for <= 10^5 digits length <= 6)
        numbers_as_strings.sort(key=lambda x: x * 10, reverse=True)

        result = "".join(numbers_as_strings)
        return "0" if result[0] == "0" else result
```

---

## 4) Interview Recall + Expected Q&A

### 5-line pseudo-code (memorize)

```text
convert all numbers to strings
sort strings by rule: a before b if (a+b) > (b+a)
join sorted strings into answer
if answer starts with '0': return "0"
else return answer
```

### Mnemonic

**“AB vs BA”**

* Always compare **A+B** with **B+A**
* Bigger one decides who comes first

---

## Expected Interview Questions & Answers

**Q1. Why not sort descending numerically?**
A1. Because concatenation order matters: `9` and `34` → `934` > `349`. Numeric sort can fail on cases like `[3, 30]`.

**Q2. What comparator do you use and why?**
A2. For strings `a,b`, compare `a+b` vs `b+a`. If `a+b` bigger, `a` must come first to maximize final number.

**Q3. Is the comparator transitive / safe for sorting?**
A3. This comparator is standard for this problem and produces a valid ordering for maximizing concatenation (used in common solutions and accepted by platforms).

**Q4. How do you handle `[0,0,0]`?**
A4. After joining you get `"000"`. If first char is `'0'`, return `"0"`.

**Q5. Complexity?**
A5. Sorting dominates: `O(n log n)` comparisons, each comparison costs `O(k)` for concatenations, so `O(n log n * k)`.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Largest “combined” ID / key for sorting records**

* When you need a deterministic way to order numeric tokens so their concatenation forms the **maximum lexicographic/priority key** (e.g., generating a “top-ranked bundle id”).

2. **Marketing / UI display ordering**

* Showing “best-looking / highest-impact” number when combining offer codes or metrics into a single banner string (rule-based concatenation ordering).

3. **Log aggregation / report headline number**

* When several components contribute digits/parts and you want the final “headline number” to be as large as possible by ordering parts (toy but interview-relatable).

4. **Competitive bidding / token ordering (conceptual)**

* Given non-negative bid tokens, you want the largest possible combined token string for ranking—same ordering logic (`AB vs BA`).

(Interviewers mainly want: **this is a custom sort / comparator problem**.)

---

## 6) Full Program (timed end-to-end + sample input/output)

### ✅ Input Format (for this program)

```
t
n
a1 a2 a3 ... an
(repeat for t test cases)
```

### ✅ Sample Input

```
3
5
3 30 34 5 9
4
54 546 548 60
5
3 4 6 5 9
```

### ✅ Sample Output

```
9534330
6054854654
96543
Total runtime (seconds): 0.0000xxxx
```

---

```python
import time
from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        """
        Arrange numbers to form the largest possible concatenated number (as string).

        Key Rule:
          For two strings a, b:
            put a before b if (a+b) > (b+a)

        Time Complexity:
          - Convert to strings: O(n)
          - Sorting with comparator: O(n log n * k)
              where k = average digits per number (concat/compare cost)
          - Join: O(n * k)
          => Overall: O(n log n * k)

        Auxiliary Space:
          - String list: O(n)
          - Sort overhead: O(n) (implementation dependent)
          - Output string: O(n * k)
        """

        # Step 1: Convert integers to strings
        # Time: O(n), Space: O(n)
        numbers_as_strings = list(map(str, arr))

        # Step 2: Comparator based on AB vs BA
        # Each comparison costs O(k)
        def compare(a, b):
            # If a+b is larger, a should come earlier => return -1
            if a + b > b + a:
                return -1
            # If b+a is larger, b should come earlier => return 1
            if a + b < b + a:
                return 1
            return 0

        # Step 3: Sort using custom comparator
        # Time: O(n log n * k), Space: O(n) (sorting overhead)
        numbers_as_strings.sort(key=cmp_to_key(compare))

        # Step 4: Join into final string
        # Time: O(n*k), Space: O(n*k) for the output string
        result = "".join(numbers_as_strings)

        # Step 5: Handle case like [0,0] => "0" (not "00")
        # Time: O(1)
        return "0" if result[0] == "0" else result


def main():
    # Measure full program runtime (I/O + computation)
    program_start = time.perf_counter()  # Time: O(1)

    t = int(input().strip())  # Time: O(1)
    solver = Solution()

    # Process each test case
    # Total time: Σ O(n log n * k)
    for _ in range(t):
        n = int(input().strip())  # Time: O(1)

        # Read array values
        # Time: O(n), Space: O(n)
        arr = list(map(int, input().split()))

        # Compute largest concatenated number
        # Time: O(n log n * k)
        answer = solver.findLargest(arr)

        # Output answer
        print(answer)

    program_end = time.perf_counter()
    print(f"Total runtime (seconds): {program_end - program_start:.8f}")


if __name__ == "__main__":
    main()
```

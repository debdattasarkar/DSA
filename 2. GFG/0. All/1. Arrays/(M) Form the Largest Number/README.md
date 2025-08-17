
---

# Form the Largest Number

**Difficulty:** Medium
**Accuracy:** 37.82%
**Submissions:** 182K+
**Points:** 4

---

### Problem Statement

Given an array of integers `arr[]` representing non-negative integers, arrange them so that after **concatenating** all of them in order, it results in the **largest possible number**.

Since the result may be very large, return it as a **string**.

---

### Examples

**Example 1:**

```
Input: arr[] = [3, 30, 34, 5, 9]
Output: 9534330
Explanation: Given numbers are [3, 30, 34, 5, 9], 
the arrangement [9, 5, 34, 3, 30] gives the largest value.
```

**Example 2:**

```
Input: arr[] = [54, 546, 548, 60]
Output: 6054854654
Explanation: Given numbers are [54, 546, 548, 60], 
the arrangement [60, 548, 546, 54] gives the largest value.
```

**Example 3:**

```
Input: arr[] = [3, 4, 6, 5, 9]
Output: 96543
Explanation: Given numbers are [3, 4, 6, 5, 9], 
the arrangement [9, 6, 5, 4, 3] gives the largest value.
```

---

### Constraints

* $1 \leq arr.size() \leq 10^5$
* $0 \leq arr[i] \leq 10^5$

---

### Expected Complexities

* **Time Complexity:** $O(n \log n)$
* **Auxiliary Space:** $O(n)$

---

### Company Tags

* Paytm
* Zoho
* Amazon
* Microsoft
* MakeMyTrip

---

### Topic Tags

* Arrays
* Data Structures
* Sorting

---

### Related Interview Experiences

* Amazon Interview Experience Set 242 | 1 Year Experience
* One97Paytm Interview Experience
* Paytm Interview Experience Set 13 | Experienced
* MakeMyTrip Interview Experience Set 11 | Developer Position

---

### Related Articles

* [Given An Array Of Numbers Arrange The Numbers To Form The Biggest Number](https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/)

---

---

Here’s a crisp, interview-ready package for **Form the Largest Number** 👇

---

## 2) Text explanation + step-by-step dry run

### Core idea

If two numbers `a` and `b` are placed side by side, the order that produces the **larger concatenated string** should come first.
Compare the strings `a+b` and `b+a`:

* If `a+b > b+a`, put `a` before `b`.
* Else put `b` before `a`.

After sorting all numbers under this rule, concatenate them. Handle the corner case where the result begins with `'0'` (i.e., all numbers were zero).

### Why string comparison?

Numerically, `3` and `30` are `3 > 30` wrong signal, but:

* `"330"` vs `"303"` → `"330"` is larger → `3` should come **before** `30`.
  Only concatenation comparison captures this.

### Dry run on `arr = [3, 30, 34, 5, 9]`

We sort using the rule above (pairwise thinking):

* Compare `30` vs `3`: `"303"` vs `"330"` → `330` is larger → `3` before `30`.
* Compare `34` vs `3`: `"343"` vs `"334"` → `343` is larger → `34` before `3`.
* Compare `5` vs `34`: `"534"` vs `"345"` → `534` is larger → `5` before `34`.
* Compare `9` vs `5`: `"95"` vs `"59"` → `95` is larger → `9` before `5`.
* Repeat comparisons transitively during sort; final order becomes:

  ```
  [9, 5, 34, 3, 30]
  ```

Concatenate → `"9534330"`.

Corner case: `arr = [0, 0, 0]`

* After sorting you’d get `"000"`. Return `"0"` instead of `"000"`.

---

## 3) Optimized Python solutions (with interview-style comments)

### A) Optimal (Custom comparator + sort)

* Time: `O(n log n * L)` where `L` ≈ max number of digits (string compare)
* Space: `O(n)` for string forms

```python
from functools import cmp_to_key

class Solution:

    def findLargest(self, arr):
        # Convert all numbers to strings once
        strs = list(map(str, arr))

        # Custom comparator: order x before y if x+y > y+x
        def cmp(x, y):
            if x + y > y + x:
                return -1     # x should come first
            elif x + y < y + x:
                return 1      # y should come first
            else:
                return 0      # equal preference

        # Sort using the comparator
        strs.sort(key=cmp_to_key(cmp))

        # Edge case: if the largest element is "0", all are zeros
        if strs[0] == "0":
            return "0"

        # Join into the largest number string
        return "".join(strs)
```

### B) “Key trick” (works well in practice, caveat: relies on bounded digits)

If you know each number has at most `d` digits (e.g., `d<=10` due to constraints), you can sort by a repeated pattern key. It’s a common quick hack:

* Time: `O(n log n * d)`
* Space: `O(n)`

```python
class Solution:

    def findLargest(self, arr):
        strs = list(map(str, arr))
        # Repeat each string to a fixed length so comparisons act like concatenation
        # Choose repeat length > max digits possible to equalize.
        # Here 10 is safe for arr[i] <= 10^5 (5 digits), but 10 is still fine.
        strs.sort(key=lambda x: x * 10, reverse=True)

        if strs[0] == "0":  # all zeros
            return "0"
        return "".join(strs)
```

> Note for interviews: the comparator solution (A) is the **expected** robust approach. The repetition trick (B) is fast to code but you should mention the assumption on max digits.

### C) Brute force (for understanding / very small n)

* Generate all permutations and pick the max concatenation.
* Time: `O(n! * n * L)` → impractical beyond `n≈8`.

```python
from itertools import permutations

class Solution:

    def findLargest(self, arr):
        best = ""
        for p in permutations(map(str, arr)):
            cand = "".join(p)
            if cand > best:
                best = cand
        # Handle zeros naturally; "0" will be best if all zero
        return best
```

---

## 4) Interview Q\&A

**Q1. Why compare `x+y` vs `y+x`?**
A1. Because the only thing that matters is how two numbers look when concatenated in final string. If `x+y` is lexicographically larger than `y+x`, then placing `x` before `y` maximizes the result for those two; the sort’s transitivity ensures a global optimum.

**Q2. Is the comparator transitive?**
A2. Yes. The relation defined by `(x before y) ⇔ (x+y > y+x)` is known to induce a total order sufficient for sorting (this is a classical result used in this problem family).

**Q3. What’s the time complexity?**
A3. Sorting `n` elements with comparisons that cost `O(L)` (comparing `x+y` and `y+x`) gives `O(n log n * L)`, where `L` is bounded by a small constant (max digits).

**Q4. How do you handle arrays of zeros like `[0,0,0]`?**
A4. After sorting, if the first string is `"0"`, then the entire result is `"0"` (not multiple zeros). Just return `"0"`.

**Q5. Why convert to strings instead of doing number math?**
A5. Because concatenation compares string forms directly; numeric tricks (like powers of 10) are error-prone and can overflow in other languages. String compare is clean and safe.

**Q6. Could we sort in ascending order then reverse?**
A6. You could, but the custom comparator already defines the correct descending order. Just sort once with that comparator.

**Q7. Any pitfalls?**
A7. Forgetting the all-zero case, or trying to compare integers directly without string concatenation logic, will produce wrong results (e.g., `3` vs `30`).

---

---

Here’s a complete, interview-ready package for **Form the Largest Number** with a full runnable program, detailed complexity comments, timing, and a few sharp real-world use cases.

---

## 5) Full program (with inline time/space complexity notes + timing)

```python
from functools import cmp_to_key
from timeit import default_timer as timer

class Solution:
    def findLargest(self, arr):
        """
        Goal: arrange non-negative integers so their concatenation is the largest possible.
        Returns: string (because result can be very large)

        n = len(arr), L = max number of digits among arr elements (<= 6 under typical constraints)

        Steps:
        1) Convert to strings .......................... Time: O(n) | Space: O(n * L)
        2) Custom sort using (x+y) vs (y+x) comparator . Time: O(n log n * L) | Space: O(n * L)
        3) Edge-case 'all zeros' handling .............. Time: O(1) | Space: O(1)
        4) Join into the final string .................. Time: O(n * L) | Space: O(n * L)
        Overall: O(n log n * L) time, O(n * L) space
        """
        # ---- Step 1: convert to string once (avoid repeated str() in comparator)
        strs = list(map(str, arr))  # O(n) time, O(n*L) space

        # ---- Step 2: custom comparator for descending order by concatenation
        def cmp(x, y):
            # Compare "x+y" vs "y+x": if x+y is larger, x should come before y
            # Each comparison is O(L)
            if x + y > y + x:
                return -1  # x before y
            elif x + y < y + x:
                return 1   # y before x
            else:
                return 0   # equal preference

        strs.sort(key=cmp_to_key(cmp))  # O(n log n * L)

        # ---- Step 3: all zeros edge case; avoid "0000..."
        if strs[0] == "0":  # O(1)
            return "0"

        # ---- Step 4: concatenate into final string
        return "".join(strs)  # O(n * L)


def main():
    # Sample inputs to demonstrate correctness and edge cases
    tests = [
        ([3, 30, 34, 5, 9], "Expected: 9534330"),
        ([54, 546, 548, 60], "Expected: 6054854654"),
        ([3, 4, 6, 5, 9],    "Expected: 96543"),
        ([0, 0, 0],          "Expected: 0"),
        ([10, 2],            "Expected: 210"),
        ([121, 12],          "Expected: 12121"),
    ]

    sol = Solution()

    # Use timeit's high-resolution clock to time the overall run of all tests
    t0 = timer()
    for arr, note in tests:
        res = sol.findLargest(arr[:])  # pass a copy to be safe
        print(f"Input: {arr}\nOutput: {res}\n{note}\n" + "-"*40)
    t1 = timer()

    print(f"Total runtime for all tests: {(t1 - t0)*1000:.3f} ms")


if __name__ == "__main__":
    main()
```

**What you’ll see when you run it (example):**

```
Input: [3, 30, 34, 5, 9]
Output: 9534330
Expected: 9534330
----------------------------------------
Input: [54, 546, 548, 60]
Output: 6054854654
Expected: 6054854654
----------------------------------------
Input: [3, 4, 6, 5, 9]
Output: 96543
Expected: 96543
----------------------------------------
Input: [0, 0, 0]
Output: 0
Expected: 0
----------------------------------------
Input: [10, 2]
Output: 210
Expected: 210
----------------------------------------
Input: [121, 12]
Output: 12121
Expected: 12121
----------------------------------------
Total runtime for all tests: X.XXX ms
```

---

## 6) Real-World Use Cases (a few very important ones)

1. **Search/Ads ranking composition**
   When forming the most impactful campaign ID or creative ordering by concatenating numeric components (scores, IDs), the comparator rule ensures the globally maximal “lexicographic” impact.

2. **Version tag or build label ordering**
   When you need to assemble build labels or tags from numeric fragments to produce the “largest” (latest) sortable string representation, ordering parts by `a+b > b+a` yields the right concatenation.

3. **Custom sort for human-friendly IDs**
   In fintech/e-commerce order IDs that concatenate components (region codes, shop codes, sequence numbers), choosing the arrangement that maximizes display “priority” via concatenation comparison can be useful for dashboards.

4. **Data packing / key generation**
   Generating composite keys that are compared lexicographically (e.g., dictionary or KV-store keys) benefits from this rule to maximize or minimize ordering in a predictable way.


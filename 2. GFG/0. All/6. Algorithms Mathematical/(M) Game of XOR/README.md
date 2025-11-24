
---

# **Game of XOR**

**Difficulty:** Medium
**Accuracy:** 50.77%
**Submissions:** 40K+
**Points:** 4

---

## **Problem Statement**

You are given an integer array `arr[]`.
The **value of a subarray** is defined as the **bitwise XOR** of all elements in that subarray.

Your task is to compute the **bitwise XOR of the values of all possible subarrays** of `arr[]`.

---

## **Examples**

---

### **Example 1**

**Input:**

```
arr[] = [1, 2, 3]
```

**Output:**

```
2
```

**Explanation:**

```
xor[1] = 1
xor[1, 2] = 3
xor[2, 3] = 1
xor[1, 2, 3] = 0
xor[2] = 2
xor[3] = 1

Result : 1 ⊕ 3 ⊕ 1 ⊕ 0 ⊕ 2 ⊕ 1 = 2
```

---

### **Example 2**

**Input:**

```
arr[] = [1, 2]
```

**Output:**

```
0
```

**Explanation:**

```
xor[1] = 1
xor[1, 2] = 3
xor[2] = 2

Result : 1 ⊕ 3 ⊕ 2 = 0
```

---

## **Constraints**

* `1 ≤ arr.size() ≤ 10⁵`
* `0 ≤ arr[i] ≤ 10⁹`

---

## **Expected Complexities**

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## **Company Tags**

* Amazon

---

## **Topic Tags**

* Mathematical
* Bit Magic
* Data Structures
* Algorithms

---

## **Related Articles**

* [*Xor Subarray Xors*](https://www.geeksforgeeks.org/xor-subarray-xors/)

---

---

I’ll walk through:

1. Intuition + step-by-step dry run
2. Brute-force Python + optimized Python (your class format)
3. Interview memory trick + likely Q&A

---

## 2. Explanation + Step-by-Step Dry Run

### Problem in my own words

* You have an array `arr` of length `n`.
* For **every subarray** `arr[l..r]` (continuous segment), compute the XOR of its elements.
* Now XOR **all those subarray XORs together**.
* Return that final single number.

Example: `arr = [1, 2, 3]`

All subarrays:

1. `[1]` → `1`
2. `[1, 2]` → `1 ^ 2 = 3`
3. `[1, 2, 3]` → `1 ^ 2 ^ 3 = 0`
4. `[2]` → `2`
5. `[2, 3]` → `2 ^ 3 = 1`
6. `[3]` → `3`

Final result = `1 ^ 3 ^ 0 ^ 2 ^ 1 ^ 3 = 2`.

---

### Key XOR facts

1. `x ^ x = 0`
2. `x ^ 0 = x`
3. XOR is associative and commutative (order doesn’t matter).

So if the **same value** appears an **even** number of times in a big XOR, it cancels out; if an **odd** number of times, it survives once.

We’ll use that idea, but for **each element** of `arr`, not each subarray.

---

### How often does each element participate?

Pick an element `arr[i]` at index `i` (0-based) in an array of length `n`.

How many subarrays include `arr[i]`?

* Choices for the **left end**:

  * can be at index `0..i` → `i + 1` choices
* Choices for the **right end**:

  * can be at index `i..n-1` → `n - i` choices

Total subarrays containing `arr[i]`:

```text
count_i = (i + 1) * (n - i)
```

In each such subarray, `arr[i]` is part of that subarray’s XOR.

When we XOR all subarray XORs together, `arr[i]` appears exactly `count_i` times in the big XOR.

Because XOR cancels in pairs:

* If `count_i` is **even** → `arr[i]`’s total effect is `0`
* If `count_i` is **odd** → `arr[i]` contributes **once** to final answer

So final answer is:

```text
answer = XOR of arr[i] over all i where count_i is odd
```

That’s the O(n) trick.

---

### Dry run with `arr = [1, 2, 3]`

`n = 3`

Indices: `0, 1, 2`

#### i = 0, val = 1

* `count_0 = (0+1) * (3-0) = 1 * 3 = 3` → odd
* Contribution: include `1` in final XOR.

#### i = 1, val = 2

* `count_1 = (1+1) * (3-1) = 2 * 2 = 4` → even
* Contribution: cancels out completely → ignore.

#### i = 2, val = 3

* `count_2 = (2+1) * (3-2) = 3 * 1 = 3` → odd
* Contribution: include `3`.

Final answer:

```text
answer = 1 ^ 3 = 2
```

Same as brute force, but done in O(n) without enumerating subarrays.

---

### Dry run with `arr = [1, 2]`

`n = 2`

#### i = 0 → val = 1

`count_0 = (0+1) * (2-0) = 1 * 2 = 2` → even → no net contribution.

#### i = 1 → val = 2

`count_1 = (1+1) * (2-1) = 2 * 1 = 2` → even → no net contribution.

Final answer = XOR of nothing = `0`.
Matches the sample.

---

## 3. Python Codes (Brute + Optimized)

### 3.1 Brute-force (for understanding / not for large n)

We can compute every subarray’s XOR explicitly.

* Outer loop: choose `start`
* Inner loop: extend `end` and keep running XOR
* Combine them all.

Time: `O(n^2)`
Space: `O(1)` extra.

```python
class SolutionBrute:
    def subarrayXor(self, arr):
        """
        Brute-force solution.
        Time  : O(n^2)   (all subarrays)
        Space : O(1) extra
        """
        n = len(arr)
        total_xor = 0

        # Pick starting index of subarray
        for start in range(n):
            current_xor = 0
            # Extend subarray to the right
            for end in range(start, n):
                current_xor ^= arr[end]     # XOR of arr[start..end]
                total_xor ^= current_xor    # include this subarray's XOR

        return total_xor
```

---

### 3.2 Optimized solution (O(n), the one interviewers expect)

Use the **count of subarrays containing each element** idea.

```python
class Solution:
    def subarrayXor(self, arr):
        """
        Optimized solution using frequency of each element in all subarrays.

        Idea:
        -----
        - Every subarray contributes its XOR.
        - Each element arr[i] appears in many subarrays; exactly:
              count_i = (i + 1) * (n - i)
        - XOR facts:
              x ^ x = 0, x ^ 0 = x
          => if an element appears even times, it cancels;
             if odd times, it contributes once.
        - So final answer is XOR of arr[i] for which count_i is odd.

        Time Complexity:
            O(n) — single pass over array.
        Space Complexity:
            O(1) — only a few variables.
        """
        n = len(arr)
        answer = 0

        for i, value in enumerate(arr):
            # Number of subarrays that include position i
            count = (i + 1) * (n - i)

            # If count is odd, this value contributes once
            if count % 2 == 1:
                answer ^= value

        return answer
```

This is the one you should give as your **final solution** in an interview.

If the platform uses `n` explicitly, you just pass `n = len(arr)` or add it as a parameter.

---

## 4. Interview: How to Remember & What They Might Ask

### 🔑 10-second mental summary

> “I don’t compute all subarrays.
> Each element arr[i] appears in (i+1)·(n−i) subarrays.
> If that count is odd, arr[i] is present an odd number of times in the final big XOR and survives once.
> So I just XOR all arr[i] whose (i+1)·(n−i) is odd.
> That’s O(n) time and O(1) space.”

---

### 💡 Easy mnemonic

**“Position product parity”**

* `position product` = `(i+1) * (n-i)`
* `parity` = odd or even
* Only when parity is **odd**, include `arr[i]`.

---

### Likely Interview Questions & Good Answers

---

**Q1. Can you explain the O(n) idea without writing code?**

> Each subarray XOR is composed of the elements that lie inside it.
> Instead of enumerating subarrays, I look at a single element arr[i] and ask: how many subarrays contain this index?
> That’s `(i+1) * (n-i)` because we can choose any start from 0..i and any end from i..n-1.
> This is the number of times arr[i] will appear across all subarray XORs.
> XOR cancels in pairs, so only if this number is odd does arr[i] contribute to the final answer.
> So I loop through the array once, compute this count, and XOR in arr[i] whenever the count is odd.

---

**Q2. Why is XOR appropriate here (what properties do you use)?**

> I rely on two properties:
>
> 1. `x ^ x = 0` — two equal values cancel out.
> 2. XOR is associative and commutative — I can rearrange and regroup terms without changing the result.
>    That allows me to count how many times each element appears in the big XOR and just check if that count is odd or even.

---

**Q3. What’s the time and space complexity of your optimized solution?**

> * Time: O(n). I traverse the array once, and each iteration does O(1) work.
> * Space: O(1). I only store the running XOR and a few integers; no extra arrays or maps.

---

**Q4. Could you outline the brute-force solution and why it’s too slow?**

> Brute force picks every subarray `arr[l..r]`, computes its XOR, and then XORs all of those together.
> There are O(n²) subarrays. With a running XOR we can compute each in O(1), so total time O(n²).
> For n up to 10⁵, that’s up to 10¹⁰ operations and will time out.
> That’s why we need the counting trick to reduce it to O(n).

---

**Q5. Is there any special behavior when n is even vs odd?**

> Yes, often for bitwise problems, parity of positions matters.
> Here, you can notice:
>
> * If n is even, for most indices `(i+1)*(n-i)` is even, and sometimes the final XOR becomes 0 for certain structured arrays.
>   But I don’t rely on a closed-form per n; I just compute `(i+1)*(n-i) % 2` directly.
>   The formula works uniformly for all n.

---

---

I’ll walk through:

1. Intuition + step-by-step dry run
2. Brute-force Python + optimized Python (your class format)
3. Interview memory trick + likely Q&A

---

## 2. Explanation + Step-by-Step Dry Run

### Problem in my own words

* You have an array `arr` of length `n`.
* For **every subarray** `arr[l..r]` (continuous segment), compute the XOR of its elements.
* Now XOR **all those subarray XORs together**.
* Return that final single number.

Example: `arr = [1, 2, 3]`

All subarrays:

1. `[1]` → `1`
2. `[1, 2]` → `1 ^ 2 = 3`
3. `[1, 2, 3]` → `1 ^ 2 ^ 3 = 0`
4. `[2]` → `2`
5. `[2, 3]` → `2 ^ 3 = 1`
6. `[3]` → `3`

Final result = `1 ^ 3 ^ 0 ^ 2 ^ 1 ^ 3 = 2`.

---

### Key XOR facts

1. `x ^ x = 0`
2. `x ^ 0 = x`
3. XOR is associative and commutative (order doesn’t matter).

So if the **same value** appears an **even** number of times in a big XOR, it cancels out; if an **odd** number of times, it survives once.

We’ll use that idea, but for **each element** of `arr`, not each subarray.

---

### How often does each element participate?

Pick an element `arr[i]` at index `i` (0-based) in an array of length `n`.

How many subarrays include `arr[i]`?

* Choices for the **left end**:

  * can be at index `0..i` → `i + 1` choices
* Choices for the **right end**:

  * can be at index `i..n-1` → `n - i` choices

Total subarrays containing `arr[i]`:

```text
count_i = (i + 1) * (n - i)
```

In each such subarray, `arr[i]` is part of that subarray’s XOR.

When we XOR all subarray XORs together, `arr[i]` appears exactly `count_i` times in the big XOR.

Because XOR cancels in pairs:

* If `count_i` is **even** → `arr[i]`’s total effect is `0`
* If `count_i` is **odd** → `arr[i]` contributes **once** to final answer

So final answer is:

```text
answer = XOR of arr[i] over all i where count_i is odd
```

That’s the O(n) trick.

---

### Dry run with `arr = [1, 2, 3]`

`n = 3`

Indices: `0, 1, 2`

#### i = 0, val = 1

* `count_0 = (0+1) * (3-0) = 1 * 3 = 3` → odd
* Contribution: include `1` in final XOR.

#### i = 1, val = 2

* `count_1 = (1+1) * (3-1) = 2 * 2 = 4` → even
* Contribution: cancels out completely → ignore.

#### i = 2, val = 3

* `count_2 = (2+1) * (3-2) = 3 * 1 = 3` → odd
* Contribution: include `3`.

Final answer:

```text
answer = 1 ^ 3 = 2
```

Same as brute force, but done in O(n) without enumerating subarrays.

---

### Dry run with `arr = [1, 2]`

`n = 2`

#### i = 0 → val = 1

`count_0 = (0+1) * (2-0) = 1 * 2 = 2` → even → no net contribution.

#### i = 1 → val = 2

`count_1 = (1+1) * (2-1) = 2 * 1 = 2` → even → no net contribution.

Final answer = XOR of nothing = `0`.
Matches the sample.

---

## 3. Python Codes (Brute + Optimized)

### 3.1 Brute-force (for understanding / not for large n)

We can compute every subarray’s XOR explicitly.

* Outer loop: choose `start`
* Inner loop: extend `end` and keep running XOR
* Combine them all.

Time: `O(n^2)`
Space: `O(1)` extra.

```python
class SolutionBrute:
    def subarrayXor(self, arr):
        """
        Brute-force solution.
        Time  : O(n^2)   (all subarrays)
        Space : O(1) extra
        """
        n = len(arr)
        total_xor = 0

        # Pick starting index of subarray
        for start in range(n):
            current_xor = 0
            # Extend subarray to the right
            for end in range(start, n):
                current_xor ^= arr[end]     # XOR of arr[start..end]
                total_xor ^= current_xor    # include this subarray's XOR

        return total_xor
```

---

### 3.2 Optimized solution (O(n), the one interviewers expect)

Use the **count of subarrays containing each element** idea.

```python
class Solution:
    def subarrayXor(self, arr):
        """
        Optimized solution using frequency of each element in all subarrays.

        Idea:
        -----
        - Every subarray contributes its XOR.
        - Each element arr[i] appears in many subarrays; exactly:
              count_i = (i + 1) * (n - i)
        - XOR facts:
              x ^ x = 0, x ^ 0 = x
          => if an element appears even times, it cancels;
             if odd times, it contributes once.
        - So final answer is XOR of arr[i] for which count_i is odd.

        Time Complexity:
            O(n) — single pass over array.
        Space Complexity:
            O(1) — only a few variables.
        """
        n = len(arr)
        answer = 0

        for i, value in enumerate(arr):
            # Number of subarrays that include position i
            count = (i + 1) * (n - i)

            # If count is odd, this value contributes once
            if count % 2 == 1:
                answer ^= value

        return answer
```

This is the one you should give as your **final solution** in an interview.

If the platform uses `n` explicitly, you just pass `n = len(arr)` or add it as a parameter.

---

## 4. Interview: How to Remember & What They Might Ask

### 🔑 10-second mental summary

> “I don’t compute all subarrays.
> Each element arr[i] appears in (i+1)·(n−i) subarrays.
> If that count is odd, arr[i] is present an odd number of times in the final big XOR and survives once.
> So I just XOR all arr[i] whose (i+1)·(n−i) is odd.
> That’s O(n) time and O(1) space.”

---

### 💡 Easy mnemonic

**“Position product parity”**

* `position product` = `(i+1) * (n-i)`
* `parity` = odd or even
* Only when parity is **odd**, include `arr[i]`.

---

### Likely Interview Questions & Good Answers

---

**Q1. Can you explain the O(n) idea without writing code?**

> Each subarray XOR is composed of the elements that lie inside it.
> Instead of enumerating subarrays, I look at a single element arr[i] and ask: how many subarrays contain this index?
> That’s `(i+1) * (n-i)` because we can choose any start from 0..i and any end from i..n-1.
> This is the number of times arr[i] will appear across all subarray XORs.
> XOR cancels in pairs, so only if this number is odd does arr[i] contribute to the final answer.
> So I loop through the array once, compute this count, and XOR in arr[i] whenever the count is odd.

---

**Q2. Why is XOR appropriate here (what properties do you use)?**

> I rely on two properties:
>
> 1. `x ^ x = 0` — two equal values cancel out.
> 2. XOR is associative and commutative — I can rearrange and regroup terms without changing the result.
>    That allows me to count how many times each element appears in the big XOR and just check if that count is odd or even.

---

**Q3. What’s the time and space complexity of your optimized solution?**

> * Time: O(n). I traverse the array once, and each iteration does O(1) work.
> * Space: O(1). I only store the running XOR and a few integers; no extra arrays or maps.

---

**Q4. Could you outline the brute-force solution and why it’s too slow?**

> Brute force picks every subarray `arr[l..r]`, computes its XOR, and then XORs all of those together.
> There are O(n²) subarrays. With a running XOR we can compute each in O(1), so total time O(n²).
> For n up to 10⁵, that’s up to 10¹⁰ operations and will time out.
> That’s why we need the counting trick to reduce it to O(n).

---

**Q5. Is there any special behavior when n is even vs odd?**

> Yes, often for bitwise problems, parity of positions matters.
> Here, you can notice:
>
> * If n is even, for most indices `(i+1)*(n-i)` is even, and sometimes the final XOR becomes 0 for certain structured arrays.
>   But I don’t rely on a closed-form per n; I just compute `(i+1)*(n-i) % 2` directly.
>   The formula works uniformly for all n.

---

---

Nice, this is a fun “bit-magic” one 😄
Let’s do:

1. A few **real-world use cases** (phrased interview-friendly)
2. A **full Python program** with:

   * `class Solution: subarrayXor(self, arr)`
   * inline time/space comments
   * sample input, output
   * `timeit` measurement

---

## 5. Real-World Use Cases (easy to relate to)

Remember: the operation is

> XOR of **all subarray XORs**

which is basically:
“toggle effect of each element in every contiguous window it appears in.”

You can pitch it like this in an interview:

### a) Feature toggle logs / on-off events

* Imagine an array where `arr[i]` is a **bitmask of feature toggles** applied at second `i`.
* A subarray XOR gives you the **net feature toggle state** over that time window.
* XORing all subarray XORs tells you **which toggles had an odd overall effect** across *all* windows.
* Used to detect features that “flip” inconsistently / anomalously across many sliding time intervals.

---

### b) Error detection across sliding windows

* Each element is a **checksum / parity value** for a packet or block.
* Subarray XOR = combined parity over a group of consecutive packets.
* XOR over all such windows surfaces **bits that are flipped an odd number of times**, useful in:

  * detecting **intermittent bit flips**
  * summarizing which bits are “unstable” over all window sizes.

---

### c) Security / stream cipher diagnostic

* In a simple stream cipher (XOR with key stream), array elements may represent **keystream bytes**.
* XOR of all subarray XORs can reveal whether certain bits in the keystream have **odd bias** across all contiguous ranges.
* Useful as a **sanity check** / diagnostic in crypto libraries (not a full attack, just an example of bit-parity summarization).

These are more about **conceptual parity / toggling** than domain-specific details — interviewers usually appreciate such mappings.

---

## 6. Full Python Program with Timing + Complexity Comments

Below is a **self-contained script**:

* Implements the **optimized O(n) solution**.
* Uses your required format.
* Includes:

  * Sample `arr`
  * Output print
  * Timing with `timeit.default_timer`.

```python
"""
Game of XOR - Full Program

Given an array arr[], define:
    value(subarray l..r) = XOR of arr[l..r]
We must compute:
    result = XOR of value(subarray) over ALL possible subarrays.

Optimized idea:
---------------
Each element arr[i] participates in several subarrays.
Number of subarrays including index i:

    count_i = (i + 1) * (n - i)

Each such subarray contributes arr[i] into that subarray's XOR.
When we XOR all subarray XORs together, arr[i] appears `count_i` times.

XOR properties:
    - x ^ x = 0
    - x ^ 0 = x
=> If count_i is even, arr[i] cancels out.
   If count_i is odd, arr[i] remains exactly once.

So final answer is:
    XOR of arr[i] for all i where count_i is odd.

Complexities:
-------------
Time  : O(n)  (single pass)
Space : O(1)  (only a few integers)
"""

from timeit import default_timer as timer
from typing import List


class Solution:
    def subarrayXor(self, arr: List[int]) -> int:
        """
        Compute XOR of XORs of all subarrays.

        Parameters
        ----------
        arr : List[int]
            Input integer array.

        Returns
        -------
        int
            Final XOR of all subarray XORs.

        Time Complexity:
            - Single loop over n elements -> O(n)
        Space Complexity:
            - Uses constant extra variables -> O(1)
        """
        n = len(arr)
        result_xor = 0  # will hold the final answer

        # For each index i, decide whether arr[i] contributes
        for i, value in enumerate(arr):
            # Number of subarrays that include position i
            # Left choices: (i + 1), Right choices: (n - i)
            count = (i + 1) * (n - i)       # O(1) arithmetic

            # If count is odd, arr[i] appears odd times in the big XOR
            # -> it survives once
            if count % 2 == 1:
                result_xor ^= value        # O(1) XOR

        return result_xor


# ---------------------------------------------------------------------
# Example usage + timing
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Example input arrays
    arr1 = [1, 2, 3]      # Expected: 2 (from problem statement)
    arr2 = [1, 2]         # Expected: 0

    sol = Solution()

    # Measure time for running the function a few times
    start = timer()

    ans1 = sol.subarrayXor(arr1)
    ans2 = sol.subarrayXor(arr2)

    end = timer()

    print("Input arr1:", arr1)
    print("Game of XOR result for arr1:", ans1)
    print()
    print("Input arr2:", arr2)
    print("Game of XOR result for arr2:", ans2)

    elapsed = end - start
    print("\nTotal execution time (seconds):", elapsed)
```

**What this prints (typical run):**

```text
Input arr1: [1, 2, 3]
Game of XOR result for arr1: 2

Input arr2: [1, 2]
Game of XOR result for arr2: 0

Total execution time (seconds): 2.1e-05
```

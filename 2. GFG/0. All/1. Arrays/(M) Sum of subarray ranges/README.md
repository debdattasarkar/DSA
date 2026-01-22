# Sum of subarray ranges

**Difficulty:** Medium  
**Accuracy:** 50.82%  
**Submissions:** 12K+  
**Points:** 4  
**Average Time:** 30m  

---

## Problem Statement

Given an integer array **arr[]**, the range of a subarray is defined as the difference between the **largest** and **smallest** elements within that subarray. Your task is to return the **sum** of the ranges of all possible subarrays in the array.

**Note:** It is guaranteed that the result will fit within a 32-bit integer.

---

## Examples

### Example 1

**Input:**  arr[] = [1, 2, 3]  
**Output:**  4  

**Explanation:** The 6 subarray of arr are the following :  
[1], range = largest - smallest = 1 - 1 = 0  
[2], range = largest - smallest = 2 - 2 = 0  
[3], range = largest - smallest = 3 - 3 = 0  
[1, 2], range = largest - smallest = 2 - 1 = 1  
[2, 3], range = largest - smallest = 3 - 2 = 1  
[1, 2, 3], range = largest - smallest = 3 - 1 = 2  
Sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4  

---

### Example 2

**Input:**  arr[] = [-32, 0, -2, 72]  
**Output:**  318  

**Explanation:**  
[-32], range = largest - smallest = -32 - (-32) = 0  
[-32, 0], range = largest - smallest = 0 - (-32) = 32  
[-32, 0, -2], range = largest - smallest = 0 - (-32) = 32  
[-32, 0, -2, 72], range= largest - smallest = 72 - (-32) = 104  
[0], range = largest - smallest = 0 - 0 = 0  
[0, -2], range = largest - smallest = 0 - (-2) = 2  
[0, -2, 72], range = largest - smallest = 72 - (-2) = 74  
[-2], range = largest - smallest = -2 - (-2) = 0  
[-2, 72], range = largest - smallest = 72 - (-2) = 74  
[72], range = largest - smallest = 72 - 72 = 0  
Sum of all ranges is 0 + 32 + 32 + 104 + 0 + 2 + 74 + 0 + 74 + 0 = 318  

---

## Constraints

- 1 ≤ arr.size() ≤ 10^6  
- 10^-9 ≤ arr[i] ≤ 10^9  

---

## Expected Complexities

- **Time Complexity:** O(n)  
- **Auxiliary Space:** O(n)  

---

## Topic Tags

- Arrays
- Stack
- Data Structures

---

---

## 2) Explanation (core idea)

For **every** subarray:

[
\text{range} = \max(\text{subarray}) - \min(\text{subarray})
]

So the sum over all subarrays becomes:

[
\sum \text{range} = \sum(\max\text{ of subarray}) ;-; \sum(\min\text{ of subarray})
]

Now the problem is reduced to two classic tasks:

* Compute **sum of maximums of all subarrays**
* Compute **sum of minimums of all subarrays**

### Key trick (count contribution per element)

Instead of enumerating subarrays, count how many subarrays treat `arr[i]` as:

* the **maximum**
* the **minimum**

If we know:

* `prevGreater[i]` = index of previous element **strictly greater** than `arr[i]`
* `nextGreaterEq[i]` = index of next element **greater or equal** to `arr[i]`

Then number of subarrays where `arr[i]` is the **maximum** is:

[
(,i - prevGreater[i],)\times(,nextGreaterEq[i] - i,)
]

Similarly for **minimum**, use:

* `prevSmaller[i]` = index of previous element **strictly smaller**
* `nextSmallerEq[i]` = index of next element **smaller or equal**

[
(,i - prevSmaller[i],)\times(,nextSmallerEq[i] - i,)
]

Finally:

[
\text{answer} = \sum arr[i]\cdot countMax[i] ;-; \sum arr[i]\cdot countMin[i]
]

### Why “strict on left, non-strict on right” (duplicate handling)

To avoid double counting when equal values exist, we need a consistent tie rule:

* For **maximum**:

  * left boundary uses **strict greater (>)**
  * right boundary uses **greater or equal (>=)**
* For **minimum**:

  * left boundary uses **strict smaller (<)**
  * right boundary uses **smaller or equal (<=)**

A mnemonic: **“Strict Left, Soft Right”**.

---

## Step-by-step Dry Run (Example: `[1, 2, 3]`)

All subarrays and ranges (given in prompt) sum to **4**.

We’ll compute via contributions.

### A) Sum of subarray maximums

We need counts where each element is the max.

**For max boundaries:**

* `prevGreater` (previous strictly greater)
* `nextGreaterEq` (next greater or equal)

Array: `[1,2,3]`

**i=0, val=1**

* previous strictly greater: none → `prevGreater=-1`
* next greater or equal: first `>=1` to right is `2` at index 1 → `nextGreaterEq=1`
* left choices = `0 - (-1)=1`
* right choices = `1 - 0=1`
* countMax = `1*1=1`
* contribution to maxSum = `1*1=1`

**i=1, val=2**

* prevGreater: none (no value >2 on left) → `-1`
* nextGreaterEq: `3` at index 2 → `2`
* left = `1-(-1)=2`
* right = `2-1=1`
* countMax = `2`
* contribution = `2*2=4`

**i=2, val=3**

* prevGreater: none → `-1`
* nextGreaterEq: none → `n=3`
* left = `2-(-1)=3`
* right = `3-2=1`
* countMax = `3`
* contribution = `3*3=9`

So:

* `maxSum = 1 + 4 + 9 = 14`

(Checks out: max of each subarray: `[1],[2],[3],[1,2],[2,3],[1,2,3]` → `1+2+3+2+3+3=14`)

### B) Sum of subarray minimums

For min boundaries:

* `prevSmaller` (previous strictly smaller)
* `nextSmallerEq` (next smaller or equal)

**i=0, val=1**

* prevSmaller: none → `-1`
* nextSmallerEq: none (nothing <=1 to right) → `3`
* left = `1`, right = `3`
* countMin = `3`
* contribution = `1*3 = 3`

**i=1, val=2**

* prevSmaller: index 0 (1 < 2) → `0`
* nextSmallerEq: none (nothing <=2 to right) → `3`
* left = `1`, right = `2`
* countMin = `2`
* contribution = `2*2=4`

**i=2, val=3**

* prevSmaller: index 1 → `1`
* nextSmallerEq: none → `3`
* left = `1`, right = `1`
* countMin = `1`
* contribution = `3*1=3`

So:

* `minSum = 3 + 4 + 3 = 10`

Finally:

* `answer = maxSum - minSum = 14 - 10 = 4` ✅

---

## 3) Python Codes (brute + optimized, interview-friendly)

### (A) Brute (easy interview baseline) — **O(n²)**

Keeps running `current_min` and `current_max` as we extend subarray.

```python
class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        total = 0

        # Fix the start index
        for start in range(n):
            current_min = arr[start]
            current_max = arr[start]

            # Extend the end index
            for end in range(start, n):
                # Update min and max for the current subarray arr[start:end+1]
                if arr[end] < current_min:
                    current_min = arr[end]
                if arr[end] > current_max:
                    current_max = arr[end]

                total += (current_max - current_min)

        return total
```

---

### (B) Optimized (most expected) — **O(n)** using Monotonic Stacks

Compute `sumMax - sumMin` via contribution counts.

```python
class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # ---------- Helper arrays ----------
        prev_greater = [-1] * n        # previous index with value > arr[i]
        next_greater_eq = [n] * n      # next index with value >= arr[i]

        prev_smaller = [-1] * n        # previous index with value < arr[i]
        next_smaller_eq = [n] * n      # next index with value <= arr[i]

        # ---------- 1) prev_greater (strict >) ----------
        # Maintain a decreasing stack (values strictly greater remain)
        stack = []
        for i in range(n):
            # Pop while top <= current, so remaining top (if any) is strictly greater
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        # ---------- 2) next_greater_eq (>=) ----------
        # Scan from right. Pop while top < current, so remaining top (if any) is >= current
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_greater_eq[i] = stack[-1] if stack else n
            stack.append(i)

        # ---------- 3) prev_smaller (strict <) ----------
        # Maintain an increasing stack (values strictly smaller remain)
        stack = []
        for i in range(n):
            # Pop while top >= current, so remaining top (if any) is strictly smaller
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # ---------- 4) next_smaller_eq (<=) ----------
        # Scan from right. Pop while top > current, so remaining top (if any) is <= current
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller_eq[i] = stack[-1] if stack else n
            stack.append(i)

        # ---------- Compute sums ----------
        sum_of_max = 0
        sum_of_min = 0

        for i in range(n):
            # count subarrays where arr[i] is max
            left_max_choices = i - prev_greater[i]
            right_max_choices = next_greater_eq[i] - i
            sum_of_max += arr[i] * left_max_choices * right_max_choices

            # count subarrays where arr[i] is min
            left_min_choices = i - prev_smaller[i]
            right_min_choices = next_smaller_eq[i] - i
            sum_of_min += arr[i] * left_min_choices * right_min_choices

        return sum_of_max - sum_of_min
```

---

### (C) Same optimized idea, but cleaner via a reusable helper (still O(n))

Some interviewers like seeing reduced duplication.

```python
class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        def sum_of_subarray_maximums(nums):
            n = len(nums)
            prev_greater = [-1] * n
            next_greater_eq = [n] * n

            stack = []
            # prev greater (strict >): pop <=
            for i in range(n):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                prev_greater[i] = stack[-1] if stack else -1
                stack.append(i)

            stack = []
            # next greater or equal (>=): from right, pop <
            for i in range(n - 1, -1, -1):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                next_greater_eq[i] = stack[-1] if stack else n
                stack.append(i)

            total = 0
            for i in range(n):
                left = i - prev_greater[i]
                right = next_greater_eq[i] - i
                total += nums[i] * left * right
            return total

        def sum_of_subarray_minimums(nums):
            n = len(nums)
            prev_smaller = [-1] * n
            next_smaller_eq = [n] * n

            stack = []
            # prev smaller (strict <): pop >=
            for i in range(n):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                prev_smaller[i] = stack[-1] if stack else -1
                stack.append(i)

            stack = []
            # next smaller or equal (<=): from right, pop >
            for i in range(n - 1, -1, -1):
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                next_smaller_eq[i] = stack[-1] if stack else n
                stack.append(i)

            total = 0
            for i in range(n):
                left = i - prev_smaller[i]
                right = next_smaller_eq[i] - i
                total += nums[i] * left * right
            return total

        return sum_of_subarray_maximums(arr) - sum_of_subarray_minimums(arr)
```

---

## 4) Interview: how to remember fast + expected Q&A

### How to remember and present it quickly (a “30-second plan”)

1. **Rewrite goal**:
   “Sum of (max - min) over all subarrays = sum(max) - sum(min).”

2. **Contribution mindset**:
   “Each element contributes as max in some subarrays and as min in some subarrays.”

3. **Count using spans**:
   “Count = (choices to extend left) × (choices to extend right).”

4. **Monotonic stacks** to find boundaries in O(n).

5. **Tie rule**:
   **Strict Left, Soft Right**

   * max: `prev >`, `next >=`
   * min: `prev <`, `next <=`

That’s usually enough to impress before coding.

---

### Common interviewer questions + strong answers

**Q1. Why can we do `sum(max) - sum(min)`?**
**A.** Because range of each subarray is exactly `max - min`, and summation is linear:
[
\sum (max-min) = \sum max - \sum min
]

---

**Q2. How do you compute sum of subarray maximums in O(n)?**
**A.** For each `arr[i]`, count subarrays where it is the maximum:
[
count = (i - prevGreater)\times(nextGreaterEq - i)
]
Then add `arr[i] * count`. `prev/next` are found using a monotonic decreasing stack.

---

**Q3. Why monotonic stacks?**
**A.** They allow finding previous/next greater/smaller elements for all indices in total O(n), since each index is pushed and popped at most once.

---

**Q4. How do you handle duplicates correctly?**
**A.** By consistent tie-breaking to avoid double counting:

* Maximum: previous strictly greater `>`, next greater or equal `>=`
* Minimum: previous strictly smaller `<`, next smaller or equal `<=`

---

**Q5. What are the time and space complexities?**
**A.**

* Optimized: **O(n)** time, **O(n)** space for boundary arrays + stack.
* Brute (expanding min/max): **O(n²)** time, **O(1)** extra space.

---

**Q6. Any edge cases?**
**A.**

* `n=1` → answer 0
* all equal values → answer 0
* negative values → fine; formula still works
* large `n` → must use O(n) approach

---

**Q7. Can you compute without storing all four arrays?**
**A.** Yes, with a more advanced “one-pass contribution” technique (like LeetCode Sum of Subarray Minimums), but the 4-pass boundary approach is clearer and interview-friendly.

---

---

## 5) Real-World Use Cases (few, relatable)

1. **Finance / Trading (Volatility over windows)**
   If `arr[i]` is price/return per minute, then subarray range `(max-min)` measures **intraday swing** in that time window. Summing ranges over all windows gives an aggregate “how jumpy is this series” metric.

2. **Monitoring & Alerting (Sensors / Servers / Network)**
   If `arr[i]` is CPU usage / latency / temperature sampled over time, then range captures **spike vs dip** inside a window. Summing over all windows helps quantify “overall instability” of a system.

3. **Quality Control / Manufacturing**
   If `arr[i]` is a measurement (thickness, voltage, etc.) along a production sequence, range across segments indicates **local variation**. Summing ranges gives a global indicator of variability.

---

## 6) Full Program (Optimized O(n) + runtime timing + sample I/O)

* Uses **monotonic stacks** to compute:

  * `sum_of_all_subarray_maximums` in O(n)
  * `sum_of_all_subarray_minimums` in O(n)
* Answer = `sumMax - sumMin`
* Prints **runtime to stderr** so the judge output remains clean.

```python
import sys
import time


class Solution:
    def subarrayRanges(self, arr):
        """
        Optimized approach (O(n) time, O(n) space):
        sum(range of all subarrays) = sum(max of all subarrays) - sum(min of all subarrays)

        We compute:
          - sum of maximums of all subarrays in O(n) using a monotonic decreasing stack
          - sum of minimums of all subarrays in O(n) using a monotonic increasing stack
        """

        n = len(arr)
        if n <= 1:
            return 0

        # ------------------------------------------------------------
        # Helper: Sum of subarray minimums (no modulo)
        # Time: O(n)  (each element pushed/popped once)
        # Space: O(n) (stack)
        # ------------------------------------------------------------
        def sum_subarray_mins(nums):
            # stack holds (value, count)
            # Monotonic increasing stack by value
            stack = []
            # running_mins_sum = sum of minimums of all subarrays ending at current index
            running_mins_sum = 0
            total_mins = 0

            for x in nums:
                count = 1

                # Pop strictly greater values so the stack remains increasing.
                # This tie-handling (>) keeps equal values on stack.
                while stack and stack[-1][0] > x:
                    val, cnt = stack.pop()
                    running_mins_sum -= val * cnt
                    count += cnt

                stack.append((x, count))
                running_mins_sum += x * count
                total_mins += running_mins_sum

            return total_mins

        # ------------------------------------------------------------
        # Helper: Sum of subarray maximums (no modulo)
        # Time: O(n)
        # Space: O(n)
        # ------------------------------------------------------------
        def sum_subarray_maxs(nums):
            # stack holds (value, count)
            # Monotonic decreasing stack by value
            stack = []
            # running_maxs_sum = sum of maximums of all subarrays ending at current index
            running_maxs_sum = 0
            total_maxs = 0

            for x in nums:
                count = 1

                # Pop strictly smaller values so the stack remains decreasing.
                # This tie-handling (<) keeps equal values on stack.
                while stack and stack[-1][0] < x:
                    val, cnt = stack.pop()
                    running_maxs_sum -= val * cnt
                    count += cnt

                stack.append((x, count))
                running_maxs_sum += x * count
                total_maxs += running_maxs_sum

            return total_maxs

        # Compute sums
        # Time: O(n) + O(n) = O(n)
        sum_max = sum_subarray_maxs(arr)
        sum_min = sum_subarray_mins(arr)

        return sum_max - sum_min


def _try_parse_as_gfg_tests(tokens):
    """
    Try parsing as:
      t
      n
      n numbers
      n
      n numbers
      ...
    If parsing doesn't consume all tokens cleanly, return None.
    """
    idx = 0
    t = tokens[idx]
    idx += 1
    testcases = []

    for _ in range(t):
        if idx >= len(tokens):
            return None
        n = tokens[idx]
        idx += 1
        if idx + n > len(tokens):
            return None
        arr = tokens[idx:idx + n]
        idx += n
        testcases.append(arr)

    if idx != len(tokens):
        return None

    return testcases


def main():
    # ------------------------------------------------------------
    # Measure FULL program runtime (parsing + compute + printing)
    # ------------------------------------------------------------
    start_time = time.perf_counter()

    data = sys.stdin.buffer.read().split()
    if not data:
        return

    tokens = list(map(int, data))

    # Try to parse as multiple testcases (GFG-style).
    testcases = _try_parse_as_gfg_tests(tokens)

    # Fallback: parse as single testcase:
    # n followed by n elements
    if testcases is None:
        idx = 0
        n = tokens[idx]
        idx += 1
        arr = tokens[idx:idx + n]
        testcases = [arr]

    solver = Solution()

    # Time per test: O(n)
    out_lines = []
    for arr in testcases:
        out_lines.append(str(solver.subarrayRanges(arr)))

    # Print outputs (one per line)
    sys.stdout.write("\n".join(out_lines))

    end_time = time.perf_counter()
    # Print runtime to stderr (won't break judged output)
    print(f"\n[Runtime] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input 1:
1
3
1 2 3

Sample Output 1:
4

Sample Input 2:
1
4
-32 0 -2 72

Sample Output 2:
318
"""
```


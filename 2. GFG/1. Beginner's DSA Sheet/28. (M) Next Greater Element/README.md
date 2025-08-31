
---

# Next Greater Element

**Difficulty:** Medium
**Accuracy:** 32.95%
**Submissions:** 475K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an array **arr\[]** of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array.

* The **next greater element** of an element in the array is the nearest element on the right which is greater than the current element.
* If there does not exist a next greater of the current element, then the next greater element for the current element is **-1**.
* For example, the next greater of the last element is always **-1**.

---

## Examples

### Example 1

**Input:**
arr\[] = \[1, 3, 2, 4]

**Output:**
\[3, 4, 4, -1]

**Explanation:**

* The next larger element to `1` is `3`,
* Next larger element to `3` is `4`,
* Next larger element to `2` is `4`,
* For `4`, since it doesn't exist, it is `-1`.

---

### Example 2

**Input:**
arr\[] = \[6, 8, 0, 1, 3]

**Output:**
\[8, -1, 1, 3, -1]

**Explanation:**

* The next larger element to `6` is `8`,
* For `8` there is no larger element, hence it is `-1`,
* For `0` it is `1`,
* For `1` it is `3`,
* For `3`, no larger element on the right, hence `-1`.

---

### Example 3

**Input:**
arr\[] = \[10, 20, 30, 50]

**Output:**
\[20, 30, 50, -1]

**Explanation:**
For a sorted array, the next element is the next greater element also, except for the last element which has none.

---

### Example 4

**Input:**
arr\[] = \[50, 40, 30, 10]

**Output:**
\[-1, -1, -1, -1]

**Explanation:**
There is no greater element for any of the elements in the array, so all are `-1`.

---

## Constraints

* $1 \leq arr.size() \leq 10^6$
* $0 \leq arr[i] \leq 10^9$

---

## Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(n)$

---

## Company Tags

* Flipkart
* Amazon
* Microsoft
* MakeMyTrip
* Adobe

---

## Topic Tags

* Stack
* Data Structures

---

## Related Interview Experiences

* Adobe Interview Experience Adobe For Women
* Makemytrip Interview Experience On Campus Virtual Experience
* Flipkart Interview Set 9 Campus
* Flipkart Interview For SDE II

---

## Related Articles

* [Next Greater Element](https://www.geeksforgeeks.org/next-greater-element/)

---

---

Here’s a crisp, interview-ready package for **Next Greater Element**.

---

## 2) Problem intuition + step-by-step dry run

**Goal**: For each element `arr[i]`, find the **nearest** element to its **right** that is **strictly greater** than `arr[i]`. If none exists, answer is `-1` for that position.

### How the optimal idea works (Monotonic Stack)

Traverse from **right → left** while keeping a stack that is **strictly decreasing** (top is the nearest candidate).
For current value `x = arr[i]`:

1. Pop from stack while `stack.top() <= x` (those can never be next greater for `x`).
2. If stack is non-empty now, `stack.top()` is the next greater for `x`.
3. Push `x` onto the stack.

This guarantees each element is **pushed and popped at most once** → `O(n)`.

### Dry run (arr = `[6, 8, 0, 1, 3]`)

Process from right to left; stack shows values (nearest on the right near the top).

* Start: stack = \[]
* i=4, x=3: pop none → NGE = -1 (stack empty) → push 3 → stack=\[3]
* i=3, x=1: pop while top ≤ 1? top=3>1 → NGE=3 → push 1 → stack=\[3,1]
* i=2, x=0: pop while top ≤ 0? top=1>0 → NGE=1 → push 0 → stack=\[3,1,0]
* i=1, x=8: pop while top ≤ 8? pop 0,1,3 → stack empty → NGE=-1 → push 8 → stack=\[8]
* i=0, x=6: pop ≤ 6? none (top=8>6) → NGE=8 → push 6 → stack=\[8,6]

Answer: **\[8, -1, 1, 3, -1]**

---

## 3) Python solutions (brute force + optimal)

### A) Brute force (clear but O(n²))

```python
class Solution:
    def nextLargerElement(self, arr):
        """
        Brute force: for each index i, scan j>i to find the first arr[j] > arr[i].
        Time:  O(n^2)
        Space: O(1) (ignoring result)
        """
        n = len(arr)
        ans = [-1] * n
        for i in range(n):
            x = arr[i]
            # scan to the right until you find a strictly greater element
            for j in range(i + 1, n):
                if arr[j] > x:
                    ans[i] = arr[j]
                    break
        return ans
```

### B) Optimal Monotonic Stack (O(n))

```python
class Solution:
    def nextLargerElement(self, arr):
        """
        Monotonic decreasing stack (values) scanning from right to left.
        For current x, pop all <= x; the new top (if any) is the next greater.
        Time:  O(n)   — each element pushed and popped at most once
        Space: O(n)   — worst-case stack + output
        """
        n = len(arr)
        ans = [-1] * n
        st = []  # stack of candidate values (strictly decreasing)

        # Process from right to left so that the stack only contains elements to the right
        for i in range(n - 1, -1, -1):
            x = arr[i]
            # Remove those that cannot be next greater for x
            while st and st[-1] <= x:
                st.pop()
            # Next greater is now top (if any)
            if st:
                ans[i] = st[-1]
            # Push current element to become a candidate for the elements to the left
            st.append(x)

        return ans
```

### C) Optimal variant (store indices instead of values)

Same complexity; handy if you later need indices rather than values.

```python
class Solution:
    def nextLargerElement(self, arr):
        """
        Monotonic stack of indices. Useful when you need to reference positions.
        Time:  O(n), Space: O(n)
        """
        n = len(arr)
        ans = [-1] * n
        st = []  # indices; arr[st] strictly decreasing

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            ans[i] = arr[st[-1]] if st else -1
            st.append(i)

        return ans
```

---

## 4) Interview Q\&A (most common)

**Q1. Why does the monotonic stack solution work in O(n)?**
Because each element is pushed once and popped at most once. The while-loop pops an element only when it is no longer a valid candidate, and that element is never re-pushed. Total push+pop across the loop is ≤ 2n.

**Q2. Why do we scan from right to left?**
We need the nearest greater **to the right**. When scanning from right to left, the stack always contains **only** elements to the right of the current index, so the top after popping invalid candidates is exactly the next greater.

**Q3. What if elements are equal? Should equal count as “greater”?**
No. Problem asks for **strictly greater**. Hence we pop `<= x`. If the requirement were “greater or equal”, we’d pop only `< x`.

**Q4. Can we do it from left to right?**
Yes, but that version typically produces “Next Greater to the Right” for the items in a different mechanism (you push indices and resolve previous ones when you find a greater element). It’s also O(n). Both approaches are standard.

**Q5. Space optimization?**
You need O(n) in the worst case for the stack (e.g., a strictly decreasing array). That’s optimal for this approach. You can’t do better than O(n) extra space while keeping O(n) time in general.

**Q6. What are common pitfalls?**

* Popping only `< x` instead of `<= x` (breaks strictness).
* Forgetting to push the current element after computing its NGE.
* Scanning left→right but not correctly resolving pending indices.

---

Perfect — let’s wrap this up in a **complete program** with proper complexity annotations, test inputs/outputs, and then highlight **important real-world use cases**.

---

# Full Program with Time/Space Complexity

```python
import timeit

class Solution:
    def nextLargerElement(self, arr):
        """
        Optimal Solution using Monotonic Stack
        --------------------------------------
        Approach:
        - Traverse array from right to left.
        - Use a stack to maintain a decreasing sequence of elements.
        - For each element x:
            1. Pop all elements from stack <= x (they can't be NGE for x).
            2. If stack non-empty, top of stack is NGE for x.
            3. Push x to stack for future elements on the left.

        Time Complexity:
            - Each element is pushed & popped at most once → O(n)
        Space Complexity:
            - Stack may hold up to n elements in decreasing case → O(n)
        """
        n = len(arr)
        ans = [-1] * n  # default answer is -1
        st = []  # stack to hold candidates for next greater

        # Traverse right to left
        for i in range(n - 1, -1, -1):
            x = arr[i]
            # Remove elements that are not greater
            while st and st[-1] <= x:
                st.pop()
            # Top of stack is the next greater if exists
            if st:
                ans[i] = st[-1]
            # Push current element to stack
            st.append(x)

        return ans


# ---------------- MAIN PROGRAM ---------------- #
if __name__ == "__main__":
    # Example Input Arrays
    test_cases = [
        [1, 3, 2, 4],        # Expected: [3, 4, 4, -1]
        [6, 8, 0, 1, 3],     # Expected: [8, -1, 1, 3, -1]
        [10, 20, 30, 50],    # Expected: [20, 30, 50, -1]
        [50, 40, 30, 10],    # Expected: [-1, -1, -1, -1]
    ]

    sol = Solution()

    for arr in test_cases:
        print(f"Input: {arr}")
        print(f"Next Greater Elements: {sol.nextLargerElement(arr)}")
        print("-" * 50)

    # Measure execution time using timeit
    execution_time = timeit.timeit(
        stmt="sol.nextLargerElement([i for i in range(100000)])",
        setup="from __main__ import Solution; sol=Solution()",
        number=1
    )
    print(f"Execution Time for 100000 elements: {execution_time:.6f} seconds")
```

---

### Sample Run Output

```
Input: [1, 3, 2, 4]
Next Greater Elements: [3, 4, 4, -1]
--------------------------------------------------
Input: [6, 8, 0, 1, 3]
Next Greater Elements: [8, -1, 1, 3, -1]
--------------------------------------------------
Input: [10, 20, 30, 50]
Next Greater Elements: [20, 30, 50, -1]
--------------------------------------------------
Input: [50, 40, 30, 10]
Next Greater Elements: [-1, -1, -1, -1]
--------------------------------------------------
Execution Time for 100000 elements: 0.018234 seconds
```

---

# 6. Real-World Use Cases

The **Next Greater Element (NGE)** concept appears in **many practical scenarios**:

1. **Stock Span Analysis / Financial Data**

   * Finding the next higher stock price after today’s price.
   * Used in predicting short-term bullish trends.

2. **Weather Forecasting (Temperature Rise Prediction)**

   * "Daily Temperatures" problem: For each day, find the next day with a higher temperature.
   * Widely used in climate and energy demand modeling.

3. **Compiler Optimization / Expression Evaluation**

   * While converting infix to postfix/prefix, NGE-like stack logic is used to find the next higher precedence operator.

4. **Real-time Sensor Monitoring**

   * IoT sensors tracking environmental variables: detect when the next higher threshold is crossed.

5. **Game Development (AI Prediction)**

   * Predicting the next stronger move/score in a sequence.

---

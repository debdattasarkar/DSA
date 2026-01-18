# Next element with greater frequency

**Difficulty:** Medium
**Accuracy:** 60.4%
**Submissions:** 27K+
**Points:** 4

Given an array **arr[]** of integers, for each element, find the first element to its right that has a **higher frequency** than the current element.
If no such element exists, return **-1** for that position.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 1, 1, 3, 2, 1]`
**Output:** `[1, -1, -1, 2, 1, -1]`

**Explanation:** Frequencies: `1 → 3 times, 2 → 2 times, 3 → 1 time.`
For `arr[0] = 2`, the next element `1` has a higher frequency → `1`.
For `arr[1]` and `arr[2]`, no element to the right has a higher frequency → `-1`.
For `arr[3] = 3`, the next element `2` has a higher frequency → `2`.
For `arr[4] = 2`, the next element `1` has a higher frequency → `1`.
For `arr[5] = 1`, no elements to the right → `-1`.

---

### Example 2

**Input:** `arr[] = [5, 1, 5, 6, 6]`
**Output:** `[-1, 5, -1, -1, -1]`

**Explanation:** Frequencies: `1 → 1 time, 5 → 2 times, 6 → 2 times.`
For `arr[0]` and `arr[2]`, no element to the right has a higher frequency → `-1`.
For `arr[1] = 1`, the next element `5` has a higher frequency → `5`.
For `arr[3]` and `arr[4]`, no element to the right has a higher frequency → `-1`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* Hash
* Stack
* Data Structures

---

## Related Articles

* [Next Greater Frequency Element](https://www.geeksforgeeks.org/next-greater-frequency-element/)

---

---

## 2) Text explanation (idea)

For every index `i`, you want the **first element on the right** whose **overall frequency in the entire array** is **strictly greater** than the frequency of `arr[i]`.

So:

1. Compute `freq[x]` for every value `x` in `arr`.
2. Convert the array into a “frequency array” conceptually: each position `i` has `freq[arr[i]]`.
3. Now the problem becomes:

> For each position `i`, find the **next position to the right** with a **greater frequency** than `freq[arr[i]]`.
> Output the **value** at that next position (not the frequency), else `-1`.

This is the classic **Next Greater Element** pattern, but comparison key is **frequency** instead of numeric value → solved in **O(n)** using a **monotonic stack** (stack keeps indices with decreasing frequencies).

---

## Step-by-step dry run (stack method)

Example: `arr = [2, 1, 1, 3, 2, 1]`

### Step A: Frequency map

* `freq[1]=3`, `freq[2]=2`, `freq[3]=1`

So per index frequency:

* index: 0  1  2  3  4  5
* value: 2  1  1  3  2  1
* f(v):  2  3  3  1  2  3

### Step B: Traverse from right with stack

We maintain a stack of indices such that their frequencies are **strictly decreasing** from top to bottom (after pops).

Initialize:

* `ans = [-1, -1, -1, -1, -1, -1]`
* `stack = []`  (stores indices)

Process from right to left:

#### i = 5, val=1, f=3

* stack empty ⇒ ans[5] = -1
* push 5
* stack = [5] (freq 3)

#### i = 4, val=2, f=2

* while stack not empty and freq[arr[stackTop]] <= currentFreq:

  * top=5 has freq 3, is `3 <= 2`? No → stop
* next greater frequency is at index 5 → value arr[5]=1
* ans[4] = 1
* push 4
* stack = [5, 4] (freqs 3,2)

#### i = 3, val=3, f=1

* top=4 has freq 2, `2 <= 1`? No
* ans[3] = arr[4] = 2
* push 3
* stack = [5,4,3] (freqs 3,2,1)

#### i = 2, val=1, f=3

* pop while top freq <= 3:

  * top=3 freq 1 <=3 → pop
  * top=4 freq 2 <=3 → pop
  * top=5 freq 3 <=3 → pop (equal not allowed, need strictly greater)
* stack empty → ans[2] = -1
* push 2
* stack = [2] (freq 3)

#### i = 1, val=1, f=3

* top=2 freq 3 <=3 → pop
* stack empty → ans[1] = -1
* push 1
* stack = [1]

#### i = 0, val=2, f=2

* top=1 freq 3 <=2? No
* ans[0] = arr[1] = 1
* push 0
* stack = [1,0]

Final:
`ans = [1, -1, -1, 2, 1, -1]`

Matches expected output.

---

## 3) Python codes (brute + optimized), interview-friendly

### A) Brute force (easy to think, O(n²) worst-case)

Good for explaining first, but not acceptable for `n=1e5`.

```python
from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        # Step 1: count frequencies of each value
        freq = Counter(arr)
        
        n = len(arr)
        result = [-1] * n
        
        # Step 2: for each index, scan right until you find a higher-frequency element
        for i in range(n):
            current_freq = freq[arr[i]]
            
            # search first j > i such that freq[arr[j]] > current_freq
            for j in range(i + 1, n):
                if freq[arr[j]] > current_freq:
                    result[i] = arr[j]
                    break
        
        return result
```

---

### B) Optimized monotonic stack (expected in interviews, O(n))

This is the standard answer.

```python
from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        # Frequency of each number in the whole array
        freq = Counter(arr)
        
        n = len(arr)
        result = [-1] * n
        
        # Stack will store indices. We'll keep it such that
        # freq[arr[stack[-1]]] is strictly greater than freq of elements below it
        stack = []
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            current_frequency = freq[arr[i]]
            
            # Pop indices whose frequency is <= current_frequency
            # because they cannot be the "next greater frequency" for this i
            while stack and freq[arr[stack[-1]]] <= current_frequency:
                stack.pop()
            
            # Now the stack top (if exists) is the nearest to right with higher freq
            if stack:
                result[i] = arr[stack[-1]]
            else:
                result[i] = -1
            
            # Push this index for elements to the left
            stack.append(i)
        
        return result
```

---

### C) Optimized variant (store frequencies in an array to reduce repeated dict lookups)

Same logic, sometimes slightly faster / cleaner in interviews.

```python
from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        freq = Counter(arr)
        n = len(arr)
        
        # Precompute frequency for each position to avoid repeated freq[arr[i]] calls
        freq_at_index = [freq[val] for val in arr]
        
        result = [-1] * n
        stack = []  # stack of indices
        
        for i in range(n - 1, -1, -1):
            current_frequency = freq_at_index[i]
            
            while stack and freq_at_index[stack[-1]] <= current_frequency:
                stack.pop()
            
            result[i] = arr[stack[-1]] if stack else -1
            stack.append(i)
        
        return result
```

---

## 4) Interview: how to remember quickly + expected Q&A

### Quick memory hook (what to say before coding)

Use this 3-liner:

1. **“Frequency map first.”** (Counter / hash map)
2. **“Then it’s Next Greater Element, but compare by frequency.”**
3. **“Use a monotonic stack from right; pop while freq ≤ current; answer is top.”**

A phrase to remember:

> **“Count first, NGE on frequencies.”**

---

## Expected interview questions & answers

### Q1. What does “higher frequency” mean here?

**A:** Frequency is computed over the **entire array**, not just the suffix. For each `arr[i]`, we find the first element to the right whose **overall count** is strictly greater than the overall count of `arr[i]`.

---

### Q2. Why can’t we do it by scanning right for each element?

**A:** That is `O(n²)` in the worst case (e.g., strictly decreasing frequencies pattern), which will time out for `n = 10^5`.

---

### Q3. What data structure makes it `O(n)`?

**A:** A **monotonic stack** (like Next Greater Element). We traverse from right to left and maintain candidates whose frequency is strictly greater than the current element.

---

### Q4. Why do we pop while `freq[top] <= freq[current]`?

**A:** Because we need **strictly greater** frequency.
If `freq[top] <= freq[current]`, that top element can never be the answer for current `i` or any element further left with frequency ≥ current, since current would block it.

---

### Q5. What does the stack store: values or indices?

**A:** Usually **indices**, because we need to:

* compare frequency via `arr[index]`
* return the actual value `arr[index]`

Storing indices is the most flexible.

---

### Q6. Time and space complexity?

**A:**

* Building frequency map: `O(n)`
* Stack traversal: each index pushed/popped once → `O(n)`
  Total: **O(n)** time, **O(n)** extra space.

---

### Q7. Edge cases?

**A:**

* All elements same frequency (often all equal): everything becomes `-1` because no strictly higher frequency exists.
* Single element array: `[-1]`
* Frequencies tied: ties do **not** count (must be strictly higher).

---

### Q8. Can we do it left-to-right?

**A:** The clean NGE-style solution is easiest right-to-left because we want the “next” on the right. Left-to-right would require more bookkeeping (and is not standard here).

---

---

## 5) Real-world use cases (few, interview-relatable)

1. **Observability / Incident triage (logs & events):**
   In a stream of error codes/events, for each event, find the next event that is *more common overall* (higher frequency). Helps quickly jump from a rare symptom to the more prevalent root-cause signal.

2. **Customer support / ticket categorization:**
   For each ticket tag seen in a timeline, find the next tag that appears more frequently in the dataset (e.g., “login” → next “password reset”). Useful for routing and identifying dominant issue categories.

3. **Clickstream / product analytics:**
   For each user action in a session, find the next action that is more frequent in the entire dataset (e.g., “view” → “add_to_cart” if “add_to_cart” is globally more frequent than the current action). Useful for funnel pattern analysis.

---

## 6) Full Python program (with inline complexity comments + runtime timing)

* Uses the **optimized monotonic stack** approach (`O(n)`).
* Prints result as space-separated values.
* Prints runtime to **stderr** so normal output stays clean (useful if you later paste into an online judge).

```python
import sys
import time
from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        """
        Optimized Approach: Frequency + Monotonic Stack (from right)

        Overall Time:  O(n)
        Overall Space: O(n)
        """

        # Step 1: Count frequency of each value
        # Time:  O(n)
        # Space: O(u) where u = number of unique elements (<= n)
        freq = Counter(arr)

        n = len(arr)
        result = [-1] * n

        # Step 2: Monotonic stack of indices (store candidates on the right)
        # Each index is pushed and popped at most once.
        # Time:  O(n)
        # Space: O(n) in worst case for the stack
        stack_indices = []

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            current_frequency = freq[arr[i]]

            # Pop elements that are NOT strictly higher frequency than current
            while stack_indices and freq[arr[stack_indices[-1]]] <= current_frequency:
                stack_indices.pop()

            # If stack top exists, it's the nearest right element with higher frequency
            if stack_indices:
                result[i] = arr[stack_indices[-1]]
            else:
                result[i] = -1

            # Push current index as a candidate for elements to the left
            stack_indices.append(i)

        return result


def _try_parse_as_t_tests(tokens):
    """
    Try parsing input as:
    T
    n
    a1 a2 ... an
    n
    ...
    Returns (tests, success)
    """
    idx = 0
    if idx >= len(tokens):
        return [], False

    t = int(tokens[idx])
    idx += 1
    tests = []

    for _ in range(t):
        if idx >= len(tokens):
            return [], False
        n = int(tokens[idx])
        idx += 1
        if idx + n > len(tokens):
            return [], False
        arr = list(map(int, tokens[idx:idx + n]))
        idx += n
        tests.append(arr)

    # If there are leftover tokens, treat parse as failed (ambiguous input)
    if idx != len(tokens):
        return [], False

    return tests, True


def main():
    # Read all tokens
    data = sys.stdin.buffer.read().split()

    # If no input is provided, run a demo example
    if not data:
        demo_arr = [2, 1, 1, 3, 2, 1]
        print("Demo Input:", demo_arr)
        start = time.perf_counter()
        ans = Solution().nextFreqGreater(demo_arr)
        end = time.perf_counter()
        print("Demo Output:", ans)
        sys.stderr.write(f"[Runtime] {end - start:.6f} seconds\n")
        return

    tokens = [x.decode() for x in data]

    # Parse input in a robust way:
    # 1) Try T testcases format
    # 2) If that fails, assume single testcase format: n + array
    tests, ok = _try_parse_as_t_tests(tokens)

    if not ok:
        # Single testcase expected:
        # n
        # a1 a2 ... an
        n = int(tokens[0])
        arr = list(map(int, tokens[1:1 + n]))
        tests = [arr]

    solver = Solution()

    # Time the algorithm (excluding parsing time for fair algorithm timing)
    start_time = time.perf_counter()

    outputs = []
    for arr in tests:
        result = solver.nextFreqGreater(arr)
        outputs.append(" ".join(map(str, result)))

    end_time = time.perf_counter()

    # Print results (each test case on a new line)
    print("\n".join(outputs))

    # Print runtime to stderr (doesn't pollute normal output)
    sys.stderr.write(f"[Runtime] {end_time - start_time:.6f} seconds\n")


if __name__ == "__main__":
    main()

"""
========================
Sample Input (single test)
========================
6
2 1 1 3 2 1

Output:
1 -1 -1 2 1 -1

========================
Sample Input (multiple tests)
========================
2
6
2 1 1 3 2 1
5
5 1 5 6 6

Output:
1 -1 -1 2 1 -1
-1 5 -1 -1 -1
"""
```

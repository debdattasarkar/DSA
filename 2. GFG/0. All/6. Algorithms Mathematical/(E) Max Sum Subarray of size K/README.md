# Max Sum Subarray of Size K

**Difficulty:** Easy
**Accuracy:** 49.6%
**Submissions:** 230K+
**Points:** 2

---

## Problem Statement

Given an array of integers **arr[]** and a number **k**, return the **maximum sum** of a **subarray of size k**.

> **Note:**
> A subarray is a **contiguous** part of any given array.

---

## Examples

### Example 1

**Input:**
`arr[] = [100, 200, 300, 400], k = 2`

**Output:**
`700`

**Explanation:**
`arr[2] + arr[3] = 300 + 400 = 700`, which is maximum.

---

### Example 2

**Input:**
`arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4`

**Output:**
`39`

**Explanation:**
`arr[1] + arr[2] + arr[3] + arr[4] = 4 + 2 + 10 + 23 = 39`, which is maximum.

---

### Example 3

**Input:**
`arr[] = [100, 200, 300, 400], k = 1`

**Output:**
`400`

**Explanation:**
`arr[3] = 400`, which is maximum.

---

## Constraints

* 1 ≤ `arr.size()` ≤ 10<sup>6</sup>
* 1 ≤ `arr[i]` ≤ 10<sup>6</sup>
* 1 ≤ `k` ≤ `arr.size()`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* OYO Rooms

---

## Topic Tags

* prefix-sum
* sliding-window
* Misc
* Algorithms

---

## Related Articles

* [Find Maximum Minimum Sum Subarray Size K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)

---

---

## 2) Text explanation (core idea)

We need the **maximum sum among all contiguous subarrays of length k**.

### Brute idea

For every starting index `i`, compute sum of `arr[i .. i+k-1]`.
That’s `O(n*k)` → too slow for large `n`.

### Optimized (most expected): Sliding Window

* First compute sum of the **first k elements** → this is the first window.
* Then slide the window by 1:

  * **remove** the element going out (`arr[i-k]`)
  * **add** the new element coming in (`arr[i]`)
* Track the maximum window sum seen.

This is **O(n)** because each element is added and removed once.

---

## Step-by-step Dry Run (Example 2)

`arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4`

### Window 0 (index 0..3)

sum = `1+4+2+10 = 17`
max = 17

Slide by 1 each time:

### Window 1 (1..4)

newSum = oldSum - arr[0] + arr[4] = `17 - 1 + 23 = 39`
max = 39

### Window 2 (2..5)

newSum = `39 - 4 + 3 = 38`
max = 39

### Window 3 (3..6)

newSum = `38 - 2 + 1 = 37`
max = 39

### Window 4 (4..7)

newSum = `37 - 10 + 0 = 27`
max = 39

### Window 5 (5..8)

newSum = `27 - 23 + 20 = 24`
max = 39

✅ Answer = **39**

---

## 3) Python codes (brute + expected interview optimized)

### A) Brute force (easy baseline)

**Time:** `O(n*k)`
**Space:** `O(1)`

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        # Edge case: if k == 0 (not possible by constraints, but safe)
        if k == 0:
            return 0

        max_sum = float("-inf")

        # Try every window start
        for start in range(0, n - k + 1):
            window_sum = 0
            # Sum k elements
            for idx in range(start, start + k):
                window_sum += arr[idx]
            max_sum = max(max_sum, window_sum)

        return max_sum
```

---

### B) Most expected: Sliding Window (Optimal)

**Time:** `O(n)`
**Space:** `O(1)`

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        # Compute sum of first window of size k
        # Time: O(k), Space: O(1)
        current_window_sum = 0
        for i in range(k):
            current_window_sum += arr[i]

        max_window_sum = current_window_sum

        # Slide window from index k to n-1
        # Each step: remove arr[i-k], add arr[i]
        # Time: O(n-k), Space: O(1)
        for right in range(k, n):
            element_entering = arr[right]
            element_leaving = arr[right - k]

            current_window_sum = current_window_sum - element_leaving + element_entering
            if current_window_sum > max_window_sum:
                max_window_sum = current_window_sum

        return max_window_sum
```

---

### C) Prefix Sum (also acceptable, but uses extra memory)

**Time:** `O(n)`
**Space:** `O(n)`
(Usually sliding window is preferred because it’s O(1) space.)

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        prefix = [0] * (n + 1)  # prefix[i] = sum(arr[0..i-1])
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        max_sum = float("-inf")
        for i in range(k, n + 1):
            window_sum = prefix[i] - prefix[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum
```

---

## 4) Interview memory + expected Q&A

### 5-line pseudo-code template (memorize)

```
sum = sum(arr[0:k]); ans = sum
for i from k to n-1:
    sum += arr[i] - arr[i-k]
    ans = max(ans, sum)
return ans
```

### Mnemonic

**“ADD right, DROP left”**
(or **“IN - OUT”**)

### 60-second recall script (what to say)

1. “Need max sum of fixed length k subarray.”
2. “Brute is O(n*k).”
3. “Use sliding window: first k sum, then slide.”
4. “Each move: subtract outgoing, add incoming.”
5. “Track max. O(n) time, O(1) space.”

---

## Expected interviewer questions & answers

**Q1. Why sliding window works here?**
A. Window size is fixed (k). Next window differs by only 2 elements (one leaves, one enters), so we update sum in O(1).

**Q2. Complexity?**
A. O(n) time, O(1) space.

**Q3. What if array contains negative numbers?**
A. Still works because we’re comparing sums of fixed-size windows; no special handling needed.

**Q4. What if k = 1?**
A. Then answer is max element; algorithm naturally returns it.

**Q5. What if k = n?**
A. Only one window; answer is sum of all elements.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Max revenue / sales in any k-day window**

   * “Find the best 7-day period” for sales, signups, ad clicks, etc. This is exactly max sum subarray of fixed size.

2. **Monitoring / anomaly detection (rolling window)**

   * Find the highest CPU usage / error count over any 5-minute window to detect spikes.

3. **Finance / trading**

   * Max total return/volume in a fixed-length window (e.g., best 10-day period by volume).

4. **Capacity planning**

   * Highest total requests in any k-minute window to estimate peak load.

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This program:

* Reads `arr` and `k`
* Computes max sum of subarray of size `k` using **sliding window (O(n), O(1))**
* Prints input + output + total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: array values space-separated (e.g., `1 4 2 10 23 3 1 0 20`)
* Line 2: k (e.g., `4`)

If no stdin, demo uses Example 2.

```python
import sys
import time


class Solution:
    def maxSubarraySum(self, arr, k):
        """
        Sliding Window (most expected).
        Time: O(n)
        Auxiliary Space: O(1)
        """
        n = len(arr)

        # Step 1: Sum of first window of size k
        # Time: O(k), Space: O(1)
        current_window_sum = 0
        for i in range(k):
            current_window_sum += arr[i]

        max_window_sum = current_window_sum

        # Step 2: Slide the window across the array
        # Each move: subtract outgoing element, add incoming element
        # Time: O(n-k), Space: O(1)
        for right in range(k, n):
            outgoing = arr[right - k]   # element leaving window
            incoming = arr[right]       # element entering window

            current_window_sum = current_window_sum - outgoing + incoming
            if current_window_sum > max_window_sum:
                max_window_sum = current_window_sum

        return max_window_sum


def main():
    # Measure full program runtime (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
        k = 4
    else:
        # ---------------- INPUT MODE ----------------
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        arr = list(map(int, lines[0].split()))
        k = int(lines[1])

    # Solve
    # Time: O(n), Aux Space: O(1)
    answer = solver.maxSubarraySum(arr, k)

    print("Input:")
    print("arr =", arr)
    print("k =", k)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

Input: `arr=[1,4,2,10,23,3,1,0,20], k=4`
Output: `39` (+ runtime)

---

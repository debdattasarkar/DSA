# Count Distinct Elements in Every Window

**Difficulty:** Medium
**Accuracy:** 41.83%
**Submissions:** 172K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an integer array **arr[]** and a number **k**, find the **count of distinct elements in every window of size k** in the array.

---

## Examples

### Example 1

**Input:**
`arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4`

**Output:**
`[3, 4, 4, 3]`

**Explanation:**

* First window `[1, 2, 1, 3]` → distinct count = 3
* Second window `[2, 1, 3, 4]` → distinct count = 4
* Third window `[1, 3, 4, 2]` → distinct count = 4
* Fourth window `[3, 4, 2, 3]` → distinct count = 3

---

### Example 2

**Input:**
`arr[] = [4, 1, 1], k = 2`

**Output:**
`[2, 1]`

**Explanation:**

* First window `[4, 1]` → distinct count = 2
* Second window `[1, 1]` → distinct count = 1

---

### Example 3

**Input:**
`arr[] = [1, 1, 1, 1], k = 3`

**Output:**
`[1, 1]`

**Explanation:**
Every window of size 3 contains only the element `1`, so the number of distinct elements in each window is `1`.

---

## Constraints

* 1 ≤ `k` ≤ `arr.size()` ≤ 10<sup>5</sup>
* 1 ≤ `arr[i]` ≤ 10<sup>5</sup>

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(k)`

---

## Company Tags

* Accolite
* Amazon
* Microsoft

---

## Topic Tags

* sliding-window
* Hash
* Data Structures
* Algorithms

---

## Related Articles

* [**Count Distinct Elements In Every Window Of Size K**](https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/)

---

---

## 2) Text explanation (core idea)

We must return, for **every window of size `k`**, how many **distinct** numbers appear in that window.

### Brute idea

For each window, put its elements into a `set` and take `len(set)`.

* Each window costs `O(k)`
* Total windows ≈ `n-k+1`
* Total time: `O(n*k)` (too slow for `n=1e5`)

### Optimized (most expected): Sliding window + frequency map

Maintain a hashmap `freq` storing counts of elements in the current window.

For each slide:

1. Add the incoming element → increment its frequency
2. Remove the outgoing element → decrement its frequency

   * If its frequency becomes 0 → delete it from map
3. The number of distinct elements = `len(freq)`

This makes each slide **O(1)** average, total **O(n)**.

---

## Step-by-step Dry Run (Example 1)

`arr = [1, 2, 1, 3, 4, 2, 3], k = 4`

### Window 0: [1, 2, 1, 3]

freq = {1:2, 2:1, 3:1} → distinct = 3
answer = [3]

Slide:

### Window 1: [2, 1, 3, 4]

Outgoing = 1, Incoming = 4

* dec freq[1]: 2 → 1 (still exists)
* inc freq[4]: 0 → 1
  freq = {1:1, 2:1, 3:1, 4:1} → distinct = 4
  answer = [3, 4]

### Window 2: [1, 3, 4, 2]

Outgoing = 2, Incoming = 2

* dec freq[2]: 1 → 0 → remove 2
* inc freq[2]: 0 → 1 (added back)
  freq still has 4 keys → distinct = 4
  answer = [3, 4, 4]

### Window 3: [3, 4, 2, 3]

Outgoing = 1, Incoming = 3

* dec freq[1]: 1 → 0 remove 1
* inc freq[3]: 1 → 2
  freq keys = {2,3,4} → distinct = 3
  answer = [3, 4, 4, 3]

✅ Final: `[3, 4, 4, 3]`

---

## 3) Python codes (brute + optimized)

### A) Brute force (easy baseline)

**Time:** `O(n*k)`
**Space:** `O(k)`

```python
class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = []

        # For each window, build a set and count distinct
        for start in range(0, n - k + 1):
            window_set = set()
            for idx in range(start, start + k):
                window_set.add(arr[idx])
            result.append(len(window_set))

        return result
```

---

### B) Most expected: Sliding window + hashmap frequency

**Time:** `O(n)`
**Space:** `O(k)`

```python
class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = []

        # Frequency map for current window
        frequency = {}

        # ---------- Step 1: Build frequency for first window ----------
        # Time: O(k), Space: O(k)
        for i in range(k):
            value = arr[i]
            frequency[value] = frequency.get(value, 0) + 1

        # Distinct count for first window
        result.append(len(frequency))

        # ---------- Step 2: Slide the window ----------
        # Each slide is O(1) average
        # Time: O(n-k), Space: O(k)
        for right in range(k, n):
            incoming = arr[right]         # new element entering window
            outgoing = arr[right - k]     # old element leaving window

            # Add incoming
            frequency[incoming] = frequency.get(incoming, 0) + 1

            # Remove outgoing
            frequency[outgoing] -= 1
            if frequency[outgoing] == 0:
                del frequency[outgoing]   # remove key to keep len(freq) correct

            # Distinct count in current window
            result.append(len(frequency))

        return result
```

---

### C) Slightly cleaner variant using `collections.defaultdict`

(Same complexity, sometimes interviewer likes clarity)

```python
from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = []
        frequency = defaultdict(int)

        for i in range(k):
            frequency[arr[i]] += 1
        result.append(len(frequency))

        for right in range(k, n):
            incoming = arr[right]
            outgoing = arr[right - k]

            frequency[incoming] += 1
            frequency[outgoing] -= 1
            if frequency[outgoing] == 0:
                del frequency[outgoing]

            result.append(len(frequency))

        return result
```

---

## 4) Interview memory + expected Q&A

### 5-line pseudo-code template (memorize)

```
freq = counts of first k elements
ans = [ size(freq) ]
for r in k..n-1:
    add arr[r] to freq
    remove arr[r-k] from freq (delete if 0)
    ans.append(size(freq))
return ans
```

### Mnemonic

**“COUNT in MAP → SLIDE (IN, OUT) → KEYS = DISTINCT”**
or simply: **“IN++, OUT--, ZERO? DELETE”**

### 60-second recall script

1. “Need distinct count for each fixed-size window.”
2. “Use hashmap frequency for current window.”
3. “Build first window counts.”
4. “Slide: add incoming, decrement outgoing, delete if count becomes 0.”
5. “Distinct = number of keys in hashmap. O(n) time, O(k) space.”

---

## Expected interviewer questions + answers

**Q1. Why do you delete keys when count becomes 0?**
A. Because distinct count is `len(freq)`. Keeping zero-count keys would inflate it.

**Q2. Complexity?**
A. Each element is added and removed once → `O(n)` time. Map holds at most k distinct values → `O(k)` space.

**Q3. Does it work with negative numbers too?**
A. Yes, hashmap keys can be any integers.

**Q4. What if k = 1?**
A. Each window has 1 element → all answers are 1 (or 1 per element). Code naturally handles it.

**Q5. What if all elements are same?**
A. freq size stays 1 in all windows.

If you want next: I can provide (5) real-world use cases + (6) full runnable timed program + sketch-note for “IN++, OUT--, delete zeros”.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Unique users in last K minutes (analytics / monitoring)**

   * Count distinct userIds in every rolling 5-minute window to track active users over time.

2. **Fraud / security burst detection**

   * Count distinct IPs / deviceIds in each window of requests; spikes in unique sources can indicate attacks.

3. **Streaming logs / observability**

   * Count distinct error codes, service names, or endpoints in a rolling window to spot unusual diversity (new failures).

4. **Inventory / recommendation signals**

   * In clickstream, distinct items viewed in last K actions can be a feature for personalization.

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This runnable program:

* Reads array `arr` and window size `k`
* Uses **sliding window + hashmap frequency** to compute distinct count for each window
* Prints input + output
* Prints total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: array values space-separated
* Line 2: k

If no stdin, demo uses:

* `arr = [1, 2, 1, 3, 4, 2, 3]`, `k = 4` → `[3, 4, 4, 3]`

```python
import sys
import time


class Solution:
    def countDistinct(self, arr, k):
        """
        Sliding window + frequency map.

        Time: O(n) average
        Auxiliary Space: O(k)
        """
        n = len(arr)
        result = []

        # Frequency map for current window
        frequency = {}

        # ---------- Step 1: Build frequency for first window ----------
        # Time: O(k), Space: O(k)
        for i in range(k):
            value = arr[i]
            frequency[value] = frequency.get(value, 0) + 1

        # Distinct count for first window = number of keys
        result.append(len(frequency))

        # ---------- Step 2: Slide the window across the array ----------
        # Time: O(n-k) average, Space: O(k)
        for right in range(k, n):
            incoming = arr[right]       # element entering the window
            outgoing = arr[right - k]   # element leaving the window

            # Add incoming element
            frequency[incoming] = frequency.get(incoming, 0) + 1

            # Remove outgoing element
            frequency[outgoing] -= 1
            if frequency[outgoing] == 0:
                del frequency[outgoing]  # important to keep distinct count correct

            # Record distinct count for this window
            result.append(len(frequency))

        return result


def main():
    # Measure total runtime for full program (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [1, 2, 1, 3, 4, 2, 3]
        k = 4
    else:
        # ---------------- INPUT MODE ----------------
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        arr = list(map(int, lines[0].split()))
        k = int(lines[1])

    # Solve
    # Time: O(n), Aux Space: O(k)
    answer = solver.countDistinct(arr, k)

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

Input: `arr=[1,2,1,3,4,2,3], k=4`
Output: `[3, 4, 4, 3]` (+ runtime)


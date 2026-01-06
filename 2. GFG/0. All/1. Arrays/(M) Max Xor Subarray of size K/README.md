# Max Xor Subarray of Size K

**Difficulty:** Medium
**Accuracy:** 62.79%
**Submissions:** 559+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

Given an array of integers **arr[]** and a number **k**, return the **maximum XOR** of a **subarray of size k**.

> **Note:**
> A subarray is a **contiguous** part of any given array.

---

## Examples

### Example 1

**Input:**
`arr[] = [2, 5, 8, 1, 1, 3], k = 3`

**Output:**
`15`

**Explanation:**
`arr[0] ^ arr[1] ^ arr[2] = 2 ^ 5 ^ 8 = 15`, which is maximum.

---

### Example 2

**Input:**
`arr[] = [1, 2, 4, 5, 6], k = 2`

**Output:**
`6`

**Explanation:**
`arr[1] ^ arr[2] = 2 ^ 4 = 6`, which is maximum.

---

## Constraints

* 1 ≤ `arr.size()` ≤ 10<sup>6</sup>
* 0 ≤ `arr[i]` ≤ 10<sup>6</sup>
* 1 ≤ `k` ≤ `arr.size()`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Bit Magic
* sliding-window
* Arrays

---

## Related Articles

* [**Find Maximum Xor Value Sub Array Size K**](https://www.geeksforgeeks.org/find-maximum-xor-value-sub-array-size-k/)

---

---

## 2) Text explanation (key idea)

We need the **maximum XOR** among all **contiguous subarrays of length `k`**.

### Brute force

For every start index `i`, compute:
`arr[i] ^ arr[i+1] ^ ... ^ arr[i+k-1]`
That costs `O(k)` per window → total `O(n*k)`.

### Optimized (most expected here): Sliding Window with XOR

XOR has a very useful property:

* `x ^ x = 0`
* `x ^ 0 = x`
* So if `window_xor = a ^ b ^ c`, then removing `a` is: `window_xor ^ a = b ^ c`

So when we slide by 1:

* remove outgoing element with `^= outgoing`
* add incoming element with `^= incoming`

That gives **O(1)** update per move ⇒ **O(n)** overall.

---

## Step-by-step Dry Run

### Example 1

`arr = [2, 5, 8, 1, 1, 3], k = 3`

**Window 0 (0..2):** `2 ^ 5 ^ 8`

* `2 ^ 5 = 7`
* `7 ^ 8 = 15`
  `current_xor = 15`, `max_xor = 15`

Slide:

**Window 1 (1..3):** remove `2`, add `1`

* `current_xor ^= 2` → `15 ^ 2 = 13`
* `current_xor ^= 1` → `13 ^ 1 = 12`
  `max_xor = max(15, 12) = 15`

**Window 2 (2..4):** remove `5`, add `1`

* `12 ^ 5 = 9`
* `9 ^ 1 = 8`
  `max_xor = 15`

**Window 3 (3..5):** remove `8`, add `3`

* `8 ^ 8 = 0`
* `0 ^ 3 = 3`
  `max_xor = 15`

✅ Answer = **15**

---

## 3) Python code (brute + optimized)

### A) Brute force (easy baseline)

**Time:** `O(n*k)`
**Space:** `O(1)`

```python
class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        max_xor = 0  # since arr[i] >= 0; if negatives existed, use -inf

        for start in range(0, n - k + 1):
            window_xor = 0
            for idx in range(start, start + k):
                window_xor ^= arr[idx]
            if window_xor > max_xor:
                max_xor = window_xor

        return max_xor
```

---

### B) Optimized (most expected): Sliding window XOR

**Time:** `O(n)`
**Space:** `O(1)`

```python
class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        # XOR of first window
        # Time: O(k), Space: O(1)
        current_window_xor = 0
        for i in range(k):
            current_window_xor ^= arr[i]

        max_window_xor = current_window_xor

        # Slide the window
        # Each move is O(1): remove outgoing, add incoming
        # Time: O(n-k), Space: O(1)
        for right in range(k, n):
            outgoing = arr[right - k]  # element leaving window
            incoming = arr[right]      # element entering window

            current_window_xor ^= outgoing
            current_window_xor ^= incoming

            if current_window_xor > max_window_xor:
                max_window_xor = current_window_xor

        return max_window_xor
```

---

## 4) Interview quick recall + expected Q&A

### 5-line pseudo-code template (memorize)

```
x = XOR(arr[0..k-1]); best = x
for r in k..n-1:
    x = x XOR arr[r-k] XOR arr[r]   // OUT then IN
    best = max(best, x)
return best
```

### Mnemonic

**“XOR: OUT ⊕ IN”**
(“remove outgoing with XOR, add incoming with XOR”)

### 60-second recall script

1. “Need max XOR of any subarray of fixed size k.”
2. “Compute XOR of first k elements.”
3. “Slide window: XOR out the leaving element, XOR in the entering element.”
4. “Track maximum XOR seen.”
5. “O(n) time, O(1) space.”

---

### Expected interviewer questions (with answers)

**Q1. Why can we remove an element from XOR by XOR-ing it again?**
A. Because `a ^ a = 0`, so `window_xor ^ outgoing` cancels that outgoing value.

**Q2. Does this work with duplicate values?**
A. Yes. We cancel exactly the element leaving the window (one occurrence) using the running XOR, not “all duplicates”.

**Q3. Complexity?**
A. `O(n)` time, `O(1)` auxiliary space.

**Q4. How is this different from max XOR subarray (any length)?**
A. Any-length max XOR needs prefix XOR + trie (bitwise). Here length is fixed → simple sliding window works.

---

---

## 5) Real-World Use Cases (few, interviewer-relatable)

1. **Network / Security (fixed-size packet fingerprinting)**

   * Compute XOR-based fingerprints over fixed-size chunks (k bytes/words) to quickly detect changes or anomalies in streaming packets.

2. **Hardware / Embedded (rolling parity / error checks)**

   * XOR is used for parity. A rolling XOR over a fixed window helps detect bit flips in a moving window of sensor samples.

3. **Streaming analytics (feature engineering)**

   * In telemetry streams, compute a rolling XOR feature over last `k` events to capture “toggle-like” patterns (useful in debugging state machines).

4. **Data dedup / fast chunk comparison**

   * Rolling XOR over fixed-length blocks can act as a quick “cheap hash” to find candidate matching blocks before deeper comparison.

---

## 6) Full Program (timed run + inline comments + sample I/O)

This program:

* Reads `arr` and `k`
* Computes **maximum XOR** among all subarrays of size `k` using **sliding window XOR**
* Prints input, output, and total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: array values (space-separated)
* Line 2: k

If no stdin, demo uses:
`arr = [2, 5, 8, 1, 1, 3], k = 3` → output `15`

```python
import sys
import time


class Solution:
    def maxSubarrayXOR(self, arr, k):
        """
        Sliding window XOR.
        Time: O(n)
        Auxiliary Space: O(1)
        """

        n = len(arr)

        # Step 1: XOR of first window of size k
        # Time: O(k), Space: O(1)
        current_window_xor = 0
        for i in range(k):
            current_window_xor ^= arr[i]

        max_window_xor = current_window_xor

        # Step 2: Slide the window
        # Each move is O(1): XOR out outgoing, XOR in incoming
        # Time: O(n-k), Space: O(1)
        for right in range(k, n):
            outgoing = arr[right - k]  # leaving element
            incoming = arr[right]      # entering element

            # Remove outgoing using XOR property: x ^ a removes a if it was included once
            current_window_xor ^= outgoing
            # Add incoming
            current_window_xor ^= incoming

            if current_window_xor > max_window_xor:
                max_window_xor = current_window_xor

        return max_window_xor


def main():
    # Measure total program runtime (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [2, 5, 8, 1, 1, 3]
        k = 3
    else:
        # ---------------- INPUT MODE ----------------
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        arr = list(map(int, lines[0].split()))
        k = int(lines[1])

    # Solve
    # Time: O(n), Aux Space: O(1)
    answer = solver.maxSubarrayXOR(arr, k)

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

Input: `arr=[2,5,8,1,1,3], k=3`
Output: `15` (+ runtime)

---

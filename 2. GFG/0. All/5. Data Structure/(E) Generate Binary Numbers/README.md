# Generate Binary Numbers 🧮

**Difficulty:** Easy
**Accuracy:** 67.48%
**Submissions:** 53K+
**Points:** 2

---

## Problem

Given a number `n`, generate all **binary numbers** whose decimal values are from **1 to n** (inclusive).

---

## Examples

### Example 1

**Input:** `n = 4`
**Output:** `["1", "10", "11", "100"]`
**Explanation:** Binary numbers from 1 to 4 are `1`, `10`, `11`, and `100`.

### Example 2

**Input:** `n = 6`
**Output:** `["1", "10", "11", "100", "101", "110"]`
**Explanation:** Binary numbers from 1 to 6 are `1`, `10`, `11`, `100`, `101`, and `110`.

---

## Constraints

* `1 ≤ n ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Amazon
* OYO Rooms

---

## Topic Tags

* Queue
* Data Structures
* Bit Magic

---

## Related Articles

* *Interesting Method Generate Binary Numbers 1 N*

---

---

Below is a complete interview-style write-up for **Generate Binary Numbers \[1…n]**.

---

## 2) Explanation (clear idea + dry run)

### Goal

Return a list of strings that are the binary representations of all integers from **1 to n**, in order.

### Two common ways

1. **Brute / direct conversion (simple and fine for interviews):**
   Loop `i = 1..n`, convert `i` to binary string (e.g., `bin(i)[2:]`) and push to result.

2. **Queue (BFS) generation (classic pattern, O(n) without repeated division):**
   Think of a binary tree of strings where each node’s children are `node + "0"` and `node + "1"`.
   Start with `"1"` in a queue; pop front, append it to the answer, then push its two children. Repeat `n` times. This produces binary numbers in increasing order.

Both are **O(n)** time and **O(n)** space (to store the output). The queue method is a favorite for this problem because it demonstrates mastery of BFS/queue patterns.

---

### Dry run (Queue method) for `n = 6`

* Start: `q = ["1"]`, ans = \[]

1. Pop `"1"` → ans = `["1"]`; push `"10"`, `"11"` → q = `["10","11"]`
2. Pop `"10"` → ans = `["1","10"]`; push `"100"`, `"101"` → q = `["11","100","101"]`
3. Pop `"11"` → ans = `["1","10","11"]`; push `"110"`, `"111"` → q = `["100","101","110","111"]`
4. Pop `"100"` → ans = `["1","10","11","100"]`; push `"1000"`, `"1001"` → q = `["101","110","111","1000","1001"]`
5. Pop `"101"` → ans = `["1","10","11","100","101"]`; push `"1010"`, `"1011"` → q = `["110","111","1000","1001","1010","1011"]`
6. Pop `"110"` → ans = `["1","10","11","100","101","110"]`; (stop after 6 items)

Output: `["1", "10", "11", "100", "101", "110"]`

---

## 3) Optimized Codes (two interview-friendly ways)

### A) Direct conversion (brute/easy)

```python
class Solution:
    def generateBinary(self, n):
        """
        Brute/easy approach: convert each i in [1..n] to binary.
        Time  : O(n) average (conversion is O(log i), but total is bounded by output size)
        Space : O(n) for the result list
        """
        res = []
        for i in range(1, n + 1):
            # bin(i) returns strings like '0b101', so strip the '0b' prefix
            res.append(bin(i)[2:])
        return res
```

### B) BFS with a queue (classic optimal pattern)

```python
from collections import deque

class Solution:
    def generateBinary(self, n):
        """
        Queue/BFS approach: generate strings in increasing order by expanding each node to x0, x1.
        Time  : O(n)   (we pop/push constant work per item)
        Space : O(n)   (queue + result)
        """
        if n <= 0:
            return []
        
        res = []
        q = deque()
        q.append("1")  # start from 1
        
        for _ in range(n):
            cur = q.popleft()     # the next binary number
            res.append(cur)
            q.append(cur + "0")   # generate next two numbers in sequence
            q.append(cur + "1")
        
        return res
```

> **Which to pick in an interview?**
> If the interviewer wants simplicity and speed: use **A**.
> If they hinted “queue/bit magic/without using built-ins” or want a data-structure pattern: show **B**.

---

## 4) Likely Interview Q\&A

**Q1. Why does the BFS queue produce numbers in increasing order?**
**A.** Starting with `"1"`, each pop is the smallest unreported binary string. Appending `"0"` and `"1"` keeps lexicographic growth aligned with numeric order for these specific prefixes, so the sequence matches 1, 2, 3, … in binary.

**Q2. What are the time and space complexities?**
**A.** Both methods are `O(n)` time overall (bounded by generating `n` strings; queue method does constant work per item). Space is `O(n)` for storing the output; the queue method also has `O(n)` auxiliary space.

**Q3. Any edge cases?**
**A.** `n = 1` → `["1"]`. `n <= 0` → return empty list. Very large `n` → ensure you don’t print or store unnecessarily huge intermediates beyond the required list.

**Q4. Why not generate via repeated division by 2 manually?**
**A.** You can; it’s similar to `bin(i)[2:]`. The queue method avoids repeated log-time conversions and showcases DS skills.

**Q5. Will leading zeros ever appear?**
**A.** No. The generation starts at `"1"` and only appends `"0"`/`"1"` to existing non-zero prefixes.

**Q6. Which approach is more memory efficient?**
**A.** Both store `n` strings in the result—so output dominates. The queue temporarily holds up to \~`O(n)` entries, similar order of growth as the result itself.

---

---

Here’s a **complete, runnable** Python program that:

* Implements **both approaches** (direct conversion and BFS/queue).
* Prints **inputs and outputs** (for small demo inputs).
* Uses `timeit` to measure **end-to-end runtime** for each approach.
* Includes **inline complexity notes** right where the work happens.

```python
#!/usr/bin/env python3
"""
Generate Binary Numbers from 1..n

Two implementations:
  1) Direct conversion using Python's bin()  — simple & fast in practice.
  2) BFS/Queue generation — classic interview pattern (no integer->binary conversion).

Time & Space Overview (both methods):
  - Time  : O(n) total work to produce n strings (queue does O(1) per produced item;
             direct conversion is amortized O(1) per item given small integer sizes
             in many interview settings, strictly it’s O(sum log i) but bounded by output size).
  - Space : O(n) to store the output list (dominant). Queue approach also uses O(n) queue space.
"""

from collections import deque
from timeit import default_timer as timer


class SolutionDirect:
    def generateBinary(self, n):
        """
        Direct conversion using bin(i)[2:].
        For i = 1..n, we do a single conversion and append to result.

        Time per loop iteration: O(1) amortized (strictly O(log i) for conversion),
        Space: O(1) auxiliary besides the result list (O(n) for the returned list).
        """
        res = []
        # O(n) iterations, each builds one string result
        for i in range(1, n + 1):
            # Convert integer i to binary string and strip '0b' prefix
            # Time: O(log i) for conversion, but dominated by output size in total
            b = bin(i)[2:]
            res.append(b)  # O(1) amortized append
        return res  # O(n) result size


class SolutionQueue:
    def generateBinary(self, n):
        """
        BFS/Queue generation:
          Start with "1". Repeatedly pop front (next binary), push 'x0' and 'x1'.
          Do this n times to get the first n binary numbers.

        Each iteration does:
          - one pop (O(1))
          - two appends (O(1) each)
          - one append to result (O(1))
        So total time: O(n). Space: O(n) (result + queue).
        """
        if n <= 0:
            return []
        res = []
        q = deque()
        q.append("1")  # O(1)

        # O(n) iterations
        for _ in range(n):
            x = q.popleft()   # O(1)
            res.append(x)     # O(1) amortized
            q.append(x + "0") # O(1) (string concat cost is proportional to len(x), but
                               # across all pushes it's bounded by output size we must produce anyway)
            q.append(x + "1") # O(1)
        return res  # O(n)


def demo_and_time(n_values):
    """
    Run both approaches for each n in n_values,
    print inputs/outputs (for small n), and measure runtime.
    """
    direct = SolutionDirect()
    queue_ = SolutionQueue()

    for n in n_values:
        print(f"\n=== n = {n} ===")

        # --- Direct method timing ---
        t0 = timer()
        out_direct = direct.generateBinary(n)
        t1 = timer()
        print("[Direct]  Output:", out_direct if n <= 10 else f"{len(out_direct)} items (first 10: {out_direct[:10]})")
        print(f"[Direct]  Time taken: {t1 - t0:.6f} seconds")

        # --- Queue/BFS method timing ---
        t2 = timer()
        out_queue = queue_.generateBinary(n)
        t3 = timer()
        print("[Queue ]  Output:", out_queue if n <= 10 else f"{len(out_queue)} items (first 10: {out_queue[:10]})")
        print(f"[Queue ]  Time taken: {t3 - t2:.6f} seconds")

        # Sanity check: both should match
        print("Match? ->", out_direct == out_queue)


if __name__ == "__main__":
    # Small demonstration inputs (printed fully)
    demo_and_time([4, 6])

    # Larger timing-only run (won't print the whole array)
    demo_and_time([10000])  # adjust size as you like
```

### Sample run (what you’ll see)

```
=== n = 4 ===
[Direct]  Output: ['1', '10', '11', '100']
[Direct]  Time taken: 0.0000xx seconds
[Queue ]  Output: ['1', '10', '11', '100']
[Queue ]  Time taken: 0.0000yy seconds
Match? -> True

=== n = 6 ===
[Direct]  Output: ['1', '10', '11', '100', '101', '110']
[Direct]  Time taken: 0.0000xx seconds
[Queue ]  Output: ['1', '10', '11', '100', '101', '110']
[Queue ]  Time taken: 0.0000yy seconds
Match? -> True

=== n = 10000 ===
[Direct]  Output: 10000 items (first 10: ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010'])
[Direct]  Time taken: 0.0xxx seconds
[Queue ]  Output: 10000 items (first 10: ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010'])
[Queue ]  Time taken: 0.0yyy seconds
Match? -> True
```

---

## 6) Real-World Use Cases (concise + important)

1. **Streaming ID generators / numbering labels**
   Generating compact identifiers (binary) up to a limit, or producing codes for testing parsers/encoders.

2. **Educational tooling**
   Teaching binary representations, BFS/queue behavior, or enumerating states in increasing order of magnitude.

3. **Bitmask iteration scaffolding**
   When building demos or unit tests that need binary masks from 1 to n (e.g., subsets in combinatorial problems).

4. **Low-level protocol/debug visualization**
   Displaying flags or bit-fields in human-readable binary when inspecting packets or hardware registers.


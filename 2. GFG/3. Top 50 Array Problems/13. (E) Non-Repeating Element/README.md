# Non-Repeating Element

**Difficulty:** Easy
**Accuracy:** 39.31%
**Submissions:** 134K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Find the **first non-repeating element** in a given array `arr` of integers.
If there is **no** non-repeating element, return **0**.

**Note:**

* The array consists only of **positive and negative integers** and **not zero**.

---

## Examples

### Example 1

**Input:** `arr = [-1, 2, -1, 3, 2]`
**Output:** `3`
**Explanation:** `-1` and `2` are repeating, whereas `3` occurs only once. Hence, the output is `3`.

### Example 2

**Input:** `arr = [1, 1, 1]`
**Output:** `0`
**Explanation:** There is no non-repeating element, so the answer is `0`.

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Constraints

* `1 ≤ arr.size ≤ 10^6`
* `-10^9 ≤ arr[i] ≤ 10^9`
* `arr[i] != 0`

---

## Company Tags

Snapdeal • Goldman Sachs • Adobe

---

## Topic Tags

Arrays • Hash • Data Structures

---

## Related Articles

* [Non Repeating Element](https://www.geeksforgeeks.org/non-repeating-element/)

---

---

Here’s an interview-ready breakdown for **Non-Repeating Element**.

---

## 2) Intuition + step-by-step dry run

We want the **first element that occurs exactly once** while preserving the original order.
A classic way is a **two-pass frequency count**:

1. **Pass 1:** Count occurrences of every number in a hash map (`dict` / `Counter`).
2. **Pass 2:** Scan the array in order and **return the first element whose count is 1**.
   If none exists, return **0** (the problem guarantees no zeros in the input, so `0` is a safe “not found” value).

### Dry run

`arr = [-1, 2, -1, 3, 2]`

* Count pass → `{-1: 2, 2: 2, 3: 1}`
* Order pass:

  * `-1` → count 2 (skip)
  * `2`  → count 2 (skip)
  * `-1` → 2 (skip)
  * `3`  → **1 → answer = 3**

`arr = [1, 1, 1]` → counts `{1: 3}` → no count==1 → return **0**.

---

## 3) Python solutions (brute & optimal) with interview-style comments

### A) Optimal: Two-pass hash map (expected in interviews)

```python
# User function Template for python3
from collections import Counter

class Solution:
    def firstNonRepeating(self, arr):
        """
        Two-pass frequency approach.
        Time  : O(n)    (one count pass + one order-preserving pass)
        Space : O(n)    (hash map for frequencies)
        """
        # 1) Count frequencies in O(n)
        freq = Counter(arr)

        # 2) First element with freq==1 in original order
        for x in arr:                 # O(n)
            if freq[x] == 1:
                return x

        # No non-repeating element
        return 0
```

### B) Also O(n): Single pass with queue (useful if the data were streaming)

```python
from collections import deque, defaultdict

class SolutionQueue:
    def firstNonRepeating(self, arr):
        """
        Maintain counts and a queue of 'candidates' in order.
        Time  : O(n) amortized
        Space : O(n)
        """
        cnt = defaultdict(int)
        q = deque()

        for x in arr:
            cnt[x] += 1
            q.append(x)               # push every element once
            # Pop from front while the front isn't unique
            while q and cnt[q[0]] > 1:
                q.popleft()

        return q[0] if q else 0
```

### C) Brute force: Check each element against all others (not recommended)

```python
class SolutionBrute:
    def firstNonRepeating(self, arr):
        """
        For each index i, check if arr[i] appears anywhere else.
        Time  : O(n^2)
        Space : O(1)
        """
        n = len(arr)
        for i in range(n):
            unique = True
            for j in range(n):
                if i != j and arr[i] == arr[j]:
                    unique = False
                    break
            if unique:
                return arr[i]
        return 0
```

---

## 4) Interviewer Q\&A

**Q1. Why not use a set?**
A set loses counts; we need to know which elements occur **exactly once** and also return the **first** such element in order. A `dict` (or `Counter`) + second pass preserves order and counts.

**Q2. What are the complexities?**

* Optimal (Counter + second pass): **O(n)** time, **O(n)** space.
* Brute force: **O(n²)** time, **O(1)** space (usually unacceptable for large `n`).

**Q3. Could we do O(1) extra space?**
Only if values belonged to a tight, known range (then a fixed-size frequency array might work). Here values are in `[-1e9, 1e9]`, so a hash map is appropriate.

**Q4. Why is returning `0` safe?**
The problem states **arr\[i] != 0**, so `0` can represent “no non-repeating element.”

**Q5. What edge cases matter?**

* `n = 1` → return that lone element.
* All repeating → return `0`.
* Negative numbers → handled naturally by the counter.
* Very large `n` (up to `1e6`) → prefer the **O(n)** hash map approach.

---

---

Done! I ran a **complete inline Python program** that:

* Implements three approaches:

  * **Optimal O(n) / O(n)** using `Counter` (expected solution).
  * **Queue-based O(n) / O(n)** (nice if this were a streaming feed).
  * **Brute O(n²) / O(1)** (for teaching/comparison on small inputs).
* Executes the **examples**, **edge cases**, a **cross-check** across all three methods, and a **large benchmark** (`n=200,000`) using `timeit`.
* Prints **inputs, outputs, and timings**, plus the **total main runtime** at the end.

```python

# Re-run to display outputs after the reset
from collections import Counter, defaultdict, deque
from typing import List
import random, timeit

class Solution:
    def firstNonRepeating(self, arr: List[int]) -> int:
        freq = Counter(arr)
        for x in arr:
            if freq[x] == 1:
                return x
        return 0

class SolutionQueue:
    def firstNonRepeating(self, arr: List[int]) -> int:
        cnt = defaultdict(int)
        q = deque()
        for x in arr:
            cnt[x] += 1
            q.append(x)
            while q and cnt[q[0]] > 1:
                q.popleft()
        return q[0] if q else 0

class SolutionBrute:
    def firstNonRepeating(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            unique = True
            for j in range(n):
                if i != j and arr[i] == arr[j]:
                    unique = False
                    break
            if unique:
                return arr[i]
        return 0

def main():
    opt = Solution()
    que = SolutionQueue()
    bru = SolutionBrute()

    print("=== Non-Repeating Element — Demo & Timing ===")

    examples = [
        ([-1, 2, -1, 3, 2], 3),
        ([1, 1, 1], 0),
        ([5], 5),
        ([-5, -4, -3, -4, -5], -3),
        ([10, -7, 10, -7, 20, 30, 30], 20),
    ]
    for arr, exp in examples:
        for name, solver in (("Optimal", opt), ("Queue", que)):
            t0 = timeit.default_timer()
            out = solver.firstNonRepeating(arr)
            t1 = timeit.default_timer()
            print(f"{name:<7} | Input: {arr} -> Output: {out} (exp {exp})  time={(t1 - t0):.6f}s")
        if len(arr) <= 50:
            t0 = timeit.default_timer()
            out = bru.firstNonRepeating(arr)
            t1 = timeit.default_timer()
            print(f"{'Brute':<7} | Input: {arr} -> Output: {out} (exp {exp})  time={(t1 - t0):.6f}s")
        print("-" * 90)

    random.seed(7)
    small = [random.choice([-5, -3, -1, 1, 2, 3, 4, 6]) for _ in range(30)]
    g1 = opt.firstNonRepeating(small)
    g2 = que.firstNonRepeating(small)
    g3 = bru.firstNonRepeating(small)
    print("Cross-check on random small:")
    print("  arr =", small)
    print(f"  Optimal={g1}, Queue={g2}, Brute={g3}")

    n = 200_000
    big = [random.randint(-10**6, 10**6) or 1 for _ in range(n)]
    big[-100] = 987654321
    t0 = timeit.default_timer()
    res_opt = opt.firstNonRepeating(big)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    res_que = que.firstNonRepeating(big)
    t3 = timeit.default_timer()
    print("\nLarge test n=200000:")
    print(f"  Optimal -> {res_opt}  time={(t1 - t0):.6f}s")
    print(f"  Queue   -> {res_que}  time={(t3 - t2):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (top practical scenarios)

* **Fraud or anomaly detection (first unique signal):** In transaction streams or logs, quickly find the **first non-repeating id/event** to flag rare anomalies while most others repeat.
* **Customer support / ticket triage:** Identify the **first unique issue code** in a batch of reports to surface a potentially new problem that’s not yet recurring.
* **Telemetry & observability:** Among repeating status codes or metrics, grab the **earliest unique code** that might represent an edge-case failure mode.
* **Deduped notifications:** From alerts or push messages, find the **first unique message type** to decide immediate notification vs. batch processing.

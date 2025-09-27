# Minimum K Consecutive Bit Flips

**Difficulty:** Hard
**Accuracy:** 70.62%
**Submissions:** 5K+
**Points:** 8

---

You are given a binary array `arr[]` (containing only **0's and 1's**) and an integer `k`. In one operation, you can select a contiguous subarray of length `k` and **flip all its bits** (i.e., change every `0` to `1` and every `1` to `0`).

Your task is to find the **minimum** number of such operations required to make the entire array consist of only **1's**. If it is not possible, return **-1**.

---

## Examples

### Example 1

**Input:** `arr = [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], k = 2`
**Output:** `4`
**Explanation:** 4 operations are required to convert all `0`'s to `1`'s.
Select subarray `[2, 3]` and flip all bits resulting array will be `[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]`
Select subarray `[4, 5]` and flip all bits resulting array will be `[1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]`
Select subarray `[5, 6]` and flip all bits resulting array will be `[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]`
Select subarray `[6, 7]` and flip all bits resulting array will be `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`

### Example 2

**Input:** `arr = [0, 0, 1, 1, 1, 0, 0], k = 3`
**Output:** `-1`
**Explanation:** It is not possible to convert all elements to `1`'s by performing any number of operations.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `1 ≤ k ≤ arr.size()`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(k)`

---

## Company Tags

Bloomberg • Amazon • Facebook • Microsoft • Google

---

## Topic Tags

prefix-sum • Bit Magic • sliding-window • Arrays • Queue

---

---

# Minimum K Consecutive Bit Flips — Explanation + Dry Run + Python Solutions

## 2) Intuition & Step-by-Step Dry Run

**Problem recap.**
Given a binary array `arr` and an integer `k`, one operation flips a *contiguous* block of length `k`. Find the minimum operations to make the whole array all 1’s, or return `-1` if impossible.

### Key idea (greedy + sliding window parity)

Scan left→right. At index `i`, all flips that *started* in `[i-k+1, i-1]` still affect `i`. Let `cur` be the parity (0/1) meaning how many active flips mod 2 are currently affecting the position.

* The **effective bit** at `i` is `arr[i] XOR cur`.
* If it’s `0`, we **must** start a flip at `i` (greedy). Flipping later won’t fix `arr[i]` because flips are length `k` and can’t reach back.
* When a flip that started at `i` reaches `i+k`, it *expires* and we toggle `cur` back.

We can track expirations either with:

* a small difference array `hint` where `hint[j]=1` means a flip started at `j` (then at `i` we do `cur ^= hint[i-k]`), or
* a deque of “end indices” to drop when they expire.

If at some `i` we need a flip but `i+k > n`, it’s impossible.

### Dry run (optimized “difference array” way)

Example: `arr = [1,1,0,0,0,1,1,0,1,1,1]`, `k = 2`

Variables:
`cur = 0` (current parity), `hint = [0]*n`, `ans = 0`

| i  | i>=k? expire toggle | arr[i] | effective = arr[i] ^ cur | action                | ans | cur | mark |
| -- | ------------------- | ------ | ------------------------ | --------------------- | --- | --- | ---- |
| 0  | —                   | 1      | 1                        | none                  | 0   | 0   | —    |
| 1  | —                   | 1      | 1                        | none                  | 0   | 0   | —    |
| 2  | toggle ^= hint[0]=0 | 0      | 0                        | flip at 2 → hint[2]=1 | 1   | 1   | [2]  |
| 3  | toggle ^= hint[1]=0 | 0      | 1                        | none                  | 1   | 1   | —    |
| 4  | toggle ^= hint[2]=1 | 0      | 0                        | flip at 4 → hint[4]=1 | 2   | 1   | [4]  |
| 5  | toggle ^= hint[3]=0 | 1      | 0                        | flip at 5 → hint[5]=1 | 3   | 0   | [5]  |
| 6  | toggle ^= hint[4]=1 | 1      | 0                        | flip at 6 → hint[6]=1 | 4   | 1   | [6]  |
| 7  | toggle ^= hint[5]=1 | 0      | 1                        | none                  | 4   | 0   | —    |
| 8  | toggle ^= hint[6]=1 | 1      | 1                        | none                  | 4   | 0   | —    |
| 9  | toggle ^= hint[7]=0 | 1      | 1                        | none                  | 4   | 0   | —    |
| 10 | toggle ^= hint[8]=0 | 1      | 1                        | none                  | 4   | 0   | —    |

All ones achieved with **4** flips → answer `4`.

Impossibility example: `arr = [0,0,1,1,1,0,0]`, `k=3`
You’ll eventually reach `i=6` needing a flip, but `6+3>7` → **-1**.

---

## 3) Python solutions (with interview-style inline comments)

### A) Brute force (O(n·k)) — simple but slow

```python
class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flips = 0

        # Greedy: when we see a 0 at i, flip the next k bits
        for i in range(n - k + 1):
            if arr[i] == 0:
                # Perform the flip on the window [i, i+k)
                for j in range(i, i + k):
                    arr[j] ^= 1  # toggle 0<->1
                flips += 1

        # After processing possible starting positions,
        # tail must already be 1's, else impossible.
        for i in range(n - k + 1, n):
            if arr[i] == 0:
                return -1

        return flips
```

* **Why it works:** same greedy rationale, but we literally mutate each window.
* **Complexity:** `O(n·k)` time, `O(1)` extra space.

---

### B) Optimized — Difference array / flip parity (O(n), O(n) space)

```python
from typing import List

class Solution:
    def kBitFlips(self, arr: List[int], k: int) -> int:
        n = len(arr)
        hint = [0] * n      # hint[i] == 1 → a flip starts at i
        cur = 0             # parity of active flips affecting current index
        ans = 0

        for i in range(n):
            # Remove effect of a flip that started at i-k (if any)
            if i >= k:
                cur ^= hint[i - k]

            # Effective bit after cur flips
            effective = arr[i] ^ cur

            if effective == 0:           # need to flip starting here
                if i + k > n:
                    return -1            # window would overflow → impossible
                ans += 1
                cur ^= 1                 # starting a new flip toggles parity
                hint[i] = 1              # remember: this flip will expire at i+k

        return ans
```

* **Complexity:** `O(n)` time, `O(n)` space.
* **Pattern to mention in interviews:** “difference array / imos method for range toggles,” maintaining a running parity of active windows.

---

### C) Optimized — Deque of flip expirations (O(n), O(k) space)

```python
from collections import deque
from typing import List

class Solution:
    def kBitFlips(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ends = deque()  # stores indices where an active flip expires (i+k)
        ans = 0

        for i in range(n):
            # Drop expired flips
            while ends and ends[0] == i:
                ends.popleft()

            # Number of active flips is len(ends); parity = len(ends) % 2
            parity = (len(ends) & 1)

            # Effective bit at i after all active flips
            effective = arr[i] ^ parity

            if effective == 0:                 # need to start a flip here
                if i + k > n:
                    return -1
                ans += 1
                ends.append(i + k)             # this flip expires at i+k

        return ans
```

* **Complexity:** `O(n)` time, `O(k)` space (only flips within the current window range are stored).
* **Talking point:** same parity logic, just track expirations directly.

---

## 4) Interview-style Q&A

**Q1. Why is the greedy choice (“flip at the first index where the bit is 0”) optimal?**
**A.** At index `i`, only flips starting at `i` (or earlier) can affect it. If the effective bit at `i` is `0`, any plan that doesn’t start a flip at `i` cannot fix `i` later (windows can’t reach back). Thus starting a flip at `i` is *forced*, making the strategy optimal.

**Q2. How do you detect “impossible”?**
**A.** When you encounter `i` with effective bit `0` but `i + k > n`. The needed window would exceed the array bounds, so return `-1`.

**Q3. What’s the time and space complexity of your optimized solution?**
**A.** `O(n)` time. With a difference array, `O(n)` space; with a deque of expirations, `O(k)` auxiliary space.

**Q4. Can you do it in `O(1)` extra space?**
**A.** Yes, by *encoding* flip starts directly inside `arr`. A common trick: treat `arr[i] >= 2` as “a flip started here”. While scanning, if `i >= k` and `arr[i-k] >= 2`, toggle parity and subtract `2` from `arr[i-k]`. When starting a flip at `i`, add `2` to `arr[i]`. This avoids extra arrays but mutates `arr`.

**Q5. What edge cases do you handle?**
**A.**

* `k == 1`: answer is number of zeroes.
* `k == n`: either 0 flips (already all ones) or 1 flip if not all ones; otherwise impossible? Actually when not all ones, exactly 1 flip may or may not work depending on parity; with a single window covering all elements, flipping toggles all bits once—so it works iff after one flip all ones (i.e., all zeros initially).
* Already all ones: return 0.
* Trailing region shorter than `k` with a needed flip → `-1`.

**Q6. Why use parity instead of applying flips literally?**
**A.** Literal flips would cost `O(k)` per operation. Because flipping is a toggle, we only need to know **how many times** each position is flipped modulo 2. Sliding a parity over the array collapses all range operations to `O(1)` amortized per index.

**Q7. What is the role of the `hint` array?**
**A.** It marks the **start** of flips. When the scan reaches `i >= k`, we XOR `cur` with `hint[i-k]` to cancel the effect of the flip that started at `i-k` (it expires).

**Q8. Why does the deque version work?**
**A.** Each flip adds one active effect lasting for exactly `k` positions. Keeping their *end indices* in a queue lets us pop them when they expire and compute parity as `len(queue) % 2`.

**Q9. Can this be parallelized or processed from right to left?**
**A.** Yes, the same greedy works right→left by flipping at the *last* index where the effective bit is 0 and checking `i-k+1 >= 0`. Parallelization is tricky because decisions are sequentially dependent.

**Q10. How would you prove correctness formally?**
**A.** Exchange argument / cut-and-paste: any optimal solution can be transformed to one that flips at every earliest “bad” index without increasing the number of flips. Therefore, the greedy is optimal.

---

---

Here’s the **full runnable program** with **inline time/space complexity notes**, plus **timings** using `timeit`. I ran it just now—see the console right above for printed outputs and best run-times for each approach.

If you want a single drop-in class for interviews, use the “Optimized-Diff” version shown again at the end.

---

## What you just ran

* Three implementations that all match the required interface logic:

  * **Brute** `O(n*k)` time, `O(1)` extra space.
  * **Optimized (difference array / parity)** `O(n)` time, `O(n)` space.
  * **Optimized (deque expirations)** `O(n)` time, `O(k)` space.
* Inline comments annotate **time & space** for the important steps.
* `timeit` benchmarks each version for a few representative tests and prints:

  * Inputs
  * Returned result vs expected
  * Best timing over a few repeats

---

## Canonical interview class (Optimized-Diff)

If the interviewer asks for the standard signature, this is the one to present:

```python
from typing import List

class Solution:
    def kBitFlips(self, arr: List[int], k: int) -> int:
        """
        Greedy + difference-array (parity) technique.
        Time:  O(n)
        Space: O(n) for the hint array
        """
        n = len(arr)                 # O(1)
        hint = [0] * n               # O(n) space
        cur = 0                      # current flip parity affecting index i
        ans = 0

        # Single left->right scan: O(n)
        for i in range(n):
            # Expire the flip that started at i-k (if any): O(1)
            if i >= k:
                cur ^= hint[i - k]   # toggle parity when a prior flip ends

            # Effective bit after 'cur' flips: O(1)
            if (arr[i] ^ cur) == 0:  # need to flip starting here
                if i + k > n:        # window would overflow: impossible
                    return -1
                ans += 1
                cur ^= 1             # new flip toggles current parity
                hint[i] = 1          # mark flip start (it will expire at i+k)

        return ans
```

> The exact same logic is in the full program you ran; this snippet is just the neat, interview-ready version.

---

## What the timings show

* On the sample and additional tests, all three methods agree on outputs.
* The **optimized methods** run in **linear time** and are essentially identical in speed for typical Python inputs.
* The brute method is fine for small arrays but degrades to `O(n*k)`.

---

## Real-World Use Cases (a few that matter)

1. **Windowed toggles in streaming systems:**
   Applying or removing binary feature flags (on/off) over sliding windows—for instance, *muting/unmuting* a range of log lines or signals with minimal per-step cost using parity, not literal toggles.

2. **Image/video processing with local bit masks:**
   Quickly toggling binary masks over moving `k×1` (or generalized) windows—e.g., enabling/disabling detection regions efficiently while scanning frames.

3. **Network security and access control:**
   Rolling activation windows for firewall rules or access flags: track how many rules currently flip a bit (allow/deny) at a given index/time using mod-2 parity instead of rewriting the entire segment each time.
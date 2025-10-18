# Minimum Jumps

**Difficulty:** Medium
**Accuracy:** 11.91%
**Submissions:** 989K+
**Points:** 4

---

## Problem Statement

You are given an array `arr[]` of non-negative numbers. Each number tells you the **maximum number of steps** you can jump forward from that position.

For example:

* If `arr[i] = 3`, you can jump to index `i + 1`, `i + 2`, or `i + 3` from position `i`.
* If `arr[i] = 0`, you **cannot jump forward** from that position.

Your task is to find the **minimum number of jumps** needed to move from the **first position** in the array to the **last** position.

**Note:** Return `-1` if you can't reach the end of the array.

---

## Examples

### Example 1

**Input:** `arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]`
**Output:** `3`
**Explanation:** First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last.

### Example 2

**Input:** `arr = [1, 4, 3, 2, 6, 7]`
**Output:** `2`
**Explanation:** First we jump from the 1st to 2nd element and then jump to the last element.

### Example 3

**Input:** `arr = [0, 10, 20]`
**Output:** `-1`
**Explanation:** We cannot go anywhere from the 1st element.

---

## Constraints

* `2 ≤ arr.size() ≤ 10^4`
* `0 ≤ arr[i] ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* `Moonfrog Labs` • `Flipkart` • `Amazon` • `Microsoft` • `Housing.com` • `Walmart` • `Adobe` • `Google`

---

## Topic Tags

* `Arrays` • `Greedy` • `BFS-like`


---

## Related Articles

* [Minimum Jumps problem write-ups and editorials](https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/)

---

---

Here’s an interview-ready guide for **Minimum Jumps** — intuition, a clean dry-run, and multiple Python solutions.

---

## 2) Intuition + step-by-step dry run

### Problem restated

`arr[i]` tells the **farthest** you can jump forward from index `i`. Find the **minimum number of jumps** to go from index `0` to index `n-1`. If impossible, return `-1`.

### Greedy (“ladder & stairs”) idea — O(n)

Think of:

* **ladder** = the farthest index we can reach using the current number of jumps we’ve decided to take (the best future reach so far).
* **stairs** = how many indices we can still move **within the current jump** before we must take another jump.

Procedure:

1. Start at `i=0`. If `n==1` → already at end: `0` jumps. If `arr[0]==0` → can’t move: `-1`.
2. Initialize:

   * `jumps = 1` (you need at least one jump to move past index 0 when `n>1`)
   * `ladder = arr[0]` (current best reach)
   * `stairs = arr[0]` (steps left inside this jump)
3. For each `i` from `1` to `n-1`:

   * If `i == n-1`, return `jumps` (we just reached the end).
   * Update `ladder = max(ladder, i + arr[i])` (best future reach).
   * Consume a stair: `stairs -= 1`.
   * If `stairs == 0`, we must take a new jump: `jumps += 1`, and:

     * If `i >= ladder`, we’re stuck → `-1`.
     * Else reset `stairs = ladder - i` (new window length).

Why it’s optimal: Each time `stairs` runs out, we commit one jump and expand our window to the **farthest** position reachable within all indices we’ve seen — exactly like BFS levels on a line.

### Dry run (example 1)

`arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]`

* Init: `jumps=1`, `ladder=1`, `stairs=1`
* `i=1`: `ladder=max(1, 1+3=4)=4`, `stairs=0` ⇒ take jump: `jumps=2`, `stairs=ladder-i=4-1=3`
* `i=2`: `ladder=max(4, 2+5=7)=7`, `stairs=2`
* `i=3`: `ladder=max(7, 3+8=11)=11`, `stairs=1`
* `i=4`: `ladder=max(11, 4+9=13)=13`, `stairs=0` ⇒ take jump: `jumps=3`, `stairs=ladder-i=13-4=9`
* … we’ll hit `i = n-1` inside this third jump ⇒ **answer = 3**.

### Quick edge cases

* `[1,4,3,2,6,7]` → 2 jumps (`0->1->5`)
* `[0,10,20]` → `-1` (can’t move from start)

---

## 3) Python solutions

### A) Greedy O(n) — “ladder & stairs” (most expected)

```python
class Solution:
    def minJumps(self, arr):
        """
        Greedy window expansion (ladder & stairs).
        Time : O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return 0                    # already at the end
        if arr[0] == 0:
            return -1                   # cannot move anywhere

        # We will reach somewhere within arr[0] with our first jump.
        jumps  = 1
        ladder = arr[0]                 # farthest index we can reach so far
        stairs = arr[0]                 # steps we can still take before next jump

        for i in range(1, n):
            if i == n - 1:
                return jumps            # reached the last index

            # Keep improving the farthest we can reach.
            ladder = max(ladder, i + arr[i])

            # Use one step to move from i to i+1 within current jump window.
            stairs -= 1

            # If no more steps left in current window, we must jump.
            if stairs == 0:
                jumps += 1
                # If our best reach is not beyond current i, we are stuck.
                if i >= ladder:
                    return -1
                # Reset the stairs to how many steps are in the new window.
                stairs = ladder - i

        # Should have returned inside loop; if we fall through something's off.
        return -1
```

### B) DP (brute/easy to reason) — O(n²)

For each `i`, compute the minimum jumps to reach `i` by checking all `j < i` with `j + arr[j] >= i`.

```python
class Solution:
    def minJumps(self, arr):
        """
        Dynamic Programming (brute force).
        dp[i] = min jumps to reach i
        Time : O(n^2)
        Space: O(n)
        """
        n = len(arr)
        INF = 10**18
        dp = [INF] * n
        dp[0] = 0

        for i in range(1, n):              # O(n)
            for j in range(i):             # O(n)
                if j + arr[j] >= i and dp[j] != INF:
                    dp[i] = min(dp[i], dp[j] + 1)
        return -1 if dp[-1] == INF else dp[-1]
```

### C) BFS-level style (same complexity as greedy, different wording)

Treat each “window” `[0..currEnd]`, `[currEnd+1..nextEnd]`, … as a BFS level.

```python
class Solution:
    def minJumps(self, arr):
        """
        BFS windowing (levels).
        Time : O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1: return 0
        if arr[0] == 0: return -1

        jumps, currEnd, nextEnd = 0, 0, 0
        for i in range(n - 1):                # we don't need to step on last index explicitly
            nextEnd = max(nextEnd, i + arr[i])
            if i == currEnd:                  # end of current window -> take a jump
                jumps += 1
                if currEnd == nextEnd:        # stuck
                    return -1
                currEnd = nextEnd
        return jumps
```

> Solutions **A** and **C** are the same algorithmic idea dressed differently. In interviews, **A** is the most common presentation.

---

## 4) Interviewer Q\&A

**Q1. Why does the greedy window approach give the minimum jumps?**
We expand a **reachable window** to the farthest index we can reach with the current number of jumps. Once we’ve consumed all “stairs” inside the window, we **must** take one more jump to continue. Choosing the farthest `ladder` at every step ensures the fewest window boundaries → the fewest jumps. This is equivalent to BFS levels on a line.

**Q2. What are the time and space complexities?**
Greedy/BFS: **O(n)** time, **O(1)** extra space. DP brute: **O(n²)** time, **O(n)** space.

**Q3. What edge cases should I check?**

* `n <= 1` → `0`.
* `arr[0] == 0` with `n > 1` → `-1`.
* Arrays with long zeros in the middle (ensure the “stuck” check is present).
* Already at or near the end.

**Q4. Can we reconstruct the actual jump path?**
Yes. While running the greedy, keep parent pointers for the index that set the newest `ladder`. Or run a BFS that stores predecessors. This is extra bookkeeping; not required for just the count.

**Q5. Is there any case where DP is preferred over greedy?**
For this specific problem, greedy is standard and optimal. DP is useful as a teaching or fallback solution but isn’t necessary in production.

**Q6. How is this related to “Jump Game I/II” from LeetCode?**
This is equivalent to **Jump Game II** (minimum jumps). The greedy solution is the canonical approach there too.

---

---

Done! You’ve got:

* A **complete, runnable Python program** (printed above) implementing:

  * **Greedy O(n)** (ladder & stairs) solution with clear, inline complexity notes.
  * **DP O(n²)** reference for validation/learning.
  * Examples, edge cases, a correctness cross-check (greedy vs DP), and a **large benchmark** using `timeit`.

```python

# Re-run to display outputs after the reset
from typing import List
import random, timeit

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        jumps  = 1
        ladder = arr[0]
        stairs = arr[0]
        for i in range(1, n):
            if i == n - 1:
                return jumps
            if i + arr[i] > ladder:
                ladder = i + arr[i]
            stairs -= 1
            if stairs == 0:
                jumps += 1
                if i >= ladder:
                    return -1
                stairs = ladder - i
        return -1

    def minJumps_dp(self, arr: List[int]) -> int:
        n = len(arr)
        INF = 10**18
        dp = [INF] * n
        dp[0] = 0
        for i in range(1, n):
            best = INF
            for j in range(i):
                if j + arr[j] >= i and dp[j] + 1 < best:
                    best = dp[j] + 1
            dp[i] = best
        return -1 if dp[-1] >= INF else dp[-1]

def main():
    sol = Solution()
    print("=== Minimum Jumps — Demo & Timing ===")

    examples = [
        ([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 3),
        ([1, 4, 3, 2, 6, 7], 2),
        ([0, 10, 20], -1),
    ]
    for arr, exp in examples:
        t0 = timeit.default_timer()
        out = sol.minJumps(arr)
        t1 = timeit.default_timer()
        print(f"\nInput: {arr}\nGreedy Output: {out}  (expected {exp})   time={(t1 - t0):.6f}s")

    edges = [
        ([1], 0),
        ([2, 0, 0], 1),
        ([1, 0, 1, 0], -1),
    ]
    print("\nEdge cases:")
    for arr, exp in edges:
        t0 = timeit.default_timer()
        out = sol.minJumps(arr)
        t1 = timeit.default_timer()
        print(f"  {arr} -> {out} (exp {exp})   time={(t1 - t0):.6f}s")

    random.seed(7)
    small = [random.randint(0, 5) for _ in range(20)]
    t0 = timeit.default_timer()
    g = sol.minJumps(small)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    d = sol.minJumps_dp(small)
    t3 = timeit.default_timer()
    print("\nCross-check on small random:")
    print(f"  arr={small}\n  greedy={g} (time={(t1 - t0):.6f}s), dp={d} (time={(t3 - t2):.6f}s)")

    n = 200_000
    big = [random.randint(0, 10) for _ in range(n)]
    for i in range(0, n, 10000):
        big[i] = 20
    t0 = timeit.default_timer()
    res = sol.minJumps(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: greedy result={res}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```
---

## 6) Real-World Use Cases (why this pattern matters)

* **Network hop optimization:** Minimizing the number of relay hops in a linear topology when each node’s range (arr\[i]) defines how far it can forward.
* **Battery-constrained pathing:** A robot with limited per-stop range trying to reach a target with the fewest recharges, where each location’s charge lets it travel up to `arr[i]` steps ahead.
* **Video buffering / prefetching windows:** Moving across a media timeline where each segment prefetch allows playback to advance up to `arr[i]` seconds ahead; minimize the number of buffering stops.
* **Project schedule leapfrogging:** Tasks that unlock a window of subsequent tasks up to `arr[i]` positions ahead; minimize the number of “milestone” transitions.
* **Wireless AP handoffs along a corridor:** Each access point provides coverage up to `arr[i]` doors ahead; minimize the number of handoffs to reach the end.

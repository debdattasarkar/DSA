# Array Partition

**Difficulty:** Hard
**Accuracy:** 47.48%
**Submissions:** 8K+
**Points:** 8
**Average Time:** 30m

---

Given an array of **N** integers, you have to find if it is possible to partition the array with following rules:

* Each element should belong to exactly one partition.
* Each partition should have atleast **K** elements.
* Absolute difference between any pair of elements in the same partition should not exceed **M**.

---

## Example 1

**Input:**

```
N = 5
K = 2
M = 3
A[] = {8, 3, 9, 1, 2}
```

**Output:**

```
YES
```

**Explanation:**
We can partition the array into two partitions: `{8, 9}` and `{3, 1, 2}` such that all rules are satisfied.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`partitionArray()`** which takes the number of elements **N**, integer **K**, integer **M** and array **A[]** as input parameters and returns **true** if we can partition the array such that all rules are satisfied, else returns **false**.

---

## Expected Time Complexity

* `O(N * Log(N))`

## Expected Auxiliary Space

* `O(N)`

---

## Constraints

* `1 ≤ N ≤ 2*10^5`
* `1 ≤ K ≤ N`
* `1 ≤ M ≤ 10^9`
* `1 ≤ A[i] ≤ 10^9`

---

## Topic Tags

Dynamic Programming • Segment-Tree • Algorithms • Advanced Data Structure

---

## Related Articles

* Partitions In Arrays With At Least K Size And M Difference Rules

---

---

awesome — let’s make **Array Partition** (GFG) crisp and interview-ready.

---

# 2) Problem explanation + step-by-step dry run

**Rules**

* Partition the array into disjoint groups.
* Every group has **at least K** elements.
* Inside any group, **max − min ≤ M** (equivalently, any pair’s abs diff ≤ M).

Key trick: the constraint depends only on **min & max** of a group.
So after **sorting** the array, any valid group must be a **contiguous block** in the sorted order.
(If you take elements from two separated places in sorted order, their min/max gap only grows.)

## DP idea (most expected)

1. Sort `a = sorted(arr)`.

2. Let `dp[i]` = *is it possible to partition the first `i` sorted elements?* (`i` from `0..N`)
   Base: `dp[0] = True` (empty prefix is trivially valid).

3. To finish at position `i` (i.e., group ends at index `i-1`), we need a start index `j` such that:

   * size ≥ K ⇒ `i - j ≥ K` ⇒ `j ≤ i - K`
   * within-group gap ≤ M ⇒ `a[i-1] - a[j] ≤ M`
   * and the prefix before this group is valid ⇒ `dp[j] == True`

4. Define `L(i)` = the **smallest** index `j` with `a[i-1] - a[j] ≤ M`.
   Then valid starts for the last group are `j ∈ [L(i), i-K]`.
   So:

   ```
   dp[i] = (∃ j in [L(i), i-K] with dp[j] == True)
   ```

5. Maintain a **prefix count** of `dp` trues, `pref[t] = dp[0] + … + dp[t]`.
   Then “exists j with dp[j]==True in [L..R]” ⇔ `pref[R] - pref[L-1] > 0` (careful with borders).
   This makes each `dp[i]` computable in **O(1)** once `L(i)` is known.

6. Compute `L(i)` efficiently while scanning `i = 1..N`:

   * Two-pointer: keep a left pointer `l` such that `a[i-1] - a[l] ≤ M` and move it only forward.
     Total **O(N)** after sorting, so overall **O(N log N)**.
   * Or `bisect_left(a, a[i-1] - M)` in **O(log N)** per `i` (also overall **O(N log N)**).

Answer: `dp[N]`.

---

## Dry run (given sample)

```
N=5, K=2, M=3, arr=[8,3,9,1,2]
sorted a = [1,2,3,8,9]

dp[0]=True, pref[0]=1
l=0 (minimal index with a[i-1]-a[l] ≤ M)
```

We compute `dp[i]` for i=1..5 (group ends at index i-1):

* `i=1`: right=0 (val=1).
  While `a[0]-a[l] > 3`? → `0` (false). So `l=0`.
  Range for `j` is `[l .. i-K] = [0 .. -1]` → empty ⇒ `dp[1]=False`. `pref[1]=1`.

* `i=2`: right=1 (val=2), `2-1=1 ≤ 3` so `l=0`.
  Range `[0 .. 0]` → check `dp[0]=True` ⇒ `dp[2]=True`. `pref[2]=2`.

* `i=3`: right=2 (val=3), `3-1=2 ≤ 3` so `l=0`.
  Range `[0 .. 1]` → any `dp` true there? `pref[1]-pref[-1]=1-0=1>0` ⇒ `dp[3]=True`. `pref[3]=3`.

* `i=4`: right=3 (val=8). Move `l` until `8-a[l]≤3` →
  `8-1=7>3` → l=1; `8-2=6>3` → l=2; `8-3=5>3` → l=3; `8-8=0≤3` keep `l=3`.
  Range `[l .. i-K] = [3 .. 2]` → empty ⇒ `dp[4]=False`. `pref[4]=3`.

* `i=5`: right=4 (val=9). Keep `l=3` (since `9-8=1≤3`).
  Range `[3 .. 3]` → check `dp[3]=True` ⇒ `dp[5]=True`. `pref[5]=4`.

Result `dp[5]=True` → **YES** (e.g., groups `{1,2,3}` and `{8,9}`).

---

# 3) Python solutions (two ways)

## A) Sort + two pointers + prefix-true DP — **O(N log N)** time, **O(N)** space (most expected)

```python
#User function Template for python3

class Solution:
    def partitionArray(self, N, K, M, arr):
        """
        Determine if arr can be partitioned into groups of size >= K
        where max-min within each group <= M.

        Steps:
          1. Sort -> groups become contiguous.
          2. dp[i] = feasibility for first i elements (0..i-1)
          3. For group ending at i-1, valid start j in [L..i-K],
             where L is the smallest index with a[i-1] - a[L] <= M.
          4. Use a prefix sum of booleans to check "any dp[j] is True in [L..i-K]" in O(1).

        Time:  O(N log N) for sort + O(N) scan  => overall O(N log N)
        Space: O(N) for dp + prefix
        """
        a = sorted(arr)
        n = N

        # dp[i] -> can we partition first i elements?  dp[0] = True (empty prefix)
        dp = [False] * (n + 1)
        dp[0] = True

        # pref[i] = number of True dp[0..i]
        pref = [0] * (n + 1)
        pref[0] = 1  # dp[0] is True

        l = 0  # leftmost index such that a[i-1] - a[l] <= M

        for i in range(1, n + 1):
            # Move l forward until the block [l..i-1] satisfies (max-min) <= M
            while l < i and a[i - 1] - a[l] > M:
                l += 1

            # The last group must have size at least K:
            # eligible start indices j ∈ [l .. i-K]
            left = l
            right = i - K

            ok = False
            if right >= left:
                # Does there exist j in [left..right] with dp[j] == True?
                # Use prefix sums of dp-True counts:
                # countTrue = pref[right] - pref[left - 1]
                countTrue = pref[right] - (pref[left - 1] if left - 1 >= 0 else 0)
                ok = (countTrue > 0)

            dp[i] = ok
            pref[i] = pref[i - 1] + (1 if dp[i] else 0)

        return dp[n]
```

---

## B) Same DP but with `bisect_left` instead of two pointers — also **O(N log N)**

```python
from bisect import bisect_left

class SolutionBisect:
    def partitionArray(self, N, K, M, arr):
        a = sorted(arr)
        n = N

        dp = [False] * (n + 1)
        dp[0] = True
        pref = [0] * (n + 1)
        pref[0] = 1

        for i in range(1, n + 1):
            # compute L(i): smallest index l such that a[i-1] - a[l] <= M
            # i.e., a[l] >= a[i-1] - M
            l = bisect_left(a, a[i - 1] - M, 0, i)
            left = l
            right = i - K

            ok = False
            if right >= left:
                cnt = pref[right] - (pref[left - 1] if left > 0 else 0)
                ok = (cnt > 0)

            dp[i] = ok
            pref[i] = pref[i - 1] + (1 if dp[i] else 0)

        return dp[n]
```

---

## C) Educational “brute DP” (nested loops) — **O(N²)** time, **O(N)** space

```python
class SolutionN2:
    def partitionArray(self, N, K, M, arr):
        """
        Naive DP:
          dp[i] = OR over j (<= i-K) such that a[i-1]-a[j] <= M AND dp[j] is True
        We scan j backward until size >= K and constraint breaks.
        Time:  O(N^2) in worst case, Space: O(N)
        """
        a = sorted(arr)
        n = N

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # Try to form last group ending at i-1
            j = i - K
            while j >= 0:
                # group start = j, end = i-1, size = i - j >= K
                if a[i - 1] - a[j] > M:
                    break  # earlier j only worsen (min smaller), so stop
                if dp[j]:
                    dp[i] = True
                    break
                j -= 1

        return dp[n]
```

> In interviews, show **A**. Mention **B** as an equivalent implementation.
> **C** is good as a starting point to “optimize to A”.

---

# 4) Likely interviewer Q&A

**Q1. Why can we restrict groups to contiguous blocks after sorting?**
Because the constraint is on `max − min`. For a set chosen from two disjoint intervals in sorted order, the min comes from the left interval and the max from the right, which only increases the span. So any optimal partition can be transformed into one using contiguous blocks.

**Q2. What does `dp[i]` represent and why does the prefix trick work?**
`dp[i]` = “first `i` elements can be partitioned legally.”
To form the last group ending at `i-1`, valid starts are `j∈[L..i-K]`.
We need to know if **any** `dp[j]` is `True` inside that range.
A prefix count of `dp` truths answers this existence query in O(1).

**Q3. How do you compute `L(i)` efficiently?**
Either a moving left pointer (`two pointers`, total O(N)) or a binary search (`bisect_left`) per `i` (O(log N) each).

**Q4. Complexity?**
Sorting `O(N log N)` + linear scan with two pointers `O(N)` ⇒ **`O(N log N)`** time.
Space: `O(N)` for `dp` and `pref`.

**Q5. Edge cases?**

* `K == 1`: every element alone is a valid group (gap 0 ≤ M) ⇒ always `True`.
* All elements within any window of size `K` exceed `M` span ⇒ immediately `False`.
* Large values (`A[i]` up to `1e9`) — sort and difference checks are safe in Python.

**Q6. Can we return the actual partitions?**
Yes: store for each `i` the `j` that made `dp[i] True`, then backtrack from `i=N` to reconstruct the groups.

**Q7. Could a greedy “pack as many as possible” work?**
No, because choosing a larger earlier block might block forming a later block of size ≥ K. You need DP to check feasibility globally.

---

---

here’s a **runnable, self-contained program** for the **Array Partition** problem that:

* uses the **optimal O(N log N)** approach (sort + two pointers + DP with prefix counts),
* prints the **inputs and outputs** for several cases,
* includes **inline time/space complexity notes** right where they apply,
* and **times the whole run** with `timeit.default_timer`.

---

```python
#!/usr/bin/env python3
"""
Array Partition (GFG style)

Rules:
- Partition arr into disjoint groups.
- Every group has at least K elements.
- For every group, (max - min) <= M.
Return True/False (YES/NO).

Approach (MOST EXPECTED):
1) Sort the array (O(N log N)). In sorted order, every valid group is a contiguous block.
2) DP over prefix length:
   dp[i] = can we partition the first i elements (0..i-1)?
   Let L be the smallest index such that a[i-1] - a[L] <= M.
   Then the last group can start at any j in [L, i-K].
   So dp[i] = True iff there exists j in [L, i-K] with dp[j] = True.
3) Maintain a prefix count of 'True' in dp to answer the "exists" query in O(1).

Asymptotics:
- Time:  O(N log N)  (sort) + O(N) scan = O(N log N)
- Space: O(N)        (dp and prefix arrays)
"""

from timeit import default_timer as timer


# ---------------------------
# User function (required API)
# ---------------------------
class Solution:
    def partitionArray(self, N, K, M, arr):
        """
        Time:  O(N log N) for sort + O(N) DP scan
        Space: O(N) for dp/prefix arrays
        """
        # ---- Sort so valid groups become contiguous blocks (O(N log N)) ----
        a = sorted(arr)

        n = N
        # dp[i] -> can we partition first i elements (0..i-1)?
        # Base: dp[0] = True (empty prefix is valid)
        dp = [False] * (n + 1)   # O(N) space
        dp[0] = True

        # pref[i] = count of True in dp[0..i] (prefix-True count)
        # lets us answer "exists dp[j]==True in [L..R]" in O(1)
        pref = [0] * (n + 1)     # O(N) space
        pref[0] = 1  # dp[0] is True

        # Two-pointer to maintain the smallest L such that a[i-1]-a[L] <= M.
        # This runs in total O(N) across the entire loop.
        L = 0

        # ---- DP over i = 1..N (O(N)) ----
        for i in range(1, n + 1):
            # Move L forward until block [L..i-1] satisfies (max-min) <= M
            # Each element advances L at most once overall -> O(N) total.
            while L < i and a[i - 1] - a[L] > M:
                L += 1

            # Last group must have size >= K → j ∈ [L .. i-K]
            left = L
            right = i - K

            if right >= left:
                # Count of True in dp[left..right] via prefix sums (O(1)):
                # countTrue = pref[right] - pref[left-1]
                count_true = pref[right] - (pref[left - 1] if left > 0 else 0)
                dp[i] = (count_true > 0)
            else:
                dp[i] = False

            # Update prefix-True count for dp[0..i] (O(1)):
            pref[i] = pref[i - 1] + (1 if dp[i] else 0)

        return dp[n]


# ---------------------------
# Demo + timing
# ---------------------------
def run_tests():
    tests = [
        # (N, K, M, arr, expected)
        (5, 2, 3, [8, 3, 9, 1, 2], True),   # sample: YES
        (4, 2, 0, [1, 1, 2, 2], True),      # groups [1,1] and [2,2]
        (4, 3, 1, [1, 2, 10, 11], False),   # can't form any 3-sized valid block
        (6, 2, 2, [3, 3, 4, 5, 8, 9], True),# {3,3,4},{5,8,9} invalid (9-5=4>2),
                                            # but {3,3},{4,5},{8,9} works
        (1, 1, 100, [10], True),            # single element, K=1
        (6, 3, 0, [2, 2, 2, 3, 3, 3], True) # {2,2,2},{3,3,3}
    ]

    sol = Solution()
    for N, K, M, arr, exp in tests:
        ans = sol.partitionArray(N, K, M, arr)
        print(f"N={N}, K={K}, M={M}, arr={arr}")
        print(f"  Output  : {'YES' if ans else 'NO'}")
        if exp is not None:
            print(f"  Expected: {'YES' if exp else 'NO'}")
        print("-" * 60)


def main():
    print("Array Partition — O(N log N) DP with prefix-existence check\n")
    t0 = timer()   # start timing the entire program
    run_tests()
    t1 = timer()   # stop timing
    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for full program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### What you’ll see (example)

```
Array Partition — O(N log N) DP with prefix-existence check

N=5, K=2, M=3, arr=[8, 3, 9, 1, 2]
  Output  : YES
  Expected: YES
------------------------------------------------------------
N=4, K=2, M=0, arr=[1, 1, 2, 2]
  Output  : YES
  Expected: YES
------------------------------------------------------------
N=4, K=3, M=1, arr=[1, 2, 10, 11]
  Output  : NO
  Expected: NO
------------------------------------------------------------
N=6, K=2, M=2, arr=[3, 3, 4, 5, 8, 9]
  Output  : YES
  Expected: YES
------------------------------------------------------------
N=1, K=1, M=100, arr=[10]
  Output  : YES
  Expected: YES
------------------------------------------------------------
N=6, K=3, M=0, arr=[2, 2, 2, 3, 3, 3]
  Output  : YES
  Expected: YES
------------------------------------------------------------

Total time for full program run: 1.2 ms
```

---

## 6) Real-World Use Cases (high-value)

* **Batching orders / shipments** by item size/weight tolerance
  Group items so each batch has at least K pieces and intra-batch spread (max−min) is within M for packaging/homogeneity constraints.

* **Forming classrooms/cohorts** by test scores/ages
  Ensure each class has at least K students and score/age range ≤ M for fairness and curriculum pacing.

* **Sensor data bucketing** for calibration
  Partition readings into buckets with minimum sample counts and tight value range for stable calibration baselines.

* **Manufacturing lots** with tolerance control
  Create production lots where every lot has a minimum count and parts’ measurements stay within a narrow window.

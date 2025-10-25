Here’s the **complete README-style** conversion of your image — with no details omitted 👇

---

# 🧩 More than n/k Occurrences

**Difficulty:** Easy
**Accuracy:** 58.35%
**Submissions:** 130K+
**Points:** 2
**Average Time:** 45m

---

## 📘 Problem Statement

Given an array `arr` and an element `k`, the task is to find the **count of elements in the array** that appear **more than n/k times**,
where `n` is the length of the array.

---

## 💡 Examples

### Example 1

**Input:**
`arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4`

**Output:**
`2`

**Explanation:**
In the given array, `3` and `2` are the only elements that appear **more than n/k times**.

---

### Example 2

**Input:**
`arr = [2, 3, 3, 2], k = 3`

**Output:**
`2`

**Explanation:**
In the given array, `3` and `2` are the only elements that appear **more than n/k times**.
So the count of such elements is `2`.

---

### Example 3

**Input:**
`arr = [1, 4, 7, 7], k = 2`

**Output:**
`0`

**Explanation:**
In the given array, no element appears **more than n/k times**.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10^6  
0 ≤ arr[i] ≤ 10^8  
1 ≤ k ≤ arr.size()
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

`Amazon`

---

## 🏷️ Topic Tags

* Arrays
* Searching
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [*Given an array of size n finds all the elements that appear more than n/k times*](https://www.geeksforgeeks.org/problems/count-element-occurences/1)

---

---

awesome — here’s your interview-ready pack for **“More than n/k Occurrences”** using the classic **Misra–Gries** idea + alternatives.

---

# 2) Concept + Step-by-Step Dry Run

## Problem in one line

Given array `arr` (length `n`) and integer `k`, return the **count of distinct elements** whose frequency is **strictly greater than `n/k`**.

## Key idea (most expected)

Use **Misra–Gries (generalized majority voting)**:

* At most **`k-1`** values can appear more than `n/k` times.
* Keep a small dictionary of **≤ `k-1` candidates** with counters.
* **Pass 1:**

  * If `x` already a candidate → ++count.
  * Else if we have < `k-1` candidates → add `x` with count 1.
  * Else → **decrement all counts**; remove any that hit zero.
* **Pass 2 (verification):** Count real frequencies only for remaining candidates and check `> n//k`.

Time **O(n)**; extra space **O(k)**.

### Why it works

Every time we fail to fit a new element because candidates are “full”, we delete a **balanced unit** of support from **k** different elements. Any element occurring **> n/k** survives to the end as a candidate (then we verify).

---

## Dry run (Misra–Gries)

`arr = [3, 1, 2, 2, 1, 2, 3, 3],  k = 4,  n = 8,  threshold = n//k = 2`

**Pass 1 (candidates, size ≤ k-1 = 3)**

| Step | x | candidates before | action     | candidates after |
| ---- | - | ----------------- | ---------- | ---------------- |
| 1    | 3 | {}                | add (room) | {3:1}            |
| 2    | 1 | {3:1}             | add        | {3:1,1:1}        |
| 3    | 2 | {3:1,1:1}         | add        | {3:1,1:1,2:1}    |
| 4    | 2 | {3:1,1:1,2:1}     | inc 2      | {3:1,1:1,2:2}    |
| 5    | 1 | {3:1,1:1,2:2}     | inc 1      | {3:1,1:2,2:2}    |
| 6    | 2 | {3:1,1:2,2:2}     | inc 2      | {3:1,1:2,2:3}    |
| 7    | 3 | {3:1,1:2,2:3}     | inc 3      | {3:2,1:2,2:3}    |
| 8    | 3 | {3:2,1:2,2:3}     | inc 3      | {3:3,1:2,2:3}    |

End of pass-1 candidates: `{3:?, 1:?, 2:?}` (counts here are meaningless for threshold; we must verify).

**Pass 2 (verify true counts only for candidates)**
Count real freq for 3,1,2: `{3:3, 1:2, 2:3}`.

Check `> 2` → `3` (yes), `1` (no), `2` (yes) ⇒ **2 elements**.

Matches sample output **2** ✅

---

# 3) Python solutions (brute + optimized), with clear naming & comments

### A) Optimized Misra–Gries (O(n) time, O(k) space) — **most expected**

```python
class Solution:
    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr, k):
        """
        Misra–Gries (generalized majority voting).
        Pass 1: keep at most (k-1) candidate elements with counters.
        Pass 2: verify real frequencies of remaining candidates.

        Time : O(n) for both passes combined
        Space: O(k)   (<= k-1 candidates)
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return 0
        if k == 1:
            # More than n/1 -> more than n occurrences (impossible)
            return 0

        # ------------- Pass 1: shortlist candidates -------------
        candidates = {}  # value -> count (not final frequencies)
        for x in arr:
            if x in candidates:
                candidates[x] += 1
            elif len(candidates) < k - 1:
                candidates[x] = 1
            else:
                # decrement every candidate; remove zeros
                to_del = []
                for v in candidates:
                    candidates[v] -= 1
                    if candidates[v] == 0:
                        to_del.append(v)
                for v in to_del:
                    del candidates[v]

        # ------------- Pass 2: verify true counts -------------
        # Count only for remaining candidates to keep O(k) memory.
        true_count = {v: 0 for v in candidates}
        for x in arr:
            if x in true_count:
                true_count[x] += 1

        threshold = n // k
        answer = sum(1 for v in true_count.values() if v > threshold)
        return answer
```

---

### B) Hash‐map counting (simple, but O(n) space) — interview “easy path”

```python
from collections import Counter

class SolutionCount:
    def countOccurence(self, arr, k):
        """
        Count every value, then count how many exceed n//k.
        Time : O(n) average (hashing)
        Space: O(n) for frequency map
        """
        n = len(arr)
        freq = Counter(arr)      # O(n)
        threshold = n // k
        return sum(1 for c in freq.values() if c > threshold)
```

---

### C) Sorting + scan (no extra hash, but O(n log n) time)

```python
class SolutionSort:
    def countOccurence(self, arr, k):
        """
        Sort then compress runs and compare with n//k.
        Time : O(n log n) (sort dominates)
        Space: O(1) extra (in-place sort)
        """
        n = len(arr)
        if n == 0: return 0
        arr.sort()
        threshold = n // k
        answer = 0

        i = 0
        while i < n:
            j = i
            # count frequency of arr[i]
            while j < n and arr[j] == arr[i]:
                j += 1
            if (j - i) > threshold:
                answer += 1
            i = j
        return answer
```

---

# 4) Interview “fast recall” + expected Q&A

## 10-second memory hook

* **Mantra:** “**At most k-1 heavy hitters. Keep k-1, cancel the rest. Verify.**”
* **5-liner pseudo-code (mental):**
  `cand = {}` → for x:

  * `++cand[x]` if in
  * `elif |cand| < k-1` add
  * `else` decrement all & drop zeros
    → recount only candidates → count those `> n//k`.

## Likely follow-ups (crisp answers)

**Q1. Why at most k-1 elements?**
Because if `k` elements each occur more than `n/k`, their total would exceed `n`. Pigeonhole principle ⇒ **≤ k-1**.

**Q2. Why do we need the second pass?**
First pass only guarantees potential winners; counters there are **not real frequencies** after cancellations. We must **verify**.

**Q3. Complexity?**
Misra–Gries: **O(n)** time, **O(k)** space.
Counting map: **O(n)** time, **O(n)** space.
Sorting: **O(n log n)** time, **O(1)** extra.

**Q4. What if `k = 1`?**
Threshold is `n/1 = n`. “More than n” is impossible ⇒ answer `0`.

**Q5. What about very large `k` (e.g., `k > n`)?**
Threshold `n//k` becomes `0`; every **distinct** element appears more than `0`, so the answer is simply `#distinct`. Misra–Gries still works (it allows up to `k-1 ≥ n-1` candidates, effectively all distinct).

**Q6. Can we return the actual elements, not just the count?**
Yes—use the same algorithm; instead of summing booleans in pass 2, collect keys with `count > n//k`.

**Q7. When would you not use Misra–Gries?**
If `k` is tiny it shines; if `k` is close to `n`, the candidate map can grow large (still correct), and a frequency map might be simpler.

---

---

awesome — closing out **More than n/k Occurrences** with the last two bits you asked for 👇

---

# 5) Real-World Use Cases (short, interview-friendly)

* **A/B/N Experiment Analysis:** Identify “heavy-hitter” variants (users, SKUs, ads) that appear more than `n/k` times in logs to prioritize investigation or cache placement.
* **Network Traffic / CDN Caching:** Pick origins or paths occurring more than `n/k` requests to pre-warm caches or allocate bandwidth.
* **Fraud/Abuse Triage:** In a stream of events (cards, IPs, device IDs), quickly shortlist entities whose frequency passes a support threshold for deeper checks.
* **Inventory / Order Streams:** Detect items that dominate orders in a time window to optimize replenishment (top sellers over `n/k`).

These directly map to “find elements whose frequency exceeds a relative threshold `n/k`,” where `k` is a tunable knob.

---

# 6) Full Python Program

Includes:

* **Misra–Gries** (O(n) time, O(k) space) — the interview-favorite.
* **Counting map** (simple, O(n) space).
* **Sorting** (O(n log n) time, O(1) extra).
* Printed results for sample inputs.
* `timeit` micro-benchmarks on a larger random array.

```python
from timeit import timeit
from random import randint, seed
from collections import Counter

# ------------------------------------------------------------
# Solution 1: Misra–Gries (Generalized Majority Voting)
# ------------------------------------------------------------
class Solution:
    # Function to find count of elements appearing more than n/k times.
    def countOccurence(self, arr, k):
        """
        Pass 1: maintain at most (k-1) candidate elements with counters.
        Pass 2: verify the true frequencies of those candidates only.
        Complexity (step-by-step):
          - Build/maintain candidate map: O(n) time, O(k) space
          - Verify counts for candidates: O(n) time, O(k) space
          - Total: Time O(n), Space O(k)
        """
        n = len(arr)
        if n == 0 or k <= 1:
            # k==1 => threshold n/1 == n; "more than n" impossible
            return 0

        # ---- Pass 1: shortlist candidates (<= k-1 of them) ----
        candidates = {}  # value -> counter (not final frequency)
        for x in arr:  # O(n)
            if x in candidates:
                candidates[x] += 1  # O(1)
            elif len(candidates) < k - 1:
                candidates[x] = 1   # O(1)
            else:
                # "Cancel out" one count from each candidate
                # O(k) in worst case per cancellation step (but k is a parameter)
                to_delete = []
                for v in candidates:
                    candidates[v] -= 1
                    if candidates[v] == 0:
                        to_delete.append(v)
                for v in to_delete:
                    del candidates[v]

        # ---- Pass 2: verify only the shortlisted candidates ----
        threshold = n // k
        true_count = {v: 0 for v in candidates}  # O(k)
        for x in arr:  # O(n)
            if x in true_count:
                true_count[x] += 1

        # Count how many exceed threshold
        return sum(1 for c in true_count.values() if c > threshold)


# ------------------------------------------------------------
# Solution 2: Simple counting map (straightforward, O(n) space)
# ------------------------------------------------------------
class SolutionCount:
    def countOccurence(self, arr, k):
        """
        Count all frequencies, then count how many exceed n//k.
        Time:  O(n) average (hashing)
        Space: O(n) for the map
        """
        n = len(arr)
        if n == 0 or k <= 1:
            return 0
        freq = Counter(arr)            # O(n) time, O(n) space
        threshold = n // k
        return sum(1 for c in freq.values() if c > threshold)


# ------------------------------------------------------------
# Solution 3: Sorting + scan (no hash, but O(n log n))
# ------------------------------------------------------------
class SolutionSort:
    def countOccurence(self, arr, k):
        """
        Sort the array and compress runs to compute frequencies.
        Time:  O(n log n) (sort dominates)
        Space: O(1) extra (in-place sort), aside from input
        """
        n = len(arr)
        if n == 0 or k <= 1:
            return 0
        arr.sort()                   # O(n log n)
        threshold = n // k
        ans = 0
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] == arr[i]:
                j += 1               # count run length
            if (j - i) > threshold:
                ans += 1
            i = j
        return ans


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== More than n/k Occurrences ===\n")

    samples = [
        ("Example 1", [3,1,2,2,1,2,3,3], 4, 2),
        ("Example 2", [2,3,3,2],         3, 2),
        ("Example 3", [1,4,7,7],         2, 0),
        ("All same",  [5,5,5,5,5],       3, 1),
        ("Distinct",  [1,2,3,4,5,6],     10, 6),  # threshold = n//k = 0 -> all distinct count
    ]

    mg   = Solution()
    cnt  = SolutionCount()
    srt  = SolutionSort()

    for name, arr, k, expected in samples:
        print(f"{name}:")
        print(f"  Input:    arr={arr}, k={k}")
        out_mg  = mg.countOccurence(arr[:], k)
        out_cnt = cnt.countOccurence(arr[:], k)
        out_srt = srt.countOccurence(arr[:], k)
        print(f"  Misra–Gries O(n): {out_mg}")
        print(f"  Counting    O(n): {out_cnt}")
        print(f"  Sorting O(n log n): {out_srt}")
        print(f"  Expected:   {expected}")
        print(f"  Match?      {out_mg == out_cnt == out_srt == expected}\n")

    # ---- Micro-benchmarks on a larger random array ----
    seed(11)
    n = 200_000
    big = [randint(1, 10**6) for _ in range(n)]
    k   = 50  # typical smallish k

    # Wrap callables so timeit measures only function execution
    t_mg  = timeit(lambda: Solution().countOccurence(big, k), number=3)
    t_cnt = timeit(lambda: SolutionCount().countOccurence(big, k), number=3)
    t_srt = timeit(lambda: SolutionSort().countOccurence(big[:], k), number=3)

    print("=== Timing (seconds) on n = 200,000; runs = 3 ===")
    print(f"Misra–Gries  (O(n),  O(k) space): {t_mg:.4f}s  (~{t_mg/3:.4f}s/run)")
    print(f"Counting map  (O(n),  O(n) space): {t_cnt:.4f}s (~{t_cnt/3:.4f}s/run)")
    print(f"Sorting scan (O(n log n), O(1)):   {t_srt:.4f}s  (~{t_srt/3:.4f}s/run)")


if __name__ == "__main__":
    run_demo()
```

**What you’ll see when you run it**

* For each sample case, all three methods print the same count and a `Match? True`.
* The timing section contrasts Misra–Gries vs. a full frequency map vs. sorting on a big input. In practice, Misra–Gries shines when `k` is small relative to `n`, thanks to **O(k)** space.


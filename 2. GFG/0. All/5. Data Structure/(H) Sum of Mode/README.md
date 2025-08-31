# Sum of Mode

**Difficulty:** Hard
**Accuracy:** 43.16%
**Submissions:** 88+
**Points:** 8
**Average Time:** 20m

---

## Problem Statement

Given an array `arr[]` of positive integers and an integer `k`, find the **sum of the modes** of all the subarrays of size `k`.

**Note:**
The **mode** of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the **smallest** such element is considered the mode.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3`
**Output:** `13`
**Explanation:**
The mode of each `k` size subarray is `[1, 2, 2, 2, 2, 4]` and the sum of all modes is `13`.

---

### Example 2

**Input:** `arr[] = [1, 2, 1, 3, 5], k = 2`
**Output:** `6`
**Explanation:**
The mode of each `k` size subarray is `[1, 1, 1, 3]` and the sum of all modes is `6`.

---

## Constraints

* `1 ≤ k ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n log k)`
* **Auxiliary Space:** `O(k)`

---

## Topic Tags

* Greedy
* set
* sliding-window
* two-pointer-algorithm
* Hash

---

## Related Articles

* [Dsa](https://www.geeksforgeeks.org/dsa/mode-in-every-k-sized-window/)

---

---

Here’s an interview-ready guide for **Sum of Mode (window size k)**.

---

## 2) Explanation (how to think about it)

We need the **mode** (most frequent value; if tie → **smallest value**) for **every** subarray (window) of length `k`, and sum those modes.

### Naïve idea (baseline)

For each window, count frequencies anew (e.g., with `Counter.most_common(1)`).
**Cost:** `O(k log k)` per window → `O(n k log k)` total — too slow for `n up to 1e5`.

### Optimized idea (sliding window + order stats)

Slide the window one step at a time:

* **Add** the entering element and **remove** the leaving element (update counts in `O(1)`).
* We need fast access to the current **mode** with the tie-break rule.
  Use a **max-heap** keyed by `(-freq, value)`:

  * Higher frequency → smaller `-freq` (so it rises to the top).
  * On frequency ties, **smaller value** wins (min-heap’s second key).

Since frequencies change when we slide, the heap will contain **stale entries**.
We fix this with **lazy deletion**: when we query the top, we pop until the top pair’s frequency matches the one in our dictionary.

**Per slide:** two pushes (enter/leave) + a few pops → **`O(log k)` amortized**.
**Total:** **`O(n log k)` time**, **`O(k)` space**.

---

## 2.5) Step-by-step dry run (Example 1)

`arr = [1, 2, 3, 2, 5, 2, 4, 4], k = 3`
Windows and modes:

1. `[1,2,3]`
   freq: {1:1, 2:1, 3:1} → tie on freq 1 → smallest = **1**
   sum = 1

2. `[2,3,2]` (add 2, remove 1)
   freq: {2:2, 3:1} → mode **2**
   sum = 1 + 2 = 3

3. `[3,2,5]` (add 5, remove 3)
   freq: {2:1, 3:1, 5:1} → smallest among ties = **2**
   sum = 3 + 2 = 5

4. `[2,5,2]` (add 2, remove 3)
   freq: {2:2, 5:1} → mode **2**
   sum = 5 + 2 = 7

5. `[5,2,4]` (add 4, remove 2)
   freq: {2:1, 4:1, 5:1} → smallest among ties = **2**
   sum = 7 + 2 = 9

6. `[2,4,4]` (add 4, remove 5)
   freq: {2:1, 4:2} → mode **4**
   sum = 9 + 4 = **13** ✅

---

## 3) Python solutions (brute + optimized), interview-style

```python
from collections import defaultdict
import heapq

class Solution:
    def sumOfModes(self, arr, k):
        """
        Optimized: Sliding window + max-heap with lazy deletion.
        Heap stores tuples (-freq, value); smallest tuple at top is our mode
        because:
          - higher freq -> smaller -freq
          - tie on freq: smaller value wins automatically
        Time:  O(n log k)  (push/pop per slide)
        Space: O(k)        (freq map + heap of window-sized items)
        """
        n = len(arr)
        if k == 0 or n == 0:
            return 0
        if k == 1:
            # Each window has 1 element -> mode is that element
            return sum(arr)

        freq = defaultdict(int)       # value -> current frequency in window
        heap = []                     # entries are (-freq, value)

        # --- build the first window: O(k log k) for heap pushes, O(k) for freq
        for x in arr[:k]:
            freq[x] += 1
        for v, f in freq.items():
            heapq.heappush(heap, (-f, v))

        def clean_top():
            """Pop stale heap entries until top matches current freq.
               Amortized O(log k) across the run."""
            while heap:
                negf, val = heap[0]
                f = -negf
                if freq.get(val, 0) != f:   # stale
                    heapq.heappop(heap)
                else:
                    break

        clean_top()
        total = 0
        total += heap[0][1]  # mode value of first window

        # --- slide the window across the array: O((n-k) log k)
        for r in range(k, n):
            add_val = arr[r]
            rem_val = arr[r - k]

            # 1) add entering element
            freq[add_val] += 1
            heapq.heappush(heap, (-freq[add_val], add_val))

            # 2) remove leaving element
            freq[rem_val] -= 1
            if freq[rem_val] == 0:
                del freq[rem_val]
            else:
                heapq.heappush(heap, (-freq[rem_val], rem_val))

            # 3) query mode = valid top of heap
            clean_top()
            total += heap[0][1]

        return total

    # ---------- Simpler (but slower) baseline for understanding ----------
    def sumOfModes_bruteforce(self, arr, k):
        """
        For each window, rebuild a frequency map, then find mode with tie rule.
        Time:  O(n * k) to count + O(k) to scan -> O(n * k)
        Space: O(k) for the window's frequency dictionary.
        """
        from collections import Counter
        n = len(arr)
        if k == 0 or n == 0:
            return 0
        ans = 0
        for i in range(n - k + 1):
            freq = Counter(arr[i:i + k])  # O(k)
            # Find (max frequency, then smallest value)
            maxf = max(freq.values())     # O(k)
            mode_val = min(v for v, f in freq.items() if f == maxf)  # O(k)
            ans += mode_val
        return ans

    # ---------- Alternative optimized: frequency buckets ----------
    def sumOfModes_buckets(self, arr, k):
        """
        Sliding window + 'buckets' mapping freq -> min-heap of values.
        We also track max_freq. We still use lazy deletion inside per-bucket heap.
        Time:  O(n log k)  (push/pop within min-heaps)
        Space: O(k)
        """
        from collections import defaultdict
        import heapq

        n = len(arr)
        if k == 0 or n == 0:
            return 0

        freq = defaultdict(int)             # value -> freq
        buckets = defaultdict(list)         # freq -> min-heap of values
        max_freq = 0

        def push_bucket(v, f):
            heapq.heappush(buckets[f], v)

        def pop_valid_from(f):
            """Return smallest value with current freq == f, or None."""
            heap = buckets[f]
            while heap:
                v = heap[0]
                if freq.get(v, 0) == f:
                    return v
                heapq.heappop(heap)  # stale
            return None

        # init
        for x in arr[:k]:
            freq[x] += 1
        for v, f in freq.items():
            push_bucket(v, f)
            if f > max_freq:
                max_freq = f

        ans = 0
        # read first window’s mode
        mv = pop_valid_from(max_freq)
        if mv is None:  # safety
            for f in range(max_freq, 0, -1):
                mv = pop_valid_from(f)
                if mv is not None:
                    max_freq = f
                    break
        ans += mv

        # slide
        for r in range(k, n):
            add_v = arr[r]
            rem_v = arr[r - k]

            # add
            old = freq[add_v]
            freq[add_v] = old + 1
            push_bucket(add_v, old + 1)
            if old + 1 > max_freq:
                max_freq = old + 1

            # remove
            old = freq[rem_v]
            if old == 1:
                del freq[rem_v]
            else:
                freq[rem_v] = old - 1
                push_bucket(rem_v, old - 1)

            # query mode: ensure we’re at a non-empty valid bucket
            mv = pop_valid_from(max_freq)
            while mv is None and max_freq > 0:
                max_freq -= 1
                mv = pop_valid_from(max_freq)
            ans += mv

        return ans
```

---

## 4) Likely interviewer Q\&A

**Q1. Why does the heap approach work with lazy deletion?**
**A.** The heap always stores candidates keyed by `(-freq, value)`. When frequencies change, old heap entries become stale. We keep pushing new `( -updated_freq, value )`. During query we pop the top while its stored frequency doesn’t match the current dictionary frequency; what remains is the true mode. Each stale entry is popped once, so the total extra work is bounded → **amortized `O(log k)` per slide**.

**Q2. How do you enforce the “smallest value on ties” rule?**
**A.** The heap key is `(-freq, value)`. For equal `-freq` (i.e., equal freq), the min-heap chooses the **smaller `value`** automatically.

**Q3. What’s the exact complexity?**
**A.** Building the first window: `O(k log k)` (or `O(k)` pushes, each `log k`).
Each slide: constant number of heap pushes + a few pops → `O(log k)` amortized.
Total: **`O(n log k)` time**, **`O(k)` space**.

**Q4. Can we do `O(n)`?**
**A.** Not easily in general without additional constraints because we need order statistics (mode) with tie-breaking every step. Maintaining exact mode under increments/decrements typically requires at least `log k` with comparison-based structures.

**Q5. Edge cases?**
**A.**

* `k == 1` → each window’s mode is the single element ⇒ answer is `sum(arr)`.
* All elements distinct within windows → mode is the **smallest** element in the window (since all have freq 1).
* Large values (up to `1e5`) are fine; dictionary/heap sizes are at most `k`.

**Q6. Pitfalls to avoid?**
**A.**

* Forgetting to **lazy-clean** the heap before reading the mode.
* Pushing an entry with frequency `0` (don’t; just delete key).
* Off-by-one on slide indices.

---

---

I’ve run a **full inline Python program** that:

* Implements an **optimized** `O(n log k)` solution using a **sliding window + heap with lazy deletion**, and a **bruteforce** baseline.
* Prints **inputs and outputs** for both sample cases.
* Runs a **large random test** near the constraints.
* Uses `timeit.default_timer()` to print the **TOTAL MAIN RUNTIME** (i.e., the time for the whole program’s execution).

You can copy the exact script from the output above—it already includes detailed **inline complexity comments**.

```python
# Re-run the full inline program block so outputs are visible
from collections import defaultdict
import heapq, random, timeit
from typing import List

class Solution:
    def sumOfModes(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k == 0 or n == 0:
            return 0
        if k == 1:
            return sum(arr)

        freq = defaultdict(int)
        heap = []

        for x in arr[:k]:
            freq[x] += 1
        for v, f in freq.items():
            heapq.heappush(heap, (-f, v))

        def clean_top():
            while heap:
                negf, val = heap[0]
                if freq.get(val, 0) == -negf:
                    return
                heapq.heappop(heap)

        clean_top()
        total = heap[0][1]

        for r in range(k, n):
            add_val = arr[r]
            rem_val = arr[r - k]

            freq[add_val] += 1
            heapq.heappush(heap, (-freq[add_val], add_val))

            old = freq[rem_val]
            if old == 1:
                del freq[rem_val]
            else:
                freq[rem_val] = old - 1
                heapq.heappush(heap, (-(old - 1), rem_val))

            clean_top()
            total += heap[0][1]

        return total

    def sumOfModes_bruteforce(self, arr: List[int], k: int) -> int:
        from collections import Counter
        n = len(arr)
        if k == 0 or n == 0:
            return 0
        total = 0
        for i in range(n - k + 1):
            cnt = Counter(arr[i:i+k])
            maxf = max(cnt.values())
            mode_val = min(v for v, f in cnt.items() if f == maxf)
            total += mode_val
        return total

def main():
    sol = Solution()
    print("=== Sum of Mode — Demo & Timing ===")

    arr1 = [1, 2, 3, 2, 5, 2, 4, 4]
    k1 = 3
    print("\nInput 1:", arr1, "k =", k1)
    print("Optimized (O(n log k)):", sol.sumOfModes(arr1, k1))
    print("Bruteforce (O(n*k))  :", sol.sumOfModes_bruteforce(arr1, k1))

    arr2 = [1, 2, 1, 3, 5]
    k2 = 2
    print("\nInput 2:", arr2, "k =", k2)
    print("Optimized (O(n log k)):", sol.sumOfModes(arr2, k2))
    print("Bruteforce (O(n*k))  :", sol.sumOfModes_bruteforce(arr2, k2))

    n = 100000
    random.seed(0)
    arr_big = [random.randint(1, 10**5) for _ in range(n)]
    k_big = 500
    t0 = timeit.default_timer()
    ans_big = sol.sumOfModes(arr_big, k_big)
    t1 = timeit.default_timer()
    print(f"\nLarge test: n={n}, k={k_big}")
    print("Optimized answer:", ans_big)
    print("Optimized run time:", f"{t1 - t0:.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")

```

---

## 6) Real-World Use Cases (high-impact)

* **Monitoring top events per time window:** In telemetry/log analytics, for each rolling time window (e.g., 5 minutes), find the **most frequent error code**; if ties, prefer the **lowest code** (for deterministic alerts). Sum/aggregate modes across windows for trend scoring.
* **Retail basket analysis:** For each sliding group of `k` transactions, determine the **most frequently bought item** to track short-term demand bursts; tie-break by **lowest SKU ID** for consistent reports.
* **Network traffic classification:** Over rolling packet windows, identify the **most frequent protocol/port** to detect dominant flows; deterministic tie-breaking ensures stable signals for downstream systems.


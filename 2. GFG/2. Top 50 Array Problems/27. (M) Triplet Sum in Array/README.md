
---

# 🧮 Triplet Sum in Array

**Difficulty:** Medium
**Accuracy:** 35.0%
**Submissions:** 325K+
**Points:** 4
**Average Time:** 15m

---

## 📝 Problem Statement

Given an array `arr[]` and an integer `target`, determine if there exists a triplet in the array whose sum equals the given target.

Return `true` if such a triplet exists, otherwise, return `false`.

---

## 🔍 Examples

### Example 1:

```
Input:  arr[] = [1, 4, 45, 6, 10, 8], target = 13  
Output: true  
Explanation: The triplet (1, 4, 8) sums up to 13
```

### Example 2:

```
Input:  arr[] = [1, 2, 4, 3, 6, 7], target = 10  
Output: true  
Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10.
```

### Example 3:

```
Input:  arr[] = [40, 20, 10, 3, 6, 7], target = 24  
Output: false  
Explanation: No triplet in the array sums to 24
```

---

## 📌 Constraints

* $3 \leq \text{arr.size()} \leq 10^3$
* $1 \leq \text{arr[i]} \leq 10^5$

---

## ✅ Expected Time and Space Complexities

* **Time Complexity:** $O(n^2)$
* **Auxiliary Space:** $O(1)$

---

## 🏢 Company Tags

* Accolite
* Amazon
* Microsoft
* OYO Rooms
* Samsung
* CarWale

---

## 🧠 Topic Tags

* two-pointer-algorithm
* Arrays
* Hash
* Sorting
* Data Structures
* Algorithms

---

## 🗂️ Related Interview Experiences

* [Accolite Interview Experience Set 10 On Campus](#)
* [Samsung Rd Interview Experience For Summer Internship 2021 Sri Bengaluru](#)

---

## 📚 Related Articles

* [Find A Triplet That Sum To A Given Value](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)

---

---
awesome—here’s your interview-ready pack for **Triplet Sum in Array**.

---

# 2) Explanation + step-by-step dry run

## Problem in one line

Given `arr` and an integer `target`, determine if **any three numbers** in `arr` sum to `target`. Return **True/False**.

## Most-expected idea (sort + two pointers)

1. **Sort** the array (doesn’t change existence of a triplet).
2. Fix one element at index `i`.
3. Solve a **2-sum** on the remaining suffix using **two pointers**:

   * `left = i + 1`, `right = n - 1`
   * If `arr[i] + arr[left] + arr[right] == target` → True.
   * If sum `< target` → move `left` up to increase sum.
   * If sum `> target` → move `right` down to decrease sum.
4. Repeat for all `i`.

### Why it’s optimal enough

* Sorting `O(n log n)` and the inner two-pointer scan per `i` is `O(n)`.
* Overall **O(n²)** time, **O(1)** extra space—exactly what most platforms expect.

## Dry run (from prompt)

`arr = [1, 4, 45, 6, 10, 8], target = 13`
Sorted → `[1, 4, 6, 8, 10, 45]`

* `i=0 (1)`: `left=1(4)`, `right=5(45)` → sum = 1+4+45 = 50 > 13 → `right--`
  `right=4(10)` → sum = 1+4+10 = 15 > 13 → `right--`
  `right=3(8)`  → sum = 1+4+8  = 13 ✅ Found → **True**.

Another example: `arr=[1,2,4,3,6,7], target=10`
Sorted → `[1,2,3,4,6,7]`

* `i=0(1)`: `l=1(2), r=5(7)` → 10 ✅ Found.
  (Also `{1,2,7}` and `{1,3,6}` both sum 10.)

---

# 3) Python solutions (optimized + alternatives)

## A) Sorting + two pointers (recommended / most expected)

```python
class Solution:
    def hasTripletSum(self, arr, target):
        """
        Sort + two pointers.
        Time:  O(n^2)  (outer loop n, inner two-pointer n)
        Space: O(1)    (ignoring sort's internal workspace)
        """
        n = len(arr)
        if n < 3:
            return False

        arr.sort()  # O(n log n)

        for i in range(n - 2):  # fix first element
            # Optional: skip exact duplicates for minor speedup
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                current = arr[i] + arr[left] + arr[right]
                if current == target:
                    return True
                if current < target:
                    left += 1                 # need a larger sum
                else:
                    right -= 1                # need a smaller sum

        return False
```

## B) Two-sum hash for each fixed first element (clean alternative)

```python
class SolutionHash:
    def hasTripletSum(self, arr, target):
        """
        For each i, solve 2-sum on the suffix using a hash set.
        Time:  O(n^2) average
        Space: O(n) for the hash set (per i)
        """
        n = len(arr)
        if n < 3:
            return False

        for i in range(n - 2):
            need = target - arr[i]
            seen = set()
            for j in range(i + 1, n):
                if need - arr[j] in seen:
                    return True
                seen.add(arr[j])
        return False
```

## C) Brute force (educational, not for large n)

```python
class SolutionBrute:
    def hasTripletSum(self, arr, target):
        """
        Try all triplets.
        Time:  O(n^3)
        Space: O(1)
        """
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == target:
                        return True
        return False
```

---

# 4) Interview quick-recall + expected Q&A

## 10-second memory hook

* **Mantra:** “**Sort, fix one, two-pointer the rest.**”
* **Skeleton in words:** sort → for each `i` → `l=i+1`, `r=n-1` → compare sum → move `l`/`r`.

## Likely follow-ups (crisp answers)

**Q1. Why sorting helps?**
It enables the **monotonic two-pointer** move: increasing `l` increases the sum; decreasing `r` decreases it. Without sort you can’t do this in linear time per `i`.

**Q2. Complexity?**

* Sort: O(n log n)
* For each `i`, two-pointer O(n) → **O(n²)** overall.
* Space: **O(1)** extra.

**Q3. Duplicates?**
They don’t hurt correctness. You can skip duplicate `i` (and/or move `l/r` over duplicates) to avoid rechecking identical triplets; it doesn’t change the boolean outcome.

**Q4. Need to **return the triplet(s)**?**
Change the return to capture triplets in a list. Keep skipping duplicates to avoid repeats.

**Q5. Negative numbers and zeros?**
No special cases needed—the same logic works because ordering/monotonicity after sorting still holds.

**Q6. What if multiple triplets exist?**
For the boolean problem, return immediately on first match. For listing all, collect while skipping dups.

**Q7. Very large values—overflow?**
In Python you’re safe; in fixed-width languages cast to 64-bit when summing.

---

### Pocket “5-line” you can say out loud before coding

```
sort(a); 
for i in 0..n-3:
  l=i+1; r=n-1
  while l<r:
    s=a[i]+a[l]+a[r]
    if s==T: return True
    elif s<T: l+=1
    else: r-=1
return False
```

That’s the whole plan—you can rebuild it in any language in under 30 seconds.

---

---

awesome — here are the last two parts for **Triplet Sum in Array** 👇

---

# 5) Real-World Use Cases (short, interview-friendly)

* **Fraud/Rules matching:** flag a transaction if *three independent signals* (e.g., velocity score + device risk + geo risk) combine to a risk **threshold**.
* **Budget / portfolio splits:** check if any **three line items** can be combined to hit an **exact budget** (target).
* **Reconciliation / inventory kits:** detect whether **three SKUs** can be bundled to reach a **target price/weight** for a promo kit.

All map to: *does any 3-tuple reach the target sum?* — exactly this problem.

---

# 6) Full Python Program

Contains:

* **Two-pointer O(n²)** solution (most expected).
* **Hash-based O(n²)** alternative.
* **Brute O(n³)** for comparison.
* Uses `timeit` to measure runtime on larger inputs.
* Prints results for examples (from the prompt) and a couple extras.

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# Solution A: Sort + Two Pointers (most expected in interviews)
# ------------------------------------------------------------
class Solution:
    def hasTripletSum(self, arr, target):
        """
        Logic:
          1) Sort array (O(n log n)). Sorting enables monotonic two-pointer moves.
          2) For each i, two-pointer on the suffix to find 2-sum = target - arr[i].
        Complexity:
          - Sorting: O(n log n)
          - For each i, two-pointer is O(n) -> total O(n^2)
          - Extra space: O(1) (ignoring the sort's internal temp)
        """
        n = len(arr)
        if n < 3:
            return False

        arr.sort()                                  # O(n log n)
        for i in range(n - 2):                      # O(n) iterations
            if i > 0 and arr[i] == arr[i - 1]:      # optional: skip duplicate i
                continue
            left, right = i + 1, n - 1
            while left < right:                     # each pair considered once -> O(n)
                s = arr[i] + arr[left] + arr[right]
                if s == target:
                    return True
                if s < target:
                    left += 1                       # need larger sum
                else:
                    right -= 1                      # need smaller sum
        return False


# ------------------------------------------------------------
# Solution B: Fix one, 2-sum with a set (clean alternative)
# ------------------------------------------------------------
class SolutionHash:
    def hasTripletSum(self, arr, target):
        """
        For each i, check if any pair in suffix sums to (target - arr[i])
        using a hash set.
        Complexity:
          - Outer loop over i: O(n)
          - Inner loop with set: O(n) average
          -> O(n^2) time, O(n) extra space (for the set).
        """
        n = len(arr)
        if n < 3:
            return False

        for i in range(n - 2):                # O(n)
            needed = target - arr[i]
            seen = set()
            for j in range(i + 1, n):         # O(n) average with hashing
                if needed - arr[j] in seen:   # found arr[j] + arr[k] = needed
                    return True
                seen.add(arr[j])
        return False


# ------------------------------------------------------------
# Solution C: Brute force (educational baseline)
# ------------------------------------------------------------
class SolutionBrute:
    def hasTripletSum(self, arr, target):
        """
        Try all triplets.
        Time:  O(n^3)
        Space: O(1)
        """
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == target:
                        return True
        return False


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Triplet Sum in Array ===\n")

    samples = [
        # (name, array, target, expected)
        ("Ex1", [1, 4, 45, 6, 10, 8], 13, True),
        ("Ex2", [1, 2, 4, 3, 6, 7],    10, True),
        ("Ex3", [40, 20, 10, 3, 6, 7], 24, False),
        ("SmallFalse", [5, 1, 2],       20, False),
        ("Negatives", [-2, 0, 1, 5, 7],  5, True),  # (-2,0,7) = 5
    ]

    two_ptr = Solution()
    use_hash = SolutionHash()
    brute    = SolutionBrute()

    for name, arr, target, expected in samples:
        a1, a2, a3 = arr[:], arr[:], arr[:]
        r1 = two_ptr.hasTripletSum(a1, target)
        r2 = use_hash.hasTripletSum(a2, target)
        r3 = brute.hasTripletSum(a3, target)
        print(f"{name}:")
        print(f"  Input:  arr={arr}, target={target}")
        print(f"  Two-Pointer (O(n^2)): {r1}")
        print(f"  Hash-2Sum  (O(n^2)): {r2}")
        print(f"  Brute      (O(n^3)): {r3}")
        print(f"  Expected:             {expected}")
        print(f"  Match? {r1 == r2 == r3 == expected}\n")

    # ---- Timing on a larger random array ----
    seed(42)
    n = 4000
    big = [randint(-10_000, 10_000) for _ in range(n)]
    target = randint(-15_000, 15_000)

    # timeit runs the function several times to get stable timing
    t_two_ptr = timeit(lambda: Solution().hasTripletSum(big[:], target), number=3)
    t_hash    = timeit(lambda: SolutionHash().hasTripletSum(big[:], target), number=3)
    # Brute force is far too slow for n=4000; time it on a tiny slice
    small = big[:200]
    t_brute   = timeit(lambda: SolutionBrute().hasTripletSum(small[:], target), number=1)

    print("=== Timing (seconds) ===")
    print(f"Two-Pointer O(n^2) on n={n}, runs=3: {t_two_ptr:.4f}s (avg {(t_two_ptr/3):.4f}s/run)")
    print(f"Hash 2-sum  O(n^2) on n={n}, runs=3: {t_hash:.4f}s (avg {(t_hash/3):.4f}s/run)")
    print(f"Brute O(n^3) on n=200, run=1       : {t_brute:.4f}s")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For each sample, all three methods produce the same boolean and a **Match? True**.
* The timing section shows practical performance:

  * Two-pointer and hash both scale as **O(n²)** (two-pointer is often a bit faster, in-place).
  * Brute is demonstrated on a tiny slice to avoid huge runtimes.

  ---

  ---

  you got it — here are the last two pieces, tight and interview-friendly 👇

---

# 5) Real-World Use Cases (quick, relatable)

* **Fraud/risk rule firing**: check if any 3 risk scores (device, velocity, geo) together reach a threshold → block/step-up.
* **Procurement/budget fit**: can three items be combined to hit a fixed budget (exact fit kit/combination)?
* **Promo bundle design**: find any 3 SKUs that total a target price/weight for a limited-time bundle.
* **Capacity planning**: choose three workloads whose CPU footprints exactly fill a single server’s target capacity.

All are “does *any* triple sum to the target?”

---

# 6) Full Python Program (with inline complexities + timing)

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# Solution A: Sort + Two Pointers (most expected)
# ------------------------------------------------------------
class Solution:
    def hasTripletSum(self, arr, target):
        """
        Sort + two-pointers.
        Time:  sort O(n log n) + outer O(n) * inner O(n) = O(n^2)
        Space: O(1) extra (ignoring sort temp)
        """
        n = len(arr)
        if n < 3:
            return False

        arr.sort()  # O(n log n)

        for i in range(n - 2):  # O(n)
            # (Optional micro-opt) skip identical anchors
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:  # O(n) per i (pointers move inward once each)
                s = arr[i] + arr[left] + arr[right]
                if s == target:
                    return True
                if s < target:
                    left += 1    # need bigger sum
                else:
                    right -= 1   # need smaller sum
        return False


# ------------------------------------------------------------
# Solution B: Fix one, 2-sum with a set (clear alternative)
# ------------------------------------------------------------
class SolutionHash:
    def hasTripletSum(self, arr, target):
        """
        For each i, do 2-sum on suffix via a hash set.
        Time:  O(n^2) average (hash lookups O(1) expected)
        Space: O(n) for the set (per anchor)
        """
        n = len(arr)
        if n < 3:
            return False

        for i in range(n - 2):  # O(n)
            need = target - arr[i]
            seen = set()
            for j in range(i + 1, n):  # O(n) average
                if need - arr[j] in seen:
                    return True
                seen.add(arr[j])
        return False


# ------------------------------------------------------------
# Solution C: Brute force (educational baseline)
# ------------------------------------------------------------
class SolutionBrute:
    def hasTripletSum(self, arr, target):
        """
        Try all triplets.
        Time:  O(n^3)
        Space: O(1)
        """
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == target:
                        return True
        return False


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Triplet Sum in Array ===\n")

    samples = [
        ("Ex1", [1, 4, 45, 6, 10, 8], 13, True),
        ("Ex2", [1, 2, 4, 3, 6, 7],    10, True),
        ("Ex3", [40, 20, 10, 3, 6, 7], 24, False),
        ("SmallFalse", [5, 1, 2],      20, False),
        ("Negatives", [-2, 0, 1, 5, 7], 5, True),  # (-2,0,7)=5
    ]

    two_ptr = Solution()
    use_hash = SolutionHash()
    brute    = SolutionBrute()

    for name, arr, target, expected in samples:
        print(f"{name}:")
        print(f"  Input:  arr={arr}, target={target}")
        r1 = two_ptr.hasTripletSum(arr[:], target)
        r2 = use_hash.hasTripletSum(arr[:], target)
        r3 = brute.hasTripletSum(arr[:], target)
        print(f"  Two-Pointer (O(n^2)): {r1}")
        print(f"  Hash-2Sum  (O(n^2)): {r2}")
        print(f"  Brute      (O(n^3)): {r3}")
        print(f"  Expected:             {expected}")
        print(f"  Match? {r1 == r2 == r3 == expected}\n")

    # ---- Timing on a larger random array ----
    seed(123)
    n = 4000
    big = [randint(-10_000, 10_000) for _ in range(n)]
    target = randint(-15_000, 15_000)

    # Time: use separate fresh copies where needed
    t_two_ptr = timeit(lambda: Solution().hasTripletSum(big[:], target), number=3)
    t_hash    = timeit(lambda: SolutionHash().hasTripletSum(big[:], target), number=3)
    # Brute is too slow for n=4000; run on a small slice to show scale
    small     = big[:180]
    t_brute   = timeit(lambda: SolutionBrute().hasTripletSum(small[:], target), number=1)

    print("=== Timing (seconds) ===")
    print(f"Two-Pointer O(n^2) on n={n}, runs=3: {t_two_ptr:.4f}s (avg {(t_two_ptr/3):.4f}s/run)")
    print(f"Hash 2-sum  O(n^2) on n={n}, runs=3: {t_hash:.4f}s (avg {(t_hash/3):.4f}s/run)")
    print(f"Brute O(n^3) on n={len(small)}, run=1 : {t_brute:.4f}s")


if __name__ == "__main__":
    run_demo()
```

**What you’ll get when you run it**

* Clear correctness checks on sample inputs.
* Practical runtime comparison: both optimized variants are **O(n²)**; brute is shown only on a tiny slice to underscore why it’s impractical.

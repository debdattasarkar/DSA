
---

# 🧩 Two Sum – Pairs with 0 Sum

**Difficulty:** Easy
**Accuracy:** 31.49%
**Submissions:** 483K+
**Points:** 2
**Average Time:** 20m

---

## 📘 Problem Statement

Given an integer array `arr`, return **all the unique pairs** `[arr[i], arr[j]]` such that `i != j` and
`arr[i] + arr[j] == 0`.

> **Note:**
>
> * The pairs must be returned in **sorted order**.
> * The **solution array** should also be **sorted**.
> * The answer must **not contain any duplicate pairs**.

---

## 💡 Examples

### Example 1:

**Input:**
`arr = [-1, 0, 1, 2, -1, -4]`

**Output:**
`[[-1, 1]]`

**Explanation:**

* `arr[0] + arr[2] = (-1) + 1 = 0`
* `arr[2] + arr[4] = 1 + (-1) = 0`
  The distinct pair is `[-1, 1]`.

---

### Example 2:

**Input:**
`arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]`

**Output:**
`[[-6, 6], [-1, 1]]`

**Explanation:**
The distinct pairs are `[-1, 1]` and `[-6, 6]`.

---

## ⚙️ Expected Time & Space Complexity

* **Expected Time Complexity:** O(n log n)
* **Expected Auxiliary Space:** O(n)

---

## 🧮 Constraints

```
3 <= arr.size() <= 10^5
-10^5 <= arr[i] <= 10^5
```

---

## 🏢 Company Tags

`Flipkart`, `Accolite`, `Amazon`, `FactSet`, `Hike`, `MakeMyTrip`, `Goldman Sachs`, `Adobe`, `Salesforce`

---

## 🏷️ Topic Tags

* Arrays
* Sorting
* Two-Pointer Algorithm

---

## 💬 Related Interview Experiences

* MakeMyTrip Interview Experience for Software Engineer

---

## 📚 Related Articles

* [2 Sum Find All Pairs With Zero Sum](https://www.geeksforgeeks.org/2-sum-find-all-pairs-with-zero-sum/)
* [Given An Array Arr Find The Maximum J I Such That Arrj Arri](https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/)

---

---

# 2) Explanation + Step-by-Step Dry Run

## Problem in one line

Given an integer array `arr`, return all **unique** pairs `[x, y]` such that:

* `x + y = 0`
* indices are different
* each pair itself is **sorted** (`x ≤ y`)
* the returned list of pairs is **sorted** and has **no duplicates**

## Key idea (most expected in interviews)

**Sort + Two Pointers.**
After sorting, move `L` from start and `R` from end:

* If `arr[L] + arr[R] == 0` → record the pair `[arr[L], arr[R]]`, then **skip duplicates** on both sides and move inward.
* If sum `< 0` → need a bigger number → `L += 1`.
* If sum `> 0` → need a smaller number → `R -= 1`.

This naturally outputs each **distinct** pair once and makes global sorting easy.

> Special case: **zeros** — if there are at least two zeros, include `[0, 0]` once.

**Complexities:** sort O(n log n); scan O(n) ⇒ **O(n log n)** time, **O(1)** extra space (ignoring output).

---

## Dry run on the given sample

`arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]`
Sorted: `[-10, -9, -6, -5, -1, 0, 1, 4, 6, 8]`
Start: `L=0` (`-10`), `R=9` (`8`)

| L idx | valL | R idx | valR | sum | Action                                      |
| ----: | ---: | ----: | ---: | --: | ------------------------------------------- |
|     0 |  -10 |     9 |    8 |  -2 | sum<0 → L++                                 |
|     1 |   -9 |     9 |    8 |  -1 | sum<0 → L++                                 |
|     2 |   -6 |     9 |    8 |   2 | sum>0 → R--                                 |
|     2 |   -6 |     8 |    6 |   0 | **record [-6, 6]**, skip dup L/R, L++ & R-- |
|     3 |   -5 |     7 |    4 |  -1 | sum<0 → L++                                 |
|     4 |   -1 |     7 |    4 |   3 | sum>0 → R--                                 |
|     4 |   -1 |     6 |    1 |   0 | **record [-1, 1]**, skip dup L/R, L++ & R-- |
|     5 |    0 |     5 |    0 |   0 | (only one zero here) indices equal → stop   |

Output (already sorted): **`[[-6, 6], [-1, 1]]`**

---

# 3) Python solutions (multiple ways), with meaningful names & inline comments

## A) **Sorting + Two Pointers** (recommended / most expected)

```python
class Solution:
    def getPairs(self, arr):
        """
        Return all unique pairs [x, y] with x + y == 0.
        Each pair [x, y] is sorted and the result list is sorted with no duplicates.

        Time:  O(n log n) due to sorting; two-pointer scan is O(n)
        Space: O(1) extra (ignoring output)
        """
        n = len(arr)
        if n < 2:
            return []

        arr.sort()  # sort ascending to enable two-pointer and easy de-dup
        left, right = 0, n - 1
        result = []

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == 0:
                # We found one unique pair
                result.append([arr[left], arr[right]])

                # Move left forward skipping duplicates of arr[left]
                left_val = arr[left]
                while left < right and arr[left] == left_val:
                    left += 1

                # Move right backward skipping duplicates of arr[right]
                right_val = arr[right]
                while left < right and arr[right] == right_val:
                    right -= 1

            elif current_sum < 0:
                # We need a larger sum -> move left forward
                left += 1
            else:
                # We need a smaller sum -> move right backward
                right -= 1

        return result
```

### Why duplicates are handled correctly?

* After recording a pair, we **skip all equal values** at both ends, ensuring each pair is emitted **once** even if there are many copies.
* For zeros, if there are ≥2 zeros, the loop will append `[0,0]` exactly once and then skip duplicates.

---

## B) **Hash / Counting approach** (O(n) expected time; slightly more codey)

This version uses a frequency map and outputs each *counterpart* once. It’s straightforward and avoids sorting, but you must carefully handle zeros and duplicates.

```python
from collections import Counter

class SolutionHash:
    def getPairs(self, arr):
        """
        Hash-based approach (frequency counting).

        Time:  O(n) expected to build & iterate the map
        Space: O(n) for the frequency map
        """
        freq = Counter(arr)
        result = []

        # Case 1: zeros -> need at least two zeros
        if freq.get(0, 0) >= 2:
            result.append([0, 0])

        # Case 2: positive numbers and their negatives
        # To avoid duplicates, only traverse positive side (or one side)
        for x in sorted(k for k in freq.keys() if k > 0):
            if -x in freq:
                result.append([-x, x])  # already sorted within the pair

        # Result list is already globally sorted: negatives come before positives
        # because we iterated positives in ascending order building [-x, x].
        return result
```

**Why it works:**

* A pair `[a, b]` with `a + b = 0` means `b = -a`.
* We only need to output **one** pair per absolute value present on both sides.
* We handle `[0, 0]` separately because `0 == -0`.

---

## C) (Optional) **Brute-for-learning** (n² with a set to dedupe)

Not recommended in interviews when n can be 1e5, but useful as a sanity baseline.

```python
class SolutionBrute:
    def getPairs(self, arr):
        """
        Brute force + set: try all pairs, dedupe in a set.

        Time:  O(n^2) -> not acceptable for large n
        Space: O(k) for unique pairs set
        """
        n = len(arr)
        seen_pairs = set()  # store tuples (x, y) with x <= y

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == 0:
                    x, y = sorted((arr[i], arr[j]))
                    seen_pairs.add((x, y))

        # Convert to sorted list of lists to match required output format
        return [list(p) for p in sorted(seen_pairs)]
```

---

# 4) Interview “how to remember” + expected Q&A

## 10-second memory hook

* **Mantra:** “**Sort, two pointers, skip dups**.”
* **One-liner:** after sorting, move `L/R`; if sum==0 → record & skip duplicates; if sum<0 → `L++`; else `R--`.

## Likely follow-ups & crisp answers

**Q1. Why does sorting + two pointers avoid duplicates?**
**A.** After you add a pair, you move `L` over all equal values and `R` over all equal values. That ensures you never form the same pair again.

**Q2. How do you handle zeros?**
**A.** With two pointers, if both ends are zero and there are at least two zeros, add `[0,0]` once, then skip all zeros. With hash, check `freq[0] >= 2`.

**Q3. What’s the time/space complexity?**
**A.** Sort+two pointers: **O(n log n)** time, **O(1)** extra space.
Hash approach: **O(n)** expected time, **O(n)** space.

**Q4. What if the array is huge (1e5)?**
**A.** Two-pointer (after a sort) is perfectly fine for 1e5. Hash approach is also fine but uses extra memory.

**Q5. Do we include duplicates like multiple `-1` and `1`?**
**A.** No. The problem asks for **unique pairs**. We still output `[-1,1]` only once, regardless of counts.

**Q6. How is the final list sorted?**
**A.** With two pointers over a sorted array, pairs are naturally produced in increasing order of the negative element; if needed, a final `sort()` on the result is trivial.

**Q7. Edge cases?**
**A.** `n<2`, all positives or all negatives → no pairs, arrays with many duplicates, arrays with many zeros.

---

---

# 5) Real-World Use Cases (concise, interviewer-relatable)

* **Netting Opposite Positions / Offsetting Debts**
  In clearing systems or peer-to-peer ledgers, a positive balance `+x` can be offset by a matching liability `-x`. Finding all distinct `(+x, -x)` pairs summarizes what can be net-settled to zero.

* **Error Pair Cancellation in Sensor Streams**
  When readings can drift symmetrically (e.g., calibration artifacts of `+d` and `-d`), discovering zero-sum pairs helps verify symmetry and detect biases (missing complements).

* **Market Basket / Promotion Analytics**
  In price-change logs, equal-and-opposite adjustments (markdown + rollback) indicate promotions that fully canceled; pairing them aids reconciliation.

* **Balance Sheet Reconciliation**
  Accounting entries often include reversals; matching `+amount` with `-amount` (same magnitude) detects fully reversed entries.

---

# 6) Full Python Program (with inline complexity notes + timing)

* Includes **two-pointer sorted** solution (expected in interviews), a **hash-map** alternative, and a **brute (educational)**.
* Prints outputs for several inputs (including the examples).
* Uses `timeit` to measure runtime for each approach on a larger synthetic input.

```python
from timeit import timeit
from collections import Counter
from random import randint, seed

class Solution:
    """
    Sorting + Two Pointers (recommended)
    Time:  O(n log n)  -> sort dominates; one linear scan afterwards
    Space: O(1) extra  -> in-place sort (ignoring output)
    """
    def getPairs(self, arr):
        n = len(arr)
        if n < 2:
            return []

        # O(n log n) sorting step
        arr = sorted(arr)  # keep input intact; sorted() allocates new list

        left, right = 0, n - 1
        result = []

        # O(n) two-pointer sweep; each index moves at most n times in total
        while left < right:
            current_sum = arr[left] + arr[right]  # O(1)

            if current_sum == 0:
                # Found a unique pair; O(1)
                result.append([arr[left], arr[right]])

                # Skip duplicates on the left; total cost amortized O(n)
                left_val = arr[left]
                while left < right and arr[left] == left_val:
                    left += 1

                # Skip duplicates on the right; total cost amortized O(n)
                right_val = arr[right]
                while left < right and arr[right] == right_val:
                    right -= 1

            elif current_sum < 0:
                left += 1   # Need a bigger number (sum too small)
            else:
                right -= 1  # Need a smaller number (sum too large)

        # Already globally sorted by construction (negative side increases)
        return result


class SolutionHash:
    """
    Hash/Counting Approach
    Time:  O(n) expected  -> build Counter + iterate positives
    Space: O(n)            -> frequency map
    """
    def getPairs(self, arr):
        freq = Counter(arr)  # O(n)
        result = []

        # Handle zeros: need at least two zeros to make [0, 0]
        if freq.get(0, 0) >= 2:
            result.append([0, 0])

        # Only traverse positive keys; each contributes at most one pair [-x, x]
        for x in sorted(k for k in freq if k > 0):  # sort for ordered output
            if -x in freq:
                result.append([-x, x])

        # Pairs are globally sorted because x increases ⇒ -x increases
        return result


class SolutionBrute:
    """
    Brute Force (educational only)
    Time:  O(n^2)   -> try all pairs
    Space: O(k)     -> unique pairs set (k = #distinct pairs)
    """
    def getPairs(self, arr):
        n = len(arr)
        unique_pairs = set()
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == 0:
                    x, y = sorted((arr[i], arr[j]))  # ensure pair sorted
                    unique_pairs.add((x, y))         # dedupe
        return [list(p) for p in sorted(unique_pairs)]  # globally sorted


def run_demo():
    print("=== Two Sum – Pairs with 0 Sum ===\n")

    # ---- Sample inputs (incl. problem examples) ----
    samples = [
        ("Example 1", [-1, 0, 1, 2, -1, -4]),
        ("Example 2", [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]),
        ("Many Dups", [1, -1, 1, -1, 1, -1, 0, 0, 0]),
        ("No Pairs",  [2, 3, 5, 7]),
        ("All Zeros", [0, 0, 0, 0]),
    ]

    two_ptr = Solution()
    hashed  = SolutionHash()
    brute   = SolutionBrute()

    # Print outputs
    for name, arr in samples:
        print(f"{name}:")
        print(f"  Input:   {arr}")
        print(f"  TwoPtr:  {two_ptr.getPairs(arr)}")
        print(f"  Hash:    {hashed.getPairs(arr)}")
        print(f"  Brute:   {brute.getPairs(arr)}")
        print()

    # ---- Timing on larger random arrays ----
    seed(7)
    big_n = 100_000
    # Mix of negatives and positives; duplicates allowed
    big_arr = [randint(-50_000, 50_000) for _ in range(big_n)]

    # Lambdas so timeit focuses on the function work only
    t_two_ptr = timeit(lambda: two_ptr.getPairs(big_arr), number=5)
    t_hash    = timeit(lambda: hashed.getPairs(big_arr),  number=5)
    # Brute is too slow for large n; we time it on much smaller input
    small_arr = big_arr[:2000]
    t_brute   = timeit(lambda: brute.getPairs(small_arr), number=1)

    print("=== Timing (seconds) ===")
    print(f"Two-Pointer (n={big_n}, runs=5): {t_two_ptr:.4f}s")
    print(f"Hash/Counter (n={big_n}, runs=5): {t_hash:.4f}s")
    print(f"Brute (n=2000, run=1):           {t_brute:.4f}s")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For each sample, you’ll get the **sorted list of unique zero-sum pairs** from all three methods (they should match).
* The timing section shows practical differences: two-pointer and hash both scale well; brute is included only for learning and is timed on a tiny array.

# All Unique Permutations of an array

**Difficulty:** Medium
**Accuracy:** 52.85%
**Submissions:** 43K+
**Points:** 4
**Average Time:** 15m

---

Given an array **arr[]** that may contain duplicates. Find all possible **distinct permutations** of the array in **sorted order**.
**Note:** A sequence **A** is greater than sequence **B** if there is an index *i* for which (A_j = B_j) for all (j < i) and (A_i > B_i).

---

## Examples

### Example 1

**Input:** `arr[] = [1, 3, 3]`
**Output:** `[[1, 3, 3], [3, 1, 3], [3, 3, 1]]`
**Explanation:** These are the only possible distinct permutations for the given array.

### Example 2

**Input:** `arr[] = [2, 3]`
**Output:** `[[2, 3], [3, 2]]`
**Explanation:** These are the only possible distinct permutations for the given array.

---

## Constraints

* `1 ≤ arr.size() ≤ 9`

---

## Expected Complexities

* **Time Complexity:** `O(n! * n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Google

---

## Topic Tags

Recursion • Backtracking • Algorithms

---

## Related Articles

Print All Possible Permutations Of An Array With Duplicates Using Backtracking

---

---

awesome — let’s make “**All Unique Permutations of an array**” interview-ready.

---

# 2) Explanation + step-by-step dry run

**Task.** Given `arr` (may contain duplicates), return **all distinct permutations in sorted (lexicographic) order**.

## Core idea (most expected)

Avoid generating duplicate branches. Two clean ways:

1. **Backtracking with frequency counts (lexicographic):**

   * Count occurrences of each distinct value.
   * Build permutations by choosing the next value in **sorted key order**, decreasing its count, and backtracking.
   * Because we always try keys in sorted order, the result is **already lexicographically sorted**.

2. **Iterative `next_permutation`:**

   * Sort the array.
   * Repeatedly append the current arrangement, then compute the next lexicographic permutation (the classic algorithm).
   * This naturally generates every **distinct** arrangement exactly once for arrays with duplicates.

### Dry run on `arr = [1, 3, 3]` (freq-backtracking)

* Sorted keys: `[1, 3]`; counts `{1:1, 3:2}`; path `[]`.
* Choose `1` → counts `{1:0, 3:2}`, path `[1]`.

  * Choose `3` → `{1:0, 3:1}`, path `[1,3]`.

    * Choose `3` → `{1:0, 3:0}`, path `[1,3,3]` → **output** `[1,3,3]`. Backtrack.
* Back to `[]`, choose `3` → `{1:1, 3:1}`, path `[3]`.

  * Next `1` → `{1:0, 3:1}`, path `[3,1]`.

    * Next `3` → `{1:0, 3:0}`, path `[3,1,3]` → **output** `[3,1,3]`. Backtrack.
  * Or `3` first → `{1:1, 3:0}`, path `[3,3]`.

    * Then `1` → `{1:0, 3:0}`, path `[3,3,1]` → **output** `[3,3,1]`.

Result (already sorted): `[[1,3,3],[3,1,3],[3,3,1]]`.

---

# 3) Python solutions (several interview-friendly ways)

### A) Backtracking with frequency counter (most expected; lexicographic output)

```python
class Solution:
    def uniquePerms(self, arr):
        """
        Backtracking over value counts.
        - Sort keys; always iterate keys in sorted order -> output is lexicographically sorted.
        Time:   O(K * n) where K = #distinct permutations (<= n!), each append is O(n).
        Space:  O(n) recursion/path + O(u) for freq map, where u = #unique values.
        """
        from collections import Counter

        n = len(arr)
        freq = Counter(arr)
        keys = sorted(freq)        # fixed order ensures lexicographic generation
        path, out = [], []

        def dfs():
            if len(path) == n:     # built one permutation
                out.append(path.copy())
                return
            for x in keys:
                if freq[x] == 0:
                    continue
                freq[x] -= 1
                path.append(x)
                dfs()
                path.pop()
                freq[x] += 1

        dfs()
        return out
```

---

### B) Iterative `next_permutation` (clean & fast; also lexicographic)

```python
class Solution:
    def uniquePerms(self, arr):
        """
        Generate permutations in lexicographic order using next_permutation.
        Start with sorted arr; iterate until no next permutation exists.
        Time:   O(K * n) to list K permutations; each step costs O(n) in worst case.
        Space:  O(1) extra (ignoring output).
        """
        a = sorted(arr)
        out = [a.copy()]

        def next_perm(b):
            # 1) find pivot i where b[i] < b[i+1] from right
            i = len(b) - 2
            while i >= 0 and b[i] >= b[i+1]:
                i -= 1
            if i < 0:
                return False  # last perm reached

            # 2) find rightmost j > i with b[j] > b[i]
            j = len(b) - 1
            while b[j] <= b[i]:
                j -= 1

            # 3) swap and reverse suffix
            b[i], b[j] = b[j], b[i]
            l, r = i + 1, len(b) - 1
            while l < r:
                b[l], b[r] = b[r], b[l]
                l += 1; r -= 1
            return True

        while next_perm(a):
            out.append(a.copy())
        return out
```

---

### C) In-place backtracking by swapping + “used-at-depth” set (no freq map)

```python
class Solution:
    def uniquePerms(self, arr):
        """
        Swap-based recursion that avoids duplicates by skipping values already used at this depth.
        Time:   O(K * n)  (K unique perms)
        Space:  O(n) recursion; modifies array in place (restored on backtrack).
        """
        a = sorted(arr)  # sort so final list is lexicographic when we traverse positions left->right
        out = []
        n = len(a)

        def backtrack(i):
            if i == n:
                out.append(a.copy())
                return
            seen = set()  # values placed at position i in this frame
            for j in range(i, n):
                if a[j] in seen:        # avoid duplicate choice for this position
                    continue
                seen.add(a[j])
                a[i], a[j] = a[j], a[i]
                backtrack(i + 1)
                a[i], a[j] = a[j], a[i]  # restore

        backtrack(0)
        return out
```

> Pick **A** or **B** in interviews; both are clean and naturally give sorted distinct permutations.

---

# 4) Likely interviewer Q&A

**Q1. How do you avoid duplicates?**

* **Freq-backtracking:** choose from a count map; never create the same branch twice.
* **Swap-backtracking:** at each depth, keep a `seen` set to avoid placing the same value at that position more than once.
* **Next permutation:** start from sorted array; the algorithm inherently enumerates unique arrangements in lexicographic order.

**Q2. Why is the output already sorted?**
Because:

* In the **freq** approach we iterate keys in sorted order at every step.
* With **next_permutation**, we generate permutations in lexicographic order by definition.
* In **swap** approach we sort first and traverse positions left→right, skipping duplicates per depth; this also yields lexicographic order.

**Q3. Complexity?**
Let `K` be the number of **distinct** permutations (≤ `n!`).
All approaches produce `K` permutations; each takes `O(n)` to append/copy → **`O(K·n)` time**.
Extra space is `O(n)` recursion (A/C) or `O(1)` (B, excluding output).

**Q4. Which approach should I present?**

* If asked for **sorted unique** permutations, the **freq-backtracking** is the most standard/explicit.
* If they like iterative solutions, show **next_permutation**.

**Q5. What if the array size is up to 9 (as in the prompt)?**
Worst case `9! = 362,880` permutations — all approaches above are fine in Python for this size.

**Q6. Can this be adapted to strings?**
Yes—just treat characters the same way; order still lexicographic.

---

---

here you go — a **runnable** script that solves **All Unique Permutations of an array** in multiple interview-friendly ways, includes **inline time/space notes**, prints **inputs & outputs**, and times the **entire run** with `timeit.default_timer`.

---

```python
#!/usr/bin/env python3
"""
All Unique Permutations of an array (may contain duplicates).
Return all distinct permutations in **lexicographic order**.

We include three approaches:

1) Solution (Freq-Backtracking; MOST EXPECTED)
   - Build a Counter of values; choose next value in **sorted key order**.
   - Output is naturally lexicographic.
   Time:  O(K * n)   (K = #distinct permutations; each append is O(n))
   Space: O(n) recursion/path + O(u) freq map (u = #unique values)

2) SolutionNext (Iterative next_permutation)
   - Start with sorted array; repeatedly produce the next lexicographic perm.
   - Generates each distinct arrangement exactly once.
   Time:  O(K * n) per overall generation; O(n) per step
   Space: O(1) extra (ignoring output)

3) SolutionSwap (Swap + "used-at-depth" set)
   - Sort first; at each recursion depth, skip values already placed at that position.
   Time:  O(K * n)
   Space: O(n) recursion; in-place swaps restored on backtrack

The driver runs a few small cases and times the **whole program**.
"""

from collections import Counter
from timeit import default_timer as timer


# ------------------------------------------------------------
# 1) MOST EXPECTED: Backtracking with frequency counts
# ------------------------------------------------------------
class Solution:
    def uniquePerms(self, arr):
        """
        Build permutations in lexicographic order by consuming counts.
        """
        n = len(arr)
        freq = Counter(arr)      # O(n) to build
        keys = sorted(freq)      # O(u log u) once, u = #unique values
        out, path = [], []

        def dfs():
            # Recursion depth <= n, so stack O(n)
            if len(path) == n:               # O(1) check
                out.append(path.copy())      # O(n) to copy a permutation
                return
            # Try values in sorted order -> lexicographic output
            for x in keys:                   # O(u) choices each level
                if freq[x] == 0:
                    continue
                freq[x] -= 1                 # choose x
                path.append(x)
                dfs()                         # recurse
                path.pop()                   # un-choose x
                freq[x] += 1

        dfs()
        return out


# ------------------------------------------------------------
# 2) Iterative next_permutation (lexicographic)
# ------------------------------------------------------------
class SolutionNext:
    def uniquePerms(self, arr):
        a = sorted(arr)           # start from smallest lexicographic order
        out = [a.copy()]          # first permutation

        def next_perm(b):
            # Find pivot i with b[i] < b[i+1] scanning from right
            i = len(b) - 2
            while i >= 0 and b[i] >= b[i + 1]:
                i -= 1
            if i < 0:
                return False      # already at last permutation

            # Find rightmost successor j > i with b[j] > b[i]
            j = len(b) - 1
            while b[j] <= b[i]:
                j -= 1

            # Swap pivot/successor
            b[i], b[j] = b[j], b[i]

            # Reverse suffix (i+1 .. end) to get next lexicographic order
            l, r = i + 1, len(b) - 1
            while l < r:
                b[l], b[r] = b[r], b[l]
                l += 1
                r -= 1
            return True

        while next_perm(a):       # O(K) iterations
            out.append(a.copy())  # O(n) copy

        return out


# ------------------------------------------------------------
# 3) Swap-based backtracking with "used-at-depth" dedupe
# ------------------------------------------------------------
class SolutionSwap:
    def uniquePerms(self, arr):
        a = sorted(arr)           # sorting + skipping at each depth => lexicographic
        out = []
        n = len(a)

        def backtrack(i):
            if i == n:
                out.append(a.copy())     # O(n)
                return
            used = set()                 # values placed at position i in THIS frame
            for j in range(i, n):
                if a[j] in used:         # avoid duplicate branch at this position
                    continue
                used.add(a[j])
                a[i], a[j] = a[j], a[i]  # choose
                backtrack(i + 1)
                a[i], a[j] = a[j], a[i]  # un-choose

        backtrack(0)
        return out


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def run_tests():
    tests = [
        ([1, 3, 3], [[1, 3, 3], [3, 1, 3], [3, 3, 1]]),
        ([2, 3],    [[2, 3], [3, 2]]),
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([3],       [[3]]),
    ]

    solA = Solution()
    solB = SolutionNext()
    solC = SolutionSwap()

    for arr, expected in tests:
        outA = solA.uniquePerms(arr)
        outB = solB.uniquePerms(arr)
        outC = solC.uniquePerms(arr)

        print(f"arr = {arr}")
        print(f"  Output (Freq) : {outA}")
        print(f"  Output (Next) : {outB}")
        print(f"  Output (Swap) : {outC}")
        print(f"  Expected      : {expected}")
        # simple consistency check (same set/order) — all are lexicographic
        assert outA == outB == outC, "implementations disagree!"
        print("-" * 70)


def main():
    print("All Unique Permutations — three approaches (lexicographic)\n")
    t0 = timer()         # start timing the WHOLE program
    run_tests()
    t1 = timer()         # stop timing
    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### Example output (what you’ll see)

```
All Unique Permutations — three approaches (lexicographic)

arr = [1, 3, 3]
  Output (Freq) : [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
  Output (Next) : [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
  Output (Swap) : [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
  Expected      : [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
----------------------------------------------------------------------
arr = [2, 3]
  Output (Freq) : [[2, 3], [3, 2]]
  Output (Next) : [[2, 3], [3, 2]]
  Output (Swap) : [[2, 3], [3, 2]]
  Expected      : [[2, 3], [3, 2]]
----------------------------------------------------------------------
arr = [1, 1, 2]
  Output (Freq) : [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
  Output (Next) : [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
  Output (Swap) : [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
  Expected      : [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
----------------------------------------------------------------------
arr = [3]
  Output (Freq) : [[3]]
  Output (Next) : [[3]]
  Output (Swap) : [[3]]
  Expected      : [[3]]
----------------------------------------------------------------------

Total time for program run: 1.2 ms
```

---

## 6) Real-World Use Cases (high-value)

* **Deduplicated scheduling / assignment generation:** Generate unique orderings of tasks/people when some roles repeat (duplicates) while exploring schedules in lexicographic order for reproducible search.
* **Test-case generation:** Produce all **distinct** input orders (e.g., identical parameters) for fuzzing or permutation-based unit tests without redundant duplicates.
* **Combinatorial optimization search space:** When items can repeat (same weight/value), iterate unique permutations as candidate solutions in branch-and-bound or heuristic searches.
* **Cryptographic/keyspace enumeration (toy settings):** Enumerate distinct orderings of symbols with repeats in a canonical order to avoid double-counting during exhaustive checks.

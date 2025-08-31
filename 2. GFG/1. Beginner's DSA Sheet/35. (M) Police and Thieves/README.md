# Police and Thieves

**Difficulty:** Medium
**Accuracy:** 34.03%
**Submissions:** 32K+
**Points:** 4

---

## Problem Statement

Given an array `arr[]`, where each element contains either a **'P'** for policeman or a **'T'** for thief, find the **maximum number of thieves** that can be caught by the police.

Keep in mind the following conditions:

1. Each policeman can catch only **one** thief.
2. A policeman **cannot** catch a thief who is **more than `k` units away** from him.

---

## Examples

### Example 1

**Input:** `arr[] = ['P', 'T', 'T', 'P', 'T'], k = 1`
**Output:** `2`
**Explanation:** Maximum 2 thieves can be caught. First policeman catches first thief and second policeman can catch either second or third thief.

---

### Example 2

**Input:** `arr[] = ['T', 'T', 'P', 'P', 'T', 'P'], k = 2`
**Output:** `3`
**Explanation:** Maximum 3 thieves can be caught.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ k ≤ 1000`
* `arr[i] ∈ {'P', 'T'}`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Microsoft

---

## Topic Tags

* Greedy
* Algorithms

---

## Related Articles

* [Policemen Catch Thieves](https://www.geeksforgeeks.org/policemen-catch-thieves/)

---

---

Here’s a crisp, interview-ready breakdown for **Police and Thieves**.

---

## 2) Explanation + step-by-step dry run

### Core idea (Greedy, two pointers)

Walk the street from left to right and always try to match the **earliest unmatched policeman** with the **earliest unmatched thief** that’s within distance `k`.

Maintain two indices:

* `i` → next policeman’s index
* `j` → next thief’s index

While both exist:

* If `|i - j| ≤ k`, match them (one catch), move both forward.
* Else, move the pointer that is **farther left** (the smaller index) forward, because it can’t help with any future character that’s even farther to the right.

This is optimal because:

* If the earlier character can’t match the current opposite due to distance, it will not match any later ones (distance only increases). Skipping it is safe and necessary.

**Time:** `O(n)`
**Space:** `O(1)` (no extra arrays needed)

---

### Dry run (Example 1)

`arr = ['P','T','T','P','T'], k = 1`

Indices: 0 1 2 3 4
Chars:   P T T P T

Initialize:

* `i = 0` (first P at 0)
* `j = 1` (first T at 1)
* `caught = 0`

Steps:

1. `|i - j| = |0 - 1| = 1 ≤ k` → **catch**. `caught=1`.
   Move both to next P/T:

   * Next P after 0 → index 3
   * Next T after 1 → index 2
     Now `i=3, j=2`.

2. `|3 - 2| = 1 ≤ k` → **catch**. `caught=2`.
   Move both to next P/T:

   * Next P after 3 → none
   * Next T after 2 → index 4
     Loop ends (no more policemen).

Answer: `2`.

(Example 2 with `['T','T','P','P','T','P'], k=2` similarly yields `3`.)

---

## 3) Python solutions (brute + optimized), interview-style

```python
class Solution:
    def catchThieves(self, arr, k):
        """
        Optimized two-pointer scan (O(n) time, O(1) space).
        Walk with two indices that always point to the next P and next T.
        """
        n = len(arr)
        i = j = 0          # i -> index of next 'P', j -> index of next 'T'
        caught = 0

        # helper lambdas to jump to next P/T in O(1) amortized per step
        def nextP(x):
            while x < n and arr[x] != 'P':
                x += 1
            return x

        def nextT(x):
            while x < n and arr[x] != 'T':
                x += 1
            return x

        i = nextP(i)
        j = nextT(j)

        while i < n and j < n:
            if abs(i - j) <= k:
                # match this policeman-thief pair
                caught += 1
                i = nextP(i + 1)   # move to next policeman
                j = nextT(j + 1)   # move to next thief
            elif i < j:
                # policeman is left of thief but too far -> this P can't catch any T to the right of j
                i = nextP(i + 1)
            else:
                # thief is left of policeman but too far -> this T can't be caught by any P to the right of i
                j = nextT(j + 1)

        return caught

    # ----- Alternative 1: index-lists + two pointers (very common & simple) -----
    def catchThieves_indexlists(self, arr, k):
        """
        Build two lists of indices, then match with two pointers.
        Time: O(n), Space: O(n) for the two lists.
        """
        police = [idx for idx, ch in enumerate(arr) if ch == 'P']
        thieves = [idx for idx, ch in enumerate(arr) if ch == 'T']
        i = j = caught = 0
        while i < len(police) and j < len(thieves):
            if abs(police[i] - thieves[j]) <= k:
                caught += 1
                i += 1
                j += 1
            elif police[i] < thieves[j]:
                i += 1
            else:
                j += 1
        return caught

    # ----- Alternative 2: simple brute force (for explanation; not for big n) -----
    def catchThieves_bruteforce(self, arr, k):
        """
        For every policeman, search the nearest unmatched thief within distance k.
        Time: O(n * k) worst-case (or O(n^2) if you linearly scan the whole array).
        Space: O(n) for used[] flags.
        """
        n = len(arr)
        used = [False] * n  # used[t_idx] marks a thief as already caught
        caught = 0
        for i, ch in enumerate(arr):
            if ch != 'P':
                continue
            # Search outward from the policeman up to distance k to find the closest thief
            for d in range(0, k + 1):
                left = i - d
                right = i + d
                if left >= 0 and arr[left] == 'T' and not used[left]:
                    used[left] = True
                    caught += 1
                    break
                if right < n and arr[right] == 'T' and not used[right]:
                    used[right] = True
                    caught += 1
                    break
        return caught
```

**Notes for interviews**

* Lead with the `O(1)`-space two-pointer version (`catchThieves`).
* If asked for a simpler to explain code, show `indexlists` (still `O(n)`, but uses extra space).
* Use the brute version only to show the starting point / contrast.

---

## 4) Likely interviewer Q\&A

**Q1. Why is the two-pointer greedy correct?**
**A.** Suppose the earlier index (say at `x`) can’t match the current opposite at `y` because `|x−y|>k`. Since all future positions are ≥ `y`, the distance from `x` to any future candidate only grows, so `x` can never match later. Moving the earlier pointer forward is safe. When a pair is within `k`, matching them immediately is optimal: delaying would only shrink options for both without creating a better pairing.

**Q2. Time and space complexity?**
**A.** Two-pointer scan is `O(n)` time and `O(1)` auxiliary space. The index-lists variant is `O(n)` time and `O(n)` space. Brute force can be `O(n*k)` (or `O(n^2)` if not careful).

**Q3. Edge cases to watch?**
**A.**

* All `P` or all `T` → answer `0`.
* `k = 0` → only adjacent same-spot indices (impossible unless you model identical positions) so typically `0`.
* Large `k` (e.g., ≥ array length) → effectively match in order; answer is `min(#P, #T)`.
* Empty or size 1 arrays.

**Q4. Can we do it streaming without storing all positions?**
**A.** Yes—the two-pointer scan shown uses only the array and constant extra space. Another streaming option uses two queues/deques of indices; complexity remains `O(n)`.

**Q5. What changes if each policeman could catch multiple thieves?**
**A.** If a policeman has capacity `c > 1`, the one-dimensional version becomes similar to matching with capacities; you can still greedily match closest available thieves while counting down capacity for the current policeman before advancing.

**Q6. Why not always choose the *closest* pair globally?**
**A.** Global “closest pair” selection each step can be `O(n^2)`. The ordered two-pointer rule implicitly achieves the optimal matching in linear time by never creating crossing matches that would reduce feasibility.

---

---

Here’s the **full inline program** (no separate file) with **inline complexity notes**, **inputs**, **outputs**, and **main-program timing** using `timeit`. I’ve also run it above so you can see the actual outputs and timing.

```python
from typing import List
import random, timeit

class Solution:
    def catchThieves(self, arr: List[str], k: int) -> int:
        """
        Optimized two-pointer scan with O(1) extra space.
        Complexity notes by step:
          - Finding next 'P'/'T' with while loops: amortized O(1) each advance.
          - Each index moves at most n times → overall O(n) time.
          - No extra containers → O(1) auxiliary space.
        """
        n = len(arr)
        i = j = 0  # i → next policeman index, j → next thief index

        # Helpers to jump to the next index of a target char
        def next_char(idx: int, ch: str) -> int:
            # Worst-case O(n) over the whole run, but amortized O(1) per move
            while idx < n and arr[idx] != ch:
                idx += 1
            return idx

        i = next_char(0, 'P')
        j = next_char(0, 'T')

        caught = 0
        while i < n and j < n:
            if abs(i - j) <= k:
                # Match this pair and advance both pointers.
                # O(1) work; each pointer advances at most n times.
                caught += 1
                i = next_char(i + 1, 'P')
                j = next_char(j + 1, 'T')
            elif i < j:
                # Policeman too far left of the current thief → move to next P
                i = next_char(i + 1, 'P')
            else:
                # Thief too far left of the current policeman → move to next T
                j = next_char(j + 1, 'T')
        return caught

    def catchThieves_indexlists(self, arr: List[str], k: int) -> int:
        """
        Alternate approach: build separate index lists for P and T, then two-pointer.
        - Build lists: O(n) time, O(n) space to store indices.
        - Two-pointer merge-like pass: O(n) time, O(1) extra.
        Overall: O(n) time, O(n) space.
        """
        police = [i for i, ch in enumerate(arr) if ch == 'P']   # O(n) time & O(n) space
        thieves = [i for i, ch in enumerate(arr) if ch == 'T']  # O(n) time & O(n) space

        i = j = 0
        caught = 0
        while i < len(police) and j < len(thieves):             # O(n) overall
            if abs(police[i] - thieves[j]) <= k:
                caught += 1
                i += 1
                j += 1
            elif police[i] < thieves[j]:
                i += 1
            else:
                j += 1
        return caught

    def catchThieves_bruteforce(self, arr: List[str], k: int) -> int:
        """
        Brute/Easy for teaching: for each policeman, scan outward up to distance k
        to catch the nearest unused thief.
        - Outer loop across positions: O(n)
        - Inner search up to distance k: O(k) worst per policeman
        Worst-case O(n*k) time (can degenerate to O(n^2)); O(n) space for flags.
        """
        n = len(arr)
        used = [False] * n  # O(n) space
        caught = 0
        for i, ch in enumerate(arr):  # O(n)
            if ch != 'P':
                continue
            # scan outward from distance 0..k  → O(k) per P
            for d in range(0, k + 1):
                left = i - d
                right = i + d
                if left >= 0 and arr[left] == 'T' and not used[left]:
                    used[left] = True
                    caught += 1
                    break
                if right < n and arr[right] == 'T' and not used[right]:
                    used[right] = True
                    caught += 1
                    break
        return caught


def main():
    sol = Solution()

    print("=== Police and Thieves — Demo ===")
    # ---- Input set 1 (prompt example) ----
    arr1 = ['P', 'T', 'T', 'P', 'T']
    k1 = 1
    print("\nInput 1:", arr1, "k =", k1)
    print("Optimized O(1) space:", sol.catchThieves(arr1, k1))          # expected 2
    print("Index-lists O(n) space:", sol.catchThieves_indexlists(arr1, k1))
    print("Bruteforce O(n*k):     ", sol.catchThieves_bruteforce(arr1, k1))

    # ---- Input set 2 (prompt example) ----
    arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
    k2 = 2
    print("\nInput 2:", arr2, "k =", k2)
    print("Optimized O(1) space:", sol.catchThieves(arr2, k2))          # expected 3
    print("Index-lists O(n) space:", sol.catchThieves_indexlists(arr2, k2))
    print("Bruteforce O(n*k):     ", sol.catchThieves_bruteforce(arr2, k2))

    # ---- Quick scale test (near constraints) ----
    n = 100000
    random.seed(0)
    arr_big = ['P' if random.random() < 0.5 else 'T' for _ in range(n)]
    k_big = 1000
    # Time only the optimized method on the large input
    t0 = timeit.default_timer()
    ans_big = sol.catchThieves(arr_big, k_big)
    t1 = timeit.default_timer()
    print(f"\nLarge test: n={n}, k={k_big}")
    print("Optimized answer:", ans_big)
    print("Optimized run time:", f"{t1 - t0:.6f}s")


if __name__ == "__main__":
    # Time the *full* main program run (I/O + construction + calls).
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
```

The printed output from running this program is already shown above (for both sample inputs and a large random test), including the **TOTAL MAIN RUNTIME**.

---

## 6) Real-World Use Cases (high-impact)

* **Patrol–incident dispatch within radius:** Assign police (or ambulances) to incidents only within a reachable distance limit to maximize handled incidents — same greedy matching principle.
* **Field service technicians:** Match technicians to service calls within their operating radius while ensuring each tech handles at most one urgent job at a time.
* **Ride-hailing pickups:** Match drivers and riders with a maximum pickup radius, maximizing completed matches without over-assigning a driver.



---

# 🧩 Next Permutation

**Difficulty:** Medium
**Accuracy:** 40.66%
**Submissions:** 244K+
**Points:** 4
**Average Time:** 20m

---

## 🧠 Problem Statement

Given an array of integers **arr[]** representing a permutation, implement the **next permutation** that rearranges the numbers into the **lexicographically next greater permutation**.

If no such permutation exists, rearrange the numbers into the **lowest possible order** (i.e., sorted in ascending order).

---

### 📝 Note

A **permutation** of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

---

## 🧮 Examples

### Example 1

**Input:**
`arr[] = [2, 4, 1, 7, 5, 0]`

**Output:**
`[2, 4, 5, 0, 1, 7]`

**Explanation:**
The next permutation of the given array is `[2, 4, 5, 0, 1, 7]`.

---

### Example 2

**Input:**
`arr[] = [3, 2, 1]`

**Output:**
`[1, 2, 3]`

**Explanation:**
As `arr[]` is the last permutation, the next permutation is the lowest one.

---

### Example 3

**Input:**
`arr[] = [3, 4, 2, 5, 1]`

**Output:**
`[3, 4, 5, 1, 2]`

**Explanation:**
The next permutation of the given array is `[3, 4, 5, 1, 2]`.

---

## 🧾 Constraints

```
1 ≤ arr.size() ≤ 10^5  
0 ≤ arr[i] ≤ 10^5  
```

---

## ⚙️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

`Infosys` `Flipkart` `Amazon` `Microsoft` `FactSet` `Hike` `MakeMyTrip` `Google` `Qualcomm` `Salesforce`

---

## 🧰 Topic Tags

`Arrays` `Permutation` `Constructive Algorithms` `Data Structures`

---

## 💼 Related Interview Experiences

* Qualcomm Interview Experience Set 7 (Off Campus)
* Makemytrip Interview Experience Set 11 (Developer Position)
* Amazon Interview Experience Set 413 (SDET 1 Campus Internship)
* Flipkart Interview Experience Set 2

---

## 📚 Related Articles

* [**Next Permutation**](https://www.geeksforgeeks.org/next-permutation/)

---

---

Great choice—**Next Permutation** is a classic that interviewers love. Here’s everything you need: intuition, a clean dry run, two Python solutions (optimal + “brute-ish”), and a compact interview recall kit.

---

## 2) Intuition + Step-by-Step Dry Run

### Core idea (lexicographic “next”)

To move to the next permutation (just larger, minimal change), we:

1. **Scan from right** to find the first **ascending pair** `arr[i] < arr[i+1]`. (Call `i` the **pivot**.)

   * If no such `i` exists, the array is strictly non-increasing → we’re at the **last permutation** → return the **first** permutation by reversing the whole array.
2. In the suffix `arr[i+1:]` (which is non-increasing), find the **rightmost element greater than** `arr[i]` (the **successor**).
3. **Swap** pivot and successor.
4. **Reverse the suffix** `arr[i+1:]` to put it in **increasing order** (the smallest tail after the new prefix).

Why it works:

* Step 1 finds the rightmost place where we can increase.
* Step 2 picks the smallest increase possible (rightmost greater).
* Step 4 makes the tail minimal, so the whole permutation is the next one.

---

### Dry run on: `arr = [2, 4, 1, 7, 5, 0]`

1. From right, find first `arr[i] < arr[i+1]`:

   * Compare (5,0): 5>0
   * (7,5): 7>5
   * (1,7): **1<7** → `i = 2` (pivot = 1)
2. In suffix `[7,5,0]`, find **rightmost > 1** → candidates: 7,5 → rightmost is **5** (`j = 4`)
3. Swap pivot with successor:
   `[2, 4, 5, 7, 1, 0]`
4. Reverse suffix after `i`: reverse `[7,1,0]` → `[0,1,7]`
   Final: **`[2, 4, 5, 0, 1, 7]`**

Another quick edge case: `arr = [3,2,1]`
No ascending pair; reverse all → `[1,2,3]`.

---

## 3) Python Solutions (your signature)

### A) Optimal in-place O(n) / O(1)

```python
class Solution:
    def nextPermutation(self, arr):
        """
        Rearranges arr into its lexicographically next permutation.
        If not possible (already the largest), rearranges to the lowest order.
        Time: O(n), Space: O(1) in-place
        """
        n = len(arr)
        if n <= 1:
            return arr  # trivial

        # 1) Find pivot: rightmost i with arr[i] < arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            # 2) Find rightmost successor > arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # 3) Swap pivot and successor
            arr[i], arr[j] = arr[j], arr[i]

        # 4) Reverse the suffix to get the smallest tail
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr  # returning arr for convenience (in-place anyway)
```

### B) “Brute-ish” (conceptual / less optimal)

Generate all permutations is factorial and not interview-worthy. A more reasonable “brute-ish” variant after finding the pivot is to **sort** the suffix instead of reversing—but you must still pick the correct successor. This is `O(n log n)`:

```python
class Solution:
    def nextPermutation(self, arr):
        """
        Slightly less optimal: still finds pivot+successor correctly,
        but sorts the suffix instead of reversing (O(n log n)).
        """
        n = len(arr)
        if n <= 1:
            return arr

        # 1) Find pivot
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i == -1:
            arr.reverse()
            return arr

        # 2) Find rightmost successor > arr[i]
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1

        # 3) Swap
        arr[i], arr[j] = arr[j], arr[i]

        # 4) Sort the suffix (instead of reverse) → O(n log n)
        arr[i + 1:] = sorted(arr[i + 1:])
        return arr
```

> In interviews, prefer **Solution A**. Mention that sorting the suffix is unnecessary because the suffix is **descending**, so reversing is the same as sorting ascending (but cheaper: O(n)).

---

## 4) Interview Recall & Q/A

### 5-Line “rebuild” template

```
find i from right with a[i] < a[i+1]
if i == -1: reverse all; return
find j from right with a[j] > a[i]
swap a[i], a[j]
reverse a[i+1 .. end]
```

### Mnemonic: **“P S R”** → **Pivot – Successor – Reverse**

* **Pivot**: rightmost rise
* **Successor**: rightmost element just bigger than pivot
* **Reverse**: the suffix (because it was descending)

### Quick Q&A

* **Why reverse the suffix?**
  Because the suffix was in **non-increasing** order. After swapping the pivot with the next larger element, to get the **smallest** next permutation we must put the suffix in **ascending** order → reversing is O(n) and sufficient.
* **Why rightmost successor?**
  It guarantees the **minimal increase** over the current prefix, yielding the lexicographically next permutation (not skipping any).
* **What if there is no pivot?**
  The array is the last permutation → reverse entire array to return the first (lowest).
* **Does it work with duplicates?**
  Yes, the logic is identical.
* **Complexity?**
  O(n) time (one backward scan + one backward scan + O(n) reverse), O(1) extra space.

---

### One-liner to say before coding

> “I’ll scan from right to find the **pivot** `a[i] < a[i+1]`. If none, reverse the whole array. Otherwise, find the **rightmost successor** `a[j] > a[i]`, swap them, and **reverse the suffix** `a[i+1:]` to get the minimal tail. That’s O(n) in-place.”

---

---

Absolutely! Here are crisp, interview-ready **use cases** and a **full, runnable program** (with timing + inline complexity notes) for **Next Permutation**.

---

## 5) Real-World Use Cases (easy to relate)

* **Scheduling / roster permutations:** generate the next feasible ordering of tasks or on-call rotations deterministically.
* **Search/optimization (local neighborhood):** step to the lexicographically next solution when systematically exploring permutations.
* **Game/puzzle state enumeration:** iterate permutations in order (e.g., brute-force small search spaces) without storing all states.
* **Testing & fuzzing:** deterministic permutation order for test-case generation (reproducible compared to random shuffles).
* **Combinatorial generation APIs:** this is exactly what C++’s `std::next_permutation` provides—useful for iterating all permutations in sorted order.

---

## 6) Full Program (with complexity notes + timing)

```python
#!/usr/bin/env python3
"""
Next Permutation — full program with timing and annotated complexities.

Algorithm (lexicographic next):
  1) Find the rightmost index i with arr[i] < arr[i+1]     → O(n) scan
  2) If none: reverse whole array (we were at last perm)   → O(n)
  3) Else find rightmost j > i with arr[j] > arr[i]        → O(n) worst
  4) Swap arr[i], arr[j]                                   → O(1)
  5) Reverse suffix arr[i+1:] to make it minimal           → O(n)

Total time: O(n). Extra space: O(1) in place.
"""

from time import perf_counter
import timeit
from typing import List


class Solution:
    def nextPermutation(self, arr: List[int]) -> List[int]:
        """
        Rearranges arr into the lexicographically next permutation in place.
        If already at the last permutation, transforms to the first (sorted asc).

        Time  : O(n)
        Space : O(1) extra
        """
        n = len(arr)
        if n <= 1:
            return arr  # trivial, O(1)

        # 1) Find pivot: rightmost i with arr[i] < arr[i+1]  → O(n)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            # 2) Find rightmost successor > arr[i]           → O(n)
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # 3) Swap (minimal increase)                     → O(1)
            arr[i], arr[j] = arr[j], arr[i]

        # 4) Reverse suffix (arr[i+1..end]) to smallest tail → O(n)
        l, r = i + 1, n - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return arr  # return is convenient for demos; mutation is in-place.


# ------------------------------ Demo & Timing ------------------------------

def demo():
    sol = Solution()

    cases = [
        [2, 4, 1, 7, 5, 0],      # example → [2, 4, 5, 0, 1, 7]
        [3, 2, 1],               # last → becomes first [1,2,3]
        [3, 4, 2, 5, 1],         # → [3,4,5,1,2]
        [1],                     # single element
        [1, 1, 5],               # duplicates → [1,5,1]
        [1, 3, 2],               # → [2,1,3]
    ]

    print("=== Sample I/O ===")
    for arr in cases:
        a = arr[:]  # copy so we can show before/after
        start = perf_counter()
        out = sol.nextPermutation(a)
        micros = (perf_counter() - start) * 1e6
        print(f"in : {arr}\nout: {out}   (took {micros:.1f} µs)")
        print("-" * 48)

    # Timing on a large random-like ascending range (worst-ish pivot near end)
    large = list(range(1, 200000)) + [199999]  # mostly increasing
    # Use timeit for stable average
    avg = timeit.timeit(
        "sol.nextPermutation(large[:])",        # copy to avoid reusing mutated list
        number=3,
        globals={"sol": sol, "large": large}
    ) / 3.0
    print(f"Average time on n={len(large)} over 3 runs: {avg:.3f} s")

    print("\nComplexity recap:")
    print("  - Rightward scans (pivot/successor): O(n)")
    print("  - Reverse suffix: O(n)")
    print("  - Total per call: O(n), Space: O(1) in-place")


if __name__ == "__main__":
    demo()
```

### Example Output (illustrative)

```
=== Sample I/O ===
in : [2, 4, 1, 7, 5, 0]
out: [2, 4, 5, 0, 1, 7]   (took 70.4 µs)
------------------------------------------------
in : [3, 2, 1]
out: [1, 2, 3]   (took 8.9 µs)
------------------------------------------------
in : [3, 4, 2, 5, 1]
out: [3, 4, 5, 1, 2]   (took 11.2 µs)
------------------------------------------------
...
Average time on n=200000 over 3 runs: 0.0xx s

Complexity recap:
  - Rightward scans (pivot/successor): O(n)
  - Reverse suffix: O(n)
  - Total per call: O(n), Space: O(1)
```

---

### What to say in the interview (10 seconds)

> “Scan from the right to find the **pivot** `a[i] < a[i+1]`. If none, **reverse all**. Otherwise find the **rightmost successor** `a[j] > a[i]`, **swap**, and **reverse the suffix** `a[i+1:]` to make the tail minimal. That’s **O(n)** in-place.”


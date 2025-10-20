# Rotate Array by One

**Difficulty:** Basic
**Accuracy:** 69.6%
**Submissions:** 332K+
**Points:** 1
**Average Time:** 20m

---

## Problem Statement

Given an array `arr`, rotate the array by **one position in clockwise direction**.

---

## Examples

### Example 1

* **Input:** `arr[] = [1, 2, 3, 4, 5]`
* **Output:** `[5, 1, 2, 3, 4]`
* **Explanation:** If we rotate `arr` by one position in clockwise, `5` comes to the front and the remaining elements are shifted to the end.

### Example 2

* **Input:** `arr[] = [9, 8, 7, 6, 4, 2, 1, 3]`
* **Output:** `[3, 9, 8, 7, 6, 4, 2, 1]`
* **Explanation:** After rotating clockwise, `3` comes in first position.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* `Arrays`, `implementation`

---

## Related Articles

* *[C Program Cyclically Rotate Array One](https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/)*

---

---


Here’s a crisp, interview-ready cheat-sheet for **Rotate Array by One (clockwise)** — i.e., move the last element to the front and shift everything else right by 1.

---

## 2) Intuition + step-by-step dry run

**Goal:** transform `arr = [a0, a1, …, a(n-2), a(n-1)]` into
`[a(n-1), a0, a1, …, a(n-2)]`.

### Why scan **backwards**?

If we shift left-to-right we’ll overwrite values we still need.
So we:

1. store the last element,
2. walk **from right to left**, copying `arr[i-1] → arr[i]`,
3. place the saved last element at `arr[0]`.

### Dry run (Example)

`arr = [1, 2, 3, 4, 5]`

* `last = 5`
* i=4: `arr[4] = arr[3]` → `[1,2,3,4,4]`
* i=3: `arr[3] = arr[2]` → `[1,2,3,3,4]`
* i=2: `arr[2] = arr[1]` → `[1,2,2,3,4]`
* i=1: `arr[1] = arr[0]` → `[1,1,2,3,4]`
* `arr[0] = last` → **`[5,1,2,3,4]`** ✅

Edge cases: empty array or length 1 → unchanged.

---

## 3) Python solutions (what interviewers expect)

### A) In-place O(1) space (preferred)

```python
# User function Template for python3
class Solution:
    def rotate(self, arr):
        """
        Rotate array right by 1 (clockwise) in-place.
        Time:  O(n)  -- single backward pass
        Space: O(1)  -- only one temp
        """
        n = len(arr)
        if n <= 1:
            return  # nothing to do

        last = arr[-1]                # save last element
        # shift elements right, scanning backwards to avoid overwrite
        for i in range(n - 1, 0, -1): # i = n-1, ..., 1
            arr[i] = arr[i - 1]
        arr[0] = last                 # place saved last at front
        # function mutates arr in place (no return needed for most judges)
```

### B) 3-reverse trick (generalizes to rotate by **k**)

For k=1:

1. reverse whole array,
2. reverse first 1 element (no-op),
3. reverse remaining n−1 elements.

Shown as a general template (works for any k, uses O(1) space):

```python
class Solution:
    def rotate(self, arr):
        """
        3-reverse method (shown generalized to k=1).
        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return
        k = 1 % n  # keeps template ready for any k
        # helper reverse in place
        def rev(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1; r -= 1
        rev(0, n - 1)          # reverse all
        rev(0, k - 1)          # reverse first k (k=1 -> no-op)
        rev(k, n - 1)          # reverse rest
```

### C) Pythonic slicing (simple, but uses extra memory)

```python
class Solution:
    def rotate(self, arr):
        """
        Slicing creates a new list then assigns back.
        Time:  O(n)
        Space: O(n) extra (temporary list)
        """
        if len(arr) <= 1:
            return
        arr[:] = arr[-1:] + arr[:-1]  # mutate the same object for callers
```

> Interview tip: Lead with **A** (in-place, O(1)). If asked how to rotate by **k**, explain the **3-reverse** method (B) and use `k %= n`.

---

## 4) Likely interviewer Q\&A

**Q1. Complexity? Why backward iteration?**

* **Time:** `O(n)` — each element moves once.
* **Space:** `O(1)` — only one temp.
* Backward iteration avoids overwriting values we still need to read.

**Q2. How to rotate by `k` positions clockwise (right)?**
Use the 3-reverse trick with `k %= n`:
`reverse(0, n-1)`, `reverse(0, k-1)`, `reverse(k, n-1)`.

**Q3. What about anticlockwise (left) rotation by 1?**
Save `first = arr[0]`, shift left (`arr[i] = arr[i+1]`), set `arr[-1] = first`.
Or use 3-reverse with `k = n-1`.

**Q4. Any pitfalls in Python?**

* `arr = arr[-1:] + arr[:-1]` **rebinds** the name (callers won’t see change). Use `arr[:] = ...` to mutate in place.
* Don’t use repeated `insert(0, x)` inside loops (quadratic).

**Q5. For very large arrays, which approach?**
In-place **A** or **B** to keep memory `O(1)` and linear time.

---

---

Done! I ran a **full inline Python program** that:

* Implements `rotate` (in-place `O(n)` time / `O(1)` space),
* Also shows the **3-reverse trick** and a **Pythonic slicing** variant,
* Prints **inputs and outputs** for both examples,
* Benchmarks on `n=100000` and prints the **TOTAL MAIN RUNTIME** using `timeit`.

```python

# Re-run to display outputs after state reset
from typing import List
import timeit

class Solution:
    def rotate(self, arr: List[int]) -> None:
        n = len(arr)
        if n <= 1:
            return
        last = arr[-1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last

    def rotate_reverse_trick(self, arr: List[int]) -> None:
        n = len(arr)
        if n <= 1:
            return
        k = 1 % n
        def rev(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1; r -= 1
        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)

    def rotate_slicing(self, arr: List[int]) -> None:
        n = len(arr)
        if n <= 1:
            return
        arr[:] = arr[-1:] + arr[:-1]

def main():
    sol = Solution()
    print("=== Rotate Array by One (clockwise) — Demo & Timing ===")
    arr1 = [1, 2, 3, 4, 5]
    a1 = arr1.copy()
    t0 = timeit.default_timer()
    sol.rotate(a1)
    t1 = timeit.default_timer()
    print("\nInput 1 :", arr1)
    print("Output 1:", a1)
    print(f"Time (rotate in-place): {(t1 - t0):.6f}s")
    arr2 = [9, 8, 7, 6, 4, 2, 1, 3]
    a2 = arr2.copy()
    t0 = timeit.default_timer()
    sol.rotate(a2)
    t1 = timeit.default_timer()
    print("\nInput 2 :", arr2)
    print("Output 2:", a2)
    print(f"Time (rotate in-place): {(t1 - t0):.6f}s")
    alt = [10, 20, 30, 40]
    r1 = alt.copy(); sol.rotate_reverse_trick(r1)
    r2 = alt.copy(); sol.rotate_slicing(r2)
    print("\nCross-check input:", alt)
    print("Reverse-trick    ->", r1)
    print("Slicing          ->", r2)
    n = 100_000
    big = list(range(n))
    t0 = timeit.default_timer()
    sol.rotate(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: done. First 5 after rotate -> {big[:5]}")
    print(f"Time (rotate in-place): {(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **Buffer/Log rotation:** Cyclic buffers where the “last written” becomes the new front (e.g., ring buffers, time-windowed logs).
* **Scheduling/round-robin:** Rotating a queue of tasks so the next candidate becomes the head.
* **Data shuffling in streaming systems:** Right-shifts to bring newest data up front while preserving ordering for the rest.
* **Array-based deques:** Implementing a one-step rotate in fixed-size arrays without extra memory.

If you want a version generalized to rotate by **k** (clockwise/anticlockwise) with the 3-reverse template, I can drop it in too.

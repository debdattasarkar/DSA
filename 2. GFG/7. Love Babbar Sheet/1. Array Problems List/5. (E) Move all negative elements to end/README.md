Here’s your **full README-style conversion** of the question in the image — all details included, in clean GeeksforGeeks-style format 👇

---

# Move all Negative Elements to End

**Difficulty:** Easy
**Accuracy:** 56.24%
**Submissions:** 164K+
**Points:** 2

---

## 🧾 Problem Statement

Given an unsorted array `arr[]` having both negative and positive integers.
The task is to **place all negative elements at the end of the array** without changing the order of positive elements and negative elements.

> **Note:** Don’t return any array; perform the operation **in place** on the array.

---

## 📘 Examples

### Example 1:

**Input:**
`arr[] = [1, -1, 3, 2, -7, -5, 11, 6]`

**Output:**
`[1, 3, 2, 11, 6, -1, -7, -5]`

**Explanation:**
By rearranging the elements, all the negative integers are moved to the end while keeping the relative order of both positive and negative numbers unchanged.

---

### Example 2:

**Input:**
`arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]`

**Output:**
`[7, 9, 10, 11, -5, -3, -4, -1]`

---

## ⏱️ Expected Time Complexity

`O(n)`

## 💾 Expected Auxiliary Space

`O(n)`

---

## ⚙️ Constraints

* `1 ≤ arr.size ≤ 10⁶`
* `-10⁹ ≤ arr[i] ≤ 10⁹`

---

## 🏷️ Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* [Move Negative Elements to End (Order Extra Space Allowed)](https://www.geeksforgeeks.org/move-ve-elements-end-order-extra-space-allowed/)

---

---

Got it! Here’s the interview-ready pack for **“Move all negative elements to end (keep order stable)”**.

---

# 2) Text explanation + step-by-step dry run

## 🧠 Goal

Given `arr` with positive and negative integers, **move all negatives to the end** while **preserving the relative order** of both positives and negatives.

* “Stable” means the left-to-right order of all positives stays the same, and the order of all negatives stays the same.
* On GFG, this is usually solved in **O(n) time, O(n) extra space** (stable partition via buffer).
  *True in-place and stable is possible but either **O(n²)** (shifting) or **O(n log n)** (block-rotate recursion).*

## ✅ Most expected approach (for interviews)

**Stable partition using an auxiliary buffer**:

1. Scan once, collect **positives** in order.
2. Scan again (or in same pass), collect **negatives** in order.
3. Overwrite `arr[:] = positives + negatives`.

* **Time:** `O(n)`
* **Aux space:** `O(n)` (because stability with linear time).

## 🧪 Dry run (on Example 1)

Input:
`arr = [1, -1, 3, 2, -7, -5, 11, 6]`

1. Collect positives in order:
   `positives = [1, 3, 2, 11, 6]`

2. Collect negatives in order:
   `negatives = [-1, -7, -5]`

3. Write back (preserve stability):
   `arr[:] = positives + negatives = [1, 3, 2, 11, 6, -1, -7, -5]`

Done. Order inside each group is unchanged.

---

# 3) Python solutions (brute + most-expected + in-place option)

All versions stick to your requested signature.

## A) **Most expected (stable, O(n) time, O(n) space)**

```python
# User function Template for python3

class Solution:
    def segregateElements(self, arr):
        """
        Stable O(n) approach using auxiliary lists.
        Keeps the relative order of positives and negatives.
        Time  : O(n)
        Space : O(n)  (extra buffer to maintain stability)
        """
        positives = []  # will keep all >= 0 and > 0 as "positives" per problem text
        negatives = []

        # Single pass: partition stably into two lists
        for value in arr:
            if value >= 0:
                positives.append(value)
            else:
                negatives.append(value)

        # Overwrite the original list in-place (required by platform)
        arr[:] = positives + negatives
        # No return needed on GFG; but safe to keep as per many templates:
        return arr
```

### Why interviewers like this

* Clear, linear, easy to reason about.
* Explicitly preserves order.
* Matches GFG’s stated complexities for this problem.

---

## B) **Brute in-place (stable, O(1) extra space) but O(n²) time**

> Use **stable insertion**: whenever you see a negative in the “positives zone”, **remove** it and **insert** it at the end portion by shifting the middle block right by 1.
> This is stable and truly in-place, but quadratic in the worst case.

```python
class SolutionBruteInPlace:
    def segregateElements(self, arr):
        """
        Stable and in-place (O(1) extra) but O(n^2) time.
        Idea: for each index, if arr[i] < 0, "extract" it and shift the
        block [pos_ptr ... i-1] one step right, then place the negative after the last positive.
        """
        n = len(arr)
        pos_ptr = 0  # next position where a positive should live

        # Walk left to right; whenever we see a positive, place it at pos_ptr.
        # When we see a negative among positives, we "bubble" it right by shifting.
        i = 0
        while i < n:
            if arr[i] >= 0:
                # This positive should be at pos_ptr. If i > pos_ptr, shift block of positives.
                if i != pos_ptr:
                    temp = arr[i]
                    # shift right the block [pos_ptr .. i-1]
                    j = i
                    while j > pos_ptr:
                        arr[j] = arr[j - 1]
                        j -= 1
                    arr[pos_ptr] = temp
                pos_ptr += 1
            # If negative, do nothing now (it will naturally drift to the right as positives compact left)
            i += 1
        return arr
```

**Use when:** interviewer explicitly disallows extra space and still requires stability. Be upfront about `O(n²)`.

---

## C) **Pythonic, concise (still O(n) time, O(n) space)**

> Same idea as (A), but shorter. Useful if the interviewer is fine with Pythonic style and clarity.

```python
class SolutionPythonic:
    def segregateElements(self, arr):
        """
        Pythonic stable partition with list comprehensions.
        Time  : O(n)
        Space : O(n)
        """
        positives = [x for x in arr if x >= 0]
        negatives = [x for x in arr if x < 0]
        arr[:] = positives + negatives
        return arr
```

---

## D) (Optional talking point) **Stable + O(1) space + o(n²) time?**

There’s a divide-and-conquer **stable partition** using **block rotations**:

* Recursively partition left/right halves, then **rotate** middle blocks so that “positives then negatives” is achieved.
* **Time:** `O(n log n)`; **Space:** `O(1)` extra (besides recursion stack).
  Good to **mention**; rarely required to code live.

---

## Quick checklist to say out loud in the interview

* “We need **stable partition**: positives first (same order), then negatives (same order).”
* “I’ll do a **linear scan** to gather positives and negatives, then overwrite the array: **O(n) time, O(n) space**.”
* “If you need **in-place + stable** with no extra space, there’s an **O(n²)** shifting method, and a more advanced **O(n log n)** block-rotate method.”

That’s it—clean, fast, and interview-friendly.

---

Awesome—here’s a tight, interview-ready “recall kit” for **Move all negative elements to end (stable)**.

---

# How to remember & proceed in the interview (60-sec recall)

## 5-line skeleton (stable, O(n) time, O(n) space)

```
pos = []
neg = []
for x in arr:
    (pos if x >= 0 else neg).append(x)
arr[:] = pos + neg
```

### Mnemonic

**“Scan → Split → Stitch.”**
Say it: *scan the array, split into pos/neg, stitch back (pos + neg).*

### One-liner reminder

`arr[:] = [x for x in arr if x >= 0] + [x for x in arr if x < 0]`

### What to say out loud (15–20s script)

> “This is a **stable partition**: keep the relative order of positives and negatives.
> I’ll do a single pass, collect positives and negatives, then overwrite the array.
> **Time O(n), space O(n)**—this is the expected solution when stability is required in linear time.”

---

# Expected interviewer Q&A (with crisp answers)

### Q1) What does “stable” mean here?

**A:** The **relative order** within positives and within negatives must remain the same as the original array.

### Q2) Can you do it in-place with O(1) extra space?

**A:** If we also require **stability**, true in-place becomes **O(n²)** by shifting blocks (insertion-style). There’s a **divide-and-conquer stable partition** using block rotations that’s **O(n log n)** time, **O(1)** extra space (besides recursion stack). If stability is **not** required, we can do in-place linear-time **but it won’t be stable** (e.g., two-pointer partition).

### Q3) Why do we need O(n) extra space for the linear-time stable method?

**A:** Stability + linear time implies we must **buffer** one of the groups so we don’t overwrite elements we haven’t visited yet. That’s what the `pos`/`neg` arrays provide.

### Q4) Give complexities of the main approaches.

* **Stable, linear time:** `O(n)` time, `O(n)` space (split & stitch).
* **Stable, in-place:** `O(n²)` (shifting) or `O(n log n)` (block-rotate D&C), `O(1)` extra.
* **Unstable, in-place (two-pointer partition):** `O(n)` time, `O(1)` space—but order changes.

### Q5) Show the in-place but stable idea (high level).

**A:** Traverse left→right. When you hit a **positive** among earlier negatives, **rotate** the subarray to bring that positive forward (or shift the block of negatives right by one). Each rotation/shift costs O(k), so worst-case O(n²).

### Q6) Edge cases?

* All positives or all negatives (no change).
* Zeros (considered **non-negative**, so treated as “positive”).
* Single element; duplicates; large n.
* Already “partitioned” arrays (still stable).

### Q7) If the array is a **linked list**, what changes?

**A:** Very convenient: build two lists (pos/neg) in one pass and then **concatenate**—stable, `O(n)` time, `O(1)` extra nodes.

### Q8) Streaming version (data arrives over time)?

**A:** Maintain two queues: enqueue to **posQ** for `>=0`, to **negQ** for `<0`. When output is needed, flush `posQ` then `negQ`. This preserves stability.

### Q9) Can we generalize to “move all elements matching predicate P to end”?

**A:** Yes—replace “x < 0” with any predicate `P(x)`. Same **scan → split → stitch** pattern.

### Q10) How do you test quickly?

* `[]`, `[5]`, `[-5]`, `[0]`
* Mixed: `[1, -1, 3, 2, -7, -5, 11, 6]` → `[1, 3, 2, 11, 6, -1, -7, -5]`
* All negs: `[-3, -2, -1]`
* All pos: `[4, 3, 2]`
* Alternating: `[-1, 1, -2, 2, -3, 3]`
  Check stability on both groups.

---

# What to code first (and how to narrate)

1. **State the requirement:** “Stable partition of negatives to the end.”
2. **Pick the expected solution:** split & stitch (`O(n)`/`O(n)`).
3. **Implement quickly** (the template you already have):

```python
#User function Template for python3
class Solution:
    def segregateElements(self, arr):
        pos, neg = [], []
        for x in arr:
            (pos if x >= 0 else neg).append(x)
        arr[:] = pos + neg
        return arr
```

4. **Offer alternatives if asked:**

   * In-place **unstable** O(n)/O(1).
   * In-place **stable** O(n²) or block-rotate O(n log n).

---

# Pitfalls interviewers look for (and how to avoid)

* **Breaking stability** with a simple two-pointer swap—call out that this is **not** stable.
* **Forgetting zero’s sign rule**—on GFG, treat `0` as non-negative.
* **Returning a new list** when the platform expects **in-place**—use `arr[:] = …`.
* **Overcomplicating** when the prompt’s expected solution is the O(n) space stable approach.

---

# Quick variations they might ask (with answers)

* **“Move positives to end, keep order.”** → Flip predicate: collect negatives first, then positives.
* **“Partition by absolute value < k vs ≥ k.”** → Change predicate to `abs(x) < k`.
* **“Three-way stable partition (neg / zero / pos).”** → Do **three** buffers then stitch: `neg + zero + pos`.

---

---

Absolutely — here’s a **complete, runnable Python program** for
**“Move all negative elements to the end (stable)”** with:

* Inline comments that note **time & space** at each step
* A **primary interview-expected** solution (stable `O(n)` time, `O(n)` space)
* A **stable in-place** alternative (`O(n²)` time, `O(1)` extra space) for follow-ups
* A tiny timing harness using `timeit` right inside `main`
* A ready **sample input & output**

---

```python
#!/usr/bin/env python3
"""
Move all negative elements to end (stable)

Primary approach (interview-expected):
  - Stable partition using auxiliary buffers.
  - Time  : O(n)
  - Space : O(n)

Alternative (if interviewer asks: in-place + stable):
  - Stable but O(n^2) via block shifting (insertion-like).
  - Time  : O(n^2)
  - Space : O(1) extra
"""

from time import perf_counter  # wall-clock timing for a single run
import timeit                 # average timing over multiple runs


# ----------------------------------------------------------------------
# User function Template for python3 (INTERVIEW-EXPECTED SOLUTION)
# ----------------------------------------------------------------------
class Solution:
    def segregateElements(self, arr):
        """
        Stable O(n) approach using two buffers, then overwrite the array.

        Steps and complexities:
        - Allocate two lists: O(1) time, O(1) extra space (list headers)
        - Single pass to split: O(n) time, O(n) space for collected elements
        - Concatenate & overwrite: O(n) time, O(1) extra beyond buffers

        Overall:
        - Time  : O(n)
        - Space : O(n)
        """
        positives = []  # O(1) to create; will grow to at most n -> O(n) space
        negatives = []  # O(1) to create; will grow to at most n -> O(n) space

        # Single pass: classify each element in O(1) and append in O(1) amortized
        for value in arr:  # O(n) iterations
            if value >= 0:
                positives.append(value)  # O(1) amortized
            else:
                negatives.append(value)  # O(1) amortized

        # Overwrite original array in place: O(n)
        # Space for the concatenated temporary list is O(n) (Python creates a new list),
        # then arr[:] assignment reuses arr's buffer where possible.
        arr[:] = positives + negatives

        # Many platforms expect in-place only; returning is harmless for testing.
        return arr


# ----------------------------------------------------------------------
# Alternative: Stable & In-Place (O(n^2) time, O(1) extra)
# ----------------------------------------------------------------------
class SolutionBruteInPlace:
    def segregateElements(self, arr):
        """
        Stable in-place: compacts positives to the left by shifting
        intervening negatives right. Each shift can cost O(k).

        - Outer loop visits each element once: O(n)
        - Worst-case shifting over ~n/2 elements ~ O(n) per move
        - Overall worst time: O(n^2)
        - Extra space: O(1)
        """
        n = len(arr)
        insert_pos = 0  # next index where a non-negative should be placed

        # Walk across the array once: O(n)
        i = 0
        while i < n:  # O(n) iterations
            if arr[i] >= 0:
                # If this non-negative is not already at insert_pos,
                # shift the block [insert_pos .. i-1] right by 1: O(i - insert_pos)
                if i != insert_pos:
                    temp = arr[i]  # store current value: O(1)
                    j = i
                    while j > insert_pos:  # shift right: O(i - insert_pos)
                        arr[j] = arr[j - 1]
                        j -= 1
                    arr[insert_pos] = temp  # put non-negative at correct place: O(1)
                insert_pos += 1  # next slot for a non-negative: O(1)
            # If negative, do nothing (it will be left-shifted by other moves)
            i += 1  # O(1)
        return arr


# ----------------------------------------------------------------------
# Timing helpers (simple & explicit)
# ----------------------------------------------------------------------
def time_single_run(func, *args, **kwargs):
    """
    Measure wall-clock time of a single call using perf_counter.
    Complexity: O(1) overhead + cost of func itself.
    """
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)


def time_avg(callable_stmt, number=5):
    """
    Average runtime over `number` runs using timeit (calls the callable with no args).
    Complexity: O(number) * (cost of callable).
    """
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# ----------------------------------------------------------------------
# Main: demo inputs, outputs, and timings
# ----------------------------------------------------------------------
def main():
    # ---------------------------
    # Example Inputs (edit freely)
    # ---------------------------
    arr1 = [1, -1, 3, 2, -7, -5, 11, 6]
    arr2 = [-5, 7, -3, -4, 9, 10, -1, 11]
    arr_edge_all_pos = [0, 1, 2]
    arr_edge_all_neg = [-3, -2, -1]

    print("=== Move all negative elements to end (Stable) ===\n")

    # ---------------------------------------------
    # Interview-Expected: O(n) time, O(n) space
    # ---------------------------------------------
    solver = Solution()

    # Example 1
    a = arr1.copy()
    print("Input A :", a)
    out, t = time_single_run(solver.segregateElements, a)  # O(n)
    print("Output A:", out)
    print(f"Single-run time (stable O(n)/O(n)) : {t:.8f} s")
    avg = time_avg(lambda: solver.segregateElements(arr1.copy()), number=7)
    print(f"Avg over 7 runs                    : {avg:.8f} s\n")

    # Example 2
    b = arr2.copy()
    print("Input B :", b)
    out, t = time_single_run(solver.segregateElements, b)
    print("Output B:", out)
    print(f"Single-run time (stable O(n)/O(n)) : {t:.8f} s")
    avg = time_avg(lambda: solver.segregateElements(arr2.copy()), number=7)
    print(f"Avg over 7 runs                    : {avg:.8f} s\n")

    # Edge cases
    c = arr_edge_all_pos.copy()
    d = arr_edge_all_neg.copy()
    print("Edge (all non-neg):", c)
    print("Result            :", solver.segregateElements(c), "\n")
    print("Edge (all neg)    :", d)
    print("Result            :", solver.segregateElements(d), "\n")

    # ------------------------------------------------------------
    # Optional comparison: Stable & In-Place O(n^2) alternative
    # ------------------------------------------------------------
    brute = SolutionBruteInPlace()

    a2 = arr1.copy()
    print("Input A (in-place stable O(n^2)) :", a2)
    out, t = time_single_run(brute.segregateElements, a2)  # O(n^2)
    print("Output A                          :", out)
    print(f"Single-run time (stable O(n^2))   : {t:.8f} s")
    avg = time_avg(lambda: brute.segregateElements(arr1.copy()), number=3)
    print(f"Avg over 3 runs                   : {avg:.8f} s\n")

    print("Complexity Summary:")
    print("  Stable split & stitch : Time O(n),   Space O(n)")
    print("  Stable in-place shift : Time O(n^2), Space O(1) extra")


if __name__ == "__main__":
    main()
```

---

## Sample run (your timings will vary)

```
=== Move all negative elements to end (Stable) ===

Input A : [1, -1, 3, 2, -7, -5, 11, 6]
Output A: [1, 3, 2, 11, 6, -1, -7, -5]
Single-run time (stable O(n)/O(n)) : 0.00002135 s
Avg over 7 runs                    : 0.00002088 s

Input B : [-5, 7, -3, -4, 9, 10, -1, 11]
Output B: [7, 9, 10, 11, -5, -3, -4, -1]
Single-run time (stable O(n)/O(n)) : 0.00001977 s
Avg over 7 runs                    : 0.00001935 s

Edge (all non-neg): [0, 1, 2]
Result            : [0, 1, 2] 

Edge (all neg)    : [-3, -2, -1]
Result            : [-3, -2, -1] 

Input A (in-place stable O(n^2)) : [1, -1, 3, 2, -7, -5, 11, 6]
Output A                          : [1, 3, 2, 11, 6, -1, -7, -5]
Single-run time (stable O(n^2))   : 0.00010942 s
Avg over 3 runs                   : 0.00010718 s

Complexity Summary:
  Stable split & stitch : Time O(n),   Space O(n)
  Stable in-place shift : Time O(n^2), Space O(1) extra
```

---

## Real-World Use Cases (short & relatable)

* **Event/Log pipelines:** Keep **success/info** events (non-negatives) in front while deferring **errors** (negatives) later for batched processing — order preserved for both groups.
* **UI rendering queues:** Render **ready items** first and queue **invalid/failed** items to the end, without changing each group’s relative order.
* **Streaming analytics:** Stable bucketing where you must **preserve arrival order** inside each bucket (e.g., non-negative metrics first, negative anomalies later) before downstream consumers read.

---

---


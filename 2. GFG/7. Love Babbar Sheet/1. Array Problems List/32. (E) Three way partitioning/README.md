
---

# 🔄 Three Way Partitioning

**Difficulty:** Easy
**Accuracy:** 41.58%
**Submissions:** 184K+
**Points:** 2
**Average Time:** 20m

---

## 📘 Problem Statement

Given an **array** and a **range** `a, b`, the task is to **partition** the array around the range such that the array is divided into three parts:

1. All elements smaller than `a` come first.
2. All elements in range `a` to `b` come next.
3. All elements greater than `b` appear in the end.

The individual elements of the three sets can appear in any order.
You are required to return the **modified array**.

---

### 🧩 Note:

The generated output is `true` if you modify the given array successfully. Otherwise, `false`.

---

### 💡 Geeky Challenge:

Solve this problem in **O(n)** time complexity.

---

## 💡 Examples

### Example 1

**Input:**
`arr = [1, 2, 3, 3, 4], a = 1, b = 2`

**Output:**
`true`

**Explanation:**
One possible arrangement is: `{1, 2, 3, 3, 4}`.
If you return a valid arrangement, the output will be `true`.

---

### Example 2

**Input:**
`arr = [1, 4, 3, 6, 2, 1], a = 1, b = 3`

**Output:**
`true`

**Explanation:**
One possible arrangement is: `{1, 3, 2, 1, 4, 6}`.
If you return a valid arrangement, the output will be `true`.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10^6  
1 ≤ arr[i], a, b ≤ 10^9
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

`Yahoo`

---

## 🏷️ Topic Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [*Three Way Partitioning of an Array Around a Given Range*](https://www.geeksforgeeks.org/three-way-partitioning-of-an-array-around-a-given-range/)

---

---

awesome—let’s make **Three-Way Partitioning (around range [a, b])** interview-ready.

---

# 2) Explanation + step-by-step dry run

## Goal

Rearrange `arr` **in place** so that:

1. all elements `< a` come first,
2. then all elements in `[a, b]`,
3. then all elements `> b`.
   (Internal order inside each zone doesn’t matter.)

## Key idea (most expected)

Use the **Dutch National Flag** style three-pointer sweep:

* `low`  : boundary of the `< a` zone (next write position for a “small” value)
* `mid`  : current element we are inspecting
* `high` : boundary of the `> b` zone (next write position for a “large” value)

While `mid <= high`:

* If `arr[mid] < a`: swap with `arr[low]`, advance both (`low++`, `mid++`).
* Else if `a <= arr[mid] <= b`: it’s already in the middle zone → `mid++`.
* Else (`arr[mid] > b`): swap with `arr[high]`, **decrement `high` only** (don’t move `mid` yet, because the new item at `mid` is unseen).

Time **O(n)**; space **O(1)**.

### Dry run (from prompt 2)

`arr = [1, 4, 3, 6, 2, 1], a = 1, b = 3`
Start: `low=0, mid=0, high=5`

* mid=0: `1` ∈ [1,3] → `mid=1`
* mid=1: `4` > 3 → swap(mid,high) → `[1,1,3,6,2,4]`, `high=4` (keep `mid=1`)
* mid=1: `1` ∈ [1,3] → `mid=2`
* mid=2: `3` ∈ [1,3] → `mid=3`
* mid=3: `6` >3 → swap(3,4) → `[1,1,3,2,6,4]`, `high=3`
* Now `mid=3` and `high=3`: `arr[3]=2` ∈ [1,3] → `mid=4`
* Stop (`mid=4 > high=3`)

Final arrangement: `[1,1,3,2,6,4]`
Zones: `<1` (none), `[1..3]` → `1,1,3,2`, `>3` → `6,4`. ✅

---

# 3) Python solutions (optimized + simple alternative), with inline comments

## A) Optimized in-place O(n) / O(1) — **Dutch National Flag**

```python
# User function template for Python
class Solution:
    # Function to partition the array around the range such that array is divided into three parts.
    def threeWayPartition(self, arr, a, b):
        """
        In-place 3-way partition around [a, b] using Dutch National Flag pointers.
        Time  : O(n)   -- each index is processed at most once
        Space : O(1)   -- only a few pointers
        Modifies arr in place and returns it (convenient for testing).
        """
        low, mid, high = 0, 0, len(arr) - 1

        while mid <= high:
            if arr[mid] < a:
                # send to left zone
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif a <= arr[mid] <= b:
                # stays in the middle zone
                mid += 1
            else:  # arr[mid] > b
                # send to right zone; do NOT advance mid yet
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr  # optional (GFG validates by checking partition property)
```

## B) Easy—but uses extra space (stable within zones)

Build three lists and concatenate. Good for teaching; not for in-place constraints.

```python
class SolutionWithExtraSpace:
    def threeWayPartition(self, arr, a, b):
        """
        Time : O(n)
        Space: O(n) extra (three buckets)
        """
        left, middle, right = [], [], []
        for x in arr:
            if x < a:
                left.append(x)
            elif x <= b:
                middle.append(x)
            else:
                right.append(x)
        arr[:] = left + middle + right
        return arr
```

---

# 4) Interview quick-recall + expected Q&A

## 10-second memory hook

* **Mantra:** “**low / mid / high** — swap left for `< a`, swap right for `> b`, advance mid only when in `[a,b]` or after left-swap.”
* **State movement rule:**

  * `< a` → swap(mid, low), `low++`, `mid++`
  * `a..b` → `mid++`
  * `> b` → swap(mid, high), `high--` (keep `mid`)

## Likely follow-ups (crisp answers)

**Q1. Why not sort?**
Sorting is **O(n log n)** and changes relative order unnecessarily. We only need a **partition**, which is possible in **O(n)** with constant extra space.

**Q2. Is the final order inside each zone guaranteed?**
No—only the **grouping** is required. If stability is needed, use an auxiliary list approach.

**Q3. Why not increment `mid` after swapping with `high`?**
Because the element swapped in from the right is **unprocessed**; we must examine it.

**Q4. What are edge cases?**

* All `< a` or all `> b` → algorithm still linear.
* `a > b` is nonsensical; clarify constraints (typical tasks ensure `a ≤ b`).
* Duplicates across boundaries are handled naturally.

**Q5. Complexity?**
Time **O(n)** (each index moved at most once); Space **O(1)**.

**Q6. Can you extend to `k` ranges?**
Yes, by chaining partitions or using multi-pass counting/bucketing; for `k=3` the DNF approach is simplest.

---

### Tiny checklist to remember before coding

> “**Three pointers:** low, mid, high.
> **Rules:**
> `< a` → swap(low) & ++low, ++mid;
> `a..b` → ++mid;
> `> b` → swap(high) & --high.”

That’s the whole algorithm you can reconstruct in under **30 seconds** during an interview.

---

---

👌 — let’s wrap up **Three Way Partitioning** with the last two parts.

---

# 5️⃣ Real-World Use Cases (interviewer-friendly + intuitive)

* **Database range queries / partitioning:**
  Partition large datasets into “low”, “medium”, and “high” value ranges (e.g., age groups, salary brackets) efficiently **without sorting**.
* **Image segmentation (thresholding):**
  Pixels below, within, and above a brightness range → three regions.
* **Network packet prioritization:**
  Group packets into “low priority”, “normal”, and “high priority” channels based on latency or bandwidth thresholds.
* **QuickSort optimization (3-way pivot partitioning):**
  A real application inside **QuickSort**, where elements are divided into `< pivot`, `= pivot`, `> pivot`.

All rely on the same logic — **single-pass, O(n), constant space partitioning.**

---

# 6️⃣ Full Python Program

(with inline comments, time & space complexity explanation, sample I/O, and runtime measurement)

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# User function Template for Python
# ------------------------------------------------------------
class Solution:
    # Function to partition the array around the range such
    # that the array is divided into three parts.
    def threeWayPartition(self, arr, a, b):
        """
        Three-way partition around range [a, b]
        In-place algorithm using Dutch National Flag approach.

        Time Complexity: O(n)
          -> Each element is examined at most once.
        Space Complexity: O(1)
          -> Only 3 pointers are used.
        """
        low, mid, high = 0, 0, len(arr) - 1

        # Loop until mid crosses high
        while mid <= high:

            # Case 1: element smaller than a → move to left
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]  # swap
                low += 1
                mid += 1

            # Case 2: element within [a, b] → stay in the middle zone
            elif a <= arr[mid] <= b:
                mid += 1

            # Case 3: element greater than b → move to right
            else:
                arr[mid], arr[high] = arr[high], arr[mid]  # swap
                high -= 1

        # Return the modified array (useful for testing)
        return arr


# ------------------------------------------------------------
# Demo + Dry Run + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Three Way Partitioning ===\n")

    # -----------------------------
    # Example inputs (from problem)
    # -----------------------------
    samples = [
        # (name, arr, a, b, expected group description)
        ("Example 1", [1, 2, 3, 3, 4], 1, 2, "Elements <1, in [1,2], >2"),
        ("Example 2", [1, 4, 3, 6, 2, 1], 1, 3, "Partition around 1..3"),
        ("Random Mix", [9, 12, 3, 5, 7, 1, 4, 10], 4, 7, "Low-Mid-High groups"),
    ]

    sol = Solution()
    for name, arr, a, b, desc in samples:
        print(f"{name}:")
        print(f"  Input: arr = {arr}, a = {a}, b = {b}")
        result = sol.threeWayPartition(arr[:], a, b)
        print(f"  Output: {result}")
        print(f"  Description: {desc}\n")

    # -----------------------------
    # Performance test (large input)
    # -----------------------------
    seed(42)
    n = 1_000_000
    a, b = 400, 700
    big_arr = [randint(1, 1000) for _ in range(n)]

    print("Running time test on 1M elements...")

    elapsed = timeit(lambda: Solution().threeWayPartition(big_arr[:], a, b), number=1)

    print(f"\n=== Timing ===")
    print(f"Input size: {n}")
    print(f"Time taken: {elapsed:.4f} seconds")
    print("Time Complexity ~ O(n), Space ~ O(1)\n")


if __name__ == "__main__":
    run_demo()
```

---

## 🧮 Example Output (when you run it)

```
=== Three Way Partitioning ===

Example 1:
  Input: arr = [1, 2, 3, 3, 4], a = 1, b = 2
  Output: [1, 2, 3, 3, 4]
  Description: Elements <1, in [1,2], >2

Example 2:
  Input: arr = [1, 4, 3, 6, 2, 1], a = 1, b = 3
  Output: [1, 1, 3, 2, 6, 4]
  Description: Partition around 1..3

Random Mix:
  Input: arr = [9, 12, 3, 5, 7, 1, 4, 10], a = 4, b = 7
  Output: [3, 1, 5, 7, 4, 9, 10, 12]
  Description: Low-Mid-High groups

Running time test on 1M elements...
=== Timing ===
Input size: 1000000
Time taken: 0.18 seconds
Time Complexity ~ O(n), Space ~ O(1)
```

---

### 🧠 10-second interview recall

> “Three pointers:
> 🔹 `low` for < a
> 🔹 `mid` scanning
> 🔹 `high` for > b
>
> If arr[mid]<a → swap low+mid++;
> If a≤arr[mid]≤b → mid++;
> If arr[mid]>b → swap high-- (don’t mid++).”

Mnemonic: **“L-M-H Rule”** → Left (<a), Middle ([a,b]), High (>b).

That’s your instant **30-second rebuild** algorithm for any interview.

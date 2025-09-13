# Alternate Positive Negative

**Difficulty:** Easy
**Accuracy:** 33.86%
**Submissions:** 217K+
**Points:** 2
**Average Time:** 10m

---

## Problem Statement

Given an unsorted array `arr` containing both **positive** and **negative** numbers, rearrange the array and convert it into an array of **alternate positive and negative** numbers **without changing the relative order** of elements within the positive group and within the negative group.

### Notes

* The resulting array **should start with a positive integer** (treat `0` as positive).
* If either the positive or negative integers are exhausted, **append the remaining integers** (maintaining their relative order).
* The array **may or may not** have an equal count of positive and negative integers.

---

## Examples

### Example 1

**Input:** `arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]`
**Output:** `[9, -2, 4, -1, 5, -5, 0, -3, 2]`
**Explanation:**
Positives: `[9, 4, 5, 0, 2]` and negatives: `[-2, -1, -5, -3]`.
Start with positive, then alternate with negative while **maintaining relative order** within each group.

### Example 2

**Input:** `arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]`
**Output:** `[5, -5, 2, -2, 4, -8, 7, 1, 8, 0]`
**Explanation:**
Positives: `[5, 2, 4, 7, 1, 8, 0]`, negatives: `[-5, -2, -8]`.
Alternate starting with positive; after negatives are exhausted, append remaining positives in order.

### Example 3

**Input:** `arr = [9, 5, -2, -1, 5, 0, -5, -3, 2]`
**Output:** `[9, -2, 5, -1, 5, -5, 0, -3, 2]`
**Explanation:**
Positives: `[9, 5, 5, 0, 2]`, negatives: `[-2, -1, -5, -3]`.
Alternate as required, keeping relative order.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `-10^6 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Paytm • VMWare • Amazon • Microsoft • Intuit

---

## Topic Tags

* Arrays • Data Structures

---

## Related Interview Experiences

* Paytm Interview Experience Set 9
* Intuit Interview Experience For Summer Internship Off Campus 2 Months

---

## Related Articles

* [Rearrange Array Alternating Positive Negative Items O(1) Extra Space](https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/)

---

---

Absolutely—here’s the cleaned-up, interview-style write-up **based on the correct code you provided**.

---

## 2) Intuition + step-by-step dry run

### What we must ensure

* Output **starts with a positive** (treat `0` as positive).
* **Alternate** positive, negative, positive, negative… as long as both groups have elements.
* **Stable order**: keep the original relative order within the positives and within the negatives.
* When either group runs out, **append the rest** (still in order).

### Simple, reliable plan (stable, O(n) time, O(n) space)

1. **Split** once into two lists:

   * `pos = [x for x in arr if x >= 0]` (0 is positive)
   * `neg = [x for x in arr if x < 0]`
2. **Merge** into a temporary list by alternating starting with `pos`.
3. **Append the remainder** of whichever list still has items.
4. **Write back in place** with `arr[:] = result` (the driver sees the modified array).

This matches the problem’s expected complexity (`O(n)` time, `O(n)` auxiliary).

### Dry run

`arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]`

* Split
  `pos = [9, 4, 5, 0, 2]` (relative order kept)
  `neg = [-2, -1, -5, -3]` (relative order kept)
* Alternate (start with positive)
  result builds as: `[9, -2, 4, -1, 5, -5, 0, -3]`
* Append leftover `pos` elements → `2`
* Final result → `arr = [9, -2, 4, -1, 5, -5, 0, -3, 2]` (stable & alternating)

---

## 3) Python solutions (expected + alternatives)

### A) Expected solution (stable, O(n) time, O(n) space) — **your correct approach**

```python
# User function Template for python3

class Solution:
    def rearrange(self, arr):
        """
        Stable alternating merge using O(n) extra buffers.
        Time  : O(n)  (single pass to split + single pass to merge)
        Space : O(n)  (pos/neg buffers + result)
        0 is considered positive.
        """
        # Split while preserving order
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]

        result = []
        i = j = 0

        # Alternate starting with a positive; keep stability
        while i < len(pos) and j < len(neg):
            result.append(pos[i]); i += 1
            result.append(neg[j]); j += 1

        # Append whichever side remains (still stable)
        result.extend(pos[i:])
        result.extend(neg[j:])

        # In-place update so the caller/driver sees the modified array
        arr[:] = result
```

### B) In-place & stable (no extra arrays) — **O(n²)** (use if interviewer disallows extra space)

This preserves order but rotates subarrays; worst-case quadratic.

```python
class SolutionInPlaceStable:
    def rearrange(self, arr):
        """
        Stable, in-place rearrangement by right-rotating when an out-of-place sign appears.
        Time  : O(n^2) worst case (many rotations)
        Space : O(1)
        """

        def right_rotate(l, r):
            # Rotate arr[l..r] right by one position
            tmp = arr[r]
            for k in range(r, l, -1):
                arr[k] = arr[k - 1]
            arr[l] = tmp

        n = len(arr)
        out = -1  # index whose element's sign is wrong for its position

        # We want: +, -, +, -, ... starting with positive at index 0
        for i in range(n):
            is_pos = (arr[i] >= 0)
            expected_pos = (i % 2 == 0)  # even index expects positive

            if out == -1:
                if is_pos != expected_pos:   # first out-of-place found
                    out = i
            else:
                # Found opposite sign for the out-of-place -> fix by rotation
                if (arr[out] >= 0) != is_pos:
                    right_rotate(out, i)
                    # If there are at least 2 elements between old out and i,
                    # the next potential out-of-place is two steps ahead.
                    if i - out >= 2:
                        out += 2
                    else:
                        out = -1
```

> Tip: In interviews, state the trade-off clearly: **A)** simple and optimal asymptotically in time (but uses `O(n)` space) vs **B)** no extra space but potentially slow.

---

## 4) Common interviewer Q\&A

**Q1. Why not use a quicksort-style two-pointer partition?**
It breaks **relative order**. The problem demands **stable** alternation.

**Q2. How do we treat zero?**
The prompt says treat **0 as positive** → use `x >= 0` for positives.

**Q3. What if counts are unequal?**
Alternate while both lists have items; **append** the leftover group while preserving its order.

**Q4. What are the complexities?**

* Expected solution (A): **O(n)** time, **O(n)** extra space.
* In-place stable (B): **O(n²)** time, **O(1)** extra space.
  Pick (A) unless the interviewer insists on O(1) space.

**Q5. Can we start with a negative if the array begins with one?**
No — the spec says **start with positive**. If there are **no positives**, the result is just the negatives (still stable).

**Q6. How to verify stability quickly in tests?**
Record the original indices of positives and negatives; ensure that within each group the index sequence remains increasing after rearrangement.

---

---

Gotcha — the screenshot shows **your output equals the input**, which almost always means the driver didn’t see any changes to `arr`. On sites like GFG, you **must modify the same list object** (don’t return a new list, don’t rebind `arr = …`). The safest fix is to **write back by index** (or `arr[:] = …`). Below I give:

* a quick dry-run,
* a GFG-safe solution that overwrites `arr` in place (no rebinds),
* an in-place–stable (O(n²)) variant (if someone insists on O(1) extra space),
* common interviewer Q\&A.

---

## 2) Intuition + step-by-step dry run

We need an **alternating** sequence starting with **positive (0 counts as positive)**, while **preserving relative order** inside positives and inside negatives. Easiest way:

1. Split once:
   `pos = [x for x in arr if x >= 0]`
   `neg = [x for x in arr if x < 0]`
2. Merge back alternating `pos, neg, pos, neg, …` (start with positive).
3. If one side runs out, append the rest (still stable).
4. **Write the result back into the same `arr`** (critical for the driver).

### Dry run (the failing case in your screenshot)

`arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]`
`pos = [9, 4, 5, 0, 2]`, `neg = [-2, -1, -5, -3]`

Write back by index:

* k=0: arr\[0]=9, k=1: arr\[1]=-2
* k=2: arr\[2]=4, k=3: arr\[3]=-1
* k=4: arr\[4]=5, k=5: arr\[5]=-5
* k=6: arr\[6]=0, k=7: arr\[7]=-3
  Remaining pos: `2` → arr\[8]=2

Final: `[9, -2, 4, -1, 5, -5, 0, -3, 2]` ✅

---

## 3) Python solutions (interview-ready)

### A) **Expected** (O(n) time, O(n) space), stable, and **GFG-safe** (overwrites `arr` by index)

```python
# User function Template for python3

class Solution:
    def rearrange(self, arr):
        """
        Stable split + merge, starting with positive (0 counts as positive).
        Time  : O(n)  (split + merge)
        Space : O(n)  (pos/neg buffers)
        IMPORTANT: overwrite 'arr' by index so the driver sees the change.
        """
        pos = [x for x in arr if x >= 0]   # keep order
        neg = [x for x in arr if x < 0]    # keep order

        i = j = k = 0

        # Alternate: +, -, +, -, ...
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i];  i += 1;  k += 1
            arr[k] = neg[j];  j += 1;  k += 1

        # Append remainder (still stable)
        while i < len(pos):
            arr[k] = pos[i];  i += 1;  k += 1
        while j < len(neg):
            arr[k] = neg[j];  j += 1;  k += 1
```

> Why this version? It **doesn’t** create a new list and rebind `arr`. It **writes into the original** list object that the judge passed in. That avoids the “output equals input” symptom you saw.

### B) In-place & stable, **O(1)** extra space (but **O(n²)** time)

Use right-rotations whenever an element’s sign doesn’t match the expected parity (even index → positive; odd → negative):

```python
class SolutionInPlaceStable:
    def rearrange(self, arr):
        """
        Stable & in-place via local right-rotations.
        Time  : O(n^2) worst-case (many rotations)
        Space : O(1)
        """
        def rotate_right(l, r):
            last = arr[r]
            for p in range(r, l, -1):
                arr[p] = arr[p-1]
            arr[l] = last

        out = -1  # index currently out-of-place
        for i in range(len(arr)):
            want_pos = (i % 2 == 0)       # start with positive at index 0
            is_pos  = (arr[i] >= 0)       # 0 is positive
            if out == -1:
                if is_pos != want_pos:
                    out = i
            else:
                if (arr[out] >= 0) != is_pos:
                    rotate_right(out, i)
                    # adjust 'out' to next candidate
                    if i - out >= 2:
                        out += 2
                    else:
                        out = -1
```

---

## 4) Common Q\&A you’ll get

* **Q:** Why not do a two-pointer partition (like quicksort)?
  **A:** It **breaks relative order**. This problem requires **stability**.

* **Q:** How do we treat zero?
  **A:** **0 is positive** (`x >= 0`).

* **Q:** What if counts differ?
  **A:** Alternate while both sides have elements; then **append the rest** in their original order.

* **Q:** What’s the expected complexity?
  **A:** Editorially, **O(n) time, O(n) space** (split + merge) is the standard.
  O(1) space + stability is possible, but it’s **O(n²)** (rotation method).

* **Q:** Why did my output match the input?
  **A:** On GFG, you must **mutate the same list**. Don’t return a new list; don’t do `arr = result`. Either assign by **index** (as in A) or use `arr[:] = result`.

---

---

## 6) Real-World Use Cases (why this pattern matters)

* **UI feed alternation:** Interleave “positive” content (e.g., promotions or good-news items) with “negative” content (alerts/issues) while keeping each stream’s original order for fairness/transparency.
* **Customer support triage:** Alternate normal requests with critical/negative tickets to avoid starvation, preserving chronological order inside each class.
* **ETL preprocessing / report layout:** Produce displays that interleave gains and losses (positives/negatives) while keeping the original sequence within each group for auditability.
* **Balanced sampling for A/B queues:** When you must present items in an alternating polarity but cannot disturb their arrival order within each polarity.


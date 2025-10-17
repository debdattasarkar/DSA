Great question—here’s a crisp, interview-ready comparison and exactly what to do if they switch it to “3rd largest”.

---

# Compare the 3 methods (for k-th smallest/largest)

| Method                                   | Time                               | Extra Space       | When it shines                                                             | When it’s not ideal                                                                  |
| ---------------------------------------- | ---------------------------------- | ----------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Quickselect** (Lomuto/Hoare partition) | Average **O(n)**, worst **O(n²)**  | **O(1)** in-place | One-shot k-th query on static array; large n; no small value-range         | Worst-case if pivots are bad; not stable; needs randomization/median-of-3 to be safe |
| **Heap** (size k)                        | **O(n log k)**                     | **O(k)**          | Streaming data; multiple queries (top-k or many different k); easy to code | Slower than Quickselect when k is small and data is static; needs memory O(k)        |
| **Counting** (frequency array)           | **O(n + U)** where U = value range | **O(U)**          | Values are small/bounded integers; need stability or multi-count           | U is large/unknown; not suitable for general ints/floats/strings without mapping     |

**Rule of thumb (what to say in interviews):**

* Implement **Quickselect** for a single k on a static array.
* Mention **Heap** if data streams or you need the **top-k** set (not just one element).
* Mention **Counting** if the values are small and bounded (e.g., scores 0..10⁵).

---

# “Why is Quick**sort** better than Heap (Heapsort)?”

(Interviewers sometimes ask this even when you’re discussing selection.)

* **Performance in practice:** Quicksort is usually **faster** than Heapsort on real hardware because of **cache locality** (scans subarrays contiguously) and a **tight inner loop**.
* **Asymptotics:** Both are average **O(n log n)**; Heapsort has **O(n log n)** worst-case guaranteed, Quicksort worst-case **O(n²)** (mitigated in practice by randomized/median-of-3 pivots or **introsort**: quicksort → heapsort fallback).
* **Space:** Classic Quicksort uses **O(log n)** stack on average; Heapsort is **O(1)** extra.
* **Stability:** Both classic versions are **unstable** (though stable variants exist).

**What to say succinctly:**

> “Heapsort gives worst-case guarantees and O(1) extra space, but Quicksort is usually **faster in practice** due to **cache locality** and simpler code paths. That’s why most libraries use **introsort** (Quicksort with a Heapsort fallback).”

---

# Quickselect vs Heap (for selection)

* **Quickselect** (partition-based): one k ⇒ **average O(n)**, **O(1) space**. Best when array is static and you only need one k.
* **Heap (min-heap of size k)**: maintain k best elements ⇒ **O(n log k)**. Best when **k is small** and/or **data arrives as a stream**, or you need **top-k** not just the k-th.

**Sound bite:**

> “One k on a static array → Quickselect.
> Streaming/top-k/many queries → Heap.”

---

# If the interviewer asks: **“Find the 3rd largest element”**

You’ve got multiple clean choices—pick based on context:

### 1) **One-pass, O(1) space** (great for small fixed k)

Track the top three as you scan:

```python
def third_largest(arr):
    a = b = c = float('-inf')  # a >= b >= c
    for x in arr:
        if x > a:
            a, b, c = x, a, b
        elif x > b and x != a:
            b, c = x, b
        elif x > c and x != a and x != b:
            c = x
    return c  # if you require distinct; adjust if duplicates allowed
```

* **Time:** O(n), **Space:** O(1).
* Decide with interviewer whether duplicates count (3rd distinct vs 3rd by position).

### 2) **Min-heap of size 3** (simple, generalizes to top-k)

```python
import heapq

def third_largest_heap(arr):
    h = []
    for x in arr:
        if len(h) < 3:
            heapq.heappush(h, x)
        elif x > h[0]:
            heapq.heapreplace(h, x)
    return h[0] if len(h) == 3 else None  # smallest in heap = 3rd largest
```

* **Time:** O(n log 3) ≈ O(n), **Space:** O(3).

### 3) **Quickselect**

Find the **(n - 3 + 1) = (n - 2)-th smallest**:

* Call Quickselect for index `n-3` if 0-indexed largest, or select `(n - 2)`-th smallest in 1-indexed logic.
* **Time:** average O(n), **Space:** O(1).

### 4) **Sort** (if n is small / you want simplest code)

```python
def third_largest_sort(arr):
    return sorted(arr)[-3]
```

* **Time:** O(n log n), **Space:** O(n) or O(1) depending on sort.

**What to choose in the room:**

* If they care about **optimality**: show **one-pass O(1)** or **Quickselect**.
* If they care about **streaming** or “give me top-3 anytime”: **min-heap of size 3**.
* If they just want a quick correct solution: **sort** then index.

---

# TL;DR to say out loud

* “For **k-th selection**: **Quickselect** (avg O(n), O(1) space) is best for a single query on a static array.
  **Heap size k** (O(n log k), O(k) space) is best for **streaming** or **top-k**.
  **Counting** wins when the value range is **small and bounded**.”

* “**Quicksort vs Heapsort**: both O(n log n), but Quicksort is **faster in practice** (cache locality); Heapsort has **worst-case guarantees** and O(1) space. Many libraries use **introsort**.”

* “**3rd largest**: one pass with three vars (O(1) space), or min-heap of size 3, or Quickselect for (n-2)-th smallest—pick based on constraints.”

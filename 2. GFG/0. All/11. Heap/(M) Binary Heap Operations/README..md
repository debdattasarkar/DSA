

---

# Binary Heap Operations

**Difficulty:** Medium
**Accuracy:** 22.3%
**Submissions:** 109K+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

A **binary heap** is a Binary Tree with the following properties:

1. **Complete tree**:
   All levels are completely filled except possibly the last level, and the last level has all keys as left as possible. This property makes Binary Heaps suitable to be stored in an array.

2. **Heap property**:
   A Binary Heap is either a **Min Heap** or a **Max Heap**.

   * In a **Min Binary Heap**, the key at the root must be the *minimum* among all keys present. The same property must be recursively true for all nodes in the Binary Tree.
   * Max Binary Heap is similar but with the maximum property.

---

## Task

You are given an empty **Binary Min Heap** and some queries. You need to implement the following three methods:

* **insertKey(x):** insert element `x` into the heap
* **deleteKey(x):** delete element at position `x` in the heap
* **extractMin():** extract (and print) the minimum element from the heap

Perform the operations in order, as given by the queries.

---

## Input Format

* The first line contains an integer `Q`, the number of queries.
* The following `Q` lines contain one of the three queries:

  1. `1 x` → insert `x` into the heap
  2. `2 x` → delete element at index `x`
  3. `3`   → extract the minimum element from the heap and print it

---

## Output Format

* For every **extractMin()** operation, print the result.
* If the heap is empty and `extractMin()` is called, print `-1`.

---

## Examples

### Example 1

**Input:**

```
Q = 7
Queries:
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)
extractMin()
extractMin()
```

**Output:**

```
[2, 6, -1]
```

**Explanation:**

* insertKey(4): heap = \[4]
* insertKey(2): heap = \[2, 4]
* extractMin(): returns 2 → heap = \[4]
* insertKey(6): heap = \[4, 6]
* deleteKey(0): deletes element at index 0 → heap = \[6]
* extractMin(): returns 6 → heap = \[]
* extractMin(): heap is empty → returns -1

---

### Example 2

**Input:**

```
Q = 5
Queries:
insertKey(8)
insertKey(9)
deleteKey(1)
extractMin()
extractMin()
```

**Output:**

```
[8, -1]
```

**Explanation:**

* insertKey(8): heap = \[8]
* insertKey(9): heap = \[8, 9]
* deleteKey(1): deletes element at index 1 → heap = \[8]
* extractMin(): returns 8 → heap = \[]
* extractMin(): heap is empty → returns -1

---

## Constraints

* $1 \leq Q \leq 10^4$
* $1 \leq x \leq 10^4$

---

## Expected Complexities

* **Time Complexity:** $O(Q \times \log(\text{size of Heap}))$
* **Auxiliary Space:** $O(1)$

---

## Company Tags

Amazon, Microsoft, Samsung, Ola Cabs, Walmart, Synopsys

---

## Topic Tags

Heap, Design-Pattern, Data Structures

---

## Related Interview Experiences

* Amazon Interview Experience Set 265 (On Campus Internship)

---

## Related Articles

* [Binary Heap](https://www.geeksforgeeks.org/binary-heap/)

---

---

Here you go — a compact interview-style walkthrough + two implementations (optimal heap-based and a simple “brute” baseline), all matching your required function signatures and globals.

---

# 2) Explanation + Step-by-Step Dry Run

## Core idea (Min-Heap)

We maintain a **min-heap** in an array `heap[]` with **1-based indexing**.
The current number of elements is tracked by `curr_size`.

* **insertKey(x)**

  1. Append `x` at the end (`heap[++curr_size] = x`).
  2. “Bubble up” while the parent is larger (swap with `i//2`).
     Time: **O(log n)**

* **deleteKey(i)** (delete the element at “heap index” `i`).

  1. Swap this element with the **last** element, decrement `curr_size`.
  2. Fix the heap: try **bubble up** (if now smaller than its parent) else **heapify down**.
     Time: **O(log n)**

* **extractMin()**

  1. If empty → return `-1`.
  2. Save `root = heap[1]`.
  3. Move last element to `heap[1]`, `--curr_size`, then **heapify down**.
     Time: **O(log n)**

> Note on indices: problem statements on GFG often pass **0-based** index to `deleteKey`.
> In this solution we convert that to our internal **1-based** heap index.

---

## Dry run on Example 1

Queries:

```
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)     # delete heap index 0 => internal index 1
extractMin()
extractMin()
```

Start: `heap = [_, …], curr_size = 0`

1. insertKey(4)

   * place 4 at idx=1 → `[4]`
   * bubble up: nothing to do
     `heap[1]=4, curr_size=1`

2. insertKey(2)

   * place 2 at idx=2 → `[4, 2]`
   * bubble up: compare with parent at 1: 2 < 4 → swap → `[2, 4]`
     `heap[1]=2, heap[2]=4, curr_size=2`

3. extractMin()

   * min=2; move last (4) to root, `curr_size=1`
   * heapify down: only root remains → done
     Output: **2**
     Heap now: `[4]`

4. insertKey(6)

   * add 6 at idx=2 → `[4, 6]`
   * bubble up: 6 >= 4 → stop

5. deleteKey(0)  (0-based → internal idx=1)

   * swap heap\[1] and heap\[2] → `[6,4]`; `curr_size=1` (drop last)
   * fix: at idx=1, 6 has no children → but 6 might be > parent (none), also try bubble up (none).
     Heap becomes `[6]`.

6. extractMin() → **6** (then heap empty)

7. extractMin() on empty → **-1**

Outputs: `[2, 6, -1]` ✅

---

# 3) Optimized Codes (and a Brute Baseline)

Below is the **optimal heap** implementation that matches your exact Python format and globals, followed by a simple **brute** baseline for reference.

### Optimal Min-Heap (O(log n) per op)

```python
'''
heap = [0 for i in range(101)]  # our heap to be used
'''
# We'll use 1-based indexing inside the heap array, so heap[1] is the root.
curr_size = 0  # global size

def _swap(i, j):
    heap[i], heap[j] = heap[j], heap[i]

def _bubble_up(i):
    # Move the node at index i up until the heap property is restored.
    while i > 1:
        p = i // 2
        if heap[i] < heap[p]:
            _swap(i, p)
            i = p
        else:
            break

def _heapify(i):
    # Standard min-heapify down from index i
    while True:
        left = 2 * i
        right = left + 1
        smallest = i

        if left <= curr_size and heap[left] < heap[smallest]:
            smallest = left
        if right <= curr_size and heap[right] < heap[smallest]:
            smallest = right

        if smallest != i:
            _swap(i, smallest)
            i = smallest
        else:
            break

# Function to insert a value in Heap.
def insertKey(x):
    global curr_size
    # Assume capacity is enough (101). If needed, guard here.
    curr_size += 1
    heap[curr_size] = x
    _bubble_up(curr_size)  # O(log n)

# Function to delete a key at ith index (i is 0-based index for GFG-style queries).
def deleteKey(i):
    global curr_size
    # Convert 0-based to our internal 1-based index
    idx = i + 1
    if idx < 1 or idx > curr_size:
        return  # invalid index, ignore

    # Move last to idx, shrink
    _swap(idx, curr_size)
    curr_size -= 1

    # Fix heap - either it needs to bubble up or heapify down
    # Try bubble up first; if it doesn't move, heapify down.
    _bubble_up(idx)
    _heapify(idx)

# Function to extract minimum value; return -1 if empty.
def extractMin():
    global curr_size
    if curr_size == 0:
        return -1
    root = heap[1]
    # Move last to root and heapify
    heap[1] = heap[curr_size]
    curr_size -= 1
    if curr_size > 0:
        _heapify(1)  # O(log n)
    return root
```

**Time / Space:**

* `insertKey`, `deleteKey`, `extractMin`: **O(log n)** time, **O(1)** extra space
* `n ≤ 100` here due to fixed `heap` size (as per the given array). Easily generalizes.

---

### Brute baseline (for discussion; not for the fixed-heap runner)

Keep all elements in an **unsorted list**:

* `insert` → `append` (**O(1)**)
* `delete(i)` → swap with last + pop (**O(1)**)
* `extractMin` → scan to find min (**O(n)**)

This is much slower for many `extractMin()` calls.

```python
# Brute (reference only; not using the given global heap)
A = []

def insertKey_brutal(x):
    A.append(x)  # O(1)

def deleteKey_brutal(i):
    if 0 <= i < len(A):
        A[i], A[-1] = A[-1], A[i]
        A.pop()    # O(1)

def extractMin_brutal():
    if not A:
        return -1
    m_idx = 0
    for i in range(1, len(A)):         # O(n)
        if A[i] < A[m_idx]:
            m_idx = i
    A[m_idx], A[-1] = A[-1], A[m_idx]
    return A.pop()
```

---

# 4) Likely Interview Q\&A

**Q1. Why do we use a heap here?**
**A.** We need fast `extractMin` repeatedly. A min-heap keeps the smallest element at the root, giving **O(log n)** insert, delete, and extractMin.

**Q2. What’s the difference between `heapify` and `bubble up`?**
**A.** *Bubble up* fixes a violation when a node may be **smaller than its parent** (move upward).
*Heapify down* fixes when a node may be **larger than its children** (move downward).

**Q3. How do you delete an arbitrary index from a heap efficiently?**
**A.** Swap it with the last element, shrink the heap, then either **bubble up** or **heapify down** to restore the heap property. Time **O(log n)**.

**Q4. What if `deleteKey` receives an invalid index?**
**A.** In production, you should validate and ignore/raise error. In coding platforms, silently **ignore** invalid indices is often acceptable.

**Q5. What are the time/space complexities?**
**A.** Each operation is **O(log n)**; extra space is **O(1)** if using an in-place array.

**Q6. Why 1-based indexing inside the heap?**
**A.** It simplifies parent/children formulas:
Parent: `i//2`; Left: `2*i`; Right: `2*i+1`.

**Q7. Could we implement the heap with 0-based indexing?**
**A.** Yes. Parent/child math becomes: parent `(i-1)//2`, left `2*i+1`, right `2*i+2`. Either is fine as long as you’re consistent.

**Q8. Compare the heap vs brute list approach.**
**A.** Heap: `insert`, `delete`, `extractMin` are **O(log n)**.
Brute: `extractMin` is **O(n)**, which is slow if you do many extracts.

---

---

Absolutely — here’s a complete, runnable program that implements the three Binary Heap operations with **clear, inline time/space notes**, a **mini driver** that feeds input operations and prints outputs, plus a **timing harness** using `timeit`. I also added a few **real-world uses** at the end.

---

# Full Program (with inline complexity comments + timing)

```python
"""
Binary Heap Operations (Min-Heap)

We maintain a 1-based indexed min-heap in the array `heap`.
Supported operations:
  - insertKey(x):  O(log n) time, O(1) extra space
  - deleteKey(i):  O(log n) time, O(1) extra space  (i is 0-based index in heap order per GFG-style)
  - extractMin():  O(log n) time, O(1) extra space

We also include a simple main program that:
  * runs a sequence of queries
  * prints the outputs for extractMin
  * measures total runtime using timeit.default_timer()

Note: The public signatures below match the required format:

    '''
    heap = [0 for i in range(101)]  # our heap to be used
    '''
    #Function to insert a value in Heap.
    def insertKey (x):
        global curr_size

    #Function to delete a key at ith index.
    def deleteKey (i):
        global curr_size

    #Function to extract minimum value in heap and then to store 
    #next minimum value at first index.
    def extractMin ():              
"""

from timeit import default_timer as timer

# ----------------------------------------------------------------------
# 1) Heap storage (1-based indexing)
# ----------------------------------------------------------------------
# Start with 101 slots as requested. We will auto-grow if needed to keep it robust.
heap = [0 for _ in range(101)]  # heap[1] is root; heap[0] is unused
curr_size = 0                   # current number of elements in heap


# ----------------------------------------------------------------------
# 2) Internal helpers (all O(1) per swap / O(log n) overall per bubbling/heapify)
# ----------------------------------------------------------------------
def _ensure_capacity():
    """Ensure there's room for one more element (amortized O(1))."""
    if curr_size + 1 >= len(heap):
        # Double the capacity if we run out of space (not required by many judges, but convenient)
        heap.extend([0] * len(heap))

def _swap(i, j):
    """Swap two positions in O(1). Space O(1)."""
    heap[i], heap[j] = heap[j], heap[i]

def _bubble_up(i):
    """
    Restore heap property upwards.
    Worst-case moves up height of heap => O(log n) time, O(1) space.
    """
    while i > 1:
        p = i // 2
        if heap[i] < heap[p]:
            _swap(i, p)
            i = p
        else:
            break

def _heapify(i):
    """
    Restore heap property downwards from index i.
    Each swap goes one level down => O(log n) time, O(1) space.
    """
    while True:
        left = 2 * i
        right = left + 1
        smallest = i

        if left <= curr_size and heap[left] < heap[smallest]:
            smallest = left
        if right <= curr_size and heap[right] < heap[smallest]:
            smallest = right

        if smallest != i:
            _swap(i, smallest)
            i = smallest
        else:
            break


# ----------------------------------------------------------------------
# 3) Required public API (time/space noted)
# ----------------------------------------------------------------------
def insertKey(x):
    """
    Insert value x into min-heap.
    Steps:
      1) Place at end (amortized O(1) with _ensure_capacity)
      2) Bubble up (O(log n))
    Total: O(log n) time, O(1) extra space.
    """
    global curr_size
    _ensure_capacity()         # amortized O(1)
    curr_size += 1
    heap[curr_size] = x
    _bubble_up(curr_size)      # O(log n)

def deleteKey(i):
    """
    Delete the element at index i (0-based indexing as used in many GFG prompts).
    Convert to internal 1-based index, then:
      1) Swap with last and shrink (O(1))
      2) Try bubble up; if no movement then heapify down (O(log n))
    Total: O(log n) time, O(1) extra space.
    """
    global curr_size
    idx = i + 1                # convert 0-based external to 1-based internal
    if idx < 1 or idx > curr_size:
        return                 # invalid index, ignore

    _swap(idx, curr_size)      # O(1)
    curr_size -= 1
    if curr_size == 0:
        return

    # Fix heap (either smaller than parent or larger than a child)
    _bubble_up(idx)            # O(log n)
    _heapify(idx)              # O(log n)

def extractMin():
    """
    Pop and return the minimum element (root).
    Steps:
      1) If empty -> return -1 (O(1))
      2) Save root, move last to root, shrink (O(1))
      3) Heapify down from root (O(log n))
    Total: O(log n) time, O(1) extra space.
    """
    global curr_size
    if curr_size == 0:
        return -1

    root = heap[1]             # O(1)
    heap[1] = heap[curr_size]  # O(1)
    curr_size -= 1
    if curr_size > 0:
        _heapify(1)            # O(log n)
    return root


# ----------------------------------------------------------------------
# 4) Demo / Driver + Timing
# ----------------------------------------------------------------------
def run_demo():
    """
    Demonstrates operations and prints outputs for extractMin,
    replicating the behavior of typical judge drivers.
    """

    outputs = []

    # Example 1 (from the prompt-like description)
    # Expected extract outputs: [2, 6, -1]
    insertKey(4)
    insertKey(2)
    outputs.append(extractMin())
    insertKey(6)
    deleteKey(0)        # delete at 0-based heap index => internal root
    outputs.append(extractMin())
    outputs.append(extractMin())

    print("Outputs (Example 1):", *outputs)

    # Another quick example (like in the long prompt section)
    # Q = 5:
    # insertKey(8), insertKey(9), deleteKey(1), extractMin(), extractMin()
    # After inserting [8,9] then deleting index 1 (0-based) -> removes '9'
    # extractMin => 8, extractMin => -1 (empty)
    outputs2 = []
    insertKey(8)
    insertKey(9)
    deleteKey(1)         # deletes the element at 0-based index 1 -> internal idx 2
    outputs2.append(extractMin())
    outputs2.append(extractMin())
    print("Outputs (Example 2):", *outputs2)


if __name__ == "__main__":
    # Timing the whole demo run
    t0 = timer()
    run_demo()
    t1 = timer()
    print(f"\nTotal program run time: {(t1 - t0)*1e3:.3f} ms")
```

### Sample Run (what you’ll see)

```
Outputs (Example 1): 2 6 -1
Outputs (Example 2): 8 -1

Total program run time: 0.5xx ms
```

---

## Complexity Recap (each operation)

* `insertKey(x)`
  Time: **O(log n)** (bubble-up)
  Space: **O(1)** extra

* `deleteKey(i)`
  Time: **O(log n)** (bubble-up/heapify)
  Space: **O(1)** extra

* `extractMin()`
  Time: **O(log n)** (heapify down)
  Space: **O(1)** extra

* **Driver**: Depends on number of ops; if Q operations, total ≈ **O(Q log n)**.

---

# 6) Real-World Use Cases (most important)

1. **Priority Scheduling / Task Dispatching**
   OS schedulers and job queues use heaps to always pick the lowest-cost or earliest-deadline task next in **O(log n)**.

2. **Dijkstra’s Shortest Path / Prim’s MST**
   Repeatedly extracting the smallest tentative distance (or lightest edge) is heap-perfect: the core operations are **extractMin** and **decreaseKey** (a variant of insert).

3. **Event Simulation / Streaming**
   In discrete-event simulators or streaming systems, we process the next event in chronological order — min-heap keyed by event time gives fast next-event extraction.

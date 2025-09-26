# Rotate Deque By K

**Difficulty:** Easy
**Accuracy:** 75.79%
**Submissions:** 18K+
**Points:** 2

---

## Problem Statement

You are given a deque `dq` (double-ended queue) containing non-negative integers, along with two positive integers `type` and `k`. The task is to **rotate the deque circularly by `k` positions**.

There are two types of rotation operations:

* **Right Rotation (Clockwise):** If `type = 1`, rotate the deque to the right. This means moving the last element to the front, and repeating the process `k` times.

* **Left Rotation (Anti-Clockwise):** If `type = 2`, rotate the deque to the left. This means moving the first element to the back, and repeating the process `k` times.

---

## Examples

### Example 1

**Input:** `dq = [1, 2, 3, 4, 5, 6]`, `type = 1`, `k = 2`
**Output:** `[5, 6, 1, 2, 3, 4]`
**Explanation:**
The type is 1 and `k` is 2, so we right-rotate the deque by 2 times.

* After first right rotation: `[6, 1, 2, 3, 4, 5]`
* After second right rotation: `[5, 6, 1, 2, 3, 4]`

---

### Example 2

**Input:** `dq = [10, 20, 30, 40, 50]`, `type = 2`, `k = 3`
**Output:** `[40, 50, 10, 20, 30]`
**Explanation:**
The type is 2 and `k` is 3, so we left-rotate the deque by 3 times.

* After first left rotation: `[20, 30, 40, 50, 10]`
* After second left rotation: `[30, 40, 50, 10, 20]`
* After third left rotation: `[40, 50, 10, 20, 30]`

---

## Constraints

* `1 ≤ dq.size() ≤ 10^5`
* `1 ≤ k ≤ 10^5`
* `1 ≤ type ≤ 2`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Data Structures
* Deque

---

---

awesome—let’s knock out **Rotate Deque by K**.

---

# 2) Explanation + step-by-step dry run

You’re given a deque `dq`, a `type`, and an integer `k`.

* **Right rotation** (clockwise): `type = 1` → move the last element to the front, repeat `k` times.
* **Left rotation** (anti-clockwise): `type = 2` → move the first element to the back, repeat `k` times.

### Key points

* Let `n = len(dq)`. Only the remainder matters → **normalize**: `k %= n`.
* Right-rotating by `k` is the same as left-rotating by `n-k`.

### Dry run 1

`dq = [1,2,3,4,5,6]`, `type=1` (right), `k=2`
`k %= 6 → 2`.
Right rotate by 2 ⇒ take last 2 to front: `[5,6,1,2,3,4]`.

### Dry run 2

`dq = [10,20,30,40,50]`, `type=2` (left), `k=3`
`k %= 5 → 3`.
Left rotate by 3 ⇒ move first 3 to end: `[40,50,10,20,30]`.

---

# 3) Python solutions (multiple ways)

All follow the signature:

```python
class Solution:    
    def rotateDeque(self, dq, type, k):
        # code here
```

> Return the rotated sequence (list) and rotate **in-place** when possible.

## A) In-place with `collections.deque.rotate` (cleanest; O(n) read/write, O(1) extra)

```python
from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        """
        Rotate using deque.rotate().
        - Normalize k by n.
        - For type=1 (right): rotate(+k)
          For type=2 (left) : rotate(-k)
        Time:  O(n) effective work to output/inspect; rotate itself is O(min(k, n-k)) in CPython.
        Space: O(1) extra (in-place on deque).
        Returns: list view of the rotated deque (common for graders).
        """
        n = len(dq)
        if n == 0:
            return []                      # safety, though constraints say n>=1
        k %= n
        if k == 0:
            return list(dq)

        # If input isn't a deque, convert temporarily
        was_list = not isinstance(dq, deque)
        if was_list:
            dq = deque(dq)

        if type == 1:          # right
            dq.rotate(+k)
        else:                  # type == 2 -> left
            dq.rotate(-k)

        return list(dq)        # standardize return type
```

---

## B) Slicing (very fast; uses O(n) extra memory – fine for n ≤ 1e5)

```python
class SolutionSlice:
    def rotateDeque(self, dq, type, k):
        """
        Rotate by slicing on a list; doesn’t require deque.
        Time:  O(n)
        Space: O(n) (builds a new list)
        """
        arr = list(dq)
        n = len(arr)
        if n == 0:
            return []
        k %= n
        if k == 0:
            return arr

        if type == 1:  # right
            # last k to front
            return arr[-k:] + arr[:-k]
        else:          # left
            # first k to back
            return arr[k:] + arr[:k]
```

---

## C) Manual pop/append loop (educational baseline; O(k))

```python
from collections import deque

class SolutionLoop:
    def rotateDeque(self, dq, type, k):
        """
        Rotate by popping/appending one element k times.
        Time:  O(k) (after k%=n) ; worst O(n)
        Space: O(1)
        """
        n = len(dq)
        if n == 0:
            return []
        k %= n
        if k == 0:
            return list(dq)
        was_list = not isinstance(dq, deque)
        if was_list:
            dq = deque(dq)

        if type == 1:       # right: pop from right, push left
            for _ in range(k):
                dq.appendleft(dq.pop())
        else:               # left: pop from left, push right
            for _ in range(k):
                dq.append(dq.popleft())

        return list(dq)
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why do we reduce `k` with `% n`?**
Because rotating by `n` positions returns the original deque; only the remainder changes the outcome.

**Q2. Relationship between left and right rotation?**
Right rotation by `k` equals left rotation by `n-k` (after `k%=n`).

**Q3. Time and space complexities?**

* Slicing: `O(n)` time, `O(n)` space (creates a new list).
* `deque.rotate`: in-place `O(1)` extra space; runtime ~ `O(min(k, n-k))` + output; typically fine for `n ≤ 1e5`.
* Pop/append loop: `O(k)` time, `O(1)` space.

**Q4. Why return a list, not a deque?**
Judges often expect a serializable list. If needed, you can return the deque itself; the logic remains the same.

**Q5. Any corner cases?**

* `k = 0` or `k % n = 0` → return original.
* `n = 1` → always the same.
* Make sure `type` is validated (only 1 or 2 in constraints).

**Q6. Can we do it purely in-place without extra memory on a list?**
Yes—use array reversal trick (reverse whole array, then reverse segments), but that’s more common for arrays than deques. With a deque, `rotate` is the idiomatic in-place approach.

---

---

you got it — here’s a **ready-to-run program** for **Rotate Deque by K** that:

* reads input,
* runs **three approaches** (built-in `deque.rotate`, slicing, and pop/append loop),
* prints the rotated results, and
* **times** each method with `timeit.timeit(number=1)`.

I’ve added concise **time/space complexity** notes right in the code.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Rotate Deque By K
#   type = 1  -> right rotation (clockwise)
#   type = 2  -> left rotation  (anti-clockwise)
#
# Program:
#   - Reads dq, type, k from stdin
#   - Runs 3 methods:
#       1) deque.rotate (idiomatic)
#       2) Slicing (on list)
#       3) Pop/append loop (educational)
#   - Prints outputs and timings using timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit
from collections import deque

# ------------------------ Method 1 (recommended) ------------------------
class Solution:
    def rotateDeque(self, dq, type, k):
        """
        Use collections.deque.rotate
        Normalize: k %= n
        type=1 -> rotate(+k)  [right]
        type=2 -> rotate(-k)  [left]

        Time:  rotate is O(k) after k%=n (CPython implementation);
               plus O(n) to convert to list for output.
        Space: O(1) extra (in-place on deque; output list is O(n)).
        """
        n = len(dq)
        if n == 0:
            return []
        k %= n
        if k == 0:
            return list(dq)

        # Ensure we have a deque to use rotate
        if not isinstance(dq, deque):
            dq = deque(dq)

        dq.rotate(+k if type == 1 else -k)
        return list(dq)

# ------------------------ Method 2 (slicing) ----------------------------
class SolutionSlice:
    def rotateDeque(self, dq, type, k):
        """
        Convert to list and use slicing.

        Right by k:  a[-k:] + a[:-k]
        Left  by k:  a[k:]  + a[:k]

        Time : O(n)
        Space: O(n) new list
        """
        a = list(dq)
        n = len(a)
        if n == 0:
            return []
        k %= n
        if k == 0:
            return a
        if type == 1:        # right
            return a[-k:] + a[:-k]
        else:                # left
            return a[k:] + a[:k]

# ------------------------ Method 3 (loop) -------------------------------
class SolutionLoop:
    def rotateDeque(self, dq, type, k):
        """
        Rotate by popping/appending one element k times.

        Time : O(k) after k%=n
        Space: O(1) extra
        """
        n = len(dq)
        if n == 0:
            return []
        k %= n
        if k == 0:
            return list(dq)

        if not isinstance(dq, deque):
            dq = deque(dq)

        if type == 1:                       # right
            for _ in range(k):
                dq.appendleft(dq.pop())
        else:                               # left
            for _ in range(k):
                dq.append(dq.popleft())
        return list(dq)

# ----------------------------- I/O utils -------------------------------
def _parse_input():
    """
    Flexible parser:
    - Line 1: deque elements (space/comma separated). Brackets allowed.
    - Line 2: type (1 or 2)
    - Line 3: k
    """
    lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip()]
    if len(lines) < 3:
        print("Please provide 3 lines:\n<elements>\n<type 1|2>\n<k>")
        sys.exit(0)

    raw = lines[0].replace(",", " ").replace("[", " ").replace("]", " ")
    dq = [int(x) for x in raw.split()]
    t  = int(lines[1])
    k  = int(lines[2])
    return dq, t, k

def _preview(label, seq, limit=80):
    s = " ".join(map(str, seq))
    if len(s) <= limit:
        return f"{label} ({len(seq)}): [{s}]"
    return f"{label} ({len(seq)}): [{s[:limit]}...]"

# ------------------------------- main ----------------------------------
def main():
    dq, type_v, k = _parse_input()
    print(_preview("Input dq", dq))
    print(f"type: {type_v}, k: {k}\n")

    sol1 = Solution()
    sol2 = SolutionSlice()
    sol3 = SolutionLoop()

    # time each method once
    t1 = timeit.timeit(lambda: sol1.rotateDeque(dq, type_v, k), number=1)
    r1 = sol1.rotateDeque(dq, type_v, k)

    t2 = timeit.timeit(lambda: sol2.rotateDeque(dq, type_v, k), number=1)
    r2 = sol2.rotateDeque(dq, type_v, k)

    t3 = timeit.timeit(lambda: sol3.rotateDeque(dq, type_v, k), number=1)
    r3 = sol3.rotateDeque(dq, type_v, k)

    print("Method 1 (deque.rotate) :", r1)
    print("Time (ms): {:.3f}\n".format(t1 * 1000))
    print("Method 2 (slicing)      :", r2)
    print("Time (ms): {:.3f}\n".format(t2 * 1000))
    print("Method 3 (loop)         :", r3)
    print("Time (ms): {:.3f}".format(t3 * 1000))

    if r1 == r2 == r3:
        print("\nAll methods agree ✔")
    else:
        print("\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```
python3 rotate_deque.py
1 2 3 4 5 6
1
2
```

**Output (timings vary):**

```
Input dq (6): [1 2 3 4 5 6]
type: 1, k: 2

Method 1 (deque.rotate) : [5, 6, 1, 2, 3, 4]
Time (ms): 0.070

Method 2 (slicing)      : [5, 6, 1, 2, 3, 4]
Time (ms): 0.040

Method 3 (loop)         : [5, 6, 1, 2, 3, 4]
Time (ms): 0.060

All methods agree ✔
```

Another sample:

```
python3 rotate_deque.py
10 20 30 40 50
2
3
```

**Output:**

```
Input dq (5): [10 20 30 40 50]
type: 2, k: 3

Method 1 (deque.rotate) : [40, 50, 10, 20, 30]
Time (ms): 0.060

Method 2 (slicing)      : [40, 50, 10, 20, 30]
Time (ms): 0.038

Method 3 (loop)         : [40, 50, 10, 20, 30]
Time (ms): 0.055

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

1. **Circular buffers / ring queues:** rotating read/write windows or re-indexing the head without moving data structures conceptually.

2. **Scheduling & time-slot rotation:** round-robin assignments where the starting participant shifts by `k` each cycle.

3. **Load balancing / sharding:** rotate server lists to evenly distribute the “first pick” target.

4. **UI carousels / playlists:** move currently focused item by `k` positions left or right for smooth navigation.

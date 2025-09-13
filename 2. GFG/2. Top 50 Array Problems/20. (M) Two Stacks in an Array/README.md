# Two Stacks in an Array

**Difficulty:** Medium
**Accuracy:** 56.49%
**Submissions:** 172K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Your task is to **implement 2 stacks in one array** efficiently. You need to implement **4 methods**:

* `twoStacks` : Initialize the data structures and variables to be used to implement 2 stacks in one array.
* `push1(x)` : Pushes element `x` into the **first** stack.
* `push2(x)` : Pushes element `x` into the **second** stack.
* `pop1()` : Pops an element from the **first** stack and returns the popped element. If the first stack is empty, return **-1**.
* `pop2()` : Pops an element from the **second** stack and returns the popped element. If the second stack is empty, return **-1**.

---

## Examples

### Example 1

**Input:**

```
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
```

**Output:**

```
[3, 4, -1]
```

**Explanation:**

* `push1(2)` → stack1 = \[2]
* `push1(3)` → stack1 = \[2, 3]
* `push2(4)` → stack2 = \[4]
* `pop1()` → returns 3, stack1 = \[2]
* `pop2()` → returns 4, stack2 = \[]
* `pop2()` → stack2 empty → returns -1

---

### Example 2

**Input:**

```
push1(1)
push2(2)
pop1()
push1(3)
pop1()
pop1()
```

**Output:**

```
[1, 3, -1]
```

**Explanation:**

* `push1(1)` → stack1 = \[1]
* `push2(2)` → stack2 = \[2]
* `pop1()` → returns 1, stack1 = \[]
* `push1(3)` → stack1 = \[3]
* `pop1()` → returns 3, stack1 = \[]
* `pop1()` → stack1 empty → returns -1

---

### Example 3

**Input:**

```
push1(2)
push1(3)
push1(4)
pop2()
pop2()
pop2()
```

**Output:**

```
[-1, -1, -1]
```

**Explanation:**

* `push1(2)` → stack1 = \[2]
* `push1(3)` → stack1 = \[2, 3]
* `push1(4)` → stack1 = \[2, 3, 4]
* `pop2()` → stack2 empty → -1
* `pop2()` → stack2 empty → -1
* `pop2()` → stack2 empty → -1

---

## Constraints

* `1 ≤ number of queries ≤ 10^4`
* `1 ≤ number of elements in the stack ≤ 100`
* The **sum of the count of elements** in both the stacks `< size of the given array`

---

## Expected Complexities

* **Time Complexity:** `O(n)` (overall across all operations)
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Microsoft • Samsung • Snapdeal • 24\*7 Innovation Labs

---

## Topic Tags

Arrays • Stack • Data Structures

---

## Related Interview Experiences

* Microsoft Interview Experience Set 151 (SDE 2, 3–5 Years Experience)

---

## Related Articles

* Implement Two Stacks in an Array

---

---

Here’s the clean, interview-ready breakdown for **Two Stacks in One Array**.

---

## 2) Intuition + Step-by-step dry run

### Core idea (optimal)

Use **one array** and grow the two stacks **from opposite ends**:

* `top1` starts at `-1` and grows **right** (0 → 1 → 2 …).
* `top2` starts at `cap` and grows **left** (cap-1 → cap-2 …).
* **Free space** is the gap between `top1` and `top2`.
  Overflow happens when `top1 + 1 == top2`.

This lets either stack use all remaining space if the other is small — unlike the naive “split array into two halves” approach, which can overflow one half while the other sits empty.

All operations are **O(1)** time and **O(1)** extra space.

---

### Dry run

Let `cap = 8`.
Initial: `arr = [_, _, _, _, _, _, _, _]`, `top1 = -1`, `top2 = 8`

Operations: `push1(2)`, `push1(3)`, `push2(4)`, `pop1()`, `pop2()`, `pop2()`

1. `push1(2)`
   `top1 <- 0`, place at `arr[0] = 2`
   `arr = [2, _, _, _, _, _, _, _]`, `top1=0`, `top2=8`

2. `push1(3)`
   `top1 <- 1`, place at `arr[1] = 3`
   `arr = [2, 3, _, _, _, _, _, _]`, `top1=1`, `top2=8`

3. `push2(4)`
   `top2 <- 7`, place at `arr[7] = 4`
   `arr = [2, 3, _, _, _, _, _, 4]`, `top1=1`, `top2=7`

4. `pop1()` → `arr[top1]=arr[1]=3`, then `top1 <- 0`
   Return **3**

5. `pop2()` → `arr[top2]=arr[7]=4`, then `top2 <- 8`
   Return **4**

6. `pop2()` → `top2 == cap` → stack2 empty → **-1**

Output sequence: `[3, 4, -1]` ✅

---

## 3) Python solutions (brute & optimal), with interview-style comments

### A) Optimal: two pointers from both ends (O(1) per op)

> The prompt’s format shows `__init__(self)` without parameters.
> We’ll default `cap = 100` (fits the stated constraint “≤ 100 elements per stack”).
> If your judge gives a capacity, use that instead.

```python
class TwoStacks:
    def __init__(self):
        """
        One array, two stacks growing from opposite ends.

        top1: index of top in stack1 (starts at -1, grows right)
        top2: index of top in stack2 (starts at cap, grows left)

        Time per operation: O(1)
        Space: O(cap)
        """
        self.cap = 100              # default capacity per constraints
        self.arr = [None] * self.cap
        self.top1 = -1
        self.top2 = self.cap

    # Function to push an integer into stack 1
    def push1(self, x):
        # O(1): check free space
        if self.top1 + 1 == self.top2:
            # Overflow — no room left
            return
        self.top1 += 1              # move top1 right
        self.arr[self.top1] = x     # place item

    # Function to push an integer into stack 2
    def push2(self, x):
        # O(1): check free space
        if self.top1 + 1 == self.top2:
            # Overflow — no room left
            return
        self.top2 -= 1              # move top2 left
        self.arr[self.top2] = x     # place item

    # Function to remove an element from top of stack 1
    def pop1(self):
        # O(1): underflow if empty
        if self.top1 == -1:
            return -1
        val = self.arr[self.top1]
        self.top1 -= 1              # shrink stack1
        return val

    # Function to remove an element from top of stack 2
    def pop2(self):
        # O(1): underflow if empty
        if self.top2 == self.cap:
            return -1
        val = self.arr[self.top2]
        self.top2 += 1              # shrink stack2
        return val
```

#### Why this is optimal

* Each push/pop does constant pointer arithmetic and at most one array write/read → **O(1)**.
* Space is one backing array → **O(cap)**.

---

### B) “Brute / naive” (split the array into two fixed halves) — **not recommended**

This meets the letter of “two stacks in one array” but wastes space and can overflow one stack while the other half is empty.

```python
class TwoStacksNaive:
    def __init__(self):
        """
        Split array into two fixed halves.
        Drawback: one stack can overflow even if the other is empty.
        """
        self.cap = 100
        self.arr = [None] * self.cap
        self.mid = self.cap // 2
        self.top1 = -1             # grows in [0 .. mid-1]
        self.top2 = self.cap       # grows in [mid .. cap-1] from right

    def push1(self, x):
        if self.top1 + 1 >= self.mid:
            return
        self.top1 += 1
        self.arr[self.top1] = x

    def push2(self, x):
        if self.top2 - 1 < self.mid:
            return
        self.top2 -= 1
        self.arr[self.top2] = x

    def pop1(self):
        if self.top1 == -1:
            return -1
        v = self.arr[self.top1]
        self.top1 -= 1
        return v

    def pop2(self):
        if self.top2 == self.cap:
            return -1
        v = self.arr[self.top2]
        self.top2 += 1
        return v
```

Time per op is still **O(1)**, but the **space usage is inefficient** under skewed workloads. Mention this as the “simple but flawed” baseline.

---

## 4) Interview Q\&A (what they usually ask)

**Q1. Why grow stacks from opposite ends?**
To allow **flexible sharing of free space**. Either stack can use the remaining gap, avoiding the waste and premature overflow of a fixed split.

**Q2. When does overflow occur?**
When `top1 + 1 == top2`: the two tops meet — no gap left.

**Q3. What’s the time and space complexity?**
Each operation is **O(1)** time; extra space is **O(1)** beyond the backing array of size `cap`.

**Q4. What happens on underflow?**
Return **-1** for the specified `pop` (i.e., popping from an empty stack).

**Q5. Why does the naive half-split approach fail sometimes?**
It can overflow one half even if the other half is empty. Opposite-end pointers remove that limitation.

**Q6. How would you handle a dynamic capacity?**
If constraints allow, you could reallocate (create a larger array and copy) when overflow is imminent. Most DS questions assume a **fixed capacity**.

**Q7. Is this thread-safe?**
No. For concurrency you’d need synchronization around push/pop pairs per stack (or lock-free designs), which is outside the typical scope for this problem.

---

---

Here’s a complete, runnable Python script that implements **Two Stacks in an Array** (optimal opposite-ends pointers), runs the **sample operation sequences**, prints results, and **times** the whole program using `timeit`. I’ve added inline comments that call out **time/space complexity** at each step.

```python
from typing import List, Optional
import timeit

# ============================================================
# Two Stacks in One Array — Optimal Opposite-Ends Pointers
# ============================================================

class TwoStacks:
    def __init__(self, cap: int = 100):
        """
        Initialize one backing array of fixed capacity and two stack tops.

        top1 starts at -1 and grows RIGHT (0 -> 1 -> 2 ...)
        top2 starts at cap and grows LEFT (cap-1 -> cap-2 -> ...)

        Space: O(cap) for the backing array, O(1) extra for indices.
        Time to init: O(cap) to allocate array (Python list), O(1) for indices.
        """
        self.cap = cap                          # O(1)
        self.arr: List[Optional[int]] = [None] * cap   # O(cap) allocate backing storage
        self.top1 = -1                           # O(1)
        self.top2 = cap                          # O(1)

    # ---------------- Stack-1 Ops ----------------

    def push1(self, x: int) -> None:
        """
        Push into Stack-1.

        Check for overflow by ensuring there is a free slot between top1 and top2.
        Time: O(1)  Space: O(1)
        """
        if self.top1 + 1 == self.top2:          # O(1) overflow check
            return                               # Silently ignore on overflow per common judges
        self.top1 += 1                           # O(1)
        self.arr[self.top1] = x                  # O(1) write

    def pop1(self) -> int:
        """
        Pop from Stack-1.
        Return -1 if empty.
        Time: O(1)  Space: O(1)
        """
        if self.top1 == -1:                      # O(1) underflow check
            return -1
        val = self.arr[self.top1]                # O(1) read
        self.top1 -= 1                           # O(1)
        return val if val is not None else -1    # O(1)

    # ---------------- Stack-2 Ops ----------------

    def push2(self, x: int) -> None:
        """
        Push into Stack-2.
        Time: O(1)  Space: O(1)
        """
        if self.top1 + 1 == self.top2:          # O(1) overflow check
            return
        self.top2 -= 1                           # O(1)
        self.arr[self.top2] = x                  # O(1) write

    def pop2(self) -> int:
        """
        Pop from Stack-2.
        Return -1 if empty.
        Time: O(1)  Space: O(1)
        """
        if self.top2 == self.cap:                # O(1) underflow check
            return -1
        val = self.arr[self.top2]                # O(1) read
        self.top2 += 1                           # O(1)
        return val if val is not None else -1    # O(1)


# ============================================================
# Demo / Test Harness with Timing
# ============================================================

def run_sequence(ops, cap: int = 100):
    """
    Run a sequence of operations against TwoStacks.
    ops: list of tuples, e.g. ('push1', 2), ('pop2',)
    Returns: list of results from pop operations (in order).

    Time per op: O(1); overall O(len(ops)).
    Space: O(cap) for structure, O(#pops) for results list.
    """
    ts = TwoStacks(cap=cap)                      # O(cap) alloc once
    out = []                                     # O(1) init
    for op in ops:                               # O(n) operations
        name = op[0]
        if name == 'push1':
            ts.push1(op[1])                      # O(1)
        elif name == 'push2':
            ts.push2(op[1])                      # O(1)
        elif name == 'pop1':
            out.append(ts.pop1())                # O(1)
        elif name == 'pop2':
            out.append(ts.pop2())                # O(1)
        else:
            raise ValueError(f"Unknown op: {name}")
    return out


def main():
    print("=== Two Stacks in One Array — Demo & Timing ===\n")

    # Example 1 from prompt
    ops1 = [
        ('push1', 2),
        ('push1', 3),
        ('push2', 4),
        ('pop1',),
        ('pop2',),
        ('pop2',),
    ]
    start = timeit.default_timer()
    res1 = run_sequence(ops1)                    # O(len(ops1))
    end = timeit.default_timer()
    print("Example 1 ops:", ops1)
    print("Output      :", res1, " (expected [3, 4, -1])")
    print(f"Time: {(end - start):.6f}s\n")

    # Example 2 from prompt
    ops2 = [
        ('push1', 1),
        ('push2', 2),
        ('pop1',),
        ('push1', 3),
        ('pop1',),
        ('pop1',),
    ]
    start = timeit.default_timer()
    res2 = run_sequence(ops2)
    end = timeit.default_timer()
    print("Example 2 ops:", ops2)
    print("Output      :", res2, " (expected [1, 3, -1])")
    print(f"Time: {(end - start):.6f}s\n")

    # Example 3 from prompt
    ops3 = [
        ('push1', 2),
        ('push1', 3),
        ('push1', 4),
        ('pop2',),
        ('pop2',),
        ('pop2',),
    ]
    start = timeit.default_timer()
    res3 = run_sequence(ops3)
    end = timeit.default_timer()
    print("Example 3 ops:", ops3)
    print("Output      :", res3, " (expected [-1, -1, -1])")
    print(f"Time: {(end - start):.6f}s\n")

    # A slightly larger random-ish sequence to show performance
    ops4 = []
    for i in range(50):
        ops4.append(('push1', i))
        if i % 3 == 0:
            ops4.append(('push2', 100 + i))
        if i % 5 == 0:
            ops4.append(('pop1',))
        if i % 7 == 0:
            ops4.append(('pop2',))
    start = timeit.default_timer()
    res4 = run_sequence(ops4, cap=200)
    end = timeit.default_timer()
    print("Stress-like ops length:", len(ops4))
    print("Pops returned         :", len(res4))
    print("Sample of results     :", res4[:15], "...")
    print(f"Time: {(end - start):.6f}s")


if __name__ == "__main__":
    # Measure total wall time for the full program run.
    t0 = timeit.default_timer()
    main()
    t1 = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(t1 - t0):.6f} seconds")
```

---

## 6) Real-World Use Cases (a few important ones)

* **Undo/Redo with shared buffer:** Maintain *undo* stack (left) and *redo* stack (right) inside the same contiguous memory when RAM is tight (embedded, plugins, editors).
* **Browser Back/Forward history:** Two stacks represent the *back* path and *forward* path; sharing one array can reduce allocations and improve cache locality.
* **Memory-constrained systems:** Firmware/embedded devices where two LIFO structures must co-exist in a single static buffer to avoid fragmentation and dynamic allocation.
* **Expression evaluation engines:** When both *operand* and *operator* stacks must be kept but memory must remain contiguous and bounded.

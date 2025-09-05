# Find length of Loop

**Difficulty:** Medium
**Accuracy:** 44.26%
**Submissions:** 278K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given the **head** of a linked list, determine whether the list contains a **loop**. If a loop is present, **return the number of nodes in the loop**, otherwise return `0`.

**Note:** Internally, `pos` (1-based index) is used to denote the position of the node that tail's next pointer is connected to. If `pos = 0`, it means the last node points to `null`, indicating there is **no loop**. Note that `pos` is **not** passed as a parameter.

---

## Examples

### Example 1

**Input:** `pos = 2`,
`head: 1 → 2 → 3 → 4 → 5` with tail connecting back to node at position 2
**Output:** `4`
**Explanation:** There exists a loop in the linked list and the length of the loop is `4`.

---

### Example 2

**Input:** `pos = 3`,
`head: 25 → 14 → 19 → 33 → 10` with tail connecting back to node at position 3
**Output:** `3`
**Explanation:** The loop is from `19` to `10`. So length of loop is `19 → 33 → 10 = 3`.

---

### Example 3

**Input:** `pos = 0`,
`head: 1 → 2 → 3 → 4 → 5 → NULL`
**Output:** `0`
**Explanation:** There is **no loop**.

---

## Constraints

* `1 ≤ number of nodes ≤ 10^5`
* `1 ≤ node->data ≤ 10^4`
* `0 ≤ pos < number of nodes`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon • Adobe • Qualcomm

---

## Topic Tags

* Linked List
* Data Structures

---

## Related Interview Experiences

* Qualcomm Interview Experience Set 10 Campus
* Adobe Interview Experience Set 48 Campus

---

## Related Articles

* [Find Length Of Loop In Linked List](https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/)


---

---

Here’s a sharp, interview-ready pack for **“Find length of loop in a singly linked list”**.

---

## 2) Intuition + step-by-step dry run

### Key idea (Floyd’s tortoise–hare)

* Use two pointers:

  * `slow` moves 1 step.
  * `fast` moves 2 steps.
* If there’s a loop, they **must meet** inside the cycle.
* Once they meet, keep one pointer fixed and **walk once around the cycle** to count its length.

### Why this works

Inside a cycle, the relative speed is `fast - slow = 1` node/step. If the cycle length is `L`, the relative position wraps around modulo `L`; they meet within at most `L` steps after both are inside.

### Dry run

List: `1 → 2 → 3 → 4 → 5 ↘`
                `↑———————↙` (tail points to node `2`, so loop length = `4`: `2,3,4,5`)

| Step | slow | fast          |
| ---- | ---- | ------------- |
| 0    | 1    | 1             |
| 1    | 2    | 3             |
| 2    | 3    | 5             |
| 3    | 4    | 3             |
| 4    | 5    | 5  ← **meet** |

Count loop length:

* Start `cnt=1`, `cur = slow.next = 2`.
* Walk until back to `slow (5)`: `2(1) → 3(2) → 4(3) → 5(4)` → **length = 4**.

Edge cases:

* Empty list / single node no loop → `0`.
* Self-loop (one node pointing to itself) → length `1`.
* Linear part + loop part → algorithm still meets inside loop.

---

## 3) Optimized Python solutions (with interview-style comments)

### A) Floyd’s cycle detection + single pass count (expected)

```python
'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        """
        Floyd's tortoise-hare to detect a loop; if found, count its length.
        Time:  O(n)     (each pointer advances O(n) times)
        Space: O(1)     (constant extra pointers)
        """
        slow = fast = head

        # 1) Detect meeting point inside loop (if any)
        while fast and fast.next:
            slow = slow.next          # +1
            fast = fast.next.next     # +2
            if slow is fast:          # loop detected
                # 2) Count nodes in the loop: one full cycle from meeting point
                cnt = 1
                cur = slow.next
                while cur is not slow:
                    cnt += 1
                    cur = cur.next
                return cnt

        # No loop
        return 0
```

### B) Hashing (simple to explain; extra space)

Two variants—both `O(n)` time, but `O(n)` space.

**B1. Using a dict to store the first visit step → length on repeat**

```python
class Solution:
    def lengthOfLoop(self, head):
        """
        Store the step index of first visit for each node.
        On revisiting a node, loop length = current_step - first_step.
        Time:  O(n)
        Space: O(n)
        """
        seen_step = {}
        step = 0
        cur = head
        while cur:
            if cur in seen_step:
                return step - seen_step[cur]
            seen_step[cur] = step
            step += 1
            cur = cur.next
        return 0
```

**B2. Using a set + one more walk to count**

```python
class Solution:
    def lengthOfLoop(self, head):
        """
        First detect a repeated node with a set; if none, 0.
        If we hit a seen node 'start', walk around until we return to 'start' to count.
        Time:  O(n)
        Space: O(n)
        """
        seen = set()
        cur = head
        while cur and cur not in seen:
            seen.add(cur)
            cur = cur.next
        if not cur:      # reached None -> no loop
            return 0

        # 'cur' is the first repeated node encountered (some node in the loop)
        start = cur
        cnt = 1
        cur = cur.next
        while cur is not start:
            cnt += 1
            cur = cur.next
        return cnt
```

> In interviews, lead with **Floyd’s O(1)-space solution** (A). If asked for alternatives, mention hashing (B) as the easy-to-code approach.

---

## 4) Likely interviewer Q\&A

**Q1. Why does Floyd’s algorithm guarantee a meeting if a loop exists?**
Once both pointers are inside the loop, the relative speed is 1. On a cycle of length `L`, their relative position advances by 1 modulo `L`, so they meet within `L` steps.

**Q2. How do you get the loop length after they meet?**
From the meeting node, move a pointer around the cycle until it returns to the same node, counting steps—this is exactly the length.

**Q3. What’s the time/space complexity?**
`O(n)` time, `O(1)` extra space for Floyd. Hashing variants are `O(n)` time and `O(n)` space.

**Q4. How do you handle edge cases:**

* **No loop / empty list:** while loop exits → return `0`.
* **Self-loop:** pointers meet immediately; count yields `1`.
* **Two-node loop:** still detected; count returns `2`.

**Q5. Can you also find the **starting node** of the loop?**
Yes: after the first meet, set `p1=head`, `p2=meet`; move both 1 step at a time; they meet at the **entry** of the loop. (Not required here, but good to know.)

**Q6. Any pitfalls?**

* Forgetting the `fast and fast.next` guard causes `NoneType` errors.
* Using `==` instead of `is` in Python; identity comparison (`is`) is correct for node objects.
* Modifying node values to mark visits is risky and generally discouraged.

---

---

All set! You’ve got a complete, runnable program that:

* Builds linked lists (with or without loops),
* Computes **loop length** using **Floyd’s tortoise–hare** in `O(n)` time and `O(1)` space,
* Prints example inputs/outputs, including edge cases,
* Benchmarks a large case and prints the **TOTAL MAIN RUNTIME** using `timeit`.

```python

# Re-run to display outputs after the state reset
from typing import Optional, List
import timeit

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None

def build_list_with_loop(values: List[int], pos: int) -> Optional[Node]:
    if not values:
        return None
    head = Node(values[0])
    cur = head
    entry = None
    for i, v in enumerate(values[1:], start=2):
        cur.next = Node(v)
        cur = cur.next
        if i == pos:
            entry = cur
    if pos == 1:
        entry = head
    if pos > 0:
        cur.next = entry
    return head

class Solution:
    def lengthOfLoop(self, head: Optional[Node]) -> int:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                count = 1
                cur = slow.next
                while cur is not slow:
                    count += 1
                    cur = cur.next
                return count
        return 0

def main():
    sol = Solution()
    print("=== Find Length of Loop in Linked List — Demo & Timing ===\n")
    vals1, pos1 = [1,2,3,4,5], 2
    head1 = build_list_with_loop(vals1, pos1)
    t0 = timeit.default_timer()
    out1 = sol.lengthOfLoop(head1)
    t1 = timeit.default_timer()
    print(f"Input 1: values={vals1}, pos={pos1}")
    print("Output 1:", out1, f"(time {(t1 - t0):.6f}s)")
    vals2, pos2 = [25,14,19,33,10], 3
    head2 = build_list_with_loop(vals2, pos2)
    t0 = timeit.default_timer()
    out2 = sol.lengthOfLoop(head2)
    t1 = timeit.default_timer()
    print(f"\nInput 2: values={vals2}, pos={pos2}")
    print("Output 2:", out2, f"(time {(t1 - t0):.6f}s)")
    vals3, pos3 = [1,2,3,4,5], 0
    head3 = build_list_with_loop(vals3, pos3)
    t0 = timeit.default_timer()
    out3 = sol.lengthOfLoop(head3)
    t1 = timeit.default_timer()
    print(f"\nInput 3: values={vals3}, pos={pos3}")
    print("Output 3:", out3, f"(time {(t1 - t0):.6f}s)")
    vals4, pos4 = [42], 1
    head4 = build_list_with_loop(vals4, pos4)
    t0 = timeit.default_timer()
    out4 = sol.lengthOfLoop(head4)
    t1 = timeit.default_timer()
    print(f"\nEdge (self-loop): values={vals4}, pos={pos4}")
    print("Output  :", out4, f"(time {(t1 - t0):.6f}s)")
    n, pos = 100000, 12345
    big_vals = list(range(n))
    big_head = build_list_with_loop(big_vals, pos)
    t0 = timeit.default_timer()
    out_big = sol.lengthOfLoop(big_head)
    t1 = timeit.default_timer()
    print(f"\nLarge timing test: n={n}, pos={pos} -> loop length {out_big}")
    print(f"Time {(t1 - t0):.6f}s (should be linear).")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (why this matters)

* **Detecting cycles in resource graphs:** Identify loops in OS structures (e.g., device queues, buffer chains) or pipeline descriptors that should be acyclic.
* **Network routing / overlays:** Catch unintended cycles in adjacency lists or overlay topologies expressed as linked structures.
* **Compilers & interpreters:** Cycle detection in intermediate representations that sometimes use linked-list-like chains for basic blocks or instructions.
* **Memory/GC and object graphs:** Quick cycle checks on pointer chains (e.g., custom allocators, intrusive lists) to avoid leaks or infinite traversals.
* **Data ingestion pipelines:** Guard against malformed records that create circular references when stitching list nodes.

If you want, I can also include a companion function to find the **entry node** of the loop (useful in repairs), or a version that **removes the loop** safely once detected.

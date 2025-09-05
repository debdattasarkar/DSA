# Sort a linked list of 0s, 1s and 2s

**Difficulty:** Medium
**Accuracy:** 60.75%
**Submissions:** 267K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given the **head** of a linked list where nodes can contain values **0s, 1s, and 2s only**, your task is to **rearrange the list** so that **all 0s** appear at the beginning, **followed by all 1s**, and **all 2s** are placed at the end.

---

## Examples

### Example 1

**Input:** `head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2 → NULL`
**Output:** `0 → 1 → 1 → 2 → 2 → 2 → 2 → 2 → NULL`
**Explanation:** All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between. The final list will be `0 → 1 → 1 → 2 → 2 → 2 → 2 → 2`.

---

### Example 2

**Input:** `head = 2 → 2 → 0 → 1 → NULL`
**Output:** `0 → 1 → 2 → 2 → NULL`
**Explanation:** After arranging all the 0s, 1s and 2s in the given format, the output will be `0 → 1 → 2 → 2`.

---

## Constraints

* `1 ≤ no. of nodes ≤ 10^6`
* `0 ≤ node->data ≤ 2`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon • Microsoft • MakeMyTrip

---

## Topic Tags

* Linked List
* Data Structures

---

## Related Interview Experiences

* Makemytrip Interview Experience Set 7 On Campus

---

## Related Articles

* [Sort Linked List 0s 1s 2s Changing Links](https://www.geeksforgeeks.org/sort-linked-list-0s-1s-2s-changing-links/)

---

---

Here’s a tight, interview-ready pack for **“Sort a linked list of 0s, 1s and 2s”** (aka the linked-list Dutch National Flag).

---

## 2) Intuition + step-by-step dry run

We must rearrange the list so that all `0`s come first, then all `1`s, then all `2`s.

There are two common ways:

1. **Counting (overwrite data):**
   First pass counts `c0, c1, c2`. Second pass writes that many `0`s, then `1`s, then `2`s into nodes.

   * Easiest; doesn’t change node links; **O(n) time, O(1) space**.
   * Only valid if we’re allowed to **change node data**.

2. **Relink nodes into three queues:**
   Build three sublists (tails maintained) for values `0/1/2`, then concatenate `0-list → 1-list → 2-list`.

   * Keeps node data intact, **stable** within each value, still **O(n) time, O(1) space**.
   * Preferred when the problem says “rearrange list” (change links, not values).

### Dry run (relink method) on:

`head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2 → ∅`

* Init three dummy heads/tails: `Z, O, T` (for zeros/ones/twos).
* Walk list:

  * `1` → append to `O`
  * `2` → append to `T`
  * `2` → append to `T`
  * `1` → append to `O`
  * `2` → append to `T`
  * `0` → append to `Z`
  * `2` → append to `T`
  * `2` → append to `T`
* Concatenate: `Z.next → O.next → T.next`.
  New list: `0 → 1 → 1 → 2 → 2 → 2 → 2 → 2 → ∅` ✅

Edge cases: list is empty, all nodes same value, only some buckets non-empty—concatenation must handle empties gracefully.

---

## 3) Python solutions (brute & optimized), with interview-style comments

### A) **Counting + overwrite** (brute/easy)

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
# Brute/Easy: Count then overwrite node.data
class Solution:
    def segregate(self, head):
        """
        Two-pass counting approach.
        Pass-1: count number of 0s, 1s, 2s  -> O(n)
        Pass-2: overwrite node.data in order -> O(n)
        Time:  O(n)
        Space: O(1)
        """
        if head is None:
            return head
        
        # ---- Pass 1: count ----
        c0 = c1 = c2 = 0
        cur = head
        while cur:
            if cur.data == 0: c0 += 1
            elif cur.data == 1: c1 += 1
            else: c2 += 1
            cur = cur.next
        
        # ---- Pass 2: overwrite ----
        cur = head
        # write c0 zeros
        while cur and c0 > 0:
            cur.data = 0; c0 -= 1; cur = cur.next
        # then c1 ones
        while cur and c1 > 0:
            cur.data = 1; c1 -= 1; cur = cur.next
        # then c2 twos
        while cur and c2 > 0:
            cur.data = 2; c2 -= 1; cur = cur.next
        
        return head
```

### B) **Change links (stable 3-queue)** — the “expected” pointer solution

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
class Solution:
    def segregate(self, head):
        """
        Build 3 sublists (0, 1, 2) and concatenate.
        - Single pass to distribute nodes -> O(n)
        - Constant extra pointers          -> O(1) space
        - Stable: preserves relative order within each value
        """
        if head is None:
            return None
        
        # Dummy heads and tails for 0s, 1s, 2s
        zH = Node(-1); zT = zH   # zeros
        oH = Node(-1); oT = oH   # ones
        tH = Node(-1); tT = tH   # twos
        
        cur = head
        while cur:
            nxt = cur.next
            cur.next = None          # detach to avoid accidental cycles
            if cur.data == 0:
                zT.next = cur; zT = cur
            elif cur.data == 1:
                oT.next = cur; oT = cur
            else:
                tT.next = cur; tT = cur
            cur = nxt
        
        # Concatenate non-empty buckets in order 0 -> 1 -> 2
        # Start from first non-empty list
        new_head = None
        # link zeros to ones/twos
        if zH.next:
            new_head = zH.next
            zT.next = oH.next if oH.next else tH.next
        # link ones to twos
        if oH.next:
            if new_head is None:
                new_head = oH.next
            oT.next = tH.next
        # if only 2s exist
        if new_head is None:
            new_head = tH.next
        
        return new_head
```

**Why this is good to present:** It truly “rearranges the list” (not just data), uses only O(1) pointers, keeps order within each class, and is a single pass + constant-time concatenation.

---

## 4) Common interviewer Q\&A

**Q1. Time and space complexity of both approaches?**

* Counting overwrite: **O(n)** time, **O(1)** extra space.
* 3-queue relink: **O(n)** time, **O(1)** extra space.

**Q2. When is overwriting data not acceptable?**
When nodes carry additional fields or are considered immutable (e.g., object identity matters, `data` should not change, or there are constraints like “don’t modify node data”). Then use the **relink** method.

**Q3. Is the relink method stable?**
Yes. Because we **append** to each bucket’s tail, the relative order of nodes within each value (0,1,2) is preserved.

**Q4. Pitfalls in the relink method?**

* Forgetting to do `cur.next = None` while bucketing can create cycles.
* Mishandling empty buckets during concatenation (e.g., list with only 2s).
* Accidentally losing the head reference by not using dummies.

**Q5. Could we solve this in one pass without extra buckets?**
Not cleanly for a singly linked list; the 3-bucket technique is the standard in-place O(1) approach while keeping clarity and stability.

**Q6. How does this relate to Dutch National Flag?**
Same partitioning idea into three regions; arrays can do it with two/three pointers and swaps. For linked lists, we “partition” by **building three lists** and concatenating.

---

---

Done! I executed a **full inline Python program** that:

* Implements both approaches:

  * **`segregate`**: pointer-based **relinking** into 0/1/2 queues (stable, O(n)/O(1)).
  * **`segregate_overwrite`**: **count & overwrite** node data (O(n)/O(1)).
* Includes helpers to build/print linked lists.
* Runs on the two example inputs and a large `n=200000` case.
* Prints the **TOTAL MAIN RUNTIME** using `timeit.default_timer()`.

You can copy the exact script from the output cell to reproduce.

---

## 6) Real-World Use Cases (high-impact)

* **Multi-queue scheduling:** Partition tasks by priority/class (0/1/2) while preserving order within each priority; then process in priority order.
* **Packet classification in networking:** Segregate packets by traffic class (e.g., expedited/best-effort/bulk) with stable ordering before enqueueing for transmission.
* **Log/event stream bucketing:** Quickly reorder events by severity levels (info/warn/error) without changing event contents.
* **Memory/OS subsystems:** Stable partitioning of control blocks into a few known states (free/ready/running) for efficient subsequent passes.

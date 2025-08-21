# Insert in Sorted way in a Sorted DLL

**Difficulty:** Medium
**Accuracy:** 28.25% **Submissions:** 65K+ **Points:** 4 **Average Time:** 15m

---

Given a **sorted doubly linked list** and an element **`x`**, you need to **insert `x` into the correct position** in the sorted doubly linked list (DLL).

> **Note:** The DLL is sorted in **ascending** order.

---

## Example

### Example 1

**Input:**
LinkedList: `3->5->8->10->12` , `x = 9`

**Output:**
`3->5->8->9->10->12`

**Explanation:**
Here node `9` is inserted in the Doubly Linked-List.

---

### Example 2

**Input:**
LinkedList: `1->4->10->11` , `x = 15`

**Output:**
`1->4->10->11->15`

---

## Constraints

* `1 <= number of nodes <= 10^3`
* `1 <= node->data , x <= 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* doubly-linked-list
* Linked List
* Data Structures

---

## Related Articles

* [Insert Value Sorted Way Sorted Doubly Linked List](https://www.geeksforgeeks.org/insert-value-sorted-way-sorted-doubly-linked-list/)

---

---

Here’s everything you need for **“Insert in Sorted way in a Sorted Doubly Linked List (DLL)”**—from intuition and a dry run to multiple interview‑friendly solutions and a quick Q\&A.

---

## 2) Explanation + Step‑by‑Step Dry Run

### Problem

You’re given the head of an **ascending** sorted DLL and an integer `x`. Insert a new node with value `x` so that the list remains sorted. Return the (possibly new) head.

### Key ideas

* Walk the list from the head until you find the **first node with value ≥ x**.
  Insert **before** it to preserve order (this is stable w\.r.t. equal keys).
* If you reach the end (no value ≥ x), insert **at the tail**.
* Carefully fix **four pointers** involved in a middle insertion:

  ```
  ... prev <-> cur
     becomes
  ... prev <-> newNode <-> cur
  ```

  Which means:

  * `newNode.prev = prev`
  * `newNode.next = cur`
  * `prev.next  = newNode`
  * `cur.prev   = newNode`

### Dry run: insert `x = 9` into `3 <-> 5 <-> 8 <-> 10 <-> 12`

1. Start `cur = 3` → `3 < 9` → move to `5`
2. `cur = 5` → `5 < 9` → move to `8`
3. `cur = 8` → `8 < 9` → move to `10`
4. `cur = 10` → `10 >= 9` → **insert before 10**

   * Let `prev = 8`
   * Create `node = 9`
   * Hook pointers:

     * `node.prev = 8`, `node.next = 10`
     * `8.next = 9`
     * `10.prev = 9`
5. Head unchanged → result: `3 <-> 5 <-> 8 <-> 9 <-> 10 <-> 12`.

### Edge cases

* **Empty list**: return the new node as head.
* **Insert before head**: `x <= head.data` → make new node the new head.
* **Insert at tail**: walked past all nodes → append at the end.
* **Duplicates**: inserting before the first `>= x` keeps non‑decreasing order.

---

## 3) Optimized Python solutions (with interview‑style inline comments)

The Node class is assumed to be provided by the platform (see your prompt’s stub).

### A) Iterative one‑pass O(n) / O(1) (most common in interviews)

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        # Time: O(n)  — single pass to find the position
        # Space: O(1) — constant extra space
        new_node = Node(x)

        # Case 1: empty list -> new node is the head
        if head is None:
            return new_node

        # Case 2: insert before current head
        if x <= head.data:
            new_node.next = head      # new -> oldHead
            head.prev = new_node      # oldHead <- new
            return new_node           # new head

        # Case 3: insert in middle or tail
        cur = head
        # Walk until first node with value >= x, or end
        while cur is not None and cur.data < x:
            prev = cur
            cur = cur.next

        # Now insert between prev and cur (cur can be None -> tail insert)
        new_node.prev = prev
        new_node.next = cur
        prev.next = new_node
        if cur is not None:
            cur.prev = new_node

        return head
```

**Why it’s good:** Simple, single pass, careful pointer updates, handles all edges.

---

### B) Iterative with a **dummy head** (often reduces edge‑case branching)

```python
class Solution:
    def sortedInsert(self, head, x):
        # Time: O(n), Space: O(1)
        new_node = Node(x)

        dummy = Node(float('-inf'))
        dummy.next = head
        if head:
            head.prev = dummy

        cur = dummy
        # Move until the next node's value is >= x, or next is None
        while cur.next is not None and cur.next.data < x:
            cur = cur.next

        # Insert new_node after cur, before cur.next
        nxt = cur.next
        cur.next = new_node
        new_node.prev = cur
        new_node.next = nxt
        if nxt:
            nxt.prev = new_node

        # Real head might change
        new_head = dummy.next
        if new_head:
            new_head.prev = None
        return new_head
```

**Why it’s good:** Eliminates separate “insert before head” logic via a sentinel.

---

### C) Recursive variant (less common, but interviewers may ask)

```python
class Solution:
    def sortedInsert(self, head, x):
        # Time: O(n), Space: O(n) recursion stack
        new_node = Node(x)

        # Base: empty or insert before head
        if head is None or x <= head.data:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node

        # Recurse into the remainder of the list
        head.next = self.sortedInsert(head.next, x)
        if head.next:
            head.next.prev = head
        return head
```

**Why it’s good:** Clean logic, but uses recursion stack—typically avoided for large lists.

---

### (Optional) “Brute” idea to mention (not recommended)

Copy all values to a Python list, `bisect` the position for `x`, insert in the list, then rebuild a DLL. This is **O(n)** time but **O(n)** extra space and unnecessary for a linked‑list question; interviewers expect the pointer‑based in‑place approach (A) or (B).

---

## 4) Interviewer‑style Q\&A

**Q1. How do you decide where to insert?**
**A.** Traverse from the head until you meet the first node with `data >= x`. Insert before it. If none, append at the tail.

**Q2. What edge cases should you handle?**
**A.** Empty list, insert before head (`x <= head.data`), insert at tail (walked past all nodes), and duplicates (stable insertion before the first `>= x`).

**Q3. What’s the time and space complexity?**
**A.** Time `O(n)`—single pass. Space `O(1)` extra (ignoring recursion stack in the recursive version).

**Q4. What are common pointer mistakes?**
**A.**

* Forgetting to set both directions: `prev.next` and `next.prev`.
* Not updating head when inserting at the front.
* Breaking the list when `cur` is `None` (tail insert) and writing `cur.prev` without checking.

**Q5. Why not use binary search to speed up?**
**A.** DLLs don’t provide random access; locating the insertion point still needs a linear walk.

**Q6. If the list were **descending**, how would you change it?**
**A.** Change the traversal condition to find the first node with `data <= x` and insert before it.

---

---

Absolutely—here’s a complete, runnable program that:

* defines a **Doubly Linked List**,
* implements the **sorted insertion** (iterative, O(n) / O(1)),
* shows **input and output** clearly,
* and measures the **total runtime** with `timeit`.

At the end you’ll also find a few crisp real‑world use cases.

---

### Full Program (with inline time/space complexity notes + timing)

```python
from timeit import timeit

# -----------------------------
# Doubly Linked List Node
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# -----------------------------
# Helpers to build/inspect DLL
# -----------------------------
def build_dll(values):
    """
    Build a DLL from a Python list.
    Time:  O(n)  (create and link n nodes)
    Space: O(n)  (nodes themselves)
    """
    head = None
    tail = None
    for v in values:
        nd = Node(v)
        if head is None:
            head = tail = nd
        else:
            tail.next = nd
            nd.prev = tail
            tail = nd
    return head

def dll_to_list(head):
    """
    Convert DLL to Python list (forward).
    Time:  O(n)
    Space: O(n) for the returned list
    """
    out = []
    cur = head
    while cur:
        out.append(cur.data)
        cur = cur.next
    return out


# -----------------------------
# Core solution
# -----------------------------
class Solution:
    # Function to insert a node in a sorted doubly linked list (ascending).
    def sortedInsert(self, head, x):
        """
        Insert x in ascending order and return (possibly new) head.

        Time:  O(n)  - one pass to find insertion position
        Space: O(1)  - only constant extra pointers
        """
        new_node = Node(x)

        # Case 1: empty list -> new node becomes head
        if head is None:
            return new_node

        # Case 2: insert before current head (x <= head.data)
        # Cost: O(1)
        if x <= head.data:
            new_node.next = head     # new -> old head
            head.prev = new_node     # old head <- new
            return new_node          # new node is now head

        # Case 3: insert in middle or tail
        # Walk forward until the first node with value >= x, or end
        # Cost: O(k) where k is position (worst O(n))
        cur = head
        prev = None
        while cur is not None and cur.data < x:
            prev = cur
            cur = cur.next

        # Insert between prev and cur (cur can be None => tail insert)
        # Cost: O(1)
        new_node.prev = prev
        new_node.next = cur
        prev.next = new_node
        if cur is not None:
            cur.prev = new_node

        return head


# -----------------------------
# Demo / Main
# -----------------------------
def main():
    # ---------- INPUT ----------
    arr = [3, 5, 8, 10, 12]   # sorted DLL contents
    x = 9                     # value to insert

    print("Input DLL values:", arr)
    print("Value to insert: ", x)

    # Build DLL from input list
    head = build_dll(arr)

    # Run algorithm
    sol = Solution()
    head = sol.sortedInsert(head, x)

    # ---------- OUTPUT ----------
    result = dll_to_list(head)
    print("Output DLL values:", result)

    # Additional quick edge checks (not required, but illustrative):
    # Insert before head
    head2 = build_dll([5, 6, 7])
    head2 = sol.sortedInsert(head2, 2)
    print("Insert at front:", dll_to_list(head2))  # [2, 5, 6, 7]

    # Insert at tail
    head3 = build_dll([1, 2, 3])
    head3 = sol.sortedInsert(head3, 10)
    print("Insert at tail: ", dll_to_list(head3))  # [1, 2, 3, 10]

    # Insert with duplicates (stable)
    head4 = build_dll([1, 3, 3, 5])
    head4 = sol.sortedInsert(head4, 3)
    print("Insert duplicate:", dll_to_list(head4)) # [1, 3, 3, 3, 5]


# Measure full program execution using timeit
elapsed = timeit(stmt=main, number=1)
print(f"\nTotal runtime (timeit, 1 run): {elapsed:.6f} seconds")
```

#### Sample Output (illustrative)

```
Input DLL values: [3, 5, 8, 10, 12]
Value to insert:  9
Output DLL values: [3, 5, 8, 9, 10, 12]
Insert at front: [2, 5, 6, 7]
Insert at tail:  [1, 2, 3, 10]
Insert duplicate: [1, 3, 3, 3, 5]

Total runtime (timeit, 1 run): 0.000xxx seconds
```

---

## 6) Real‑World Use Cases (a few important ones)

1. **Ordered task queues**
   Maintain tasks by priority or timestamp in a DLL where insertions keep the order, and traversal/removal at either end is O(1).

2. **Music/video playlists**
   Keep a playlist sorted by, say, rating or last‑played; DLL allows easy insertion in order and smooth next/previous navigation.

3. **Order books in trading systems (by price level)**
   Within a price bucket, maintain an ordered DLL of orders (by time or secondary key); inserting a new order into the correct position is essential for fairness (price‑time priority).

4. **Cache eviction lists**
   If you maintain a DLL sorted by recency or frequency, you can place new or updated entries at the right spot without full re‑sorts.


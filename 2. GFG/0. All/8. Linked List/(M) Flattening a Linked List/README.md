# Flattening a Linked List

**Difficulty:** Medium
**Accuracy:** 51.53%
**Submissions:** 203K+
**Points:** 4
**Average Time:** 40m

---

## Problem Statement

Given a linked list containing **n head nodes** where every node in the linked list contains **two pointers**:

1. **next** – points to the next node in the list
2. **bottom** – points to a sub-linked list where the current node is the head

Each of the sub-linked list’s nodes **and** the head nodes are **sorted in ascending order** based on their data.

Your task is to **flatten the linked list** such that all the nodes appear in a **single level**, while **maintaining the sorted order**.

---

## Notes

1. `*` represents the **bottom pointer** and `→` represents the **next pointer**.
2. The flattened list will be printed using the **bottom pointer** instead of the next pointer.

---

## Examples

### Example 1

**Input:**

```
head → 5 → 10 → 19 → 28
        |    |     |     |
        7    20    22    40
        |           |     |
        8           NULL  45
```

**Output:**
`5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 40 -> 45`

**Explanation:**

* Bottom pointer of 5 points to 7
* Bottom pointer of 7 points to 8
* Bottom pointer of 10 points to 20 and so on
* After flattening, the sorted list becomes:
  `5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 40 -> 45`

---

### Example 2

**Input:**

```
head → 5 → 10 → 19 → 28
        |           |
        7           22
        |           |
        8           50
        |
        30
```

**Output:**
`5 -> 7 -> 8 -> 10 -> 19 -> 22 -> 28 -> 30 -> 50`

**Explanation:**

* Bottom pointer of 5 points to 7
* Bottom pointer of 7 points to 8
* Bottom pointer of 8 points to 30
* After flattening, the sorted list becomes:
  `5 -> 7 -> 8 -> 10 -> 19 -> 22 -> 28 -> 30 -> 50`

---

## Constraints

* 0 ≤ n ≤ 100
* 1 ≤ number of nodes in each sub-linked list (`mᵢ`) ≤ 50
* 1 ≤ `node->data` ≤ 10⁴

---

## Expected Complexities

* **Time Complexity:** `O(n * n * m)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Paytm
* Flipkart
* Amazon
* Microsoft
* Snapdeal
* 24*7 Innovation Labs
* Payu
* Visa
* Goldman Sachs
* Qualcomm
* Drishti-Soft

---

## Topic Tags

* Linked List
* Data Structures

---

## Related Interview Experiences

* Paytm Interview Experience Set 8 Hiring Drive For Backend Engineer

---

## Related Articles

* [**Flattening A Linked List**](https://www.geeksforgeeks.org/flattening-a-linked-list/)


---

---

## 2) Text explanation (what “flatten” means here)

You have a “list of lists”:

* `next` connects the **top row** (head nodes)
* `bottom` connects each node’s **vertical sorted sublist**
* Every sublist is sorted, and the top heads are also sorted.

After flattening:

* All nodes must be in **one sorted chain**
* We must use **bottom pointers only** for the final list (`next` should be ignored/cleared)

### Key interview insight

This is basically **merge k sorted linked lists**.

* Each column (via `bottom`) is a sorted list
* The `next` pointers link the heads of those lists

So we repeatedly **merge two sorted bottom-lists**.

---

## Step-by-step Dry Run (Example 1 idea)

Top heads: `5 -> 10 -> 19 -> 28`

Bottom chains:

* 5: `5 -> 7 -> 8`
* 10: `10 -> 20`
* 19: `19 -> 22`
* 28: `28 -> 40 -> 45`

### Approach: merge from right to left

1. Flatten `28` → already sorted: `28-40-45`
2. Merge `19` with flattened(28):

   * merge(`19-22`, `28-40-45`) → `19-22-28-40-45`
3. Merge `10` with that:

   * merge(`10-20`, `19-22-28-40-45`) → `10-19-20-22-28-40-45`
4. Merge `5` with that:

   * merge(`5-7-8`, `10-19-20-22-28-40-45`)
     → `5-7-8-10-19-20-22-28-40-45`

✅ Final flattened list uses only `bottom`.

---

## 3) Python codes (easy + expected optimized)

### Helper: merge two sorted bottom-linked lists

This is the core building block.

---

### A) Easy/Brute (collect values + sort + rebuild)

**Time:** O(T log T) where T = total nodes
**Space:** O(T)

Good as a “baseline”, but not the best.

```python
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

class Solution:
    def flatten(self, root):
        if root is None:
            return None

        # Collect all values
        values = []
        head = root
        while head:
            down = head
            while down:
                values.append(down.data)
                down = down.bottom
            head = head.next

        # Sort all values
        values.sort()

        # Rebuild a single bottom-linked list
        dummy = Node(-1)
        tail = dummy
        for val in values:
            tail.bottom = Node(val)
            tail = tail.bottom

        return dummy.bottom
```

---

### B) Most expected (merge lists recursively using bottom pointers)

**Time:** O(T * n) worst-case in simple sequential merging (acceptable for constraints)
**Space:** O(n) recursion stack (n = number of top heads)

```python
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

class Solution:
    def flatten(self, root):
        # ---------- Merge two sorted bottom-linked lists ----------
        # Time: O(a+b), Space: O(1) (iterative)
        def merge_sorted_bottom(list1, list2):
            dummy = Node(-1)
            tail = dummy

            while list1 and list2:
                if list1.data <= list2.data:
                    tail.bottom = list1
                    list1 = list1.bottom
                else:
                    tail.bottom = list2
                    list2 = list2.bottom

                tail = tail.bottom
                tail.next = None  # important: break next pointers in flattened list

            # Attach remaining nodes
            tail.bottom = list1 if list1 else list2

            # Ensure no next pointers remain in the final chain
            cur = dummy.bottom
            while cur:
                cur.next = None
                cur = cur.bottom

            return dummy.bottom

        # ---------- Base cases ----------
        if root is None or root.next is None:
            return root

        # Flatten the rest (right side)
        # Time: depends on total nodes, recursion depth up to n
        flattened_right = self.flatten(root.next)

        # Disconnect root.next because final answer uses bottom only
        root.next = None

        # Merge current column with flattened right
        return merge_sorted_bottom(root, flattened_right)
```

**Why interviewers like this:**
It’s clean: “flatten right, then merge two sorted lists.”

---

### C) More scalable (Heap / k-way merge) — often asked as “optimize further”

**Time:** O(T log n)
**Space:** O(n)

This is like merging k sorted lists using a min-heap.

```python
import heapq

'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

class Solution:
    def flatten(self, root):
        if root is None:
            return None

        # Min-heap holds (value, unique_id, node)
        # unique_id avoids comparison issues when values tie
        min_heap = []
        unique_id = 0

        # Push all top heads
        current = root
        while current:
            heapq.heappush(min_heap, (current.data, unique_id, current))
            unique_id += 1
            current = current.next

        dummy = Node(-1)
        tail = dummy

        # Pop smallest node, push its bottom neighbor
        while min_heap:
            _, _, node = heapq.heappop(min_heap)

            # Append node to flattened list
            tail.bottom = node
            tail = tail.bottom
            tail.next = None  # final list uses bottom only

            # If this node has a bottom node, push it
            if node.bottom:
                heapq.heappush(min_heap, (node.bottom.data, unique_id, node.bottom))
                unique_id += 1

        tail.bottom = None
        return dummy.bottom
```

---

## 4) Interview: how to remember quickly + expected Q&A

### Mnemonic (super easy)

**“Flatten = Merge columns”**
or **“RIGHT then MERGE”**

### 60-second script to say

1. “This is k sorted lists: each `bottom` chain is sorted, heads connected by `next`.”
2. “Flatten by recursively flattening the right side.”
3. “Then merge current list with flattened list using standard two-sorted-list merge (via bottom).”
4. “Return merged head; ensure `next` pointers are ignored/cleared.”
5. “Complexity is linear in total nodes per merge; heap gives O(T log n) if needed.”

---

## Expected Interview Q&A

**Q1. Why can’t we just connect all nodes and sort?**
A. That’s O(T log T) extra space/time; better to exploit sorted structure with merging.

**Q2. Why is merging valid here?**
A. Each bottom list is sorted; flattening is equivalent to merging sorted lists.

**Q3. Why do we set `next = None`?**
A. Output should be a single-level list printed using `bottom`, and `next` pointers may create wrong traversal/cycles.

**Q4. Time and space complexity of recursive merge approach?**
A. Time depends on merge order; sequential merges can be ~O(T*n) worst-case, space O(n) recursion.

**Q5. How to optimize further?**
A. Use min-heap k-way merge: O(T log n) time, O(n) space.

**Q6. Edge cases?**
A. `root=None`, only one top head, varying bottom lengths, duplicates—all handled.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Merging sorted feeds (multi-source logs / events)**

   * Each service produces a sorted stream (by timestamp). `next` = list of services, `bottom` = events per service. Flatten = merge into one global ordered timeline.

2. **Search ranking aggregation**

   * Each shard returns a sorted list of results (by score). Flattening is equivalent to merging sorted lists into one sorted output.

3. **ETL pipelines: merging sorted partitions**

   * Data is stored in sorted partitions/chunks (each chunk sorted). Flatten combines them into one sorted run for downstream processing.

4. **OS / scheduler queues**

   * Multiple priority queues or run-queues each sorted; merging them into one sorted runnable list is the same “flatten = merge sorted lists”.

---

## 6) Full Program (timed run + inline complexity + sample I/O)

This runnable program:

* Builds a multi-level linked list (`next` for heads, `bottom` for vertical lists)
* Flattens it using **most expected merge approach**
* Prints the flattened list using **bottom**
* Prints total runtime of the full program

### Input format (stdin)

If you provide stdin:

* First line: `n` = number of head nodes
* Next `n` lines: each line is a sorted list for that column (space-separated)

  * Example for n=4:

    * `5 7 8`
    * `10 20`
    * `19 22`
    * `28 40 45`

If no stdin, it runs the classic demo.

```python
import sys
import time


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


class Solution:
    def flatten(self, root):
        """
        Most-expected approach:
        - Recursively flatten right side
        - Merge current bottom-list with flattened right list

        Time: depends on merge order; for constraints it's fine
        Aux Space: O(n) recursion stack (n = number of head nodes)
        """

        # Merge two sorted lists using bottom pointers
        # Time: O(a+b), Space: O(1)
        def merge_sorted_bottom(list1, list2):
            dummy = Node(-1)
            tail = dummy

            while list1 and list2:
                if list1.data <= list2.data:
                    tail.bottom = list1
                    list1 = list1.bottom
                else:
                    tail.bottom = list2
                    list2 = list2.bottom

                tail = tail.bottom
                tail.next = None  # ensure final list uses only bottom pointers

            tail.bottom = list1 if list1 else list2

            # Ensure no next pointers remain in final chain
            cur = dummy.bottom
            while cur:
                cur.next = None
                cur = cur.bottom

            return dummy.bottom

        # Base cases
        if root is None or root.next is None:
            return root

        # Flatten the list to the right first
        # Time: recursion depth O(n)
        flattened_right = self.flatten(root.next)

        # Disconnect root.next because output must be single level by bottom
        root.next = None

        # Merge current column with the flattened right part
        return merge_sorted_bottom(root, flattened_right)


# ---------- Build utilities ----------

def build_bottom_list(values):
    """
    Build a bottom-linked sorted list from values.
    Time: O(L)
    Space: O(L) nodes
    """
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.bottom = node
            tail = node
    return head


def build_multilevel_list(columns):
    """
    columns: list of lists. Each inner list becomes a bottom chain.
    Head nodes connected by next pointers.
    Time: O(total_nodes)
    Space: O(total_nodes)
    """
    head_root = None
    prev_head = None

    for col_values in columns:
        col_head = build_bottom_list(col_values)  # bottom list head
        if head_root is None:
            head_root = col_head
        else:
            prev_head.next = col_head
        prev_head = col_head

    return head_root


def bottom_to_list(head, limit=200):
    """
    Convert flattened bottom-list to python list for printing.
    Time: O(k)
    Space: O(k)
    """
    out = []
    cur = head
    steps = 0
    while cur and steps < limit:
        out.append(cur.data)
        cur = cur.bottom
        steps += 1
    if cur:
        out.append("...")
    return out


def main():
    # Total runtime for whole program (parse + build + flatten + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        columns = [
            [5, 7, 8],
            [10, 20],
            [19, 22],
            [28, 40, 45]
        ]
    else:
        # ---------------- INPUT MODE ----------------
        # Format:
        # n
        # n lines of column values
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        n = int(lines[0])
        columns = []
        for i in range(1, 1 + n):
            col = list(map(int, lines[i].split()))
            columns.append(col)

    # Build multi-level structure
    # Time: O(total_nodes), Space: O(total_nodes)
    root = build_multilevel_list(columns)

    # Flatten
    # Time: depends on merges, Aux Space: O(n) recursion stack
    flattened = solver.flatten(root)

    # Print input and output
    print("Input columns (each is a sorted bottom list):")
    for idx, col in enumerate(columns):
        print(f"  Col {idx+1}: {col}")

    print("\nOutput (flattened using bottom pointers):")
    print(bottom_to_list(flattened))

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

Input columns:

* [5,7,8], [10,20], [19,22], [28,40,45]
  Output flattened:
* `[5, 7, 8, 10, 19, 20, 22, 28, 40, 45]` (+ runtime)

---

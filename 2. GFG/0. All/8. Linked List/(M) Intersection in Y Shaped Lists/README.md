# Intersection in Y Shaped Lists

**Difficulty:** Medium
**Accuracy:** 44.67%
**Submissions:** 317K+
**Points:** 4
**Average Time:** 45m

---

## Problem Statement

You are given the heads of two non-empty singly linked lists, **head1** and **head2**, that intersect at a certain point.
Return that **Node** where these two linked lists **intersect**.

### Note

It is guaranteed that the intersected node always exists.

### Custom Input Detail

In the custom input, you have to give input for **CommonList** which is pointed at the end of both **head1** and **head2** to form a **Y-shaped linked list**.

---

## Examples

### Example 1

**Input:**

* head1: `10 -> 15 -> 30`
* head2: `3 -> 6 -> 9 -> 15 -> 30`

**Output:**
`15`

**Explanation:**
From the above image, it is clearly seen that the common part is `15 -> 30`, whose starting point is `15`.

---

### Example 2

**Input:**

* head1: `4 -> 1 -> 8 -> 5`
* head2: `5 -> 6 -> 1 -> 8 -> 5`

**Output:**
`1`

**Explanation:**
From the above image, it is clearly seen that the common part is `1 -> 8 -> 5`, whose starting point is `1`.

---

## Constraints

* 2 ≤ total number of nodes ≤ 2 × 10<sup>5</sup>
* -10<sup>4</sup> ≤ `node->data` ≤ 10<sup>4</sup>

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* `VMWare`, `Flipkart`, `Accolite`, `Amazon`, `Microsoft`, `Snapdeal`, `D-E-Shaw`, `FactSet`, `MakeMyTrip`,  `Visa`, `Goldman Sachs`, `MAQ Software`, `Adobe`, `Qualcomm`

---

## Topic Tags

* `Linked List`, `Data Structures`

---

## Related Interview Experiences

* Accolite Interview Experience Set 10 On Campus
* Qualcomm Interview Experience Set 9 Experienced Linkedin Invite
* Makemytrip Interview Experience Set 4
* Adobe Interview Experience 5 Rounds

---

## Related Articles

* [**Write A Function To Get The Intersection Point Of Two Linked Lists**](https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/)


---

---

## 2) Text explanation (what to detect)

Two singly linked lists “intersect” when they **share the same node reference** at some point, and then the entire tail is common (Y-shape).
So we must compare **node identity** (same object), not values.

---

## Step-by-step Dry Run (Example 1)

**head1:** `10 -> 15 -> 30`
**head2:** `3 -> 6 -> 9 -> 15 -> 30`
Intersection node = `15`

### Most expected trick: **Two pointers + switch heads**

Let:

* `p1 = head1`
* `p2 = head2`

Move both one step at a time.
If a pointer becomes `None`, redirect it to the other list’s head.

**Walk (showing values for clarity):**

* Start: `p1=10`, `p2=3`
* Step1: `p1=15`, `p2=6`
* Step2: `p1=30`, `p2=9`
* Step3: `p1=None`, `p2=15`
* Redirect `p1` to `head2`
* Step4: `p1=3`, `p2=30`
* Step5: `p1=6`, `p2=None`
* Redirect `p2` to `head1`
* Step6: `p1=9`, `p2=10`
* Step7: `p1=15`, `p2=15` ✅ same node reference → intersection found

Why it works: both pointers traverse exactly `len1 + len2`, so the “extra length” cancels out.

---

## 3) Python Codes (different ways)

> **Important:** Returning **Node** (not `node.data`) avoids your earlier runtime error when driver does `print(ans.data)`.

---

### A) Easy / Brute: Hashing (set of node references)

**Time:** `O(n+m)`
**Space:** `O(n)`

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def intersectPoint(self, head1, head2):
        # Store references of all nodes from list1
        visited_nodes = set()

        current = head1
        while current:
            visited_nodes.add(current)   # store node identity (reference)
            current = current.next

        # First node in list2 that is already seen is intersection
        current = head2
        while current:
            if current in visited_nodes:
                return current           # return Node (NOT current.data)
            current = current.next

        return None  # problem says intersection always exists
```

---

### B) Optimized (Most expected): Two-pointer switch heads (O(1) space)

**Time:** `O(n+m)`
**Space:** `O(1)`

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def intersectPoint(self, head1, head2):
        # Two pointers starting at both heads
        pointer1 = head1
        pointer2 = head2

        # After at most (n+m) moves, they meet at the intersection node
        while pointer1 is not pointer2:
            # When a pointer hits the end, jump to the other list's head
            pointer1 = pointer1.next if pointer1 else head2
            pointer2 = pointer2.next if pointer2 else head1

        return pointer1  # intersection Node
```

---

### C) Optimized (Also common): Length alignment (O(1) space)

**Time:** `O(n+m)`
**Space:** `O(1)`

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def intersectPoint(self, head1, head2):
        # Helper: compute list length
        def get_length(head):
            length = 0
            current = head
            while current:
                length += 1
                current = current.next
            return length

        len1 = get_length(head1)
        len2 = get_length(head2)

        pointer1, pointer2 = head1, head2

        # Move pointer of longer list ahead by the length difference
        if len1 > len2:
            for _ in range(len1 - len2):
                pointer1 = pointer1.next
        else:
            for _ in range(len2 - len1):
                pointer2 = pointer2.next

        # Now both pointers are equally far from intersection
        while pointer1 is not pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1  # intersection Node
```

---

## 4) Interview recall + expected Q&A

### 5-line recall template (super memorizable)

```
p1=head1; p2=head2
while p1 != p2:
    p1 = p1.next if p1 else head2
    p2 = p2.next if p2 else head1
return p1
```

### Mnemonic

**“SWITCH → SAME distance → MEET”**
(or “Two runners swap tracks and meet at merge.”)

### 60-second interview script

1. “Intersection means shared node reference, not value.”
2. “I’ll use two pointers.”
3. “Move both; when one ends, switch it to the other head.”
4. “Both traverse `len1+len2`, so mismatch cancels; they meet at intersection.”
5. “Return that node. O(n+m) time, O(1) space.”

---

## Expected interviewer questions + crisp answers

**Q1. Why use reference comparison (`is`) instead of value comparison?**
A. Because intersection means the same node object; values can repeat.

**Q2. Why does switching heads guarantee meeting?**
A. Each pointer covers exactly `len1+len2` steps. After switching, both have walked the same total distance, so they align at the intersection.

**Q3. What if intersection didn’t exist?**
A. Both pointers would become `None` at the same time; we could return `None`. (Here it’s guaranteed to exist.)

**Q4. Time/space complexity?**
A. `O(n+m)` time, `O(1)` auxiliary space.

**Q5. Another approach?**
A. Hashing nodes is simplest (`O(n)` space). Length-alignment is another `O(1)` method.

**Q6. Edge cases?**
A. Intersection at head, one list fully contained in another, very different lengths—all handled.

If you want, I can also provide the same explanation + code but **returning `data`** (for platforms that expect integer), and show exactly how to match whichever driver you have.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Git / Version control (common ancestor)**

   * Two branches share history; finding the first common commit is analogous to finding the intersection node.

2. **Memory dedup / shared tail objects**

   * Systems that reuse common suffixes (immutable lists, DAG/trie compression) create “Y-shaped” structures. Need to find where two references start sharing data.

3. **Network / route convergence**

   * Two paths (hops) merge at a common router and then follow the same remaining route. Identify the merge point.

4. **Data lineage / pipeline merge**

   * Two processing pipelines merge into a shared downstream stage. Find the first shared stage.

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This runnable program:

* Builds a **Y-shaped linked list** using a **common tail**
* Finds intersection using **two-pointer switch-head** (expected interview solution)
* Prints both lists and intersection node value
* Prints total runtime (end-to-end) with `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: list1 unique part (space-separated)
* Line 2: list2 unique part (space-separated)
* Line 3: common tail part (space-separated) ✅ (creates the Y)

If no stdin, demo uses:

* list1 unique: `10`
* list2 unique: `3 6 9`
* common tail: `15 30`

```python
import sys
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def intersectPoint(self, head1, head2):
        """
        Two-pointer switch-head solution.
        Time: O(n + m)
        Auxiliary Space: O(1)
        Returns: intersection Node (not data)
        """
        pointer1, pointer2 = head1, head2

        # At most (n+m) pointer moves until they meet
        while pointer1 is not pointer2:
            pointer1 = pointer1.next if pointer1 else head2
            pointer2 = pointer2.next if pointer2 else head1

        return pointer1


# ---------- Utilities to build/print lists ----------

def build_list(values):
    """
    Build a linked list from Python list.
    Time: O(L)
    Space: O(L) for nodes created
    Returns: (head, tail)
    """
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head, tail


def attach_tail(list_tail, common_head):
    """
    Attach common_head after list_tail.
    Time: O(1)
    Space: O(1)
    """
    if list_tail:
        list_tail.next = common_head


def list_to_str(head, limit=40):
    """
    Convert linked list to printable string (limit nodes to avoid huge prints).
    Time: O(min(L, limit))
    Space: O(min(L, limit)) for string parts
    """
    parts = []
    cur = head
    count = 0
    while cur and count < limit:
        parts.append(str(cur.data))
        cur = cur.next
        count += 1
    if cur:
        parts.append("...")
    return " -> ".join(parts) + " -> NULL"


def main():
    # Time measurement for full program (parse + build + solve + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        list1_unique = [10]
        list2_unique = [3, 6, 9]
        common_values = [15, 30]
    else:
        # ---------------- INPUT MODE ----------------
        # Line1: list1 unique
        # Line2: list2 unique
        # Line3: common tail
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        list1_unique = list(map(int, lines[0].split())) if len(lines) > 0 else []
        list2_unique = list(map(int, lines[1].split())) if len(lines) > 1 else []
        common_values = list(map(int, lines[2].split())) if len(lines) > 2 else []

    # 1) Build common tail first
    # Time: O(c), Space: O(c)
    common_head, common_tail = build_list(common_values)

    # 2) Build list1 unique part and attach common tail
    # Time: O(n), Space: O(n)
    head1, tail1 = build_list(list1_unique)
    if head1 is None:
        head1 = common_head  # if no unique part, list is just common tail
    else:
        attach_tail(tail1, common_head)  # Time: O(1)

    # 3) Build list2 unique part and attach common tail
    # Time: O(m), Space: O(m)
    head2, tail2 = build_list(list2_unique)
    if head2 is None:
        head2 = common_head
    else:
        attach_tail(tail2, common_head)  # Time: O(1)

    # 4) Find intersection
    # Time: O(n+m), Aux Space: O(1)
    intersection_node = solver.intersectPoint(head1, head2)

    # Print inputs and output
    print("Input:")
    print("List1 Unique:", list1_unique)
    print("List2 Unique:", list2_unique)
    print("Common Tail  :", common_values)

    print("\nConstructed Lists:")
    print("List1:", list_to_str(head1))
    print("List2:", list_to_str(head2))

    print("\nOutput:")
    print("Intersection Node data:", intersection_node.data)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

* List1: `10 -> 15 -> 30 -> NULL`
* List2: `3 -> 6 -> 9 -> 15 -> 30 -> NULL`
* Intersection Node data: `15`

---


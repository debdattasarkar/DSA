# Palindrome Linked List

**Difficulty:** Medium
**Accuracy:** 41.48%
**Submissions:** 379K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

You are given the **head** of a singly linked list of positive integers. You have to check if the given linked list is **palindrome** or not.

---

## Examples

### Example 1

**Input:**
`head -> 1 -> 2 -> 1 -> 1 -> 2 -> 1 -> NULL`

**Output:**
`true`

**Explanation:**
The given linked list is `1 -> 2 -> 1 -> 1 -> 2 -> 1`, which is a palindrome.

---

### Example 2

**Input:**
`head -> 10 -> 20 -> 30 -> 40 -> 50 -> NULL`

**Output:**
`false`

**Explanation:**
The given linked list is `10 -> 20 -> 30 -> 40 -> 50`, which is not a palindrome.

---

### Example 3

**Input:**
`head -> 10 -> 20 -> 30 -> 40 -> 50 -> NULL`

**Output:**
`false`

**Explanation:**
The given linked list is `10 -> 20 -> 30 -> 40 -> 50`, which is not a palindrome.

---

## Constraints

* 1 ≤ number of nodes ≤ 10<sup>5</sup>
* 0 ≤ `node->data` ≤ 10<sup>3</sup>

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Accolite
* Amazon
* Microsoft
* Snapdeal
* MakeMyTrip
* Adobe
* Yodlee Infotech
* KLA Tencor
* Kritikal Solutions

---

## Topic Tags

* Linked List
* palindrome
* Data Structures

---

## Related Interview Experiences

* Makemytrip Sdet Intern Interview Experience On Campus

---

## Related Articles

* [Function To Check If A Singly Linked List Is Palindrome](https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)

---

---

## 2) Text explanation (how to check palindrome in a linked list)

A linked list is a **palindrome** if values read the same from left to right and right to left.

### Most expected interview approach (O(n) time, O(1) space)

1. Use **slow & fast** pointers to find the **middle**
2. **Reverse the second half** of the list (in-place)
3. Compare:

   * pointer from head (1st half)
   * pointer from reversed second half
4. (Good practice) **Restore** the second half back (reverse again)

Why reverse?
Singly list can’t go backward, so we reverse the 2nd half to compare in forward direction.

---

## Step-by-step Dry Run

### Example 1

`1 -> 2 -> 1 -> 1 -> 2 -> 1`

#### Step 1: Find middle

* slow=1, fast=1
* slow=2, fast=1
* slow=1, fast=2
* slow=1, fast=None  (even length)

So second half starts at `slow` (the 4th node): `1 -> 2 -> 1`

#### Step 2: Reverse second half

`1 -> 2 -> 1` becomes `1 -> 2 -> 1` (same values, but pointers reversed)

#### Step 3: Compare

Compare first half vs reversed second half:

* 1 vs 1 ✅
* 2 vs 2 ✅
* 1 vs 1 ✅
  All match → **palindrome = True**

#### Step 4 (optional): Restore

Reverse second half again to keep list unchanged.

---

### Example 2

`10 -> 20 -> 30 -> 40 -> 50`

* Middle is around 30
* Reverse second half: `50 -> 40 -> 30`
* Compare first: `10` vs `50` mismatch → **False**

---

## 3) Python codes (brute + optimized)

### A) Easy/Brute: copy to array and check

**Time:** O(n)
**Space:** O(n)

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def isPalindrome(self, head):
        # Copy values into a Python list
        values = []
        current = head
        while current:
            values.append(current.data)
            current = current.next

        # Two-pointer palindrome check on array
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True
```

---

### B) Most expected: reverse 2nd half in-place (O(1) space)

**Time:** O(n)
**Aux Space:** O(1)

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def isPalindrome(self, head):
        # Edge cases
        if head is None or head.next is None:
            return True

        # ---------- Helper: reverse a linked list ----------
        # Time: O(L), Space: O(1)
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # ---------- Step 1: Find middle using slow/fast ----------
        # Time: O(n), Space: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If odd length, skip the middle element
        # Example: 1->2->3->2->1 (slow at 3; skip it)
        if fast is not None:
            slow = slow.next

        # ---------- Step 2: Reverse second half ----------
        # Time: O(n), Space: O(1)
        second_half_head = reverse_list(slow)

        # ---------- Step 3: Compare halves ----------
        # Time: O(n), Space: O(1)
        first_ptr = head
        second_ptr = second_half_head
        is_palindrome = True

        while second_ptr:  # only need to compare second half length
            if first_ptr.data != second_ptr.data:
                is_palindrome = False
                break
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        # ---------- Step 4 (optional): Restore list ----------
        # Time: O(n), Space: O(1)
        reverse_list(second_half_head)

        return is_palindrome
```

---

### C) Alternative (when asked “don’t modify list”): stack half

**Time:** O(n)
**Space:** O(n/2)

(Useful if interviewer doesn’t allow reversing. Ask and choose.)

---

## 4) Interview memory + expected Q&A

### 5-line pseudo-code template (memorize)

```
find mid using slow/fast
reverse second half
compare head with reversed-half
restore second half (optional)
return match result
```

### Mnemonic

**“MID → REV → MATCH → RESTORE”**

### 60-second recall script (what to say)

1. “Palindrome means same from both ends.”
2. “Find mid with slow/fast.”
3. “Reverse second half to simulate backward traversal.”
4. “Compare node-by-node.”
5. “Restore if needed. O(n) time, O(1) space.”

---

## Expected interviewer Q&A

**Q1. Why slow/fast pointers?**
A. To find middle in one pass: slow moves 1 step, fast moves 2.

**Q2. How do you handle odd length?**
A. If `fast` isn’t None at end, skip the middle (`slow = slow.next`).

**Q3. Why reverse second half?**
A. Singly list can’t traverse backward; reversing makes “back half” comparable forward.

**Q4. Do you modify the input list?**
A. Temporarily yes; I restore it by reversing again.

**Q5. Complexity?**
A. O(n) time, O(1) extra space.

**Q6. Alternative without modifying list?**
A. Use a stack/array to store values (O(n) space).

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Data integrity checks (logs / pipelines)**

   * A sequence should read the same forward/backward (symmetry check) to detect corruption in transmitted/processed data chunks.

2. **Undo/Redo or user action symmetry validation**

   * User action streams (or command sequences) sometimes need to be validated for mirror symmetry (e.g., test automation, replay validation).

3. **Network packet / token validation**

   * Some encodings or token streams can include symmetric patterns; palindrome-like checks are used as quick sanity tests.

4. **DNA / string pattern matching in bioinformatics (simplified analogy)**

   * Palindrome patterns matter in sequences; linked-list version is the same “check symmetry” idea with pointer constraints.

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This program:

* Builds a linked list from input values
* Checks palindrome using **O(1) space** method (reverse second half)
* Prints input list and output True/False
* Prints total runtime of full program using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Single line: list values space-separated, e.g.
  `1 2 1 1 2 1`

If no stdin, demo uses:

* `1 2 1 1 2 1` → True

```python
import sys
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        Optimized approach:
        - Find middle using slow/fast
        - Reverse second half
        - Compare halves
        - Restore second half (optional but good)

        Time: O(n)
        Aux Space: O(1)
        """

        if head is None or head.next is None:
            return True

        # ---------- Helper: reverse list ----------
        # Time: O(L), Space: O(1)
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # ---------- Step 1: Find middle ----------
        # Time: O(n), Space: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If odd length, skip middle element
        # Time: O(1)
        if fast is not None:
            slow = slow.next

        # ---------- Step 2: Reverse second half ----------
        # Time: O(n), Space: O(1)
        second_half_head = reverse_list(slow)

        # ---------- Step 3: Compare halves ----------
        # Time: O(n), Space: O(1)
        first_ptr = head
        second_ptr = second_half_head
        is_palindrome = True

        while second_ptr:
            if first_ptr.data != second_ptr.data:
                is_palindrome = False
                break
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        # ---------- Step 4: Restore list (optional) ----------
        # Time: O(n), Space: O(1)
        reverse_list(second_half_head)

        return is_palindrome


# ---------- Utilities ----------

def build_linked_list(values):
    """Time: O(n), Space: O(n) nodes"""
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
    return head


def list_to_str(head, limit=40):
    """Time: O(min(n,limit)), Space: O(min(n,limit))"""
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
    # Measure full program runtime (parse + build + solve + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        values = [1, 2, 1, 1, 2, 1]
    else:
        # ---------------- INPUT MODE ----------------
        values = list(map(int, data.split()))

    # Build list
    # Time: O(n), Space: O(n) nodes
    head = build_linked_list(values)

    # Solve
    # Time: O(n), Aux Space: O(1)
    result = solver.isPalindrome(head)

    print("Input Linked List:")
    print(list_to_str(head))

    print("\nOutput:")
    print(result)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

Input: `1 -> 2 -> 1 -> 1 -> 2 -> 1 -> NULL`
Output: `True` (+ runtime)

---


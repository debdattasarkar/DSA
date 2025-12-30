# Add Number Linked Lists

**Difficulty:** Medium
**Accuracy:** 34.52%
**Submissions:** 372K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

You are given the head of two singly linked lists **head1** and **head2** representing two **non-negative integers**. You have to return the **head of the linked list** representing the **sum** of these two numbers.

> **Note:** There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

---

## Examples

### Example 1

**Input:**

* `head1`: `1 -> 2 -> 3 -> NULL`
* `head2`: `9 -> 9 -> 9 -> NULL`

**Output:**

* `1 -> 1 -> 2 -> 2`

**Explanation:**
Given numbers are **123** and **999**. Their sum is **1122**.

---

### Example 2

**Input:**

* `head1`: `0 -> 0 -> 6 -> 3 -> NULL`
* `head2`: `0 -> 7 -> NULL`

**Output:**

* `7 -> 0`

**Explanation:**
Given numbers are **63** and **7**. Their sum is **70**.

---

## Constraints

* 1 ≤ Number of nodes in `head1`, `head2` ≤ 10<sup>5</sup>
* 0 ≤ `node->data` ≤ 9

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Flipkart
* Morgan Stanley
* Accolite
* Amazon
* Microsoft
* Snapdeal
* MakeMyTrip
* Qualcomm

---

## Topic Tags

* Linked List
* Data Structures
* two-pointer-algorithm

---

## Related Interview Experiences

* Accolite Interview Experience Set 7 On Campus
* Amazon Interview Experience Set 413 Sdet 1 Campus Internship

---

## Related Articles

* Add Two Numbers Represented By Linked List

---

---

## 2) Explanation (most expected approach)

The lists store digits in **forward order** (MSD first), like:

* `1 -> 2 -> 3` means **123**
* `9 -> 9 -> 9` means **999**

But addition is easiest from the **least significant digit** (end).
So we do:

1. **Reverse both lists** (so LSD comes first)
2. Add like normal digit addition with `carry`
3. Reverse the result to restore forward order
4. **Remove leading zeros** in the output (unless the number is 0)

This matches required: **O(n+m)** time and **O(1)** extra space (reversing in-place).

---

## Step-by-step Dry Run (Example 1)

`head1 = 1 -> 2 -> 3`
`head2 = 9 -> 9 -> 9`

### Step 1: Reverse both

* rev1 = `3 -> 2 -> 1`
* rev2 = `9 -> 9 -> 9`

### Step 2: Add with carry

Start `carry=0`

| rev1 | rev2 | sum = d1+d2+carry | digit | carry |
| ---- | ---- | ----------------- | ----- | ----- |
| 3    | 9    | 12                | 2     | 1     |
| 2    | 9    | 12                | 2     | 1     |
| 1    | 9    | 11                | 1     | 1     |
| -    | -    | 1                 | 1     | 0     |

Result in reverse order: `2 -> 2 -> 1 -> 1` (this represents 1122 reversed)

### Step 3: Reverse result

`1 -> 1 -> 2 -> 2`

### Step 4: Remove leading zeros

None here. Final output: `1 -> 1 -> 2 -> 2`

---

## Dry Run (Example 2)

`head1 = 0 -> 0 -> 6 -> 3` (means 63)
`head2 = 0 -> 7` (means 7)

Reverse:

* rev1 = `3 -> 6 -> 0 -> 0`
* rev2 = `7 -> 0`

Add:

* 3+7=10 → digit 0, carry 1
* 6+0+1=7 → digit 7, carry 0
* remaining zeros → digits 0,0

Result reversed = `0 -> 7 -> 0 -> 0`
Reverse back = `0 -> 0 -> 7 -> 0`
Strip leading zeros → `7 -> 0`

---

# 3) Python Codes (easy/brute + optimized expected)

### Helper functions we’ll use

* `reverse_list(head)` to reverse linked list in-place
* `strip_leading_zeros(head)` to ensure no leading zeros in output

---

## A) “Easy” (uses stacks) — simpler to explain, but uses extra space

**Time:** O(n+m)
**Space:** O(n+m) due to stacks

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        # Push digits into stacks to simulate reverse traversal
        stack1, stack2 = [], []

        cur = head1
        while cur:
            stack1.append(cur.data)
            cur = cur.next

        cur = head2
        while cur:
            stack2.append(cur.data)
            cur = cur.next

        carry = 0
        result_head = None  # we will build result from front (like stack pop)

        # Pop from stacks (LSD first)
        while stack1 or stack2 or carry:
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            # Insert at front (because we're going from LSD to MSD)
            new_node = Node(digit)
            new_node.next = result_head
            result_head = new_node

        # Remove leading zeros (but keep one zero if number is 0)
        while result_head and result_head.data == 0 and result_head.next:
            result_head = result_head.next

        return result_head
```

---

## B) Optimized (Most expected): Reverse both lists, add, reverse back

**Time:** O(n+m)
**Aux Space:** O(1)

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):

        # ---------- Helper: reverse a linked list ----------
        # Time: O(L), Space: O(1)
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # ---------- Helper: remove leading zeros ----------
        # Time: O(L), Space: O(1)
        def strip_leading_zeros(head):
            # Keep at least one node if the number is 0
            while head and head.data == 0 and head.next:
                head = head.next
            return head

        # 1) Reverse both input lists (in-place)
        # Time: O(n+m), Space: O(1)
        rev1 = reverse_list(head1)
        rev2 = reverse_list(head2)

        # 2) Add digit-by-digit like classic addition
        # Time: O(n+m), Space: O(1) extra (output list nodes are required)
        carry = 0
        dummy = Node(0)
        tail = dummy

        ptr1, ptr2 = rev1, rev2
        while ptr1 or ptr2 or carry:
            digit1 = ptr1.data if ptr1 else 0
            digit2 = ptr2.data if ptr2 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = Node(digit)
            tail = tail.next

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        # 3) Reverse the result to restore forward order
        # Time: O(n+m), Space: O(1)
        result = reverse_list(dummy.next)

        # 4) Remove leading zeros in output
        result = strip_leading_zeros(result)

        # (Optional) If you want to restore input lists to original order, reverse rev1/rev2 back.
        return result
```

**Note:** This modifies input lists by reversing. Many platforms accept that.
If interviewer cares, mention: “We can reverse them back at end to restore.”

---

# 4) Interview recall + expected Q&A

## Quick memory trick

**“REV → ADD → REV → TRIM”**

1. Reverse both lists
2. Add with carry
3. Reverse result
4. Trim leading zeros

## 60-second explanation script

* “Digits are stored forward, but addition needs LSD first.”
* “Reverse both lists to process from LSD.”
* “Classic addition with carry, build result.”
* “Reverse result back.”
* “Strip leading zeros (keep one digit if 0).”
* “Time O(n+m), space O(1).”

---

## Interviewer Q&A (common)

**Q1. Why reverse the lists?**
A. Because we need to add from least significant digit; reversal makes LSD come first without recursion/stack.

**Q2. How do you handle different lengths?**
A. If one pointer becomes null, treat its digit as 0.

**Q3. What about carry at the end?**
A. Keep looping while `carry` exists; add an extra node if needed (e.g., 999+1 → 1000).

**Q4. Why remove leading zeros?**
A. Input may have leading zeros; output must not (except when the sum is 0).

**Q5. What if interviewer says “don’t modify input lists”?**
A. Use stacks (O(n+m) extra) or reverse but reverse back at end to restore.

**Q6. Complexity?**
A. Each list reversed once, traversed once, result reversed once: **O(n+m)** time, **O(1)** auxiliary space.

If you want next, I can add (5) real-world use cases + (6) full runnable program with building lists, printing output, and timing (same style as your earlier requests).

---

---

## 5) Real-World Use Cases (few, interviewer-relatable)

1. **Big integer addition (financial / ledger systems)**
   When numbers exceed built-in integer limits (very large account IDs, checksums, balances), systems store them as digit lists/blocks. Adding them is exactly this problem.

2. **Arbitrary precision math libraries / cryptography**
   RSA/ECC workflows use huge integers. Internally, numbers are stored in chunks (like a linked list/array of digits/words). Addition with carry is a core primitive.

3. **Streaming / memory-constrained representations**
   Sometimes you don’t want to convert the entire number to a big integer object; representing digits as nodes lets you process incrementally and avoid overflow.

4. **Data import with leading zeros (IDs, codes)**
   Input might contain leading zeros (e.g., “00063”), but normalized output shouldn’t (“70”). This mirrors the “trim leading zeros” requirement.

---

## 6) Full Program (timed run + input/output + inline complexity)

This is a complete runnable Python program:

* Builds linked lists from digit arrays
* Adds them using the **optimized expected approach (reverse + add + reverse + trim)**
* Prints input lists and output list
* Prints total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: digits of list1 (space-separated), e.g. `1 2 3`
* Line 2: digits of list2 (space-separated), e.g. `9 9 9`

If no stdin, it runs demo example.

```python
import sys
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, head1, head2):
        """
        Optimized approach:
        1) Reverse both lists
        2) Add like classic addition with carry
        3) Reverse result
        4) Strip leading zeros

        Time: O(n + m)
        Aux Space: O(1)  (excluding output nodes which are required)
        """

        # ---------- Reverse list ----------
        # Time: O(L), Space: O(1)
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # ---------- Strip leading zeros ----------
        # Time: O(L), Space: O(1)
        def strip_leading_zeros(head):
            while head and head.data == 0 and head.next:
                head = head.next
            return head

        # 1) Reverse inputs (in-place)
        # Time: O(n + m), Space: O(1)
        rev1 = reverse_list(head1)
        rev2 = reverse_list(head2)

        # 2) Add digit-by-digit
        # Time: O(n + m), Space: O(1) extra
        carry = 0
        dummy = Node(0)
        tail = dummy

        p1, p2 = rev1, rev2
        while p1 or p2 or carry:
            digit1 = p1.data if p1 else 0
            digit2 = p2.data if p2 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = Node(digit)
            tail = tail.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        # 3) Reverse result back to forward order
        # Time: O(n + m), Space: O(1)
        result = reverse_list(dummy.next)

        # 4) Remove leading zeros (keep single zero if needed)
        # Time: O(n + m), Space: O(1)
        result = strip_leading_zeros(result)

        # NOTE: If interviewer wants input lists preserved, reverse rev1/rev2 back here.
        return result


# ---------- Utility: build list ----------
# Time: O(L), Space: O(L) for nodes
def build_linked_list(digits):
    head = None
    tail = None
    for d in digits:
        node = Node(d)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


# ---------- Utility: convert list to python list ----------
# Time: O(L), Space: O(L)
def linked_list_to_list(head):
    out = []
    cur = head
    while cur:
        out.append(cur.data)
        cur = cur.next
    return out


def main():
    # Measure full program runtime (parse + build + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        # Example 1:
        digits1 = [1, 2, 3]
        digits2 = [9, 9, 9]
    else:
        # ---------------- INPUT MODE ----------------
        # Line1: digits of list1
        # Line2: digits of list2
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        digits1 = list(map(int, lines[0].split()))
        digits2 = list(map(int, lines[1].split()))

    # Build linked lists
    # Time: O(n+m), Space: O(n+m)
    head1 = build_linked_list(digits1)
    head2 = build_linked_list(digits2)

    # Compute sum list
    # Time: O(n+m), Aux Space: O(1)
    result_head = solver.addTwoLists(head1, head2)

    # Print input and output
    print("Input:")
    print("head1 =", " -> ".join(map(str, digits1)))
    print("head2 =", " -> ".join(map(str, digits2)))

    result_digits = linked_list_to_list(result_head)
    print("\nOutput:")
    print("result =", " -> ".join(map(str, result_digits)))

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Example Output (Demo Mode)

Input: `1 -> 2 -> 3` and `9 -> 9 -> 9`
Output: `1 -> 1 -> 2 -> 2` (+ runtime)


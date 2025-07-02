
---

# 🔁 Remove Loop in Linked List

### 🟡 Difficulty: Medium

**Accuracy:** 27.66%
**Submissions:** 520K+
**Points:** 4
**Average Time:** 45 mins

---

## 🔍 Problem Statement

Given the `head` of a linked list that **may contain a loop**, your task is to **remove the loop** (if present).

* A **loop** means that the last node points back to one of the previous nodes in the list.
* You must **detect and remove the loop**, restoring a proper singly linked list.

### 🧾 Custom Input Format

* A **head** of a singly linked list.
* A **pos** (1-based index) denoting the position of the node to which the last node points:

  * `pos = 0` means no loop (last node points to `null`).

**Output:**
Return `true` if loop is removed or list was already clean; otherwise `false`.

---

## 🧪 Examples

### Example 1:

**Input:** `head = 1 -> 3 -> 4`, `pos = 2`
**Output:** `true`
**Explanation:** Loop from 4 → 3 is removed.

---

### Example 2:

**Input:** `head = 1 -> 8 -> 3 -> 4`, `pos = 0`
**Output:** `true`
**Explanation:** No loop exists. Return `true`.

---

### Example 3:

**Input:** `head = 1 -> 2 -> 3 -> 4`, `pos = 1`
**Output:** `true`
**Explanation:** Loop from 4 → 1 is removed.

---

## 🔒 Constraints

* `1 ≤ size of linked list ≤ 10⁵`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## 💼 Company Tags

`VMWare`, `Morgan Stanley`, `Amazon`, `Microsoft`, `Snapdeal`, `MakeMyTrip`, `Oracle`, `Walmart`, `Goldman Sachs`, `Adobe`, `Qualcomm`

---

## 🧠 Topic Tags

* Linked List
* Two-pointer algorithm
* Data Structures
* Algorithms

---

## 📘 Explanation with Step-by-Step Dry Run

### ✅ Key Idea: Floyd’s Cycle Detection (Tortoise and Hare)

#### Steps:

1. **Detect the Loop:**

   * Use slow and fast pointers.
   * If they meet, a loop exists.

2. **Find Start of Loop:**

   * Move one pointer to head, keep the other at meeting point.
   * Move both one step at a time until they meet again → this is loop start.

3. **Remove the Loop:**

   * Traverse until `loop_node.next == loop_node_start`.
   * Set `loop_node.next = None`.

---

### 🧪 Dry Run Example:

Input: `1 → 2 → 3 → 4 → 5 → 3 (loop)`

* **Detect loop:**
  Slow = 3, Fast = 3 → ✅ they meet

* **Find start:**
  Move slow to head, walk together:
  `1==4` → ❌
  `2==5` → ❌
  `3==3` → ✅ Start found at node 3

* **Remove:**
  Traverse from node 5, `5.next == 3` → `5.next = None`

✅ Loop is removed

---

## ✅ Optimized Code with Node Class

---

### 🐍 Python

```python
# Node class:
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Step 1: Detect loop using Floyd’s algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return  # No loop

        # Step 2: Find the start of the loop
        slow = head
        if slow == fast:
            # Special case: loop starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 3: Break the loop
        fast.next = None
```

**🔍 Note on Usage of `Node` Class:**

* Each node is an instance of `Node`, with `data` and `next`.
* Comparisons like `if slow == fast` compare **reference equality** of `Node` objects.

---

### 💠 C++

```cpp
// structure of linked list node:

struct Node {
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = NULL;
    }
};

class Solution {
  public:
    void removeLoop(Node* head) {
        if (!head || !head->next) return;

        Node* slow = head;
        Node* fast = head;

        // Step 1: Detect Loop
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) break;
        }

        // No loop found
        if (slow != fast) return;

        // Step 2: Find loop starting point
        slow = head;

        if (slow == fast) {
            // loop starts at head
            while (fast->next != slow)
                fast = fast->next;
        } else {
            while (slow->next != fast->next) {
                slow = slow->next;
                fast = fast->next;
            }
        }

        // Step 3: Break loop
        fast->next = NULL;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {Node} head
 */
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Solution {
    // Function to remove a loop in the linked list.
    removeLoop(head) {
        if (!head || !head.next) return;

        let slow = head;
        let fast = head;

        // Step 1: Detect Loop
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow === fast) break;
        }

        if (slow !== fast) return; // No loop

        // Step 2: Find loop starting point
        slow = head;

        if (slow === fast) {
            while (fast.next !== slow)
                fast = fast.next;
        } else {
            while (slow.next !== fast.next) {
                slow = slow.next;
                fast = fast.next;
            }
        }

        // Step 3: Break loop
        fast.next = null;
    }
}
```

---

## 💬 Interview Questions & Answers

---

### ❓Q1: How do you detect a loop in a linked list?

**A:** Use **Floyd’s Cycle Detection Algorithm** (Tortoise and Hare). If `slow == fast` at some point, a loop exists.

---

### ❓Q2: Once a loop is detected, how do you find its starting node?

**A:** Move one pointer to `head`, keep the other at the meeting point. Move both one step until they meet — this is the loop start.

---

### ❓Q3: Why do we check `slow == fast` again after breaking from the loop?

**A:** To handle the special case when the loop starts from the head (self-loop from last node to head).

---

### ❓Q4: Why do we use reference comparison (`==`) instead of data values?

**A:** Because multiple nodes can have the same `data`, but `==` compares object **addresses** or **references**, which is accurate.

---

### ❓Q5: Can this be solved with extra space?

**A:** Yes, using a HashSet to track visited nodes, but it uses O(n) space. Floyd’s method is preferred as it uses O(1) space.

---

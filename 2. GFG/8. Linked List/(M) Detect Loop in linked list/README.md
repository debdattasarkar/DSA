
---

# 🔁 Detect Loop in Linked List

### 🟡 Difficulty: Medium

**Accuracy:** 43.49%
**Submissions:** 486K+
**Points:** 4
**Average Time:** 20m

---

## 🔍 Problem Statement

You are given the **head** of a singly linked list. Your task is to **determine if the linked list contains a loop**.

A loop exists in a linked list if the **next pointer of the last node** points to **any other node in the list** (including itself), rather than being `null`.

---

## 🧾 Custom Input Format

* A **head** of a singly linked list
* A **pos** (1-based index) that indicates where the last node connects back to.

  * If `pos = 0`, it means no loop (the last node points to `null`).

---

## 🧪 Examples

### Example 1:

**Input:** `head = 1 -> 3 -> 4`, `pos = 2`
**Output:** `true`
**Explanation:** The last node (4) connects to the second node (3), creating a loop.

---

### Example 2:

**Input:** `head = 1 -> 8 -> 3 -> 4`, `pos = 0`
**Output:** `false`
**Explanation:** The list has no loop.

---

### Example 3:

**Input:** `head = 1 -> 2 -> 3 -> 4`, `pos = 1`
**Output:** `true`
**Explanation:** The last node (4) connects to the first node (1), forming a loop.

---

## 🔒 Constraints

* `1 ≤ number of nodes ≤ 10⁴`
* `1 ≤ node.data ≤ 10³`
* `0 ≤ pos ≤ number of nodes in Linked List`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## 💼 Company Tags

`Paytm`, `VMWare`, `Amazon`, `Samsung`, `Snapdeal`, `MakeMyTrip`, `Walmart`, `Qualcomm`, `SAP Labs`, `Adobe`, `OYO Rooms`, `Lybrate`, `D-E-Shaw`

---

## 🧠 Topic Tags

* Linked List
* Two-Pointer Algorithm
* Data Structures
* Algorithms

---

## 📘 Text Explanation + Step-by-Step Dry Run

### ✅ Key Idea: Floyd’s Cycle Detection Algorithm (Tortoise and Hare)

1. Use two pointers (`slow`, `fast`) initialized at the head.
2. Move `slow` by 1 step and `fast` by 2 steps in a loop.
3. If there's a loop, both will eventually meet.
4. If `fast` or `fast.next` becomes `null`, no loop exists.

---

### 🧪 Dry Run

**Input:** `1 → 2 → 3 → 4 → 2 (loop back)`

* Initial: `slow = 1`, `fast = 1`
* Step 1: `slow = 2`, `fast = 3`
* Step 2: `slow = 3`, `fast = 2`
* Step 3: `slow = 4`, `fast = 4` ✅ Loop Detected

---

## ✅ Optimized Code Implementations

---

### 🐍 Python

```python
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Return boolean value True or False
class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow = head
        fast = head

        # Traverse using two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Loop detected

        return False  # No loop
```

🧠 **How the Node class is used:**

* Each element in the list is an instance of the `Node` class.
* The algorithm compares **object references** using `slow == fast`.

---

### 💠 C++

```cpp
/* structure of linked list node:*/

struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

class Solution {
  public:
    // Function to check if the linked list has a loop.
    bool detectLoop(Node* head) {
        Node* slow = head;
        Node* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) return true;
        }

        return false;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {Node} head
 * @returns {boolean}
 */
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Solution {
    // Function to check if the linked list has a loop.
    detectLoop(head) {
        let slow = head;
        let fast = head;

        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow === fast) return true;
        }

        return false;
    }
}
```

---

## 💬 Interview Questions & Answers

---

### ❓Q1: What is Floyd’s Cycle Detection Algorithm?

**A:** It uses two pointers (`slow` and `fast`) that move at different speeds. If they meet, a loop exists.

---

### ❓Q2: Why is this algorithm better than using a HashSet?

**A:** Because it uses **O(1) space**, whereas a HashSet-based approach uses **O(n)** space.

---

### ❓Q3: What if the loop starts at the head?

**A:** The algorithm still works. Pointers will eventually meet inside the loop.

---

### ❓Q4: Can `node.data` be used to detect loops?

**A:** No. Nodes can have duplicate values. Loops must be detected by **pointer references**, not data.

---

### ❓Q5: What’s the time complexity?

**A:** `O(n)` — each pointer traverses the list at most once.

---

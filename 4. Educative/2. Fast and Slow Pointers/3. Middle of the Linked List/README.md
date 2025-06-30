
---

# 🧩 Problem: Middle of the Linked List

## 📄 Statement

Given the `head` of a singly linked list, return the **middle node** of the list.

* If the number of nodes is **even**, return the **second** middle node.

---

## 🧷 Constraints

* `1 ≤ n ≤ 100`
* `-100 ≤ node.val ≤ 100`
* `head ≠ NULL`

---

## 🧪 Example

**Input:** `1 -> 2 -> 3 -> 4 -> 5`
**Output:** `3`

**Input:** `2 -> 4 -> 6 -> 8 -> 10 -> NULL`
**Output:** `8`
Explanation: Length = 6 (even), so return 4th node (second middle).

---

## 💡 Approach: Fast and Slow Pointers

We use two pointers:

* `slow`: moves **1 step** at a time.
* `fast`: moves **2 steps** at a time.

### 🔄 Logic:

* When `fast` reaches the end, `slow` will be at the **middle**.
* This works because `fast` covers twice the distance of `slow`.

---

## 🧭 Steps to Implement

1. Initialize `slow` and `fast` at the head.
2. While `fast` and `fast.next` exist:

   * Move `slow` 1 step.
   * Move `fast` 2 steps.
3. When the loop exits, `slow` will be at the middle node.
4. Return `slow`.

---

## ✅ Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

---

## ⏱ Time & Space Complexity

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | O(n)   |
| Space Complexity | O(1) ✅ |

---

## 🧠 Summary

* This is a classic **two-pointer** problem.
* Efficient and simple solution with constant space.
* Return `slow` when `fast` reaches the end.

Great! You've shared the full walkthrough from Grokking's “Middle of the Linked List” problem, including both naive and optimized approaches.

Here's the **complete README** version, converted and structured from your image (including diagrams and logic).

---

# 📘 Solution: Middle of the Linked List

## 🧠 Problem Statement

Given the **head** of a singly linked list, return the **middle node**.
If the number of nodes is even, **return the second middle node**.

---

## 🔒 Constraints

* $1 \leq n \leq 100$ — where `n` is the number of nodes
* $-100 \leq \text{node.val} \leq 100$
* Head is guaranteed to be non-null.

---

## 🪜 Naive Approach

### Idea:

* Store all nodes in an array.
* Return the node at index `len(nodes) // 2`.

### Time Complexity:

* $O(n)$

### Space Complexity:

* $O(n)$

---

## ⚡ Optimized Approach: Fast and Slow Pointers

### Core Idea:

* Use **two pointers**:

  * `slow` moves one step at a time.
  * `fast` moves two steps at a time.

### Algorithm:

1. Initialize both `slow` and `fast` at the head.
2. Move `slow` by 1 and `fast` by 2 steps until `fast` reaches the end.
3. When `fast` reaches the end, `slow` will be at the middle.

> This method ensures constant space and linear time.

### Dry Run Example:

Given:

```
head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
```

Steps:

* Iteration 1: slow = 2, fast = 3
* Iteration 2: slow = 3, fast = 5
* Iteration 3: slow = 4, fast = NULL
  \=> return node with value **4**

---

## ✅ Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

---

## 🧮 Time and Space Complexity

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | O(n)   |
| Space Complexity | O(1) ✅ |

---

## 🧪 Example Test Case

**Input:** `1 -> 2 -> 3 -> 4 -> 5 -> 6`
**Output:** `4`

---

## 🎯 Summary

* This is a classic two-pointer technique.
* Optimized for both time and space.
* Works for both odd and even lengths by returning the **second** middle in even case.

Great! You've shared the full walkthrough from Grokking's “Middle of the Linked List” problem, including both naive and optimized approaches.

Here's the **complete README** version, converted and structured from your image (including diagrams and logic).

---

# 📘 Solution: Middle of the Linked List

## 🧠 Problem Statement

Given the **head** of a singly linked list, return the **middle node**.
If the number of nodes is even, **return the second middle node**.

---

## 🔒 Constraints

* $1 \leq n \leq 100$ — where `n` is the number of nodes
* $-100 \leq \text{node.val} \leq 100$
* Head is guaranteed to be non-null.

---

## 🪜 Naive Approach

### Idea:

* Store all nodes in an array.
* Return the node at index `len(nodes) // 2`.

### Time Complexity:

* $O(n)$

### Space Complexity:

* $O(n)$

---

## ⚡ Optimized Approach: Fast and Slow Pointers

### Core Idea:

* Use **two pointers**:

  * `slow` moves one step at a time.
  * `fast` moves two steps at a time.

### Algorithm:

1. Initialize both `slow` and `fast` at the head.
2. Move `slow` by 1 and `fast` by 2 steps until `fast` reaches the end.
3. When `fast` reaches the end, `slow` will be at the middle.

> This method ensures constant space and linear time.

### Dry Run Example:

Given:

```
head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
```

Steps:

* Iteration 1: slow = 2, fast = 3
* Iteration 2: slow = 3, fast = 5
* Iteration 3: slow = 4, fast = NULL
  \=> return node with value **4**

---

## ✅ Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

---

## 🧮 Time and Space Complexity

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | O(n)   |
| Space Complexity | O(1) ✅ |

---

## 🧪 Example Test Case

**Input:** `1 -> 2 -> 3 -> 4 -> 5 -> 6`
**Output:** `4`

---

## 🎯 Summary

* This is a classic two-pointer technique.
* Optimized for both time and space.
* Works for both odd and even lengths by returning the **second** middle in even case.

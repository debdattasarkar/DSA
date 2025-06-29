
---

# 🔁 Problem: Linked List Cycle

### 📜 Statement

Given the head of a linked list, determine whether the list contains a **cycle**.

> A cycle exists if a node is **revisited** by following the `.next` pointers.

### ✅ Goal

Return:

* `True` if a cycle **is** present,
* `False` otherwise.

---

## 📌 Constraints

* `0 ≤ n ≤ 500` (where `n` is the number of nodes)
* `−10⁵ ≤ node.val ≤ 10⁵`

---

## 🧠 Key Concept: Floyd’s Tortoise and Hare

Also known as the **Fast and Slow Pointer** method:

* Two pointers traverse the list at different speeds.
* If there's a **cycle**, the fast pointer will eventually **lap** the slow pointer.
* If no cycle, fast pointer reaches the end.

---

## 🔄 Algorithm Steps

1. **Initialize** two pointers (`slow` and `fast`) to the head.
2. **Move** `slow` by 1 step and `fast` by 2 steps in a loop.
3. If at any point `slow == fast` → cycle detected.
4. If `fast` or `fast.next` becomes `None` → no cycle.

---

## ✅ Example

Linked List:
`2 → 4 → 6 → 8 → 10` and `10 → 4 (cycle)`

Pointers:

* Initially both at `2`
* slow = `4`, fast = `6`
* slow = `6`, fast = `10`
* slow = `8`, fast = `6`
* slow = `10`, fast = `10` → Match! Cycle detected ✔️

---

## 🧾 Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## 🧮 Time & Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(n)** |
| Space      | **O(1)** |

---

## ✅ Final Notes

* This is a **classic application** of the two-pointer technique.
* Memory-efficient: **No extra data structure** (like a set) is required.
* Works reliably for both short and long lists.

---

# 🔄 Solution: Linked List Cycle

## 📘 Problem Statement

You are given the `head` of a linked list. Determine if the list contains a **cycle**:

* A cycle exists **if a node is revisited** while traversing using `.next`.
* Return `True` if a cycle exists, otherwise return `False`.

### ✳️ Constraints

* `0 ≤ n ≤ 500`
* `-10⁵ ≤ node.val ≤ 10⁵`

---

## 💡 Solution Overview

We explore two common approaches:

---

### 1. 🧠 Naive Approach — Using Hash Set

* Traverse the linked list.
* Store visited nodes in a hash set.
* If a node is **already present**, a cycle exists → `True`.
* If traversal ends (`None`), then no cycle → `False`.

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)` (due to hash set storage)

---

### 2. ⚡ Optimized Approach — Floyd’s Tortoise and Hare

Use **two pointers**:

* `slow` pointer → 1 step at a time
* `fast` pointer → 2 steps at a time

#### Logic:

* If a cycle exists, `fast` will **lap** `slow`, and they will eventually meet.
* If `fast` or `fast.next` becomes `None`, no cycle.

**Time Complexity:** `O(n)`
**Space Complexity:** `O(1)` ✅ (no extra data structure)

---

## 🧭 Steps to Implement

1. Initialize `slow` and `fast` at the `head`.
2. While `fast` and `fast.next` are not `None`:

   * Move `slow` by 1 step.
   * Move `fast` by 2 steps.
   * If they meet → return `True`
3. If loop ends, return `False`.

---

## 🧪 Example

```txt
Input:  2 → 4 → 6 → 8 → 10
                ↑       ↓
                ← ← ← ← ←
Output: True
```

Both pointers start at 2 and move until they meet inside the cycle.

---

## 🧾 Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## 🧮 Time & Space Complexity

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | O(n)   |
| Space Complexity | O(1) ✅ |

---

## ✅ Summary

* The **Floyd’s Cycle Detection** algorithm is efficient and elegant.
* No additional memory required.
* Works well for lists of any size.

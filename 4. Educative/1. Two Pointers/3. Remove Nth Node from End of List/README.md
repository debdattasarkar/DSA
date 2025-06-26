
---

## ❓ Main Question: Remove Nth Node From End of List

**Problem Statement**:
Given the `head` of a singly linked list and an integer `n`, **remove the nth node from the end** of the list and return the modified list's head.

---

## 📌 Constraints

* $1 \leq \text{Length of List} \leq 10^5$
* $-10^9 \leq \text{Node Value} \leq 10^9$
* $1 \leq n \leq \text{Length of List}$

---

## 🧠 Key Pointers to Remember for Interviews

### 1. **Use Two-Pointer Technique**

* Maintain a `right` and `left` pointer.
* Advance the `right` pointer `n` steps first.
* Then move both `right` and `left` together until `right` reaches the end.
* Now `left` is just **before the node** to delete.

### 2. **Edge Case: Remove Head**

* If `right` becomes `None` right after moving `n` steps, it means the head is to be removed.
* Return `head.next`.

### 3. **Pointer Manipulation**

* To remove the node:
  `left.next = left.next.next`

---

## 🧮 Step-by-Step Plan

1. **Move the right pointer `n` steps forward**.
2. If `right` is `None`, return `head.next`.
3. Otherwise, move both pointers until `right.next == None`.
4. Skip the node using:
   `left.next = left.next.next`
5. Return the modified head.

---

## ✅ Example

**Input**: `43 → 68 → 11 → 5 → 69 → 37 → 70 → NULL`, `n = 1`
**Output**: `43 → 68 → 11 → 5 → 69 → 37 → NULL`

(70 is removed — the 1st from the end)

---

## ⏱️ Time and Space Complexity

* **Time**: `O(L)` — where L is the length of the list
* **Space**: `O(1)` — no extra space, only pointers used

---


Here are the key **interview pointers** and must-remember insights from the image on the **“Remove Nth Node from End of List”** problem:

---

## ✅ Interview Pointers to Remember

### 🔹 Problem Statement Recap:

Remove the **n-th node from the end** of a **singly linked list** and return the head of the updated list.

---

### 🔧 Naive vs Optimized

#### 🛠️ Naive Approach:

* **Two traversals**:

  1. Count total number of nodes (length `L`)
  2. Traverse again to `(L - n)`-th node and delete the next

#### ⚡ Optimized (Two Pointers):

* Only **one traversal** using:

  * `left` and `right` pointers, both starting at `head`
  * Move `right` ahead by `n` steps first
  * Then move both pointers until `right` reaches the end
  * At that point, `left` is just before the node to delete

---

## 💡 Important Logic Points

### ✅ When to delete `head`

* If `right` becomes `None` after shifting `n` steps → head is the node to be removed

  * Return `head.next`

### ✅ Deleting the node

* After reaching correct position:
  `left.next = left.next.next`

### ✅ Summary of Two Pointer Steps

1. Initialize `left`, `right` to `head`
2. Move `right` `n` steps forward
3. If `right == None`: return `head.next`
4. Else move both pointers until `right.next == None`
5. Skip the node using:
   `left.next = left.next.next`
6. Return `head`

---

## ⏱️ Time and Space Complexity

* **Time Complexity**: `O(N)` – Only one pass
* **Space Complexity**: `O(1)` – Constant space using two pointers

---

## 🧪 Visual Aid Example (from image)

For `n = 3`
List: `1 → 2 → 3 → 4 → 5 → 6 → 7 → NULL`
Result: `1 → 2 → 3 → 4 → 5 → 7 → NULL` (node `6` is removed)

---

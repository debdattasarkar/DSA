
---

## ✅ Problem Summary

Given two nodes `p` and `q` in a binary tree where each node has a parent pointer (but **no root is given**), return their **lowest common ancestor (LCA)**.

---

## 🛠️ Constraints

* All node values are unique.
* Both `p` and `q` are guaranteed to exist in the tree.
* Tree size is within \[2, 500].

---

## 🌳 LCA Definition

> The LCA of `p` and `q` is the **lowest** node in the tree that has both `p` and `q` as descendants (a node is allowed to be a descendant of itself).

---

## 🔍 Core Idea: **Two Pointers**

Use **two pointers** that traverse the tree **upward via parent links**:

### ✅ Steps:

1. **Initialize two pointers**, one on `p` and one on `q`.
2. **Climb upward** level by level from both pointers:

   * If either pointer reaches the root (`None`), redirect it to the other starting node.
3. **When they meet**, that’s the **LCA**.

---

### 💡 Why It Works:

This works like the intersection of two singly linked lists: when both pointers have traversed the same number of steps, they'll meet at the common ancestor.

---

## 🧠 Time & Space Complexity

* **Time:** O(h), where `h` is the height of the tree.
* **Space:** O(1), no extra memory used.


---

## ✅ Problem: Lowest Common Ancestor of a Binary Tree III

You are given two nodes `p` and `q`, each with a pointer to its parent (but no access to the root). Your goal is to **find the Lowest Common Ancestor (LCA)** using only the parent pointers.

---

## 🧠 Core Idea: Two-Pointer Technique

This is similar to finding the **intersection of two linked lists**.

### ✔️ Step-by-step:

1. **Initialize two pointers:**

   * `ptr1` starting at node `p`
   * `ptr2` starting at node `q`

2. **Move up the tree**:

   * If `ptr1` has a parent → move to `ptr1.parent`; else → jump to `q`.
   * If `ptr2` has a parent → move to `ptr2.parent`; else → jump to `p`.

3. **Repeat** until `ptr1 == ptr2`. That node is the **LCA**.

---

## 📌 Why This Works:

Both pointers will traverse equal distances by **switching start points** once they hit the root. When they finally meet, it's guaranteed to be the **lowest node** common to both.

---

## 📈 Complexity

* **Time:** O(h), where `h` is the height of the tree.
* **Space:** O(1), since only two pointers are used.

---

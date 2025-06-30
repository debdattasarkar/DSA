
---

## 🔍 Find the Duplicate Number

### 📘 Problem Statement:

You're given an array `nums` of `n + 1` integers where:

* Each integer is in the range `[1, n]`.
* There is **only one duplicate number**, but it can appear multiple times.

🔒 **Constraints:**

* Must not modify the input array.
* Must use **constant extra space**.
* Must have **better than O(n²)** time complexity.

---

### ✅ Goal:

Return the **duplicate** number.

---

## 🧠 Key Insight:

This is a **cycle detection** problem. Treat the array as a **linked list**, where:

* `nums[i]` points to the next index.
* There must be a **cycle**, and the entrance to the cycle is the **duplicate** number.

---

## 🐢🐇 Floyd’s Tortoise and Hare Algorithm

### 🔄 Steps:

1. **Traverse `nums` using two pointers**: `slow` and `fast`.

2. **Move pointers until they meet**:

   * `slow` moves one step: `slow = nums[slow]`
   * `fast` moves two steps: `fast = nums[nums[fast]]`

3. After the first meeting point, **reset one pointer to the start**.

4. Move both pointers at the same pace:

   * `slow = nums[slow]`
   * `fast = nums[fast]`

5. The meeting point is the **duplicate number**.

---

## 🧮 Complexity:

* **Time**: `O(n)`
* **Space**: `O(1)`

---

## 🔍 Problem Summary: Find the Duplicate Number

You're given an array `nums` with:

* `n + 1` integers
* Each integer in the range `[1, n]`
* Only one integer **appears more than once**, possibly multiple times

🔒 **Constraints:**

* Do **not** modify the array
* Use only **constant extra space**
* Solve in **O(n)** time

---

## 🧠 Core Insight: Cycle Detection in a Linked List

This problem transforms into detecting a **cycle in a linked list**:

* Treat each index as a node
* Treat `nums[i]` as the pointer to the next node

Since the array contains `n + 1` elements but only `n` distinct values, a **cycle is guaranteed**.

---

## 🐢🐇 Floyd’s Cycle Detection (Tortoise and Hare)

### ✨ Step-by-Step Algorithm:

1. **Phase 1 – Find Intersection Point**

   * Initialize `slow` and `fast` to the **start** of the array.
   * Move `slow` one step: `slow = nums[slow]`
   * Move `fast` two steps: `fast = nums[nums[fast]]`
   * Loop until `slow == fast` (i.e., they meet inside the cycle)

2. **Phase 2 – Find Cycle Entrance (Duplicate Number)**

   * Reinitialize `slow = 0`
   * Move both `slow` and `fast` one step at a time until `slow == fast`
   * The meeting point is the **duplicate number**

---

### 🔄 Mathematical Mapping:

Let `f(x) = nums[x]`, so the traversal becomes:

```
x → nums[x] → nums[nums[x]] → ...
```

---

### 🧪 Example:

Input: `[2, 3, 1, 3]`
Start: `x = nums[0] = 2` → next: `nums[2] = 1` → next: `nums[1] = 3` → next: `nums[3] = 3` (cycle)

Cycle is formed starting at 3.

---

## ⏱️ Time and Space Complexity:

* **Time**: `O(n)`
* **Space**: `O(1)` (no extra space used)

---

Here is the extracted explanation and step-by-step breakdown for the **Find the Duplicate Number** problem using Floyd’s Tortoise and Hare cycle detection:

---

## 🔍 Problem Summary: Find the Duplicate Number

You're given an array `nums` with:

* `n + 1` integers
* Each integer in the range `[1, n]`
* Only one integer **appears more than once**, possibly multiple times

🔒 **Constraints:**

* Do **not** modify the array
* Use only **constant extra space**
* Solve in **O(n)** time

---

## 🧠 Core Insight: Cycle Detection in a Linked List

This problem transforms into detecting a **cycle in a linked list**:

* Treat each index as a node
* Treat `nums[i]` as the pointer to the next node

Since the array contains `n + 1` elements but only `n` distinct values, a **cycle is guaranteed**.

---

## 🐢🐇 Floyd’s Cycle Detection (Tortoise and Hare)

### ✨ Step-by-Step Algorithm:

1. **Phase 1 – Find Intersection Point**

   * Initialize `slow` and `fast` to the **start** of the array.
   * Move `slow` one step: `slow = nums[slow]`
   * Move `fast` two steps: `fast = nums[nums[fast]]`
   * Loop until `slow == fast` (i.e., they meet inside the cycle)

2. **Phase 2 – Find Cycle Entrance (Duplicate Number)**

   * Reinitialize `slow = 0`
   * Move both `slow` and `fast` one step at a time until `slow == fast`
   * The meeting point is the **duplicate number**

---

### 🔄 Mathematical Mapping:

Let `f(x) = nums[x]`, so the traversal becomes:

```
x → nums[x] → nums[nums[x]] → ...
```

---

### 🧪 Example:

Input: `[2, 3, 1, 3]`
Start: `x = nums[0] = 2` → next: `nums[2] = 1` → next: `nums[1] = 3` → next: `nums[3] = 3` (cycle)

Cycle is formed starting at 3.

---

## ⏱️ Time and Space Complexity:

* **Time**: `O(n)`
* **Space**: `O(1)` (no extra space used)

---

## 🧠 Understanding Cycle Detection via Floyd’s Tortoise and Hare

### 📍 Key Concepts:

* `slow` moves 1 step at a time
* `fast` moves 2 steps at a time
* There's a cycle because the array represents a function mapping `nums[i] → nums[nums[i]]`
* A duplicate causes a cycle

---

### 🌀 Cycle Setup:

From the diagram:

* **F**: Distance from start to cycle entry
* **a**: Distance from entry to meeting point
* **C**: Total cycle length

**slow** moves:

```
d_slow = F + a
```

**fast** moves:

```
d_fast = F + C + a (at least one full loop)
```

Since `fast` moves twice as fast:

```
d_fast = 2 × d_slow
```

---

### 🔢 Deriving the Equation:

Equating both expressions:

```
F + C + a = 2(F + a)
```

Simplify:

```
F + C + a = 2F + 2a
C = F + a
```

So, to get from **meeting point back to entry point**:

```
F = C - a
```

Which means:

* Start one pointer from start (`F`)
* One from meeting point (`C - a`)
* Both move 1 step at a time
* They meet at cycle **entry point** (duplicate)

---

### 🧾 Note on Multiple Laps:

If `F` is longer than one loop:

* Let `n` be number of cycles fast completes
* `fast = F + nC + a`
* Still simplifies to:

```
F = nC - a → F = C - a (modulo cycle length)
```

So the property holds **regardless of laps**.

---

### ✅ Summary:

To find duplicate:

1. Detect cycle with fast & slow
2. Reset one pointer to start
3. Move both at 1 step until they meet
4. Meeting point is **duplicate**

---

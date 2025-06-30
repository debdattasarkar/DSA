
---

## 🔁 Circular Array Loop

### Statement

Given a circular list of non-zero integers `nums`, each number tells how many steps to move forward or backward.

* If `nums[i] > 0`, move `nums[i]` steps **forward**
* If `nums[i] < 0`, move `abs(nums[i])` steps **backward**

### Circular movement rules:

* Forward from last → wraps to first
* Backward from first → wraps to last

### A cycle must:

1. Be formed by moving per rules and revisiting indices
2. Only contain elements with the **same sign**
3. Be longer than 1 (no single-element cycles)

Return `True` if a valid cycle exists, else `False`.

---

### Constraints

* $1 \leq \text{nums.length} \leq 10^4$
* $-5000 \leq \text{nums[i]} \leq 5000$
* `nums[i] ≠ 0`

---

### ✅ Example

For `nums = [2, -1, 1, 2, 2]`, output is `True`:

* Case 1: Start from index `0 → 2 → 3 → 0` (valid forward cycle)
* Case 2 & 3: Similar check from other indices confirms at least one valid cycle

---

### 🔍 Step-by-step plan ("Figure it out")

1. Start scanning each index as a possible start of a cycle
2. For each index:

   * Use two pointers: slow (1 step), fast (2 steps)
   * Move in the same direction (all pos or all neg)
   * If a direction changes → invalid
   * If slow == fast again → valid loop of > 1 → return `True`
3. If no valid cycle found → return `False`

---

Here’s the correct logical sequence to detect a **circular array loop** using fast and slow pointers:

---

### ✅ Correct Order of Steps:

1. **Start iterating through the array**, considering each element a potential starting position.

2. **Initialize two pointers at the current position during each iteration**:
   A slow pointer (one step at a time) and a fast pointer (two steps at a time).

3. **Move each pointer forward or backward** according to the number at its current position.

4. **Stop exploring** from the current index if:

   * The direction changes (mixed signs),
   * Or the pointer forms a **single-element loop** (returns to the same position).

5. **If the slow and fast pointers meet** at the same position, a **valid loop is detected** — immediately return `TRUE`.

6. **If no valid loop is found** after checking all positions, return `FALSE`.

---

## 🔁 Circular Array Loop – Optimized Approach

### 🧠 Problem Summary

We’re given a **circular list** of non-zero integers `nums`. Each number tells you how many steps to move forward/backward. A valid loop must:

1. Repeat indices (i.e., form a cycle).
2. Contain elements with the **same direction** (all positive or all negative).
3. Be longer than 1 element.

### ✅ Return:

* `True` if such a valid cycle exists.
* `False` otherwise.

---

## 🐢🐇 Optimized Approach: Fast and Slow Pointers

### 🚀 Key Idea:

Use **two pointers** (`slow` and `fast`) to detect cycles. A valid cycle must not:

* Include a single-element loop.
* Mix directions (positive/negative).

---

### 🔄 Workflow:

For each element in `nums`, repeat the following:

#### Step 1:

Initialize:

```python
slow = i
fast = i
```

#### Step 2:

Move pointers:

```python
slow = get_next_index(nums, slow)
fast = get_next_index(nums, get_next_index(nums, fast))
```

* `get_next_index(nums, idx)` moves to the next valid index circularly using:

  ```python
  (idx + nums[idx]) % len(nums)
  ```

#### Step 3:

**Cycle Validity Check**:

* If `slow == fast`, check:

  1. `slow` doesn’t point to itself (single-element loop check).
  2. Movement is in the **same direction**.

#### Step 4:

If invalid, mark visited elements as `0` to skip them in future iterations.

---

## 🧠 Cycle Validity Conditions:

| Condition                    | Valid?    |
| ---------------------------- | --------- |
| Mixed signs in loop          | ❌ Invalid |
| Cycle length = 1 (self-loop) | ❌ Invalid |
| Same sign, >1 length         | ✅ Valid   |

---


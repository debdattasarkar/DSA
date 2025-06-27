
---

## ✅ Problem: Count Pairs Whose Sum is Less Than Target

You are given:

* An array `nums[]` of integers.
* A value `target`.

You must count all **distinct pairs** `(i, j)` where `i < j` and:

```
nums[i] + nums[j] < target
```

---

## 🔍 Key Insights

### Brute-force (O(n²)):

* Check every pair `(i, j)` with nested loops.

### Optimized Two-Pointer Approach (O(n log n)):


### ✅ Final Step-by-Step Sequence:

1. **Sort the array**, `nums`, in an ascending order.
2. **Initialize two pointers**: `low` at the start of the array and `high` at the end.
3. **If the sum at `low` and `high` is less than target**, count all pairs between `low` and `high`, and move the `low` pointer forward.
4. **Else**, if the sum is greater than or equal to the target, move the `high` pointer backward.
5. **Continue until `low < high`** and return the total count of valid pairs.

---

## 🧠 Dry Run Example

```text
nums = [1, 2, 3, 4, 5], target = 6

Sorted: [1, 2, 3, 4, 5]

Pairs:
(1,2), (1,3), (1,4), (2,3)

Answer = 4
```

---

## 📈 Complexity

* **Time:** O(n log n) due to sorting.
* **Space:** O(1) if sorting in-place, else O(n) with extra copy.

---

The final image you've shared summarizes the **correct solution and code implementation** for the problem **"Count Pairs Whose Sum is Less than Target"**. Here's a complete README-style recap with explanation, dry run, code, and complexity:

---

# ✅ Problem: Count Pairs Whose Sum is Less than Target

## Statement

Given a 0-indexed integer array `nums` of length `n`, and an integer `target`, return the **number of distinct index pairs `(i, j)`** such that:

* `0 ≤ i < j < n`
* `nums[i] + nums[j] < target`

---

## 🔍 Approach: Two Pointer Technique

### Steps:

1. **Sort** the array to enable ordered traversal.
2. **Initialize** two pointers:

   * `low` at the beginning (`0`)
   * `high` at the end (`n - 1`)
3. **While `low < high`**:

   * If `nums[low] + nums[high] < target`, then:

     * All pairs `(low, low+1), ..., (low, high)` are valid.
     * Add `high - low` to count.
     * Move `low` forward.
   * Else, move `high` backward to reduce the sum.

---

## 🧠 Dry Run:

```python
nums = [1, 2, 3, 4, 5]
target = 6

Sorted: [1, 2, 3, 4, 5]
low = 0, high = 4

1 + 5 = 6 >= 6 → move high--
1 + 4 = 5 < 6 → count += 4 - 0 = 4, low++
2 + 4 = 6 >= 6 → high--
2 + 3 = 5 < 6 → count += 3 - 1 = 2, low++
3 + 3 = 6 >= 6 → high--

Done. Total = 6 valid pairs
```

---

## ⏱️ Time Complexity

* **Sorting**: `O(n log n)`
* **Two-pointer traversal**: `O(n)`
* **Total**: `O(n log n)`

## 📦 Space Complexity

* `O(1)` extra space (just pointers and counter)

---

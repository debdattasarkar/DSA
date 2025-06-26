
---

## ❓ Main Question: 3Sum

**Problem Statement**
Given an integer array `nums`, return **all unique triplets** `(nums[i], nums[j], nums[k])` such that:

```
i ≠ j, i ≠ k, j ≠ k  
AND  
nums[i] + nums[j] + nums[k] == 0
```

> 🔹 The **order of triplets** in the output **does not matter**.
> 🔹 Each triplet must be **unique**.

---

## 📌 Constraints

* `3 ≤ nums.length ≤ 500`
* `-10⁵ ≤ nums[i] ≤ 10⁵`

---

## 🧠 Key Pointers to Remember for Interviews

### 1. **Sort the Array First**

Sorting helps to:

* Easily skip duplicates.
* Use the two-pointer technique efficiently.

### 2. **Iterate with a Fixed Pointer**

* Loop through `i` from `0` to `n-2`.
* Skip duplicates at the `i-th` position to avoid redundant triplets.

### 3. **Two-Pointer Technique Inside the Loop**

* Use `left = i + 1`, `right = n - 1`.
* Check the sum: `nums[i] + nums[left] + nums[right]`.

#### Based on the sum:

* If **sum < 0** → Move `left` forward.
* If **sum > 0** → Move `right` backward.
* If **sum == 0** → Add to result and skip duplicates on both sides.

### 4. **Avoid Duplicate Triplets**

* Skip same elements at:

  * `i` (main loop)
  * `left` and `right` (after finding a valid triplet)

### 5. **Time Complexity**

* **O(n²)** overall:

  * `O(n)` for main loop × `O(n)` for two-pointer search
* Sorting is `O(n log n)` but dominated by the main loop.

### 6. **Space Complexity**

* **O(1)** (if output list doesn't count), else depends on number of triplets returned.

---

## ✅ Example

**Input**: `[-2, 0, 2, -2, 1, -1]`
**Output**: `[[-2, 0, 2], [-1, 0, 1]]`

Only **unique triplets** included, even if permutations of same values exist.

---

Here are the **interview pointers to remember** from the solution page for the **3Sum problem**:

---

## ✅ Key Pointers to Remember – 3Sum (Two Pointers Approach)

### 🔹 Problem Summary

> Find all **unique triplets** `(i, j, k)` in the array such that:
> `nums[i] + nums[j] + nums[k] == 0` and `i ≠ j ≠ k`.

---

### 📌 Must-Remember Concepts

#### 1. **Sort the Array First**

* Required to use the **two-pointer technique**.
* Helps in **skipping duplicates efficiently**.

#### 2. **Avoid Duplicates at Each Step**

* **At `i`**: Skip if `nums[i] == nums[i - 1]` to prevent repeating triplets.
* **At `low` and `high`** pointers: After a valid triplet is found, skip duplicate numbers on both ends.

#### 3. **Two-Pointer Search**

For each index `i`:

* Set `low = i + 1`, `high = n - 1`
* Calculate `total = nums[i] + nums[low] + nums[high]`

  * If `total == 0`: Store triplet, move both pointers, skip duplicates.
  * If `total < 0`: Move `low++`
  * If `total > 0`: Move `high--`

---

### 🧠 Tips from the Explanation

* If `nums[i] > 0`, you can **break early** — no triplet can sum to 0 since the array is sorted.
* Use a result list to collect **only unique** triplets.
* Carefully update pointers and use `while` to skip repeated values.

---

### ⏱️ Time and Space Complexity

* **Time Complexity**:
  `O(n²)` overall

  * Sorting: `O(n log n)`
  * Main loop + two-pointer scan: `O(n²)`

* **Space Complexity**:
  `O(1)` (not counting result list) — only uses fixed pointers and loop counters.

---

### ✅ Example Trace (from image)

Input: `[-4, -1, -1, 0, 1, 2]`
Output: `[[-1, -1, 2], [-1, 0, 1]]`

Shows how duplicates are skipped and how sorted traversal helps maintain efficiency.

---

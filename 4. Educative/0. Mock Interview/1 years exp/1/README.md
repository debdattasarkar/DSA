
---

### 🧩 Problem Statement

You are given:

* A **0-indexed array** `nums` of integers.
* An integer `target`.

Your task is to count **distinct pairs of indices** `(i, j)` such that:

* $0 \leq i < j < n$
* $\text{nums}[i] + \text{nums}[j] < \text{target}$

---

### 🧷 Constraints:

* $1 \leq n \leq 50$
* $-50 \leq \text{nums}[i], \text{target} \leq 50$

---

### 🧪 Example

**Input:**
`nums = [1, 3, 4, 2]`, `target = 7`
**Output:** `4`
**Explanation:** Valid pairs are:

* (1,3) → 1+2 = 3
* (1,4) → 1+4 = 5
* (1,2) → 1+3 = 4
* (3,2) → 2+3 = 5
  All are < 7.

---

### ✅ Python Code

```python
def count_pairs(nums, target):
    count = 0
    n = len(nums)
    
    # Iterate over all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                count += 1
                
    return count

# Example usage
nums = [1, 3, 4, 2]
target = 7
print(count_pairs(nums, target))  # Output: 4
```

---

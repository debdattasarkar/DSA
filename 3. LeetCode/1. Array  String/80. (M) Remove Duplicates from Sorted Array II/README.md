
---

# 🔁 Remove Duplicates from Sorted Array II (Leetcode #80)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Two Pointers`

---

## 📘 Problem Statement

Given a **sorted** integer array `nums`, remove some duplicates **in-place** so that each unique element appears **at most twice**.
The **relative order** of elements must be preserved.

Return the number `k` — the length of the modified array. The first `k` elements should contain the allowed elements.
Do **not** allocate extra space; the modification must happen **in-place** using **O(1)** extra memory.

---

## 🔒 Constraints

* `1 <= nums.length <= 30,000`
* `-10⁴ <= nums[i] <= 10⁴`
* `nums` is sorted in **non-decreasing** order

---

## 🧠 Approach – Two Pointers

Use a pointer `i` to track where the next valid element should go, and a pointer `j` to iterate through `nums`.

Since a number can appear **at most twice**, we allow:

* All elements until the **first two** to be added directly.
* From the third onward, only add `nums[j]` if `nums[j] != nums[i - 2]`.

---

## 📊 Dry Run Example

**Input:**
`nums = [1,1,1,2,2,3]`

### Step-by-step:

| j | nums\[j] | i | Check Condition (`nums[j] != nums[i-2]`) | Action       | nums (in-place after action) |
| - | -------- | - | ---------------------------------------- | ------------ | ---------------------------- |
| 0 | 1        | 0 | First two elements → always keep         | nums\[0] = 1 | \[1, \_, \_, \_, \_, \_]     |
| 1 | 1        | 1 | First two elements → always keep         | nums\[1] = 1 | \[1, 1, \_, \_, \_, \_]      |
| 2 | 1        | 2 | 1 == nums\[i-2] → skip                   | -            | \[1, 1, \_, \_, \_, \_]      |
| 3 | 2        | 2 | 2 != nums\[i-2] (2 ≠ 1) → keep           | nums\[2] = 2 | \[1, 1, 2, \_, \_, \_]       |
| 4 | 2        | 3 | 2 != nums\[i-2] (2 ≠ 1) → keep           | nums\[3] = 2 | \[1, 1, 2, 2, \_, \_]        |
| 5 | 3        | 4 | 3 != nums\[i-2] (3 ≠ 2) → keep           | nums\[4] = 3 | \[1, 1, 2, 2, 3, \_]         |

✅ Result:
`k = 5`, `nums = [1, 1, 2, 2, 3, _]`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # Already satisfies the condition
        
        i = 2  # Start placing from index 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:  # Check last two entries
                nums[i] = nums[j]
                i += 1
        return i  # Length of valid elements
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();

        int i = 2; // First two elements are always valid
        for (int j = 2; j < nums.size(); ++j) {
            if (nums[j] != nums[i - 2]) {
                nums[i] = nums[j]; // Copy valid element
                i++;
            }
        }
        return i; // Return the new length
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length <= 2) return nums.length;

    let i = 2; // Pointer for placement
    for (let j = 2; j < nums.length; j++) {
        if (nums[j] !== nums[i - 2]) {
            nums[i] = nums[j]; // Keep valid element
            i++;
        }
    }
    return i; // Length of unique elements (max 2 repeats)
};
```

---

## ✅ Summary

| Metric           | Value           |
| ---------------- | --------------- |
| Time Complexity  | O(n)            |
| Space Complexity | O(1) (in-place) |
| Technique        | Two Pointers    |

---

Let me know if you want a version for "at most **k** duplicates" or test generation!


Yes! The version you just posted is also **correct and elegant**. Here's a breakdown and comparison to the standard solution:

---

## ✅ Your Code

```python
def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if j == 1 or nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j
```

---

## 🔍 Dry Run on Example

Input: `[1, 1, 1, 2, 2, 3]`

| i | nums\[i] | j | Condition         | Action       | Resulting nums          |
| - | -------- | - | ----------------- | ------------ | ----------------------- |
| 1 | 1        | 1 | j == 1 → ✅        | nums\[1] = 1 | \[1, 1, \_, \_, \_, \_] |
| 2 | 1        | 2 | 1 == nums\[0] → ❌ | skip         | \[1, 1, \_, \_, \_, \_] |
| 3 | 2        | 2 | 2 != nums\[0] → ✅ | nums\[2] = 2 | \[1, 1, 2, \_, \_, \_]  |
| 4 | 2        | 3 | 2 != nums\[1] → ✅ | nums\[3] = 2 | \[1, 1, 2, 2, \_, \_]   |
| 5 | 3        | 4 | 3 != nums\[2] → ✅ | nums\[4] = 3 | \[1, 1, 2, 2, 3, \_]    |

Returns `j = 5`

---

## ✅ Is It Correct?

Yes. The logic is clean:

* It handles the first 2 elements safely (`j == 1`)
* It compares the new value to `nums[j - 2]` to ensure **at most 2 copies**

---

## 🆚 Comparison to Canonical Version

| Aspect         | Canonical `i = 2` Version            | Your `j = 1` Version          |
| -------------- | ------------------------------------ | ----------------------------- |
| Initialization | Starts writing at `i = 2`            | Starts `j = 1`, writes at `j` |
| Clarity        | Slightly clearer separation of roles | Slightly more compact         |
| Performance    | Same `O(n)` and `O(1)`               | Same `O(n)` and `O(1)`        |
| Readability    | Both are readable                    | Yours is more compact         |

---

## ✅ Final Thoughts

Your version is:

* ✔️ Compact
* ✔️ Elegant
* ✔️ Correct
* ✔️ Just as efficient as the traditional two-pointer method

No improvements needed unless you want to make it more readable for beginners (e.g., by renaming `j` to `write` or `pos`).

Let me know if you'd like to generalize this to **"at most k duplicates"** — that's a great follow-up!

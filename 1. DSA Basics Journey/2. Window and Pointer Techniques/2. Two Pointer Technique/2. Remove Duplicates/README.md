Let’s explore **Leetcode 26 – Remove Duplicates from Sorted Array**, a classic **Two Pointer** problem.

---

## 🔍 Problem Statement

> Given a **sorted array `nums`**, remove the duplicates **in-place** such that each element appears **only once** and return the new length.
>
> Do **not** allocate extra space — modify the input array in-place.

---

### 🧪 Example

```python
Input: nums = [1, 1, 2]  
Output: 2, nums = [1, 2, _]
```

---

## ✅ Key Observations

* The array is **sorted**, so **duplicates are adjacent**
* We use a **slow pointer** (`i`) to mark the position of the last unique element
* A **fast pointer** (`j`) scans the array and copies new unique elements

---

## 🧑‍💻 Python Code (Two Pointer Approach)

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Slow pointer to mark position of last unique element
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Overwrite next unique position

        return i + 1  # Length is index + 1
```

---

## 🧠 Dry Run

Input:

```python
nums = [1, 1, 2, 2, 3]
```

| Step | i (slow) | j (fast) | nums         | Comment                                   |
| ---- | -------- | -------- | ------------ | ----------------------------------------- |
| Init | 0        | 1        | \[1,1,2,2,3] | nums\[1] == nums\[0] → skip               |
| 2    | 0        | 2        | \[1,1,2,2,3] | nums\[2] ≠ nums\[0] → write 2 to nums\[1] |
|      | 1        |          | \[1,2,2,2,3] |                                           |
| 3    | 1        | 3        | \[1,2,2,2,3] | nums\[3] == nums\[1] → skip               |
| 4    | 1        | 4        | \[1,2,2,2,3] | nums\[4] ≠ nums\[1] → write 3 to nums\[2] |
|      | 2        |          | \[1,2,3,2,3] |                                           |

✅ Return `3`, and first 3 elements are `[1,2,3]`.

---

## ⏱ Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## ❓ Interview Questions & Variations

| Question                                        | Answer                                      |
| ----------------------------------------------- | ------------------------------------------- |
| Can you use extra space?                        | No — in-place only                          |
| What happens to elements beyond the new length? | Irrelevant; not checked                     |
| Can it be done for unsorted arrays?             | Not this way — would require hashing or set |
| What's the return type?                         | Integer: the new length of unique prefix    |

---


## 🧪 Real-World Use Cases

* **Deduplicating sorted logs** before further processing
* Compressing sorted arrays before transmission
* In-memory optimization of sorted datasets (e.g., time series)

---

Here’s the **text explanation**, **dry run**, and **solutions** in Python, C++, and JavaScript for **Leetcode 88: Merge Sorted Array**.

---

## 📝 Problem Summary

You are given two **sorted arrays**:

* `nums1` of size `m + n`, where the first `m` elements are valid and the last `n` are placeholders (`0`).
* `nums2` of size `n`.

**Task:** Merge `nums2` into `nums1` in-place to get one **sorted array** of size `m + n`.

---

## ✅ Approach

Use **three pointers** starting from the **end** of the arrays:

* `p1 = m - 1`: last valid index in `nums1`
* `p2 = n - 1`: last index in `nums2`
* `p = m + n - 1`: last index in merged `nums1`

Compare elements from the end and **place the larger one** at position `p`, moving backward.

---

## 🧮 Dry Run

**Input:**

```
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
```

**Step-by-step:**

| p1 | p2 | p | nums1                |
| -- | -- | - | -------------------- |
| 2  | 2  | 5 | \[1,2,3,0,0,6] ← 6>3 |
| 2  | 1  | 4 | \[1,2,3,0,5,6] ← 5>3 |
| 2  | 0  | 3 | \[1,2,3,3,5,6] ← 3=2 |
| 1  | 0  | 2 | \[1,2,2,3,5,6] ← 2=2 |
| 0  | -1 | 1 | Done                 |

**Output:**

```
[1,2,2,3,5,6]
```

---

## ✅ Python Code

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 has leftover elements
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
```

---

## ✅ C++ Code

```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1, p2 = n - 1, p = m + n - 1;

        while (p1 >= 0 && p2 >= 0) {
            nums1[p--] = (nums1[p1] > nums2[p2]) ? nums1[p1--] : nums2[p2--];
        }

        while (p2 >= 0) {
            nums1[p--] = nums2[p2--];
        }
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    merge(nums1, m, nums2, n) {
        let p1 = m - 1, p2 = n - 1, p = m + n - 1;

        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }

        while (p2 >= 0) {
            nums1[p--] = nums2[p2--];
        }
    }
}
```

---

Here is the **completed version** of your `merge` method with in-place modification of `nums1`:

---

### ✅ Full Python Code with Comments:

```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place so that nums1 becomes a sorted array.
        """
        # Set up three pointers:
        # p1: end of nums1's valid part
        # p2: end of nums2
        # p: last position of nums1 (where merge result goes)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge in reverse order to avoid overwriting nums1 elements
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If any elements remain in nums2, copy them (nums1's left part is already sorted)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
```

---

### 🧠 Why it works:

* Since `nums1` has space at the end (`m + n` size), we use the **end of the array** to place merged values.
* We **merge from the back**, preventing any overwrite of original values.

---

### ✅ Example Dry Run

**Input:**

```python
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
```

**Output:**

```python
nums1 = [1,2,2,3,5,6]
```


Yes, you **can** use the built-in `sort()` function — especially if the problem **does not restrict** you from doing so (check for constraints like “must do in-place without sort”).

### ✅ Using `sort()` — Simplified Solution:

This is **not optimal** in time complexity, but it's acceptable for small inputs and passes in interviews or quick prototypes:

```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Replace the last n zeros in nums1 with elements of nums2
        nums1[m:] = nums2
        
        # Sort the entire nums1 in-place
        nums1.sort()
```

### 🔍 Time Complexity:

* `nums1.sort()` → **O((m + n) log(m + n))**
* In contrast, the **two-pointer method** is **O(m + n)** — faster for large inputs.

---

### 🚫 When **not** to use `sort()`:

* If the question explicitly says “**do not use sort()**”
* If asked to achieve **better than O(n log n)** performance
* If working in **real-time systems** or **performance-critical** code

---

To solve the **"Merge Sorted Array"** problem using a **heap**, you can combine both arrays and use a min-heap to maintain sorted order. This is more educational than efficient (since the two-pointer method is faster), but it's a good exercise.

---

### ✅ Python Code Using `heapq` (Min-Heap)

```python
import heapq
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums1 and nums2 using a heap. Modify nums1 in-place.
        """
        # Take only the first m valid elements from nums1
        heap = nums1[:m] + nums2[:n]  # Combine valid parts
        
        heapq.heapify(heap)  # Build a min-heap from combined list
        
        # Replace nums1's contents in sorted order
        for i in range(m + n):
            nums1[i] = heapq.heappop(heap)
```

---

### 🧠 How it works:

* Takes `nums1[:m]` (valid part of `nums1`) and `nums2`
* Builds a **min-heap** (`heapify`) in O(m + n)
* Pops smallest values from heap and writes back into `nums1`

---

### ⏱️ Time Complexity:

* `heapify()` → **O(m + n)**
* Each of `m + n` `heappop()` calls → **O(log(m + n))**
* **Total**: `O((m + n) log(m + n))`
  (slower than two-pointer which is O(m + n), but still valid)

---

### ❗In-place caveat:

Technically, this uses extra space for the heap, so **it's not truly in-place** like the two-pointer solution. But still acceptable in interviews if the question doesn’t strictly enforce space limits.

---

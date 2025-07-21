Let’s break down **LeetCode 704: Binary Search** step-by-step.

---

## 🧩 Problem Statement (Easy)

> Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, return the index if the target is found. If not, return `-1`.

* Must solve in **O(log n)** time → Use **Binary Search**

---

## 🔍 Binary Search Strategy

We initialize two pointers:

* `left = 0`, `right = len(nums) - 1`
* While `left <= right`:

  * Compute mid: `mid = (left + right) // 2`
  * If `nums[mid] == target`: return `mid`
  * If `target < nums[mid]`: search left (`right = mid - 1`)
  * Else: search right (`left = mid + 1`)

---

## 🧠 Dry Run Example

```text
nums = [-10, -3, 0, 5, 9, 12], target = 9

left = 0, right = 5
mid = (0+5)//2 = 2 → nums[2] = 0 → 9 > 0 → left = 3

left = 3, right = 5
mid = (3+5)//2 = 4 → nums[4] = 9 → match → return 4
```

---

## ✅ Code Template

### Python

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
```


---

## 🕐 Time & Space Complexity

* **Time:** `O(log n)` — classic binary search.
* **Space:** `O(1)` — iterative version uses constant space.

---

---

Absolutely! Let's go deep into the **optimal iterative binary search solution in Python** for **LeetCode 704: Binary Search**.

---

## ✅ Optimal Solution (Iterative Binary Search)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
```

---

## 🧠 How It Works (Step-by-Step Logic)

1. Start with the full search space: `left = 0`, `right = len(nums) - 1`.
2. Find the midpoint: `mid = (left + right) // 2`.
3. Compare `nums[mid]` with `target`:

   * If equal → **return mid** (target found).
   * If target is smaller → search **left half** (`right = mid - 1`).
   * If target is larger → search **right half** (`left = mid + 1`).
4. If the loop ends, target is not in array → **return -1**.

---

## 🔍 Dry Run

```python
nums = [-10, -3, 0, 5, 9, 12]
target = 9

left = 0, right = 5
mid = 2 → nums[2] = 0 → 9 > 0 → search right → left = 3

mid = 4 → nums[4] = 9 → match → return 4
```

---

## 🕐 Time and Space Complexity

* **Time:** `O(log n)` – divide the search space in half each iteration.
* **Space:** `O(1)` – iterative method uses constant space.

---

## 🧪 Sample Test Cases

```python
assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
assert Solution().search([1], 1) == 0
assert Solution().search([1], 0) == -1
```

---

## 🔁 Common Interview Folleft-ups

* How to return the **index of first or last occurrence** if duplicates exist?
* How to adapt this for **floating point numbers** or **rotated sorted arrays**?
* Can you implement the same using **recursion**?

---

---

# 🌍 Real-World Use Cases

Here are the **top real-world use cases** of **Binary Search** — fundamental and widely used in high-performance systems:

---

### ✅ 1. **Databases and Indexing**

* Used to quickly **search sorted data**, like B-trees, indexes, or binary logs.
* Enables **O(log n)** time for key retrieval in massive datasets.

---

### ✅ 2. **Memory Management & OS Kernels**

* Binary search is used in **virtual memory allocation**, **page table lookups**, and **address range searches**.

---

### ✅ 3. **Search Engines & Autocomplete**

* Efficient lookup in **sorted dictionaries**, prefix tries, or ranking systems.

---

### ✅ 4. **Compiler Optimization & Numerical Methods**

* Used in **function approximation**, **root finding**, and **interval narrowing** (e.g., sqrt, log, etc.).

---

These are core use cases where binary search powers **critical lookup, optimization, and decision-making** in modern systems.



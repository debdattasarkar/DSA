The **Two Pointer Technique** is a powerful and versatile algorithmic pattern widely used in DSA problems. It uses **two indices (pointers)** that move through a data structure (typically arrays or strings) to reduce time complexity — often from `O(n²)` to `O(n)` or `O(n log n)`.

---

## 🧠 Concept

> Use **two pointers**, typically named `left` and `right`, to scan the array or string in a strategic way (from start & end, or both from start, etc.)

---

## 🔧 Common Patterns

| Pattern                       | Usage Example                          | Pointer Movement                                |
| ----------------------------- | -------------------------------------- | ----------------------------------------------- |
| Opposite Direction            | Sorted array: find pair with given sum | Start from both ends, move inward               |
| Same Direction (Sliding)      | Longest substring, prefix matching     | Both start at beginning, move right             |
| Window Expansion/Shrinking    | Variable Sliding Window                | Expand right, shrink left                       |
| Nested Increment (Merge sort) | Merge two sorted arrays/lists          | Both pointers start at 0, advance on conditions |

---

## 🔍 Classic Use Cases

| Problem Type                  | Example                                                                     | Two Pointers Usage                           |
| ----------------------------- | --------------------------------------------------------------------------- | -------------------------------------------- |
| **Pair Sum in Sorted Array**  | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)   | `left`, `right` from both ends               |
| **Remove Duplicates**         | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | One slow, one fast                           |
| **Reverse String or Array**   | [LC 344](https://leetcode.com/problems/reverse-string/)                     | `left` and `right` swap until they meet      |
| **Container With Most Water** | [LC 11](https://leetcode.com/problems/container-with-most-water/)           | Max area by comparing ends                   |
| **Trapping Rainwater**        | [LC 42](https://leetcode.com/problems/trapping-rain-water/)                 | Left max/right max tracking                  |
| **Palindrome Check**          | Is string a palindrome?                                                     | `left` and `right` comparing chars           |
| **Merge Sorted Arrays**       | [LC 88](https://leetcode.com/problems/merge-sorted-array/)                  | Compare and place using two pointers         |
| **3Sum / 4Sum**               | [LC 15, 18](https://leetcode.com/problems/3sum/)                            | Sort array, fix one number, use two pointers |

---

## 🧑‍💻 Example Code: Two Sum in Sorted Array

```python
def two_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]  # Not found
```

### ⏱ Time Complexity: `O(n)`

### 🧠 Space: `O(1)`

---

## 🎯 When to Use Two Pointers?

Use when:

* The array is **sorted** (or can be sorted)
* You're **merging, matching, or comparing** from two ends
* You want to find **minimum/maximum condition** in a range
* You're trying to **maintain a window or segment** dynamically

---

## 🧩 Real-Life Applications

* Comparing **two time series logs** (merging events)
* Streaming **real-time data** and matching against a range
* Managing **interval overlaps** (e.g. meeting rooms)
* Finding optimal pairs (e.g. **price pairs ≤ budget**)

---

## 🔗 Related Techniques

| Technique          | When Used                              |
| ------------------ | -------------------------------------- |
| Sliding Window     | When window size is fixed or variable  |
| Fast/Slow Pointers | Detect loops (e.g. linked list cycle)  |
| Binary Search      | On index or condition with sorted data |

---


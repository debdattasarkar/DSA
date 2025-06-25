
---

# 🧮 At Least Two Greater Elements

**Difficulty:** Basic
**Accuracy:** 58.49%
**Submissions:** 59K+
**Points:** 1

---

## 📝 Problem Statement

Given an array `arr[]` of **distinct elements**, the task is to return an array of **all elements except the two greatest elements** in **sorted order**.

---

## 📚 Examples

### Example 1:

**Input:**
`arr[] = [2, 8, 7, 1, 5]`
**Output:**
`[1, 2, 5]`
**Explanation:**
We return an array that contains `1`, `2`, and `5`, and we exclude the two greatest elements `7` and `8`.

---

### Example 2:

**Input:**
`arr[] = [7, -2, 3, 4, 9, -1]`
**Output:**
`[-2, -1, 3, 4]`
**Explanation:**
We return an array that contains `-2`, `-1`, `3`, and `4`, and we exclude the two greatest elements `7` and `9`.

---

## ⏱ Expected Time Complexity

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)`

---

## 🔒 Constraints

* `3 ≤ arr.size() ≤ 10⁵`
* `-10⁶ ≤ arr[i] ≤ 10⁶`

---

## 🏷 Company Tags

* Amazon

---

## 🏷 Topic Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Program To Find Largest Element In An Array](#)

---
Sure! Let's break it down as requested:

---

## ✅ 1. Text Explanation & Step-by-Step Dry Run

### **Problem Summary**

You are given an array `arr[]` of **distinct integers**. You need to return a **sorted list** of all elements **except the two greatest elements**.

---

### **Approach**

1. **Find the two largest elements**.
2. **Exclude** them from the array.
3. **Sort** the remaining elements and return them.

---

### 🔍 **Dry Run**

#### Input:

```
arr = [2, 8, 7, 1, 5]
```

#### Steps:

* Step 1: Sort the array → `[1, 2, 5, 7, 8]`
* Step 2: Remove last 2 elements → `[1, 2, 5]`
* Step 3: Return this list → Output: `[1, 2, 5]`

---

## ✅ 2. Code Implementations with Inline Comments

---

### ✅ Python Code

```python
class Solution:
    def findElements(self, arr):
        # Sort the array in ascending order
        arr.sort()
        
        # Remove the last two elements (the largest two)
        result = arr[:-2]
        
        return result
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    vector<int> findElements(vector<int> arr) {
        // Step 1: Sort the array
        sort(arr.begin(), arr.end());

        // Step 2: Remove last two elements (exclude two greatest)
        arr.resize(arr.size() - 2);

        return arr;
    }
};
```

---

### ✅ JavaScript Code

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
class Solution {
    findElements(arr) {
        // Step 1: Sort the array
        arr.sort((a, b) => a - b);

        // Step 2: Remove last two elements
        return arr.slice(0, arr.length - 2);
    }
}
```

---

## ✅ 3. Interview Questions & Sample Answers

---

### ❓Q1. What is the time complexity of your solution?

**🅰️:** Sorting takes `O(n log n)`, and slicing/removal is `O(n)` in worst case, so total time complexity is `O(n log n)`.

---

### ❓Q2. Can this be done without sorting?

**🅰️:** Yes, we can use a **two-pass scan** to find the top two largest elements in `O(n)`, then do a filter to remove them. But if output needs to be **sorted**, we still need sorting → `O(n log n)`.

---

### ❓Q3. Can you do it in-place?

**🅰️:** Not if we need to **return a new sorted array**. But we can do it in-place before copying to result using `partition` methods if allowed.

---

### ❓Q4. Will this code work if there are **duplicates** in the array?

**🅰️:** No, the problem specifies **distinct** elements. If duplicates were allowed, we’d need to carefully handle counts or use a multiset.

---

Would you like the in-place `O(n)` version as an alternative approach too?

Great! Here's the optimized **O(n)** approach **without sorting**, assuming you do **not need the result in sorted order** (or you can sort at the end if needed).

---

## ✅ Optimized O(n) Approach (Without Sorting)

### 🔍 **Idea**

* First pass: Find the largest and second largest elements.
* Second pass: Collect all elements except those two.

---

### ✅ Python Code

```python
class Solution:
    def findElements(self, arr):
        n = len(arr)
        if n < 3:
            return []  # Less than 3 elements means no valid result

        # Step 1: Find the top two maximum elements
        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        # Step 2: Collect elements except the top two
        result = [num for num in arr if num != first and num != second]
        return result
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    vector<int> findElements(vector<int> arr) {
        int n = arr.size();
        if (n < 3) return {};

        // Step 1: Find largest and second largest
        int first = INT_MIN, second = INT_MIN;
        for (int num : arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second) {
                second = num;
            }
        }

        // Step 2: Collect elements excluding the top two
        vector<int> result;
        for (int num : arr) {
            if (num != first && num != second) {
                result.push_back(num);
            }
        }

        return result;
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    findElements(arr) {
        if (arr.length < 3) return [];

        // Step 1: Find the largest and second largest
        let first = -Infinity, second = -Infinity;
        for (let num of arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second) {
                second = num;
            }
        }

        // Step 2: Filter out top two elements
        return arr.filter(num => num !== first && num !== second);
    }
}
```

---

### 🔁 Optional: Sort the Result

If output must be sorted, you can sort the `result` array at the end:

* Python: `return sorted(result)`
* C++: `sort(result.begin(), result.end());`
* JS: `result.sort((a, b) => a - b);`

---

### ✅ Time & Space Complexity

| Operation           | Time       | Space |
| ------------------- | ---------- | ----- |
| Find top 2 elements | O(n)       | O(1)  |
| Filter elements     | O(n)       | O(n)  |
| (Optional) Sort     | O(n log n) | O(1)  |

👉 If sorting is not needed, overall is **O(n) time and O(n) space**.

---


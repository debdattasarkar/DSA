# Overlapping Intervals  

## Problem Statement

Given an array of Intervals `arr[][]`, where `arr[i] = [startᵢ, endᵢ]`, the task is to merge all of the **overlapping intervals**.

### Example 1:
```
Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: 
Intervals [1,3] and [2,4] overlap and merge into [1,4].
```

### Example 2:
```
Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: 
All intervals overlap with [1,9], so they merge into [1,9].
```

## Constraints
- `1 ≤ arr.size() ≤ 10⁵`
- `0 ≤ startᵢ ≤ endᵢ ≤ 10⁵`

## Expected Complexities
- **Time Complexity:** O(n log n)
- **Auxiliary Space:** O(1)

## Tags

- Arrays
- Hash
- Sorting
- Data Structures
- Algorithms

## Company Tags

- Amazon
- Microsoft
- Google
- Nutanix
- Zoho

## Related Articles

- [Merging Intervals](https://www.geeksforgeeks.org/merging-intervals/)

---

Here’s a complete response for the **Overlapping Intervals** problem based on the GeeksforGeeks prompt.

---

## 📘 Problem: Overlapping Intervals

### Task

Given an array `arr[][]`, where `arr[i] = [startᵢ, endᵢ]`, merge all **overlapping intervals** and return the merged intervals.

---

## 🧠 Explanation

### What is an Overlapping Interval?

Two intervals `[a, b]` and `[c, d]` **overlap** if `c <= b`.

### Approach:

1. **Sort the intervals** by their starting time.
2. Traverse through the sorted list:

   * If the current interval overlaps with the last one in the result, **merge them**.
   * Otherwise, **add it** as a new interval.

---

## 🔍 Dry Run

### Input:

```
arr = [[1,3], [2,4], [6,8], [9,10]]
```

### Step-by-Step:

1. **Sort**: `[[1,3], [2,4], [6,8], [9,10]]`
2. Start with `[1,3]`
3. Compare with `[2,4]` → Overlap → Merge to `[1,4]`
4. Compare with `[6,8]` → No Overlap → Add `[6,8]`
5. Compare with `[9,10]` → No Overlap → Add `[9,10]`

### Output:

```
[[1,4], [6,8], [9,10]]
```

---

## ✅ Time & Space Complexity

* **Time Complexity**: O(n log n) (due to sorting)
* **Auxiliary Space**: O(1) if in-place; O(n) if using extra list

---

## 🐍 Python Code

```python
class Solution:
    def mergeOverlap(self, arr):
        # Sort intervals based on start time
        arr.sort(key=lambda x: x[0])
        
        merged = []
        for interval in arr:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # no overlap
            else:
                # merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    vector<vector<int>> mergeOverlap(vector<vector<int>>& arr) {
        // Sort based on start time
        sort(arr.begin(), arr.end());
        
        vector<vector<int>> merged;
        
        for (auto& interval : arr) {
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);  // no overlap
            } else {
                merged.back()[1] = max(merged.back()[1], interval[1]);  // merge
            }
        }
        
        return merged;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    mergeOverlap(arr) {
        // Sort by start time
        arr.sort((a, b) => a[0] - b[0]);

        const merged = [];

        for (const interval of arr) {
            if (merged.length === 0 || merged[merged.length - 1][1] < interval[0]) {
                merged.push(interval);  // no overlap
            } else {
                merged[merged.length - 1][1] = Math.max(
                    merged[merged.length - 1][1], interval[1]
                );  // merge
            }
        }

        return merged;
    }
}
```

---


---

# 🚉 Minimum Platforms

### 🟡 Difficulty: Medium

**Accuracy:** 26.84%
**Submissions:** 561K+
**Points:** 4
**Average Time:** 30 minutes

---

## 🔍 Problem Statement

You are given the **arrival times `arr[]`** and **departure times `dep[]`** of all trains that arrive at a railway station on the same day.
Your task is to determine the **minimum number of platforms** required at the station to ensure that **no train is kept waiting**.

> At any given time, **the same platform cannot be used** for both the **arrival of one train and the departure of another**.
> So, **when two trains arrive at the same time**, or **when one arrives before another departs**, **additional platforms** are required to accommodate both trains.

---

## 🧪 Examples

### Example 1:

**Input:**
`arr[] = [900, 940, 950, 1100, 1500, 1800]`
`dep[] = [910, 1200, 1120, 1130, 1900, 2000]`
**Output:** `3`
**Explanation:**
There are **3 trains** during the time **9:40 to 12:00**. So, a minimum of **3 platforms** is needed.

---

### Example 2:

**Input:**
`arr[] = [900, 1235, 1100]`
`dep[] = [1000, 1240, 1200]`
**Output:** `1`
**Explanation:**
All train timings are mutually exclusive. So, only **1 platform** is required.

---

### Example 3:

**Input:**
`arr[] = [1000, 935, 1100]`
`dep[] = [1200, 1240, 1130]`
**Output:** `3`
**Explanation:**
All trains have to be there from **11:00 to 11:30** → **3 trains** → need **3 platforms**.

---

## 📌 Constraints

* `1 ≤ number of trains ≤ 50,000`
* `0000 ≤ arr[i], dep[i] ≤ 2359`

> **Note:** Times are in **24-hour format (HHMM)**.

* First two digits: hours (00 to 23)
* Last two digits: minutes (00 to 59)

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## 💼 Company Tags

`Paytm`, `Amazon`, `Microsoft`, `D-E-Shaw`, `Hike`, `Walmart`, `Adobe`, `Google`,
`Boomerang Commerce`, `Zillious`, `Atlassian`

---

## 🧠 Topic Tags

* Arrays
* Greedy
* Sorting
* Binary Search
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Minimum Number Platforms Required Railwaybus Station Set 2 Map Based Approach](https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaystation-set-2/)
* [Minimum Number Platforms Required Railwaybus Station](https://www.geeksforgeeks.org/minimum-number-of-platforms-required-for-a-railway/)

---

## 📘 Step-by-Step Explanation

### 💡 Key Idea:

This is a classical **interval overlap** problem.

We:

1. Sort both `arr[]` and `dep[]` individually.
2. Use two pointers `i` and `j` for arrival and departure arrays.
3. Track:

   * `platforms_needed`: current platforms in use
   * `max_platforms`: max platforms required at any point

At each step:

* If `arr[i] <= dep[j]`:
  Train arrives before previous one departs → Need **new platform**
* Else:
  A train departs → **free one platform**

---

### 🧪 Dry Run:

#### Input:

`arr = [900, 940, 950, 1100, 1500, 1800]`
`dep = [910, 1200, 1120, 1130, 1900, 2000]`
→ Sorted already.

| i (arr)                              | j (dep) | Current Platforms | Explanation                      |
| ------------------------------------ | ------- | ----------------- | -------------------------------- |
| 0                                    | 0       | 1                 | 900 arrives → +1 platform        |
| 1                                    | 0       | 2                 | 940 arrives before 910 departs   |
| 2                                    | 0       | 3                 | 950 arrives before 910 departs   |
| 2                                    | 1       | 2                 | 910 departs → -1 platform        |
| 3                                    | 2       | 3                 | 1100 arrives before 1120 departs |
| ...                                  |         |                   |                                  |
| 👉 **Max platforms at any time = 3** |         |                   |                                  |

---

## ✅ Optimized Code

---

### 🐍 Python

```python
#User function Template for python3

class Solution:    
    def minimumPlatform(self, arr, dep):
        n = len(arr)
        arr.sort()
        dep.sort()

        platform_needed = 0
        max_platforms = 0
        i = j = 0

        # Process all events in sorted order
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            else:
                platform_needed -= 1
                j += 1
            max_platforms = max(max_platforms, platform_needed)

        return max_platforms
```

---

### 💠 C++

```cpp
class Solution {
  public:
    int findPlatform(vector<int>& arr, vector<int>& dep) {
        sort(arr.begin(), arr.end());
        sort(dep.begin(), dep.end());

        int n = arr.size();
        int platform_needed = 0, max_platforms = 0;
        int i = 0, j = 0;

        while (i < n && j < n) {
            if (arr[i] <= dep[j]) {
                platform_needed++;
                i++;
            } else {
                platform_needed--;
                j++;
            }
            max_platforms = max(max_platforms, platform_needed);
        }

        return max_platforms;
    }
};
```

---

### 🌐 JavaScript

```javascript
// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number[]} dep
 * @returns {number}
 */

class Solution {
    findPlatform(arr, dep) {
        arr.sort((a, b) => a - b);
        dep.sort((a, b) => a - b);

        let i = 0, j = 0;
        let platform_needed = 0, max_platforms = 0;
        const n = arr.length;

        while (i < n && j < n) {
            if (arr[i] <= dep[j]) {
                platform_needed++;
                i++;
            } else {
                platform_needed--;
                j++;
            }
            max_platforms = Math.max(max_platforms, platform_needed);
        }

        return max_platforms;
    }
}
```

---

## 💬 Interview Questions & Answers

---

### ❓Q1. Why do we sort both arrival and departure arrays?

**A:** Sorting ensures we process events in chronological order. This helps simulate platform allocation in real time.

---

### ❓Q2. What if a train arrives at the same time another departs?

**A:** Since arrival is `<=` departure, we increment platform (treat arrival first), ensuring no train waits unnecessarily.

---

### ❓Q3. Can we use a priority queue instead?

**A:** Yes. It’s another valid approach (for unsorted dep\[]), but it increases space and time complexity to O(n log n).

---

### ❓Q4. What is the time and space complexity?

* **Time Complexity:** `O(n log n)` (due to sorting)
* **Space Complexity:** `O(1)` (if in-place sorting is used)

---

### ❓Q5. Can we handle more than 24 hours?

**A:** If times go over 2359, you’d need to normalize or use minutes since midnight, but constraints here keep it within 24-hour format.

---

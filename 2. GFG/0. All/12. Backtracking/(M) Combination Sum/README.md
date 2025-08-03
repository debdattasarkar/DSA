
# 🧮 Combination Sum

---

## 📝 Problem Statement

Given an array `arr[]` and a `target`, your task is to **find all unique combinations** in the array where the sum is equal to the `target`.
You may reuse the same number from the array **any number of times**.

You can return the answer in **any order**.

---

## 📌 Example

### Example 1

```text
Input: arr[] = [2, 4, 6, 8], target = 8  
Output: [[2, 2, 2, 2], [2, 2, 4], [2, 6], [4, 4], [8]]
Explanation: Total number of possible combinations are 5.
```

### Example 2

```text
Input: arr[] = [2, 7, 6, 5], target = 16  
Output: [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 6], [2, 2, 5, 5], [2, 2, 2, 2, 4, 4], [2, 2, 6, 6], [2, 5, 7], [5, 5, 6]]
Explanation: Total number of possible combinations are 7.
```

### Example 3

```text
Input: arr[] = [6, 5, 7], target = 8  
Output: []
Explanation: There are no possible combinations such that target sum is 8.
```

---

## ✅ Constraints

* `1 <= arr.size() <= 30`
* `2 <= arr[i] <= 40`
* `2 <= target <= 40`
* All elements in `arr[]` are **distinct**

---

## ⏱ Expected Time & Space Complexity

* **Time Complexity:** O(K \* 2^K), where K = target / min(arr)
* **Auxiliary Space:** O(K)

---

## 🏢 Company Tags

`Amazon`, `Microsoft`, `Adobe`

---

## 🧠 Topic Tags

`Recursion`, `Backtracking`, `Algorithms`

---

## 🔁 Related Articles

* [Combinational Sum – GeeksforGeeks](https://www.geeksforgeeks.org/find-all-combinations-that-sum-to-a-target/)
* [Backtracking Techniques](https://www.geeksforgeeks.org/backtracking-introduction/)

---

Sure! Here's a full explanation using **backtracking** logic along with **step-by-step dry run**, followed by the **code for Python, C++, and JavaScript** with inline comments.

---

## 🔍 Problem Recap: Combination Sum

You are given an array of **distinct positive integers** and a **target** value. Return all **unique combinations** of elements that sum to the target. Each number in `arr` can be used **multiple times**.

---

## 🧠 Backtracking Logic

**Core Idea:**
We use backtracking to try all possible combinations. At every step:

* We either **include** the current number and **stay** at the same index (because repetition is allowed).
* Or we **exclude** it and move to the next index.

**Pruning Conditions:**

* If the current sum becomes **greater** than the target → backtrack.
* If the current sum becomes **equal** to the target → store the current path.

---

## 🔁 Step-by-Step Dry Run

### Input:

```python
arr = [2, 3, 6, 7], target = 7
```

### Process:

* Sort `arr` → \[2, 3, 6, 7]
* Start from index 0:

  * Take `2`, remaining = 5 → \[2]

    * Take `2`, remaining = 3 → \[2, 2]

      * Take `2`, remaining = 1 → \[2, 2, 2]

        * Take `2`, remaining = -1 → stop
      * Backtrack
    * Take `3`, remaining = 0 → ✅ \[2, 2, 3]
  * Take `3`, remaining = 4 → ...
  * Take `7`, remaining = 0 → ✅ \[7]

### Output:

```
[[2, 2, 3], [7]]
```

---

## ✅ Python Code

```python
#User function Template for python3

class Solution:
    def combinationSum(self, arr, target):
        res = []
        arr.sort()  # sort to help with pruning and consistency

        def backtrack(index, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0 or index == len(arr):
                return

            # include arr[index]
            path.append(arr[index])
            backtrack(index, path, remaining - arr[index])
            path.pop()

            # exclude arr[index] and move forward
            backtrack(index + 1, path, remaining)

        backtrack(0, [], target)
        return res
```

---

## ✅ C++ Code

```cpp
// User function template for C++

class Solution {
  public:
    vector<vector<int>> res;

    void backtrack(vector<int>& arr, int index, int target, vector<int>& path) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        if (target < 0 || index >= arr.size())
            return;

        // include arr[index]
        path.push_back(arr[index]);
        backtrack(arr, index, target - arr[index], path);
        path.pop_back();

        // exclude arr[index]
        backtrack(arr, index + 1, target, path);
    }

    vector<vector<int>> combinationSum(vector<int> &arr, int target) {
        sort(arr.begin(), arr.end()); // helpful for pruning
        vector<int> path;
        backtrack(arr, 0, target, path);
        return res;
    }
};
```

---

## ✅ JavaScript Code

```javascript
// User function Template for javascript

class Solution {
    combinationSum(arr, target) {
        let res = [];
        arr.sort((a, b) => a - b);

        const backtrack = (index, path, remaining) => {
            if (remaining === 0) {
                res.push([...path]);
                return;
            }
            if (remaining < 0 || index === arr.length) return;

            // include arr[index]
            path.push(arr[index]);
            backtrack(index, path, remaining - arr[index]);
            path.pop();

            // exclude arr[index]
            backtrack(index + 1, path, remaining);
        };

        backtrack(0, [], target);
        return res;
    }
}
```

---

Certainly! Let’s break down the code **line by line** and walk through the **core logic, recursion, and backtracking** used to solve the **Combination Sum** problem.

---

## 🧩 Problem Recap:

Given:

* An array `arr[]` of **distinct positive integers**
* A `target` sum

Goal:

* Find all **unique combinations** of numbers from `arr[]` that **sum to `target`**
* Each number can be used **any number of times**
* The same combination **order doesn’t matter** (e.g., `[2,2,3]` is the same as `[2,3,2]`)

---

## 🧠 High-Level Strategy: Backtracking

Backtracking = Try → Explore → Undo
We try each number:

* **Include it** (and stay on the same index since reuse is allowed)
* **Skip it** (move to the next index)

---

## 🧵 Detailed Code Explanation

```python
class Solution:
    def combinationSum(self, arr, target):
```

We define a class `Solution` and its method `combinationSum(arr, target)`. This will be called with a list `arr[]` of integers and the desired `target` sum.

```python
        res = []
```

We initialize a list `res` to store all valid combinations that sum to the target.

```python
        arr.sort()  # sort to help with pruning and consistency
```

Sorting is **not required** for correctness but:

* Helps with **early stopping** in some implementations
* Keeps combinations in consistent order (optional benefit)

```python
        def backtrack(index, path, remaining):
```

We define a **recursive helper function** `backtrack(...)`:

* `index`: current index in `arr`
* `path`: current combination being built (list of numbers)
* `remaining`: the sum left to reach the target

```python
            if remaining == 0:
                res.append(path[:])
                return
```

✅ **Base case**: If the remaining sum is exactly 0, we found a valid combination. Append a copy (`[:]`) of `path` to the result.

```python
            if remaining < 0 or index == len(arr):
                return
```

❌ **Pruning case**:

* If `remaining` is negative, we overshot → backtrack
* If `index` is out of bounds, stop recursion

---

## 🔁 Recursive Choices

```python
            # include arr[index]
            path.append(arr[index])
            backtrack(index, path, remaining - arr[index])
            path.pop()
```

### 🟢 Include current number (`arr[index]`):

* Subtract it from `remaining`
* Recurse with the **same index** (you can reuse this number)
* After recursion, **undo** the choice with `path.pop()` (classic backtracking)

```python
            # exclude arr[index] and move forward
            backtrack(index + 1, path, remaining)
```

### 🔴 Exclude current number:

* Skip it and go to the **next index**
* Do **not** change the remaining sum

---

```python
        backtrack(0, [], target)
```

Kick off the recursion from:

* Index `0`
* Empty path `[]`
* Full `target`

---

```python
        return res
```

Return the list of all valid combinations.

---

## ✅ Example Dry Run

### Input:

```python
arr = [2, 3, 6, 7]
target = 7
```

### First few calls:

```
backtrack(0, [], 7)
→ include 2 → backtrack(0, [2], 5)
  → include 2 → backtrack(0, [2,2], 3)
    → include 2 → backtrack(0, [2,2,2], 1)
      → include 2 → backtrack(0, [2,2,2,2], -1) ❌
    → exclude 2 → try 3 → [2,2,3] ✅
→ exclude 2 → try 3 → backtrack(1, [3], 4) ...
→ try 7 → [7] ✅
```

### Final output:

```
[[2, 2, 3], [7]]
```

---

## ⏱️ Time & Space Complexity

| Metric      | Value                                                  |
| ----------- | ------------------------------------------------------ |
| Time        | O(K \* 2^K) in worst case, where K = target / min(arr) |
| Space       | O(K) recursion stack                                   |
| Output size | Varies by answer count                                 |

---

## 📌 Summary

| Step         | Action                                   |
| ------------ | ---------------------------------------- |
| ✅ Base Case  | If remaining == 0 → store path           |
| ⛔ Stop       | If remaining < 0 or index == len(arr)    |
| 🔁 Include   | Add arr\[index], recurse with same index |
| 🔁 Exclude   | Skip arr\[index], recurse with index + 1 |
| 🔙 Backtrack | Undo the path using `path.pop()`         |

---

Let me know if you'd like this traced visually or implemented iteratively!

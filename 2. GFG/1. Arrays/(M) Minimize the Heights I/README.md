
---

# Minimize the Heights I

**Difficulty**: Medium
**Accuracy**: 26.16%
**Submissions**: 120K+
**Points**: 4
**Average Time**: 25m

---

## Problem Statement

Given an array `arr[]` and a positive integer `k` denoting heights of towers, you have to modify the height of each tower either by increasing or decreasing them by `k` **only once**.

Find out what could be the possible **minimum difference** of the height of **shortest** and **longest** towers after you have modified each tower. The modified height of the tower can be negative.

> **Note**: A slight modification of the problem can be found [here](https://practice.geeksforgeeks.org/problems/minimize-the-heights-ii/1).

---

## Examples

### Example 1:

```
Input: arr[] = [1, 5, 8, 10], k = 2  
Output: 5  
Explanation: The array can be modified as [3, 3, 6, 8].  
The difference between the largest and the smallest is 8 - 3 = 5.
```

### Example 2:

```
Input: arr[] = [3, 9, 12, 16, 20], k = 3  
Output: 11  
Explanation: The array can be modified as [6, 12, 9, 13, 17].  
The difference between the largest and the smallest is 17 - 6 = 11.
```

---

## Constraints

* $1 \leq k \leq 10^4$
* $1 \leq \text{number of towers} \leq 10^5$
* $0 \leq \text{arr}[i] \leq 10^5$

---

## Expected Complexities

* **Time Complexity**: $O(n \log n)$
* **Auxiliary Space**: $O(1)$

---

## Company Tags

`Adobe`

---

## Topic Tags

* `two-pointer-algorithm`
* `Arrays`
* `Greedy`
* `Data Structures`
* `Algorithms`

---
You're absolutely right — and thank you for sharing the correct and clean implementation. ✅
You're using the **most optimal and interviewer-expected version** of the solution. Let's break this down and document it thoroughly so it can serve as a solid reference.

---

## ✅ Minimize the Heights I — README Style

### Problem Statement

You are given an array `arr[]` and a positive integer `k`.
Your task is to **modify each element only once**, by either increasing or decreasing it by `k`, and then **minimize the difference** between the maximum and minimum elements in the modified array.

---

### Constraints

* `1 ≤ k ≤ 10⁴`
* `1 ≤ number of towers ≤ 10⁵`
* `0 ≤ arr[i] ≤ 10⁵`
* Time: `O(n log n)`
* Space: `O(1)`

---

### Examples

#### Input:

```
arr = [1, 5, 8, 10]
k = 2
```

#### Output:

```
5
```

#### Explanation:

* Modify the array as `[3, 3, 6, 8]`
* Max = 8, Min = 3 → Diff = 5

---

### ✅ Optimal Code (Python)

```python
#User function Template for python3

class Solution:
    def getMinDiff(self,arr,k):
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()
        diff = arr[-1] - arr[0]  # Initial difference

        for i in range(n - 1):
            # min and max values after modifying elements
            low = min(arr[0] + k, arr[i + 1] - k)
            high = max(arr[-1] - k, arr[i] + k)
            diff = min(diff, high - low)

        return diff
```

---

### 📊 Dry Run (with example: arr = \[1, 5, 8, 10], k = 2)

| i | arr\[i] | arr\[i+1] | low = min(arr\[0]+k, arr\[i+1]-k) | high = max(arr\[-1]-k, arr\[i]+k) | high - low |
| - | ------- | --------- | --------------------------------- | --------------------------------- | ---------- |
| 0 | 1       | 5         | min(3, 3) = 3                     | max(8, 3) = 8                     | 5          |
| 1 | 5       | 8         | min(3, 6) = 3                     | max(8, 7) = 8                     | 5          |
| 2 | 8       | 10        | min(3, 8) = 3                     | max(8, 10) = 10                   | 7          |

* ✅ Final Answer: `min(5, 5, 7) = 5`

---

### ✅ C++ Version

```cpp
class Solution {
  public:
    int getMinDiff(vector<int> &arr, int k) {
        int n = arr.size();
        if (n == 1) return 0;
        sort(arr.begin(), arr.end());
        int diff = arr[n-1] - arr[0];

        for (int i = 0; i < n - 1; i++) {
            int low = min(arr[0] + k, arr[i + 1] - k);
            int high = max(arr[n - 1] - k, arr[i] + k);
            diff = min(diff, high - low);
        }
        return diff;
    }
};
```

---

### ✅ JavaScript Version

```javascript
class Solution {
    getMinDiff(arr, k) {
        arr.sort((a, b) => a - b);
        let n = arr.length;
        if (n === 1) return 0;

        let diff = arr[n - 1] - arr[0];

        for (let i = 0; i < n - 1; i++) {
            let low = Math.min(arr[0] + k, arr[i + 1] - k);
            let high = Math.max(arr[n - 1] - k, arr[i] + k);
            diff = Math.min(diff, high - low);
        }

        return diff;
    }
}
```

---

Great question! Here's a list of **potential follow-up interview questions** that build upon the "Minimize the Heights I" problem. These are commonly asked by interviewers at product-based companies like Amazon, Adobe, Flipkart, etc., especially to assess your ability to optimize, adapt, and extend core logic.

---

## ✅ **Follow-Up Questions and Variations**

### 1. **Minimize the Heights II**

> 🔁 **Each element in the array can be increased or decreased by `k`, and you can do this at most `once`.**

🧠 **Twist**: In this variation, the decision is made per element — either add or subtract `k` — to minimize the overall max-min difference.

👨‍💻 **New logic**:

* Use greedy + sorting.
* Track potential minimum and maximum values after either `+k` or `-k` operation on each element.
* It's more dynamic compared to the fixed operation in the original problem.

📘 Related GFG link: ["Minimize the Heights II"](https://practice.geeksforgeeks.org/problems/minimize-the-heights-ii/1)

---

### 2. **What if you are allowed to change `at most x` elements?**

> 🎯 “Minimize the height difference by changing at most x elements.”

🧠 **Assessment**:

* You need to choose **which x elements to modify**.
* May involve **priority queues** (min-heap / max-heap) or a **greedy strategy** to maximize impact per operation.

---

### 3. **What if k is different for each tower?**

> 🏗️ Each `arr[i]` has its own `k[i]` that can be added/subtracted once.

🧠 **Impact**:

* You can no longer globally sort and apply k uniformly.
* Use a customized structure (like a `pair<height, k>`) and determine optimal values with local greedy comparison.

---

### 4. **What if negative heights are not allowed?**

> ❗ “Ensure no modified height becomes negative.”

🧠 **Change**:

* When doing `arr[i] - k`, check: `arr[i] - k >= 0`
* This adds a **boundary constraint**, and may restrict which values can be reduced.

---

### 5. **Minimize Cost to Equalize Heights**

> 💸 You are given a `cost[i]` array — cost to change each tower's height by 1 unit.

🧠 **Objective**:

* Choose a common target height `h`.
* Minimize `sum(cost[i] * abs(arr[i] - h))`
* Use **binary search on answer**, or take the **weighted median** as optimal height.

📘 Similar to: “Equalize the Towers” or “Weighted Median of Heights”

---

### 6. **Can you solve this in-place without sorting?**

> ⚡ "What if the input array is large and you must work in-place with O(1) extra space?"

🧠 **Why it's asked**:

* To check **memory-aware optimizations**.
* In-place partitioning, like Dutch National Flag problem, or rotating logic may be tested.

---

### 7. **How would you handle very large k (k > 1e9)?**

> 🧠 Check if candidate understood that applying `+k`/`-k` repeatedly becomes meaningless if `k` exceeds the difference range.

---


## 📌 Conclusion

Mastering the original “Minimize Heights I” problem opens doors to a range of interview variations. These extensions test:

* **Greedy vs DP** thinking
* **Edge handling**
* **Time and space trade-offs**
* **Scalability**

---

## 🔄 Meta-level Interviewer Questions

These assess your communication and optimization skills:

* Can you prove your solution is optimal?
* What would the complexity be if you used brute force?
* Can your logic handle duplicates or all equal values?
* Can you write tests to validate all edge cases?
* How would you test this function in production?

Absolutely — these **meta-level questions** are gold for interviews. They help you **stand out** by showcasing clarity, critical thinking, and a software engineering mindset. Here’s how to **answer each one confidently** using the *“Minimize the Heights I”* problem as a base:

---

## ✅ **1. Can you prove your solution is optimal?**

### 🔍 What they’re checking:

* Whether you understand the **greedy strategy** and **why** it works.

### ✅ Sample Response:

> Yes. My solution is based on sorting the array and trying all possible boundaries between elements to minimize the max-min difference after applying `+k` and `-k`.
> For any index `i`, we:
>
> * Increase elements up to index `i` by `k`.
> * Decrease the rest by `k`.
>
> The **optimal answer** is among these transitions because:
>
> * Sorting ensures we explore increasing and decreasing patterns in order.
> * We cover all cut-off points and compute the minimal difference.
>
> This is the standard greedy approach for this category of problems and has been proven to work correctly via **problem constraints** and **mathematical proof** of min-max optimization.

---

## ✅ **2. What would the complexity be if you used brute force?**

### 🔍 What they’re checking:

* Do you know how inefficient naive methods can get?

### ✅ Sample Response:

> Brute force would involve trying **all possible `+k`/`-k` combinations** for every element:
>
> * Each element has 2 choices → total 2^n combinations.
> * For `n = 10^5`, this is infeasible.
>
> Even checking all combinations for small `n = 20` is slow.
> That’s why we **sort the array** and reduce the transitions to only `n-1` points (O(n)) instead.

---

## ✅ **3. Can your logic handle duplicates or all equal values?**

### 🔍 What they’re checking:

* Does your algorithm gracefully handle edge cases?

### ✅ Sample Response:

> Yes, the solution handles duplicates and identical values.
>
> * If all elements are equal, the difference is 0, and no operation is needed.
> * Duplicates do not affect correctness since the array is sorted, and each element is independently considered.
>
> ✅ Example:
>
> * arr = \[5, 5, 5], k = 2 → All values become either 3 or 7 → Difference = 4
> * But we can pick the same `+k` or `-k` strategy for all → min diff = 0.

---

## ✅ **4. Can you write tests to validate all edge cases?**

### 🔍 What they’re checking:

* Do you think like a test engineer?

### ✅ Sample Response:

```python
# 1. All equal elements
assert getMinDiff([4, 4, 4, 4], 5) == 0

# 2. Only one element
assert getMinDiff([10], 3) == 0

# 3. Two elements
assert getMinDiff([1, 10], 5) == 4  # becomes [6, 5]

# 4. Already optimal
assert getMinDiff([1, 5, 8, 10], 2) == 5

# 5. Negative heights not allowed (implicitly handled since we take max/min)

# 6. Random large input
arr = list(range(1, 100001))
assert getMinDiff(arr, 0) == arr[-1] - arr[0]
```

---

## ✅ **5. How would you test this function in production?**

### 🔍 What they’re checking:

* Can you think about real-world deployment?

### ✅ Sample Response:

> In production, I’d:
>
> * **Add extensive unit tests** covering boundaries and edge cases (1 element, 100K elements, k = 0, large k).
> * Run **property-based tests**: like, "after applying k, the range never exceeds original max-min".
> * Use **fuzz testing** to generate random but valid arrays.
> * Add **logging** around extreme values and result boundaries.
> * Validate memory usage for very large arrays (1e5+) to ensure no crash or slowdown.
> * Include in CI pipeline with **assertions**, **timeouts**, and **input validation**.

---

## 🧠 Final Note

Mastering **meta questions** like these shows you’re not just solving the problem — you're thinking like a **reliable engineer** who:

* Understands complexity
* Writes maintainable/testable code
* Anticipates edge behavior
* Thinks at scale


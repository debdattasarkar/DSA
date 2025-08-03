
---

# 🏗️ Equalize the Towers

**Difficulty:** Medium
**Tags:** Binary Search, Greedy, Arrays, Cost Optimization

---

## 📘 Problem Statement

You are given an array `heights[]` representing the height of each tower and an array `cost[]` representing the cost to increase or decrease the height of that respective tower **by 1 unit**.

> Modify the towers such that all towers have the same height, with the **minimum total cost**.

---

## 🧮 Constraints

* `1 ≤ heights.length = cost.length ≤ 10^5`
* `1 ≤ heights[i] ≤ 10^4`
* `1 ≤ cost[i] ≤ 10^3`

---

## ✅ Example

### Example 1

```
Input:
heights = [1, 2, 3]
cost = [10, 100, 1000]

Output:
120

Explanation:
Best to raise tower 1 by 1 (10), tower 2 by 0 (0), and lower tower 3 by 1 (1000). Total: 10 + 0 + 110 = 120.
```

---

### Example 2

```
Input:
heights = [7, 1, 5]
cost = [1, 1, 1]

Output:
6

Explanation:
Targeting height = 5: (2 + 4 + 0) = 6 total units, each unit costs 1 → total = 6.
```

---

## 🔍 Approach

We want to **minimize the total cost** to make all heights the same.

Let the target height be `h`. Then, the cost to make `heights[i]` → `h` is:

```
abs(heights[i] - h) * cost[i]
```

We try all values of `h` (in a smart way — binary search!) from the **minimum** to **maximum height** in `heights[]`.

---

## 👣 Step-by-Step Dry Run

For:

```python
heights = [1, 2, 3]
cost = [10, 100, 1000]
```

Let’s binary search over possible target heights \[1..3]:

| Target Height | Cost Calculation                                         | Total Cost |
| ------------- | -------------------------------------------------------- | ---------- |
| h = 2         | (1→2)=1×10 + (2→2)=0×100 + (3→2)=1×1000 → 10 + 0 + 1000  | 1010       |
| h = 3         | (1→3)=2×10 + (2→3)=1×100 + (3→3)=0×1000 → 20 + 100 + 0   | 120        |
| h = 1         | (1→1)=0×10 + (2→1)=1×100 + (3→1)=2×1000 → 0 + 100 + 2000 | 2100       |

✅ Minimum is **120** when h = 3.

---

## 🧠 Time Complexity

* Binary search height range: `O(log(maxHeight))`
* For each height guess, compute total cost in `O(n)`
* **Total Time: `O(n * log(max(heights)))`**

---

## 🐍 Python Code

```python
class Solution:
    def minCost(self, heights, cost):
        def compute_total(h):
            return sum(abs(h - heights[i]) * cost[i] for i in range(len(heights)))

        left, right = min(heights), max(heights)
        ans = compute_total(heights[0])

        while left < right:
            mid = (left + right) // 2
            cost1 = compute_total(mid)
            cost2 = compute_total(mid + 1)

            ans = min(cost1, cost2)

            if cost1 < cost2:
                right = mid
            else:
                left = mid + 1

        return ans
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    long long computeTotal(int h, vector<int>& heights, vector<int>& cost) {
        long long total = 0;
        for (int i = 0; i < heights.size(); i++)
            total += 1LL * abs(heights[i] - h) * cost[i];
        return total;
    }

    int minCost(vector<int>& heights, vector<int>& cost) {
        int left = *min_element(heights.begin(), heights.end());
        int right = *max_element(heights.begin(), heights.end());
        long long ans = computeTotal(heights[0], heights, cost);

        while (left < right) {
            int mid = (left + right) / 2;
            long long cost1 = computeTotal(mid, heights, cost);
            long long cost2 = computeTotal(mid + 1, heights, cost);
            ans = min(cost1, cost2);

            if (cost1 < cost2) right = mid;
            else left = mid + 1;
        }

        return ans;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    minCost(heights, cost) {
        const computeTotal = (h) => {
            let total = 0;
            for (let i = 0; i < heights.length; i++)
                total += Math.abs(heights[i] - h) * cost[i];
            return total;
        };

        let left = Math.min(...heights);
        let right = Math.max(...heights);
        let ans = computeTotal(heights[0]);

        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            let cost1 = computeTotal(mid);
            let cost2 = computeTotal(mid + 1);
            ans = Math.min(cost1, cost2);

            if (cost1 < cost2) right = mid;
            else left = mid + 1;
        }

        return ans;
    }
}
```

---

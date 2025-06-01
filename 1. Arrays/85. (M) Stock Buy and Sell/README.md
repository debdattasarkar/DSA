### ✅ Problem Summary: **Stock Buy and Sell (Multiple Transactions)**

Given an array `arr[]` representing stock prices over `n` days, the task is to **maximize profit** by choosing multiple **buy-sell** pairs — i.e., buy on a day and sell on a later day, repeatedly.

#### Constraints:

* You can only hold one stock at a time.
* Buy before you sell.
* You can do this multiple times to accumulate profit.

---

### 🧠 Intuition & Strategy:

You earn profit by buying at a **local minima** and selling at a **local maxima**.
A simpler realization: **every increasing pair contributes to the profit**.

### ➕ Key Insight:

If `arr[i+1] > arr[i]`, **buy at `i` and sell at `i+1`**, i.e., add `arr[i+1] - arr[i]` to the profit.

---

### 🧪 Dry Run

```plaintext
arr = [100, 180, 260, 310, 40, 535, 695]

Buy at 100, sell at 310 → profit = 210
Buy at 40, sell at 695 → profit = 655

Total Profit = 210 + 655 = 865 ✅
```

---

## ✅ Python Code (with comments)

```python
class Solution:
    def stockBuySell(self, arr):
        profit = 0
        for i in range(1, len(arr)):
            # Add profit from every increasing pair
            if arr[i] > arr[i - 1]:
                profit += arr[i] - arr[i - 1]
        return profit
```

---

## ✅ C++ Code (with comments)

```cpp
class Solution {
  public:
    int stockBuySell(vector<int> &arr) {
        int profit = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] > arr[i - 1]) {
                profit += arr[i] - arr[i - 1]; // Add profit from uptrend
            }
        }
        return profit;
    }
};
```

---

## ✅ JavaScript Code (with comments)

```javascript
class Solution {
    stockBuySell(arr) {
        let profit = 0;
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i - 1]) {
                profit += arr[i] - arr[i - 1]; // Buy low, sell high on rise
            }
        }
        return profit;
    }
}
```

---

### ⏱️ Time and Space Complexity

* **Time:** O(n) — Single pass.
* **Space:** O(1) — Constant space.

---

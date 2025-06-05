Here’s a clear breakdown of the **“Stock Buy and Sell – Max 2 Transactions Allowed”** problem, along with:

1. **Step-by-step dry run**
2. **Intuition & logic**
3. **Solutions in Python, C++, and JavaScript with inline comments**

---

### 🧠 Problem Summary

Given an array `prices[]` representing daily stock prices, we need to **maximize profit** by making at most **two transactions** (buy→sell→buy→sell).

⚠️ Constraint:

* Second buy must happen **after** the first sell.

---

### 🔍 Intuition & Dry Run

We split the process into two phases:

* **Forward pass**: Compute `profitLeft[i]`: the max profit if we sell on or before day `i`
* **Backward pass**: Compute `profitRight[i]`: the max profit if we buy on or after day `i`

Finally, `max(profitLeft[i] + profitRight[i])` gives the answer.

---

### 🧪 Dry Run for Input: `[10, 22, 5, 75, 65, 80]`

**Forward Profit (left to right)**:

* Buy at 10, max profit till each day: `[0, 12, 12, 70, 70, 70]`

**Backward Profit (right to left)**:

* Sell at 80, max profit from each day: `[70, 70, 75, 5, 15, 0]`

**Combined**:

* Max total = max(`forward[i] + backward[i]`) = `12 + 75 = 87`

---

### ✅ Python Code (With Inline Comments)

```python
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        
        # Forward pass: max profit until day i (1st transaction)
        left_profits = [0]*n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)
        
        # Backward pass: max profit from day i (2nd transaction)
        max_price = prices[-1]
        max_total = left_profits[-1]
        right_profit = 0
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profit = max(right_profit, max_price - prices[i])
            # Combine with first transaction
            max_total = max(max_total, left_profits[i] + right_profit)
        
        return max_total
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    int maxProfit(vector<int> &prices) {
        int n = prices.size();
        if (n == 0) return 0;
        
        vector<int> left(n, 0); // max profit up to i
        int min_price = prices[0];
        
        for (int i = 1; i < n; ++i) {
            min_price = min(min_price, prices[i]);
            left[i] = max(left[i - 1], prices[i] - min_price);
        }
        
        int max_price = prices[n - 1], right_profit = 0, max_total = left[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            max_price = max(max_price, prices[i]);
            right_profit = max(right_profit, max_price - prices[i]);
            max_total = max(max_total, left[i] + right_profit);
        }
        
        return max_total;
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    maxProfit(prices) {
        const n = prices.length;
        if (n === 0) return 0;

        let left = Array(n).fill(0);
        let minPrice = prices[0];

        for (let i = 1; i < n; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            left[i] = Math.max(left[i - 1], prices[i] - minPrice);
        }

        let maxPrice = prices[n - 1];
        let rightProfit = 0, maxTotal = left[n - 1];

        for (let i = n - 2; i >= 0; i--) {
            maxPrice = Math.max(maxPrice, prices[i]);
            rightProfit = Math.max(rightProfit, maxPrice - prices[i]);
            maxTotal = Math.max(maxTotal, left[i] + rightProfit);
        }

        return maxTotal;
    }
}
```

---

Would you like a version that allows **k transactions**, or is 2 enough for now?

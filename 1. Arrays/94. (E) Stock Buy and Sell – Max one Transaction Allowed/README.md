# 📈 Stock Buy and Sell – Max One Transaction Allowed

## 🧩 Problem Statement

Given an array `prices[]` of length `n`, where each element represents the price of a stock on day `i`, find the **maximum profit** that can be earned by buying and selling the stock **only once**. You must buy before you sell.

If no profitable transaction is possible, return `0`.

### ❗ Constraints

* `1 ≤ prices.length ≤ 10^5`
* `0 ≤ prices[i] ≤ 10^4`

---

## 🧠 Explanation

### Approach

* Traverse the array while tracking the **minimum price seen so far**.
* At each step, compute the potential profit by selling on the current day (`current price - min price`).
* Update the **maximum profit** accordingly.

### Dry Run

#### Example 1:

```
prices = [7, 10, 1, 3, 6, 9, 2]
```

* Day 0: min\_price = 7, profit = 0
* Day 1: min\_price = 7, profit = 10 - 7 = 3
* Day 2: min\_price = 1, profit = 0
* Day 3: profit = 3 - 1 = 2
* Day 4: profit = 6 - 1 = 5
* Day 5: profit = 9 - 1 = 8 ✅
* Day 6: profit = 2 - 1 = 1

→ Maximum profit = **8**

#### Example 2:

```
prices = [7, 6, 4, 3, 1]
```

* Prices decrease continuously.
  → No profitable transaction → Return **0**

---

## 🧮 Time & Space Complexity

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(1)

---

## ✅ Sample Output

### Example 1:

```
Input: [7, 10, 1, 3, 6, 9, 2]
Output: 8
```

### Example 2:

```
Input: [7, 6, 4, 3, 1]
Output: 0
```

---

## 🐍 Python Code

```python
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit
```

---

## 💻 C++ Code

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;

        for (int price : prices) {
            if (price < min_price)
                min_price = price;
            else
                max_profit = max(max_profit, price - min_price);
        }

        return max_profit;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    maxProfit(prices) {
        let minPrice = Infinity;
        let maxProfit = 0;

        for (let price of prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }

        return maxProfit;
    }
}
```

---

## 🏷️ Tags

`Greedy` `Arrays` `Sliding Window` `One Pass`

---

Let me know if you'd like this in a `.md` file or packaged with test cases.

Here is a README-style explanation and implementation for **Leetcode 274 – H-Index**, including a dry run and code in **Python**, **C++**, and **JavaScript** with inline comments.

---

# 📊 H-Index (Leetcode #274)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Sorting`, `Counting Sort`

---

## 📘 Problem Statement

You're given an array `citations`, where `citations[i]` is the number of citations for the i-th paper.
Return the **H-index** of the researcher.

📌 **Definition of H-index**:
It is the **maximum number `h`** such that the researcher has at least **`h` papers** with **`≥ h` citations**.

---

## 🧪 Examples

### Example 1:

```
Input:  [3, 0, 6, 1, 5]
Output: 3

Explanation:
Papers = [3, 0, 6, 1, 5]
Sorted = [0, 1, 3, 5, 6]
3 papers have ≥ 3 citations → h = 3 ✅
```

### Example 2:

```
Input:  [1, 3, 1]
Output: 1
Only 1 paper has ≥ 2 citations, but 2 papers have ≥ 1 citation ⇒ h = 1
```

---

## ✅ Intuition & Approach

### Sort-based Method:

1. Sort citations in **descending** order.
2. Iterate over the sorted list:

   * At position `i`, check if `citations[i] >= i + 1`
   * The largest such `i + 1` is the H-index

---

## 🧪 Dry Run for `[3, 0, 6, 1, 5]`

Sorted: `[6, 5, 3, 1, 0]`

| i | citations\[i] | i+1 | Condition (≥ i+1)? |
| - | ------------- | --- | ------------------ |
| 0 | 6             | 1   | ✅                  |
| 1 | 5             | 2   | ✅                  |
| 2 | 3             | 3   | ✅                  |
| 3 | 1             | 4   | ❌                  |

✅ Answer: `3`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i  # First time citation is less than position
        return len(citations)  # All values >= positions
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.rbegin(), citations.rend());
        for (int i = 0; i < citations.size(); ++i) {
            if (citations[i] < i + 1)
                return i;
        }
        return citations.size();
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    citations.sort((a, b) => b - a);
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] < i + 1) return i;
    }
    return citations.length;
};
```

---

## 🔁 Alternate (Counting Sort) – O(n)

Because all `citations[i] <= 1000`, we can use **counting sort** to optimize to O(n) time. Let me know if you want that!

---

## ✅ Summary

| Metric           | Value                  |
| ---------------- | ---------------------- |
| Time Complexity  | `O(n log n)` (sort)    |
| Space Complexity | `O(1)` (in-place sort) |
| Alternate        | `O(n)` using counting  |

---

Absolutely! The **counting sort approach** is an efficient `O(n)` solution for computing the **H-index** when `citations[i]` are bounded (as in this problem).

---

# ⚡️ Counting Sort Version – H-Index (Leetcode #274)

---

## 💡 Key Insight

If a researcher has `n` papers, then their **H-index is at most `n`**, regardless of how high citations go.

So instead of sorting, we can:

1. Count how many papers have `i` citations (for `i = 0` to `n`)
2. Count how many papers have at least `i` citations
3. Return the highest `i` where the count ≥ `i`

---

## 📊 Dry Run for `citations = [3, 0, 6, 1, 5]`

```
n = 5
bucket = [0, 0, 0, 0, 0, 0]  // size n+1

→ cap all values at n (citations > n → bucket[n]++)
bucket = [1, 1, 0, 1, 0, 2]
          ^  ^     ^     ^
          0  1     3     5+

Now scan from i = 5 to 0:
cumulative = 0
→ i = 5: cumulative = 2 → not ≥ 5
→ i = 4: cumulative = 2 → not ≥ 4
→ i = 3: cumulative = 3 → ✅ H-index = 3
```

---

## 🐍 Python Code (O(n))

```python
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)

        # Count citation frequency
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += bucket[i]
            if total >= i:
                return i

        return 0
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> bucket(n + 1, 0);

        for (int c : citations) {
            if (c >= n) bucket[n]++;
            else bucket[c]++;
        }

        int total = 0;
        for (int i = n; i >= 0; --i) {
            total += bucket[i];
            if (total >= i) return i;
        }

        return 0;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    const n = citations.length;
    const bucket = Array(n + 1).fill(0);

    for (let c of citations) {
        if (c >= n) bucket[n]++;
        else bucket[c]++;
    }

    let total = 0;
    for (let i = n; i >= 0; i--) {
        total += bucket[i];
        if (total >= i) return i;
    }

    return 0;
};
```

---

## ✅ Summary

| Metric           | Value                            |
| ---------------- | -------------------------------- |
| Time Complexity  | `O(n)`                           |
| Space Complexity | `O(n)`                           |
| Best for         | Large arrays with bounded values |

---

Here’s a refined and clear version of the **Counting Sort approach** for **Leetcode 274 – H-Index**, using **O(n)** time and space.

---

# 📊 H-Index – Counting Sort Approach

### ✅ Goal:

Find the largest number **`h`** such that **at least `h` papers** have **`≥ h` citations**.

---

## 🔍 Idea:

1. You have `n` papers.

2. Create a bucket array of size `n + 1`, where:

   * `bucket[i]` = number of papers with exactly `i` citations
   * All citations ≥ `n` are counted in `bucket[n]`

3. Scan from the end (highest citation count) down to 0, keeping a cumulative total of papers with `≥ i` citations.

4. When cumulative count ≥ `i`, that’s the H-index.

---

## 🧪 Dry Run

**Input:** `[3, 0, 6, 1, 5]`

1. `n = 5`

2. Build bucket:

   ```
   bucket[0] = 1  (0 citations)
   bucket[1] = 1  (1 citation)
   bucket[3] = 1  (3 citations)
   bucket[5] = 2  (5 and 6 → capped to 5)
   ```

   ➜ `bucket = [1,1,0,1,0,2]`

3. Accumulate from i = 5 to 0:

   ```
   i = 5 → total = 2 → total < 5
   i = 4 → total = 2
   i = 3 → total = 3 ✅ ⇒ h-index = 3
   ```

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)

        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += bucket[i]
            if total >= i:
                return i
        return 0
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> bucket(n + 1, 0);

        for (int c : citations) {
            if (c >= n) bucket[n]++;
            else bucket[c]++;
        }

        int total = 0;
        for (int i = n; i >= 0; --i) {
            total += bucket[i];
            if (total >= i) return i;
        }

        return 0;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    const n = citations.length;
    const bucket = Array(n + 1).fill(0);

    for (let c of citations) {
        if (c >= n) bucket[n]++;
        else bucket[c]++;
    }

    let total = 0;
    for (let i = n; i >= 0; i--) {
        total += bucket[i];
        if (total >= i) return i;
    }

    return 0;
};
```

---

## ✅ Summary

| Feature                 | Value             |
| ----------------------- | ----------------- |
| Time Complexity         | `O(n)`            |
| Space Complexity        | `O(n)`            |
| Handles large citations | Yes (clamps to n) |

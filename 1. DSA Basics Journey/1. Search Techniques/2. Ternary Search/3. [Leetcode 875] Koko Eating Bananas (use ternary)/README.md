Let’s deep dive into **Leetcode 875: Koko Eating Bananas** using a **ternary search approach**, even though it's more commonly solved with binary search. We’ll walk through the problem, dry run, logic, and provide a detailed Python implementation.

---

## 🍌 Leetcode 875: Koko Eating Bananas

🔗 [Leetcode Link](https://leetcode.com/problems/koko-eating-bananas/)

### ✅ Problem:

Koko loves bananas and has `piles[]` where each element is the number of bananas in a pile.
She eats at most `k` bananas per hour (constant rate), and she has `h` hours to finish them.

**Find the minimum integer value of `k` such that she can eat all the bananas in `h` hours.**

---

## 🧠 Key Insight:

* If `k` is **too small**, she won’t finish in time.
* If `k` is **large**, she may finish early.
* The total hours required for a given `k` is:

```python
hours = sum(ceil(pile / k) for pile in piles)
```

✅ This function is **monotonically decreasing** with `k` ⇒ we can apply **ternary search** (or binary).

---

## ✍️ Dry Run Example

```python
piles = [3, 6, 7, 11]
h = 8

Try k = 5:
  3//5 = 1, 6//5 = 2, 7//5 = 2, 11//5 = 3 → Total = 8 ✅

Try k = 4:
  3//4 = 1, 6//4 = 2, 7//4 = 2, 11//4 = 3 → Total = 8 ✅

Try k = 3:
  3//3 = 1, 6//3 = 2, 7//3 = 3, 11//3 = 4 → Total = 10 ❌

➡️ Answer = 4
```

---

## 🔁 Ternary Search Implementation (Integer Version)

```python
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_hours(speed: int) -> int:
            return sum(math.ceil(pile / speed) for pile in piles)

        left, right = 1, max(piles)
        answer = right  # Initialize worst case

        while right - left > 2:  # Ternary search loop
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            time1 = total_hours(mid1)
            time2 = total_hours(mid2)

            if time1 <= h:
                answer = min(answer, mid1)
                right = mid2 - 1
            else:
                left = mid1 + 1

        # Final check in narrowed window
        for k in range(left, right + 1):
            if total_hours(k) <= h:
                answer = min(answer, k)

        return answer
```

---

## ⏱️ Time & Space Complexity

| Complexity | Value                                                          |
| ---------- | -------------------------------------------------------------- |
| Time       | `O(n * log(max(piles)))` — log from search, `n` per hour check |
| Space      | `O(1)` — constant                                              |

---

## ✅ Summary

| Concept            | Detail                                            |
| ------------------ | ------------------------------------------------- |
| Search Type        | Ternary search on integer domain                  |
| Target             | Minimum speed `k` such that total hours ≤ `h`     |
| Function Type      | Monotonically decreasing (`speed ↑ ⇒ time ↓`)     |
| Alternate Approach | Binary Search (commonly used and slightly faster) |

---

# Comparison of **ternary vs binary** on this problem?

Perfect! Let’s compare **Ternary Search vs Binary Search** on **Leetcode 875: Koko Eating Bananas** from multiple angles:

---

## 🧠 1. **Conceptual Comparison**

| Feature         | **Binary Search**                         | **Ternary Search**                            |
| --------------- | ----------------------------------------- | --------------------------------------------- |
| Search Strategy | Divide into 2 parts                       | Divide into 3 parts                           |
| When Used       | Boolean monotonic conditions (True/False) | Unimodal function (valley or peak shape)      |
| Function Type   | Monotonic                                 | Unimodal                                      |
| Best Suited For | "Yes/No" decisions                        | Optimizing a real value (min/max)             |
| Precision       | Integer or float                          | Typically float (but works with int too)      |
| Performance     | `O(log N)`                                | `O(log N)` but slightly slower due to 2 calls |

---

## 📦 2. **Problem Mapping: Koko’s Case**

In **Leetcode 875**, the function:

```python
total_hours(k) = sum(ceil(pile / k))
```

is:

* **Monotonically decreasing** in `k`
* We want the **minimum `k`** such that `total_hours(k) ≤ h`

✅ **Binary Search is ideal** here because:

* We want the **smallest `k`** that satisfies a Boolean condition (`canFinish(k)`).
* This makes binary search cleaner and slightly faster.

🔁 But **Ternary Search still works** because:

* The function is monotonic ⇒ also unimodal in the valid domain.
* Slower but logically sound.

---

## ✅ 3. **Python Code Comparison**

### 🔹 Binary Search Version (recommended):

```python
def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        hours = sum(math.ceil(p / mid) for p in piles)

        if hours <= h:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
```

### 🔹 Ternary Search Version (works, less common):

```python
def minEatingSpeed(piles, h):
    def total_hours(k):
        return sum(math.ceil(p / k) for p in piles)

    left, right = 1, max(piles)
    answer = right

    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if total_hours(mid1) <= h:
            answer = min(answer, mid1)
            right = mid2 - 1
        else:
            left = mid1 + 1

    for k in range(left, right + 1):
        if total_hours(k) <= h:
            answer = min(answer, k)

    return answer
```

---

## ⏱️ 4. **Performance Summary**

| Metric          | Binary Search                                                       | Ternary Search       |
| --------------- | ------------------------------------------------------------------- | -------------------- |
| Time Complexity | `O(n * log(max(p))`                                                 | `O(n * log(max(p)))` |
| Function Calls  | 1 per loop                                                          | 2 per loop           |
| Precision       | Works with int                                                      | Better with float    |
| Preferred for   | Leetcode 875, where target is smallest `k` satisfying a condition ✅ |                      |

---

## 🧪 5. **Dry Run Result Comparison**

For:

```python
piles = [3, 6, 7, 11]
h = 8
```

Both methods return:

```python
Output: 4
```

✅ But **binary search reaches it faster**, with fewer calls to `total_hours()`.

---

## 📌 Final Recommendation

Use **binary search** when:

* You have a **monotonic Boolean function**
* You're finding **minimum/maximum value** that satisfies a constraint

Use **ternary search** when:

* You want to **optimize a function value**
* The function has a **single peak or trough**

---

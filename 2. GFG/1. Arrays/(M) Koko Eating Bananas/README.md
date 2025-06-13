
---

# 🐵🍌 Koko Eating Bananas

**Difficulty:** Medium
**Accuracy:** 50.27%
**Submissions:** 29K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Koko is given an array `arr[]`, where each element represents a pile of bananas. She has exactly `k` hours to eat all the bananas.

Each hour, Koko can choose **one pile** and eat up to `s` bananas from it.

* If the pile has **at least `s`** bananas, she eats exactly `s` bananas.
* If the pile has **fewer than `s`** bananas, she eats the **entire pile** in that hour.

**Koko can only eat from one pile per hour.**

---

## Goal

Find the **minimum value of `s`** (bananas per hour) such that Koko can finish **all the piles** within `k` hours.

---

## Example 1

```txt
Input:
arr[] = [5, 10, 3]
k = 4

Output:
5

Explanation:
- Koko eats 5 bananas per hour.
- Time for each pile = [1, 2, 1] hours = 4 hours.
```

---

## Example 2

```txt
Input:
arr[] = [5, 10, 15, 20]
k = 7

Output:
10

Explanation:
- Eating rate 10 bananas/hour gives time = [1, 1, 2, 2] = 6 hours ≤ 7.
- 9 would require 8 hours.
```

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^6`
* `1 ≤ k ≤ 10^6`

---

## Expected Time & Space Complexity

* **Time Complexity:** O(n × log(max(arr\[i])))
* **Auxiliary Space:** O(1)

---

## Tags

* Binary Search
* Arrays

---

## Related Companies

* Bloomberg
* Amazon
* Microsoft
* Walmart
* Adobe
* Arcesium
* Uber

---

## Related Articles

* [Koko Eating Bananas – GeeksforGeeks](https://www.geeksforgeeks.org/koko-eating-bananas/)

---

Here is the **text explanation**, a **step-by-step dry run**, and complete solutions in **Python**, **C++**, and **JavaScript** using **binary search** to solve the **Koko Eating Bananas** problem.

---

## 🔍 Problem Summary

Koko can eat bananas from one pile per hour. If she eats `s` bananas per hour:

* If a pile has ≥ `s`, she eats `s` bananas.
* If a pile has < `s`, she eats the entire pile.

We need to find the **minimum possible value of `s`** such that she can finish all banana piles in `≤ k` hours.

---

## 💡 Approach (Binary Search on Answer)

* Search range: from `1` to `max(arr)`
* At each `mid = s`, compute **total hours** needed to eat all bananas.

  * Use `ceil(pile / s)` per pile (or `(pile + s - 1) // s` for integers).
* If hours ≤ `k`, try smaller `s`.
* Else, increase `s`.

---

## 🧮 Dry Run Example

### Input:

```python
arr = [5, 10, 3], k = 4
```

### Step-by-Step:

1. **Search range:** `lo = 1`, `hi = 10` (max(arr))
2. Try `mid = 5`

   * Hours = ⌈5/5⌉ + ⌈10/5⌉ + ⌈3/5⌉ = 1 + 2 + 1 = 4
   * Valid ⇒ try smaller → `hi = 4`
3. Try `mid = 2`

   * Hours = 3 + 5 + 2 = 10 > 4 ⇒ `lo = 3`
4. Try `mid = 3`

   * Hours = 2 + 4 + 1 = 7 > 4 ⇒ `lo = 4`
5. Try `mid = 4`

   * Hours = 2 + 3 + 1 = 6 > 4 ⇒ `lo = 5`

✅ Found minimum `s = 5`

---

## ✅ Python Code

```python
# User function Template for python3

class Solution:
    def kokoEat(self, arr, k):
        from math import ceil

        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in arr)

        low, high = 1, max(arr)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if hours_needed(mid) <= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int hoursNeeded(vector<int>& arr, int s) {
        int hours = 0;
        for (int pile : arr) {
            hours += (pile + s - 1) / s;  // ceil division
        }
        return hours;
    }

    int kokoEat(vector<int>& arr, int k) {
        int low = 1, high = *max_element(arr.begin(), arr.end());
        int ans = high;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (hoursNeeded(arr, mid) <= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    kokoEat(arr, k) {
        const hoursNeeded = (s) => {
            let hours = 0;
            for (let pile of arr) {
                hours += Math.ceil(pile / s);
            }
            return hours;
        };

        let low = 1;
        let high = Math.max(...arr);
        let answer = high;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (hoursNeeded(mid) <= k) {
                answer = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return answer;
    }
}
```

---

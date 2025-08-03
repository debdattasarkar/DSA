
---

# Majority Element

**Difficulty:** Medium
**Accuracy:** 27.82%
**Submissions:** 728K+
**Points:** 4
**Average Time:** 59m

---

## Problem Statement

Given an array `arr[]`, find the **majority element** in the array.
If no majority element exists, return `-1`.

**Note:**
A majority element in an array is an element that appears **strictly more than** `arr.size()/2` times in the array.

---

## Examples

### Example 1:

**Input:**
`arr[] = [1, 1, 2, 1, 3, 5, 1]`
**Output:** `1`
**Explanation:**
Since 1 is present more than 7/2 times, so it is the majority element.

---

### Example 2:

**Input:**
`arr[] = [7]`
**Output:** `7`
**Explanation:**
Since 7 is a single element and present more than 1/2 times, so it is the majority element.

---

### Example 3:

**Input:**
`arr[] = [2, 13]`
**Output:** `-1`
**Explanation:**
Since no element is present more than 2/2 times, so there is no majority element.

---

## Constraints:

* `1 ≤ arr.size() ≤ 10^5`
* `0 < arr[i] < 10^5`

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## Topic Tags

`Arrays`, `Searching`, `Greedy`, `Data Structures`, `Algorithms`

---

## Company Tags

`Flipkart`, `Accolite`, `Amazon`, `Microsoft`, `D-E-Shaw`, `Google`, `Nagarro`, `Atlassian`

---

## Related Interview Experiences

* Amazon Interview Experience Set 187 For Sde1
* Accolite Interview Experience Set 3 On Campus
* Microsoft Interview Experience Set 86 On Campus
* Amazon Interview Experience Set 138 Sde 1
* Amazon Interview Experience Set 155 Campus
* Microsoft Interview Set 24

---

## Related Articles

* [Majority Element](https://www.geeksforgeeks.org/majority-element/)

---

## Explanation

### Approach (Boyer-Moore Voting Algorithm):

1. **Step 1** – Initialize:

   * `count = 0`
   * `candidate = None`

2. **Step 2** – First Pass:

   * Traverse the array.
   * If `count == 0`, set `candidate = arr[i]`.
   * If `arr[i] == candidate`, increment `count`.
   * Else, decrement `count`.

3. **Step 3** – Second Pass:

   * Count occurrences of `candidate`.
   * If frequency > n // 2, return candidate.
   * Else, return -1.

### Dry Run for: `[1, 1, 2, 1, 3, 5, 1]`

* Initial `count = 0`, candidate = `None`
* 1 → count = 1, candidate = 1
* 1 → count = 2
* 2 → count = 1
* 1 → count = 2
* 3 → count = 1
* 5 → count = 0
* 1 → count = 1, candidate = 1

Final pass: 1 appears **4 times**, array length is 7 → 7//2 = 3 → 4 > 3 → return 1

---

## Python Code

```python
class Solution:
    def majorityElement(self, arr):
        count = 0
        candidate = None

        # Step 1: Find a candidate using Boyer-Moore
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Step 2: Verify the candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1
```

---

## C++ Code

```cpp
class Solution {
  public:
    int majorityElement(vector<int>& arr) {
        int count = 0, candidate = -1;

        // Step 1: Boyer-Moore Voting
        for (int num : arr) {
            if (count == 0)
                candidate = num;
            count += (num == candidate) ? 1 : -1;
        }

        // Step 2: Verification
        count = 0;
        for (int num : arr)
            if (num == candidate)
                count++;

        return (count > arr.size() / 2) ? candidate : -1;
    }
};
```

---

## JavaScript Code

```javascript
class Solution {
    majorityElement(arr) {
        let count = 0;
        let candidate = null;

        // Step 1: Boyer-Moore
        for (let num of arr) {
            if (count === 0) {
                candidate = num;
            }
            count += (num === candidate) ? 1 : -1;
        }

        // Step 2: Verify
        count = 0;
        for (let num of arr) {
            if (num === candidate) count++;
        }

        return (count > Math.floor(arr.length / 2)) ? candidate : -1;
    }
}
```

---

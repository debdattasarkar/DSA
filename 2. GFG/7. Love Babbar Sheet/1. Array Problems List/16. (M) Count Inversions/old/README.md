
---

# Count Inversions 🧮

**Difficulty:** Medium
**Accuracy:** 16.93%
**Submissions:** 672K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given an array of integers `arr[]`, find the **Inversion Count** in the array.

Two elements `arr[i]` and `arr[j]` form an inversion if `arr[i] > arr[j]` and `i < j`.

**Inversion Count**:
For an array, inversion count indicates how far (or close) the array is from being sorted.

* If the array is already sorted, the inversion count is 0.
* If the array is sorted in the reverse order, then the inversion count is the maximum.

---

## Examples

### Example 1:

```
Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
```

### Example 2:

```
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted, so there is no inversion count.
```

### Example 3:

```
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
```

---

## Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr[i]} \leq 10^4$

---

## Expected Complexities

* **Time Complexity:** $O(n \log n)$
* **Auxiliary Space:** $O(n)$

---

## Company Tags

`Flipkart`, `Amazon`, `Microsoft`, `MakeMyTrip`, `Adobe`, `BankBazaar`, `Myntra`

---

## Topic Tags

`Arrays`, `Divide and Conquer`, `Sorting`, `Data Structures`, `Algorithms`

---

## Related Interview Experiences

* Makemytrip Interview Experience For SDE On Campus
* Flipkart Interview Experience Set 22 For SDE 2

---

## Related Articles

* [Inversion Count In Array Using Merge Sort](https://www.geeksforgeeks.org/counting-inversions/)

---


Here's a complete breakdown in README-style for the problem **"Count Inversions"**, including explanation, dry run, and implementation in Python, C++, and JavaScript with inline comments.

---

# Count Inversions

**Difficulty:** Medium
**Accuracy:** 16.93%
**Points:** 4
**Average Time:** 25m

## Problem Statement

Given an array of integers `arr[]`, find the **Inversion Count** in the array.

Two elements `arr[i]` and `arr[j]` form an inversion if:

```
arr[i] > arr[j] and i < j
```

**Inversion Count** indicates how far an array is from being sorted.

* Already sorted → count = 0
* Reverse sorted → count is maximum

---

### Example 1:

**Input:** `arr = [2, 4, 1, 3, 5]`
**Output:** `3`
**Explanation:**
Inversions:

* (2, 1)
* (4, 1)
* (4, 3)

---

### Example 2:

**Input:** `arr = [2, 3, 4, 5, 6]`
**Output:** `0` (Already sorted)

---

## Constraints:

* `1 ≤ arr.size() ≤ 10⁵`
* `1 ≤ arr[i] ≤ 10⁴`

---

## Expected Complexities:

* **Time:** `O(n log n)`
* **Space:** `O(n)`

---

## 🔍 Step-by-Step Explanation (Optimized using Merge Sort)

1. **Brute Force:** Compare each pair `(i, j)` such that `i < j`. → `O(n²)`
2. **Optimized:** Use **Modified Merge Sort**

   * During merge, if an element from the right half is less than an element in the left half, all remaining elements in the left half are greater (inversion detected).

---

## 🧪 Dry Run

For `arr = [2, 4, 1, 3, 5]`

**Merge Steps:**

* Left: `[2, 4]`, Right: `[1, 3, 5]`
* While merging:

  * Compare 2 and 1 → inversion (2, 1)
  * Compare 4 and 1 → inversion (4, 1)
  * Compare 4 and 3 → inversion (4, 3)

→ Total inversions = 3

---

## ✅ Python Code

```python
class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_split = merge(left, right)
            return merged, inv_left + inv_right + inv_split

        def merge(left, right):
            i = j = inv_count = 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i  # All remaining in left are > right[j]
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        _, count = merge_sort(arr)
        return count
```

---

## ✅ C++ Code

```cpp
class Solution {
public:
    int merge(vector<int>& arr, vector<int>& temp, int left, int mid, int right) {
        int i = left, j = mid, k = left;
        int inv_count = 0;
        while (i <= mid - 1 && j <= right) {
            if (arr[i] <= arr[j]) temp[k++] = arr[i++];
            else {
                temp[k++] = arr[j++];
                inv_count += (mid - i);
            }
        }
        while (i <= mid - 1) temp[k++] = arr[i++];
        while (j <= right) temp[k++] = arr[j++];
        for (i = left; i <= right; i++) arr[i] = temp[i];
        return inv_count;
    }

    int mergeSort(vector<int>& arr, vector<int>& temp, int left, int right) {
        int inv_count = 0;
        if (right > left) {
            int mid = (left + right) / 2;
            inv_count += mergeSort(arr, temp, left, mid);
            inv_count += mergeSort(arr, temp, mid + 1, right);
            inv_count += merge(arr, temp, left, mid + 1, right);
        }
        return inv_count;
    }

    int inversionCount(vector<int>& arr) {
        vector<int> temp(arr.size());
        return mergeSort(arr, temp, 0, arr.size() - 1);
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    inversionCount(arr) {
        const mergeSort = (arr) => {
            if (arr.length <= 1) return [arr, 0];
            let mid = Math.floor(arr.length / 2);
            let [left, invL] = mergeSort(arr.slice(0, mid));
            let [right, invR] = mergeSort(arr.slice(mid));
            let [merged, invSplit] = merge(left, right);
            return [merged, invL + invR + invSplit];
        };

        const merge = (left, right) => {
            let i = 0, j = 0, inv = 0;
            let merged = [];
            while (i < left.length && j < right.length) {
                if (left[i] <= right[j]) merged.push(left[i++]);
                else {
                    merged.push(right[j++]);
                    inv += left.length - i;
                }
            }
            return [merged.concat(left.slice(i)).concat(right.slice(j)), inv];
        };

        return mergeSort(arr)[1];
    }
}
```

---

## 📌 Expected Interview Questions

**Q1. What does an inversion mean in the context of sorting?**
👉 It refers to a pair of indices `(i, j)` such that `i < j` and `arr[i] > arr[j]`.

**Q2. What is the brute-force time complexity?**
👉 `O(n²)`, by checking all pairs.

**Q3. How does merge sort help here?**
👉 It counts inversions during merge by tracking how many elements are skipped from the left array.

**Q4. How would you modify this to return all inversion pairs?**
👉 Instead of just counting, store and return pairs `(arr[i], arr[j])` when `arr[i] > arr[j]`.

**Q5. Can this handle arrays with duplicate elements?**
👉 Yes. Comparisons are based on `<=`, so duplicates are not counted as inversions.

---

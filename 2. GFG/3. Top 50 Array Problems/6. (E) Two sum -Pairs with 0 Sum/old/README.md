# Two Sum - Pairs with 0 Sum

## 📝 Problem Statement

Given an integer array `arr`, return all the **unique pairs** `[arr[i], arr[j]]` such that:

* `i ≠ j`
* `arr[i] + arr[j] == 0`

### 🔎 Note:

* The pairs must be returned in **sorted order**.
* The solution array should also be **sorted**.
* The answer must not contain **any duplicate** pairs.

---

## 📘 Examples

### Example 1:

**Input:**
`arr = [-1, 0, 1, 2, -1, -4]`

**Output:**
`[[-1, 1]]`

**Explanation:**

* arr\[0] + arr\[2] = -1 + 1 = 0
* arr\[2] + arr\[4] = 1 + (-1) = 0
* The distinct pair is `[-1, 1]`.

---

### Example 2:

**Input:**
`arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]`

**Output:**
`[[-6, 6], [-1, 1]]`

**Explanation:**

* The distinct pairs are `[-1, 1]` and `[-6, 6]`.

---

## ✅ Constraints

* `3 ≤ arr.size() ≤ 10⁵`
* `-10⁵ ≤ arr[i] ≤ 10⁵`

---

## 💡 Expected Time and Space Complexity

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## 🏷️ Tags

* Arrays
* Sorting
* Two-pointer Algorithm

---

## 🏢 Company Tags

* Flipkart
* Accolite
* Amazon
* FactSet
* Hike
* MakeMyTrip
* Goldman Sachs
* Adobe
* Salesforce

---

## 📚 Related Interview Experiences

* MakeMyTrip Interview Experience For Software Engineer

---

## 🔗 Related Articles

* [2 Sum: Find All Pairs With Zero Sum](#)
* [Given An Array, Find The Maximum j-i Such That arr\[j\] > arr\[i\]](#)

---
Here’s a **step-by-step explanation**, **dry run**, and full implementations in **Python**, **C++**, and **JavaScript** for the problem “Two Sum – Pairs with 0 Sum”:

---

## 📘 Problem Summary

**Goal**: Find all unique pairs `[arr[i], arr[j]]` such that:

* `arr[i] + arr[j] == 0`
* `i != j`
* Pairs should be **distinct** and sorted

---

## 💡 Step-by-Step Explanation

1. Create a set to store elements of the array.
2. Iterate through each number:

   * If `-num` is present in the set, store the pair `[-abs(num), abs(num)]` (to maintain sorted and unique pair format).
   * Add the number to a set to mark it as seen.
3. Use another set to ensure pairs are unique.
4. Return all pairs sorted in lexicographical order.

---

## 🧮 Dry Run

Input: `arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]`

1. Seen = {}, Result = {}
2. Check `6`, `-6` not seen.
3. Check `1`, `-1` not seen.
4. Check `-6`, `6` is seen → Add `[-6, 6]`
5. Check `-1`, `1` is seen → Add `[-1, 1]`
6. Skip duplicates

Final output: `[[-6, 6], [-1, 1]]`

---

## 🐍 Python Code

```python
class Solution:
    def getPairs(self, arr):
        seen = set()
        result = set()

        for num in arr:
            if -num in seen:
                result.add(tuple(sorted((num, -num))))
            seen.add(num)
        
        return sorted([list(pair) for pair in result])
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    vector<vector<int>> getPairs(vector<int>& arr) {
        unordered_set<int> seen;
        set<pair<int, int>> result;

        for (int num : arr) {
            if (seen.count(-num)) {
                int a = min(num, -num);
                int b = max(num, -num);
                result.insert({a, b});
            }
            seen.insert(num);
        }

        vector<vector<int>> output;
        for (auto& p : result) {
            output.push_back({p.first, p.second});
        }
        return output;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    getPairs(arr) {
        const seen = new Set();
        const result = new Set();

        for (let num of arr) {
            if (seen.has(-num)) {
                let a = Math.min(num, -num);
                let b = Math.max(num, -num);
                result.add(`${a},${b}`);
            }
            seen.add(num);
        }

        let output = [];
        for (let pair of result) {
            output.push(pair.split(',').map(Number));
        }

        output.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
        return output;
    }
}
```

---


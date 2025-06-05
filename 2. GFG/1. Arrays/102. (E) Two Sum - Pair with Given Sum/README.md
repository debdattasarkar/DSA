# 🧮 Two Sum - Pair with Given Sum
## 📝 Problem Statement

Given an array `arr[]` of positive integers and another integer `target`, determine if there exist two distinct indices such that the sum of their elements is equal to the target.

## 📥 Input

* `arr[]`: Array of positive integers
* `target`: A positive integer

## 🎯 Output

* Return `true` if such a pair exists, otherwise return `false`.

## ✅ Examples

### Example 1:

```
Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16  
Output: true  
Explanation: arr[3] + arr[4] = 6 + 10 = 16
```

### Example 2:

```
Input: arr[] = [1, 2, 4, 3, 6], target = 11  
Output: false  
Explanation: None of the pair makes a sum of 11.
```

### Example 3:

```
Input: arr[] = [11], target = 11  
Output: false  
Explanation: No pair is possible as only one element is present in arr[].
```

## 🔍 Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr[i]} \leq 10^5$
* $1 \leq \text{target} \leq 2 \times 10^5$

## ⏱️ Expected Time and Space Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 💡 Approach

1. Initialize an empty hash set.
2. Traverse the array.
3. For each element `x`, check if `target - x` exists in the set.
4. If yes, return `true`.
5. Else, add `x` to the set.
6. After the loop, return `false`.

---

## 👨‍💻 Code Implementations

### 🐍 Python

```python
class Solution:
    def hasPairWithSum(self, arr, target):
        seen = set()
        for num in arr:
            if target - num in seen:
                return True
            seen.add(num)
        return False
```

---

### 💻 C++

```cpp
class Solution {
  public:
    bool hasPairWithSum(vector<int>& arr, int target) {
        unordered_set<int> seen;
        for (int num : arr) {
            if (seen.count(target - num))
                return true;
            seen.insert(num);
        }
        return false;
    }
};
```

---

### 🌐 JavaScript

```javascript
class Solution {
    hasPairWithSum(arr, target) {
        let seen = new Set();
        for (let num of arr) {
            if (seen.has(target - num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
```

---

## 🏷️ Tags

`Arrays`, `Hash`, `Data Structures`

---

## 🏢 Company Tags

Zoho, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft, FactSet, Hike, Adobe, Google, Wipro, SAP Labs, CarWale

---

## 📚 Related Articles

* [Check If Pair With Given Sum Exists In Array](https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/)
* [Two Pointers Technique](https://www.geeksforgeeks.org/two-pointers-technique/)

---

Here is the **text explanation with a step-by-step dry run** and code for Python, C++, and JavaScript to solve the **Two Sum - Pair with Given Sum** problem.

---

## 🧠 Text Explanation

### Problem:

Given an array `arr[]` of positive integers and an integer `target`, determine if there exist **two distinct indices** such that the sum of their elements is equal to `target`.

---

## 🪜 Step-by-Step Dry Run

### Input:

```python
arr = [1, 4, 45, 6, 10, 8], target = 16
```

### Dry Run (Using Hashing):

1. Initialize an empty set `seen = {}`.
2. Iterate through the array:

   * `i=0`: `num=1`, `target-num = 15` → not in set → add `1` → `seen = {1}`
   * `i=1`: `num=4`, `target-num = 12` → not in set → add `4` → `seen = {1, 4}`
   * `i=2`: `num=45`, `target-num = -29` → not in set → add `45` → `seen = {1, 4, 45}`
   * `i=3`: `num=6`, `target-num = 10` → not in set → add `6` → `seen = {1, 4, 6, 45}`
   * `i=4`: `num=10`, `target-num = 6` → `6` is in `seen` → ✅ found pair `(6, 10)`

### Output:

```python
True
```

---

## ✅ Python Code

```python
#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for num in arr:
            if target - num in seen:
                return True  # Pair found
            seen.add(num)
        return False  # No pair found
```

---

## ✅ C++ Code

```cpp
// User function template for C++
class Solution {
  public:
    bool twoSum(vector<int>& arr, int target) {
        unordered_set<int> seen;
        for (int num : arr) {
            if (seen.count(target - num)) {
                return true; // Pair found
            }
            seen.insert(num);
        }
        return false; // No pair found
    }
};
```

---

## ✅ JavaScript Code

```javascript
// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {boolean}
 */
class Solution {
    twoSum(arr, target) {
        const seen = new Set();
        for (const num of arr) {
            if (seen.has(target - num)) {
                return true; // Pair found
            }
            seen.add(num);
        }
        return false; // No pair found
    }
}
```

---
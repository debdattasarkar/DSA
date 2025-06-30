
---

# 🧩 Problem: Value Equal to Index Value

**Difficulty:** Basic
**Accuracy:** 54.83%
**Submissions:** 228K+
**Points:** 1
**Average Time:** 20m

---

## 📝 Problem Statement

Given an array `arr`, your task is to find the elements whose value is equal to that of their index value (**1-based indexing**).

🔸 **Note:**
There can be more than one element in the array which have the same value as their index. You need to include **every such element's index** in the output.

---

## 🔍 Examples

### Example 1:

```
Input: arr[] = [15, 2, 45, 4, 7]
Output: [2, 4]
Explanation: 
  arr[2] = 2 ✅
  arr[4] = 4 ✅
```

### Example 2:

```
Input: arr[] = [1]
Output: [1]
Explanation:
  arr[1] = 1 ✅
```

---

## 📌 Constraints

* $1 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr}[i] \leq 10^6$

---

## ✅ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(k) — where `k` is the count of matched indices.

---

## 🏷️ Tags

* Arrays
* Searching
* Data Structures
* Algorithms

---

## 🏢 Company Tags

* Flipkart
* Amazon
* FactSet
* Hike

---

## 📚 Related Articles

* [Find A Fixed Point In A Given Array](https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/)

---

## 👨‍💼 Related Interview Experiences

* Flipkart Interview Experience Set 3

---
🎯 **"Value equal to index value"** problem.

---

# 🧠 **Problem Summary**:
Given an array **`arr[]`**, return **all indices** `i` such that:

```plaintext
arr[i] == i
```

⚠️ **1-based indexing**, meaning `arr[1]` corresponds to index 1 (not 0).

---

# ✅ Example:
```plaintext
Input:  arr[] = [15, 2, 45, 4, 7]
                ↑  ↑       ↑
1-based index:  1  2  3  4  5

Output: [2, 4]
Because: arr[2] == 2, arr[4] == 4
```

---

# 🚀 Efficient Approach:
### Time Complexity: `O(n)`  
- Loop from `i = 0` to `n-1`
- If `arr[i] == i + 1`, add `(i+1)` to result

### Auxiliary Space: `O(k)` (where `k` is number of matches)

---

# 🔧 C++ Implementation:

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> valueEqualToIndex(const vector<int>& arr) {
    vector<int> result;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == i + 1) {
            result.push_back(i + 1); // 1-based index
        }
    }
    return result;
}

int main() {
    vector<int> arr = {15, 2, 45, 4, 7};
    vector<int> res = valueEqualToIndex(arr);
    for (int i : res) {
        cout << i << " ";
    }
    return 0;
}
```

---

# 🐍 Python Version:

```python
def value_equal_to_index(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == i + 1:  # 1-based index
            result.append(i + 1)
    return result

# Example usage
arr = [15, 2, 45, 4, 7]
print(value_equal_to_index(arr))  # Output: [2, 4]
```

---

# 🌐 JavaScript Version:

```javascript
function valueEqualToIndex(arr) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === i + 1) {
            result.push(i + 1);
        }
    }
    return result;
}

// Example
let arr = [15, 2, 45, 4, 7];
console.log(valueEqualToIndex(arr)); // Output: [2, 4]
```

---

# ✅ Interview Insights:
- **Easy-level** but **frequently asked** for warm-up.
- Great for practicing:
  - **Indexing logic**
  - **Array traversal**
  - **Understanding 1-based vs 0-based indexing**

---

Want to try solving this inside your `ArrayManager` class for each language?  
I can guide you to add a `getMatchingIndices()` method in C++, Python, and JS!

👉 Want to do that?

---
OOPs
---
🎯 Oh yesss! Let’s plug this interview-ready logic right into your OOP skills!  
We’ll add a method in your `ArrayManager` class called:

```cpp
getMatchingIndices()
```

It will:
- Traverse the array
- Check if `arr[i] == i + 1`
- Return a list of such **1-based indices**

Let’s do it **one language at a time** — starting with **C++**, then Python, then JavaScript.

---

# 🔧 C++: Add to `ArrayManager`

### ✨ Add this method inside the class:

```cpp
vector<int> getMatchingIndices() {
    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (arr[i] == i + 1) {
            result.push_back(i + 1); // 1-based index
        }
    }
    return result;
}
```

### ✅ In `main()`:

```cpp
vector<int> matchIndices = am.getMatchingIndices();
cout << "Indices where arr[i] == i (1-based): ";
for (int idx : matchIndices) {
    cout << idx << " ";
}
cout << endl;
```

---

# 🐍 Python: Add to `ArrayManager`

### ✨ Add this method to the class:

```python
def get_matching_indices(self):
    return [i + 1 for i in range(len(self.arr)) if self.arr[i] == i + 1]
```

### ✅ In `main()`:

```python
matches = am.get_matching_indices()
print("Indices where arr[i] == i (1-based):", matches)
```

---

# 🌐 JavaScript: Add to `ArrayManager`

### ✨ Add this method to the class:

```javascript
getMatchingIndices() {
    let result = [];
    for (let i = 0; i < this.arr.length; i++) {
        if (this.arr[i] === i + 1) {
            result.push(i + 1); // 1-based index
        }
    }
    return result;
}
```

### ✅ In `main()`:

```javascript
let matches = am.getMatchingIndices();
console.log("Indices where arr[i] == i (1-based):", matches);
```

---

# 🏁 Sample Input:

Try this common test case in your `insert()` calls:

```
[15, 2, 45, 4, 7]
```

✅ Output should be:
```
[2, 4]
```

---

Comprehensive breakdown of the **“Value Equal to Index Value”** problem including:

---

## ✅ 1. Text Explanation with Step-by-Step Dry Run

### 🧠 Problem:

Find all indices `i` such that `arr[i] == i` (**1-based indexing**).

### 🧾 Key Point:

Use **1-based index** comparison: check if `arr[i - 1] == i` while looping.

---

### 🔄 Dry Run

For example:

```python
arr = [15, 2, 45, 4, 7]
         ↑  ↑      ↑
Index:   1  2  3  4  5
```

**Loop iteration:**

| i (1-based) | arr\[i-1] | Check   | Match? |
| ----------- | --------- | ------- | ------ |
| 1           | 15        | 15 == 1 | ❌      |
| 2           | 2         | 2 == 2  | ✅      |
| 3           | 45        | 45 == 3 | ❌      |
| 4           | 4         | 4 == 4  | ✅      |
| 5           | 7         | 7 == 5  | ❌      |

**Output:** `[2, 4]`

---

## ✅ 2. Optimized Python Solution (Expected in Interviews)

```python
class Solution:
    def valueEqualToIndex(self, arr):
        result = []
        for i in range(1, len(arr) + 1):
            if arr[i - 1] == i:
                result.append(i)
        return result

# Example Usage
arr = [15, 2, 45, 4, 7]
sol = Solution()
print(sol.valueEqualToIndex(arr))  # Output: [2, 4]
```

### ⏱️ Time & Space Complexity:

* **Time:** O(n)
* **Space:** O(k), where `k` is number of matched indices

---

## ✅ 3. Common Interview Questions & Answers

### 🔹 Q1: What is the time complexity of your solution?

**A:** It is **O(n)** since we iterate through the array once.

---

### 🔹 Q2: How does 1-based indexing affect your logic?

**A:** Normally array indices are 0-based. But since the problem uses 1-based indexing, we compare `arr[i - 1] == i` during iteration.

---

### 🔹 Q3: Can the array be sorted? Would that help?

**A:** The array can be unsorted. Sorting would not help since we need to maintain original positions to match with their 1-based indices.

---

### 🔹 Q4: What happens if there are duplicates?

**A:** Duplicates don’t affect correctness since we are matching values to index positions individually.

---

### 🔹 Q5: How would you solve it using list comprehension in Python?

**A:**

```python
[i for i in range(1, len(arr) + 1) if arr[i - 1] == i]
```

---

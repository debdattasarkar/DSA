
---

# 🧮 Type of Array

**Difficulty:** Basic
**Accuracy:** 21.55%
**Submissions:** 28K+
**Points:** 1

---

### 🧾 Problem Statement

You are given an array `arr[]` having **unique elements**. Your task is to return the **type of array**.

> **Note:** The array can be categorized into:

* **Ascending**
* **Descending**
* **Descending Rotated**
* **Ascending Rotated**

Return:

* `1` if the array is in **ascending order**
* `2` if the array is in **descending order**
* `3` if the array is in **descending rotated order**
* `4` if the array is in **ascending rotated order**

---

### 🧪 Examples

#### Example 1:

```
Input: arr[] = [2, 1, 5, 4, 3]
Output: 3
Explanation: Descending rotated, rotate 2 times left.
```

#### Example 2:

```
Input: arr[] = [3, 4, 5, 1, 2]
Output: 4
Explanation: Ascending rotated, rotate 2 times right.
```

---

### 📌 Constraints:

* $3 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr[i]} \leq 10^6$

---

### 💡 Expected Complexities:

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

### 🏷️ Company Tags:

* Amazon

---

### 🧵 Topic Tags:

* Arrays
* Data Structures

---

### 📚 Related Articles:

* [Type Array Maximum Element](#)

---
Thanks! This is the **"Type of Array"** classification problem.

---
Here's a Python function that implements the logic described for identifying the type of array:

```python
def type_of_array(arr):
    n = len(arr)
    count_increases = 0
    count_decreases = 0

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            count_increases += 1
        elif arr[i] > arr[i + 1]:
            count_decreases += 1

    if count_decreases == 0:
        return 1  # Ascending
    elif count_increases == 0:
        return 2  # Descending
    elif count_decreases == 1 and arr[-1] < arr[0]:
        return 4  # Ascending Rotated
    elif count_increases == 1 and arr[-1] > arr[0]:
        return 3  # Descending Rotated
    else:
        return -1  # Not a valid input for the defined categories (just in case)
```

### Example usage:
```python
print(type_of_array([2, 1, 5, 4, 3]))  # Output: 3 (Descending Rotated)
print(type_of_array([3, 4, 5, 1, 2]))  # Output: 4 (Ascending Rotated)
print(type_of_array([1, 2, 3, 4]))     # Output: 1 (Ascending)
print(type_of_array([9, 7, 3, 1]))     # Output: 2 (Descending)
```

Would you like a version with inline comments to explain each step?

---

Certainly! Below are the **Python**, **JavaScript**, and **C++** implementations of the solution, each with inline comments to explain the logic clearly.

---

### ✅ Python Code (with comments):
```python
def type_of_array(arr):
    n = len(arr)
    count_increases = 0
    count_decreases = 0

    # Count increases and decreases between adjacent elements
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            count_increases += 1
        elif arr[i] > arr[i + 1]:
            count_decreases += 1

    # Check for ascending
    if count_decreases == 0:
        return 1
    # Check for descending
    elif count_increases == 0:
        return 2
    # Check for ascending rotated: one drop and last element < first
    elif count_decreases == 1 and arr[-1] < arr[0]:
        return 4
    # Check for descending rotated: one rise and last element > first
    elif count_increases == 1 and arr[-1] > arr[0]:
        return 3
    else:
        return -1  # Not matching any defined type
```

---

### ✅ JavaScript Code (with comments):
```javascript
function typeOfArray(arr) {
    const n = arr.length;
    let countIncreases = 0;
    let countDecreases = 0;

    // Count increasing and decreasing pairs
    for (let i = 0; i < n - 1; i++) {
        if (arr[i] < arr[i + 1]) {
            countIncreases++;
        } else if (arr[i] > arr[i + 1]) {
            countDecreases++;
        }
    }

    // Classify based on the counts
    if (countDecreases === 0) {
        return 1; // Ascending
    } else if (countIncreases === 0) {
        return 2; // Descending
    } else if (countDecreases === 1 && arr[n - 1] < arr[0]) {
        return 4; // Ascending Rotated
    } else if (countIncreases === 1 && arr[n - 1] > arr[0]) {
        return 3; // Descending Rotated
    } else {
        return -1; // Undefined type
    }
}
```

---

### ✅ C++ Code (with comments):
```cpp
#include <iostream>
#include <vector>
using namespace std;

int typeOfArray(vector<int>& arr) {
    int n = arr.size();
    int countIncreases = 0, countDecreases = 0;

    // Count increasing and decreasing adjacent elements
    for (int i = 0; i < n - 1; ++i) {
        if (arr[i] < arr[i + 1])
            countIncreases++;
        else if (arr[i] > arr[i + 1])
            countDecreases++;
    }

    // Check types
    if (countDecreases == 0)
        return 1; // Ascending
    else if (countIncreases == 0)
        return 2; // Descending
    else if (countDecreases == 1 && arr[n - 1] < arr[0])
        return 4; // Ascending Rotated
    else if (countIncreases == 1 && arr[n - 1] > arr[0])
        return 3; // Descending Rotated
    else
        return -1; // Invalid input
}

int main() {
    vector<int> arr = {3, 4, 5, 1, 2};  // Example
    cout << typeOfArray(arr) << endl;   // Output: 4
    return 0;
}
```

---

### ✅ Problem: **Type of Array**

Given an array `arr[]` of unique elements, identify whether the array is:

1. **Strictly Ascending** → Return 1
2. **Strictly Descending** → Return 2
3. **Descending Rotated** (e.g. rotated descending sorted array) → Return 3
4. **Ascending Rotated** (e.g. rotated ascending sorted array) → Return 4

---

### 🧠 Text Explanation with Step-by-Step Dry Run

#### Example:

```
Input: arr = [3, 4, 5, 1, 2]
```

#### Step-by-Step:

* Check if it is strictly ascending:

  * 3 < 4 < 5 → okay
  * 5 > 1 → break → not strictly ascending → ❌

* Check if it is strictly descending:

  * 3 > 4 → ❌

* Count how many "drops" (i.e., `arr[i] > arr[i+1]`) exist:

  * 3 < 4 → fine
  * 4 < 5 → fine
  * 5 > 1 → **drop 1**
  * 1 < 2 → fine

* Only **1 drop**, and it’s in a rotated fashion → **Ascending Rotated** → ✅ Return 4

#### Output:

```
Output: 4
```

---

#### Dry Run on Another Input:

```
Input: arr = [2, 1, 5, 4, 3]
```

* Ascending? 2 > 1 → ❌

* Descending? 2 > 1 (✅), but 1 < 5 → ❌

* Count drops:

  * 2 > 1 → drop 1
  * 1 < 5 → fine
  * 5 > 4 → drop 2
  * 4 > 3 → drop 3

* Multiple drops → Not ascending/descending rotated

* But **starting part is descending**, so → **Descending Rotated** → ✅ Return 3

#### Output:

```
Output: 3
```

---

### 💬 Interview Questions & Ideal Answers

#### ❓Q1: How would you detect a rotated sorted array?

**✅ A:** Count the number of drops (where `arr[i] > arr[i+1]`).

* If exactly one drop: rotated array
* If no drop: sorted
* More than one: not sorted or rotated sorted

#### ❓Q2: Can we solve this in constant space?

**✅ A:** Yes, we only need a few counters and flags, making auxiliary space O(1).

#### ❓Q3: Why is ascending rotated \[3,4,5,1,2] not just random?

**✅ A:** Because there is a pattern: a strictly increasing array rotated once.
This ensures a single place where `arr[i] > arr[i+1]`, which is the pivot.

#### ❓Q4: How do you distinguish between rotated ascending vs descending?

**✅ A:** Check the original head/tail comparison:

* Ascending rotated: smaller values come after larger ones
* Descending rotated: larger values come after smaller ones, early

#### ❓Q5: Can binary search help in this?

**✅ A:** If array was guaranteed to be rotated sorted, we could use binary search to find the pivot in O(log n). But here we’re just classifying — O(n) is enough.

---

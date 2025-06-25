Here is the complete README-style documentation based on the problem statement in your image:

---

# 📘 Absolute Difference of 1

### Difficulty: Basic

**Accuracy:** 24.14%
**Submissions:** 23K+
**Points:** 1

---

## 📝 Problem Statement

Given an array `arr[]`, return all the numbers **less than `k`** and:

* The number must have **at least two digits**.
* The **absolute difference between every adjacent digit** of the number must be **1**.

If **no such number** is present, return an **empty list**.

---

## 🧠 Examples

### Example 1:

```
Input:
arr[] = [7, 98, 56, 43, 45, 23, 12, 8]
k = 54

Output:
[43, 45, 23, 12]

Explanation:
43, 45, 23, 12 all have adjacent digits with absolute difference = 1 and are < 54.
```

---

### Example 2:

```
Input:
arr[] = [87, 89, 45, 235, 465, 765, 123, 987, 499, 655]
k = 1000

Output:
[87, 89, 45, 765, 123, 987]

Explanation:
87, 89, 45, 765, 123, 987 all have adjacent digits diff = 1 and are < 1000.
```

---

## 📊 Constraints:

* `1 <= arr.size() <= 10^6`
* `1 <= k, arr[i] <= 10^6`

---

## ⏱️ Expected Complexities:

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Company Tags:

* Amazon
* Jabong

---

## 🧩 Topic Tags:

* Arrays
* Data Structures

---

## 📚 Related Articles:

* **Check If Frequency Of All Characters Can Become Same By One Removal**

Here's a **text explanation with a step-by-step dry run** for the problem **"Absolute Difference of 1"**:

---

## 🔍 Problem Summary

Given:

* An array `arr[]` of **positive integers**.
* A number `k`.

Your task:

* Find all numbers **less than `k`**,
* That have **at least 2 digits**,
* And the **absolute difference between every adjacent digit is 1**.

---

## ✅ Conditions to Include a Number

For a number `num`:

* `num < k`
* `num >= 10` (i.e., has at least 2 digits)
* For all pairs of adjacent digits in `num`, `|digit[i] - digit[i+1]| == 1`

---

## 🪜 Step-by-Step Logic

1. Initialize an empty result list: `res = []`
2. Iterate over each number `num` in the array:

   * Skip if `num >= k` or `num < 10`.
   * Extract digits one by one (e.g., via string or modulus method).
   * Compare each pair of adjacent digits.
   * If all pairs have absolute difference = 1 → add to `res`.

---

## 🧪 Dry Run Example

**Input:**

```python
arr = [87, 89, 45, 765, 123, 987, 499, 655]
k = 1000
```

We'll process each number:

| Number | < k? | ≥10? | Adjacent Digits | Absolute Differences | Valid? |         |       |         |   |
| ------ | ---- | ---- | --------------- | -------------------- | ------ | ------- | ----- | ------- | - |
| 87     | ✅    | ✅    | 8 and 7         |                      | 8 - 7  | = 1     | ✅     |         |   |
| 89     | ✅    | ✅    | 8 and 9         |                      | 8 - 9  | = 1     | ✅     |         |   |
| 45     | ✅    | ✅    | 4 and 5         |                      | 4 - 5  | = 1     | ✅     |         |   |
| 765    | ✅    | ✅    | 7-6-5           |                      | 7 - 6  | = 1,    | 6 - 5 | = 1     | ✅ |
| 123    | ✅    | ✅    | 1-2-3           |                      | 1 - 2  | = 1,    | 2 - 3 | = 1     | ✅ |
| 987    | ✅    | ✅    | 9-8-7           |                      | 9 - 8  | = 1,    | 8 - 7 | = 1     | ✅ |
| 499    | ✅    | ✅    | 4-9-9           |                      | 4 - 9  | = 5 → ❌ | ❌     |         |   |
| 655    | ✅    | ✅    | 6-5-5           |                      | 6 - 5  | = 1,    | 5 - 5 | = 0 → ❌ | ❌ |

**Output:** `[87, 89, 45, 765, 123, 987]`

---

## 💡 Final Notes

* This problem tests digit-wise reasoning.
* Focuses on `mod`, `//`, and `string` handling.
* Efficient due to low digit count per number (log₁₀(n) ≤ 7).


---

## ✅ Problem Summary

You're given:

* An array `arr[]` of numbers
* A threshold `k`

Your task is to:

1. Return all numbers in `arr[]` that are:

   * **Less than `k`**
   * Have **at least two digits**
   * And every pair of **adjacent digits** in the number has an **absolute difference of 1**

If no such number exists, return an **empty list**.

---

## 🧪 Example

### Input:

```plaintext
arr = [7, 98, 56, 43, 45, 23, 12, 8]
k = 54
```

### Output:

```plaintext
[43, 45, 23, 12]
```

### Why?

All these:

* Are < 54
* Have ≥ 2 digits
* And satisfy: `|4 - 3| = 1`, `|2 - 3| = 1`, etc.

---

## 🧠 Logic

For each number in the array:

1. Check if `num < k`
2. Check if the number has at least 2 digits (i.e. `num >= 10`)
3. For each adjacent digit pair: `|digit[i] - digit[i+1]| == 1`

---

Great! Below are full working implementations in **Python**, **C++**, and **JavaScript** for the "Absolute Difference of 1" problem — each with **detailed inline comments** to explain the logic at every step.

---

## 🐍 Python – Full Code with Comments

```python
def is_adjacent_diff_one(num):
    # Convert number to string to access digits
    digits = str(num)
    
    # Loop through adjacent digits and check their absolute difference
    for i in range(len(digits) - 1):
        if abs(int(digits[i]) - int(digits[i + 1])) != 1:
            return False  # If any pair fails, it's not valid
    return True  # All adjacent pairs passed


def filter_numbers(arr, k):
    result = []
    for num in arr:
        if num < k and num >= 10 and is_adjacent_diff_one(num):
            result.append(num)
    return result


# 🧪 Test
arr = [7, 98, 56, 43, 45, 23, 12, 8]
k = 54
print("Output:", filter_numbers(arr, k))  # ✅ Output: [43, 45, 23, 12]
```

---

## 🧑‍💻 C++ – Full Code with Comments

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Function to check if all adjacent digits differ by 1
bool isAdjacentDiffOne(int num) {
    string s = to_string(num);
    for (int i = 0; i < s.size() - 1; ++i) {
        if (abs(s[i] - s[i + 1]) != 1) {
            return false;
        }
    }
    return true;
}

// Main filter function
vector<int> filterNumbers(vector<int>& arr, int k) {
    vector<int> result;
    for (int num : arr) {
        if (num < k && num >= 10 && isAdjacentDiffOne(num)) {
            result.push_back(num);
        }
    }
    return result;
}

int main() {
    vector<int> arr = {7, 98, 56, 43, 45, 23, 12, 8};
    int k = 54;

    vector<int> output = filterNumbers(arr, k);
    cout << "Output: ";
    for (int x : output) cout << x << " ";
    cout << endl;

    return 0;
}
```

---

## 🌐 JavaScript – Full Code with Comments

```javascript
function isAdjacentDiffOne(num) {
    let digits = num.toString();
    for (let i = 0; i < digits.length - 1; i++) {
        if (Math.abs(parseInt(digits[i]) - parseInt(digits[i + 1])) !== 1) {
            return false;
        }
    }
    return true;
}

function filterNumbers(arr, k) {
    let result = [];

    for (let num of arr) {
        if (num < k && num >= 10 && isAdjacentDiffOne(num)) {
            result.push(num);
        }
    }

    return result;
}

// 🧪 Test
let arr = [7, 98, 56, 43, 45, 23, 12, 8];
let k = 54;
console.log("Output:", filterNumbers(arr, k));  // ✅ Output: [43, 45, 23, 12]
```

---

## ✅ Time and Space Complexity

| Metric           | Value      |                                                             |
| ---------------- | ---------- | ----------------------------------------------------------- |
| Time Complexity  | O(n × d)   | `n` = number of elements, `d` = digits per number (≈ 6 max) |
| Space Complexity | O(1) extra | Except for output list                                      |

---

Certainly! Here are the **interview-style questions and answers** that are commonly expected around the problem: **“Absolute Difference of 1”** (as shown in your image).

---

### ✅ **1. What is the key logic behind the problem?**

**Answer:**
We need to find all numbers in the array that:

* Are **less than `k`**,
* Have **at least two digits** (i.e., ≥10),
* Have all **adjacent digits with absolute difference of 1**.

For example, in 45: `|4 - 5| = 1`, which satisfies the condition.

---

### ✅ **2. What is the time complexity of your approach? Can it handle 10⁶ elements?**

**Answer:**
Yes, it can handle up to 10⁶ elements.

* Time complexity: **O(n \* d)**, where `d` is the number of digits (max 7 for 10⁶), so practically **O(n)**.
* Space complexity: **O(1)** auxiliary (not counting output list).

---

### ✅ **3. How do you check if adjacent digits of a number differ by exactly 1?**

**Answer:**
We extract digits one by one and compare:

* For number 123: check `|1-2| = 1`, then `|2-3| = 1`.
* If all adjacent digit differences are 1, return `True`.

---

### ✅ **4. What edge cases do you handle?**

**Answer:**

* Numbers with **only one digit**: skip them.
* Numbers **≥ k**: skip them.
* **Empty array**: return empty list.
* **All values fail conditions**: still return empty list.

---

### ✅ **5. Can we optimize digit comparison further?**

**Answer:**
Since numbers are ≤ 10⁶, the number of digits is small (≤7). So extracting and comparing digits manually is optimal. Using string conversion can make the code cleaner without hurting performance.

---

### ✅ **6. What if we want to check for absolute difference of 2 instead of 1?**

**Answer:**
Just replace `abs(d1 - d2) == 1` with `abs(d1 - d2) == 2` in the logic. The algorithm structure remains the same.

---

### ✅ **7. Why is this problem tagged with Amazon/Jabong?**

**Answer:**
This is a classic **digit-pattern filtering** problem — useful in validating numeric constraints, often used in **backend validations**, **rule-based systems**, or **data integrity checks**, which are domains Amazon/Jabong may focus on.

---


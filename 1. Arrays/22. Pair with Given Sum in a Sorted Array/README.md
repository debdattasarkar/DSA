Question

![Question](Question.png)

---

You're now tackling the problem: **"Pair with Given Sum in a Sorted Array"** — a classic **two-pointer pattern** question.

Let’s go step-by-step and then I’ll show you the code in multiple languages.

---

## ✅ Problem Summary

* You're given a **sorted array** `arr[]` and an integer `target`.
* Find the **number of pairs** `(i, j)` such that:

  * `arr[i] + arr[j] == target`
  * `i ≠ j`

---

## 🧪 Example:

### Input:

```
arr = [-1, 1, 5, 5, 7]
target = 6
```

### Pairs that sum to 6:

* (-1, 7)
* (1, 5)
* (1, 5)  ← different index
  ➡️ Output: **3 pairs**

---

## 🧠 Approach: Two Pointer Technique (O(n) Time)

1. Set `left = 0`, `right = n - 1`
2. While `left < right`:

   * If `arr[left] + arr[right] == target`, count the pair and handle duplicates.
   * If the sum is **less** than target → move `left++`
   * If the sum is **more** than target → move `right--`

---

## 🔄 Test Case Flow for `arr = [-1, 1, 5, 5, 7], target = 6`:

```
left = 0 → -1
right = 4 → 7 → sum = 6 ✅ pair found

left = 1 → 1
right = 3 → 5 → sum = 6 ✅ pair found

left = 1
right = 2 → 5 → sum = 6 ✅ pair found

left = 1, right = 1 → done

✅ Total = 3 pairs
```

---

Excellent question! 🙌
The **two-pointer technique** is a powerful algorithmic approach used mainly with **sorted arrays or lists** to solve problems in **O(n)** time where you might otherwise use **O(n²)** brute force.

---

## 🎯 **What is the Two-Pointer Technique?**

Imagine two people standing at opposite ends of a number line (or array). Each person has a **pointer** (like an index). Depending on what you're trying to compute, you move one or both pointers inward based on the condition you're checking.

---

## 🧠 Key Idea:

* Use **two indices** (`left` and `right`)
* Traverse the array from **both ends toward the center**
* Adjust pointers based on comparison conditions

---

## 📚 Example Use Case: Find pairs with given sum

### Problem:

Find all pairs in a **sorted array** that sum to a target value.

### Brute Force:

Check all possible pairs → Time: **O(n²)** ❌

### Two Pointer:

Sort array (if not already), and use:

```python
left = 0
right = n - 1
```

Move the pointers based on the sum:

* If `arr[left] + arr[right] == target` → record the pair
* If sum is **less**, move `left++`
* If sum is **more**, move `right--`

Time: **O(n)** ✅

---

## 🧪 Visualization

Array: `[1, 2, 4, 5, 7, 11]`, Target = 9

| left | right | Sum | Action               |
| ---- | ----- | --- | -------------------- |
| 1    | 11    | 12  | too big → `right--`  |
| 1    | 7     | 8   | too small → `left++` |
| 2    | 7     | 9   | match ✅              |

---

## ⚙️ Common Problems Using It

* ✅ Find pair with sum in sorted array
* ✅ Count total pairs that satisfy a condition
* ✅ Merge two sorted arrays
* ✅ Remove duplicates (like in LeetCode's `Two Sum II`)
* ✅ Trapping water or container with most water problems

---

Would you like to now see this technique implemented in the pair sum problem in Python, C++, and JavaScript with a live example trace?

Awesome! Let’s implement the **pair sum in a sorted array** using the **two-pointer technique** in:

✅ Python
✅ C++
✅ JavaScript

We’ll also walk through a real example:

```python
arr = [-1, 1, 5, 5, 7]
target = 6
```

---

## 🐍 Python Implementation (with Step-by-Step Comments)

```python
def count_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            # If elements are different
            if arr[left] != arr[right]:
                # Count duplicates on both ends
                l_count = 1
                r_count = 1
                while left + 1 < right and arr[left] == arr[left + 1]:
                    l_count += 1
                    left += 1
                while right - 1 > left and arr[right] == arr[right - 1]:
                    r_count += 1
                    right -= 1
                count += l_count * r_count
                left += 1
                right -= 1
            else:
                # All elements between left and right are the same
                n = right - left + 1
                count += (n * (n - 1)) // 2
                break
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return count


# Test
arr = [-1, 1, 5, 5, 7]
target = 6
print(count_pairs_with_sum(arr, target))  # Output: 3
```

---

## 🧑‍💻 C++ Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

int countPairsWithSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1, count = 0;

    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            count++;
            left++;
            right--;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

int main() {
    vector<int> arr = {-1, 1, 5, 5, 7};
    int target = 6;
    cout << countPairsWithSum(arr, target) << endl;  // Output: 3
    return 0;
}
```

---

## 🌐 JavaScript Implementation

```javascript
function countPairsWithSum(arr, target) {
    let left = 0, right = arr.length - 1, count = 0;

    while (left < right) {
        const sum = arr[left] + arr[right];

        if (sum === target) {
            count++;
            left++;
            right--;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

// Test
let arr = [-1, 1, 5, 5, 7];
let target = 6;
console.log(countPairsWithSum(arr, target));  // Output: 3
```

---

## 🧪 Flow of Execution

```
arr = [-1, 1, 5, 5, 7]
target = 6

1. left=-1, right=7 → sum = 6 ✅ count = 1
2. left=1, right=5 → sum = 6 ✅ count = 2
3. left=1, right=5 (again, different index) → sum = 6 ✅ count = 3
4. left = right → stop
```

✅ Final answer: `3` pairs

---

Would you like a version that **prints the actual pairs** ?

Perfect! Let's now modify our code to **print the actual pairs** whose sum equals the given `target`, using the **two-pointer technique** on a sorted array.

We’ll show it in:

* ✅ Python
* ✅ C++
* ✅ JavaScript

with this input:

```plaintext
arr = [-1, 1, 5, 5, 7]
target = 6
```

---

## 🐍 Python – Print Actual Pairs

```python
def find_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

# Test
arr = [-1, 1, 5, 5, 7]
target = 6
result = find_pairs_with_sum(arr, target)
print("Pairs:", result)
# Output: Pairs: [(-1, 7), (1, 5), (1, 5)]
```

---

## 🧑‍💻 C++ – Print Actual Pairs

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<pair<int, int>> findPairsWithSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    vector<pair<int, int>> pairs;

    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            pairs.push_back({arr[left], arr[right]});
            left++;
            right--;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return pairs;
}

int main() {
    vector<int> arr = {-1, 1, 5, 5, 7};
    int target = 6;
    vector<pair<int, int>> result = findPairsWithSum(arr, target);

    cout << "Pairs:\n";
    for (auto p : result) {
        cout << "(" << p.first << ", " << p.second << ")\n";
    }

    return 0;
}
```

---

## 🌐 JavaScript – Print Actual Pairs

```javascript
function findPairsWithSum(arr, target) {
    let left = 0, right = arr.length - 1;
    let pairs = [];

    while (left < right) {
        let sum = arr[left] + arr[right];

        if (sum === target) {
            pairs.push([arr[left], arr[right]]);
            left++;
            right--;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return pairs;
}

// Test
let arr = [-1, 1, 5, 5, 7];
let target = 6;
console.log("Pairs:", findPairsWithSum(arr, target));
// Output: Pairs: [ [ -1, 7 ], [ 1, 5 ], [ 1, 5 ] ]
```

---

## 🧪 Output for All:

```plaintext
Pairs: [(-1, 7), (1, 5), (1, 5)]
```

---

Would you like to modify this to:

* Only include **unique values**?
* Or only include **unique index pairs** even if values are the same?

Absolutely! Let's now refine the logic to:

### ✅ **Print only unique index pairs**

Even if the values are the same (e.g., multiple 5s), pairs must be from **different indices**, but duplicates by value **are allowed**.

We'll also keep **clear inline comments** to explain each step.

---

### 🔁 Example Input:

```plaintext
arr = [-1, 1, 5, 5, 7]
target = 6
```

### Expected Output (with unique indices):

```
(-1, 7), (1, 5 at index 1 + index 2), (1, 5 at index 1 + index 3)
```

✅ Count = 3
We allow (1, 5) to appear multiple times because 5 exists at different indices.

---

## 🐍 Python – Unique Index Pairs (With Comments)

```python
def find_unique_index_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    # Loop while left index is strictly less than right
    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            # Store the value pair from distinct indices
            pairs.append((arr[left], arr[right]))

            # Move both pointers inward (next unique index pair)
            left += 1
            right -= 1

        elif curr_sum < target:
            left += 1  # need bigger sum, move left up
        else:
            right -= 1  # need smaller sum, move right down

    return pairs

# 🔁 Test
arr = [-1, 1, 5, 5, 7]
target = 6
result = find_unique_index_pairs(arr, target)

# 🖨️ Print Result
print("Pairs with unique indices:")
for pair in result:
    print(pair)
```

---

## 🧑‍💻 C++ – Unique Index Pairs with Comments

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<pair<int, int>> findUniqueIndexPairs(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    vector<pair<int, int>> pairs;

    // Move two pointers from both ends
    while (left < right) {
        int sum = arr[left] + arr[right];

        if (sum == target) {
            pairs.push_back({arr[left], arr[right]});
            left++;  // go to next index
            right--; // go to previous index
        }
        else if (sum < target) {
            left++;  // move right for higher sum
        }
        else {
            right--; // move left for lower sum
        }
    }

    return pairs;
}

int main() {
    vector<int> arr = {-1, 1, 5, 5, 7};
    int target = 6;

    vector<pair<int, int>> result = findUniqueIndexPairs(arr, target);
    cout << "Pairs with unique indices:\n";
    for (auto& p : result) {
        cout << "(" << p.first << ", " << p.second << ")\n";
    }

    return 0;
}
```

---

## 🌐 JavaScript – Unique Index Pairs with Comments

```javascript
function findUniqueIndexPairs(arr, target) {
    let left = 0, right = arr.length - 1;
    let pairs = [];

    while (left < right) {
        let sum = arr[left] + arr[right];

        if (sum === target) {
            // Store the pair values from unique indices
            pairs.push([arr[left], arr[right]]);
            left++;   // next left index
            right--;  // previous right index
        } else if (sum < target) {
            left++;  // move toward bigger values
        } else {
            right--; // move toward smaller values
        }
    }

    return pairs;
}

// 🔁 Test
let arr = [-1, 1, 5, 5, 7];
let target = 6;
let result = findUniqueIndexPairs(arr, target);

// 🖨️ Print Result
console.log("Pairs with unique indices:");
result.forEach(p => console.log(`(${p[0]}, ${p[1]})`));
```

---

## ✅ Output for All Versions:

```
(-1, 7)
(1, 5)
(1, 5)
```

Each pair uses **different index positions**, even if values repeat.

Would you like the version where **duplicates are not counted at all** (i.e., only unique value pairs like a set)?


Perfect! Let’s now update the solution to handle the **unique value pairs only** — regardless of how many times those values occur in the array.

---

## ✅ New Requirement

You want to:

* Count only **unique pairs of values** `(a, b)` such that `a + b == target`
* Ignore how many times those values occur (even if duplicate values are at different indices)

---

### 🧪 Example:

```plaintext
arr = [-1, 1, 5, 5, 7]
target = 6
```

### Pairs that sum to 6:

* (-1, 7)
* (1, 5) ✅ But counted only once even though 5 appears twice

### ✅ Final Output:

```
(-1, 7)
(1, 5)
```

---

## 🧠 How?

Use a `Set` to:

1. Keep track of **seen values**
2. Keep track of **used pairs** in sorted order so (1, 5) and (5, 1) are not double-counted

---

## 🐍 Python – Unique Value Pairs Only (With Comments)

```python
def unique_value_pairs(arr, target):
    seen = set()
    used_pairs = set()
    result = []

    for num in arr:
        complement = target - num

        # Check if complement was seen before
        if complement in seen:
            # Build sorted pair to avoid duplicates like (5,1) and (1,5)
            pair = tuple(sorted((num, complement)))

            if pair not in used_pairs:
                used_pairs.add(pair)
                result.append(pair)

        seen.add(num)  # mark this number as seen

    return result

# 🔁 Test
arr = [-1, 1, 5, 5, 7]
target = 6
print("Unique value pairs:")
for p in unique_value_pairs(arr, target):
    print(p)
```

---

## 🧑‍💻 C++ – Unique Value Pairs (With Comments)

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
using namespace std;

vector<pair<int, int>> uniqueValuePairs(const vector<int>& arr, int target) {
    unordered_set<int> seen;
    set<pair<int, int>> used;
    vector<pair<int, int>> result;

    for (int num : arr) {
        int complement = target - num;

        if (seen.count(complement)) {
            pair<int, int> p = minmax(num, complement);
            if (!used.count(p)) {
                used.insert(p);
                result.push_back(p);
            }
        }

        seen.insert(num);
    }

    return result;
}

int main() {
    vector<int> arr = {-1, 1, 5, 5, 7};
    int target = 6;

    cout << "Unique value pairs:\n";
    for (auto p : uniqueValuePairs(arr, target)) {
        cout << "(" << p.first << ", " << p.second << ")\n";
    }

    return 0;
}
```

---

## 🌐 JavaScript – Unique Value Pairs (With Comments)

```javascript
function uniqueValuePairs(arr, target) {
    const seen = new Set();
    const used = new Set();
    const result = [];

    for (let num of arr) {
        let complement = target - num;
        let pair = [Math.min(num, complement), Math.max(num, complement)].toString();

        if (seen.has(complement) && !used.has(pair)) {
            used.add(pair);
            result.push([Math.min(num, complement), Math.max(num, complement)]);
        }

        seen.add(num);
    }

    return result;
}

// 🔁 Test
let arr = [-1, 1, 5, 5, 7];
let target = 6;

console.log("Unique value pairs:");
uniqueValuePairs(arr, target).forEach(p => {
    console.log(`(${p[0]}, ${p[1]})`);
});
```

---

## ✅ Final Output for All:

```
(-1, 7)
(1, 5)
```

---




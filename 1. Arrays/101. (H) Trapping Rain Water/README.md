Here is a well-structured README file for the **"Trapping Rain Water"** problem from GeeksforGeeks:

---

# 🌧️ Trapping Rain Water

## 📝 Problem Statement

Given an array `arr[]` representing the heights of blocks (non-negative integers), compute how much water can be trapped between the blocks during the rainy season. Assume that each block has a width of `1`.

---

## 🧠 Explanation

The water trapped on each block depends on the minimum of the tallest bar on the left and the right, minus the height of the current bar.

### 🔍 Core Formula:

```
water_at_i = min(max_left[i], max_right[i]) - height[i]
```

### ⚙️ Efficient Approach:

Use a two-pointer technique to solve in **O(n)** time and **O(1)** space.

---

## 🔍 Examples

### Example 1:

**Input:**

```python
arr[] = [3, 0, 1, 0, 4, 0, 2]
```

**Output:**

```
10
```

**Explanation:**
Water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = **10 units**

---

### Example 2:

**Input:**

```python
arr[] = [3, 0, 2, 0, 4]
```

**Output:**

```
7
```

**Explanation:**
Water trapped = 0 + 3 + 1 + 3 + 0 = **7 units**

---

### Example 3:

**Input:**

```python
arr[] = [1, 2, 3, 4]
```

**Output:**

```
0
```

**Explanation:**
No trapping possible as there are no bounding bars on both sides.

---

## 🧪 Constraints

* 1 ≤ arr.size() ≤ 10⁵
* 0 ≤ arr\[i] ≤ 10³

---

## 🧩 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 📊 Step-by-Step Dry Run

**Input:**

```
arr[] = [2, 1, 5, 3, 1, 0, 4]
```

* max\_left:   \[2, 2, 5, 5, 5, 5, 5]
* max\_right:  \[5, 5, 5, 4, 4, 4, 4]

Trapped water:

* at index 1 = min(2, 5) - 1 = 1
* at index 3 = min(5, 4) - 3 = 1
* at index 4 = min(5, 4) - 1 = 3
* at index 5 = min(5, 4) - 0 = 4

**Total water = 1 + 1 + 3 + 4 = 9 units**

---

## 💻 Code Implementation

### Python

```python
class Solution:
    def trappingWater(self, arr, n):
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left <= right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        
        return water
```

---

### C++

```cpp
class Solution {
public:
    int trappingWater(int arr[], int n) {
        int left = 0, right = n - 1;
        int left_max = 0, right_max = 0, water = 0;

        while (left <= right) {
            if (arr[left] < arr[right]) {
                if (arr[left] >= left_max)
                    left_max = arr[left];
                else
                    water += left_max - arr[left];
                left++;
            } else {
                if (arr[right] >= right_max)
                    right_max = arr[right];
                else
                    water += right_max - arr[right];
                right--;
            }
        }
        return water;
    }
};
```

---

### JavaScript

```javascript
class Solution {
    trappingWater(arr, n) {
        let left = 0, right = n - 1;
        let left_max = 0, right_max = 0;
        let water = 0;

        while (left <= right) {
            if (arr[left] < arr[right]) {
                if (arr[left] >= left_max)
                    left_max = arr[left];
                else
                    water += left_max - arr[left];
                left++;
            } else {
                if (arr[right] >= right_max)
                    right_max = arr[right];
                else
                    water += right_max - arr[right];
                right--;
            }
        }

        return water;
    }
}
```

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft
* Google
* Goldman Sachs

---

## 🏷️ Topic Tags

* Arrays
* Data Structures
* Algorithms
* Stack
* Two-Pointer Algorithm

---

## 📚 Related Articles

* [Trapping Rain Water](https://www.geeksforgeeks.org/trapping-rain-water/)

---

Let me know if you'd like this in a downloadable format or additional variations of this problem!


Here’s a complete **text explanation**, step-by-step **dry run**, and the **code implementations** in Python, C++, and JavaScript for the **Trapping Rain Water** problem from GeeksforGeeks.

---

## 🧠 Explanation

### **Problem Summary**:

Given an array `arr[]` representing block heights, compute how much water can be trapped between the blocks after raining.

### **Idea**:

For each index `i`, the water trapped above `i` depends on the minimum of:

* Maximum height to the left (`left_max[i]`)
* Maximum height to the right (`right_max[i]`)

**Water trapped at i = min(left\_max\[i], right\_max\[i]) - arr\[i]**

### **Efficient Two-Pointer Approach**:

* Initialize two pointers: `left = 0`, `right = n - 1`
* Track `left_max` and `right_max`
* At each step, move the smaller height inward
* Accumulate water if the current height is less than the running max

---

## 🧪 Dry Run

**Input:** `[3, 0, 1, 0, 4, 0, 2]`
**Step-by-step:**

```
left = 0, right = 6, left_max = 0, right_max = 0, water = 0

left:  arr[0] = 3 → left_max = 3 → move left
left:  arr[1] = 0 → water += 3 - 0 = 3
left:  arr[2] = 1 → water += 3 - 1 = 2
left:  arr[3] = 0 → water += 3 - 0 = 3
left:  arr[4] = 4 → left_max = 4 → move left
left:  arr[5] = 0 → water += 4 - 0 = 4
left:  arr[6] = 2 → water += 4 - 2 = 2

Total = 3 + 2 + 3 + 4 + 2 = 14 ✅
```

---

## ✅ Python Code

```python
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0

        while left <= right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        
        return water
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int maxWater(vector<int> &arr) {
        int n = arr.size();
        int left = 0, right = n - 1;
        int left_max = 0, right_max = 0, water = 0;

        while (left <= right) {
            if (arr[left] < arr[right]) {
                if (arr[left] >= left_max)
                    left_max = arr[left];
                else
                    water += left_max - arr[left];
                left++;
            } else {
                if (arr[right] >= right_max)
                    right_max = arr[right];
                else
                    water += right_max - arr[right];
                right--;
            }
        }
        return water;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    maxWater(arr) {
        let n = arr.length;
        let left = 0, right = n - 1;
        let left_max = 0, right_max = 0;
        let water = 0;

        while (left <= right) {
            if (arr[left] < arr[right]) {
                if (arr[left] >= left_max)
                    left_max = arr[left];
                else
                    water += left_max - arr[left];
                left++;
            } else {
                if (arr[right] >= right_max)
                    right_max = arr[right];
                else
                    water += right_max - arr[right];
                right--;
            }
        }
        return water;
    }
}
```

---

## 🧾 Key Notes

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Use Case:** Best suited for large arrays due to its optimal space/time balance.

Let me know if you'd like a visualization, a test harness, or an explanation of other variations!


---

# 🔢 Sort 0s, 1s and 2s

**Difficulty:** Medium
**Accuracy:** 50.58%
**Submissions:** 778K+
**Points:** 4
**Average Time:** 10m

---

## 📘 Problem Statement

Given an array `arr[]` containing only **0s**, **1s**, and **2s**, sort the array in **ascending order**.

You need to solve this problem **without** using the built-in sort function.

---

## 🔁 Examples

### Example 1

**Input:**
`arr[] = [0, 1, 2, 0, 1, 2]`

**Output:**
`[0, 0, 1, 1, 2, 2]`

**Explanation:**
0s, 1s and 2s are segregated into ascending order.

---

### Example 2

**Input:**
`arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]`

**Output:**
`[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]`

**Explanation:**
0s, 1s and 2s are segregated into ascending order.

---

### Follow-up:

> Could you come up with a **one-pass** algorithm using only **constant extra space**?

---

## ✅ Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `0 ≤ arr[i] ≤ 2`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🧠 Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

## 💼 Company Tags

* Paytm
* Flipkart
* Morgan Stanley
* Amazon
* Microsoft
* OYO Rooms
* Samsung
* Snapdeal
* Hike
* MakeMyTrip
* Ola Cabs
* Walmart
* MAQ Software
* Adobe
* Yatra.com
* SAP Labs
* Qualcomm

---

## 📚 Related Interview Experiences

* Paytm Interview Experience Set 14 For Senior Android Developer
* Ola Cabs Interview Experience Set 4 For SDE 2
* Paytm Interview Experience Set 5 Recruitment Drive
* Amazon Interview Experience For SDE Internship

---

## 📄 Related Articles

* [Sort An Array Of 0s 1s And 2s](https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)

---

## 📘 Problem Statement

Given an array `arr[]` containing only 0s, 1s, and 2s, sort the array in **ascending order**.
You must **not** use any built-in sort function.

### Follow-Up:

Can you solve this in **one pass** using only **constant extra space**?

---

## 🧠 Key Insight

This is a classic problem solved using the **Dutch National Flag algorithm**.

We maintain three pointers:

* `low` → the next position for 0
* `mid` → current index being evaluated
* `high` → the next position for 2

**Idea:**

* If `arr[mid] == 0`: swap with `low` and increment both
* If `arr[mid] == 1`: move `mid`
* If `arr[mid] == 2`: swap with `high` and decrement `high`

---

## 🧪 Example

**Input:**
`arr = [0, 1, 2, 0, 1, 2]`
**Output:**
`[0, 0, 1, 1, 2, 2]`

---

## 🧮 Dry Run

| Step | low | mid | high | arr                 | Action        |
| ---- | --- | --- | ---- | ------------------- | ------------- |
| 0    | 0   | 0   | 5    | \[0, 1, 2, 0, 1, 2] | swap(0,0), ++ |
| 1    | 1   | 1   | 5    | \[0, 1, 2, 0, 1, 2] | mid++         |
| 2    | 1   | 2   | 5    | \[0, 1, 2, 0, 1, 2] | swap(2,5), -- |
| 3    | 1   | 2   | 4    | \[0, 1, 2, 0, 1, 2] | swap(2,4), -- |
| 4    | 1   | 2   | 3    | \[0, 1, 1, 0, 2, 2] | mid++ (1)     |
| 5    | 1   | 3   | 3    | \[0, 1, 1, 0, 2, 2] | swap(0,1)     |
| 6    | 2   | 4   | 3    | \[0, 0, 1, 1, 2, 2] | done          |

---

## ✅ Python Code

```python
class Solution:
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    void sort012(vector<int>& arr) {
        int low = 0, mid = 0, high = arr.size() - 1;

        while (mid <= high) {
            if (arr[mid] == 0)
                swap(arr[low++], arr[mid++]);
            else if (arr[mid] == 1)
                mid++;
            else
                swap(arr[mid], arr[high--]);
        }
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    sort012(arr) {
        let low = 0, mid = 0, high = arr.length - 1;

        while (mid <= high) {
            if (arr[mid] === 0) {
                [arr[low], arr[mid]] = [arr[mid], arr[low]];
                low++;
                mid++;
            } else if (arr[mid] === 1) {
                mid++;
            } else {
                [arr[mid], arr[high]] = [arr[high], arr[mid]];
                high--;
            }
        }
    }
}
```

---

## 💬 Interviewer Expectation

* Optimal solution in O(n)
* In-place
* One-pass
* No built-in sort
* Able to simulate dry run on whiteboard

---

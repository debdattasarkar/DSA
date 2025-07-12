💥 OH YES — this is **exactly** how pros prep for interviews! 💼
You’re now leveling up from learning to **strategic company-focused practice.** 🎯

---

# 🎯 What We're Doing:

We’ll go through **real interview-style array questions** asked at top tech companies like:

* ✅ **NVIDIA**
* ✅ **Amazon**
* ✅ (and others in similar FAANG-tier)

**Language:** Python 🐍
**Format:**
For each question, I’ll give you:

1. ✅ **Problem Statement**
2. 🧠 **Why it's asked / what it tests**
3. 🚀 **Python Implementation**
4. 📝 **Follow-up/variant questions**

We’ll go from:

* 🟢 **Easy**
* 🟡 **Medium**
* 🔴 **Hard**

---

## 🟢 EASY QUESTION 1: **Check if Array is Sorted (Non-Decreasing Order)**

### ✅ Asked By: NVIDIA, TCS, Infosys

### ❓ Problem Statement:

Given an array of integers, determine if it's sorted in non-decreasing order (each element is ≥ the previous one).

```python
Input: [1, 2, 2, 4, 5]
Output: True

Input: [5, 4, 3]
Output: False
```

---

### 🧠 What It Tests:

* Basic loop logic
* Comparisons and array traversal
* Clean implementation (edge case handling)

---

### 🐍 Python Code:

```python
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Test cases
print(is_sorted([1, 2, 2, 4, 5]))  # True
print(is_sorted([5, 4, 3]))        # False
```

---

### 💬 Follow-up Questions:

* Can you make it work for **strictly increasing**?
* Can you modify it to detect if it’s **strictly decreasing**?

---

## 🟢 EASY QUESTION 2: **Move All Zeros to End**

### ✅ Asked By: Amazon

### ❓ Problem Statement:

Given an array, move all zeros to the end while maintaining the order of non-zero elements.

```python
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

---

### 🧠 What It Tests:

* In-place updates
* Two-pointer logic
* Clean swaps and index management

---

### 🐍 Python Code:

```python
def move_zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr

# Test
print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
```

---

### 💬 Follow-up Questions:

* Can you do it with **O(1)** extra space?
* What if zero has a **special meaning** in the context?

---

# 🚀 Next Step:

👉 I can give you a **medium-level array problem** from Amazon/NVIDIA next —
Shall we continue with that?

OR
Would you like to **code one of the above yourself** and I review it?

🎯 You choose!

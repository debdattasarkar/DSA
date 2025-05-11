Awesome! Since you're ready to keep going, let's jump into the **next level: Medium difficulty** — straight from Amazon-style interview playbooks. 🟡💼

---

## 🟡 MEDIUM QUESTION: **"Two Sum"**

### ✅ Asked By: Amazon, Microsoft, NVIDIA

---

### ❓ **Problem Statement**

Given an array of integers and a target sum, return the **indices** of two numbers that add up to the target.

> You may assume that each input would have exactly one solution, and you may not use the same element twice.

```python
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

---

### 🧠 **What It Tests**

* Hash map usage for O(n) time
* Efficient pair searching
* Data structure + logic thinking

---

### 🐍 Python Solution (O(n) Time)

```python
def two_sum(nums, target):
    index_map = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

---

### 💡 Follow-up Interview Questions:

* Can you do it **without extra space**? (Brute force is O(n²))
* How would you solve it if the array was **sorted**?
* What if you had to **return all such pairs**?

---

## ✅ Want to Try It Out?

Would you like to:

* 🧪 Try coding the “Two Sum” in Python yourself and get feedback?
* 🟠 Or shall I move to the next **Hard-Level Array** problem asked at Amazon/NVIDIA?

You’re on fire — let’s keep the momentum going! 💥
**What's your pick?** 🚀

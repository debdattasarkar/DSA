Let's dive into the **Variable Sliding Window** technique — a powerful extension of the fixed sliding window that dynamically adjusts its size based on a **constraint**.

---

## 🪟 What is the Variable Sliding Window Technique?

### 📌 Definition:

A **variable window** is a subarray or substring whose size **changes dynamically** during iteration to **satisfy a certain condition**.

* Unlike fixed-size windows, the **start and end pointers move independently**.
* It helps solve problems where you need the **longest/shortest subarray/substring** that meets some condition.

---

## 🧠 When to Use It?

Use this technique when the problem asks for:

| Objective                                 | Example Problem                     |
| ----------------------------------------- | ----------------------------------- |
| Longest substring with unique characters  | Leetcode 3                          |
| Smallest window containing all characters | Leetcode 76                         |
| Max number of 1s with at most K flips     | Leetcode 1004 / GFG                 |
| Longest substring with ≤ K distinct chars | Leetcode 340                        |
| Count substrings matching pattern         | GFG – Count Occurrences of Anagrams |

---

## 🔧 Core Template

```python
left = 0
for right in range(len(arr)):
    # Expand window by adding arr[right]
    
    while condition is violated:
        # Shrink window from the left
        left += 1

    # Check window validity or update result
```

---

## ✅ Example: Longest Substring Without Repeating Characters (Leetcode 3)

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
```

### 🔍 Key Observations:

* **Window size changes** dynamically based on repeated character detection.
* When a repeat is found, shrink the window from the **left** until valid again.

---

## 🧪 Time and Space Complexity

| Metric | Value |                              |
| ------ | ----- | ---------------------------- |
| Time   | O(n)  |                              |
| Space  | O(k)  | (at most `k` distinct chars) |

---

## 💡 Real-World Analogy

Imagine you're standing at a buffet with a tray. You can only carry plates that satisfy a diet constraint (say ≤ 3 desserts). If you pick too many desserts, you remove some from the left side of your tray until you're within the limit again.

---

## 📋 Top Interview Problems Using Variable Window

| Problem                                                                                                        | Description                               |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [Leetcode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)                    | Longest substring without duplicates      |
| [Leetcode 76](https://leetcode.com/problems/minimum-window-substring/)                                         | Smallest window containing all characters |
| [Leetcode 1004](https://leetcode.com/problems/max-consecutive-ones-iii/)                                       | Max consecutive ones with k flips         |
| [Leetcode 424](https://leetcode.com/problems/longest-repeating-character-replacement/)                         | Longest substring with replaceable chars  |
| [GFG – Count Subarrays with Sum ≤ K](https://www.geeksforgeeks.org/count-of-subarrays-having-sum-less-than-k/) | Subarray sum with constraint              |

---

## 🔄 Fixed vs Variable Window

| Feature         | Fixed Window                  | Variable Window                       |
| --------------- | ----------------------------- | ------------------------------------- |
| Window Size     | Constant (`k`)                | Dynamically adjusted                  |
| When to Use     | Exact-size subarrays          | Constraints on sum, distinct elements |
| Example Problem | Max sum of subarray of size k | Longest substring without repetition  |

---

## ➕ Extensions with Hashmaps

Most variable window problems involve:

* **HashMaps** for counting characters
* **Frequency arrays**
* **Two pointers (left & right)**

---

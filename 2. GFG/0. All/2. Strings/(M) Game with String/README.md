
---

# 🧩 Game with String

**Difficulty:** Medium
**Accuracy:** 53.96%
**Submissions:** 58K+
**Points:** 4
**Average Time:** 15m

---

## 📝 Problem Statement

Given a string `s` consisting of lowercase alphabets and an integer `k`, your task is to find the **minimum** possible value of the string after removing exactly `k` characters.

> The **value** of the string is defined as the **sum of the squares** of the frequencies of each distinct character present in the string.

---

## 📌 Examples

### Example 1:

```
Input:  s = "abbccc", k = 2  
Output: 6  
Explanation:  
We can:
- Remove two 'c': value = 1² + 2² + 1² = 6  
- OR remove one 'b' and one 'c': value = 1² + 1² + 2² = 6
```

### Example 2:

```
Input:  s = "aaab", k = 2  
Output: 2  
Explanation:  
We remove two 'a's.
- Final frequencies: a = 1, b = 1
- Value = 1² + 1² = 2
```

---

## 🧮 Constraints

* $0 \leq k \leq s.length() \leq 10^5$

---

## 📈 Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(n)$

---

## 🏢 Company Tags

* Amazon

---

## 🏷️ Topic Tags

* Strings
* Heap
* Data Structures

---

## 🔗 Related Articles

* [Minimum Sum Squares Characters Counts Given String Removing K Characters](https://practice.geeksforgeeks.org/problems/game-with-string4100/1)

---

Here’s the complete explanation, step-by-step dry run, and implementation in Python, C++, and JavaScript, along with common **interview questions and answers** for this problem:

---

## 🧠 1. Text Explanation

### Problem Summary:

You are given a string `s` and an integer `k`. In **k operations**, you can **remove one character** from the string each time. Your goal is to **minimize the total value** of the string after those removals.

**Value of the string** = Sum of squares of frequencies of characters.

---

## 🔍 Step-by-Step Dry Run

### Example:

`s = "aaabbbcc", k = 2`

* Frequencies: a=3, b=3, c=2
* Initial value: 3² + 3² + 2² = 9 + 9 + 4 = **22**

### Goal:

We want to reduce the highest frequencies (since squares grow fast).

1. **Put frequencies in a max-heap** (invert sign since Python/C++ only support min-heap natively):
   Max-heap: `[-3, -3, -2]`

2. **Operation 1**: Pop `-3`, reduce it → `-2`, push back:
   Heap: `[-3, -2, -2]`

3. **Operation 2**: Pop `-3`, reduce it → `-2`, push back:
   Heap: `[-2, -2, -2]`

Final frequencies: 2, 2, 2
Final value = 2² + 2² + 2² = **12**

✅ **Optimal reduction**

---

## ✅ Optimized Approach

1. Count frequencies of each character.
2. Use a max-heap to store all frequencies.
3. Repeat `k` times:

   * Pop max freq, decrement it, push it back (if > 0).
4. Calculate the final value.

**Time Complexity**: O(n + k log 26) ≈ O(n)
**Space Complexity**: O(26) = O(1)

---

## 🧪 2. Code Implementations

### ✅ Python

```python
import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        # Step 1: Count frequency of each character
        freq = Counter(s)
        
        # Step 2: Use a max-heap (invert to simulate max-heap)
        max_heap = [-val for val in freq.values()]
        heapq.heapify(max_heap)

        # Step 3: Perform k removals
        while k > 0 and max_heap:
            top = heapq.heappop(max_heap)
            top += 1  # Since negative, incrementing means reducing abs value
            if top < 0:
                heapq.heappush(max_heap, top)
            k -= 1

        # Step 4: Calculate sum of squares of remaining frequencies
        return sum(x * x for x in max_heap)  # still negative, so square cancels
```

---

### ✅ C++

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
  public:
    int minValue(string &s, int k) {
        unordered_map<char, int> freq;
        for (char c : s) freq[c]++;

        priority_queue<int> maxHeap;
        for (auto &p : freq) maxHeap.push(p.second);

        while (k-- && !maxHeap.empty()) {
            int top = maxHeap.top();
            maxHeap.pop();
            if (--top > 0) maxHeap.push(top);
        }

        int result = 0;
        while (!maxHeap.empty()) {
            int f = maxHeap.top(); maxHeap.pop();
            result += f * f;
        }
        return result;
    }
};
```

---

### ✅ JavaScript

```javascript
class Solution {
    minValue(s, k) {
        let freq = new Map();
        for (let c of s) {
            freq.set(c, (freq.get(c) || 0) + 1);
        }

        // Use a max heap simulation with array sort
        let heap = [...freq.values()];
        heap.sort((a, b) => b - a);  // max-heap simulation

        while (k > 0) {
            heap[0] -= 1;
            k--;
            heap.sort((a, b) => b - a);  // re-sort
        }

        return heap.reduce((sum, f) => sum + f * f, 0);
    }
}
```

---

## 🎯 3. Interview Questions & Answers

### Q1: Why use a max-heap?

**A:** We always want to remove characters from the most frequent character to minimize the value quickly. Max-heaps allow efficient access to the largest frequency.

---

### Q2: What if k is greater than the total number of characters?

**A:** We keep removing from the highest frequency till heap is empty. If all characters are removed, the result is `0`.

---

### Q3: Why use square of frequency as the value?

**A:** The question defines "value" in that way. Squaring increases the penalty for higher frequency, making the goal to balance frequencies as low as possible.

---

### Q4: Can we do better than heap?

**A:** Heap is already O(k log n), optimal for k ≤ 10⁵. Alternatives like bucket frequency might work for small alphabets, but heap is flexible and general.

---


Here is the complete **README-style documentation** based on the given image, including problem description, constraints, examples, tags, and complexity:

---

# 🚀 Lexicographically Largest String After Deleting K Characters

**Difficulty**: Medium
**Accuracy**: 50.0%
**Submissions**: 14K+
**Points**: 4
**Average Time**: 15 mins

---

## 📝 Problem Statement

Given a string `s` consisting of **lowercase English letters** and an integer `k`, your task is to **remove exactly `k` characters** from the string.
The resulting string must be the **largest possible in lexicographical order**, while maintaining the **relative order** of the remaining characters.

---

## 🔍 Examples

### Example 1:

**Input**:

```
s = "ritz", k = 2
```

**Output**:

```
tz
```

**Explanation**:
By removing two characters in all possible ways, we get:

* "ri", "rt", "rz", "it", "iz", and "tz"

Among these, **"tz"** is the **lexicographically largest** string.

---

### Example 2:

**Input**:

```
s = "zebra", k = 3
```

**Output**:

```
zr
```

**Explanation**:
Removing "e", "b", and "a" results in "zr", which is **lexicographically largest**.

---

## 📌 Constraints

* `1 ≤ s.length() ≤ 10⁵`
* `0 ≤ k ≤ s.length()`

---

## 📈 Expected Complexities

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(n)

---

## 🏷️ Tags

* Stack
* Strings
* Greedy
* Data Structures

---

## 🔗 Related Articles

* [Lexicographically Largest String After K Removals (GeeksforGeeks)](https://www.geeksforgeeks.org/lexicographically-largest-string-after-k-removals/) *(link inferred from title)*

---

---

## 📘 Text Explanation with Step-by-Step Dry Run

### 🔍 Problem Recap:

Given a string `s` and an integer `k`, remove **exactly `k` characters** to form the **lexicographically largest** possible string, **preserving character order**.

---

### ✅ Approach (Greedy + Stack):

We want to keep the result as large as possible **lexicographically**. This means we:

* Prefer 'z' > 'y' > ... > 'a'.
* Remove characters from the left if they are **smaller than upcoming ones**, and we still have deletion quota `k`.

### 🔧 Steps:

1. Initialize an empty stack.
2. Traverse each character `c` in the string `s`:

   * While the stack is not empty, and the top of the stack is less than `c`, and `k > 0`, pop from the stack and decrement `k`.
   * Push `c` to the stack.
3. If `k > 0` (we didn't use all deletions), pop the last `k` characters from the end.
4. Return the final string built from the stack.

---

### 🔁 Dry Run

**Input**:
`s = "zebra"`, `k = 3`
**Goal**: Remove 3 characters → Max lexicographical

**Stack Process**:

* 'z' → stack: `['z']`
* 'e' → stack: `['z', 'e']`
* 'b' → stack: `['z', 'e', 'b']`
* 'r':
  `'b' < 'r'` → pop `'b'`, k=2
  `'e' < 'r'` → pop `'e'`, k=1
  stack: `['z', 'r']`
* 'a' → stack: `['z', 'r', 'a']`

Still 1 deletion left → remove from right: `'a'`

Final Result: **"zr"**

---

## ✅ Optimized Code Implementations

---

### ✅ Python Code

```python
class Solution:
    def maxSubseq(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        keep = n - k  # we want to keep (n-k) characters
        
        for i, c in enumerate(s):
            while stack and k > 0 and stack[-1] < c:
                stack.pop()
                k -= 1
            stack.append(c)

        # Remove extra characters if k remains
        return ''.join(stack[:keep])
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    string maxSubseq(string& s, int k) {
        vector<char> stack;
        int n = s.size(), keep = n - k;

        for (char c : s) {
            while (!stack.empty() && k > 0 && stack.back() < c) {
                stack.pop_back();
                k--;
            }
            stack.push_back(c);
        }

        // Take first (n - k) characters
        return string(stack.begin(), stack.begin() + keep);
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    maxSubseq(s, k) {
        let stack = [];
        let keep = s.length - k;

        for (let c of s) {
            while (stack.length && k > 0 && stack[stack.length - 1] < c) {
                stack.pop();
                k--;
            }
            stack.push(c);
        }

        return stack.slice(0, keep).join('');
    }
}
```

---

## 📌 Interview Questions

### 1. **Why is this a greedy problem?**

> Because at each step, we make the locally optimal decision — removing a smaller character when a bigger one is available ahead.

### 2. **Why use a stack instead of a list or array?**

> Stack naturally models LIFO behavior. When we remove characters from the end, it mimics "going back" and deleting prior decisions.

### 3. **What is the time and space complexity?**

* Time: O(n)
* Space: O(n)

### 4. **Can we solve this with recursion or DP?**

> It’s possible but inefficient. The greedy approach with stack is optimal and linear.

### 5. **How would you test this in production?**

* Unit tests for edge cases: empty string, `k = 0`, all characters same, etc.
* Randomized large inputs
* Stress test with `n = 10^5`, `k = n-1`

---



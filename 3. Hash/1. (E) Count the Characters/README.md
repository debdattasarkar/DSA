Here’s a full explanation of the **“Count the Characters”** problem from GeeksforGeeks, including:

---

### ✅ **Problem Recap**

Given a string `S` and an integer `N`, count how many distinct characters occur **exactly `N` times** in the string, but:

* **Consecutive occurrences count as one**.

---

### 🔍 **Step-by-Step Explanation**

Let’s take an example:
**Input:**

```
S = "geeksforgeeks", N = 2
```

* First, collapse consecutive duplicates:

  * `'eek' → 'ek'`
  * `'ss' stays 's'`
* After collapse: `"geksforgeks"`
* Now, count how often each character appears:

  * `g:2, e:2, k:2, s:2, others:1`
* So, the answer is `4` (`g, e, k, s` appear 2 times)

---

### 🐍 Python Code (with inline comments)

```python
#User function Template for python3

class Solution:
    def getCount(self, S, N):
        # Step 1: Collapse consecutive characters to count as one
        collapsed = []
        for ch in S:
            if not collapsed or collapsed[-1] != ch:
                collapsed.append(ch)
        
        # Step 2: Count frequencies
        freq = {}
        for ch in collapsed:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 3: Count how many characters occurred exactly N times
        count = sum(1 for v in freq.values() if v == N)
        return count


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s, n = input().split()
        n = int(n)
        ob = Solution()
        print(ob.getCount(s, n))
        print("~")
```

---

### 💻 C++ Version

```cpp
class Solution {
  public:
    int getCount(string S, int N) {
        string collapsed = "";
        
        // Collapse consecutive characters
        for (char ch : S) {
            if (collapsed.empty() || collapsed.back() != ch)
                collapsed.push_back(ch);
        }

        // Count character frequencies
        unordered_map<char, int> freq;
        for (char ch : collapsed) freq[ch]++;

        // Count how many have exactly N occurrences
        int count = 0;
        for (auto [key, val] : freq)
            if (val == N) count++;
            
        return count;
    }
};
```

---

### 🌐 JavaScript Version

```javascript
class Solution {
    getCount(S, N) {
        let collapsed = [];

        // Collapse consecutive characters
        for (let i = 0; i < S.length; i++) {
            if (collapsed.length === 0 || collapsed[collapsed.length - 1] !== S[i]) {
                collapsed.push(S[i]);
            }
        }

        // Count character frequencies
        let freq = {};
        for (let ch of collapsed) {
            freq[ch] = (freq[ch] || 0) + 1;
        }

        // Count characters with exactly N occurrences
        let count = 0;
        for (let key in freq) {
            if (freq[key] === N) count++;
        }

        return count;
    }
}
```

Would you like a dry run on another test case?

### 🔍 Problem Summary: Substrings With Same First and Last Characters

Given a string `s` of lowercase letters, the goal is to count all substrings **where the first and last characters are the same**.

---

### ✅ Observations:

A substring is valid if:

* `s[i] == s[j]` where `i <= j`.

Instead of generating all substrings (which takes `O(n^2)`), we count how many times each character occurs and use combinatorics:

* For a character with frequency `f`, valid substrings:

  ```
  count = f + (f choose 2) = f + (f * (f - 1)) / 2
  ```

---

### 🧠 Dry Run Example:

For `s = "acab"`

* Frequency: a:2, b:1, c:1
* Valid substrings:

  * a: "a", "aca" → 2 (length 1) + 1 (start-end) = 3
  * b: "b" → 1
  * c: "c" → 1
* Answer = 3 + 1 + 1 = 5

Wait! Actually we missed "cab", which ends in 'b' and starts in 'c'. But it's invalid because start != end. So our method is correct.

---

### ✅ Final Formula:

```
For each character ch in a-z:
    count[ch] = frequency of ch
    result += (count[ch] * (count[ch] + 1)) // 2
```

---

### ✅ Python Code (with comments)

```python
class Solution:
    def countSubstring(self, s):
        from collections import Counter
        count = Counter(s)
        ans = 0
        for freq in count.values():
            # Each character contributes freq substrings of length 1
            # and (freq * (freq - 1)) // 2 substrings with same start & end
            ans += freq * (freq + 1) // 2
        return ans
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    int countSubstring(string &s) {
        int freq[26] = {0};
        for (char ch : s) freq[ch - 'a']++;
        
        int ans = 0;
        for (int f : freq) {
            ans += f * (f + 1) / 2;
        }
        return ans;
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    countSubstring(s) {
        let freq = new Array(26).fill(0);
        for (let ch of s) {
            freq[ch.charCodeAt(0) - 97]++;
        }

        let ans = 0;
        for (let f of freq) {
            ans += f * (f + 1) / 2;
        }
        return ans;
    }
}
```

---

### 🕒 Time & Space Complexity

* **Time**: O(n)
* **Space**: O(1) (since only 26 lowercase letters)

---

Let me know if you'd like this visualized or extended for Unicode strings.

Here is the **README** file for the **Longest Palindromic Substring** problem based on the provided image:

---

# 🔁 Longest Palindrome in a String

## 📝 Problem Statement

Given a string `s`, your task is to find the **longest palindromic substring** within `s`.

* A **substring** is a contiguous sequence of characters within a string.
* A **palindrome** is a string that reads the same forward and backward, i.e., `reverse(s) == s`.

> 🔹 If there are multiple palindromic substrings of the same length, return the **first occurrence** from the left.

---

## 📌 Examples

### Example 1

**Input:**
`s = "forgeekskeegfor"`
**Output:** `"geekskeeg"`
**Explanation:**
Substrings like `"kssk"`, `"ss"`, `"eeksskee"` exist, but `"geekskeeg"` is the longest.

---

### Example 2

**Input:**
`s = "Geeks"`
**Output:** `"ee"`
**Explanation:**
`"ee"` is the longest palindromic substring in `"Geeks"`.

---

### Example 3

**Input:**
`s = "abc"`
**Output:** `"a"`
**Explanation:**
Each character `"a"`, `"b"`, and `"c"` are palindromes. The first one (`"a"`) is returned.

---

## 🔒 Constraints

* `1 ≤ s.size() ≤ 10^3`
* `s` consists of only **lowercase English letters**

---

## ⏱️ Expected Time and Space Complexity

| Metric          | Complexity |
| --------------- | ---------- |
| Time Complexity | O(n²)      |
| Auxiliary Space | O(1)       |

---

## 🧠 Topic Tags

* Strings
* Dynamic Programming
* Palindrome
* Data Structures
* Algorithms

---

## 🏢 Company Tags

* Zoho
* Accolite
* Amazon
* Microsoft
* Samsung
* MakeMyTrip
* Visa
* Walmart
* Google
* Qualcomm
* Groupon

---

## 💼 Related Interview Experiences

* Accolite Interview Experience Set 4 On Campus
* Amazon Interview Experience Set 412 SDE I
* Samsung Research Institute Bangalore SRIB Intern

---

## 📚 Related Articles

* [Longest Palindromic Substring Using Dynamic Programming 2](#)
* [Longest Palindromic Substring](#)

---

Here's the full explanation, dry run, and implementations for **"Longest Palindrome in a String"** as requested.

---

## 🧠 Problem Explanation

Given a string `s`, find the **longest palindromic substring** within it.

### Definitions:

* A **palindrome** reads the same forward and backward.
* A **substring** is a contiguous section of a string.

> ✅ Return the first longest palindromic substring if there are multiple with the same length.

---

## 🧪 Step-by-Step Dry Run

### Input:

`s = "forgeekskeegfor"`

### Visualize Each Center:

We consider each character (and gap between characters) as a **center** of a potential palindrome and **expand outwards** while the characters match.

* Center at `'g'`: expanding → `"geekskeeg"` (length 9)
* All other centers yield shorter palindromes.

✅ **Output:** `"geekskeeg"`

---

## ✅ Python Code with Comments

```python
class Solution:
    def longestPalindrome(self, s):
        start, end = 0, 0
        
        # Helper function to expand around the center
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindromes
            l1, r1 = expandAroundCenter(i, i)
            # Even-length palindromes
            l2, r2 = expandAroundCenter(i, i + 1)
            
            # Choose the longer
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.longestPalindrome(S))
        print("~")
```

---

## ✅ C++ Code with Comments

```cpp
class Solution {
  public:
    string longestPalindrome(string &s) {
        int start = 0, end = 0;

        auto expand = [&](int l, int r) {
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                l--;
                r++;
            }
            return make_pair(l + 1, r - 1);
        };

        for (int i = 0; i < s.size(); i++) {
            auto [l1, r1] = expand(i, i);
            auto [l2, r2] = expand(i, i + 1);

            if (r1 - l1 > end - start) {
                start = l1; end = r1;
            }
            if (r2 - l2 > end - start) {
                start = l2; end = r2;
            }
        }

        return s.substr(start, end - start + 1);
    }
};


// Driver Code
int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;
        Solution ob;
        cout << ob.longestPalindrome(S) << endl;
        cout << "~" << endl;
    }
}
```

---

## ✅ JavaScript Code with Comments

```javascript
class Solution {
    longestPalindrome(s) {
        let start = 0, end = 0;

        const expand = (left, right) => {
            while (left >= 0 && right < s.length && s[left] === s[right]) {
                left--;
                right++;
            }
            return [left + 1, right - 1];
        };

        for (let i = 0; i < s.length; i++) {
            let [l1, r1] = expand(i, i);
            let [l2, r2] = expand(i, i + 1);

            if (r1 - l1 > end - start) {
                start = l1;
                end = r1;
            }

            if (r2 - l2 > end - start) {
                start = l2;
                end = r2;
            }
        }

        return s.substring(start, end + 1);
    }
}


// Driver Code
"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
    inputString += inputStdin;
});

process.stdin.on("end", (_) => {
    inputString = inputString.trim().split("\n").map((string) => string.trim());
    main();
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let S = readLine();
        let obj = new Solution();
        let res = obj.longestPalindrome(S);
        console.log(res);
        console.log("~");
    }
}
```

---

## ⏱ Time and Space Complexity

| Metric        | Value |
| ------------- | ----- |
| Time          | O(n²) |
| Space (Extra) | O(1)  |

---


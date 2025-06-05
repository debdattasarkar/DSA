### 🧠 Problem Summary: Remove Duplicates in Array (GeeksforGeeks)

**Task**:
Given an array of positive integers, remove all **duplicate elements** while **preserving the order** of their **first appearance**.

---

### 📘 Clarification

* Input: An array of integers.
* Output: A list of unique elements in the same order as they appeared first.

---

### 💡 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $2 \leq \text{arr[i]} \leq 100$

---

### 🔍 Step-by-Step Dry Run

#### Example Input:

```
arr = [2, 2, 3, 3, 7, 5]
```

**Step 1**: Start from the beginning of the array.
**Step 2**: Track elements you’ve already seen using a set.
**Step 3**: Keep adding unseen elements to the result.

Dry run:

| Element | Seen Before? | Add to Result | Seen Set     |
| ------- | ------------ | ------------- | ------------ |
| 2       | No           | ✅ Yes         | {2}          |
| 2       | Yes          | ❌ No          | {2}          |
| 3       | No           | ✅ Yes         | {2, 3}       |
| 3       | Yes          | ❌ No          | {2, 3}       |
| 7       | No           | ✅ Yes         | {2, 3, 7}    |
| 5       | No           | ✅ Yes         | {2, 3, 5, 7} |

✅ Final Output: `[2, 3, 7, 5]`

---

## ✅ Code Implementations

---

### 🔸 Python

```python
class Solution:
    def removeDuplicates(self, arr):
        seen = set()          # To track unique elements
        result = []           # Result array

        for num in arr:
            if num not in seen:
                result.append(num)
                seen.add(num)  # Mark as seen

        return result


# Driver Code
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    s = Solution().removeDuplicates(arr)
    print(" ".join(map(str, s)))
```

---

### 🔸 C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> removeDuplicates(vector<int>& arr) {
        unordered_set<int> seen;
        vector<int> result;

        for (int num : arr) {
            if (seen.find(num) == seen.end()) {
                result.push_back(num);   // Add unique
                seen.insert(num);        // Mark as seen
            }
        }
        return result;
    }
};

// Driver Code
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        int num;
        vector<int> arr;

        while (ss >> num) arr.push_back(num);

        Solution obj;
        vector<int> result = obj.removeDuplicates(arr);

        for (int x : result)
            cout << x << " ";
        cout << endl;
    }
    return 0;
}
```

---

### 🔸 JavaScript

```javascript
class Solution {
    removeDuplicates(arr) {
        const seen = new Set();
        const result = [];

        for (let num of arr) {
            if (!seen.has(num)) {
                result.push(num);     // Add if not seen
                seen.add(num);        // Track as seen
            }
        }

        return result;
    }
}

// Driver Code
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let inputLines = [], currentLine = 0;
rl.on("line", line => inputLines.push(line.trim()));
rl.on("close", () => {
    const t = parseInt(inputLines[currentLine++]);
    for (let i = 0; i < t; i++) {
        let arr = inputLines[currentLine++].split(" ").map(Number);
        const obj = new Solution();
        let res = obj.removeDuplicates(arr);
        console.log(res.join(" "));
    }
});
```

---



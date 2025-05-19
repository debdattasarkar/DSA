Here's a complete explanation and solution for the **Kadane’s Algorithm** problem as shown in the image, including:

* ✅ Text explanation
* ✅ Step-by-step dry run
* ✅ Code in Python, C++, and JavaScript with inline comments

---

## 🧠 Problem Summary

Given an array of integers, the task is to **find the maximum sum** of any **contiguous subarray** using **Kadane’s Algorithm**.

---

## 💡 Core Idea (Kadane’s Algorithm)

At every position in the array:

1. Either extend the previous subarray or start a new one.
2. Track the **maximum sum encountered so far**.

---

## 🔍 Algorithm Steps

1. Initialize:

   * `max_sum = arr[0]` (holds max seen so far)
   * `curr_sum = arr[0]` (current subarray sum)

2. Iterate from index 1:

   * `curr_sum = max(arr[i], curr_sum + arr[i])`
   * `max_sum = max(max_sum, curr_sum)`

---

## 🧪 Dry Run

**Input:** `[2, 3, -8, 7, -1, 2, 3]`

```
i = 0 → curr_sum = 2, max_sum = 2
i = 1 → curr_sum = 5, max_sum = 5
i = 2 → curr_sum = -3, max_sum = 5
i = 3 → curr_sum = 7, max_sum = 7
i = 4 → curr_sum = 6, max_sum = 7
i = 5 → curr_sum = 8, max_sum = 8
i = 6 → curr_sum = 11, max_sum = 11
```

✅ Output: `11`

---

## ✅ Python Code

```python
class Solution:
    def maxSubArraySum(self, arr, n):
        max_sum = arr[0]
        curr_sum = arr[0]
        
        for i in range(1, n):
            # Either start a new subarray at i or extend the previous one
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
```

---

## ✅ C++ Code

```cpp
class Solution {
public:
    int maxSubArraySum(int arr[], int n) {
        int max_sum = arr[0];
        int curr_sum = arr[0];
        
        for (int i = 1; i < n; i++) {
            curr_sum = max(arr[i], curr_sum + arr[i]);
            max_sum = max(max_sum, curr_sum);
        }
        
        return max_sum;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    maxSubArraySum(arr, n) {
        let maxSum = arr[0];
        let currSum = arr[0];
        
        for (let i = 1; i < n; i++) {
            currSum = Math.max(arr[i], currSum + arr[i]);
            maxSum = Math.max(maxSum, currSum);
        }
        
        return maxSum;
    }
}
```

---

## 📈 Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |

---

## 🧩 Summary

* Kadane’s Algorithm is an efficient linear solution.
* It dynamically decides at each index whether to start fresh or extend the current subarray.
* Works even when all elements are negative.

Let me know if you want to modify this to return the actual subarray (not just the sum).

Here’s the complete solution for **Kadane’s Algorithm** as requested, including:

* ✅ **Text explanation**
* ✅ **Step-by-step dry run**
* ✅ **Working code** in **Python, C++, and JavaScript** (with inline comments)

---

## ✅ Problem Summary

You are given an array of integers (positive, zero, or negative).
Your task is to return the **maximum sum of a contiguous subarray** using **Kadane’s Algorithm**.

---

## 💡 Kadane’s Algorithm – Core Idea

At every index:

* Decide whether to:

  * Continue with the previous subarray, or
  * Start a new subarray at the current index
* Track the **maximum sum** seen so far

---

## 🧪 Dry Run

### Input:

```python
arr = [2, 3, -8, 7, -1, 2, 3]
```

### Walkthrough:

| Index | Num | curr\_sum = max(num, curr\_sum + num) | max\_sum |
| ----- | --- | ------------------------------------- | -------- |
| 0     | 2   | 2                                     | 2        |
| 1     | 3   | max(3, 2+3) = 5                       | 5        |
| 2     | -8  | max(-8, 5-8) = -3                     | 5        |
| 3     | 7   | max(7, -3+7) = 7                      | 7        |
| 4     | -1  | max(-1, 7-1) = 6                      | 7        |
| 5     | 2   | max(2, 6+2) = 8                       | 8        |
| 6     | 3   | max(3, 8+3) = 11                      | 11       |

### ✅ Final Answer: `11`

---

## ✅ Python Code

```python
class Solution:
    def maxSubArraySum(self, arr):
        # Initialize max_sum and curr_sum with the first element
        max_sum = curr_sum = arr[0]

        # Traverse from second element
        for num in arr[1:]:
            # Either start new subarray or continue the current one
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum


# Driver Code
import math

def main():
    T = int(input())
    while (T > 0):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1

if __name__ == "__main__":
    main()
```

---

## ✅ C++ Code

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArraySum(vector<int> &arr) {
        int max_sum = arr[0];
        int curr_sum = arr[0];

        for (int i = 1; i < arr.size(); i++) {
            curr_sum = max(arr[i], curr_sum + arr[i]);
            max_sum = max(max_sum, curr_sum);
        }

        return max_sum;
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
        vector<int> arr;
        int x;
        while (ss >> x) arr.push_back(x);

        Solution ob;
        cout << ob.maxSubArraySum(arr) << endl;
        cout << "~" << endl;
    }
    return 0;
}
```

---

## ✅ JavaScript Code

```javascript
// Driver Template
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });
process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    while (t--) {
        const arr = readLine().split(' ').map(Number);
        let obj = new Solution();
        let ans = obj.maxSubarraySum(arr);
        console.log(ans);
        console.log("~");
    }
}

// Kadane’s Algorithm in JavaScript
class Solution {
    /**
     * @param {number[]} arr
     * @returns {number}
     */
    maxSubarraySum(arr) {
        let maxSum = arr[0];
        let currSum = arr[0];

        for (let i = 1; i < arr.length; i++) {
            currSum = Math.max(arr[i], currSum + arr[i]);
            maxSum = Math.max(maxSum, currSum);
        }

        return maxSum;
    }
}
```

---

## 📈 Complexity

| Metric          | Value |
| --------------- | ----- |
| Time Complexity | O(n)  |
| Auxiliary Space | O(1)  |

---

Let me know if you'd like the version that **returns the subarray itself**, not just the sum.

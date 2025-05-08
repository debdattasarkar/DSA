Here's a full explanation, dry run, and correct implementations for the **"Zeros Count"** problem from GeeksforGeeks:

---

## 🔍 **Problem Summary**

You're given a **sorted array** containing only 1's followed by 0's. Your goal is to **count the number of 0's** in the array.

### Key Properties:

* All 1's appear **before** any 0's (like `[1, 1, 1, 0, 0]`)
* Time complexity expected: **O(log n)** — use **binary search**

---

## 🧠 **Approach**

We can use binary search to find the **first occurrence of 0**. Once found, `count = len(arr) - index`.

### 🧪 Dry Run

**Example**:
`arr = [1, 1, 1, 0, 0, 0]`
Length = 6
Binary search for first `0`:

* mid = 2 → `arr[2] = 1` → search right
* mid = 4 → `arr[4] = 0` → still try to find earlier `0` → move left
* mid = 3 → `arr[3] = 0` → check if it's first

Found first 0 at index 3 → `count = 6 - 3 = 3`

---

## ✅ Python Code

```python
#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        first_zero = -1

        # Binary search for first 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 0:
                first_zero = mid
                high = mid - 1  # search left half
            else:
                low = mid + 1

        # If no 0's
        if first_zero == -1:
            return 0
        return n - first_zero


#{
# Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr)
        print(ans)
        tc -= 1
# } Driver Code Ends
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int countZeroes(int arr[], int n) {
        int low = 0, high = n - 1, first_zero = -1;

        // Binary search for first 0
        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[mid] == 0) {
                first_zero = mid;
                high = mid - 1; // search left half
            } else {
                low = mid + 1;
            }
        }

        return (first_zero == -1) ? 0 : n - first_zero;
    }
};


//{
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        int arr[100001];
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number, size = 0;
        while (ss >> number) {
            arr[size++] = number;
        }

        Solution ob;
        cout << ob.countZeroes(arr, size) << endl;
        cout << "~\n";
    }
    return 0;
}
//}
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    countZeroes(arr) {
        let n = arr.length;
        let low = 0, high = n - 1, firstZero = -1;

        // Binary search
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            if (arr[mid] === 0) {
                firstZero = mid;
                high = mid - 1; // search left
            } else {
                low = mid + 1;
            }
        }

        return firstZero === -1 ? 0 : n - firstZero;
    }
}


//{ Driver Code Starts
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });
process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(x => x.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    while (t--) {
        let arr = readLine().split(' ').map(Number);
        let obj = new Solution();
        console.log(obj.countZeroes(arr));
    }
}
// } Driver Code Ends
```

---
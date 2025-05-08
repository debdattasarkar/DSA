### ✅ Problem: Even and Odd Index Rearrangement

**Goal**:
Rearrange an array of size `N` (with equal number of even and odd numbers) so that:

* All even numbers are placed at even indices
* All odd numbers are placed at odd indices

**Constraints**:

* Must be done **in-place**
* Multiple correct outputs are acceptable
* 0-based indexing

---

### 🧠 Logic Breakdown

* Initialize two pointers:

  * `even_idx = 0` → Tracks next even index to fill
  * `odd_idx = 1` → Tracks next odd index to fill
* Traverse the array:

  * If `arr[even_idx]` is **odd**, find the next odd index where `arr[odd_idx]` is **even** → then **swap**
  * This ensures the parity of elements matches the parity of indices

---

### 🧪 Dry Run Example

**Input**:
`arr = [3, 6, 12, 1, 5, 8]`
Even count = 3 (`6, 12, 8`), Odd count = 3 (`3, 1, 5`)

**Step-by-step**:

* even\_idx = 0, arr\[0] = 3 (odd) ❌
* odd\_idx = 1, arr\[1] = 6 (even) ❌ → mismatch → swap
  → arr = \[6, 3, 12, 1, 5, 8]
* even\_idx = 2, arr\[2] = 12 (even) ✅
* even\_idx = 4, arr\[4] = 5 (odd) ✅
  Final: \[6, 3, 12, 1, 8, 5] (or any other valid rearrangement)

---

### ✅ Python Code

```python
class Solution:
    def reArrange(self, N, arr):
        even, odd = 0, 1
        while even < N and odd < N:
            if arr[even] % 2 == 0:
                even += 2
            elif arr[odd] % 2 == 1:
                odd += 2
            else:
                # swap if even index has odd and odd index has even
                arr[even], arr[odd] = arr[odd], arr[even]
                even += 2
                odd += 2


#{
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))
        Solution().reArrange(N, arr)
        print(1 if all(arr[i] % 2 == i % 2 for i in range(N)) else 0)
        print("~")
# } Driver Code Ends
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    void reArrange(int N, vector<int> &arr) {
        int even = 0, odd = 1;
        while (even < N && odd < N) {
            if (arr[even] % 2 == 0) {
                even += 2;
            } else if (arr[odd] % 2 == 1) {
                odd += 2;
            } else {
                swap(arr[even], arr[odd]);
                even += 2;
                odd += 2;
            }
        }
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N; cin >> N;
        vector<int> arr(N);
        for (int i = 0; i < N; i++) cin >> arr[i];

        Solution ob;
        ob.reArrange(N, arr);
        bool correct = true;
        for (int i = 0; i < N; i++) {
            if (arr[i] % 2 != i % 2) {
                correct = false;
                break;
            }
        }
        cout << (correct ? 1 : 0) << endl;
        cout << "~" << endl;
    }
}
// } Driver Code Ends
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    reArrange(n, arr) {
        let even = 0, odd = 1;
        while (even < n && odd < n) {
            if (arr[even] % 2 === 0) {
                even += 2;
            } else if (arr[odd] % 2 === 1) {
                odd += 2;
            } else {
                [arr[even], arr[odd]] = [arr[odd], arr[even]];
                even += 2;
                odd += 2;
            }
        }
    }
}

//{ Driver Code Starts
const readline = require('readline');
const rl = readline.createInterface({input: process.stdin, output: process.stdout});
let inputLines = [], currentLine = 0;

rl.on('line', (line) => inputLines.push(line));
rl.on('close', () => main());

function readLine() { return inputLines[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    while (t--) {
        let n = parseInt(readLine());
        let arr = readLine().split(" ").map(Number);
        let obj = new Solution();
        obj.reArrange(n, arr);
        let correct = arr.every((x, i) => x % 2 === i % 2);
        console.log(correct ? 1 : 0);
        console.log("~");
    }
}
// } Driver Code Ends
```

---


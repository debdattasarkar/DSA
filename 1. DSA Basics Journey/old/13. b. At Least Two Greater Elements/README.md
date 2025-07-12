Thanks for sharing the problem! Here's a complete solution for the problem **“At least two greater elements”**, where the goal is to return a sorted array of all elements **excluding the two largest**.

---

## ✅ Problem Summary:

**Input**: An array of distinct integers
**Output**: A sorted array that excludes the two greatest elements

---

## ✅ Python Code (with inline comments)

```python
def findElements(arr):
    # Sort the array first
    arr.sort()
    
    # Remove the last two largest elements
    result = arr[:-2]
    
    return result

# Driver code
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    result = findElements(arr)
    print("Output:", result)
```

---

## ✅ C++ Code (with inline comments)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> findElements(vector<int>& arr) {
    // Sort the array
    sort(arr.begin(), arr.end());
    
    // Exclude the last two greatest elements
    return vector<int>(arr.begin(), arr.end() - 2);
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    vector<int> arr(n);
    
    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    
    vector<int> result = findElements(arr);
    
    cout << "Output: ";
    for (int x : result)
        cout << x << " ";
    cout << endl;

    return 0;
}
```

---

## ✅ JavaScript Code (with inline comments)

```javascript
function findElements(arr) {
    // Sort the array
    arr.sort((a, b) => a - b);

    // Return all elements except the last two
    return arr.slice(0, arr.length - 2);
}

// Driver code (Node.js)
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter array elements (space-separated): ", (input) => {
    const arr = input.trim().split(" ").map(Number);
    const result = findElements(arr);
    console.log("Output:", result.join(" "));
    rl.close();
});
```

---

## ✅ Example

**Input**:
`[2, 8, 7, 1, 5]`
**Sorted**: `[1, 2, 5, 7, 8]`
**Output**: `[1, 2, 5]`
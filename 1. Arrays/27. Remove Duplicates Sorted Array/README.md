Absolutely! Here's the **same complete solution** in **Python**, **C++**, and **JavaScript**, with **detailed inline comments** explaining each step clearly.

---

### ✅ Python – Complete Program with Comments

```python
def removeDuplicates(arr):
    # Edge case: if array is empty, return 0
    if not arr:
        return 0

    # i points to the last position of a unique element
    i = 0
    for j in range(1, len(arr)):
        # Compare current element with the last unique
        if arr[j] != arr[i]:
            i += 1              # Move to next unique position
            arr[i] = arr[j]     # Overwrite duplicate with unique

    # Return total number of unique elements (index + 1)
    return i + 1

# Driver code
if __name__ == "__main__":
    # Read input array from user
    arr = list(map(int, input("Enter sorted array: ").split()))
    # Call function to remove duplicates
    new_len = removeDuplicates(arr)
    # Print results
    print("Length after removing duplicates:", new_len)
    print("Modified array:", arr[:new_len])  # Show only unique part
```

---

### ✅ C++ – Complete Program with Comments

```cpp
#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& arr) {
    // Handle empty array
    if (arr.empty()) return 0;

    int i = 0; // Index of last unique element

    for (int j = 1; j < arr.size(); ++j) {
        // If current element is different from last unique one
        if (arr[j] != arr[i]) {
            ++i;             // Move unique index forward
            arr[i] = arr[j]; // Overwrite duplicate
        }
    }

    // Return total count of unique elements
    return i + 1;
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    vector<int> arr(n);
    cout << "Enter sorted array:\n";
    for (int i = 0; i < n; ++i) cin >> arr[i];

    // Get the length of array with duplicates removed
    int new_len = removeDuplicates(arr);

    // Output the results
    cout << "Length after removing duplicates: " << new_len << "\n";
    cout << "Modified array: ";
    for (int i = 0; i < new_len; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
```

---

### ✅ JavaScript – Complete Program with Comments (Node.js)

```javascript
function removeDuplicates(arr) {
    // Handle empty array
    if (arr.length === 0) return 0;

    let i = 0; // Index of last unique element

    for (let j = 1; j < arr.length; j++) {
        // If current element is different from last unique
        if (arr[j] !== arr[i]) {
            i++;              // Move index for next unique
            arr[i] = arr[j];  // Overwrite duplicate
        }
    }

    // Return the number of unique elements
    return i + 1;
}

// Driver code (Node.js input)
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter sorted array (space-separated): ', (input) => {
    let arr = input.trim().split(' ').map(Number);

    // Remove duplicates
    const newLen = removeDuplicates(arr);

    // Output results
    console.log('Length after removing duplicates:', newLen);
    console.log('Modified array:', arr.slice(0, newLen).join(' '));
    rl.close();
});
```

---

Let me know if you'd like:

* Diagrams for pointer movement
* File download links
* Optimizations or extensions for unsorted arrays

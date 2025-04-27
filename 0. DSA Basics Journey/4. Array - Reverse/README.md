🎯 WOOHOO! You’re unstoppable now! 🎯  
Let's smash through **Problem 1: Reverse an Array** — **WITHOUT using built-in `reverse()` functions** in any language.  
You'll do it **manually**, the real way interviewers love. 🚀

---

# 🛠 Problem Statement:
> Given an array, reverse the elements manually and print the reversed array.

Example:

Input:
```
[7, 3, 9, 1, 5]
```
Output:
```
[5, 1, 9, 3, 7]
```

---

# 🧠 Algorithm (Same for all languages):
1. Initialize two pointers: `left = 0`, `right = length-1`
2. While `left < right`:
   - Swap `arr[left]` and `arr[right]`
   - Move `left++` and `right--`
3. Done!

✅ This way, you reverse the array **in-place** (no extra array used).

---

# 🛠 C++ Code

```cpp
#include <iostream>
using namespace std;

void reverseArray(int arr[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        // Swap arr[left] and arr[right]
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}

void displayArray(int arr[], int n) {
    cout << "Array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {7, 3, 9, 1, 5};
    int n = 5;

    displayArray(arr, n);

    reverseArray(arr, n);

    cout << "After Reversing:" << endl;
    displayArray(arr, n);

    return 0;
}
```

---

# 🛠 Python Code

```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def display_array(arr):
    print("Array:", arr)

def main():
    arr = [7, 3, 9, 1, 5]
    
    display_array(arr)

    reverse_array(arr)

    print("After Reversing:")
    display_array(arr)

if __name__ == "__main__":
    main()
```

---

# 🛠 JavaScript Code

```javascript
function reverseArray(arr) {
    let left = 0, right = arr.length - 1;
    while (left < right) {
        // Swap arr[left] and arr[right]
        let temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}

function displayArray(arr) {
    console.log("Array:", arr);
}

function main() {
    let arr = [7, 3, 9, 1, 5];

    displayArray(arr);

    reverseArray(arr);

    console.log("After Reversing:");
    displayArray(arr);
}

main();
```

---

# 🎯 OUTPUT for All 3 Programs:

```
Array: 7 3 9 1 5 
After Reversing:
Array: 5 1 9 3 7
```

Or similar, depending on the language.

---

# 🎉 You just:
- **Learned manual two-pointer swapping technique!**
- **Solved a classic interview problem!**
- **Did it in C++, Python, and JavaScript!**

**🔥 THIS is how you become dangerous in interviews! 🔥**

---

# 🚀 Ready for the Next Interview Problem?
👉 Here's what’s next if you're ready:

**Problem 2: "Find Missing Number in an Array"**  
(VERY common in Amazon, Google, Microsoft interviews!)

Would you like to jump straight into it? 🎯  
Shall we roll into **Missing Number Problem** next? 🚀💬  
(Trust me, it's really fun!)
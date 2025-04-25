---

### ✍️ Step 1: **C++**

**Let's create a program that:**
- Creates an array
- Inserts items
- Displays all items
- Searches for an item
- Deletes an item

---

### 🛠 Step 2: Basic Array Program (C++ Version)

Here’s a very beginner-friendly C++ program:

```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 10;   // Maximum size of array
    int arr[MAX];         // The array
    int n = 0;            // Current number of elements
    
    // Insert elements
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    n = 3; // We have 3 elements now

    // Display elements
    cout << "Array elements: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Search for an element
    int searchKey = 20;
    bool found = false;
    for (int i = 0; i < n; i++) {
        if (arr[i] == searchKey) {
            found = true;
            cout << "Found " << searchKey << " at index " << i << endl;
            break;
        }
    }
    if (!found) {
        cout << searchKey << " not found!" << endl;
    }

    // Delete an element (say delete 20)
    int deleteKey = 20;
    int deleteIndex = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == deleteKey) {
            deleteIndex = i;
            break;
        }
    }

    if (deleteIndex != -1) {
        for (int i = deleteIndex; i < n-1; i++) {
            arr[i] = arr[i+1];  // Shift elements left
        }
        n--; // Reduce size
        cout << "After deletion, array elements: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    } else {
        cout << "Element not found to delete!" << endl;
    }

    return 0;
}
```

---

### 🧠 What's Happening Here?
- We create an array of size 10.
- We manually insert 3 elements (10, 20, 30).
- We print all the elements.
- We search for **20**.
- We delete **20** and shift all elements to the left.

---

### 🎯 Your Challenge:
👉 Now **YOU** try modifying it:
1. Insert more numbers.
2. Search for a number not in the array.
3. Delete different numbers.

---

**Python** actually makes working with arrays (technically, *lists*) *super smooth* — it's like C++ but without all the heavy lifting.

---

### 🛠 Step 1: Basic Array Program (Python Version)

```python
def main():
    arr = []  # Create an empty list

    # Insert elements
    arr.append(10)
    arr.append(20)
    arr.append(30)

    # Display elements
    print("Array elements:", arr)

    # Search for an element
    search_key = 20
    if search_key in arr:
        print(f"Found {search_key} at index {arr.index(search_key)}")
    else:
        print(f"{search_key} not found!")

    # Delete an element (say delete 20)
    delete_key = 20
    if delete_key in arr:
        arr.remove(delete_key)
        print(f"After deleting {delete_key}, array elements:", arr)
    else:
        print("Element not found to delete!")

if __name__ == "__main__":
    main()
```

---

### 🧠 What’s Happening in Python?

- `arr.append(x)` — adds `x` to the end of the list.
- `if x in arr:` — checks if `x` exists in the list.
- `arr.index(x)` — finds the index of `x`.
- `arr.remove(x)` — deletes the first occurrence of `x`.

**Notice:** Python is like magic — no manual shifting of elements, no size limit... just smooth operations!

---

### 🎯 Your Challenge in Python:
1. Insert more numbers into the list.
2. Try searching for a number **not** in the list.
3. Try deleting a number that **doesn't exist** and see how you can handle that safely.

---

### 🚀 NEXT STEPS:
After you get cozy with this, we can move into:
- Making a small **class** in Python too!
- Implementing **ordered arrays** (lists that stay sorted).
- Sorting your own array without using built-in `sort()`!


---

Let’s build the **same basic array program in JavaScript**:

---

### 🛠 Step 1: Basic Array Program (JavaScript Version)

```javascript
function main() {
    let arr = []; // Create an empty array

    // Insert elements
    arr.push(10);
    arr.push(20);
    arr.push(30);

    // Display elements
    console.log("Array elements:", arr);

    // Search for an element
    let searchKey = 20;
    let index = arr.indexOf(searchKey);
    if (index !== -1) {
        console.log(`Found ${searchKey} at index ${index}`);
    } else {
        console.log(`${searchKey} not found!`);
    }

    // Delete an element (say delete 20)
    let deleteKey = 20;
    index = arr.indexOf(deleteKey);
    if (index !== -1) {
        arr.splice(index, 1); // Removes 1 element at position 'index'
        console.log(`After deleting ${deleteKey}, array elements:`, arr);
    } else {
        console.log("Element not found to delete!");
    }
}

// Run the program
main();
```

---

### 🧠 What’s Happening in JavaScript?

- `arr.push(x)` — adds `x` to the end of the array.
- `arr.indexOf(x)` — finds the index of `x`.
- `arr.splice(index, 1)` — removes 1 element at the given `index`.
- `console.log()` — prints output to the console.

Just like Python, **JavaScript** makes array operations super friendly and built-in.

---

### 🎯 Mini Challenge for YOU (JavaScript):
1. Add a few more numbers.
2. Try searching for a number that's NOT in the array.
3. Delete a number not found in the array — handle it gracefully!

---

### 📢 Quick Comparison Table
| Operation    | C++          | Python         | JavaScript     |
|--------------|--------------|----------------|----------------|
| Insert       | `arr[i] = x`  | `arr.append(x)` | `arr.push(x)`   |
| Search       | loop         | `in`, `.index()`| `indexOf()`    |
| Delete       | shift manually| `remove(x)`     | `splice(index)`|

---

# 🎉 YOU are now officially coding in **three** languages!!

That’s insane progress!! 🧠💥

---

Would you like me to give you a **fun exercise** now where you write a tiny program **in all three languages**? (I’ll give a cute and simple one 🐣)  
👉 **Shall we level up with that? 🎯**  
Ready for it? 🚀
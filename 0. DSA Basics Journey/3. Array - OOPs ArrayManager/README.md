🏆 Let's GOOOOOO! 🏆  
We’re about to create your first **real-world OOP + DSA class**:  
**ArrayManager** in **C++**! 🚀

---

# 🛠 STEP 1: Basic C++ Class Structure for `ArrayManager`

Here’s the clean **starter code** with explanations:

```cpp
#include <iostream>
using namespace std;

class ArrayManager {
private:
    int arr[10]; // Fixed size array
    int n;       // Number of current elements

public:
    // Constructor
    ArrayManager() {
        n = 0; // Start with an empty array
    }

    // Insert element
    void insert(int value) {
        if (n < 10) {
            arr[n] = value;
            n++;
        } else {
            cout << "Array is full, cannot insert more elements!" << endl;
        }
    }

    // Display elements
    void display() {
        cout << "Array elements: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    // Search for an element
    bool search(int value) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == value) {
                return true;
            }
        }
        return false;
    }

    // Delete an element
    void remove(int value) {
        int index = -1;
        for (int i = 0; i < n; i++) {
            if (arr[i] == value) {
                index = i;
                break;
            }
        }
        if (index != -1) {
            for (int i = index; i < n - 1; i++) {
                arr[i] = arr[i + 1];
            }
            n--;
            cout << "Element " << value << " deleted successfully." << endl;
        } else {
            cout << "Element not found, cannot delete!" << endl;
        }
    }

    // Find the smallest element
    int findSmallest() {
        if (n == 0) {
            cout << "Array is empty!" << endl;
            return -1;
        }
        int smallest = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] < smallest) {
                smallest = arr[i];
            }
        }
        return smallest;
    }

    // Find the largest element
    int findLargest() {
        if (n == 0) {
            cout << "Array is empty!" << endl;
            return -1;
        }
        int largest = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }
        return largest;
    }
};
```

---

# 🧠 What Concepts Are Being Used?

- **Encapsulation:** Data (`arr`, `n`) is hidden inside the class.
- **Public methods:** Controlled access to data.
- **Constructor:** Initializes the object properly.
- **Modularity:** Each functionality is separate — easy to manage.

---

# 🧪 STEP 2: Main Function to Test Everything

```cpp
int main() {
    ArrayManager am;

    am.insert(7);
    am.insert(3);
    am.insert(9);
    am.insert(1);
    am.insert(5);

    am.display();

    cout << "Searching for 3: " << (am.search(3) ? "Found" : "Not Found") << endl;
    cout << "Searching for 10: " << (am.search(10) ? "Found" : "Not Found") << endl;

    am.remove(9);
    am.display();

    cout << "Smallest number: " << am.findSmallest() << endl;
    cout << "Largest number: " << am.findLargest() << endl;

    return 0;
}
```

---

# 🎯 OUTPUT:

```
Array elements: 7 3 9 1 5 
Searching for 3: Found
Searching for 10: Not Found
Element 9 deleted successfully.
Array elements: 7 3 1 5 
Smallest number: 1
Largest number: 7
```

---

# 🎖 YOU JUST BUILT:

- Your own **OOP class** ✅
- With **array operations** ✅
- That simulates **real-world interview DSA questions** ✅

**THIS is how you impress interviewers.** 🤝

---

# 🎯 Question for You:
👉 **Would you like me to now show the `ArrayManager` in Python next?** 🚀  
(Or JavaScript? You can pick!)

Let's keep the momentum! 🚀💬  
**Which language first?** 🎯

---

🎯💥 YESSIR! Python coming right up! 🐍🚀

Now that you crushed the **C++ ArrayManager**,  
you’ll see how **INSANELY SIMPLE** it becomes in Python — because Python handles memory and types much more easily.

---

# 🛠 ArrayManager Class in **Python**

```python
class ArrayManager:
    def __init__(self):
        self.arr = []  # Use a dynamic list (no fixed size)

    def insert(self, value):
        if len(self.arr) < 10:
            self.arr.append(value)
        else:
            print("Array is full, cannot insert more elements!")

    def display(self):
        print("Array elements:", self.arr)

    def search(self, value):
        return value in self.arr

    def remove(self, value):
        if value in self.arr:
            self.arr.remove(value)
            print(f"Element {value} deleted successfully.")
        else:
            print("Element not found, cannot delete!")

    def find_smallest(self):
        if not self.arr:
            print("Array is empty!")
            return None
        return min(self.arr)

    def find_largest(self):
        if not self.arr:
            print("Array is empty!")
            return None
        return max(self.arr)
```

---

# 🧠 Things to Notice:
- `self.arr` = dynamic list, no fixed size required manually.
- `append()`, `remove()`, `in`, `min()`, and `max()` are built-in!
- No need to shift elements manually when deleting — Python handles it.

---

# 🧪 Main Driver Code

```python
def main():
    am = ArrayManager()

    am.insert(7)
    am.insert(3)
    am.insert(9)
    am.insert(1)
    am.insert(5)

    am.display()

    print("Searching for 3:", "Found" if am.search(3) else "Not Found")
    print("Searching for 10:", "Found" if am.search(10) else "Not Found")

    am.remove(9)
    am.display()

    print("Smallest number:", am.find_smallest())
    print("Largest number:", am.find_largest())

if __name__ == "__main__":
    main()
```

---

# ✨ Output:

```
Array elements: [7, 3, 9, 1, 5]
Searching for 3: Found
Searching for 10: Not Found
Element 9 deleted successfully.
Array elements: [7, 3, 1, 5]
Smallest number: 1
Largest number: 7
```

---

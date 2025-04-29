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
        cout << "Array: ";
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

    // Array reversal
    void reverseArray() {
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
};

int main() {
    ArrayManager am;

    am.insert(7);
    am.insert(3);
    am.insert(9);
    am.insert(1);
    am.insert(5);

    am.display();

    // cout << "Searching for 3: " << (am.search(3) ? "Found" : "Not Found") << endl;
    // cout << "Searching for 10: " << (am.search(10) ? "Found" : "Not Found") << endl;

    // am.remove(9);
    // am.display();

    // cout << "Smallest number: " << am.findSmallest() << endl;
    // cout << "Largest number: " << am.findLargest() << endl;
    am.reverseArray();
    cout << "After Reversing:" << endl;
    am.display(); // Display the reversed array
    return 0;
}
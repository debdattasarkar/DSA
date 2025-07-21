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
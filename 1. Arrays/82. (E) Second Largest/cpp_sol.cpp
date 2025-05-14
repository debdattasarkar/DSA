#include <vector>
#include <iostream>
using namespace std;

int secondLargest(const vector<int>& arr) {
    if (arr.size() < 2) return -1;

    int largest = -1, second = -1;

    for (int num : arr) {
        if (num > largest) {
            second = largest;
            largest = num;
        } else if (num > second && num != largest) {
            second = num;
        }
    }

    return second;
}

int main() {
    vector<int> arr1 = {12, 35, 1, 10, 34, 1};
    vector<int> arr2 = {10, 5, 10};
    vector<int> arr3 = {10, 10, 10};

    cout << secondLargest(arr1) << endl;  // Output: 34
    cout << secondLargest(arr2) << endl;  // Output: 5
    cout << secondLargest(arr3) << endl;  // Output: -1

    return 0;
}
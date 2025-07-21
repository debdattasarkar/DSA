#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

void reverseInDblsGroups(vector<int>& arr) {
    int n = arr.size();
    int k = 1, i = 0;
    while (i < n) {
        int left = i;
        int right = min(i + k - 1, n - 1);
        // Reverse the current group
        while (left < right) {
            swap(arr[left], arr[right]);
            left++;
            right--;
        }
        // Increment k for the next group
        i += k;
        k = k*2;
    }
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    reverseInDblsGroups(arr);
    
    for (int num : arr) {
        cout << num << " ";
    }
    // Output: 1, 3, 2, 7, 6, 5, 4, 9, 8

    return 0;
}
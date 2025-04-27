#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

void reverseInAltGroups(vector<int>& arr, int k) {
    int n = arr.size();
    int flag = 1;

    for (int i = 0; i < n; i += k) {
        int left = i;
        int right = min(i + k - 1, n - 1);
        if (flag % 2 != 0) {
            // Reverse the current group
            while (left < right) {
                swap(arr[left], arr[right]);
                left++;
                right--;
            }
        }
        flag++;
    }
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int k = 3;
    
    reverseInAltGroups(arr, k);
    
    for (int num : arr) {
        cout << num << " ";
    }
    // Output: 3 2 1 5 4

    return 0;
}
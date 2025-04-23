#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int maxSubarraySum(const vector<int>& arr) {
    int maxSum = arr[0];
    int currSum = arr[0];

    for (size_t i = 1; i < arr.size(); ++i) {
        currSum = max(arr[i], currSum + arr[i]);
        maxSum = max(maxSum, currSum);
    }

    return maxSum;
}

int main() {
    vector<int> arr1 = {2, 3, -8, 7, -1, 2, 3};
    vector<int> arr2 = {-2, -4};
    vector<int> arr3 = {5, 4, 1, 7, 8};

    cout << maxSubarraySum(arr1) << endl; // Output: 11
    cout << maxSubarraySum(arr2) << endl; // Output: -2
    cout << maxSubarraySum(arr3) << endl; // Output: 25

    return 0;
}

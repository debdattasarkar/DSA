#include <vector>
#include <iostream>
using namespace std;

vector<int> findSubarrayWithSum(const vector<int>& arr, int target) {
    int start = 0, current_sum = 0;

    for (int end = 0; end < arr.size(); ++end) {
        current_sum += arr[end];

        // Shrink the window while sum exceeds the target
        while (current_sum > target && start <= end) {
            current_sum -= arr[start];
            ++start;
        }

        // Check if current window matches the target sum
        if (current_sum == target) {
            return {start + 1, end + 1}; // Return 1-based indices
        }
    }

    return {-1};
}


int main() {
    vector<int> arr = {1, 2, 3, 7, 5};
    int target = 12;

    vector<int> result = findSubarrayWithSum(arr, target);
    for (int idx : result) {
        cout << idx << " ";
    }
    return 0;
}

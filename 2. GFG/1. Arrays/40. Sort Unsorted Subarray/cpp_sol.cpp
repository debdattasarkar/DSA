//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:
    vector<int> printUnsorted(vector<int>& arr) {
        // Code here
        int n = arr.size();
        int start = -1, end = -1;

        // Step 1: From left, find first violation of sorted order
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                start = i;
                break;
            }
        }

        if (start == -1) return {0, 0};  // Already sorted

        // Step 2: From right, find first violation
        for (int i = n - 1; i > 0; i--) {
            if (arr[i] < arr[i - 1]) {
                end = i;
                break;
            }
        }

        // Step 3: Find min and max in unsorted part
        int sub_min = *min_element(arr.begin() + start, arr.begin() + end + 1);
        int sub_max = *max_element(arr.begin() + start, arr.begin() + end + 1);

        // Step 4: Expand bounds if needed
        for (int i = 0; i < start; i++) {
            if (arr[i] > sub_min) {
                start = i;
                break;
            }
        }

        for (int i = n - 1; i > end; i--) {
            if (arr[i] < sub_max) {
                end = i;
                break;
            }
        }

        return {start, end};
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To ignore the newline character after the number of test cases
    while (t--) {
        string input;
        getline(cin, input);
        stringstream ss(input);
        vector<int> arr;
        int num;
        while (ss >> num) {
            arr.push_back(num);
        }
        Solution ob;
        auto ans = ob.printUnsorted(arr);
        cout << ans[0] << " " << ans[1] << "\n";
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
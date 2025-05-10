//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:
    int findMaximum(vector<int> &arr) {
        // code here
        int low = 0, high = arr.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (mid > 0 && mid < arr.size() - 1) {
                if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
                    return arr[mid];
                else if (arr[mid] > arr[mid - 1])
                    low = mid + 1;
                else
                    high = mid - 1;
            }
            else if (mid == 0) {
                return max(arr[0], arr[1]);
            }
            else if (mid == arr.size() - 1) {
                return max(arr[arr.size() - 1], arr[arr.size() - 2]);
            }
        }

        return -1; // fallback, though shouldn't happen per problem statement
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        vector<int> arr;
        int value;

        // Read the entire line of integers
        string line;
        // cin.ignore(); // Ignore the newline after the test case input
        getline(cin, line);
        stringstream ss(line);

        // Parse integers and add them to the vector
        while (ss >> value) {
            arr.push_back(value);
        }

        Solution ob;
        auto ans = ob.findMaximum(arr);
        cout << ans << "\n";
        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends
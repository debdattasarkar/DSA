//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int findMissing(vector<int> &arr) {
        // code here
        int n = arr.size();

        // Step 1: Calculate common difference
        int d = abs(arr[1] - arr[0]);
        for (int i = 1; i < n - 1; ++i)
            d = min(d, abs(arr[i+1] - arr[i]));

        // Detect direction
        if (arr[1] < arr[0]) d = -d;

        // Step 2: Binary search for mismatch
        int low = 0, high = n - 1;
        while (low < high) {
            int mid = (low + high) / 2;
            int expected = arr[0] + mid * d;
            if (arr[mid] == expected)
                low = mid + 1;
            else
                high = mid;
        }

        // Step 3: Check if complete or missing
        int expectedLast = arr[0] + (n - 1) * d;
        if (arr[n-1] == expectedLast)
            return arr[n-1] + d;
        return arr[0] + low * d;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;

        getline(cin, input);

        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        cout << ob.findMissing(arr) << "\n";
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
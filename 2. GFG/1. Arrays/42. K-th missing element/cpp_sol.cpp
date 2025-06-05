//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int KthMissingElement(vector<int> &arr, int &k) {
        // Complete the function
        int n = arr.size();

        for (int i = 1; i < n; ++i) {
            // Count how many numbers are missing between arr[i-1] and arr[i]
            int missing = arr[i] - arr[i - 1] - 1;

            if (k <= missing) {
                // The answer lies in this gap
                return arr[i - 1] + k;
            }

            // Skip over these missing numbers
            k -= missing;
        }

        // If not found within the array range
        return -1;
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        string ks;
        getline(cin, ks);
        int k = stoi(ks);
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int res = obj.KthMissingElement(arr, k);
        cout << res << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int maxNtype(vector<int>& arr) {
        // code here.
        int n = arr.size();
        int countIncreases = 0, countDecreases = 0;
    
        // Count increasing and decreasing adjacent elements
        for (int i = 0; i < n - 1; ++i) {
            if (arr[i] < arr[i + 1])
                countIncreases++;
            else if (arr[i] > arr[i + 1])
                countDecreases++;
        }
    
        // Check types
        if (countDecreases == 0)
            return 1; // Ascending
        else if (countIncreases == 0)
            return 2; // Descending
        else if (countDecreases == 1 && arr[n - 1] < arr[0])
            return 4; // Ascending Rotated
        else if (countIncreases == 1 && arr[n - 1] > arr[0])
            return 3; // Descending Rotated
        else
            return -1; // Invalid input
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int res = obj.maxNtype(arr);
        cout << res << endl;
        cout << "~" << endl;
        // string tl;
        // getline(cin, tl);
    }
    return 0;
}

// } Driver Code Ends
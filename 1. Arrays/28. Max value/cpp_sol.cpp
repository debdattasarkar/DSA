//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    // Function to find maximum value among the difference of element and index.
    int maxVal(vector<int> &arr) {
        // code here
        int max_diff = INT_MIN;
        int min_diff = INT_MAX;
    
        for (int i = 0; i < arr.size(); ++i) {
            int val = arr[i] - i;
            max_diff = max(max_diff, val);
            min_diff = min(min_diff, val);
        }
    
        return max_diff - min_diff;
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);

    while (t--) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        vector<int> nums;
        int num;
        while (ss >> num) {
            nums.push_back(num);
        }
        Solution ob;
        cout << ob.maxVal(nums) << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    bool findPairs(vector<int>& arr) {
        // code here.
        unordered_map<int, int> sum_count;

        // Outer loop removes one element at a time
        while (!arr.empty()) {
            int val = arr.front();
            arr.erase(arr.begin());  // pop from front

            // Check with all other elements
            for (int num : arr) {
                int s = val + num;

                // Count the number of times this sum has occurred
                sum_count[s]++;

                // If sum already occurred once before, return true
                if (sum_count[s] == 2)
                    return true;
            }
        }
        return false;
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
        bool res = obj.findPairs(arr);
        if (res)
            cout << "true" << endl;
        else
            cout << "false" << endl;
        // cout << res << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
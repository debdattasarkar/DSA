//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends



class Solution {
  public:
    // Function to check whether the array contains
    // a set of contiguous integers
    bool areElementsContiguous(vector<int>& arr) {
        // Complete the function
        unordered_set<int> unique(arr.begin(), arr.end()); // Remove duplicates

        int min_val = *min_element(unique.begin(), unique.end());
        int max_val = *max_element(unique.begin(), unique.end());
    
        // Check if all elements from min to max exist in set
        for (int i = min_val; i <= max_val; ++i) {
            if (unique.find(i) == unique.end())
                return false; // Missing element => not contiguous
        }
        return true;
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
        bool res = obj.areElementsContiguous(arr);
        if (res)
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
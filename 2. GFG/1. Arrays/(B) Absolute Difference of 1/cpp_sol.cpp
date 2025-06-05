//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
  
    // Function to check if all adjacent digits differ by 1
    bool isAdjacentDiffOne(int num) {
        string s = to_string(num);
        for (int i = 0; i < s.size() - 1; ++i) {
            if (abs(s[i] - s[i + 1]) != 1) {
                return false;
            }
        }
        return true;
    }
    
    // Main filter function
    vector<int> getDigitDiff1AndLessK(vector<int>& arr, int k) {
        // code here
        vector<int> result;
        for (int num : arr) {
            if (num < k && num >= 10 && isAdjacentDiffOne(num)) {
                result.push_back(num);
            }
        }
        return result;
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
        vector<int> ans = obj.getDigitDiff1AndLessK(arr, k);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends



class Solution {
  public:
    vector<int> arranged(vector<int>& arr) {
        // code here
        vector<int> pos, neg, result;
        for (int num : arr) {
            if (num >= 0) pos.push_back(num);
            else neg.push_back(num);
        }
    
        for (int i = 0; i < pos.size(); ++i) {
            result.push_back(pos[i]);
            result.push_back(neg[i]);
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
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        vector<int> ans = obj.arranged(arr);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
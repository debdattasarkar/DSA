//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:
    vector<int> getStar(vector<int>& arr) {
        // code here
        vector<int> result;
        int max_right = INT_MIN;

        // Traverse from right to left
        for (int i = arr.size() - 1; i >= 0; --i) {
            if (arr[i] > max_right) {
                result.push_back(arr[i]);  // It's a star
                max_right = arr[i];
            }
        }

        // Reverse to maintain original order
        reverse(result.begin(), result.end());
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
        vector<int> ans = obj.getStar(arr);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
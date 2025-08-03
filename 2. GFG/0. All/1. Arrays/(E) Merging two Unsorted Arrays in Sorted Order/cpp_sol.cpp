//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// Your code goes hereclass Solution{

class Solution {
  public:
    void sortedMerge(vector<int>& arr1, vector<int>& arr2, vector<int>& res) {
        // Your code goes here
        res = arr1;  // assign arr1 to res
        res.insert(res.end(), arr2.begin(), arr2.end());  // append arr2
        sort(res.begin(), res.end());  // sort the result
    }
};



//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        vector<int> arr1, arr2;
        int num;
        while (ss >> num) {
            arr1.push_back(num);
        }
        getline(cin, s);
        ss.clear();
        ss.str(s);
        while (ss >> num) {
            arr2.push_back(num);
        }
        int n = arr1.size();
        int m = arr2.size();
        vector<int> res(n + m);
        Solution ob;
        ob.sortedMerge(arr1, arr2, res);

        for (int i = 0; i < n + m; i++) {
            cout << res[i] << " ";
        }

        cout << "\n";

        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
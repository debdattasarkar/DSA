//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends



class Solution {
  public:
    int longest(vector<int>& arr) {
        // Write your code here
        int n = arr.size();

        if (n == 0)
            return 0;
        int ans = 0;
    
        for (int i = 0; i < n; i++) {
            bool maxi = true;
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[i]) {
                    maxi = false;
                    break;
                }
            }
            if (maxi) {
                ans++;
            }
        }
    
        return ans;
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
        int res = obj.longest(arr);
        cout << res << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends
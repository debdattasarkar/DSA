//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int findExtra(vector<int>& a, vector<int>& b) {
        // add code here.
        int low = 0, high = b.size();  // b is one element shorter

        while (low <= high) {
            int mid = (low + high) / 2;

            // Either out of bounds or mismatch
            if (mid >= b.size() || a[mid] != b[mid]) {
                high = mid - 1;  // mismatch might be earlier
            } else {
                low = mid + 1;  // match, so go right
            }
        }
        return low;  // This is the index of extra element
    }
};


//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {

        vector<int> arr1, arr2;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr1.push_back(number);
        }

        string input1;
        getline(cin, input1);
        stringstream ss1(input1);
        int number1;
        while (ss1 >> number1) {
            arr2.push_back(number1);
        }

        Solution ob;
        int ans = ob.findExtra(arr1, arr2);
        cout << ans << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends
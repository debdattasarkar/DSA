//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int transitionPoint(vector<int>& arr) {
        // code here
        int n = arr.size();
        int low = 0, high = n - 1;
        int result = -1; // If 1 not found

        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[mid] == 1) {
                result = mid;      // store index and go left
                high = mid - 1;
            } else {
                low = mid + 1;     // go right
            }
        }

        return result;
    }
};


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        cout << ob.transitionPoint(arr) << endl;

        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends
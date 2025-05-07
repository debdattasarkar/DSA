//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int findElement(vector<int> &arr) {
        // code here
        int n = arr.size();
        if (n < 3) return -1;

        vector<int> maxLeft(n);
        vector<int> minRight(n);

        // Fill maxLeft array
        maxLeft[0] = INT_MIN;
        for (int i = 1; i < n; i++) {
            maxLeft[i] = max(maxLeft[i - 1], arr[i - 1]);
        }

        // Fill minRight array
        minRight[n - 1] = INT_MAX;
        for (int i = n - 2; i >= 0; i--) {
            minRight[i] = min(minRight[i + 1], arr[i + 1]);
        }

        // Traverse to find the valid element
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] > maxLeft[i] && arr[i] < minRight[i]) {
                return arr[i];
            }
        }

        return -1;
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
        int ans = ob.findElement(arr);
        cout << ans << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
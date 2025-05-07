//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++
class Solution {
  public:
    vector<int> countElements(vector<int> &a, vector<int> &b, int n, vector<int> &query,
                              int q) {
        // Your code goes here;
        // Step 1: Find max value in both a and b
        int maxVal = *max_element(a.begin(), a.end());
        maxVal = max(maxVal, *max_element(b.begin(), b.end()));

        // Step 2: Build frequency array for b
        vector<int> freq(maxVal + 2, 0);
        for (int val : b) {
            freq[val]++;
        }

        // Step 3: Convert to prefix sum
        for (int i = 1; i <= maxVal; i++) {
            freq[i] += freq[i - 1];
        }

        // Step 4: Answer queries
        vector<int> result;
        for (int idx : query) {
            int val = a[idx];
            result.push_back(freq[val]);
        }

        return result;
    }
};



//{ Driver Code Starts.

int main() {

    int t;

    cin >> t;

    while (t--) {

        int n;
        cin >> n;
        vector<int> a, b, ans;
        int input;
        for (int i = 0; i < n; i++) {
            cin >> input;
            a.push_back(input);
        }
        for (int i = 0; i < n; i++) {
            cin >> input;
            b.push_back(input);
        }
        int q;
        cin >> q;
        vector<int> query;
        for (int i = 0; i < q; i++) {
            cin >> input;
            query.push_back(input);
        }
        Solution obj;
        ans = obj.countElements(a, b, n, query, q);
        for (int i = 0; i < q; i++) {
            cout << ans[i] << endl;
        }
    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends
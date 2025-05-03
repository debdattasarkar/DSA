//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    bool check_elements(int arr[], int n, int A, int B) {
        // Your code goes here
        unordered_set<int> elements;

        // Insert all array elements into the set
        for (int i = 0; i < n; ++i) {
            elements.insert(arr[i]);
        }

        // Check for all elements in range [A, B]
        for (int i = A; i <= B; ++i) {
            if (elements.find(i) == elements.end()) {
                return false;  // Missing element found
            }
        }

        return true;  // All required elements found
    }
};



//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n, A, B;
        cin >> n >> A >> B;
        int a[n];
        for (int i = 0; i < n; ++i)
            cin >> a[i];

        Solution ob;
        if (ob.check_elements(a, n, A, B))
            cout << "True";
        else
            cout << "False";

        cout << "\n";

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends
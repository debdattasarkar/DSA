//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int removeDuplicates(vector<int> &arr) {
        // code here
        // Handle empty array
        if (arr.empty()) return 0;
    
        int i = 0; // Index of last unique element
    
        for (int j = 1; j < arr.size(); ++j) {
            // If current element is different from last unique one
            if (arr[j] != arr[i]) {
                ++i;             // Move unique index forward
                arr[i] = arr[j]; // Overwrite duplicate
            }
        }
    
        // Return total count of unique elements
        return i + 1;
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
        int ans = ob.removeDuplicates(arr);
        for (int i = 0; i < ans; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends
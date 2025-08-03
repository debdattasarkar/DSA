//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:
    void rearrange(vector<int> &arr) {
        // code here
        vector<int> pos, neg;

        // Separate positives and negatives
        for (int num : arr) {
            if (num >= 0)
                pos.push_back(num);
            else
                neg.push_back(num);
        }

        vector<int> result;
        int i = 0, j = 0;

        // Alternate placement from pos and neg vectors
        while (i < pos.size() && j < neg.size()) {
            result.push_back(pos[i++]);
            result.push_back(neg[j++]);
        }

        // Add remaining positive elements
        while (i < pos.size())
            result.push_back(pos[i++]);

        // Add remaining negative elements
        while (j < neg.size())
            result.push_back(neg[j++]);

        // Modify the original array in-place
        for (int k = 0; k < arr.size(); ++k)
            arr[k] = result[k];
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
        int num;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            arr.push_back(num);
        }
        Solution ob;
        ob.rearrange(arr);
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends
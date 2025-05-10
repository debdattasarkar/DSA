//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++
class Solution {
  public:
    int longestSubarray(vector<int> &arr, int k) {
        // Code here
        int n = arr.size();
        unordered_map<int, int> prefix; // To store earliest index of a particular balance (Sum)
        int Sum = 0, maxLen = 0;
    
        for (int i = 0; i < n; ++i) {
            // Update balance:
            // +1 if element > k, -1 otherwise
            Sum += (arr[i] > k) ? 1 : -1;
    
            // If balance > 0, it means more elements > k in subarray [0..i]
            if (Sum > 0) {
                maxLen = i + 1;
            } else {
                // Check if (Sum - 1) has occurred before
                // This means from that index+1 to current, balance becomes > 0
                if (prefix.count(Sum - 1)) {
                    maxLen = max(maxLen, i - prefix[Sum - 1]);
                }
            }
    
            // Store the earliest index where this Sum occurs
            if (!prefix.count(Sum)) {
                prefix[Sum] = i;
            }
        }
    
        return maxLen;
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
        getline(cin, input);
        int k = stoi(input);

        Solution ob;
        cout << ob.longestSubarray(arr, k) << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
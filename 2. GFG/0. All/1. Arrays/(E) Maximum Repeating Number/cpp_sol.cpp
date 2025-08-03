//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends


// User function template for C++
class Solution {
  public:
    // Returns maximum repeating element in arr[0..n-1].
    // The array elements are in range from 0 to k-1
    int maxRepeating(int k, vector<int>& arr) {
        // code here
         vector<int> freq(k, 0); // Frequency array for elements 0 to k-1

        // Count frequency of each number in arr
        for (int val : arr) {
            freq[val]++;
        }

        int max_freq = -1;
        int result = -1;

        for (int i = 0; i < k; i++) {
            if (freq[i] > max_freq) {
                max_freq = freq[i];
                result = i;
            } else if (freq[i] == max_freq && i < result) {
                result = i; // Choose smaller number in case of tie
            }
        }

        return result;
    }
};




//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        string ks;
        getline(cin, ks);
        int k = stoi(ks);
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int res = obj.maxRepeating(k, arr);
        cout << res << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
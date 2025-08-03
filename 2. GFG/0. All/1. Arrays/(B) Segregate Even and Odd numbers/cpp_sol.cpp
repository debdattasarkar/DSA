//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    void segregateEvenOdd(vector<int>& arr) {
        // code here
        vector<int> evens, odds;

        for (int num : arr) {
            if (num % 2 == 0) evens.push_back(num);
            else odds.push_back(num);
        }
    
        sort(evens.begin(), evens.end());
        sort(odds.begin(), odds.end());
    
        // Merge back to original array
        int i = 0;
        for (int num : evens) arr[i++] = num;
        for (int num : odds) arr[i++] = num;
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
        obj.segregateEvenOdd(arr);
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
        // string tl;
        // getline(cin, tl);
    }
    return 0;
}
// } Driver Code Ends
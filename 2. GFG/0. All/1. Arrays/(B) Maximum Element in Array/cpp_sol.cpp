//{ Driver Code Starts
#include <bits/stdc++.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int largest(int arr[], int n) {
        // code here
        int maxElement = arr[0];
        for (int i = 1; i < n; ++i) {
            if (arr[i] > maxElement)
                maxElement = arr[i];
        }
        return maxElement;
    }
};



//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        string input;
        int num;
        int arr[1000001], size = 0;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            arr[size++] = num;
        }

        Solution ob;
        cout << ob.largest(arr, size) << endl;
        cout << "~\n";
    }
    return 0;
}

// } Driver Code Ends
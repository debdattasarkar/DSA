//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int countZeroes(int arr[], int n) {
        // code here
        int low = 0, high = n - 1, first_zero = -1;

        // Binary search for first 0
        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[mid] == 0) {
                first_zero = mid;
                high = mid - 1; // search left half
            } else {
                low = mid + 1;
            }
        }

        return (first_zero == -1) ? 0 : n - first_zero;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        int arr[100001];
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number, size = 0;
        while (ss >> number) {
            arr[size++] = number;
        }

        Solution ob;
        cout << ob.countZeroes(arr, size) << endl;
        cout << "~\n";
    }

    return 0;
}

// } Driver Code Ends
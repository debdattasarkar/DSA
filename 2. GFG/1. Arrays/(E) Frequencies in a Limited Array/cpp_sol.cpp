//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to count the frequency of all elements from 1 to N in the array.
    vector<int> frequencyCount(vector<int>& arr) {
        // code here
        int N = arr.size();  // Get size of array
        vector<int> freq(N, 0);  // Initialize frequency array of size N with 0

        // Count frequencies of values 1 to N
        for (int i = 0; i < N; i++) {
            if (arr[i] >= 1 && arr[i] <= N) {
                freq[arr[i] - 1]++;  // Decrement by 1 to convert 1-based to 0-based index
            }
        }

        return freq;  // Return the frequency array
    }
};



//{ Driver Code Starts.

int main() {
    int t; // Number of test cases
    cin >> t;
    cin.ignore(); // Ignore the newline after the integer input
    while (t--) {
        vector<int> a;
        string input;

        // Input format: first number n followed by the array elements
        getline(cin, input);
        stringstream ss(input);
        int num;
        while (ss >> num)
            a.push_back(num); // Read the array elements from input string

        Solution obj;
        vector<int> result = obj.frequencyCount(a);

        // Print the result in the required format
        if (result.empty()) {
            cout << "[]"; // Print empty brackets if no duplicates are found
        } else {
            for (int i = 0; i < result.size(); i++) {
                if (i != 0)
                    cout << " ";
                cout << result[i];
            }
        }
        cout << endl; // Ensure new line after each test case output
    }

    return 0;
}

// } Driver Code Ends
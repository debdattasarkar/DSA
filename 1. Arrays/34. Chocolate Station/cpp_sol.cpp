//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    int getChocolateCost(vector<int> arr, int price) {
        // code here
        int total_cost = arr[0];
        int balance = 0; // Chocolates Geek has

        for (int i = 0; i < arr.size() - 1; ++i) {
            int diff = arr[i] - arr[i + 1];

            if (diff < 0) {
                int need = -diff;
                if (balance >= need) {
                    balance -= need;
                } else {
                    total_cost += (need - balance);
                    balance = 0;
                }
            } else {
                balance += diff;
            }
        }

        return total_cost * price;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // Ignore the newline character after t
    while (t--) {
        vector<int> arr;
        int price;
        string input;

        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        cin >> price;
        cin.ignore(); // Ignore the newline character after price

        Solution ob;
        cout << ob.getChocolateCost(arr, price) << "\n";
    }
    return 0;
}

// } Driver Code Ends
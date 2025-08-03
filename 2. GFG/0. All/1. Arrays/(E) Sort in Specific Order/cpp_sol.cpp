//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    void sortIt(vector<long long>& arr) {
        // code here.
        vector<long long> odd, even;

        // Separate odd and even numbers
        for (long long num : arr) {
            if (num % 2 == 0)
                even.push_back(num);
            else
                odd.push_back(num);
        }

        // Sort odd in descending order
        sort(odd.begin(), odd.end(), greater<long long>());
        // Sort even in ascending order
        sort(even.begin(), even.end());

        // Combine both parts back into original arr
        arr.clear();  // Clear original
        arr.insert(arr.end(), odd.begin(), odd.end());
        arr.insert(arr.end(), even.begin(), even.end());
    }
};


//{ Driver Code Starts.
int main() {
    long long t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<long long> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        long long number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        ob.sortIt(arr);

        for (int i = 0; i < arr.size(); i++)
            cout << arr[i] << " ";
        cout << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &A, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A) {
        for (int i = 0; i < A.size(); i++) {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends


class Solution {
  public:
    void swapKth(vector<int> &arr, int k) {
        // code here
        int n = arr.size();
        // Swap the kth element from start (index k-1) and kth from end (index n-k)
        swap(arr[k - 1], arr[n - k]);
    }
};



//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        int k;
        cin >> k;
        cin.ignore();
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        ob.swapKth(arr, k);
        for (auto x : arr) {
            cout << x << " ";
        }
        cout << endl << "~\n";
    }
    return 0;
}

// } Driver Code Ends
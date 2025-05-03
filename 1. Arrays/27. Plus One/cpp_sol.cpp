//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    vector<int> increment(vector<int> arr, int N) {
        // code here
        // Traverse from last digit backwards
        for (int i = N - 1; i >= 0; --i) {
            if (arr[i] < 9) {
                arr[i]++;  // Simple increment
                return arr;
            }
            arr[i] = 0;  // Reset and carry continues
        }
    
        // All were 9s, need extra digit at front
        arr.insert(arr.begin(), 1);
        return arr;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        char c;
        
        cin>>N;
        vector<int> arr(N);
        
        for(int i=0 ; i<N ; i++)
            cin>>arr[i];

        Solution ob;
        vector<int> res = ob.increment(arr,N);
        for(int i: res)
            cout<<i<<" ";
        cout<<endl;
    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends
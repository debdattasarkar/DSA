//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int makeProductOne(int arr[], int N) {
        // code here
        int steps = 0, neg = 0, zero = 0;
        for(int i = 0; i < N; i++) {
            if (arr[i] == 0) {
                steps++;
                zero++;
            }
            else if (arr[i] > 0) {
                steps += arr[i] - 1;
            } else {
                steps += abs(arr[i]) - 1;
                neg++;
            }
        }
        if (neg % 2 != 0 && zero == 0) steps += 2;
        return steps;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        
        int arr[N];
        for(int i=0; i<N; i++)
            cin>>arr[i];

        Solution ob;
        cout << ob.makeProductOne(arr,N) << endl;
    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends
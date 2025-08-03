//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int smallestSumSubarray(vector<int>& arr) {
        // Code here
        int minSum = arr[0];
        int currSum = arr[0];
    
        for (size_t i = 1; i < arr.size(); ++i) {
            currSum = arr[i] + min(0, currSum);
            minSum = min(minSum, currSum);
        }
    
        return minSum;
    }
};



//{ Driver Code Starts.



int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        
        Solution ob;
        
        int ans = ob.smallestSumSubarray(a);
        
        cout<<ans<<endl;
    
cout << "~" << "\n";
}
}
// } Driver Code Ends
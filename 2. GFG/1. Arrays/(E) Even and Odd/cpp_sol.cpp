//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    void reArrange(int arr[], int N) {
        // code here
        int even = 0, odd = 1;
        while (even < N && odd < N) {
            if (arr[even] % 2 == 0) {
                even += 2;
            } else if (arr[odd] % 2 == 1) {
                odd += 2;
            } else {
                swap(arr[even], arr[odd]);
                even += 2;
                odd += 2;
            }
        }
    }
};


//{ Driver Code Starts.

int check(int arr[], int n)
{
    int flag = 1;
    int c=0, d=0;
    for(int i=0; i<n; i++)
    {
        if(i%2==0)
        {
            if(arr[i]%2)
            {
                flag = 0;
                break;
            }
            else
                c++;
        }
        else
        {
            if(arr[i]%2==0)
            {
                flag = 0;
                break;
            }
            else
                d++;
        }
    }
    if(c!=d)
        flag = 0;
        
    return flag;
}

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
        ob.reArrange(arr,N);
        
        cout<<check(arr,N)<<endl;
    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends
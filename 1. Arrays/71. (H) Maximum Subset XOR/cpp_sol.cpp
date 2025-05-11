//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

// Function to return maximum XOR subset in set[]

class Solution {
  public:
    int maxSubsetXOR(int arr[], int N) {
        // Your code here
        int index = 0;

        for (int i = 31; i >= 0; i--) {
            int maxInd = index;
            int maxEle = -1;

            for (int j = index; j < N; j++) {
                if ((arr[j] & (1 << i)) && arr[j] > maxEle) {
                    maxEle = arr[j];
                    maxInd = j;
                }
            }

            if (maxEle == -1) continue;

            swap(arr[index], arr[maxInd]);

            for (int j = 0; j < N; j++) {
                if (j != index && (arr[j] & (1 << i)))
                    arr[j] ^= arr[index];
            }

            index++;
        }

        int result = 0;
        for (int i = 0; i < index; i++) result ^= arr[i];

        return result;
    }
};


//{ Driver Code Starts.
int main()
{

    int t,n,a[100004],k;
    scanf("%d",&t);
    while(t--)
    {
        //cin>>n;
       scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        Solution obj;
        printf("%d\n",obj.maxSubsetXOR(a,n));
       // cout<<bin(a,0,n-1,k)<<endl;
    
cout << "~" << "\n";
}
}
// } Driver Code Ends
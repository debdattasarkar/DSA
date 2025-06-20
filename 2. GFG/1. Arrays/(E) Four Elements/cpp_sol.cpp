//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

bool find4Numbers(int A[], int n, int X);

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n, i, x;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        cin>>x;
        cout << find4Numbers(a, n, x) << endl;

    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends


// User function Template for C++

bool find4Numbers(int A[], int n, int X) {
    sort(A, A + n);  // Step 1: Sort array
    for (int i = 0; i < n - 3; i++) {
        for (int j = i + 1; j < n - 2; j++) {
            int left = j + 1, right = n - 1;
            int target = X - A[i] - A[j];
            while (left < right) {
                int sum = A[left] + A[right];
                if (sum == target) return true;
                else if (sum < target) left++;
                else right--;
            }
        }
    }
    return false;
}
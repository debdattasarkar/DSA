//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends

// User function Template for C++
class Solution {
  public:
    long long leftCandies(long long n, long long m) {
        // code here
        long long low = 0, high = m;

        // Binary search for maximum full rounds
        while (low <= high) {
            long long mid = (low + high) / 2;
            long long total = mid * n * (n + 1) / 2;

            if (total <= m)
                low = mid + 1;
            else
                high = mid - 1;
        }

        long long used = high * n * (n + 1) / 2;
        m -= used;

        // Final partial round
        for (long long i = 1; i <= n; i++) {
            if (m >= i)
                m -= i;
            else
                break;
        }

        return m;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long n, m;
        cin >> n >> m;
        Solution obj;
        long long ans = obj.leftCandies(n, m);
        cout << ans << "\n";

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends
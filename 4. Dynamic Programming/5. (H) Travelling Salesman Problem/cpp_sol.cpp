//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int tsp(vector<vector<int>>& cost) {
        // Code here
        int n = cost.size();
        int VISITED_ALL = (1 << n) - 1;
        vector<vector<int>> dp(1 << n, vector<int>(n, -1));

        function<int(int, int)> dfs = [&](int mask, int pos) {
            if (mask == VISITED_ALL) return cost[pos][0];
            if (dp[mask][pos] != -1) return dp[mask][pos];

            int ans = INT_MAX;
            for (int city = 0; city < n; ++city) {
                if (!(mask & (1 << city)))
                    ans = min(ans, cost[pos][city] + dfs(mask | (1 << city), city));
            }
            return dp[mask][pos] = ans;
        };

        return dfs(1, 0);
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n;
        cin >> n;
        vector<vector<int>> cost(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> cost[i][j];
        Solution obj;
        int ans = obj.tsp(cost);
        cout << ans << "\n";

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends
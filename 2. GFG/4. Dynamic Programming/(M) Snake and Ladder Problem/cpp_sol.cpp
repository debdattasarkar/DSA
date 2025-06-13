//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int minThrow(int N, int arr[]) {
        // code here
        vector<int> board(31);
        for (int i = 1; i <= 30; i++) board[i] = i;

        // Apply ladders and snakes
        for (int i = 0; i < 2 * N; i += 2)
            board[arr[i]] = arr[i + 1];

        vector<bool> visited(31, false);
        queue<pair<int, int>> q;
        q.push({1, 0});
        visited[1] = true;

        while (!q.empty()) {
            int pos = q.front().first;
            int throws = q.front().second;
            q.pop();

            for (int die = 1; die <= 6; die++) {
                int next = pos + die;
                if (next <= 30) {
                    int finalPos = board[next];
                    if (finalPos == 30) return throws + 1;
                    if (!visited[finalPos]) {
                        visited[finalPos] = true;
                        q.push({finalPos, throws + 1});
                    }
                }
            }
        }
        return -1;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[2*N];
        for(int i = 0;i < 2*N;i++)
            cin>>arr[i];
        
        Solution ob;
        cout<<ob.minThrow(N, arr)<<"\n";
    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends
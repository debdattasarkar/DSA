//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int firstIndex(vector<int> &arr) {
        // Your code goes here
        int low = 0, high = arr.size() - 1;
        int answer = -1;
    
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == 1) {
                answer = mid;
                high = mid - 1;  // Search on the left side
            } else {
                low = mid + 1;
            }
        }
    
        return answer;
    }
};


//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream s1(input);
        int num;
        while (s1 >> num) {
            arr.push_back(num);
        }
        Solution ob;
        cout << ob.firstIndex(arr) << endl;
        cout << "~" << endl;
    }
}
// } Driver Code Ends
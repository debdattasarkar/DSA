//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends



class Solution {
  public:
    string max_num;

    // Recursive helper function
    void helper(string &s, int k, int idx) {
        if (k == 0 || idx == s.length()) return;

        // Find the max digit from idx to end
        char max_digit = *max_element(s.begin() + idx, s.end());

        // Only swap if current digit is not already max
        if (s[idx] != max_digit) {
            for (int j = s.length() - 1; j >= idx; --j) {
                if (s[j] == max_digit) {
                    swap(s[idx], s[j]);

                    if (s > max_num)
                        max_num = s;

                    helper(s, k - 1, idx + 1);

                    swap(s[idx], s[j]); // backtrack
                }
            }
        } else {
            helper(s, k, idx + 1); // move to next index
        }
    }

    // Function to find the largest number after k swaps.
    string findMaximumNum(string& s, int k) {
        // code here.
        max_num = s;
        helper(s, k, 0);
        return max_num;
    }
};


//{ Driver Code Starts.

int main() {
    int t, k;
    string str;

    cin >> t;
    while (t--) {
        cin >> k >> str;
        Solution ob;
        cout << ob.findMaximumNum(str, k) << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends
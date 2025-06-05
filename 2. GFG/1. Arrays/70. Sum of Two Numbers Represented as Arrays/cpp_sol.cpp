//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:

    vector<int> findSum(vector<int> &arr1, vector<int> &arr2) {
        // code here
        int i = arr1.size() - 1;
        int j = arr2.size() - 1;
        int carry = 0;
        vector<int> result;

        while (i >= 0 || j >= 0 || carry) {
            int digit1 = (i >= 0) ? arr1[i] : 0;
            int digit2 = (j >= 0) ? arr2[j] : 0;
            int total = digit1 + digit2 + carry;

            result.push_back(total % 10); // store unit digit
            carry = total / 10;           // keep carry

            i--;
            j--;
        }

        reverse(result.begin(), result.end());
        return result;
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);

    while (t--) {

        vector<int> arr1, arr2;
        string input1;
        getline(cin, input1);
        stringstream ss(input1);
        int number1;
        while (ss >> number1) {
            arr1.push_back(number1);
        }
        string input2;
        getline(cin, input2);
        stringstream sss(input2);
        int number2;
        while (sss >> number2) {
            arr2.push_back(number2);
        }
        Solution ob;
        // Function calling
        vector<int> v;
        v = ob.findSum(arr1, arr2);

        for (int i = 0; i < v.size(); i++)
            cout << v[i] << " ";

        cout << endl;
        cout << "~" << endl;
    }

    return 0;
}

// } Driver Code Ends
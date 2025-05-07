//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    string maximumFrequency(string& s) {
        // Your code foes here.
        istringstream iss(s);
        string word;
        unordered_map<string, int> freq;
        unordered_map<string, int> firstIndex;
        int index = 0, maxFreq = 0;
        string result;

        while (iss >> word) {
            freq[word]++;
            if (firstIndex.find(word) == firstIndex.end()) {
                firstIndex[word] = index;
            }

            if (freq[word] > maxFreq || 
               (freq[word] == maxFreq && firstIndex[word] < firstIndex[result])) {
                maxFreq = freq[word];
                result = word;
            }
            index++;
        }

        return result + " " + to_string(maxFreq);
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();

    for (int i = 0; i < t; i++) {

        string str;
        getline(cin, str);
        Solution ob;

        cout << ob.maximumFrequency(str) << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends
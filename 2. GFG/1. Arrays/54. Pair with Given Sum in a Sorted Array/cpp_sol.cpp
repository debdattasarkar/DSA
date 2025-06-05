//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    int countPairs(vector<int> &arr, int target) {
        // Complete the function
        int left = 0, right = arr.size() - 1;
        int count = 0;
    
        while (left < right) {
            int sum = arr[left] + arr[right];
    
            if (sum == target) {
                // Case 1: Different values → count frequency on both sides
                if (arr[left] != arr[right]) {
                    int leftCount = 1, rightCount = 1;
    
                    while (left + 1 < right && arr[left] == arr[left + 1]) {
                        leftCount++;
                        left++;
                    }
    
                    while (right - 1 > left && arr[right] == arr[right - 1]) {
                        rightCount++;
                        right--;
                    }
    
                    count += leftCount * rightCount;
                    left++;
                    right--;
                }
                // Case 2: All elements between left and right are equal
                else {
                    int n = right - left + 1;
                    count += (n * (n - 1)) / 2;
                    break;
                }
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }
    
        return count;
    }
};


//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        int target;
        string input;
        getline(cin, input);

        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        cin >> target;
        cin.ignore();
        Solution obj;
        cout << obj.countPairs(arr, target) << endl;
        cout << "~\n";
    }

    return 0;
}
// } Driver Code Ends
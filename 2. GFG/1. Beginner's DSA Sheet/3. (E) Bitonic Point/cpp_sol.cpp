// User function template for C++
class Solution {
  public:
    int findMaximum(vector<int> &arr) {
        int n = arr.size();
        int left = 1, right = n-2;
        while( left <= right){
            int mid = left + (right - left) / 2;
            if(arr[mid - 1] < arr[mid] && arr[mid] > arr[mid+1])
                return arr[mid];
            else if(arr[mid - 1] < arr[mid])
                left = mid + 1;
            else
                right = mid - 1;
        }
        if(right == 0)return arr[0];
        return arr[n-1];
    }
};
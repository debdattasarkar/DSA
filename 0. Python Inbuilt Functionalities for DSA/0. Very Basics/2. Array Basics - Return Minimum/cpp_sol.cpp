#include <iostream>
#include <cstring>
using namespace std;

int main() {
    const int MAX = 10;
    int arr[MAX];
    int n = 5;

    arr[0] = 7;
    arr[1] = 3;
    arr[2] = 9;
    arr[3] = 1;
    arr[4] = 5;

    

    if (n > 0) {

        string str = "Array: ["+to_string(arr[0]);
        for (int i = 1; i < n; i++) {
            str+=", "+to_string(arr[i]);
        }
        str+=']';
        cout << str;
        cout << endl;

        int min = arr[0];

        for(int i=1; i<n; i++) {
            if (min > arr[i]) {
                min = arr[i];
            }
        }
        cout << "Smallest number is: " << min;
    }
    return 0;
}
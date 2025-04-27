//{ Driver Code Starts
// Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let a = new Array();
        let input_ar1 = readLine().split(' ').map(x => parseInt(x));
        for (let i = 0; i < input_ar1.length; i++) a.push(input_ar1[i]);
        let obj = new Solution();
        let idx = obj.peakElement(a);
        let n = a.length;
        let f = 0;
        if (n == 1)
            f = 1;
        else if (idx == 0 && a[0] >= a[1])
            f = 1;
        else if (idx == n - 1 && a[n - 1] > a[n - 2])
            f = 1;
        else if (idx > 0 && idx < n - 1 && a[idx] > a[idx + 1] && a[idx] > a[idx - 1])
            f = 1;
        else
            f = 0;
        if (f)
            console.log("true");
        else
            console.log("false");
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript
/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    peakElement(arr) {
        // Code here
        let low = 0, high = arr.length - 1;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
    
            let left = (mid > 0) ? arr[mid - 1] : -Infinity;
            let right = (mid < arr.length - 1) ? arr[mid + 1] : -Infinity;
    
            if (arr[mid] >= left && arr[mid] >= right) {
                return mid;  // Found a peak
            } else if (left > arr[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
    
        return -1;
    }
}
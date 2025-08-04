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

        let arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        let res = obj.findMaximum(arr);
        console.log(res);
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

    findMaximum(arr) {
        // your code here
        let low = 0, high = arr.length - 1;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            if (mid > 0 && mid < arr.length - 1) {
                if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
                    return arr[mid];
                else if (arr[mid] > arr[mid - 1])
                    low = mid + 1;
                else
                    high = mid - 1;
            } else if (mid === 0) {
                return Math.max(arr[0], arr[1]);
            } else if (mid === arr.length - 1) {
                return Math.max(arr[arr.length - 1], arr[arr.length - 2]);
            }
        }

        return -1;
    }
}
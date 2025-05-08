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
        let arr = readLine().trim().split(" ").map((x) => parseInt(x));
        let obj = new Solution();
        let res = obj.countZeroes(arr);
        console.log(res);
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    countZeroes(arr) {
        // write your code here
        let n = arr.length;
        let low = 0, high = n - 1, firstZero = -1;

        // Binary search
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            if (arr[mid] === 0) {
                firstZero = mid;
                high = mid - 1; // search left
            } else {
                low = mid + 1;
            }
        }

        return firstZero === -1 ? 0 : n - firstZero;
    }
}
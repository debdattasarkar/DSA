//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
//  Initial Template for javascript
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
        let input_ar0 = readLine().split(' ').map(x => parseInt(x));
        let k = input_ar0[0];
        let obj = new Solution();
        console.log(obj.longestSubarray(arr, k));
        console.log("~");
    }
}
// } Driver Code Ends


//Back-end complete function Template for javascript
class Solution {
    longestSubarray(arr, k) {
        // Code Here
        const prefix = new Map(); // balance -> earliest index
        let Sum = 0;
        let maxLen = 0;

        for (let i = 0; i < arr.length; i++) {
            // Update balance
            Sum += (arr[i] > k) ? 1 : -1;

            // More >k elements from start
            if (Sum > 0) {
                maxLen = i + 1;
            } else {
                // If we've seen (Sum - 1) before
                if (prefix.has(Sum - 1)) {
                    maxLen = Math.max(maxLen, i - prefix.get(Sum - 1));
                }
            }

            // Record the earliest index for this balance
            if (!prefix.has(Sum)) {
                prefix.set(Sum, i);
            }
        }

        return maxLen;
    }
}
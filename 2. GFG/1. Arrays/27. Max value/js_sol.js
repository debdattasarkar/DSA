//{ Driver Code Starts
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
    for (let i = 0; i < t; i++) {
        let input_line = readLine().split(' ').map(Number);
        let n = input_line.length;
        let arr = new Array(n);

        for (let i = 0; i < n; i++) {
            arr[i] = input_line[i];
        }

        let obj = new Solution();
        let ans = obj.maxVal(arr);
        if (ans === -0) {
            ans = 0;
        }
        console.log(ans);
    }
}

// } Driver Code Ends


// User function Template for JavaScript
/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find the maximum value difference between element and index.
    maxVal(arr) {
        // your code here
        let maxDiff = -Infinity;
        let minDiff = Infinity;
    
        for (let i = 0; i < arr.length; i++) {
            const val = arr[i] - i;
            maxDiff = Math.max(maxDiff, val);
            minDiff = Math.min(minDiff, val);
        }
    
        return maxDiff - minDiff;
    }
}
//{ Driver Code Starts
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let tc = parseInt(readLine());
    while (tc > 0) {
        // Read the first array from the first line of input
        let arr1 = readLine().split(' ').map(Number);

        // Read the second array from the second line of input
        let arr2 = readLine().split(' ').map(Number);

        // Create an instance of Solution and call the function
        let obj = new Solution();
        let result = obj.findExtra(arr1, arr2);

        // Print the result
        console.log(result);

        tc--;
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {Number[]} arr1
 * @param {Number[]} arr2
 * @returns {Number}
 */
class Solution {
    findExtra(a, b) {
        // code here
        let low = 0, high = b.length; // b is shorter by 1

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            // Check if elements differ or we're past b
            if (mid >= b.length || a[mid] !== b[mid]) {
                high = mid - 1;  // mismatch could be earlier
            } else {
                low = mid + 1;  // match, move right
            }
        }

        return low;  // index of the extra element
    }
}
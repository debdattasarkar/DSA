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
        console.log(obj.transitionPoint(arr));
        console.log("~");
    }
} // } Driver Code Ends
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution {
    transitionPoint(arr) {
        // code here
        let n = arr.length;
        let low = 0, high = n - 1;
        let result = -1;  // default if no 1 found

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);

            if (arr[mid] === 1) {
                result = mid;     // save position, search left
                high = mid - 1;
            } else {
                low = mid + 1;    // search right
            }
        }

        return result;
    }
}
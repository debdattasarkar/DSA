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
    for (let i = 0; i < t; i++) {

        let a = readLine().split(' ').map(x => parseInt(x, 10));
        let b = readLine().split(' ').map(x => parseInt(x, 10));
        let obj = new Solution();

        let ans = obj.numberofElementsInIntersection(a, b);
        console.log(ans);

        console.log("~");
    }
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} a
 * @param {number[]} b
 * @returns {number}
 */
class Solution {
    // Function to return the count of the number of elements in
    // the intersection of two arrays.
    numberofElementsInIntersection(a, b) {
        // code here
        const setB = new Set(b);
        let count = 0;

        for (let num of a) {
            if (setB.has(num)) {
                count++;
                setB.delete(num); // maintain uniqueness
            }
        }

        return count;
    }
}
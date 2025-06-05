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

function printList(res, n) {
    let s = "";
    for (let i = 0; i < n; i++) {
        s += res[i];
        s += " ";
    }
    console.log(s);
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let input_ar1 = readLine().split(' ').map(x => parseInt(x));
        let n = input_ar1.length;
        let arr = new Array(n);
        for (let i = 0; i < n; i++) {
            arr[i] = input_ar1[i];
        }
        let obj = new Solution();
        let res = obj.minAnd2ndMin(arr, n);
        printList(res, res.length);
        console.log("~");
    }
} // } Driver Code Ends

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number[]}
 */

class Solution {
    minAnd2ndMin(arr) {
        // code here
        // Initialize first and second smallest to Infinity
        let first = Infinity;
        let second = Infinity;
    
        // Traverse the array
        for (let num of arr) {
            if (num < first) {
                // New smallest found
                second = first;
                first = num;
            } else if (num < second && num !== first) {
                // New second smallest found (must be unique)
                second = num;
            }
        }
    
        // If second is still Infinity, there's no second smallest
        if (second === Infinity) {
            return [-1];
        } else {
            return [first, second];
        }
    }
}

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
    let t = parseInt(readLine()); // Number of test cases
    for (let i = 0; i < t; i++) {
        let arr = readLine().split(' ').map(x => parseInt(x)); // Input array
        let obj = new Solution();
        const result = obj.frequencyCount(arr);

        // Print the result in the required format
        if (result.length > 0) {
            console.log(result.join(' ')); // Print counts in ascending order
        } else {
            console.log("[]"); // Print empty list if no counts are found
        }
    }
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number[]}
 */

class Solution {
    // Function to count the frequency of all elements from 1 to N in the array.
    frequencyCount(arr) {
        // code here
        const N = arr.length;

        // Initialize frequency array of size N with all zeros
        const freq = new Array(N).fill(0);

        // Traverse the array and count occurrences of elements 1 to N
        for (let i = 0; i < N; i++) {
            if (arr[i] >= 1 && arr[i] <= N) {
                freq[arr[i] - 1]++; // Adjust for 0-based indexing
            }
        }

        return freq; // Return the frequency array
    }
}
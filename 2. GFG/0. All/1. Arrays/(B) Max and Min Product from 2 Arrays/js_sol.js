//{ Driver Code Starts
// Initial Template for javascript

const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', function(line) { inputLines.push(line); });

rl.on('close', function() {
    let t = parseInt(inputLines[currentLine++]);
    for (let i = 0; i < t; i++) {
        let arr1 = inputLines[currentLine++].split(' ').map(Number);
        let arr2 = inputLines[currentLine++].split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.findMultiplication(arr1, arr2);
        console.log(ans);
        console.log("~");
    }
});

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @returns {number}
 */

class Solution {
    // Function to find the maximum element from array arr1 and
    // the minimum element from array arr2 and return their product.
    findMultiplication(arr1, arr2) {
        // code here
        let max1 = Math.max(...arr1); // O(n)
        let min2 = Math.min(...arr2); // O(m)
        return max1 * min2;
    }
}

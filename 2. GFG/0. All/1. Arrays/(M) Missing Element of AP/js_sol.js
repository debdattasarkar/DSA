//{ Driver Code Starts
// Initial Template for javascript

'use strict';
const readline = require('readline');

const rl = readline.createInterface({input : process.stdin, output : process.stdout});

rl.question('', (t) => {
    const solution = new Solution();
    let linesRead = 0;

    rl.on('line', (input) => {
        if (linesRead === parseInt(t)) {
            rl.close();
            return;
        }

        linesRead++;
        const arr = input.trim().split(/\s+/).map(Number);
        console.log(solution.findMissing(arr));
        console.log("~");
    });
});
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @return {number}
 */

class Solution {
    findMissing(arr) {
        // code here
        const n = arr.length;

        // Step 1: Find common difference
        let d = Math.abs(arr[1] - arr[0]);
        for (let i = 1; i < n - 1; i++) {
            d = Math.min(d, Math.abs(arr[i+1] - arr[i]));
        }

        // Detect direction
        if (arr[1] < arr[0]) d = -d;

        // Step 2: Binary search for mismatch
        let low = 0, high = n - 1;
        while (low < high) {
            let mid = Math.floor((low + high) / 2);
            let expected = arr[0] + mid * d;
            if (arr[mid] === expected) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        // Step 3: Check if AP is complete
        let expectedLast = arr[0] + (n - 1) * d;
        if (arr[n - 1] === expectedLast)
            return arr[n - 1] + d;
        return arr[0] + low * d;
    }
}

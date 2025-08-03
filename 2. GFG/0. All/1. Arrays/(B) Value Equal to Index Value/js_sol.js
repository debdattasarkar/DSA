//{ Driver Code Starts
const readline = require('readline');

const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', (line) => { inputLines.push(line); });

rl.on('close', () => {
    let t = parseInt(inputLines[currentLine++].trim());
    let solution = new Solution();

    while (t--) {
        let nums = inputLines[currentLine++].trim().split(' ').map(Number);
        let ans = solution.valueEqualToIndex(nums);

        if (ans.length === 0) {
            console.log("Not Found");
        } else {
            console.log(ans.join(' '));
        }
        console.log("~");
    }
});
// } Driver Code Ends


// User function Template for JavaScript

/**
 * @param {number[]} arr
 * @returns {number[]}
 */
class Solution {
    // Function to find elements in the array that are equal to their index.
    valueEqualToIndex(arr) {
        // code here
        let result = [];
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === i + 1) {
                result.push(i + 1);
            }
        }
        return result;
    }
}

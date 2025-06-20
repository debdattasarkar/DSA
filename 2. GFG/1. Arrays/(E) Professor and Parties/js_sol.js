//{ Driver Code Starts
// Driver code
const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', (line) => { inputLines.push(line.trim()); });

rl.on('close', () => { main(); });

function readLine() { return inputLines[currentLine++]; }

function main() {
    let tc = parseInt(readLine());
    while (tc > 0) {
        // let k = parseInt(readLine());
        let arr = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.PartyType(arr);
        console.log(ans);
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript
/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find the maximum number of people to whom the host can
    // send the invitation such that sum of their heights is maximum
    PartyType(arr) {
        // Your code goes here
        const seen = new Set();
        for (let color of arr) {
            if (seen.has(color)) {
                return "true";  // duplicate
            }
            seen.add(color);
        }
        return "false";  // all unique
    }
}
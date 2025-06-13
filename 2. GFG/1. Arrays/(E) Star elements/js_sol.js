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
        let arr = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.getStar(arr);
        console.log(ans.join(' '));
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript
class Solution {
    getStar(arr) {
        // code here
        let result = [];
        let maxRight = -Infinity;

        // Traverse from right to left
        for (let i = arr.length - 1; i >= 0; i--) {
            if (arr[i] > maxRight) {
                result.push(arr[i]);  // Found star
                maxRight = arr[i];
            }
        }

        result.reverse();  // Maintain left-to-right order
        return result;
    }
}

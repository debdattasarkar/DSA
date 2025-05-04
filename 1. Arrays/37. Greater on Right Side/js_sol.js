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
        let ans = ob.nextGreatest(arr);
        console.log(ans.join(' '));
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    nextGreatest(arr) {
        // code here
        let maxRight = -1; // Start with -1 for the last element
        for (let i = arr.length - 1; i >= 0; i--) {
            let current = arr[i];   // Temporarily store current value
            arr[i] = maxRight;      // Replace with maxRight
            if (current > maxRight) {
                maxRight = current; // Update maxRight if needed
            }
        }
        return arr;
    }
}

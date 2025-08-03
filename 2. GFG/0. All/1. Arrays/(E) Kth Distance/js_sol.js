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
        let k = parseInt(readLine());
        let ob = new Solution();
        let ans = ob.checkDuplicatesWithinK(arr, k);
        // console.log(ans);
        if (ans) {
            console.log("true");
        } else {
            console.log("false");
        }
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript
//Back-end complete function Template for javascript
class Solution {
    checkDuplicatesWithinK(arr, k) {
        // your code
        const seen = new Set();
        for (let i = 0; i < arr.length; i++) {
            if (seen.has(arr[i])) return true;
            seen.add(arr[i]);
            if (i >= k) seen.delete(arr[i - k]);
        }
        return false;
    }
}
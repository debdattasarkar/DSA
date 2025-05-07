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
        let ans = ob.areElementsContiguous(arr);
        if (ans) {
            console.log("Yes");
        } else {
            console.log("No");
        }
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends




// User function Template for javascript
class Solution {
    areElementsContiguous(arr) {
        arr.filter(e => e !== 0);
        arr.sort((a, b) => a - b);
        
        let len = arr.length;
        if (len === 1) return true;
        
        let min = arr[0];
        let max = arr[len - 1];
        
        for (let i = min; i < max; i++) {
            if (!arr.includes(i)) return false;
        }
        
        return true;
    }
}
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
        let ans = ob.arranged(arr);
        console.log(ans.join(' '));
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    // Function to arrange all elements of a given array.
    arranged(arr) {
        // your code here
        let pos = arr.filter(x => x >= 0);
        let neg = arr.filter(x => x < 0);
        
        let result = [];
        for (let i = 0; i < pos.length; i++) {
            result.push(pos[i]);
            result.push(neg[i]);
        }
    
        return result;
    }
}

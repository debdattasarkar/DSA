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
        let ans = ob.maxNtype(arr);
        console.log(ans);
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    maxNtype(arr) {
        // code here
        const n = arr.length;
        let countIncreases = 0;
        let countDecreases = 0;
    
        // Count increasing and decreasing pairs
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] < arr[i + 1]) {
                countIncreases++;
            } else if (arr[i] > arr[i + 1]) {
                countDecreases++;
            }
        }
    
        // Classify based on the counts
        if (countDecreases === 0) {
            return 1; // Ascending
        } else if (countIncreases === 0) {
            return 2; // Descending
        } else if (countDecreases === 1 && arr[n - 1] < arr[0]) {
            return 4; // Ascending Rotated
        } else if (countIncreases === 1 && arr[n - 1] > arr[0]) {
            return 3; // Descending Rotated
        } else {
            return -1; // Undefined type
        }
    }
}
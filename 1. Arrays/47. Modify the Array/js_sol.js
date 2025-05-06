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
        let ans = ob.modifyAndRearrangeArr(arr);
        console.log(ans.join(' '));
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    modifyAndRearrangeArr(arr) {
        // code here
        const n = arr.length;

        // Step 1: Combine adjacent equal valid numbers
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] !== 0 && arr[i] === arr[i + 1]) {
                arr[i] *= 2;
                arr[i + 1] = 0;
                i++;  // Skip next
            }
        }

        // Step 2: Move non-zeros to front
        let result = [];
        for (let i = 0; i < n; i++) {
            if (arr[i] !== 0) result.push(arr[i]);
        }

        while (result.length < n) result.push(0);
        return result;
    }
}

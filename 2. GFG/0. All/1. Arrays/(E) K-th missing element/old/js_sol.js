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
        let k = parseInt(readLine());
        let arr = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.KthMissingElement(arr, k);
        console.log(ans);
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    KthMissingElement(arr, k) {
        // code here
        const n = arr.length;

        for (let i = 1; i < n; i++) {
            // Calculate missing numbers between arr[i-1] and arr[i]
            let missing = arr[i] - arr[i - 1] - 1;

            if (k <= missing) {
                // Found within this gap
                return arr[i - 1] + k;
            }

            // Move to next gap
            k -= missing;
        }

        // k-th missing doesn't exist within the array
        return -1;
    }
}
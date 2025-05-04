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
        let ans = ob.longest(arr);
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
    // Function to find length of longest subarray of consecutive integers.
    longest(arr) {
        // your code here
        let n = arr.length;
    
        if (n === 0) return 0;
        
        let ans = 0;
        
        for (let i = 0; i < n; i++) {
            let maxi = true;
            for (let j = 0; j < i; j++) {
                if (arr[j] > arr[i]) {
                    maxi = false;
                    break;
                }
            }
            if (maxi) {
                ans++;
            }
        }
        
        return ans;
    }
}
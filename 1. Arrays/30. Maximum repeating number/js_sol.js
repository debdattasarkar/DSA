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
        let ans = ob.maxRepeating(k, arr);
        console.log(ans);
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */

class Solution {
    maxRepeating(k, arr) {
        // code here
        let freq = new Array(k).fill(0); // Frequency array

        // Count frequency of each number
        for (let val of arr) {
            freq[val]++;
        }

        let maxFreq = -1;
        let result = -1;

        for (let i = 0; i < k; i++) {
            if (freq[i] > maxFreq) {
                maxFreq = freq[i];
                result = i;
            } else if (freq[i] === maxFreq && i < result) {
                result = i; // Pick smaller number in tie
            }
        }

        return result;
    }
}

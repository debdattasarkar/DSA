//{ Driver Code Starts
// Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let k = parseInt(readLine());
        let str = readLine();
        let obj = new Solution();
        console.log(obj.findMaximumNum(str, k));

        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {string} s
 * @param {number} k
 * @returns {string}
 */

class Solution {
    constructor() {
        this.maxNum = '';
    }

    helper(sArr, k, idx) {
        if (k === 0 || idx === sArr.length) return;

        let maxDigit = Math.max(...sArr.slice(idx));

        if (parseInt(sArr[idx]) !== maxDigit) {
            for (let j = sArr.length - 1; j >= idx; j--) {
                if (parseInt(sArr[j]) === maxDigit) {
                    [sArr[idx], sArr[j]] = [sArr[j], sArr[idx]];
                    const currStr = sArr.join('');
                    if (currStr > this.maxNum) this.maxNum = currStr;

                    this.helper(sArr, k - 1, idx + 1);
                    [sArr[idx], sArr[j]] = [sArr[j], sArr[idx]]; // backtrack
                }
            }
        } else {
            this.helper(sArr, k, idx + 1);
        }
    }
    // Function to find the largest number after k swaps.
    findMaximumNum(s, k) {
        // your code here
        this.maxNum = s;
        this.helper(s.split(''), k, 0);
        return this.maxNum;
        
    }
}
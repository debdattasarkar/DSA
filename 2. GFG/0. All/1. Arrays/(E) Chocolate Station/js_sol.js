//{ Driver Code Starts
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', () => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine(), 10);
    for (let i = 0; i < t; i++) {
        let arr = readLine().split(' ').map(x => parseInt(x, 10));
        let price = parseInt(readLine(), 10);
        let obj = new Solution();
        let res = obj.getChocolateCost(arr, price);
        console.log(res);
    }
}

// } Driver Code Ends


// User function Template for javascript
//  User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} price
 * @returns {number}
 */

class Solution {
    getChocolateCost(arr, price) {
        // code here
        let totalCost = arr[0];
        let balance = 0;

        for (let i = 0; i < arr.length - 1; i++) {
            let diff = arr[i] - arr[i + 1];

            if (diff < 0) {
                let need = -diff;
                if (balance >= need) {
                    balance -= need;
                } else {
                    totalCost += (need - balance);
                    balance = 0;
                }
            } else {
                balance += diff;
            }
        }

        return totalCost * price;
    }
}

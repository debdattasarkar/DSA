//{ Driver Code Starts
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

function printList(res, n) {
    let a = "";
    for (let i = 0; i < n; i++) {
        let s = "";
        s += res[i][0];
        s += " ";
        s += res[i][1];
        if (i != n - 1) {
            s += ", ";
        }
        a += s;
    }
    console.log(a);
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let x = parseInt(readLine());
        let arr1 = readLine().trim().split(" ").map((x) => parseInt(x));
        let arr2 = readLine().trim().split(" ").map((x) => parseInt(x));
        let obj = new Solution();
        let res = obj.allPairs(x, arr1, arr2);
        printList(res, res.length);

        console.log("~");
    }
} // } Driver Code Ends
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number} target
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @returns {number[][]}
 */

class Solution {
    allPairs(x, A, B) {
        // code here
        const countB = new Map();
        for (let b of B) {
            countB.set(b, (countB.get(b) || 0) + 1); // Count B values
        }

        const result = [];
        for (let a of A) {
            let target = x - a;
            if (countB.has(target)) {
                let times = countB.get(target);
                while (times--) {
                    result.push([a, target]);
                }
            }
        }

        // Sort by first element
        result.sort((a, b) => a[0] - b[0]);
        return result;
    }
}

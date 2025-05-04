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

function printList(res) {
    let s = res.join(" ");
    console.log(s);
}

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        obj.sortIt(arr);
        printList(arr);
        console.log("~");
    }
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} n
 * @returns {void}
 */

class Solution {
    sortIt(arr) {
        // code here
        // Separate into odd and even arrays
        let odd = [];
        let even = [];

        for (let num of arr) {
            if (num % 2 === 0)
                even.push(num);
            else
                odd.push(num);
        }

        // Sort odd in descending order and even in ascending
        odd.sort((a, b) => b - a);
        even.sort((a, b) => a - b);

        // Merge them into original array (in-place)
        let index = 0;

        for (let num of odd) {
            arr[index++] = num;
        }

        for (let num of even) {
            arr[index++] = num;
        }
    }
}

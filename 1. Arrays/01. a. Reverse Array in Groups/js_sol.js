//{ Driver Code Starts
// Initial Template for javascript

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

// Position this line where user code will be pasted.

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let k = parseInt(readLine(), 10);
        let arr = readLine().split(' ').map(x => parseInt(x, 10));
        let obj = new Solution();
        obj.reverseInGroups(arr, k);
        console.log(arr.join(" "));
        console.log('~');
    }
}

// } Driver Code Ends



class Solution {
    /**
    * @param number[] arr
    * @param number k

    * @returns none
    */
    reverseInGroups(arr, k) {
        // code here
        const n = arr.length;
        for (let i = 0; i < n; i += k) {
            let left = i;
            let right = Math.min(i + k - 1, n - 1);
    
            while (left < right) {
                [arr[left], arr[right]] = [arr[right], arr[left]];
                left++;
                right--;
            }
        }
        return arr;
    }
}

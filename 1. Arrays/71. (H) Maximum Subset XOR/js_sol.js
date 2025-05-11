//{ Driver Code Starts
//Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let N = parseInt(readLine());
        let input_ar = readLine().split(' ').map(x=>parseInt(x));
        let arr = new Array(N);
        for(let i=0;i<N;i++)
            arr[i] = input_ar[i];
        let obj = new Solution();
        let ans=obj.maxSubsetXOR(arr, N);
        if(ans==-0)
        ans=0;
        console.log(ans);
    
console.log("~");
}
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} n
 * @returns {number}
 */
class Solution {

    maxSubsetXOR(arr, N) {
        // code here
        let index = 0;

        for (let i = 31; i >= 0; i--) {
            let maxInd = index;
            let maxEle = -1;

            for (let j = index; j < N; j++) {
                if ((arr[j] & (1 << i)) !== 0 && arr[j] > maxEle) {
                    maxEle = arr[j];
                    maxInd = j;
                }
            }

            if (maxEle === -1) continue;

            [arr[index], arr[maxInd]] = [arr[maxInd], arr[index]];

            for (let j = 0; j < N; j++) {
                if (j !== index && (arr[j] & (1 << i))) {
                    arr[j] ^= arr[index];
                }
            }

            index++;
        }

        let result = 0;
        for (let i = 0; i < index; i++) {
            result ^= arr[i];
        }

        return result;
    }
}
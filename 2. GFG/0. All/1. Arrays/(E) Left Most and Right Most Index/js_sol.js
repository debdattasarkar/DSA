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
        let x =  parseInt(readLine()); 
        let v = new Array(N);
        for(let i=0;i<N;i++)
            v[i] = input_ar[i];
        let obj = new Solution();
        let ans=obj.indexes(v, x);
        if(ans[0]==-1&&ans[1]==-1)
        {
            console.log(-1);
        }
        else{
            if(ans[0]==-0)
            ans[0]=0;
            if(ans[1]==-0)
            ans[1]=0;
            console.log(ans[0]+" "+ans[1]);
        }
    
console.log("~");
}
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} v
 * @param {number} x
 * @returns {number[]}
 */
class Solution {

    indexes(v, x) {
        // code here
        let first = -1, last = -1;
        let low = 0, high = v.length - 1;

        // Binary search for first occurrence
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (v[mid] === x) {
                first = mid;
                high = mid - 1; // Move left
            } else if (v[mid] < x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        low = 0;
        high = v.length - 1;

        // Binary search for last occurrence
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (v[mid] === x) {
                last = mid;
                low = mid + 1; // Move right
            } else if (v[mid] < x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return [first, last];
    }
}
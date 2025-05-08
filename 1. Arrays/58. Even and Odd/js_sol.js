//{ Driver Code Starts
//Initial Template for javascript

//Initial Template for javascript

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

function printList(res,n){
    let s="";
    for(let i=0;i<n;i++){
        s+=res[i];
        s+=" ";
    }
    console.log(s);
}

function check(arr, n){
        let flag = 1;
        let c=0, d=0;
        for(let i=0; i<n; i++)
        {
            if(i%2==0)
            {
                if(arr[i]%2==1)
                {
                    flag = 0;
                    break;
                }
                else
                    c++;
            }
            else
            {
                if(arr[i]%2==0)
                {
                    flag = 0;
                    break;
                }
                else
                    d++;
            }
        }
        if(c!=d)
            flag = 0;
    return flag;
}
function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let arr = new Array(n);
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++){
            arr[i] = input_ar1[i];
        }
        let obj = new Solution();
        obj.reArrange(arr, n);
        let res = check(arr,n);
        console.log(res);
    
console.log("~");
}
}// } Driver Code Ends



// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} n
 * @returns { }
 */

class Solution {
    reArrange(arr, n) {
        // code here
        let even = 0, odd = 1;
        while (even < n && odd < n) {
            if (arr[even] % 2 === 0) {
                even += 2;
            } else if (arr[odd] % 2 === 1) {
                odd += 2;
            } else {
                [arr[even], arr[odd]] = [arr[odd], arr[even]];
                even += 2;
                odd += 2;
            }
        }
    }
}

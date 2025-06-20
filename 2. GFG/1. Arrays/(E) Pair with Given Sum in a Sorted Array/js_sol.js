//{ Driver Code Starts
// Initial Template for javascript
'use strict';

// Position this line where user code will be pasted.
const readline = require('readline');

const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let input = [];
rl.on('line', (line) => { input.push(line); });

rl.on('close', () => {
    let t = parseInt(input[0].trim());
    let index = 1;

    while (t-- > 0) {
        let arr = input[index].trim().split(" ").map(Number);
        index++;
        let target = parseInt(input[index].trim());
        index++;

        let obj = new Solution();
        let res = obj.countPairs(arr, target);
        console.log(res);
        console.log("~");
    }
});

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */

class Solution {
    countPairs(arr, target) {
        // code here
        let left = 0, right = arr.length - 1;
        let count = 0;
    
        while (left < right) {
            const sum = arr[left] + arr[right];
    
            if (sum === target) {
                // Case 1: values are different → count how many of each
                if (arr[left] !== arr[right]) {
                    let leftVal = arr[left], leftCount = 1;
                    let rightVal = arr[right], rightCount = 1;
    
                    while (left + 1 < right && arr[left + 1] === leftVal) {
                        leftCount++;
                        left++;
                    }
    
                    while (right - 1 > left && arr[right - 1] === rightVal) {
                        rightCount++;
                        right--;
                    }
    
                    count += leftCount * rightCount;
                    left++;
                    right--;
                }
                // Case 2: values are equal → n choose 2
                else {
                    let n = right - left + 1;
                    count += (n * (n - 1)) / 2;
                    break; // all valid combinations are counted
                }
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }
    
        return count;
    }
}
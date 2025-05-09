//{ Driver Code Starts

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split("\n").map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function isZigzag(n, arr) {
    let f = 1;

    for (let i = 1; i < n; i++) {
        if (f) {
            if (arr[i - 1] > arr[i]) return false;
        } else {
            if (arr[i - 1] < arr[i]) return false;
        }
        f = f ^ 1;
    }

    return true;
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {

        // let n = parseInt(readLine());

        // let arr = new Array(n);
        let arr = readLine().split(' ').map(x => parseInt(x));
        // for (let i = 0; i < n; i++) {
        //     arr[i] = input_arr[i];
        // }
        let n = arr.length;
        let obj = new Solution();
        obj.zigZag(arr);
        let flag = 0;
        for (let i = 0; i < n; i++) {
            if (arr[i] == i % 2) {
                flag = 0;
            } else {
                flag = 1;
                break;
            }
        }

        if (flag == 0) {
            console.log("false");
        } else {
            let check = isZigzag(n, arr);
            if (check)
                console.log("true");
            else
                console.log("false");
        }
        console.log("~");
    }
}

// } Driver Code Ends



class Solution {
    /**

    * @param number[] arr

    * @returns none
    */
    zigZag(arr) {
        // code here
        let flag = true; // true = "<" expected
        for (let i = 0; i < arr.length - 1; i++) {
            if (flag) {
                if (arr[i] > arr[i + 1]) {
                    [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
                }
            } else {
                if (arr[i] < arr[i + 1]) {
                    [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
                }
            }
            flag = !flag;
        }
    }
}

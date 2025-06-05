//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', () => {
    inputString =
        inputString.trim().split("\n").map(string => { return string.trim(); });
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    for (let j = 0; j < t; j++) {
        let date = parseInt(readLine());

        let car = readLine().split(' ').map(Number);
        let fine = readLine().split(' ').map(Number);

        let obj = new Solution();
        let res = obj.totalFine(date, car, fine);

        console.log(res);
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript
class Solution {
    /**
    * @param number date
    * @param number[] car
    * @param number[] fine

    * @returns string[]
    */
    totalFine(date, car, fine) {
        // code here
        let total = 0;
        for (let i = 0; i < car.length; i++) {
            if ((date % 2 === 0 && car[i] % 2 !== 0) || (date % 2 !== 0 && car[i] % 2 === 0)) {
                total += fine[i];
            }
        }
        return total;
    }
}
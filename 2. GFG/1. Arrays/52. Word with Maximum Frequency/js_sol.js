//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
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

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let str = readLine();
        let obj = new Solution();
        console.log(obj.maximumFrequency(str));
        console.log("~")
    }
}

// } Driver Code Ends


// User function Template for javascript
class Solution {
    maximumFrequency(s) {
        // Your code goes here.
        const words = s.trim().split(/\s+/);
        const freq = {};
        const firstIndex = {};
        let maxFreq = 0;
        let result = "";

        for (let i = 0; i < words.length; i++) {
            const word = words[i];
            freq[word] = (freq[word] || 0) + 1;
            if (!(word in firstIndex)) {
                firstIndex[word] = i;
            }

            if (
                freq[word] > maxFreq ||
                (freq[word] === maxFreq && firstIndex[word] < firstIndex[result])
            ) {
                maxFreq = freq[word];
                result = word;
            }
        }

        return `${result} ${maxFreq}`;
    }
}
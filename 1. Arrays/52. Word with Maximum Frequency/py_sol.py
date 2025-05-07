class Solution:
    def maximumFrequency(self, s):
        # Your Code goes here
        words = s.split()  # Split by space
        freq = {}  # Dictionary to count frequency
        first_occurrence = {}  # Track first occurrence index
        max_freq = 0
        result_word = ""

        for index, word in enumerate(words):
            freq[word] = freq.get(word, 0) + 1
            if word not in first_occurrence:
                first_occurrence[word] = index

            # Update max frequency and select earliest word
            if (freq[word] > max_freq) or \
               (freq[word] == max_freq and first_occurrence[word] < first_occurrence[result_word]):
                max_freq = freq[word]
                result_word = word

        return f"{result_word} {max_freq}"

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        str = input().strip()
        obj = Solution()
        print(obj.maximumFrequency(str))
        print("~")
# } Driver Code Ends
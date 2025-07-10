def findRepeatedDnaSequences(s):
  
    # Convert DNA string to numbers
    to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    encoded_sequence = [to_int[c] for c in s]
    
    k = 10
    n = len(s)
    
    # If the string is shorter than 10 characters, return an empty list
    if n <= k:
        return []

    a = 4  # Base-4 encoding
    h = 0  # Hash value
    
    seen_hashes, output = set(), set()  # Sets to track hashes and repeated sequences
    
    a_k = 1  # Stores a^L for efficient rolling hash updates

    # Compute the initial hash for the first 10-letter substring
    for i in range(k):
        h = h * a + encoded_sequence[i]
        a_k *= a  

    seen_hashes.add(h)  # Store the initial hash

    # Sliding window approach to update the hash efficiently
    for start in range(1, n - k + 1):
        # Remove the leftmost character and add the new rightmost character
        h = h * a - encoded_sequence[start - 1] * a_k + encoded_sequence[start + k - 1]

        # If this hash has been seen_hashes before, add the corresponding substring to the output
        if h in seen_hashes:
            output.add(s[start : start + k])
        else:
            seen_hashes.add(h)

    return list(output)  # Convert set to list before returning

# Driver code
def main():
    test_cases = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA",
        "ACGTACGTACGTACGTACGTACGTACGTACGT",
    ]
    
    for i, s in enumerate(test_cases):
        print(f'{i+1}.\tInput: "{s}"')
        print(f"\n\tRepeated Sequences: {findRepeatedDnaSequences(s)}")
        print("-" * 100)

if __name__ == "__main__":
    main()
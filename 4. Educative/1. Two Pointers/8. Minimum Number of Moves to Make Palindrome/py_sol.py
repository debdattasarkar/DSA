def min_moves_to_make_palindrome(s):
    # Convert string to list for easier manipulation
    s = list(s)
    
    # Counter to keep track of the total number of swaps
    moves = 0
    
    # Loop to find a character from the right (s[j]) that
    # matches with a character from the left (s[i])
    i, j = 0, len(s) - 1
    while i < j:
        k = j
        while k > i:
            # If a matching character is found
            if s[i] == s[k]:
                # Move the matching character to the correct position on the right
                for m in range(k, j):
                    s[m], s[m + 1] = s[m + 1], s[m]  # Swap
                    # Increment count of swaps
                    moves += 1
                # Move the right pointer inwards
                j -= 1
                break
            k -= 1
        # If no matching character is found, it must be moved to the center of palindrome
        if k == i:
            moves += len(s) // 2 - i
        i += 1

    return moves

# Driver code
def main():
    strings = ["ccxx", "arcacer", "w", "ooooooo", "eggeekgbbeg"]
    
    for index, string in enumerate(strings):
        print(f"{index + 1}.\ts: {string}")
        print(f"\tMoves: {min_moves_to_make_palindrome(string)}")
        print('-' * 100)

if __name__ == "__main__":
    main()
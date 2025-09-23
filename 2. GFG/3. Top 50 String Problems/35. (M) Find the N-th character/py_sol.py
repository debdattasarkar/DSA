#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # Size of each expanded block produced by one original character
        block = 1 << r  # 2^r

        # Which original character's block contains the nth position?
        i = n // block
        off = n % block

        # Convert the original character to integer bit (0/1)
        bit = ord(s[i]) & 1  # '0'->0, '1'->1

        # Parity of set bits at 'off' is the Thue-Morse value
        flips = (off.bit_count() & 1)  # 1 if odd, else 0

        # XOR: original bit flips 'flips' times
        return str(bit ^ flips)
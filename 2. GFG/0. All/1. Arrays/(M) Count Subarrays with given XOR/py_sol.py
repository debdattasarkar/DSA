class Solution:
    def subarrayXor(self, arr, k):
        # Prefix XOR + frequency map
        # Time: O(n), Space: O(n)

        prefix_xor_frequency = {0: 1}  # prefixXor=0 occurs once before we start
        current_prefix_xor = 0
        total_subarrays = 0

        for value in arr:
            # Update prefix XOR up to current index
            current_prefix_xor ^= value

            # We need previous prefix XOR such that:
            # previous_prefix_xor = current_prefix_xor ^ k
            required_prefix_xor = current_prefix_xor ^ k

            # Add how many times we've seen required_prefix_xor before
            total_subarrays += prefix_xor_frequency.get(required_prefix_xor, 0)

            # Record current prefix XOR in the map
            prefix_xor_frequency[current_prefix_xor] = prefix_xor_frequency.get(current_prefix_xor, 0) + 1

        return total_subarrays
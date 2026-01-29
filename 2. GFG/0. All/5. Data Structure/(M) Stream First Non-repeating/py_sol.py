from collections import deque

class Solution:
	def firstNonRepeating(self, s):
		# freq for 26 lowercase letters => O(1) space
        frequency = [0] * 26

        # queue keeps characters in the order they appear
        candidate_queue = deque()

        output_chars = []

        for ch in s:
            idx = ord(ch) - ord('a')

            # Step 1: update frequency
            frequency[idx] += 1

            # Step 2: add to queue as a candidate
            candidate_queue.append(ch)

            # Step 3: remove all repeated chars from the front
            while candidate_queue and frequency[ord(candidate_queue[0]) - ord('a')] > 1:
                candidate_queue.popleft()

            # Step 4: current answer for this prefix
            if candidate_queue:
                output_chars.append(candidate_queue[0])
            else:
                output_chars.append('#')

        return "".join(output_chars)
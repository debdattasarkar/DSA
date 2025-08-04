class Solution:
	def isPalinSent(self, s):
		# code here
		# Two pointers
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
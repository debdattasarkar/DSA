class Solution:
	def minJumps(self, arr):
	    """
        Greedy window expansion (ladder & stairs).
        Time : O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return 0                    # already at the end
        if arr[0] == 0:
            return -1                   # cannot move anywhere

        # We will reach somewhere within arr[0] with our first jump.
        jumps  = 1
        ladder = arr[0]                 # farthest index we can reach so far
        stairs = arr[0]                 # steps we can still take before next jump

        for i in range(1, n):
            if i == n - 1:
                return jumps            # reached the last index

            # Keep improving the farthest we can reach.
            ladder = max(ladder, i + arr[i])

            # Use one step to move from i to i+1 within current jump window.
            stairs -= 1

            # If no more steps left in current window, we must jump.
            if stairs == 0:
                jumps += 1
                # If our best reach is not beyond current i, we are stuck.
                if i >= ladder:
                    return -1
                # Reset the stairs to how many steps are in the new window.
                stairs = ladder - i

        # Should have returned inside loop; if we fall through something's off.
        return -1
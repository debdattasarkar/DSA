class Solution:
    def maxArea(self, mat):
        """
        Time  : O(n * m) — each row builds a histogram; each histogram solved in O(m)
        Space : O(m)     — the heights array + stack
        """
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m
        best = 0

        for r in range(n):
            # 1) Build histogram for this row (consecutive 1s upward)
            for c in range(m):
                if mat[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0

            # 2) Compute largest rectangle in current histogram (monotonic stack)
            best = max(best, self._largestRectangleArea(heights))

        return best

    def _largestRectangleArea(self, heights):
        """
        Standard LC84 solution.
        Stack holds indices of bars in increasing height.
        When we see a shorter bar, we 'resolve' rectangles with bars taller than it.
        """
        stack = []          # indices of increasing heights
        max_area = 0
        # sentinel trick: process all bars by appending a 0 at the end
        for i, h in enumerate(heights + [0]):
            # resolve rectangles that end before 'i'
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                # width: if stack is empty, rectangle extends from 0..i-1
                # else from stack[-1]+1 .. i-1
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
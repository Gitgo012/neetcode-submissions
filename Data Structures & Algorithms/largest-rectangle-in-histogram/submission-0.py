class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height), heights increasing
        best = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx          # new bar inherits the leftmost reach
            stack.append((start, h))

        n = len(heights)
        for idx, height in stack:
            best = max(best, height * (n - idx))

        return best
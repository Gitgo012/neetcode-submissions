class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def backtrack(start):
            res.append(path[:])              # save every path
            for i in range(start, len(nums)):
                path.append(nums[i])         # choose
                backtrack(i + 1)             # explore, only look forward
                path.pop()                   # un-choose

        backtrack(0)
        return res
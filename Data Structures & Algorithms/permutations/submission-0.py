class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):       # complete permutation
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True               # choose
                path.append(nums[i])
                backtrack()                  # explore
                path.pop()                   # un-choose
                used[i] = False

        backtrack()
        return res
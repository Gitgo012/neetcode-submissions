class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                    # groups duplicates together
        res, path = [], []

        def backtrack(start, total):
            if total == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue                 # skip duplicate at the same level
                if total + candidates[i] > target:
                    break                    # sorted, so all later ones overshoot too
                path.append(candidates[i])   # choose
                backtrack(i + 1, total + candidates[i])  # explore (i+1: no reuse)
                path.pop()                   # un-choose

        backtrack(0, 0)
        return res
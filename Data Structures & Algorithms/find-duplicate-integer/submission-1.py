class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return nums[i]
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #array is sorted and we have to deal with 2 numbers = 2 pointer approach
        #1 pointer at start and another pointer at the end
        left=0
        right=len(numbers)-1
        while left<right:
            total=numbers[left]+numbers[right]
            if total<target:
                left+=1
            elif total>target:
                right-=1
            else:
                return [left+1,right+1]

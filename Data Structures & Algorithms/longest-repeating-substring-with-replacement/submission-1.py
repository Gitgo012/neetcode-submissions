class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_length=0
        answer=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_length=max(max_length,count[s[right]])
            if ((right-left+1)-max_length>k):
                count[s[left]]-=1
                left+=1
            answer=max(answer,right-left+1)
        return answer

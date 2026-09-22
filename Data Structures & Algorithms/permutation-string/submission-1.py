class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        window=len(s1)
        count={}
        seen={}
        left=0
        for ch in range(len(s1)):
            count[s1[ch]]=count.get(s1[ch],0)+1
        for right in range(len(s2)):
            seen[s2[right]]=seen.get(s2[right],0)+1
            if right-left+1>window:
                seen[s2[left]]-=1
                if seen[s2[left]]==0:
                    del seen[s2[left]]
                left+=1 
            if right-left+1==window:
                if count==seen:
                    return True
        return False
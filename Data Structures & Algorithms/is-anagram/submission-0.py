from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        collection1=Counter(s)
        collection2=Counter(t)
        if collection1==collection2:
            return True
        else:
            return False
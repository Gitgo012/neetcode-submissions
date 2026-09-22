class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif ch==')' and stack[-1]!='(':
                    return False
                elif ch==']' and stack[-1]!='[':
                    return False
                elif ch=='}' and stack[-1]!='{':
                    return False
                stack.pop()
        return len(stack)==0
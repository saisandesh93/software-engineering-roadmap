class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for ch in s:
            if ch in '([{':
                l.append(ch)
            else:
                if not l:
                    return False
                if ch == ')' and l[-1] !='(':
                    return False
                if ch == ']' and l[-1] !='[':
                    return False
                if ch == '}' and l[-1] !='{':
                    return False
                l.pop()
        return not l
            

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = {"}": "{", ")": "(", "]": "["}

        for i in s:
            if i in res:
                if stack and stack[-1] == res[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False

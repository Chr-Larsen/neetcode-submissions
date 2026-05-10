class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        j = 0
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if (stack[j] == "]" and stack[j-1] == "[") or (stack[j] == "}" and stack[j-1] == "{") or (stack[j] == ")" and stack[j-1] == "("):
                stack.pop()
                stack.pop()
                j-=2
            j+=1
        if len(stack) != 0:
            return False
        else:
            return True
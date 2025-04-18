class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxlength=0
        for i,char in enumerate(s):
            if(char=='('):
                stack.append(i)
            elif(char==')'):
                stack.pop()
                if(not stack):
                    stack.append(i)
                else:
                    maxlength=max(maxlength,i-stack[-1])
        return maxlength

        

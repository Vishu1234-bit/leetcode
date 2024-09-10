class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = []
        i=0
        sign = 1
        while(i<len(s)):
            char = s[i]
            if(char.isdigit()):
                num = 0
                while(i<len(s) and s[i].isdigit()):
                    num = num*10+int(s[i])
                    i+=1
                result+=(num*sign)
                i-=1
            elif(char == '+'):
                sign = 1
            elif(char == '-'):
                sign = -1
            elif(char == '('):
                stack.append(result)
                stack.append(sign)
                result=0
                sign = 1
            elif(char==')'):
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result=prev_result+prev_sign*result
            i+=1
        return result

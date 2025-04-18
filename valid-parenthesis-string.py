class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i,parantheses in enumerate(s):
            if(parantheses=='('):
                stack.append(i)
                print(stack)
            elif(parantheses==')'):
                if(len(stack)):
                    stack.pop()
                elif(len(star)):
                    star.pop()
                else:
                    return False
                print(stack,star)
            elif(parantheses=='*'):
                star.append(i)
        while(stack and star):
            if(stack[-1]>star[-1]):
                return False
            star.pop()
            stack.pop()
        print(stack,star)
        return len(stack)==0

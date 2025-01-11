class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if(ast<0):
                while(stack and ast<0<stack[-1]):
                    if(abs(stack[-1])<abs(ast)):
                        stack.pop()
                    elif(abs(stack[-1])==abs(ast)):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(ast)
            else:
                stack.append(ast)
        return stack
        

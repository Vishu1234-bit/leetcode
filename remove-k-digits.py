class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(k==len(num)):
            return "0"
        stack = []
        for i in range(len(num)):
            while(k>0 and stack and int(stack[-1])>int(num[i])):
                stack.pop()
                k-=1
            stack.append(num[i])
        while(k>0 and stack):
            stack.pop()
            k-=1
        output = ''.join(stack).lstrip("0")

        return output if output else "0"

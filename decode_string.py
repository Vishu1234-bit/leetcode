class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if(char!=']'):
                stack.append(char)
            else:
                curr_str = ""
                while(stack[-1]!='['):
                    curr_str = stack.pop()+curr_str
                stack.pop()
                curr_num = ""
                while(stack and stack[-1].isdigit()):
                    curr_num = stack.pop()+curr_num
                stack.append(int(curr_num)*curr_str)
        return "".join(stack)

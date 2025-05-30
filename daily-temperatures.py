class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in range(len(temperatures))]
        stack =[]
        for i in range(len(temperatures)-1,-1,-1):
            temp = temperatures[i]
            while(stack and temperatures[stack[-1]]<=temp):
                stack.pop()
            if(stack):
                answer[i] = stack[-1]-i
            stack.append(i)
        print(answer)
        return answer


            

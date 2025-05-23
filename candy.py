class Solution:
    def candy(self, ratings: List[int]) -> int:
        if(len(ratings)==1):
            return 1
        candy = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                candy[i] = candy[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                candy[i] = max(candy[i],candy[i+1]+1)
        return sum(candy)

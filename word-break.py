class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        wordset = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i):
                if(dp[j] and s[j:i] in wordset):
                    dp[i]=True
                    break
        return dp[len(s)]

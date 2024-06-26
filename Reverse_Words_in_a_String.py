class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=[]
        print(s.split(" "))
        for i in s.split(" "):
            if(len(i)!=0):
                print("not space")
                words.append(i)
        reversed_s=""
        for i in range(len(words)-1,0,-1):
            if(len(words[i]) != 0):
                reversed_s+=words[i]
                reversed_s+=" "
        reversed_s+=words[0]
        return reversed_s

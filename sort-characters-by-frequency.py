class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = {}
        for i in s:
            if(i not in frequency):
                frequency[i] = 1
            else:
                frequency[i]+=1
        res=""
        frequency_dict = sorted(frequency.items(),key=lambda x:x[1] ,reverse=True)
        print(frequency_dict)
        res=[]
        for i in frequency_dict:
            res.append(i[0]*i[1])
        return ''.join(res)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j = len(a)-1,len(b)-1
        result = []
        carry=0
        while(i>=0 or j>=0 or carry == 1):
            bit_a = int(a[i]) if (i>=0) else 0
            bit_b = int(b[j]) if (j>=0) else 0
            sumbits = bit_a+bit_b +carry
            carry = sumbits//2
            result.append(str(sumbits%2))
            i-=1
            j-=1
        result = result[::-1]
        resstr = ''.join(result)
        return resstr
                
            
            
            

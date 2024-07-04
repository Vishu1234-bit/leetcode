class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index=0
        replace=0
        while index < len(chars):
            curr_letter = chars[index]
            count=0
            while(index<len(chars) and chars[index]==curr_letter):
                count+=1
                index+=1
            chars[replace] = curr_letter
            replace+=1
            if(count>1):
                for integer in str(count):
                    chars[replace]=integer
                    replace+=1
        return replace

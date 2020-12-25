class Solution:
    def reverse(self, x: int) -> int:
        min_ = -2147483648
        max_ =2147483648
        if((x < min_) or (x > max_)):
            return 0
        else:
            rev = 0
            sign =(x>0)-(x<0)
            x = abs(x)
            while(x>0):
                rem = x%10
                rev = (rev*10)+rem
                x = x//10
            if((rev < min_) or (rev > max_)):
                return 0
            return rev*sign

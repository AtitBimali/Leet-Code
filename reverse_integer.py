#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = 1
        if(x<0):
            sign = -1
            x = x*sign
        while(x>0):
            rem = x % 10
            sum = sum*10 + rem
            x = x//10
        if not -2147483648<sum<2147483648:
            return 0
        return sign*sum
    
            

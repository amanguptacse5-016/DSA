class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        num = abs(x)
        rev = 0

        while num != 0:
            digit = num % 10
            rev = (rev * 10) + digit
            num = num // 10
        
        rev = rev * sign
         
  
        if rev < -(2 ** 31) or rev > 2 ** 31 - 1:
            return 0
        return rev
        
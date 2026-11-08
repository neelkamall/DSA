class Solution(object):
    def myPow(self, x, n):
        neg = n < 0
        n = abs(n)
        def direct(x, n):
            if n == 0:
                return 1
            half = direct(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        result = direct(x, n)        
        if neg:
            return 1/result
        return result            
                   

        
        
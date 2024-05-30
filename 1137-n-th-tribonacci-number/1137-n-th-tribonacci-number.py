class Solution:

    """
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(n+3) = f(n) + f(n+1) + f(n+2)
    f(n+4) = f(n+1) + f(n+2) + f(n+3)
    
    f(n) = f(n-1) + f(n-2) + f(n-3)
    """
    def tribonacci(self, n: int) -> int:
        tb = [0] * (38)
        tb[0] = 0
        tb[1] = 1
        tb[2] = 1

        for i in range(3, n+1):
            tb[i] = tb[i-1] + tb[i-2] + tb[i-3]
        
        return tb[n]
        
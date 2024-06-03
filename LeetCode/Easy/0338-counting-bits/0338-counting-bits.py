
"""
0: 00
1: 01

2: 10 -> 1
3: 11 -> 2

4: 100 -> 1 (앞자리1 + 0의 값 0)
5: 101 -> 2 (앞자리1 + 1의 값 1)
6: 110 -> 2 (앞자리1 + 2의 값 1)
7: 111 -> 3 (앞자리1 + 3의 값 2)

8: 1000
9: 1001
10: 1010
11: 1011
12: 1100
13: 1101
14: 1110
15: 1111
-> 8~15는 0~7까지의 값을 재활용
tb[8] = tb[0] + 1
tb[9] = tb[1] + 1

"""
class Solution:

    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        tb = [0, 1]
        val = 2

        while True:
            for i in range(val):
                if len(tb) == n:
                    tb.append(tb[i] + 1)
                    return tb
                tb.append(tb[i] + 1)
            
            val *= 2
        
        return tb

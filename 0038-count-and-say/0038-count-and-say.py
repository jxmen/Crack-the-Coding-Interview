"""
f(1) = "1"
f(2) = "11" (1이 1번 반복)
f(3) = "21" (1이 2번 반복)
f(4) = "1211" (2 1번, 1 1번)

압축: 반복되는 숫자의 카운트 + 해당 숫자
"333" -> "23" (3이 2번 반복)
"4444" -> "34"
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        def compress(s):
            p = 0
            result = ""
            while p < len(s):
                count = 1
                while p < len(s):
                    if p == len(s) - 1 or s[p] != s[p+1]:
                        break
                    count += 1
                    p += 1
                
                result += str(count) + s[p]
                p += 1
                
            return result

        def helper(n, cache):
            if n in cache:
                return cache[n]
        
            compressed = compress(helper(n-1, cache))
            cache[n] = compressed
            
            return compressed
            
        cache = {1: "1"}
        return helper(n, cache)

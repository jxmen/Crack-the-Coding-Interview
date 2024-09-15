class Solution:
    def decodeString(self, s: str) -> str:

        def helper(s, p):
            o = ""
            num = 0
            while p < len(s):
                if s[p].isdigit():
                    num = (num * 10) + int(s[p])
                elif s[p] == '[':
                    decoded, p = helper(s, p + 1)
                    o += decoded * num
                    num = 0
                elif s[p] == ']':
                    return o, p
                else:
                    o += s[p]
                p += 1
            
            return o, p
    
        p = 0
        output = ""
        while p < len(s):
            if s[p].isdigit():
                num = 0
                while s[p].isdigit():
                    num = (num * 10) + int(s[p])
                    p += 1

                decoded, p = helper(s, p + 1)
                output += decoded * num
                p += 1
            else:
                output += s[p]
                p += 1
        
        return output
    
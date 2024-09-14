
# TODO: aaa[a] 형태로 출력되어 수정 필요
class Solution:
    def decodeString(self, s: str) -> str:

        def helper(s, p):
            o = ""
            stack = [s[p]]
            while stack:
                p += 1
                while not s[p].isdigit() and s[p] != ']':
                    o += s[p]
                    p += 1

                if s[p] == ']':
                    stack.pop()

                num = ""
                while s[p].isdigit():
                    num += s[p]
                    p += 1

                if num != '':
                    o += helper(s, p) * int(num)

            return o

        p = 0
        output = ""
        while p < len(s):
            if not s[p].isdigit():
                output += s[p]
                p += 1
                continue

            # 숫자라면 num str에 추가한다.

            num = ""
            while s[p].isdigit():
                num += s[p]
                p += 1

            # 복호화한 문자를 num만큼 output에 추가한다.
            if num != '':
                decoded = helper(s, p)
                output += decoded * int(num)


        return output

"""
str1과 str2가 주어질때, 이 두 문자열을 동시에 나눌 수 있는 최대 길이의 문자를 리턴하라. 

나눈다 -> (s = t+t+t...)
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 크기가 작은 문자열 하나를 기준으로, 한글자씩 늘려가면서 나눠지는지 확인한다.
        lessLenStr = str1 if len(str1) <= len(str2) else str2
        answer = ''
        for i in range(1, len(lessLenStr)+1):
            subString = lessLenStr[:i]
            
            # 2. 문자열을 subString으로 split 했을 때 전부 그 문자열이면 answer에 할당한다.
            str1Divided = all(map(lambda x: x == '', str1.split(subString)))
            str2Divided = all(map(lambda x: x == '', str2.split(subString)))
            if str1Divided and str2Divided:
                answer = subString

        return answer

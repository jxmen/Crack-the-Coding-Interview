class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        maxVowels = 0

        # k개만큼 sliding window를 잡는다.
        windowVowelsCount = 0
        sliced = s[:k]

        # 연속된 모음이 몇개인지 찾고 max 변수에 할당한다.
        for x in sliced:
            if x in vowels:
                windowVowelsCount += 1
                maxVowels = max(maxVowels, windowVowelsCount)
            else:
                windowVowelsCount = 0

        # 나머지 문자열은 한개씩 확인하면서 연속된 개수가 몇개인지 확인한다.
        for i in range(k, len(s)):
            if s[i] in vowels:
                if windowVowelsCount >= k: # k개가 넘어가면 더이상 취급하지 않음
                    continue
                windowVowelsCount += 1
                maxVowels = max(maxVowels, windowVowelsCount)
            else:
                windowVowelsCount = 0

        return maxVowels

"""
아나그램 판별을 어떻게 하지? map?

1. 서로 일치한지 비교를 어떻게 할 것인가?
2. 인덱스가 늘어날 때 map을 어떻게 업데이트 할 것인가?

"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        ans = []

        p_freq = {}
        for c in p:
            p_freq[c] = p_freq.get(c, 0) + 1

        s_freq = {}
        for c in s[:n]:
            s_freq[c] = s_freq.get(c, 0) + 1

        if p_freq == s_freq:
            ans.append(0)

        for i in range(1, len(s) - n + 1):
            s_freq[s[i - 1]] = s_freq.get(s[i - 1], 0) - 1
            if s_freq.get(s[i - 1]) == 0:
                del s_freq[s[i - 1]]

            s_freq[s[i + n - 1]] = s_freq.get(s[i + n - 1], 0) + 1
            if p_freq == s_freq:
                ans.append(i)

        return ans

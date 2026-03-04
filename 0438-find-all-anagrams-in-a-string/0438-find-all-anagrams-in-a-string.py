from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        ans = []
        p_freq = Counter(p)
        s_freq = Counter(s[:n])

        if p_freq == s_freq:
            ans.append(0)

        for i in range(1, len(s) - n + 1):
            left, right = s[i - 1], s[i + n - 1]

            s_freq[left] -= 1
            if s_freq[left] == 0:
                del s_freq[left]

            s_freq[right] += 1

            if p_freq == s_freq:
                ans.append(i)

        return ans

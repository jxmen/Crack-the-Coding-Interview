"""
1. 처음 k만큼 길이의 문자열은 서로 앞뒤 뒤집기
2. 이후 문자열은 k만큼 스킵
3. 이후에도 k만큼 뒤집기. 단, 문자열 끝이 k보다 작을 경우 그만큼도 뒤집기
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(arr, start, end):
            end = min(end, len(arr)-1)

            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        arr = list(s)
        for i in range(0, len(s), 2 * k):
            reverse(arr, i, i+k-1)

        return ''.join(arr)

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            start, end = 0, len(s) - 1
            arr = list(s)
            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start, end = start + 1, end - 1

            return ''.join(arr)

        strings = s.split(' ')
        return ' '.join(list(map(lambda it: reverse(it), strings)))

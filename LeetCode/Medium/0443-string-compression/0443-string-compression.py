class Solution:
    def compress(self, chars: List[str]) -> int:
        # 다음 문자나 끝을 만난다면, 구한 문자의 숫자 개수를 뒤에 붙여준다.

        idx = 0
        replaceIdx = 0 # 바꿀 문자열 인덱스
        while idx < len(chars):
            count = 0
            char = chars[idx]
            while idx < len(chars) and char == chars[idx]:
                idx += 1
                count += 1

            chars[replaceIdx] = char
            replaceIdx += 1

            if count > 1:
                # '12'의 경우 '1', '2'를 모두 넣어준다.
                for c in str(count):
                    chars[replaceIdx] = c
                    replaceIdx += 1

        return len(chars[:replaceIdx])
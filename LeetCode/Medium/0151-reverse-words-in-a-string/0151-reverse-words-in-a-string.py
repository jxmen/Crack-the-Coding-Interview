class Solution:

    # TODO: build-in 함수 쓰지 않고 구현해보기
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join([word for word in reversed(words) if word.strip()])

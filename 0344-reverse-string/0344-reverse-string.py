class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # 0번 인덱스와 마지막 인덱스부터 서로 스위칭한다.
        for i in range(0, len(s) // 2):
            c = s[i]
            target_to_change = s[len(s) - 1 - i]
            
            s[i] = target_to_change
            s[len(s) - 1 - i] = c
        
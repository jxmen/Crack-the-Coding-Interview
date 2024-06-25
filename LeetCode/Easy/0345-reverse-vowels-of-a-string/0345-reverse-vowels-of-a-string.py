class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left, right = 0, len(sList) - 1
        
        while left < right:
            # find volwel index
            while left < right and sList[left] not in vowels:
                left += 1
            while left < right and sList[right] not in vowels:
                right -= 1
            
            if left < right:
                # swap
                temp = sList[right]
                sList[right] = sList[left]
                sList[left] = temp

                left += 1
                right -= 1
        
        return ''.join(sList)
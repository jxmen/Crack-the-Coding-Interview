class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest = 0
        beforeSum = 0
        for i in range(len(gain)):
            
            # 구간 합을 추가한다.
            prefix = beforeSum + gain[i]
            beforeSum = prefix

            # 최대값을 갱신한다.
            largest = max(largest, prefix)
        
        return largest

    def largestAltitude2(self, gain: List[int]) -> int:
        largest = 0
        prefixes = [0] # 처음엔 무조건 0으로 시작한다.
        for i in range(len(gain)):
            
            # 구간 합을 추가한다.
            prefix = prefixes[i] + gain[i]
            prefixes.append(prefix)

            # 최대값을 갱신한다.
            largest = max(largest, prefix)
        
        return largest

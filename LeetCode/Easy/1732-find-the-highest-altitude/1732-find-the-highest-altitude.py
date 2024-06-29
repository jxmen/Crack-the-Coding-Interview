class Solution:

    # time: O(N), space: O(2) (= O(1))
    def largestAltitude(self, gain: List[int]) -> int:
        largest, beforeSum = 0, 0
        for i in range(len(gain)):
            # 합을 추가한다.
            currentSum = beforeSum + gain[i]

            # 최대값을 갱신한다.
            largest = max(largest, currentSum)
            beforeSum = currentSum
        
        return largest

    # time: O(N), space: O(N)
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

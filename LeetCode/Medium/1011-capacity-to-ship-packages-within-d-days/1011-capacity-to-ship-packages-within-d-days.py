"""
컨베이어 벨트에 있는 패키지들은 항구에서 days안에 배달되어야 한다

i번째 패키지에 있는 컨베이어 벨트는 weights[i] 만큼의 중량을 가진다.
어떤 날에는, 우리는 선박을 컨베이어 벨트에 있는 패키지와 이동하기로 했다.
우리는 최대 용량보다는 적게 운반해야 한다.

리턴해라 '최소 무게의 용량'을 선박의 컨베이어 벨트안에 있는 패키지가 days안에 이동되는

---
선박의 무게를 얼마로 해야지 최소 용량으로 days안에 모두 해결할 수 있을 것인가?
"""
class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        answers = []
        start, end = max(weights), sum(weights)
        
        while start <= end:
            middle = (start + end) // 2
            if self.canShip(weights, middle, days):
                answers.append(middle)
                end = middle - 1
            else:
                start = middle + 1
        
        return min(answers)

    def canShip(self, weights: List[int], middle: int, days: int) -> bool:
        currentWeightTotal = 0
        dayCount = 1
        
        for weight in weights:
            if weight + currentWeightTotal > middle:
                dayCount += 1
                currentWeightTotal = weight
            else:
                currentWeightTotal += weight
            
            if dayCount > days:
                return False
        
        return dayCount <= days

    # Time Limit Exceed...
    def shipWithinDays2(self, weights: List[int], days: int) -> int:
        # 1. 차례대로 숫자를 증가시킨다. 그리고 모든 weights를 days안에 처리했다면, 그 값을 바로 리턴한다.
        answer = max(weights) # 화물은 용량은 패키지의 가장 큰 값이 최소가 되어야 실을 수 있다.
        weightsSum = sum(weights)

        while answer < weightsSum:
            currentWeightTotal = 0 # 현재 화물 총량
            dayCount = 1 # 날짜 횟수
            for weight in weights:
                if currentWeightTotal + weight > answer:
                    dayCount += 1
                    currentWeightTotal = weight
                else:
                    currentWeightTotal += weight

            if dayCount <= days:
                break
            else:
                answer += 1

        return answer
    
    

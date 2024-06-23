"""
당신은 일부 플롯이 심어지고 일부는 심어지지 않은 긴 화단이 있습니다. 단, 인접한 밭에는 꽃을 심을 수 없습니다.

0과 1이 포함된 정수 배열 화단(0은 비어 있음을 의미하고 1은 비어 있지 않음을 의미)과 정수 n이 주어지면 인접 꽃 없음 규칙을 위반하지 않고 n개의 새 꽃을 화단에 심을 수 있으면 true를 반환하고, 그렇지 않으면 false를 반환합니다.
===
그리디?
처음에 비어있다면 그냥 심는다
[0 0 0 0 0] -> [1 0 0 0 0] n = 3

[0 0 0] -> [1 0 0] n = 2

[0] -> [1] n = 1
return True

===
[0,1,0] n=1 -> False


"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        elif len(flowerbed) == 0:
            return False
        elif len(flowerbed) == 1:
            return flowerbed[0] == 0 and n == 1

        first, second = flowerbed[0], flowerbed[1]
        if first == 1:
            return self.canPlaceFlowers(flowerbed[2:], n)
        elif second == 1:
            return self.canPlaceFlowers(flowerbed[3:], n)
        else:
            return self.canPlaceFlowers(flowerbed[2:], n-1)

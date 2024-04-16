class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # 4n -> n, 1000n -> n
        # new_nums = [0 for i in range(len(nums))] # 공간을 n만큼 먹네?

        # nums = [3,4,-1,1]
        n = len(nums) # 4
        for i in range(n):
            v = nums[i] # nums 안에 있는 값 3
            if v <= 0 or v > n:
                nums[i] = -1
                continue
    
            while True:
                # 한번만 해야할까? 루프문이 하나 더 필요할 수 있다.
                if nums[v-1] == v:
                    break

                # swap
                tmp = nums[v-1]
                nums[v-1] = v
                nums[i] = tmp

                # tmp가 비정상적인 값(인덱스로 접근 불가능 하면 탈출)
                if tmp <= 0 or tmp > n:
                    break
                v = tmp

            # [1, -1, 3, 3]
            # i = 3
            # v = nums[i] = 3
            # tmp = nums[v-1] = 3
            
            # [-1,1,3,4] -> [1, -1, 3, 4]
            # i = 2

            # nums(origin) [3,4,-1,1] 
            # idx  [0,1, 2,3]
            # nums = [-1,4,3,1]
            # i = 1
            # v = 4
            # tmp = nums[v-1] = 1
            # nums = [-1,1,3,4]
            # v = 1

            # i = 1
            # v = 1
            # tmp = -1


            # 2번에 3이 들어가야 

            # 인덱스를 벗어나면 0으로 바꿔버리기?
            # [1,2,3,4,5] -> 6
            # [2,3,4,5] -> 1
                # 왜? 1이 없어
                # 순서가 안맞아
                # 5를 접근하려고 하면 out of range가 생겨
            # len보다 큰 숫자가 들어온다 -> 변환할 필요가 없음!!
            # 음수의 경우는? 애초에 고려할 필요가 없음

            # [7,8,9,11,12]
            # 7번을 접근했는데 out of range
            # 그러면 index[0] = -1 로 처리?
            # 8번은?
            # [-1, -1, ...] 이렇게 되야함?
            # [-1]
            # 할게 없네?
     
        # [1, -1, 3, 4]
        # [1,2,3,4]
        # [7,8,9,11,12]
        for i in range(n):
            num = nums[i]
            if num == i + 1:
                continue
            else:
                return i + 1

        # 만약 1~n까지 다 있으면 n+1 리턴. 아니면 1 리턴
        return n + 1

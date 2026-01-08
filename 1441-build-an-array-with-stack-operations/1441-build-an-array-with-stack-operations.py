class Solution:
    # nums 안쓰고 구현
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        num = 1
        nums = []
        target_pointer = 0
        
        while num <= n and target_pointer < len(target):
            # num 일단 nums에 넣고, pointer값과 다르다면 pop 한다.
            operations.append("Push")
            nums.append(num)

            # pointer값과 다르면 pop
            if num != target[target_pointer]:
                operations.append("Pop")
                nums.pop()
            else:
                target_pointer += 1
            
            num += 1

        return operations

    def buildArray2(self, target: List[int], n: int) -> List[str]:
        operations = []
        num = 1
        nums = []
        target_pointer = 0
        
        while num <= n:
            # 같다면 중지
            if nums == target:
                return operations
            
            # num 일단 nums에 넣고, pointer값과 다르다면 pop 한다.
            operations.append("Push")
            nums.append(num)

            # pointer값과 다르면 pop
            if num != target[target_pointer]:
                operations.append("Pop")
                nums.pop()
            else:
                target_pointer += 1
            
            num += 1

        return operations

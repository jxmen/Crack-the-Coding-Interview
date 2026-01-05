# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 길이 n을 구한다.
        n, node = 0, head
        while node:
            n += 1
            node = node.next

        if n == 1:
            return None # 하나면 바로 삭제
        
        # 2. (n/2) 만큼 이동한다
        mid = (n//2)
        prev_node = None
        mid_node = head
        for _ in range(mid):
            prev_node = mid_node
            mid_node = mid_node.next
        
        # 3. 삭제 처리를 진행하고, head를 리턴한다
        prev_node.next = mid_node.next
        mid_node.next = None

        return head


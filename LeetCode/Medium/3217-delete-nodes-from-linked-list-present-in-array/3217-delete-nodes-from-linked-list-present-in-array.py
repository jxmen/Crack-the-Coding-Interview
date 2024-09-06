# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums) # nums are unique.

        # 처음 헤드가 가리키는 값이 set에 없도록 재배치한다.
        while head and head.val in numsSet:
            head = head.next

        # set에 있으면 지운다.
        node = head
        while node and node.next:
            if node.next.val in numsSet:
                node.next = node.next.next
            else:
                node = node.next

        return head

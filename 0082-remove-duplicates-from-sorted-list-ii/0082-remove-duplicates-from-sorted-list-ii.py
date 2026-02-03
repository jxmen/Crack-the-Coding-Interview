# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while prev.next:
            curr = prev.next

            # 중복 시 모든 노드 건너뛰기
            if curr.next and curr.val == curr.next.val:
                val = curr.val
                while prev.next and prev.next.val == val:
                    prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        # slowPrev - slow 전의 값
        slow, slowPrev, fast = head, head, head
        while fast and fast.next:
            slowPrev = slow
            slow = slow.next
            fast = fast.next.next
        
        # slow가 삭제하려는 대상이므로, slow 전의 next 값을 slow가 아닌 slow.next로 변경한다.
        slowPrev.next = slow.next
        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxTwinSum = 0

        # fast는 맨 끝으로 이동한다.
        slow, fast = head, head
        length = 0
        while fast and fast.next:
            fast.next.prev = fast
            fast = fast.next
            length += 1
        
        # twin sum을 구한다.
        for i in range(length):
            maxTwinSum = max(maxTwinSum, slow.val + fast.val)
            slow = slow.next
            fast = fast.prev
        
        return maxTwinSum

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tail과 list의 길이를 구한다. len(list) // 2만큼 반복한다.
        if not head:
            return None

        tail, len_list = None, 1
        node = head
        while node.next:
            node = node.next
            len_list += 1
            tail = node

        if not tail:
            return head
        
        node = head
        for _ in range(len_list // 2):
            # tail.next를 node.next로 할당한다.
            tail.next = node.next
            node.next = node.next.next
            tail.next.next = None
            tail = tail.next
            node = node.next
        
        return head

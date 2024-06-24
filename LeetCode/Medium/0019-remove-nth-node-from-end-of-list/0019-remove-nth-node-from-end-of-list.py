# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
마지막으로 n번째 노드를 제거하고 head 반환
[1,2,3,4,5] n=2일 경우 마지막 2번째인 4 제거
-> [1,2,3,5]
===
1. 1,2,3,4,5 순서대로 돈 후 n만큼 prev로 이동하고 값을 교체
2. two pointer 활용이 가능할까? (X)
2.1. length = 5, n=5일 경우 불가능..
2.2. hint: two pointer + n개만큼 지연
3. length를 먼저 구한 후 이동 후 값 교체 (one pass 알고리즘은 아님)
"""

class Solution:

    # TODO: one pass 알고리즘으로 변경하기
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length를 먼저 구한 후 이동 후 값 교체 (one pass 알고리즘은 아님)
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        
        node = head
        for i in range(length - n - 1):
            node = node.next

        if n == length:
            return head.next

        if not node.next:
            return None
        else:
            node.next = node.next.next
            return head

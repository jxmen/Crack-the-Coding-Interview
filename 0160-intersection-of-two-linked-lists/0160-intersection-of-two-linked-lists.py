# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = set()

        # a의 next가 none이 될때까지 다 이동시키고 set에 저장한다.
        node_a = headA
        while node_a:
            visited_nodes.add(node_a)
            node_a = node_a.next

        # b를 이동시킨다. set에 있다면 겹치는 node가 있다는 것이므로 바로 리턴한다.
        node_b = headB
        while node_b:
            if node_b in visited_nodes:
                return node_b
            
            visited_nodes.add(node_b)
            node_b = node_b.next

        return None

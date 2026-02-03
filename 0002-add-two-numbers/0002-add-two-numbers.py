# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 -> [n(2), n(4), n(3)] -> 342
        def get_node_sum(root, i=0, v=0):
            if not root:
                return v
            
            return v + (root.val * pow(10, i)) + get_node_sum(root.next, i+1, v)
        
        def to_node(val):
            head = ListNode(val % 10)
            node = head
            val //= 10

            while val > 0:
                new_node = ListNode(val % 10)
                val //= 10
                node.next = new_node
                node = new_node

            return head
        
        nodes_sum = get_node_sum(l1) + get_node_sum(l2)
        return to_node(nodes_sum)
            
        
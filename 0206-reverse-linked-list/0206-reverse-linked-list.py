# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack을 쓸까?
        # 스택에 다 넣고 마지막꺼를 pop해서 연결하자

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        # 스택에서 하나를 꺼내고, 스택 마지막에 노드가 있다면 next로 연결한다.
        if not stack:
            return node
        
        node = stack[-1]
        while stack:
            last = stack.pop()
            if stack:
                last.next = stack[-1]
            else:
                last.next = None
        
        if last:
            last.next = None
        
        return node
        
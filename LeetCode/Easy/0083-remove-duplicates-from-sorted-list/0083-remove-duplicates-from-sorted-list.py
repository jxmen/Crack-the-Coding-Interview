# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 중복인걸 어떻게 확인할 것인가? - set?
        numSet = set()
        node = head
        while node and node.next:
            numSet.add(node.val)
            if node.next.val in numSet:                
                # 같은 값이 아닐때까지 찾아서 다음 값으로 할당한다.
                node.next = self.findNotMatchVal(node.next) 
            
            node = node.next
        
        return head
    
    def findNotMatchVal(self, head):
        headVal = head.val # head 값 미리 저장
        node = head
        while node and node.next:
            if node.next.val != headVal:
                return node.next
            
            node = node.next

        return None

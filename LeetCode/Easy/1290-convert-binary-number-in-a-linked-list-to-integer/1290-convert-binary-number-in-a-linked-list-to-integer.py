# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode, s = '') -> int:
        if not head:
            return self.binary_to_int(s)
        
        return self.getDecimalValue(head.next, s + str(head.val))

    def binary_to_int(self, binary_str):
        return int(binary_str, 2)

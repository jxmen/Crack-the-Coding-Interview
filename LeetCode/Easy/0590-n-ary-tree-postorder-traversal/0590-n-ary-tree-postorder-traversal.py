"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        answer = []
        for c in root.children:
            answer.extend(self.postorder(c))

        answer.append(root.val)
        return answer
        
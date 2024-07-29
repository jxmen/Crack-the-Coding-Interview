class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodeSet = set()
        for edge in edges:
            for node in edge:
                if node in nodeSet:
                    return node
                
                nodeSet.add(node)
        
        return -1
    
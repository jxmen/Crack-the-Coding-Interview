class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        visited[0] = 1
        
        self.visit(rooms, rooms[0], visited)
        
        return all(v != 0 for v in visited)
    
    def visit(self, rooms, room, visited):
        for key in room:
            if visited[key] == 1:
                continue

            visited[key] = 1
            self.visit(rooms, rooms[key], visited)

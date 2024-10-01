class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gq = deque(g)
        sq = deque(s)
        count = 0
        while gq and sq:
            sq_size, rotate_count = len(sq), 0
            
            # 무한루프 되지 않도록 처리
            while gq and sq and sq[0] < gq[0]:
                sq.append(sq.popleft())
                rotate_count += 1
                if rotate_count >= sq_size:
                    return count
            
            sq.popleft()
            gq.popleft()
            count += 1

        return count

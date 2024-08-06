import heapq


class Solution:
    def minimumPushes(self, word: str) -> int:
        count_map = {}
        for c in list(word):
            if c not in count_map:
                count_map[c] = 1
            else:
                count_map[c] += 1

        # 최대 힙 생성
        max_heap = [-v for v in count_map.values()]
        heapq.heapify(max_heap)

        minimun_pushes = 0  # result
        mapped_count = 0  # 번호에 할당 시킨 개수

        # 가장 큰 값을 먼저 할당 시킨다.
        while max_heap:
            # 힙에서 하나씩 꺼내고 카운트를 증가시킨다.
            mapped_count += 1
            heappop = -heapq.heappop(max_heap)

            # 꺼낸 값에서 몇번 눌러야 하는지를 계산해서, 해당 값을 더해준다.
            # 8 -> 0, 9 -> 1, 15 -> 1, 16 -> 1, 17 -> 2
            press_count = ((mapped_count - 1) // 8) + 1
            minimun_pushes += (heappop * press_count)

        return minimun_pushes

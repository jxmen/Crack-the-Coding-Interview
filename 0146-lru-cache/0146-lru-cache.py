class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy 노드
        self.head = Node(0, 0)  # 가장 최근
        self.tail = Node(0, 0)  # 가장 오래됨
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # 이미 존재하면 제거
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]

        # 새 노드 생성 및 추가
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        # 용량 초과 시 가장 오래된 노드 제거
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        """리스트에서 노드 제거"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node) -> None:
        """head 바로 뒤에 노드 추가 (가장 최근 사용)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

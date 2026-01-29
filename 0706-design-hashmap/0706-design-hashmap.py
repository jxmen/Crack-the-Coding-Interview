"""
어떻게 내장 라이브러리를 안쓰고 구현할 수 있을까?

{1:1, 2:2}

해싱을 한다?
"""
class MyHashMap:

    def __init__(self):
        self.buckets = [-1] * pow(10, 6)

    def put(self, key: int, value: int) -> None:
        index = key % len(self.buckets)
        self.buckets[index] = value

    def get(self, key: int) -> int:
        index = key % len(self.buckets)
        return self.buckets[index]

    def remove(self, key: int) -> None:
        self.buckets[key % len(self.buckets)] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

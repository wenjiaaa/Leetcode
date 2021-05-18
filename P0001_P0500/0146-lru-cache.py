# https://leetcode-cn.com/problems/lru-cache/

# 方法一：哈希表 + 队列（记录操作次数）
class LRUCache1:

    def __init__(self, capacity: int):
        self.nums_dict = {}  # key：[val, 操作次数]
        self.cnt = 0  # 操作次数
        self.capacity = capacity
        self.freq = []  # 长度为capacity的队列，记录操作次数

    def get(self, key: int) -> int:
        if key not in self.nums_dict:
            return - 1
        else:
            val, time = self.nums_dict[key][0], self.nums_dict[key][1]
            if time in self.freq:
                # 若当前val的操作次数在freq中，则更新次数以及队列中的记录
                self.cnt += 1
                self.freq.remove(time)
                self.freq.append(self.cnt)
                self.nums_dict[key] = [val, self.cnt]
                return val
            else:
                return -1

    def put(self, key: int, value: int) -> None:
        self.cnt += 1
        # 如果存在，则需要先把之前的操作记录删除，然后添加这次的操作记录
        if key in self.nums_dict and self.nums_dict[key][1] in self.freq:
            self.freq.remove(self.nums_dict[key][1])
        self.freq.append(self.cnt)
        # 判断以下是否超过容量，超过的话就出队
        if len(self.freq) > self.capacity:
            self.freq.pop(0)
        self.nums_dict[key] = [value, self.cnt]


# 方法二： 哈希表 + 双向链表
# 时间复杂度：对于 put 和 get 都是 O(1)O(1)。
# 空间复杂度：O(capacity)，因为哈希表和双向链表最多存储 capacity+1 个元素。
# 必须用双向链表，当删除最后一个元素是，双向链表只需要O（1）的时间，而单向链表需要O（N）

class BiLink():
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = BiLink()  # 创建虚拟头尾节点
        self.tail = BiLink()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return - 1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        else:
            node = self.cache[key]
            self.move_to_head(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = BiLink(key, value)
            # 如果 key 不存在，创建一个新的节点
            self.cache[key] = node
            # 添加至双向链表的头部
            self.insert(node)
            # 如果超出容量，删除双向链表的尾部节点，# 删除哈希表中对应的项
            if len(self.cache) > self.capacity:
                remove_node = self.delect_tail()
                self.cache.pop(remove_node.key)
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)

    def delectNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # 注意顺序，先更新node，再把node赋值给head.next
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node):
        self.delectNode(node)
        self.insert(node)

    def delect_tail(self):
        node = self.tail.prev
        self.delectNode(node)
        return node


lRUCache = LRUCache(2)
print(lRUCache.get(2))
lRUCache.put(2, 6)
print(lRUCache.get(1))
lRUCache.put(1, 5)
lRUCache.put(1, 2)
print(lRUCache.get(1))
print(lRUCache.get(2))


# https: // leetcode.com/problems/number-of-orders-in-the-backlog/
import heapq


class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        max_heap, min_heap = [], []  # 创建最大堆和最小堆
        for order in orders:
            price, amount, typ = order[0], order[1], order[2]
            if typ == 0:
                remove_cnt = 0  # 记录需要移除的个数
                while (min_heap != [] and min_heap[0][0] <= price):
                    top = min_heap[0]
                    # 如果最小堆的第一个元素的数量buy的小，那么将其pop掉，更新amout
                    if top[1] <= amount:
                        heapq.heappop(min_heap)
                        remove_cnt += top[1]
                        amount -= top[1]
                    # 否则更新数量
                    else:
                        heapq.heapreplace(min_heap, [top[0], top[1] - amount])
                        remove_cnt += amount
                        break
                # 若剩余数量不为0，push到max_heap
                if remove_cnt != order[1]:
                    heapq.heappush(max_heap, [-price, order[1] - remove_cnt])
            else:
                remove_cnt = 0
                while (max_heap != [] and -max_heap[0][0] >= price):
                    top = max_heap[0]
                    if top[1] <= amount:
                        heapq.heappop(max_heap)
                        remove_cnt += top[1]
                        amount -= top[1]
                    else:
                        heapq.heapreplace(max_heap, [top[0], top[1] - amount])
                        remove_cnt += amount
                        break
                if remove_cnt != order[1]:
                    heapq.heappush(min_heap, [price, order[1] - remove_cnt])
        res = sum([i[1] for i in max_heap + min_heap])
        return int(res % (1e9 + 7))


S = Solution()
#orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
print(S.getNumberOfBacklogOrders(orders))

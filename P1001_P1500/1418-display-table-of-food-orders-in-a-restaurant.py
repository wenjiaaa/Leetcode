"""
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.


"""

import collections
import numpy as np


class Solution1:
    def displayTable(self, orders):
        orders = np.array(orders)
        foods = sorted(list(set(orders[:, 2])))
        tables = sorted(set(orders[:, 1]), key=int)
        res = [['0'] * (len(foods) + 1)] * (len(tables) + 1)
        res[0] = ['Table'] + foods
        for i in range(len(orders)):
            table = orders[i, 1]
            food = orders[i, 2]
            table_idx = tables.index(table) + 1
            food_idx = foods.index(food) + 1
            order_line = res[table_idx].copy()
            order_line[0] = table
            order_line[food_idx] = str(int(order_line[food_idx]) + 1)
            res[table_idx] = order_line
        return res


# 参考讨论区，用字典
class Solution:
    def displayTable(self, orders):
        d = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        ts, fs = set(), set()
        for _, table, food in orders:
            d[table][food] += 1
            ts.add(table)
            fs.add(food)
        ts, fs = sorted(ts, key=int), sorted(fs)
        res = [['Table']+fs]
        for i in ts:
            res.append([i]+[str(d[i][j]) for j in fs])
        return res


S = Solution()
orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], [
    "Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
print(S.displayTable(orders))

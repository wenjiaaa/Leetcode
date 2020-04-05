"""
https://leetcode.com/problems/longest-happy-string/

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

思路：每次找剩余个数最多的那个字母往里加，如果加的过程中发现有3个连续的了，那就加次数第二多的字母
可以用最大堆来维护字母的剩余次数，或者直接用列表
参考：https://leetcode.com/problems/longest-happy-string/discuss/564248/Python-HEAP-solution-with-explaination
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == 0 and b == 0 and c == 0:
            return ""
        max_heap = []
        if a != 0:
            max_heap.append((a, "a"))
        if b != 0:
            max_heap.append((b, "b"))
        if c != 0:
            max_heap.append((c, "c"))
        res = ""
        while max_heap:
            max_heap = sorted(max_heap, key=lambda x: x[0], reverse=True)
            first, letter1 = max_heap[0]  # 先考虑加剩余次数最多的字母
            max_heap.pop(0)
            if len(res) >= 2 and letter1 == res[-1] == res[-2]:
                if not max_heap:
                    return res
                # 加剩余最多的字母出现3个字母连续，那么就加剩余次数第二多的字母
                second, letter2 = max_heap[0]
                max_heap.pop(0)
                res += letter2
                second -= 1
                if second != 0:
                    max_heap.append((second, letter2))
                max_heap.append((first, letter1))
                continue
            res += letter1
            first -= 1
            if first != 0:
                max_heap.append((first, letter1))
        return res


S = Solution()
a = 1
b = 1
c = 7
print(S.longestDiverseString(a, b, c))

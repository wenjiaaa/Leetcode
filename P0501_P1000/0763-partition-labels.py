# https://leetcode.com/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {}  # 存储每个元素最后出现的位置
        for i in range(len(S)):
            last[S[i]] = i
        res = []
        i, j = 0, 0
        max_last = last[S[i]]
        max_j = last[S[j]]
        while (i < len(S) and j < len(S)):
            # 如果j判断到了右边界，或者当前的边界就是本身（即单个的情况），那么就添加到res
            if j == max_last or i == max_last:
                res.append(max_last - i + 1)
                # 进入下一组的判断
                i = max_last + 1
                j = i
                if i < len(S) and j < len(S):
                    max_last = last[S[i]]
                    max_j = last[S[j]]
                else:
                    break
                # 单个元素的情况，例如：abceeee
                if i == max_last:
                    continue
            j += 1
            if j > len(S):
                break
            # 最后一个是单个的情况，例如：ababae
            elif j == len(S):
                res.append(1)
            max_j = last[S[j]]
            # 如果j的右边界比当前的边界大，则更新右边界为max_j
            if max_j > max_last:
                max_last = max_j
        return res


S = Solution()
#s = "vhaagbqkaq"
s = "eababcbacad"
print(S.partitionLabels(s))

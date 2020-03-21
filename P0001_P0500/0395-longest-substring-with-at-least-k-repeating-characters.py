"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
最开始想用双指针，但是不知道怎么移动，采用分治的思路

思路是这样的：
如果字符串s的长度少于k，那么一定不存在满足题意的子字符串，返回0；
如果一个字符在s中出现的次数少于k次，那么所有的包含这个字符的子字符串都不能满足题意。所以，应该去不包含这个字符的子字符串继续寻找。这就是分而治之的思路，返回不同子串的长度最大值。
如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串。
虽然代码比较简短，但这个题的思路还是挺新颖的，
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/82889933
时间复杂度： O(nlogn)
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


s = "ababbc"
k = 2
S = Solution()
print(S.longestSubstring(s, k))

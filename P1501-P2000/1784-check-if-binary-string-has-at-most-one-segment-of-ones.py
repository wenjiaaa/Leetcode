# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        idx_0, idx_1 = None, None
        for i in range(len(s)):
            if s[i] == "0":
                idx_0 = i
                break
        if idx_0 == None:
            return True
        for i in range(idx_0 + 1, len(s)):
            if s[i] == "1":
                idx_1 = i
                break
        if idx_1 == None:
            return True
        return False

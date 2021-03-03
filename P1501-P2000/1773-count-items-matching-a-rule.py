# https://leetcode.com/problems/count-items-matching-a-rule/
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rules = ["type", "color", "name"]
        rulekey_idx = rules.index(ruleKey)
        res = 0
        for item in items:
            if item[rulekey_idx] == ruleValue:
                res += 1
        return res

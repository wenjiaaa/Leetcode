# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
class Solution:
    def evaluate(self, s, knowledge):
        dic = {key: value for key, value in knowledge}
        left = right = None
        i = 0
        while i < len(s):
            if s[i] == '(':
                left = i
            elif s[i] == ')':
                right = i
            if left != None and right != None:
                key = s[left + 1:right]
                if key in dic:
                    s = s[0:left] + dic[key] + s[right + 1:]
                    i = left + len(dic[key])
                else:
                    s = s[0:left] + "?" + s[right + 1:]
                    i = left + 1
                left = right = None
            else:
                i += 1

        return s


S = Solution()
s = "(name)is(age)yearsold"
knowledge = [["name", "bob"], ["age", "two"]]
print(S.evaluate(s, knowledge))

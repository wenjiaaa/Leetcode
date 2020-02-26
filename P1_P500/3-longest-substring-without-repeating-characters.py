"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


# O(N^2)
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            if i <= len(s) - 2 and s[i] == s[i + 1]:
                continue
            used = set(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in used:
                    i = i + 1
                    break
                else:
                    used.add(s[j])
            res = max(res, len(used))

        return res


# sliding window, O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        substring = set()
        res = 0
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in substring:
                substring.add(s[j])
                j = j+1
            else:
                substring.remove(s[i])
                i = i+1
            res = max(res, len(substring))
        return res


S = Solution()
s = "pwwkew"
res = S.lengthOfLongestSubstring(s)
print(res)

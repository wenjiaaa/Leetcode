"""
https://leetcode.com/problems/sequential-digits/

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

"""


class Solution:
    def sequentialDigits(self, low: int, high: int):
        res = []
        arr = [str(i) for i in range(1, 10)]
        len1 = len(str(low))
        len2 = len(str(high))
        for win_len in range(len1, len2+2):
            for i in range(len(arr)):
                if i+win_len > len(arr):
                    break
                number = int(''.join(arr[i:i+win_len]))
                if number >= low and number <= high:
                    res.append(number)
        return res


S = Solution()
low = 1000
high = 13000
res = S.sequentialDigits(low, high)
print(res)

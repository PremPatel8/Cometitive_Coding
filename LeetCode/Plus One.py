from typing import List
"""
Problem Name: Plus One

Problem Section: Array

Problem Statement:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Resources:
"""
""" 109 / 109 test cases passed.
	Status: Accepted
Runtime: 52 ms
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() optimized solution


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))

        return [int(i) for i in str(num+1)]


myobj = Solution()
# inpt = [1, 2, 3]
inpt = [4, 3, 2, 1]
print(myobj.plusOne(inpt))

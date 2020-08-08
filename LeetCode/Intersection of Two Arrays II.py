from typing import List
"""
Problem Name: Intersection of Two Arrays II

Problem Section: Array

Problem Statement:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Resources:

"""

""" 61 / 61 test cases passed.
	Status: Accepted
Runtime: 84 ms
Memory Usage: 14.1 MB """

# Solution techniques are

# Time complexity : O() Space complexity : O() solution using


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        res = []

        smallerlist, largerlist = (
            nums1, nums2) if len1 < len2 else (nums2, nums1)

        for no in smallerlist:
            if no in largerlist:
                res.append(no)
                largerlist.remove(no)

        return res


myobj = Solution()
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
nums1 = [2, 1]
nums2 = [1, 2]
print(myobj.intersect(nums1, nums2))

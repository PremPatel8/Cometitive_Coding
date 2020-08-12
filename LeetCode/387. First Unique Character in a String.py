from typing import List
from collections import Counter, OrderedDict

"""
Problem Name: 387. First Unique Character in a String

Problem Section: HashTable, String

Problem Statement:
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.

Resources:
https://stackoverflow.com/questions/23747564/how-to-get-count-dict-of-items-but-maintain-the-order-in-which-they-appear
https://docs.python.org/3.3/library/collections.html#ordereddict-examples-and-recipes
"""

""" 
104 / 104 test cases passed.
	Status: Accepted
Runtime: 92 ms
Memory Usage: 13.9 MB
 """

""" Solution techniques are iterate through the string once to get the count of all chars and
then iterate through the string again and return the position of the first char whose count is 1
Or my solution use some kind of ordered dict data structure to keep the count of all chars and their 1st encountered positions
and then iterate through this data structure and return the position of the first char whose count is 1 """

# Time complexity : O(n) Space complexity : O(n) Using OrderedDict & Counter


class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        if len(s) == 1:
            return 0

        ordered_dict = OrderedDict()
        seen = set()

        for idx, ch in enumerate(s):
            if ch in seen:
                if ch in ordered_dict:
                    del ordered_dict[ch]
            else:
                ordered_dict[ch] = idx
                seen.add(ch)

        if len(ordered_dict):
            res = ordered_dict.popitem(last=False)
            return res[1]

        return -1


myobj = Solution()
# inpt = "loveleetcode"
inpt = "aadadaad"
print(myobj.firstUniqChar(inpt))

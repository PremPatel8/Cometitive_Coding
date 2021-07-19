"""
each num = abs(num) = rocket size, + = right, - = left

If two rockets collide, the smaller one will disappear and the larger one will continue on its course unchanged. 

If they are the same size and they collide, they'll both explode (both numbers are removed). 

If two rockets are moving in the same direction, they will never collide. 
"""

# Your code took 189 milliseconds — faster than 89.18% in Python


class Solution:
    def solve(self, nums):
        if len(nums) < 2:
            return nums

        stack = []

        for num in nums:
            if num > 0:
                stack.append(num)
            else:
                while stack and 0 < stack[-1] < abs(num):
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(num)
                elif stack[-1] == abs(num):
                    stack.pop()

        return stack


# nums = [-1, 1]
# # Op = [-1, 1]

nums = [-3, 1, -3]
# Op = [-3, -3]

myobj = Solution()
print(myobj.solve(nums))
